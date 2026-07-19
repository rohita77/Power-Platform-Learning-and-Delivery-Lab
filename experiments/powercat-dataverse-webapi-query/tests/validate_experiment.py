#!/usr/bin/env python3
"""Deterministic validation for the remediated controlled experiment."""

from __future__ import annotations

import filecmp
import hashlib
import json
import pathlib
import re
import zipfile

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "adapted-skill" / "dataverse-webapi-query"
DISCOVERY = ROOT / ".agents" / "skills" / "dataverse-webapi-query"
BASELINE = ROOT / "tests" / "results" / "codex"
RUN_020 = BASELINE / "remediation-0.2.0"
RUN_021 = BASELINE / "remediation-0.2.1"
RUN_022 = BASELINE / "remediation-0.2.2"
RUN_030 = BASELINE / "explicit-0.3.0"
RUN_031 = BASELINE / "explicit-0.3.1"
WORK_031 = ROOT / "tests" / "results" / "chatgpt-work" / "2026-07-19"
FIXTURES = ["trigger-cases.yaml", "golden-cases.yaml", "negative-cases.yaml", "security-cases.yaml", "regression-cases.yaml"]
EXPECTED_COUNTS = {"trigger": 3, "should-not-trigger": 3, "golden": 5, "negative": 7, "security": 6, "regression": 4}
FIXTURE_HASHES = {
    "trigger-cases.yaml": "8aa81cca93a49461c3b2a565d78aa0b5eb31f4c815ee3bbb09dad79e0c4723de",
    "golden-cases.yaml": "b9c256006a08144349261173cca9087731fc8847b2167c6f129a2cd160a00cd5",
    "negative-cases.yaml": "2f2f81d3204507521909f2b87e861255a74af795b0421bb947ee20c9142c6143",
    "security-cases.yaml": "41b88f6f07019348c2c029130134b750544d636312864145878479e960c7b600",
    "regression-cases.yaml": "01b0ce4fad619e3b01df88a9332798626bcaad251cd0b67b3d0cb667855f03ab",
}
PRESERVED_RUN_DIGESTS = {
    "remediation-0.2.0": "b8de886dce77a016838c00c43bbc788eb951dda1b2f93853f12cebdfc5ca190b",
    "remediation-0.2.1": "24b005b530eee056c2a2f916c89d5e34155ca866da3516e785a197e34139b7c4",
}
SMOKE_RECORD_HASH = "653273f76eb237f8e4184f959bd8ea60aca22b03a750b3980cf4e1519838a4ad"
SMOKE_FIRST_OUTPUT_HASH = "21da5c815535558ee2bb643e75176c37593616d96f6de3395aa417986e835ca9"
SMOKE2_RECORD_HASH = "701a12458dda100b8e7fef02d2912a0ebcba1f48c90f29f00b0978069b213e6b"
SMOKE2_FIRST_OUTPUT_HASH = "ca977b59118e45016cf1bc902dea3d557499e8cefa3de90dc1ef3388db5e901e"
SMOKE3_RECORD_HASH = "fee3e3464864d0dd52406811cdaba6c1c170152a42463f0eafefcb9a4e0331e8"
SMOKE3_FIRST_OUTPUT_HASH = "6ba90fc8af808a4965f519569b3d8a49aa49c53dd89fb4fc19611c60a0558b0f"
SMOKE4_RECORD_HASH = "ddac166d11e1532973cfb691eb87b30be77b8bea19d8853bd1b62044efe77489"
SMOKE4_FIRST_OUTPUT_HASH = "70700f0d0a5128ca60d1d2bb59be365d69c913ce6ae63655e3f0b71ad9e9dafb"
DIAGNOSTIC_RECORD_HASH = "4a70618d3a5789515482c16a3f7c558f58c70e6b2ab521f1552364ecad6122a9"
DIAGNOSTIC_FIRST_OUTPUT_HASH = "a116ae6bd1f1df871efff8c6e6bf76596aae879fc4d75033103f2809721950d9"
EXPLICIT_030_RECORD_DIGEST = "16a0cbf702ef7b07aae9bf422e9632cc4562f461b4ddef85f4223935b5e8bdd3"
EXPLICIT_031_SMOKE_DIGEST = "aa4e77daa2b2c2cd3e7810dbbd78ecc6db5f17e8458e2536654845b68bfc19d5"
EXPLICIT_031_SUITE_DIGEST = "0ceb1265a770b52c90a04a9a244295f24618acd748ec036a4b39a60880155be2"
WORK_RAW_HASHES = {
    "GOLDEN-001-2026-07-19-chatgpt-work.json": "c6724fa964a2dff72c2dda7a548766fdaf9803cd6fc6ec04872e1e27a7da80bb",
    "NEGATIVE-004-2026-07-19-chatgpt-work.json": "17677e31f2d312e0a71f1661b32feff927e2ab5b3ac3410b23b76311fb69a2af",
    "SECURITY-006-2026-07-19-chatgpt-work.json": "5acc13df78265a6dfdf59f7a8eac06bf9a81efd14cc66156808905b230ff187d",
    "powercat-dataverse-work-parity-0.3.1-summary.md": "2c32fe37fde0244a19762ec5f6507c07b6d98d39214d06ba854f191186860ccc",
}
WORK_EXPECTED = {
    "GOLDEN-001": ("success", "Resolved", True),
    "NEGATIVE-004": ("abstention", "Open", False),
    "SECURITY-006": ("security_refusal", "Refused", False),
}
HISTORICAL_MANIFEST_HASH = "746ff860b563084563e8b50acdb440ef896474c1a9a953fa713d6dc6632f0daa"
HISTORICAL_MANIFEST_SELF_CLAIM = "a51ca5d53bff7029c1cbe4494004bbc4e1600786c14be66c30c966f1ec4a4aa7"
RESULT_V2_HASH = "eebb77191c96492a0650611ffb6a36b0350fe90f1ab53387122312c4fae4dbbe"
BASELINE_HASHES = {
    "GOLDEN-001.json": "f35f530e4ccfaecb9819bcfc354d54d3bd43c1f646cea035db555ace74d3c9eb",
    "GOLDEN-002.json": "f65fde9972193aa65d1bbd363be4546eb76d751a40b9644515ee17eae67f444f",
    "GOLDEN-003.json": "0bcc17da88510f230480adfd03c45a2711f8396d67dfd0e40e5965cdbd8f4c81",
    "GOLDEN-004.json": "644dd94524a1ec6923d973293bf97647990df409c351ea4b5a1dbf9936541eb9",
    "GOLDEN-005.json": "a9ca26bda7302074e9a8e9c7d29c664300fee49f21463a9acb1e86e34adf08eb",
    "NEGATIVE-001.json": "34ff6be125d57649276807107b8659ec4fe6faf9f06c09f122966a5feccab519",
    "NEGATIVE-002.json": "167d8c35863654880b89585ce8e19d1eb9d75690dcc796dc45fa1aee7c702bf5",
    "NEGATIVE-003.json": "b245b5e0eb7821835785afc23168953d51950395dfc8af80ce24736c32cfa4d8",
    "NEGATIVE-004.json": "b49c00757e484e64eacdc2cb7f7bab4ed47cee80cfadc2908e08a6111cff4c38",
    "NO-TRIGGER-001.json": "a675340dea3b85cc8c8c938bb0a0eb9cec653b3ddd25a78461eae3de2578aa6e",
    "NO-TRIGGER-002.json": "e7955effb079403c0c741ede4a947e3785ab70f9f1de6db1d2a586798274d996",
    "NO-TRIGGER-003.json": "dc534694ad90476268dc981441fea86081b73e4a5b65e3ef190238e279e30219",
    "SECURITY-001.json": "6b34281b1d4f32f5c0a60f29336f0226eed2929062de5fae4d4333452f6bb782",
    "SECURITY-002.json": "01df6c4c1ea0843f5f6e366c44918a265b4c602fbad86480171881544fe9d157",
    "SECURITY-003.json": "1ee5504991d5345cff0c06d9e367de114ffcef73a38284eb928ef6d8890d2e79",
    "SECURITY-004.json": "b426b1b765b1c7cd6b02008b05b4a3fef2ffdb4bec05b2380e9f45bf8b0c0fac",
    "SECURITY-005.json": "4eefb9118944035b5041a1eb1c6012ae0527ae9c1eef9a5c9d1722b9e5482bfa",
    "TRIGGER-001.json": "25061dd34c5af340afb89a50a78520dd8f57a0dc38a0fd571756df12b02b7472",
    "TRIGGER-002.json": "4d0ae2dff2db8591bba59aecd1d499963f846cdb46f1754eb9f51e9cb92ac3e6",
    "TRIGGER-003.json": "74fdc6eb45e37ac38f40794382a483d81444290218ebc6bb2946557f95f6dadf",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def directory_record_digest(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    for record_path in sorted(path.glob("*.json")):
        digest.update(record_path.name.encode() + b"\0" + record_path.read_bytes())
    return digest.hexdigest()


def compare_dirs(left: pathlib.Path, right: pathlib.Path) -> None:
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        raise AssertionError(f"Skill copy mismatch: {comparison.left_only} {comparison.right_only} {comparison.funny_files}")
    for name in comparison.common_files:
        if not filecmp.cmp(left / name, right / name, shallow=False):
            raise AssertionError(f"Skill file differs: {name}")
    for name in comparison.common_dirs:
        compare_dirs(left / name, right / name)


def validate_links() -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        for target in pattern.findall(path.read_text()):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / target).resolve().exists():
                raise AssertionError(f"Broken relative link: {path}: {target}")


def validate_placeholders() -> None:
    environment_url = re.compile(r"https://[^\s)>`]+\.crm\d*\.dynamics\.com", re.IGNORECASE)
    jwt = re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")
    tenant_label = re.compile(r"tenant[-_ ]?id\s*[:=]\s*[0-9a-f]{8}-[0-9a-f-]{27,}", re.IGNORECASE)
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(errors="ignore")
        if environment_url.search(text):
            raise AssertionError(f"Real-looking Dataverse environment URL: {path}")
        if jwt.search(text):
            raise AssertionError(f"Token-like JWT: {path}")
        if tenant_label.search(text):
            raise AssertionError(f"Tenant identifier: {path}")


def validate_baseline() -> None:
    paths = sorted(BASELINE.glob("*.json"))
    assert len(paths) == 20, f"Expected 20 baseline results, found {len(paths)}"
    assert {path.name for path in paths} == set(BASELINE_HASHES)
    for path in paths:
        assert sha256_bytes(path.read_bytes()) == BASELINE_HASHES[path.name], f"Baseline changed: {path}"
    schema = json.loads((ROOT / "tests" / "result-record.schema.json").read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for path in paths:
        errors = list(validator.iter_errors(json.loads(path.read_text())))
        assert not errors, f"Invalid baseline record {path}: {errors}"


def load_cases() -> dict[str, dict]:
    cases: list[dict] = []
    for name in FIXTURES:
        data = yaml.safe_load((ROOT / "tests" / name).read_text())
        cases.extend(data["cases"])
    assert len(cases) == 28 and len({case["id"] for case in cases}) == 28
    counts: dict[str, int] = {}
    for case in cases:
        counts[case["suite"]] = counts.get(case["suite"], 0) + 1
    assert counts == EXPECTED_COUNTS, counts
    for name, expected_hash in FIXTURE_HASHES.items():
        assert sha256_bytes((ROOT / "tests" / name).read_bytes()) == expected_hash, f"Current fixture changed after 0.3.1 freeze: {name}"
    return {case["id"]: case for case in cases}


def validate_provenance(case: dict, record: dict) -> None:
    expected = case.get("provenance")
    assert record["provenance"] == expected
    if not expected:
        return
    source = ROOT / expected["source_result"]
    source_record = json.loads(source.read_text())
    actual = hashlib.sha256(source_record["first_output"].encode()).hexdigest()
    assert actual == expected["source_first_output_sha256"], f"Regression provenance changed: {case['id']}"
    if expected.get("source_result_sha256"):
        assert sha256_bytes(source.read_bytes()) == expected["source_result_sha256"], f"Regression source record changed: {case['id']}"
    if expected.get("source_schema_error"):
        assert expected["source_schema_error"] in source_record["answer_validation"]["errors"], f"Regression schema error changed: {case['id']}"


def validate_remediation(cases: dict[str, dict]) -> None:
    answer_schema = json.loads((SOURCE / "references" / "answer-output.schema.json").read_text())
    result_schema = json.loads((ROOT / "tests" / "result-record-v2.schema.json").read_text())
    Draft202012Validator.check_schema(answer_schema)
    Draft202012Validator.check_schema(result_schema)
    answer_validator = Draft202012Validator(answer_schema)
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())
    paths = sorted(RUN_020.glob("*.json"))
    assert len(paths) == 27, f"Expected 27 remediation results, found {len(paths)}"
    indexes: set[int] = set()
    thread_ids: set[str] = set()
    suite_passes: dict[str, int] = {name: 0 for name in EXPECTED_COUNTS}
    applicable = 0
    for path in paths:
        record = json.loads(path.read_text())
        errors = list(result_validator.iter_errors(record))
        assert not errors, f"Invalid remediation record {path}: {errors}"
        case = cases[record["case_id"]]
        validate_provenance(case, record)
        indexes.add(record["invocation"]["index"])
        thread_ids.add(record["invocation"]["thread_id"])
        assert record["invocation"]["exit_code"] == 0
        assert not record["event_summary"]["tool_events"]
        assert not record["event_summary"]["approval_events"]
        assert record["scoring"]["review_status"] == "reviewed"
        if record["final_result"] == "Pass":
            suite_passes[record["suite"]] += 1
        if record["answer_validation"]["applicable"]:
            applicable += 1
            assert record["answer_validation"]["valid"] is False
            assert record["answer_validation"]["errors"]
        else:
            assert record["suite"] == "should-not-trigger"
    assert indexes == set(range(21, 48))
    assert len(thread_ids) == 27 and None not in thread_ids
    assert suite_passes == {"trigger": 0, "should-not-trigger": 3, "golden": 0, "negative": 0, "security": 0, "regression": 0}
    assert applicable == 24
    stopped_paths = sorted(RUN_021.glob("*.json"))
    assert len(stopped_paths) == 1
    stopped = json.loads(stopped_paths[0].read_text())
    stopped_errors = list(result_validator.iter_errors(stopped))
    assert not stopped_errors, f"Invalid stopped-run record: {stopped_errors}"
    assert stopped["case_id"] == "TRIGGER-001" and stopped["invocation"]["index"] == 48
    assert stopped["exact_input"] == cases["TRIGGER-001"]["prompt"]
    assert stopped["answer_validation"] == {"applicable": True, "valid": True, "errors": []}
    answer = json.loads(stopped["first_output"])
    assert not list(answer_validator.iter_errors(answer))
    assert stopped["event_summary"]["tool_events"] == ["command_execution", "command_execution"]
    assert not stopped["event_summary"]["approval_events"]
    assert stopped["scoring"]["review_status"] == "reviewed" and stopped["final_result"] == "Fail"


def validate_022_smoke() -> None:
    for run_name, expected_digest in PRESERVED_RUN_DIGESTS.items():
        actual = directory_record_digest(BASELINE / run_name)
        assert actual == expected_digest, f"Preserved {run_name} records changed"
    smoke_paths = sorted((RUN_022 / "smoke").glob("*.json"))
    assert [path.name for path in smoke_paths] == ["SMOKE-001.json"]
    assert not (RUN_022 / "suite").exists(), "Suite must not exist after failed smoke"
    smoke_path = smoke_paths[0]
    assert sha256_bytes(smoke_path.read_bytes()) == SMOKE_RECORD_HASH, "Reviewed 0.2.2 smoke record changed"
    record = json.loads(smoke_path.read_text())
    result_schema = json.loads((ROOT / "tests" / "result-record-v2.schema.json").read_text())
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())
    errors = list(result_validator.iter_errors(record))
    assert not errors, f"Invalid 0.2.2 smoke result: {errors}"
    assert record["run_id"] == "remediation-0.2.2" and record["phase"] == "smoke"
    assert record["case_id"] == "SMOKE-001" and record["invocation"]["index"] == 75
    assert record["invocation"]["model"] == "gpt-5.6-sol" and record["invocation"]["reasoning"] == "high"
    assert record["invocation"]["sandbox"] == "read-only"
    assert record["invocation"]["exit_code"] == 0 and record["invocation"]["thread_id"]
    assert hashlib.sha256(record["first_output"].encode()).hexdigest() == SMOKE_FIRST_OUTPUT_HASH
    assert record["answer_validation"]["applicable"] is True and record["answer_validation"]["valid"] is False
    assert record["final_result"] == "Fail" and record["scoring"]["review_status"] == "reviewed"
    attribution = record["event_attribution"]
    assert attribution["workflow_command_count"] == 0
    assert attribution["workflow_tool_count"] == 6 and attribution["workflow_network_count"] == 6
    assert len({event["item_id"] for event in attribution["workflow_events"]}) == 3
    assert all(event["origin"] == "workflow" and event["event_type"] == "web_search" for event in attribution["workflow_events"])
    assert attribution["evaluator_command_count"] == 1
    assert not record["event_summary"]["approval_events"]
    manifest = json.loads((RUN_022 / "smoke-manifest.json").read_text())
    assert manifest["status"] == "stopped" and manifest["result_count"] == 1
    assert manifest["workflow_command_count"] == 0
    assert manifest["workflow_tool_count"] == 6 and manifest["workflow_network_count"] == 6
    assert manifest["workflow_approval_count"] == 0 and manifest["evaluator_command_count"] == 2
    assert manifest["answer_schema_valid_count"] == 0 and manifest["answer_schema_applicable_count"] == 1
    smoke2_paths = sorted((RUN_022 / "smoke-2").glob("*.json"))
    assert [path.name for path in smoke2_paths] == ["SMOKE-002.json"]
    smoke2_path = smoke2_paths[0]
    assert sha256_bytes(smoke2_path.read_bytes()) == SMOKE2_RECORD_HASH, "Reviewed 0.2.2 corrected smoke record changed"
    record2 = json.loads(smoke2_path.read_text())
    errors2 = list(result_validator.iter_errors(record2))
    assert not errors2, f"Invalid 0.2.2 corrected smoke result: {errors2}"
    assert record2["phase"] == "smoke2" and record2["case_id"] == "SMOKE-002"
    assert record2["invocation"]["index"] == 76 and record2["exact_input"] == record["exact_input"]
    assert hashlib.sha256(record2["first_output"].encode()).hexdigest() == SMOKE2_FIRST_OUTPUT_HASH
    assert record2["answer_validation"]["applicable"] is True and record2["answer_validation"]["valid"] is False
    assert record2["final_result"] == "Fail" and record2["scoring"]["review_status"] == "reviewed"
    attribution2 = record2["event_attribution"]
    assert attribution2["workflow_command_count"] == 0
    assert attribution2["workflow_tool_count"] == 0 and attribution2["workflow_operation_count"] == 0
    assert attribution2["workflow_network_count"] == 0 and attribution2["evaluator_command_count"] == 1
    assert not record2["event_summary"]["approval_events"]
    manifest2 = json.loads((RUN_022 / "smoke2-manifest.json").read_text())
    assert manifest2["status"] == "failed" and manifest2["result_count"] == 1
    assert manifest2["web_search_mode"] == "disabled"
    assert manifest2["workflow_command_count"] == 0 and manifest2["workflow_tool_count"] == 0
    assert manifest2["workflow_operation_count"] == 0 and manifest2["workflow_network_count"] == 0
    assert manifest2["workflow_approval_count"] == 0 and manifest2["evaluator_command_count"] == 2
    assert manifest2["answer_schema_valid_count"] == 0 and manifest2["answer_schema_applicable_count"] == 1
    for directory, case_id, phase, index, record_hash, output_hash in [
        ("smoke-3", "SMOKE-003", "smoke3", 78, SMOKE3_RECORD_HASH, SMOKE3_FIRST_OUTPUT_HASH),
        ("smoke-4", "SMOKE-004", "smoke4", 79, SMOKE4_RECORD_HASH, SMOKE4_FIRST_OUTPUT_HASH),
    ]:
        paths = sorted((RUN_022 / directory).glob("*.json"))
        assert [path.name for path in paths] == [f"{case_id}.json"]
        assert sha256_bytes(paths[0].read_bytes()) == record_hash, f"Reviewed {case_id} record changed"
        smoke_record = json.loads(paths[0].read_text())
        smoke_errors = list(result_validator.iter_errors(smoke_record))
        assert not smoke_errors, f"Invalid {case_id} record: {smoke_errors}"
        assert smoke_record["phase"] == phase and smoke_record["invocation"]["index"] == index
        assert smoke_record["exact_input"] == record["exact_input"]
        assert hashlib.sha256(smoke_record["first_output"].encode()).hexdigest() == output_hash
        assert smoke_record["answer_validation"]["valid"] is False
        assert smoke_record["final_result"] == "Fail" and smoke_record["scoring"]["review_status"] == "reviewed"
        smoke_attribution = smoke_record["event_attribution"]
        assert smoke_attribution["workflow_command_count"] == 0
        assert smoke_attribution["workflow_tool_count"] == 0 and smoke_attribution["workflow_operation_count"] == 0
        assert smoke_attribution["workflow_network_count"] == 0 and smoke_attribution["evaluator_command_count"] == 1
        smoke_manifest = json.loads((RUN_022 / f"{phase}-manifest.json").read_text())
        assert smoke_manifest["status"] == "failed" and smoke_manifest["result_count"] == 1
        assert smoke_manifest["workflow_command_count"] == 0 and smoke_manifest["workflow_tool_count"] == 0
        assert smoke_manifest["workflow_operation_count"] == 0 and smoke_manifest["workflow_network_count"] == 0
        assert smoke_manifest["workflow_approval_count"] == 0 and smoke_manifest["evaluator_command_count"] == 2
        assert smoke_manifest["answer_schema_valid_count"] == 0
    diagnostic_paths = sorted((RUN_022 / "diagnostic").glob("*.json"))
    assert [path.name for path in diagnostic_paths] == ["DIAG-EXPLICIT-001.json"]
    diagnostic_path = diagnostic_paths[0]
    assert sha256_bytes(diagnostic_path.read_bytes()) == DIAGNOSTIC_RECORD_HASH, "Reviewed explicit diagnostic record changed"
    diagnostic = json.loads(diagnostic_path.read_text())
    diagnostic_errors = list(result_validator.iter_errors(diagnostic))
    assert not diagnostic_errors, f"Invalid explicit diagnostic record: {diagnostic_errors}"
    assert diagnostic["phase"] == "diagnostic" and diagnostic["invocation"]["index"] == 77
    assert diagnostic["exact_input"].startswith("$dataverse-webapi-query ")
    assert hashlib.sha256(diagnostic["first_output"].encode()).hexdigest() == DIAGNOSTIC_FIRST_OUTPUT_HASH
    assert diagnostic["answer_validation"] == {"applicable": True, "valid": True, "errors": []}
    assert diagnostic["final_result"] == "Pass" and diagnostic["scoring"]["review_status"] == "reviewed"
    diagnostic_attribution = diagnostic["event_attribution"]
    assert diagnostic_attribution["workflow_command_count"] == 0
    assert diagnostic_attribution["workflow_tool_count"] == 0 and diagnostic_attribution["workflow_operation_count"] == 0
    assert diagnostic_attribution["workflow_network_count"] == 0 and diagnostic_attribution["evaluator_command_count"] == 1
    diagnostic_manifest = json.loads((RUN_022 / "diagnostic-manifest.json").read_text())
    assert diagnostic_manifest["status"] == "passed" and diagnostic_manifest["result_count"] == 1
    assert diagnostic_manifest["answer_schema_valid_count"] == 1
    assert diagnostic_manifest["workflow_tool_count"] == 0 and diagnostic_manifest["workflow_network_count"] == 0


