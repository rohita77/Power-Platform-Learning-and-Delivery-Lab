from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures/synthetic"
TEST_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PACKAGE_ROOT))

from validators.common import canonical_digest, load_json
from validators.attestation import create_attestation, validate_attestation
from validators.package import compare_adapter_contracts, validate_package
from validators.request import validate_request
from validators.result import validate_result


AS_OF = date(2026, 7, 22)


def pointer_parts(pointer: str) -> list[str]:
    if not pointer or pointer == "/":
        return []
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/")]


def resolve(document: Any, pointer: str) -> Any:
    current = document
    for part in pointer_parts(pointer):
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current


def mutate(document: Any, mutation: dict[str, Any]) -> Any:
    if mutation["op"] == "replace-document":
        return copy.deepcopy(mutation["value"])
    result = copy.deepcopy(document)
    parts = pointer_parts(mutation["path"])
    parent = result
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    final = parts[-1]
    if mutation["op"] == "set":
        if isinstance(parent, list):
            parent[int(final)] = copy.deepcopy(mutation["value"])
        else:
            parent[final] = copy.deepcopy(mutation["value"])
    elif mutation["op"] == "delete":
        if isinstance(parent, list):
            del parent[int(final)]
        else:
            del parent[final]
    elif mutation["op"] == "append-copy":
        resolve(result, mutation["path"]).append(copy.deepcopy(resolve(result, mutation["source"])))
    else:
        raise ValueError("Unsupported test mutation")
    return result


def should_trigger(prompt: str) -> bool:
    text = prompt.lower()
    blocked = ("deploy", "licensing", "current copilot", "connect to my tenant", "inspect its agents")
    positive = ("design", "requirements", "designrequest", "carry-forward")
    return any(item in text for item in positive) and not any(item in text for item in blocked)


def codes(findings: list[dict[str, str]]) -> set[str]:
    return {item["code"] for item in findings}


def findings_digest(findings: list[dict[str, str]]) -> str:
    encoded = json.dumps(
        findings, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def extract_skill_skeleton(skill_text: str) -> dict[str, Any] | None:
    match = re.search(
        r"<!-- CANONICAL-DESIGN-RESULT-SKELETON:START -->\s*"
        r"```json\s*(\{.*?\})\s*```\s*"
        r"<!-- CANONICAL-DESIGN-RESULT-SKELETON:END -->",
        skill_text,
        re.DOTALL,
    )
    if match is None:
        return None
    try:
        parsed = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def tree_hashes(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(item for item in root.rglob("*") if item.is_file() and not item.is_symlink()):
        result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def run_document_case(case: dict[str, Any]) -> tuple[bool, str]:
    base = load_json(FIXTURE_ROOT / case["base"])
    document = mutate(base, case["mutation"])
    if case["target"] == "request":
        observed = validate_request(document, AS_OF)
    else:
        observed = validate_result(document, AS_OF)
    return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))


def run_attestation_case(case: dict[str, Any]) -> tuple[bool, str]:
    request = load_json(FIXTURE_ROOT / "GOLD-001.request.json")
    document = None if case.get("missing") else load_json(FIXTURE_ROOT / case["fixture"])
    if document is not None and case.get("mutation"):
        document = mutate(document, case["mutation"])
    used = {document.get("attestation_id")} if isinstance(document, dict) and case.get("used") else set()
    observed = validate_attestation(document, request, AS_OF, used)
    expected = case.get("expected_code")
    if expected is None:
        generated = create_attestation(request, document["attestation_id"])
        return not observed and generated == document, ",".join(sorted(codes(observed)))
    return expected in codes(observed), ",".join(sorted(codes(observed)))


def run_result_invariant_case(case: dict[str, Any]) -> tuple[bool, str]:
    request = load_json(FIXTURE_ROOT / case["request"])
    result = mutate(load_json(FIXTURE_ROOT / case["base"]), case["mutation"])
    attestation = create_attestation(request, f"ATT-{case['id']}")
    observed = validate_result(result, AS_OF, request, attestation)
    observed_codes = codes(observed)
    if case.get("expected_valid"):
        return not observed, ",".join(sorted(observed_codes))
    expected_codes = set(case["expected_codes"])
    return expected_codes.issubset(observed_codes), ",".join(sorted(observed_codes))


