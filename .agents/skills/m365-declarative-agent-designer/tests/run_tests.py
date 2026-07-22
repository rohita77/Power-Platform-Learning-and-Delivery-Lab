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
sys.path.insert(0, str(PACKAGE_ROOT))

from validators.common import canonical_digest, load_json
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
    request = load_json(FIXTURE_ROOT / case["request"])
    result = load_json(FIXTURE_ROOT / case["result"])
    if case["kind"] == "forged-reset":
        result["carry_forward"]["sequence"] = 0
        result["carry_forward"]["previous_result_id"] = None
        result["carry_forward"]["request_ids"] = [result["request_id"]]
        result["carry_forward"]["result_ids"] = [result["result_id"]]
        observed = validate_result(result, AS_OF, request)
        return case["expected_code"] in codes(observed), ",".join(sorted(codes(observed)))
    if case["kind"] == "accepted-stale":
        result["provenance"][0]["status"] = "expired"
        result["provenance"][0]["revalidate_on"] = "2026-01-01"
        result["abstentions"][0]["reason"] = "stale-evidence"
        observed = validate_result(result, AS_OF, request)
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
    observed = validate_result(result, AS_OF, request)
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
    skill_text = (PACKAGE_ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = skill_text.split("---", 2)[1].lower()
    required_trigger_terms = ("public or synthetic", "offline", "requirements discovery", "tenant", "toolkit", "connector", "mcp", "deploy")
    counts["trigger_metadata_assertions"] = len(required_trigger_terms)
    missing_terms = [term for term in required_trigger_terms if term not in frontmatter]
    if missing_terms:
        failures.append({"id": "TRIGGER-METADATA", "observed": "missing trigger boundary terms"})

    golden_cases = load_json(Path(__file__).with_name("golden-cases.json"))
    counts["golden"] = len(golden_cases)
    counts["valid_fixture_documents"] = len(golden_cases) * 2
    if len(golden_cases) < 5:
        failures.append({"id": "GOLDEN-MINIMUM", "observed": "minimum not met"})
    for case in golden_cases:
        request = load_json(Path(__file__).parent / case["request"])
        result = load_json(Path(__file__).parent / case["result"])
        observed = validate_request(request, AS_OF)
        observed.extend(validate_result(result, AS_OF, request))
        if observed:
            failures.append({"id": case["id"], "observed": ",".join(sorted(codes(observed)))})

    for category in ("negative", "security"):
        cases = load_json(Path(__file__).with_name(f"{category}-cases.json"))
        counts[category] = len(cases)
        for case in cases:
            passed, observed = run_document_case(case)
            if not passed:
                failures.append({"id": case["id"], "observed": observed or "accepted invalid fixture"})

    regression_cases = load_json(Path(__file__).with_name("regression-cases.json"))
    counts["regression"] = len(regression_cases)
    for case in regression_cases:
        passed, observed = run_regression_case(case)
        if not passed:
            failures.append({"id": case["id"], "observed": observed or "regression not detected"})

    counts["invalid_fixture_cases"] = counts["negative"] + counts["security"] + counts["regression"]

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
        "suite_version": "0.1.0",
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