def validate_explicit_030(cases: dict[str, dict]) -> None:
    paths = sorted(path for path in RUN_030.glob("*.json") if path.name != "manifest.json")
    assert len(paths) == 27, f"Expected 27 explicit-0.3.0 records, found {len(paths)}"
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.name.encode() + b"\0" + path.read_bytes())
    assert digest.hexdigest() == EXPLICIT_030_RECORD_DIGEST, "Reviewed explicit-0.3.0 records changed"
    answer_schema = json.loads((SOURCE / "references" / "answer-output.schema.json").read_text())
    result_schema = json.loads((ROOT / "tests" / "result-record-v2.schema.json").read_text())
    answer_validator = Draft202012Validator(answer_schema)
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())
    indexes: set[int] = set()
    thread_ids: set[str] = set()
    suite_passes = {name: 0 for name in EXPECTED_COUNTS}
    answer_valid_count = 0
    legacy_selector_count = 0
    forced_count = 0
    post_review_hashes: dict[str, str] = {}
    for path in paths:
        record = json.loads(path.read_text())
        errors = list(result_validator.iter_errors(record))
        assert not errors, f"Invalid explicit record {path}: {errors}"
        case = cases[record["case_id"]]
        validate_provenance(case, record)
        assert record["run_id"] == "explicit-0.3.0" and record["phase"] == "suite"
        assert record["invocation_mode"] == "explicit"
        assert record["invoked_skill"] == "dataverse-webapi-query"
        assert record["selector_control"] == "$dataverse-webapi-query"
        assert record["exact_input"] == case["prompt"] == record["exact_case_input"]
        assert sha256_bytes(record["exact_case_input"].encode()) == record["exact_case_input_sha256"]
        assert sha256_bytes(record["first_output"].encode()) == record["first_output_sha256"]
        assert record["case_input_contains_legacy_selector"] == case["prompt"].startswith("$dataverse-webapi-query")
        assert record["explicit_invocation_user_forced"] == (record["suite"] == "should-not-trigger")
        legacy_selector_count += record["case_input_contains_legacy_selector"]
        forced_count += record["explicit_invocation_user_forced"]
        invocation = record["invocation"]
        indexes.add(invocation["index"])
        thread_ids.add(invocation["thread_id"])
        assert invocation["cli_version"] == "codex-cli 0.144.5"
        assert invocation["model"] == "gpt-5.6-sol" and invocation["reasoning"] == "high"
        assert invocation["approval_policy"] == "on-request" and invocation["sandbox"] == "read-only"
        assert invocation["exit_code"] == 0 and len(invocation["attempts"]) == 1
        assert record["event_attribution"]["workflow_command_count"] == 0
        assert record["event_attribution"]["workflow_tool_count"] == 0
        assert record["event_attribution"]["workflow_operation_count"] == 0
        assert record["event_attribution"]["workflow_network_count"] == 0
        assert record["event_attribution"]["evaluator_command_count"] == 1
        assert not record["event_summary"]["tool_events"] and not record["event_summary"]["approval_events"]
        parsed = json.loads(record["first_output"])
        answer_errors = list(answer_validator.iter_errors(parsed))
        assert record["answer_validation"]["valid"] == (not answer_errors)
        if record["answer_validation"]["valid"]:
            answer_valid_count += 1
        assert record["scoring"]["review_status"] == "reviewed"
        if record["final_result"] == "Pass":
            suite_passes[record["suite"]] += 1
        post_review_hashes[path.name] = sha256_bytes(path.read_bytes())
    assert indexes == set(range(107, 134))
    assert len(thread_ids) == 27 and None not in thread_ids
    assert legacy_selector_count == 21 and forced_count == 3
    assert answer_valid_count == 26
    assert suite_passes == {"trigger": 3, "should-not-trigger": 3, "golden": 4, "negative": 7, "security": 6, "regression": 3}
    failed = json.loads((RUN_030 / "GOLDEN-005.json").read_text())
    assert failed["final_result"] == "Fail"
    assert failed["answer_validation"]["errors"] == ["{'attribute': 'statecode', 'value': 0, 'meaning': 'Active'} is not of type 'string'"]
    manifest = json.loads((RUN_030 / "manifest.json").read_text())
    assert manifest["status"] == "completed" and manifest["result_count"] == 27
    assert manifest["answer_schema_valid_count"] == 26 and manifest["answer_schema_applicable_count"] == 27
    assert manifest["result_schema_valid_count"] == 27
    assert manifest["workflow_command_count"] == 0 and manifest["workflow_tool_count"] == 0
    assert manifest["workflow_operation_count"] == 0 and manifest["workflow_network_count"] == 0
    assert manifest["workflow_approval_count"] == 0 and manifest["evaluator_command_count"] == 28
    assert manifest["post_review_result_sha256"] == post_review_hashes
    assert manifest["reviewed_pass_count"] == 26 and manifest["reviewed_fail_count"] == 1
    assert manifest["adoption_decision"] == "Reference only"
    assert manifest["work_parity_only_remaining_gate"] is False