def run_generation_shape_case(
    case: dict[str, Any], contract: dict[str, Any], skill_skeleton: dict[str, Any] | None
) -> tuple[bool, str]:
    fixture_path = TEST_ROOT / case["fixture"]
    document = load_json(fixture_path)
    request = load_json(FIXTURE_ROOT / case["request"])
    attestation = create_attestation(request, f"ATT-{case['id']}")
    observed = validate_result(document, AS_OF, request, attestation)
    observed_codes = codes(observed)
    root_properties = set(contract["exact_root_properties"])
    exact_modes = contract["exact_modes"]
    kind = case["kind"]

    if kind in {"valid", "skeleton-valid"}:
        mode_names = [item.get("mode") for item in document.get("modes", [])]
        passed = not observed and set(document) == root_properties and mode_names == exact_modes
        if kind == "skeleton-valid":
            request_findings = validate_request(request, AS_OF)
            passed = passed and not request_findings and document == skill_skeleton
    elif kind == "prohibited-root":
        extras = sorted(set(document) - root_properties)
        passed = (
            extras == case["expected_extra_root_properties"]
            and set(case["expected_codes"]).issubset(observed_codes)
        )
    elif kind == "invalid-modes":
        mode_names = [item.get("mode") for item in document.get("modes", [])]
        passed = (
            mode_names == case["expected_mode_names"]
            and mode_names != exact_modes
            and set(case["expected_codes"]).issubset(observed_codes)
        )
    elif kind in {"rc2-work-output", "rc3-work-output"}:
        raw_sha256 = hashlib.sha256(fixture_path.read_bytes()).hexdigest()
        missing = sorted(root_properties - set(document))
        prohibited = sorted(set(document) & set(contract["prohibited_root_properties"]))
        nested_mode_items = (
            document.get("design", {}).get("agent", {}).get("lifecycle_modes", [])
            if isinstance(document.get("design"), dict)
            else []
        )
        nested_modes = [
            item.get("name") for item in nested_mode_items if isinstance(item, dict)
        ]
        shared_checks = (
            raw_sha256 == case["sha256"],
            len(observed) == case["expected_findings_count"],
            findings_digest(observed) == case["expected_findings_sha256"],
            set(case["expected_codes"]) == observed_codes,
        )
        if kind == "rc2-work-output":
            incompatible_shapes = all(
                any(item["path"].startswith(prefix) for item in observed)
                for prefix in case["expected_incompatible_path_prefixes"]
            )
            passed = all(
                shared_checks
                + (
                    missing == case["expected_missing_root_properties"],
                    prohibited == case["expected_prohibited_root_properties"],
                    nested_modes == case["expected_nested_mode_names"],
                    incompatible_shapes,
                )
            )
        else:
            code_counts = {
                code: sum(1 for item in observed if item["code"] == code)
                for code in observed_codes
            }
            canonical_modes = [
                item.get("mode") for item in document.get("modes", [])
                if isinstance(item, dict)
            ]
            alternative_modes = [
                item.get("name") for item in document.get("modes", [])
                if isinstance(item, dict)
            ]
            passed = all(
                shared_checks
                + (
                    set(document) == root_properties,
                    not prohibited,
                    code_counts == case["expected_code_counts"],
                    canonical_modes == case["expected_canonical_mode_names"],
                    alternative_modes == case["expected_alternative_mode_names"],
                )
            )
    else:
        raise ValueError("Unsupported generation-shape case")
    return passed, ",".join(sorted(observed_codes))


def run_focused_generation_case(
    case: dict[str, Any], focused: dict[str, Any]
) -> tuple[bool, str]:
    request = load_json(FIXTURE_ROOT / focused["request"])
    document = mutate(load_json(FIXTURE_ROOT / focused["base"]), case["mutation"])
    attestation = create_attestation(request, f"ATT-{case['id']}")
    observed = validate_result(document, AS_OF, request, attestation)
    observed_pairs = sorted(
        ({"path": item["path"], "code": item["code"]} for item in observed),
        key=lambda item: (item["path"], item["code"]),
    )
    expected_pairs = sorted(
        case["expected_path_code_pairs"],
        key=lambda item: (item["path"], item["code"]),
    )
    return observed_pairs == expected_pairs, ",".join(
        f"{item['path']}:{item['code']}" for item in observed_pairs
    )


