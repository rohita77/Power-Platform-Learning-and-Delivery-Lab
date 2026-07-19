#!/usr/bin/env python3
"""Run the gated immutable explicit-invocation 0.3.1 remediation."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess

from jsonschema import Draft202012Validator, FormatChecker

import run_explicit_cases as base

ROOT = base.ROOT
RUN_ID = "explicit-0.3.1"
RESULTS_ROOT = base.BASELINE / RUN_ID if hasattr(base, "BASELINE") else ROOT / "tests" / "results" / "codex" / RUN_ID
SMOKE_RESULTS = RESULTS_ROOT / "smoke"
SUITE_RESULTS = RESULTS_ROOT / "suite"
SMOKE_MANIFEST = RESULTS_ROOT / "smoke-manifest.json"
SUITE_MANIFEST = RESULTS_ROOT / "suite-manifest.json"
SMOKE_INDEX = 134
SUITE_START_INDEX = 135
EXPECTED_CASES = 28
EXPECTED_SKILL_SHA256 = "47abc97160ca9bc1d06a1c5d350ef7538d1ffc0a731463843973885e43f071ab"
EXPECTED_ANSWER_SCHEMA_SHA256 = base.EXPECTED_ANSWER_SCHEMA_SHA256
EXPECTED_FIXTURE_SHA256 = {
    "trigger-cases.yaml": "8aa81cca93a49461c3b2a565d78aa0b5eb31f4c815ee3bbb09dad79e0c4723de",
    "golden-cases.yaml": "b9c256006a08144349261173cca9087731fc8847b2167c6f129a2cd160a00cd5",
    "negative-cases.yaml": "2f2f81d3204507521909f2b87e861255a74af795b0421bb947ee20c9142c6143",
    "security-cases.yaml": "41b88f6f07019348c2c029130134b750544d636312864145878479e960c7b600",
    "regression-cases.yaml": "01b0ce4fad619e3b01df88a9332798626bcaad251cd0b67b3d0cb667855f03ab",
}
PRESERVED_030_RECORD_DIGEST = "16a0cbf702ef7b07aae9bf422e9632cc4562f461b4ddef85f4223935b5e8bdd3"


def configure_base() -> None:
    base.RUN_ID = RUN_ID
    base.RESULTS_ROOT = RESULTS_ROOT
    base.MANIFEST_PATH = SUITE_MANIFEST
    base.START_INDEX = SUITE_START_INDEX
    base.EXPECTED_CASES = EXPECTED_CASES
    base.EXPECTED_SKILL_SHA256 = EXPECTED_SKILL_SHA256
    base.EXPECTED_FIXTURE_SHA256 = EXPECTED_FIXTURE_SHA256


def record_digest(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    for record_path in sorted(item for item in path.glob("*.json") if item.name != "manifest.json"):
        digest.update(record_path.name.encode() + b"\0" + record_path.read_bytes())
    return digest.hexdigest()


def preflight(phase: str):
    configure_base()
    if phase == "smoke" and RESULTS_ROOT.exists():
        raise SystemExit(f"Immutable result target already exists: {RESULTS_ROOT}")
    if phase == "suite":
        if SUITE_RESULTS.exists() or SUITE_MANIFEST.exists():
            raise SystemExit("Immutable 0.3.1 suite evidence already exists")
        if not SMOKE_MANIFEST.exists() or not (SMOKE_RESULTS / "GOLDEN-005.json").exists():
            raise SystemExit("The required GOLDEN-005 smoke evidence is absent")
        smoke_manifest = json.loads(SMOKE_MANIFEST.read_text())
        smoke_record = json.loads((SMOKE_RESULTS / "GOLDEN-005.json").read_text())
        if smoke_manifest.get("status") != "passed" or smoke_record["answer_validation"]["valid"] is not True:
            raise SystemExit("The GOLDEN-005 smoke gate did not pass")
        smoke_answer = json.loads(smoke_record["first_output"])
        if not all(isinstance(value, str) for value in smoke_answer["resolved_schema"]["choice_or_status_values"]):
            raise SystemExit("The GOLDEN-005 smoke did not serialize choice/status values as strings")
    if base.SKILL_PATH.read_bytes() != base.SOURCE_SKILL_PATH.read_bytes():
        raise SystemExit("Adaptation source and discovery SKILL.md differ")
    if base.sha256_bytes(base.SKILL_PATH.read_bytes()) != EXPECTED_SKILL_SHA256:
        raise SystemExit("Frozen 0.3.1 skill hash changed")
    if base.sha256_bytes(base.ANSWER_SCHEMA_PATH.read_bytes()) != EXPECTED_ANSWER_SCHEMA_SHA256:
        raise SystemExit("Frozen answer schema changed")
    prior = ROOT / "tests" / "results" / "codex" / "explicit-0.3.0"
    if record_digest(prior) != PRESERVED_030_RECORD_DIGEST:
        raise SystemExit("The immutable explicit-0.3.0 records changed")
    cases, fixture_hashes = base.load_cases()
    answer_schema = json.loads(base.ANSWER_SCHEMA_PATH.read_text())
    result_schema = json.loads(base.RESULT_SCHEMA_PATH.read_text())
    Draft202012Validator.check_schema(answer_schema)
    Draft202012Validator.check_schema(result_schema)
    started_at = base.now()
    command = ["codex", "--version"]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    version = completed.stdout.strip()
    if version != base.CLI_VERSION:
        raise SystemExit(f"Required {base.CLI_VERSION}; found {version}")
    version_event = base.evaluator_event(command, f"{phase.upper()}-0.3.1-RUN", started_at, "completed", "codex --version")
    return (
        cases,
        fixture_hashes,
        Draft202012Validator(answer_schema),
        Draft202012Validator(result_schema, format_checker=FormatChecker()),
        version,
        version_event,
    )


def write_manifest(
    phase: str,
    status: str,
    stop_reason: str | None,
    paths: list[pathlib.Path],
    fixture_hashes: dict[str, str],
    version: str,
    version_event: dict,
) -> None:
    records = [json.loads(path.read_text()) for path in paths]
    manifest_path = SMOKE_MANIFEST if phase == "smoke" else SUITE_MANIFEST
    manifest = {
        "run_id": RUN_ID,
        "phase": phase,
        "status": status,
        "stop_reason": stop_reason,
        "planned_result_count": 1 if phase == "smoke" else EXPECTED_CASES,
        "result_count": len(records),
        "result_files": [str(path.relative_to(ROOT)) for path in paths],
        "pre_review_result_sha256": {path.name: base.sha256_bytes(path.read_bytes()) for path in paths},
        "skill_sha256": EXPECTED_SKILL_SHA256,
        "answer_schema_sha256": EXPECTED_ANSWER_SCHEMA_SHA256,
        "result_schema_sha256": base.sha256_bytes(base.RESULT_SCHEMA_PATH.read_bytes()),
        "fixture_sha256": fixture_hashes,
        "client_version": version,
        "model": base.MODEL,
        "reasoning": base.REASONING,
        "approval_policy": "on-request",
        "sandbox": "read-only",
        "invocation_mode": "explicit",
        "invoked_skill": "dataverse-webapi-query",
        "selector_control": base.SELECTOR,
        "input_transport": base.INPUT_TRANSPORT,
        "answer_schema_valid_count": sum(record["answer_validation"]["valid"] is True for record in records),
        "answer_schema_applicable_count": len(records),
        "result_schema_valid_count": len(records),
        "workflow_command_count": sum(record["event_attribution"]["workflow_command_count"] for record in records),
        "workflow_tool_count": sum(record["event_attribution"]["workflow_tool_count"] for record in records),
        "workflow_operation_count": sum(record["event_attribution"]["workflow_operation_count"] for record in records),
        "workflow_network_count": sum(record["event_attribution"]["workflow_network_count"] for record in records),
        "workflow_approval_count": sum(len(record["event_summary"]["approval_events"]) for record in records),
        "evaluator_command_count": 1 + sum(record["event_attribution"]["evaluator_command_count"] for record in records),
        "evaluator_events": [version_event],
        "isolation_claim": base.ISOLATION,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def run_phase(phase: str) -> None:
    cases, fixture_hashes, answer_validator, result_validator, version, version_event = preflight(phase)
    output_dir = SMOKE_RESULTS if phase == "smoke" else SUITE_RESULTS
    output_dir.mkdir(parents=True)
    phase_cases = [next(case for case in cases if case["id"] == "GOLDEN-005")] if phase == "smoke" else cases
    start_index = SMOKE_INDEX if phase == "smoke" else SUITE_START_INDEX
    result_paths: list[pathlib.Path] = []
    status = "passed" if phase == "smoke" else "completed"
    stop_reason = None
    for offset, case in enumerate(phase_cases):
        attempts = [base.run_attempt(case, 1)]
        if attempts[0]["exit_code"] != 0 or not attempts[0]["first_output"]:
            attempts.append(base.run_attempt(case, 2))
        fixture_name = base.fixture_for(case["id"])
        record = base.build_record(
            case,
            start_index + offset,
            version,
            attempts,
            answer_validator,
            fixture_hashes[fixture_name],
        )
        record["phase"] = phase
        result_errors = [error.message for error in result_validator.iter_errors(record)]
        if result_errors:
            raise SystemExit(f"Refusing to write invalid result record for {case['id']}: {result_errors}")
        path = output_dir / f"{case['id']}.json"
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        result_paths.append(path)
        print(
            f"{start_index + offset:03d} {case['id']}: exit={record['invocation']['exit_code']} "
            f"answer_schema={record['answer_validation']['valid']} "
            f"workflow_operations={record['event_attribution']['workflow_operation_count']}"
        )
        if not base.record_is_safe(record):
            status = "stopped"
            stop_reason = f"Safety boundary or repeated infrastructure failure in {case['id']}"
            break
        if phase == "smoke":
            answer = json.loads(record["first_output"])
            string_items = all(isinstance(value, str) for value in answer["resolved_schema"]["choice_or_status_values"])
            if record["answer_validation"]["valid"] is not True or not string_items:
                status = "failed"
                stop_reason = "GOLDEN-005 failed answer-schema or flat-string serialization validation"
                break
    write_manifest(phase, status, stop_reason, result_paths, fixture_hashes, version, version_event)
    print(f"{phase} manifest: status={status} results={len(result_paths)}")
    if status not in {"passed", "completed"}:
        raise SystemExit(stop_reason)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["smoke", "suite"])
    args = parser.parse_args()
    run_phase(args.phase)


if __name__ == "__main__":
    main()