def validate_explicit_031(cases: dict[str, dict]) -> None:
    smoke_paths = sorted((RUN_031 / "smoke").glob("*.json"))
    suite_paths = sorted((RUN_031 / "suite").glob("*.json"))
    assert [path.name for path in smoke_paths] == ["GOLDEN-005.json"]
    assert len(suite_paths) == 28
    for paths, expected_digest in [(smoke_paths, EXPLICIT_031_SMOKE_DIGEST), (suite_paths, EXPLICIT_031_SUITE_DIGEST)]:
        digest = hashlib.sha256()
        for path in paths:
            digest.update(path.name.encode() + b"\0" + path.read_bytes())
        assert digest.hexdigest() == expected_digest, "Reviewed explicit-0.3.1 records changed"
    answer_schema = json.loads((SOURCE / "references" / "answer-output.schema.json").read_text())
    result_schema = json.loads((ROOT / "tests" / "result-record-v2.schema.json").read_text())
    answer_validator = Draft202012Validator(answer_schema)
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())
    suite_passes = {name: 0 for name in EXPECTED_COUNTS}
    indexes: set[int] = set()
    thread_ids: set[str] = set()
    for path in smoke_paths + suite_paths:
        record = json.loads(path.read_text())
        result_errors = list(result_validator.iter_errors(record))
        assert not result_errors, f"Invalid explicit-0.3.1 record {path}: {result_errors}"
        case = cases[record["case_id"]]
        validate_provenance(case, record)
        assert record["run_id"] == "explicit-0.3.1"
        assert record["invocation_mode"] == "explicit" and record["invoked_skill"] == "dataverse-webapi-query"
        assert record["selector_control"] == "$dataverse-webapi-query"
        assert record["exact_input"] == case["prompt"] == record["exact_case_input"]
        assert sha256_bytes(record["exact_case_input"].encode()) == record["exact_case_input_sha256"]
        assert sha256_bytes(record["first_output"].encode()) == record["first_output_sha256"]
        invocation = record["invocation"]
        indexes.add(invocation["index"])
        thread_ids.add(invocation["thread_id"])
        assert invocation["cli_version"] == "codex-cli 0.144.5"
        assert invocation["model"] == "gpt-5.6-sol" and invocation["reasoning"] == "high"
        assert invocation["approval_policy"] == "on-request" and invocation["sandbox"] == "read-only"
        assert invocation["exit_code"] == 0 and len(invocation["attempts"]) == 1
        attribution = record["event_attribution"]
        assert attribution["workflow_command_count"] == 0 and attribution["workflow_tool_count"] == 0
        assert attribution["workflow_operation_count"] == 0 and attribution["workflow_network_count"] == 0
        assert attribution["evaluator_command_count"] == 1
        assert not record["event_summary"]["tool_events"] and not record["event_summary"]["approval_events"]
        answer = json.loads(record["first_output"])
        assert not list(answer_validator.iter_errors(answer))
        assert record["answer_validation"] == {"applicable": True, "valid": True, "errors": []}
        assert all(isinstance(item, str) for item in answer["resolved_schema"]["choice_or_status_values"])
        assert record["scoring"]["review_status"] == "reviewed" and record["final_result"] == "Pass"
        if record["phase"] == "suite":
            suite_passes[record["suite"]] += 1
    assert indexes == set(range(134, 163))
    assert len(thread_ids) == 29 and None not in thread_ids
    assert suite_passes == EXPECTED_COUNTS
    original = RUN_030 / "GOLDEN-005.json"
    assert sha256_bytes(original.read_bytes()) == "46216cf49922631d41d96770ac96713ea50717ed1944347a210b70fc1ce256eb"
    original_record = json.loads(original.read_text())
    assert sha256_bytes(original_record["first_output"].encode()) == "1dab8f1d0dd85b091706ce6ebbeaac1bf50a2c056dd168144dd1f033278dbfaf"
    for path in [smoke_paths[0], RUN_031 / "suite" / "GOLDEN-005.json", RUN_031 / "suite" / "REG-004.json"]:
        answer = json.loads(json.loads(path.read_text())["first_output"])
        assert answer["resolved_schema"]["choice_or_status_values"] == ["statecode=0 (Active)"]
        query = answer["query_or_code"]
        for fragment in ["AccountsService.getAll", '"name"', '"accountnumber"', "statecode eq 0", "createdon desc", "top: 10"]:
            assert fragment in query, f"Query equivalence fragment missing in {path}: {fragment}"
    reg4 = json.loads((RUN_031 / "suite" / "REG-004.json").read_text())
    assert reg4["provenance"] == cases["REG-004"]["provenance"]
    smoke_manifest = json.loads((RUN_031 / "smoke-manifest.json").read_text())
    suite_manifest = json.loads((RUN_031 / "suite-manifest.json").read_text())
    assert smoke_manifest["status"] == "passed" and smoke_manifest["answer_schema_valid_count"] == 1
    assert smoke_manifest["result_schema_valid_count"] == 1 and smoke_manifest["workflow_operation_count"] == 0
    assert smoke_manifest["evaluator_command_count"] == 2 and smoke_manifest["post_review_record_digest"] == EXPLICIT_031_SMOKE_DIGEST
    assert suite_manifest["status"] == "completed" and suite_manifest["result_count"] == 28
    assert suite_manifest["answer_schema_valid_count"] == 28 and suite_manifest["result_schema_valid_count"] == 28
    assert suite_manifest["workflow_command_count"] == 0 and suite_manifest["workflow_tool_count"] == 0
    assert suite_manifest["workflow_operation_count"] == 0 and suite_manifest["workflow_network_count"] == 0
    assert suite_manifest["workflow_approval_count"] == 0 and suite_manifest["evaluator_command_count"] == 29
    assert suite_manifest["post_review_record_digest"] == EXPLICIT_031_SUITE_DIGEST
    assert suite_manifest["adoption_decision"] == "Experiment approved pending ChatGPT Work parity"
    assert suite_manifest["work_parity_only_remaining_gate"] is True
    manifest_030 = json.loads((RUN_030 / "manifest.json").read_text())
    assert manifest_030["fixture_sha256"]["regression-cases.yaml"] == "ed3d0256a9577a0bd5ccb18679dfc42da534e4243541f649a9518cd0426e85e7"