def run_regression_case(case: dict[str, Any]) -> tuple[bool, str]:
    if case["kind"] == "document":
        return run_document_case(case)
    if case["kind"] == "adapter":
        codex = load_json(PACKAGE_ROOT / "adapters/codex.contract.json")
        work = load_json(PACKAGE_ROOT / "adapters/chatgpt-work.contract.json")
        work = mutate(work, case["mutation"])
        observed = compare_adapter_contracts([codex, work])
        return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))
    if case["kind"] == "adapter-both":
        codex = load_json(PACKAGE_ROOT / "adapters/codex.contract.json")
        work = load_json(PACKAGE_ROOT / "adapters/chatgpt-work.contract.json")
        codex["network_allowed"] = True
        work["network_allowed"] = True
        observed = compare_adapter_contracts([codex, work])
        return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))
    if case["kind"] == "work-smoke-003":
        request = load_json(FIXTURE_ROOT / case["request"])
        result = load_json(FIXTURE_ROOT / case["result"])
        attestation = create_attestation(request, f"ATT-{case['id']}")
        observed = validate_result(result, AS_OF, request, attestation)
        observed_codes = codes(observed)
        return set(case["expected_codes"]).issubset(observed_codes), ",".join(sorted(observed_codes))
    request = load_json(FIXTURE_ROOT / case["request"])
    result = load_json(FIXTURE_ROOT / case["result"])
    attestation = create_attestation(request, f"ATT-{case['id']}")
    if case["kind"] == "missing-attestation":
        observed = validate_result(result, AS_OF, request, None)
        return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))
    if case["kind"] == "attested-result":
        result = mutate(result, case["mutation"])
        observed = validate_result(result, AS_OF, request, attestation)
        return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))
    if case["kind"] == "forged-reset":
        result["carry_forward"]["sequence"] = 0
        result["carry_forward"]["previous_result_id"] = None
        result["carry_forward"]["request_ids"] = [result["request_id"]]
        result["carry_forward"]["result_ids"] = [result["result_id"]]
        observed = validate_result(result, AS_OF, request, attestation)
        return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))
    if case["kind"] == "accepted-stale":
        result["provenance"][0]["status"] = "expired"
        result["provenance"][0]["revalidate_on"] = "2026-01-01"
        result["abstentions"][0]["reason"] = "stale-evidence"
        observed = validate_result(result, AS_OF, request, attestation)
        return not observed, ",".join(sorted(codes(observed)))
    if case.get("prepare") == "add-superseded":
        item = {"id": "SUP-001", "statement": "Prior synthetic design was superseded.", "evidence_refs": ["PRV-001"]}
        request["carry_forward"]["superseded_chronology"].append(copy.deepcopy(item))
        result["carry_forward"]["superseded_chronology"].append(copy.deepcopy(item))
    elif case.get("prepare") == "add-prior-failure":
        item = {"id": "OPN-FAIL", "statement": "Prior schema failure remains unresolved.", "evidence_refs": ["PRV-001"]}
        request["carry_forward"]["open_items"].append(copy.deepcopy(item))
        result["carry_forward"]["open_items"].append(copy.deepcopy(item))
    result = mutate(result, case["mutation"])
    result["request_digest"] = canonical_digest(request)
    attestation = create_attestation(request, f"ATT-{case['id']}")
    observed = validate_result(result, AS_OF, request, attestation)
    return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))


def main() -> int:
    failures: list[dict[str, str]] = []
    counts: dict[str, int] = {}

    trigger_cases = load_json(Path(__file__).with_name("trigger-cases.json"))
    counts["trigger"] = len(trigger_cases)
    counts["should_trigger"] = sum(1 for item in trigger_cases if item["should_trigger"])
    counts["should_not_trigger"] = len(trigger_cases) - counts["should_trigger"]
    if counts["should_trigger"] < 3 or counts["should_not_trigger"] < 3:
        failures.append({"id": "TRIGGER-MINIMUM", "observed": "minimum not met"})
    for case in trigger_cases:
        if should_trigger(case["prompt"]) != case["should_trigger"]:
            failures.append({"id": case["id"], "observed": "trigger mismatch"})
    generation_contract = load_json(Path(__file__).with_name("generation-shape-cases.json"))
    skill_text = (PACKAGE_ROOT / "SKILL.md").read_text(encoding="utf-8")
    skill_skeleton = extract_skill_skeleton(skill_text)
    frontmatter = skill_text.split("---", 2)[1].lower()
    required_trigger_terms = ("public or synthetic", "offline", "requirements discovery", "tenant", "toolkit", "connector", "mcp", "deploy")
    counts["trigger_metadata_assertions"] = len(required_trigger_terms)
    missing_terms = [term for term in required_trigger_terms if term not in frontmatter]
    if missing_terms:
        failures.append({"id": "TRIGGER-METADATA", "observed": "missing trigger boundary terms"})
    model_visible_terms = set(
        generation_contract["exact_root_properties"]
        + generation_contract["prohibited_root_properties"]
        + generation_contract["exact_modes"]
        + generation_contract["model_visible_nested_properties"]
    )
    counts["model_visible_contract_terms"] = len(model_visible_terms)
    missing_contract_terms = sorted(term for term in model_visible_terms if term not in skill_text)
    if missing_contract_terms:
        failures.append({"id": "GENERATION-CONTRACT-VISIBILITY", "observed": "missing model-visible contract terms"})
    required_phrases = generation_contract["schema_first_directives"] + generation_contract["nested_contract_phrases"]
    counts["schema_first_visibility_assertions"] = len(required_phrases)
    missing_phrases = [phrase for phrase in required_phrases if phrase not in skill_text]
    if missing_phrases:
        failures.append({"id": "SCHEMA-FIRST-CONTRACT-VISIBILITY", "observed": "missing schema-first contract phrases"})
    counts["embedded_skeleton"] = 1
    if skill_skeleton is None:
        failures.append({"id": "EMBEDDED-SKELETON", "observed": "model-visible skeleton is missing or invalid JSON"})

    golden_cases = load_json(Path(__file__).with_name("golden-cases.json"))
    counts["golden"] = len(golden_cases)
    counts["valid_fixture_documents"] = len(golden_cases) * 2
    if len(golden_cases) < 5:
        failures.append({"id": "GOLDEN-MINIMUM", "observed": "minimum not met"})
    for case in golden_cases:
        request = load_json(Path(__file__).parent / case["request"])
        result = load_json(Path(__file__).parent / case["result"])
        attestation = create_attestation(request, f"ATT-{case['id']}")
        observed = validate_request(request, AS_OF)
        observed.extend(validate_attestation(attestation, request, AS_OF))
        observed.extend(validate_result(result, AS_OF, request, attestation))
        if observed:
            failures.append({"id": case["id"], "observed": ",".join(sorted(codes(observed)))})

    attestation_cases = load_json(Path(__file__).with_name("attestation-cases.json"))
    counts["attestation"] = len(attestation_cases)
    counts["valid_attestation"] = sum(1 for item in attestation_cases if item.get("expected_code") is None)
    counts["invalid_attestation"] = len(attestation_cases) - counts["valid_attestation"]
    for case in attestation_cases:
        passed, observed = run_attestation_case(case)
        if not passed:
            failures.append({"id": case["id"], "observed": observed or "attestation expectation not met"})

    for category in ("negative", "security"):
        cases = load_json(Path(__file__).with_name(f"{category}-cases.json"))
        counts[category] = len(cases)
        for case in cases:
            passed, observed = run_document_case(case)
            if not passed:
                failures.append({"id": case["id"], "observed": observed or "accepted invalid fixture"})

    invariant_cases = load_json(Path(__file__).with_name("result-invariant-cases.json"))
    counts["result_invariants"] = len(invariant_cases)
    counts["valid_result_invariants"] = sum(1 for item in invariant_cases if item.get("expected_valid"))
    counts["invalid_result_invariants"] = len(invariant_cases) - counts["valid_result_invariants"]
    for case in invariant_cases:
        passed, observed = run_result_invariant_case(case)
        if not passed:
            failures.append({"id": case["id"], "observed": observed or "result invariant expectation not met"})

    generation_cases = generation_contract["cases"]
    counts["generation_shapes"] = len(generation_cases)
    counts["valid_generation_shapes"] = sum(
        1 for item in generation_cases if item["kind"] in {"valid", "skeleton-valid"}
    )
    counts["invalid_generation_shapes"] = len(generation_cases) - counts["valid_generation_shapes"]
    for case in generation_cases:
        passed, observed = run_generation_shape_case(case, generation_contract, skill_skeleton)
        if not passed:
            failures.append({"id": case["id"], "observed": observed or "generation-shape expectation not met"})

    focused_generation = load_json(TEST_ROOT / generation_contract["focused_fixture"])
    focused_cases = focused_generation["cases"]
    counts["focused_generation_contracts"] = len(focused_cases)
    for case in focused_cases:
        passed, observed = run_focused_generation_case(case, focused_generation)
        if not passed:
            failures.append({"id": case["id"], "observed": observed or "focused generation expectation not met"})

    regression_cases = load_json(Path(__file__).with_name("regression-cases.json"))
    counts["regression"] = len(regression_cases)
    for case in regression_cases:
        passed, observed = run_regression_case(case)
        if not passed:
            failures.append({"id": case["id"], "observed": observed or "regression not detected"})

    counts["invalid_fixture_cases"] = (
        counts["negative"]
        + counts["security"]
        + counts["regression"]
        + counts["invalid_attestation"]
        + counts["invalid_result_invariants"]
        + counts["invalid_generation_shapes"]
        + counts["focused_generation_contracts"]
    )

    package_findings = validate_package(PACKAGE_ROOT)
    counts["package_findings"] = len(package_findings)
    if package_findings:
        failures.append({"id": "PACKAGE", "observed": ",".join(sorted(codes(package_findings)))})

    rollback = load_json(Path(__file__).with_name("rollback-case.json"))
    before = tree_hashes(PACKAGE_ROOT)
    missing = [item for item in rollback["expected_files"] if not (PACKAGE_ROOT / item).is_file()]
    after = tree_hashes(PACKAGE_ROOT)
    counts["rollback"] = 1
    if missing or not rollback.get("must_not_mutate") or before != after:
        failures.append({"id": rollback["id"], "observed": "rollback dry-run failed"})

    payload = {
        "suite_version": "0.2.0-rc4",
        "as_of": AS_OF.isoformat(),
        "offline": True,
        "passed": not failures,
        "counts": counts,
        "failures": failures,
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