def validate_evidence_contract_032() -> None:
    assert sha256_bytes((SOURCE / "SKILL.md").read_bytes()) == "47abc97160ca9bc1d06a1c5d350ef7538d1ffc0a731463843973885e43f071ab"
    assert sha256_bytes((SOURCE / "references" / "answer-output.schema.json").read_bytes()) == "d889c80f0c7635ba006e4ca98ca717bbd7ccf5c20a89db2b92d356936ea84ad1"
    assert sha256_bytes((ROOT / "tests" / "result-record-v2.schema.json").read_bytes()) == RESULT_V2_HASH
    answer_schema = json.loads((SOURCE / "references" / "answer-output.schema.json").read_text())
    result_schema = json.loads((ROOT / "tests" / "result-record-v3.schema.json").read_text())
    Draft202012Validator.check_schema(result_schema)
    answer_validator = Draft202012Validator(answer_schema)
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())

    raw_dir = WORK_031 / "raw"
    v3_dir = WORK_031 / "v3"
    for name, expected_hash in WORK_RAW_HASHES.items():
        path = raw_dir / name
        assert path.is_file(), f"Missing immutable Work evidence: {path}"
        assert sha256_bytes(path.read_bytes()) == expected_hash, f"Raw Work evidence changed: {path}"

    copy_provenance = json.loads((WORK_031 / "raw-copy-provenance.json").read_text())
    assert copy_provenance["evidence_contract_version"] == "0.3.2"
    assert len(copy_provenance["files"]) == 4
    for item in copy_provenance["files"]:
        assert item["source_sha256"] == item["destination_sha256"]
        destination = ROOT / item["destination"]
        assert sha256_bytes(destination.read_bytes()) == item["destination_sha256"]

    historical_manifest = WORK_031 / "historical" / "powercat-dataverse-work-parity-0.3.1-MANIFEST.sha256"
    assert sha256_bytes(historical_manifest.read_bytes()) == HISTORICAL_MANIFEST_HASH
    self_lines = [line for line in historical_manifest.read_text().splitlines() if line.endswith("  ./MANIFEST.sha256")]
    assert self_lines == [f"{HISTORICAL_MANIFEST_SELF_CLAIM}  ./MANIFEST.sha256"]
    assert HISTORICAL_MANIFEST_SELF_CLAIM != HISTORICAL_MANIFEST_HASH

    codex_paths = sorted((RUN_031 / "smoke").glob("*.json")) + sorted((RUN_031 / "suite").glob("*.json"))
    work_paths = sorted(v3_dir.glob("*.json"))
    assert len(codex_paths) == 29 and len(work_paths) == 3
    answer_valid = 0
    workflow_failures = 0

    for path in codex_paths:
        record = json.loads(path.read_text())
        errors = list(result_validator.iter_errors(record))
        assert not errors, f"Codex v3 profile conflict {path}: {[error.message for error in errors]}"
        assert record["invocation"]["client"] == "Codex CLI"
        assert record["invocation"]["thread_id"]
        assert sha256_bytes(record["exact_case_input"].encode()) == record["exact_case_input_sha256"]
        assert sha256_bytes(record["first_output"].encode()) == record["first_output_sha256"]
        assert not list(answer_validator.iter_errors(json.loads(record["first_output"])))
        assert record["answer_validation"] == {"applicable": True, "valid": True, "errors": []}
        assert record["scoring"]["score_percent"] == 100.0
        assert record["scoring"]["dimensions"]["scope"]["rating"] == "Pass"
        attribution = record["event_attribution"]
        counts = [attribution[key] for key in ["workflow_command_count", "workflow_tool_count", "workflow_operation_count", "workflow_network_count"]]
        workflow_failures += sum(counts) + len(attribution["workflow_events"])
        answer_valid += 1

    expected_v3_names = {f"{case_id}-2026-07-19-chatgpt-work.json" for case_id in WORK_EXPECTED}
    assert {path.name for path in work_paths} == expected_v3_names
    for path in work_paths:
        record = json.loads(path.read_text())
        case_id = record["case_id"]
        result_type, status, runnable = WORK_EXPECTED[case_id]
        errors = list(result_validator.iter_errors(record))
        assert not errors, f"Work v3 profile conflict {path}: {[error.message for error in errors]}"
        assert record["schema_version"] == "3.0" and record["final_result"] == "Pass"
        assert record["invocation"]["client"] == "ChatGPT Work"
        unavailable_codex_fields = {"thread_id", "cli_version", "approval_policy", "sandbox", "ephemeral", "exit_code", "attempts"}
        assert not unavailable_codex_fields.intersection(record["invocation"])
        assert sha256_bytes(record["exact_case_input"].encode()) == record["exact_case_input_sha256"]
        assert sha256_bytes(record["first_output"].encode()) == record["first_output_sha256"]
        answer = json.loads(record["first_output"])
        assert not list(answer_validator.iter_errors(answer))
        assert answer["result_type"] == result_type and answer["status"] == status
        assert bool(answer["query_or_code"]) is runnable
        assert record["answer_validation"] == {"applicable": True, "valid": True, "errors": []}
        assert record["scoring"]["score_percent"] == 100.0
        assert record["scoring"]["dimensions"]["scope"]["rating"] == "Pass"
        assert all(value == 0 for key, value in record["forbidden_behavior_scoring"].items() if key != "result")
        assert record["forbidden_behavior_scoring"]["result"] == "Pass"
        attribution = record["event_attribution"]
        assert attribution["evaluator_operation_count"] == len(attribution["evaluator_events"]) == 6
        counts = [attribution[key] for key in ["workflow_command_count", "workflow_tool_count", "workflow_operation_count", "workflow_network_count"]]
        workflow_failures += sum(counts) + len(attribution["workflow_events"])
        evidence = record["evidence_contract"]
        raw_path = ROOT / evidence["source_raw_path"]
        raw_record = json.loads(raw_path.read_text())
        assert sha256_bytes(raw_path.read_bytes()) == evidence["source_raw_sha256"]
        assert raw_record["first_output"] == record["first_output"]
        assert raw_record["exact_case_input"] == record["exact_case_input"]
        assert raw_record["final_result"] == "Fail"
        assert len(evidence["normalization_mappings"]) == 8
        assert evidence["evaluator_identity"] == {"availability": "not_exposed_by_host", "value": None}
        parity = record["parity_evidence"]
        codex_path = ROOT / parity["codex_record_path"]
        assert sha256_bytes(codex_path.read_bytes()) == parity["codex_record_sha256"]
        codex_answer = json.loads(json.loads(codex_path.read_text())["first_output"])
        assert codex_answer["result_type"] == result_type and codex_answer["status"] == status
        assert parity["functional_parity"] == "Pass"
        answer_valid += 1

    manifest = json.loads((WORK_031 / "v3-manifest.json").read_text())
    assert manifest["record_count"] == 3 and manifest["answer_schema_valid"] == 3
    assert manifest["result_schema_v3_valid"] == 3 and manifest["workflow_operation_count"] == 0
    assert manifest["functional_parity"] == {case_id: "Pass" for case_id in WORK_EXPECTED}
    for name, expected_hash in manifest["record_sha256"].items():
        assert sha256_bytes((v3_dir / name).read_bytes()) == expected_hash

    assert answer_valid == 32
    assert workflow_failures == 0

    package_name = "powercat-dataverse-work-parity-0.3.2"
    zip_path = ROOT / f"{package_name}.zip"
    package_provenance = json.loads((WORK_031 / "package-0.3.2-provenance.json").read_text())
    sidecar_manifest = WORK_031 / "package-0.3.2-MANIFEST.sha256"
    assert package_provenance["zip_sha256"] == sha256_bytes(zip_path.read_bytes())
    assert package_provenance["manifest_sha256"] == sha256_bytes(sidecar_manifest.read_bytes())
    manifest_lines = sidecar_manifest.read_text().splitlines()
    assert len(manifest_lines) == package_provenance["manifest_entry_count"]
    expected_hashes = {line.split("  ./", 1)[1]: line.split("  ./", 1)[0] for line in manifest_lines}
    assert "MANIFEST.sha256" not in expected_hashes
    assert not any(path.endswith(".zip") or path.startswith(("tmp/", "temp/")) for path in expected_hashes)
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        prefix = f"{package_name}/"
        assert f"{prefix}MANIFEST.sha256" in names
        assert archive.read(f"{prefix}MANIFEST.sha256") == sidecar_manifest.read_bytes()
        for relative_path, expected_hash in expected_hashes.items():
            assert sha256_bytes(archive.read(f"{prefix}{relative_path}")) == expected_hash


def main() -> None:
    for path in sorted((ROOT / "tests").glob("*.yaml")):
        yaml.safe_load(path.read_text())
    for path in sorted(ROOT.rglob("*.json")):
        json.loads(path.read_text())
    assert not list(ROOT.rglob("*.pyc")), "Unexpected Python bytecode in experiment"
    assert not [path for path in ROOT.rglob("*") if path.is_symlink()], "Symlink found in self-contained experiment"
    compare_dirs(SOURCE, DISCOVERY)
    validate_links()
    validate_placeholders()
    validate_baseline()
    cases = load_cases()
    validate_remediation(cases)
    validate_022_smoke()
    validate_explicit_030(cases)
    validate_explicit_031(cases)
    validate_evidence_contract_032()
    print("Structure, copies, links, placeholders, baseline, fixtures, provenance, schemas, coverage, and immutable evidence: PASS")
    print("0.2.2 smoke 1: FAIL (answer contract 0/1; 0 commands; 3 web searches / 6 lifecycle events)")
    print("0.2.2 smoke 2: FAIL (answer contract 0/1; 0 commands, tools, approvals, or network events; suite blocked)")
    print("0.2.2 explicit diagnostic: PASS (answer contract 1/1; zero workflow events)")
    print("0.2.2 smokes 3-4: FAIL (answer contract 0/2; zero workflow events; implicit selection unproved)")
    print("0.3.0 explicit suite: 26/27 (answer schema 26/27; result schema 27/27; workflow operations 0; evaluator commands 28)")
    print("0.3.1 GOLDEN-005 smoke: 1/1 (answer/result schemas valid; workflow operations 0; evaluator commands 2)")
    print("0.3.1 explicit suite: 28/28 (answer/result schemas 28/28; workflow operations 0; evaluator commands 29)")
    print("0.3.2 evidence contract: Codex v3 29/29; Work v3 3/3; answer schema 32/32; Work parity 3/3; workflow failures 0")
    print("Adoption gates: PASS; Repository-level approved — explicit invocation only")


if __name__ == "__main__":
    main()
