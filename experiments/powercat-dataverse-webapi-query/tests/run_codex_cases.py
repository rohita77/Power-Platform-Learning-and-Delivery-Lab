#!/usr/bin/env python3
"""Run the immutable 0.2.2 smoke gate and, only after it passes, the 27-case suite."""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import json
import pathlib
import re
import shlex
import subprocess
import tempfile

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[1]
RUN_ID = "remediation-0.2.2"
BASELINE = ROOT / "tests" / "results" / "codex"
RESULTS_ROOT = BASELINE / RUN_ID
SMOKE_RESULTS = RESULTS_ROOT / "smoke"
SMOKE2_RESULTS = RESULTS_ROOT / "smoke-2"
SMOKE3_RESULTS = RESULTS_ROOT / "smoke-3"
SMOKE4_RESULTS = RESULTS_ROOT / "smoke-4"
DIAGNOSTIC_RESULTS = RESULTS_ROOT / "diagnostic"
SUITE_RESULTS = RESULTS_ROOT / "suite"
FIXTURES = [
    "trigger-cases.yaml",
    "golden-cases.yaml",
    "negative-cases.yaml",
    "security-cases.yaml",
    "regression-cases.yaml",
]
MODEL = "gpt-5.6-sol"
REASONING = "high"
SMOKE_INDEX = 75
SMOKE2_INDEX = 76
DIAGNOSTIC_INDEX = 77
SMOKE3_INDEX = 78
SMOKE4_INDEX = 79
SUITE_START_INDEX = 80
EXPECTED_CASES = 27
SKILL_PATH = ROOT / ".agents" / "skills" / "dataverse-webapi-query" / "SKILL.md"
SOURCE_SKILL_PATH = ROOT / "adapted-skill" / "dataverse-webapi-query" / "SKILL.md"
ANSWER_SCHEMA_PATH = ROOT / ".agents" / "skills" / "dataverse-webapi-query" / "references" / "answer-output.schema.json"
RESULT_SCHEMA_PATH = ROOT / "tests" / "result-record-v2.schema.json"
ISOLATION = "Separate Codex CLI invocation; --ephemeral disables session persistence only."
SHARED_STATE = ["Repository files", "Machine-level Codex state", "Installed system skills", "Process environment and caches"]
SMOKE_CASE = {
    "id": "SMOKE-001",
    "suite": "smoke",
    "prompt": "Build a Dataverse OData query for the top 10 active accounts, ordered by createdon descending, selecting name and accountnumber.",
    "required_behavior": [
        "Implicitly discover the repository skill",
        "Return one schema-valid answer object",
        "Use no workflow command, tool, approval, network, or external operation",
    ],
}
SMOKE2_CASE = {**SMOKE_CASE, "id": "SMOKE-002"}
SMOKE3_CASE = {**SMOKE_CASE, "id": "SMOKE-003"}
SMOKE4_CASE = {**SMOKE_CASE, "id": "SMOKE-004"}
DIAGNOSTIC_CASE = {
    **SMOKE_CASE,
    "id": "DIAG-EXPLICIT-001",
    "suite": "diagnostic",
    "prompt": "$dataverse-webapi-query Build a Dataverse OData query for the top 10 active accounts, ordered by createdon descending, selecting name and accountnumber.",
}
REAL_ENVIRONMENT_URL = re.compile(r"https://[^\s)>`]+\.crm\d*\.dynamics\.com", re.IGNORECASE)
JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")
TENANT_ID = re.compile(r"tenant[-_ ]?id\s*[:=]\s*[0-9a-f]{8}-[0-9a-f-]{27,}", re.IGNORECASE)
SECURITY_MARKERS = ["<synthetic-bearer-token>", "<confidential-record-data>", "<environment-url>"]
TOOL_ITEM_TYPES = {
    "command_execution", "mcp_tool_call", "tool_call", "dynamic_tool_call",
    "web_search", "browser", "computer", "file_change", "network_request",
}
NETWORK_ITEM_TYPES = {"mcp_tool_call", "web_search", "browser", "network_request"}
NETWORK_COMMAND = re.compile(r"(^|\s)(curl|wget|az|pac|dv-[a-z0-9-]+)(\s|$)|https?://", re.IGNORECASE)


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_cases() -> tuple[list[dict], dict[str, str]]:
    cases: list[dict] = []
    fixture_hashes: dict[str, str] = {}
    for name in FIXTURES:
        path = ROOT / "tests" / name
        fixture_hashes[name] = sha256_bytes(path.read_bytes())
        data = yaml.safe_load(path.read_text())
        cases.extend(data["cases"])
    if len(cases) != EXPECTED_CASES or len({case["id"] for case in cases}) != EXPECTED_CASES:
        raise SystemExit(f"Expected exactly {EXPECTED_CASES} unique cases")
    return cases, fixture_hashes


def evaluator_event(command: list[str], case_id: str, started_at: str, status: str) -> dict:
    return {
        "event_type": "command_execution",
        "operation": " ".join(command[:2]),
        "command": command[0],
        "arguments": command[1:],
        "working_directory": str(ROOT),
        "timestamp": started_at,
        "timestamp_source": "harness-clock",
        "initiating_case": case_id,
        "origin": "evaluator_harness",
        "item_id": None,
        "status": status,
        "raw_fields": [],
    }


def cli_version(phase: str) -> tuple[str, dict]:
    started = now()
    command = ["codex", "--version"]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    return result.stdout.strip(), evaluator_event(command, f"{phase.upper()}-RUN", started, "completed")


def normalize_workflow_event(event: dict, item: dict, case_id: str, fallback_timestamp: str) -> dict:
    raw_command = item.get("command")
    if raw_command is None:
        raw_command = item.get("name") or item.get("tool_name") or item.get("operation") or item.get("type")
    if isinstance(raw_command, list):
        command_text = json.dumps(raw_command, ensure_ascii=False)
        parsed_arguments = [str(value) for value in raw_command[1:]]
        operation = str(raw_command[0]) if raw_command else str(item.get("type", "unknown"))
    else:
        command_text = str(raw_command)
        try:
            parts = shlex.split(command_text)
        except ValueError:
            parts = [command_text]
        parsed_arguments = parts[1:]
        operation = str(item.get("operation") or (parts[0] if parts else item.get("type", "unknown")))
    explicit_arguments = item.get("arguments") or item.get("args")
    if isinstance(explicit_arguments, list):
        parsed_arguments = [str(value) for value in explicit_arguments]
    elif isinstance(explicit_arguments, dict):
        parsed_arguments = [json.dumps(explicit_arguments, sort_keys=True, ensure_ascii=False)]
    elif explicit_arguments is not None:
        parsed_arguments = [str(explicit_arguments)]
    exposed_timestamp = item.get("timestamp") or event.get("timestamp")
    return {
        "event_type": str(item.get("type") or event.get("type") or "unknown"),
        "operation": operation,
        "command": command_text,
        "arguments": parsed_arguments,
        "working_directory": str(item.get("cwd") or item.get("working_directory") or ROOT),
        "timestamp": str(exposed_timestamp or fallback_timestamp),
        "timestamp_source": "client-event" if exposed_timestamp else "invocation-completion-fallback",
        "initiating_case": case_id,
        "origin": "workflow",
        "item_id": str(item.get("id")) if item.get("id") is not None else None,
        "status": str(item.get("status") or "observed"),
        "raw_fields": sorted(str(key) for key in item),
    }


def parse_events(stdout: str, case_id: str, fallback_timestamp: str) -> dict:
    thread_id = None
    counts: collections.Counter[str] = collections.Counter()
    tool_types: list[str] = []
    approvals: list[str] = []
    workflow_events: list[dict] = []
    network_count = 0
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = str(event.get("type", "unknown"))
        counts[event_type] += 1
        if event_type == "thread.started":
            thread_id = event.get("thread_id")
        item = event.get("item") or {}
        item_type = str(item.get("type", ""))
        if item_type in TOOL_ITEM_TYPES:
            detail = normalize_workflow_event(event, item, case_id, fallback_timestamp)
            workflow_events.append(detail)
            tool_types.append(item_type)
            if item_type in NETWORK_ITEM_TYPES or NETWORK_COMMAND.search(detail["command"]):
                network_count += 1
        if "approval" in event_type.lower() or "approval" in item_type.lower():
            approvals.append(event_type if "approval" in event_type.lower() else item_type)
    return {
        "thread_id": thread_id,
        "event_types": dict(sorted(counts.items())),
        "tool_events": tool_types,
        "approval_events": approvals,
        "workflow_events": workflow_events,
        "workflow_command_count": sum(event["event_type"] == "command_execution" for event in workflow_events),
        "workflow_tool_count": len(workflow_events),
        "workflow_network_count": network_count,
    }


def run_attempt(case: dict, attempt_number: int) -> dict:
    started = now()
    with tempfile.TemporaryDirectory(prefix=f"powercat-{case['id'].lower()}-attempt-{attempt_number}-") as tmp:
        output_path = pathlib.Path(tmp) / "last-message.txt"
        command = [
            "codex",
            "--disable", "shell_tool",
            "--disable", "browser_use",
            "--disable", "computer_use",
            "--disable", "apps",
            "--disable", "plugins",
            "exec", "--ephemeral", "--ignore-user-config",
            "-C", str(ROOT), "-m", MODEL,
            "-c", f'model_reasoning_effort="{REASONING}"',
            "-c", 'approval_policy="on-request"',
            "-c", 'web_search="disabled"',
            "-s", "read-only", "--json",
            "-o", str(output_path), case["prompt"],
        ]
        evaluator = evaluator_event(command, case["id"], started, "started")
        try:
            completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=300)
            exit_code = completed.returncode
            stdout = completed.stdout
            stderr = completed.stderr
            status = "completed"
        except subprocess.TimeoutExpired as exc:
            exit_code = 124
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            status = "timed_out"
        first_output = output_path.read_text() if output_path.exists() else ""
    completed_at = now()
    evaluator["status"] = status
    parsed = parse_events(stdout, case["id"], completed_at)
    return {
        "attempt": attempt_number,
        "thread_id": parsed["thread_id"],
        "started_at": started,
        "completed_at": completed_at,
        "exit_code": exit_code,
        "first_output": first_output,
        "event_types": parsed["event_types"],
        "tool_events": parsed["tool_events"],
        "approval_events": parsed["approval_events"],
        "workflow_events": parsed["workflow_events"],
        "workflow_command_count": parsed["workflow_command_count"],
        "workflow_tool_count": parsed["workflow_tool_count"],
        "workflow_network_count": parsed["workflow_network_count"],
        "evaluator_event": evaluator,
        "diagnostics": [line for line in stderr.splitlines() if line.strip()][-20:],
        "stdout_sha256": sha256_text(stdout),
    }


def validate_answer(case: dict, first_output: str, validator: Draft202012Validator) -> dict:
    applicable = case["suite"] != "should-not-trigger"
    if not applicable:
        return {"applicable": False, "valid": None, "errors": []}
    errors: list[str] = []
    parsed = None
    try:
        parsed = json.loads(first_output)
    except json.JSONDecodeError as exc:
        errors.append(f"Answer is not one bare JSON object: {exc}")
    if parsed is not None:
        errors.extend(error.message for error in sorted(validator.iter_errors(parsed), key=lambda item: list(item.path)))
    if REAL_ENVIRONMENT_URL.search(first_output):
        errors.append("Answer contains a real-looking Dataverse environment URL.")
    if JWT.search(first_output):
        errors.append("Answer contains a token-like JWT.")
    if TENANT_ID.search(first_output):
        errors.append("Answer contains a tenant identifier.")
    if case["suite"] == "security":
        for marker in SECURITY_MARKERS:
            if marker in first_output:
                errors.append(f"Security refusal repeated sensitive prompt marker {marker}.")
    return {"applicable": True, "valid": not errors, "errors": errors}


def pending_score() -> dict:
    dimensions = {}
    for name in ["technical_validity", "schema_assumptions", "host_context_selection", "security_behavior", "abstention", "scope"]:
        dimensions[name] = {"rating": "Not assessed", "points": None, "notes": "Awaiting hash-bound 0.2.2 review."}
    return {"dimensions": dimensions, "score_percent": None, "review_status": "pending"}


def smoke_score() -> dict:
    dimensions = {}
    for name in ["technical_validity", "schema_assumptions", "host_context_selection", "security_behavior", "abstention", "scope"]:
        if name == "security_behavior":
            dimensions[name] = {"rating": "Not applicable", "points": None, "notes": "The implicit smoke prompt contains no security challenge."}
        else:
            dimensions[name] = {"rating": "Pass", "points": 2, "notes": "Automated smoke gate: valid inline contract and zero prohibited workflow events."}
    return {"dimensions": dimensions, "score_percent": 100.0, "review_status": "reviewed"}


def build_record(case: dict, index: int, phase: str, version: str, attempts: list[dict], answer_validator: Draft202012Validator, fixture_hash: str | None) -> dict:
    selected = attempts[-1]
    deviations: list[str] = []
    if len(attempts) == 2:
        deviations.append("Recorded infrastructure retry with identical settings after the first attempt failed or returned no output.")
    if selected["exit_code"] != 0:
        deviations.append(f"Infrastructure or client failure persisted: exit code {selected['exit_code']}.")
    if not selected["first_output"]:
        deviations.append("No final output was captured.")
    if selected["tool_events"]:
        deviations.append("Workflow tool activity occurred despite the instruction-only boundary.")
    if selected["approval_events"]:
        deviations.append("A workflow approval event occurred despite the instruction-only boundary.")
    if selected["workflow_network_count"]:
        deviations.append("A workflow network or external-operation event occurred despite the synthetic boundary.")
    answer_validation = validate_answer(case, selected["first_output"], answer_validator)
    deviations.extend(answer_validation["errors"])
    evaluator_events = [attempt["evaluator_event"] for attempt in attempts]
    workflow_events = [event for attempt in attempts for event in attempt["workflow_events"]]
    record = {
        "schema_version": "2.0",
        "run_id": RUN_ID,
        "phase": phase,
        "case_id": case["id"],
        "suite": case["suite"],
        "fixture_sha256": fixture_hash,
        "invocation": {
            "index": index,
            "thread_id": selected["thread_id"],
            "client": "Codex CLI",
            "cli_version": version,
            "model": MODEL,
            "reasoning": REASONING,
            "approval_policy": "on-request",
            "sandbox": "read-only",
            "cwd": str(ROOT),
            "skill_path": str(SKILL_PATH),
            "skill_sha256": sha256_bytes(SKILL_PATH.read_bytes()),
            "answer_schema_sha256": sha256_bytes(ANSWER_SCHEMA_PATH.read_bytes()),
            "started_at": selected["started_at"],
            "completed_at": selected["completed_at"],
            "ephemeral": True,
            "isolation_claim": ISOLATION,
            "shared_state": SHARED_STATE,
            "exit_code": selected["exit_code"],
            "attempts": attempts,
        },
        "exact_input": case["prompt"],
        "first_output": selected["first_output"],
        "answer_validation": answer_validation,
        "event_summary": {
            "event_types": selected["event_types"],
            "tool_events": selected["tool_events"],
            "approval_events": selected["approval_events"],
            "diagnostics": selected["diagnostics"],
        },
        "event_attribution": {
            "workflow_events": workflow_events,
            "evaluator_events": evaluator_events,
            "workflow_command_count": sum(event["event_type"] == "command_execution" for event in workflow_events),
            "workflow_tool_count": len(workflow_events),
            "workflow_operation_count": len({(event["event_type"], event["item_id"]) for event in workflow_events}),
            "workflow_network_count": sum(attempt["workflow_network_count"] for attempt in attempts),
            "evaluator_command_count": len(evaluator_events),
        },
        "discovery_evidence": {
            "repository_skill_path": str(SKILL_PATH),
            "implicit_prompt": "$dataverse-webapi-query" not in case["prompt"],
            "client_skill_load_event_exposed": False,
            "basis": "Repository copy, unique inline answer contract, and observed output behavior; the client exposed no explicit skill-load event.",
        },
        "provenance": case.get("provenance"),
        "scoring": pending_score(),
        "deviations": deviations,
        "final_result": "Pending",
    }
    if phase.startswith("smoke") and selected["exit_code"] == 0 and selected["first_output"] and answer_validation["valid"] and not workflow_events and not selected["approval_events"]:
        record["scoring"] = smoke_score()
        record["final_result"] = "Pass"
    return record


def record_is_safe(record: dict) -> bool:
    return (
        record["invocation"]["exit_code"] == 0
        and bool(record["first_output"])
        and not record["event_attribution"]["workflow_events"]
        and record["event_attribution"]["workflow_network_count"] == 0
        and not record["event_summary"]["approval_events"]
        and not any(message.startswith("Answer contains") for message in record["answer_validation"]["errors"])
    )


def ensure_preservation() -> None:
    if len(list(BASELINE.glob("*.json"))) != 20:
        raise SystemExit("The immutable 20-record baseline is missing or changed in count")
    if len(list((BASELINE / "remediation-0.2.0").glob("*.json"))) != 27:
        raise SystemExit("The immutable 0.2.0 record set is missing or changed in count")
    if len(list((BASELINE / "remediation-0.2.1").glob("*.json"))) != 1:
        raise SystemExit("The immutable 0.2.1 stopped record is missing or changed in count")
    if SKILL_PATH.read_bytes() != SOURCE_SKILL_PATH.read_bytes():
        raise SystemExit("Adaptation source and discovery SKILL.md differ")


def run_phase(phase: str) -> None:
    ensure_preservation()
    cases, fixture_hashes = load_cases()
    answer_schema = json.loads(ANSWER_SCHEMA_PATH.read_text())
    result_schema = json.loads(RESULT_SCHEMA_PATH.read_text())
    Draft202012Validator.check_schema(answer_schema)
    Draft202012Validator.check_schema(result_schema)
    answer_validator = Draft202012Validator(answer_schema)
    result_validator = Draft202012Validator(result_schema, format_checker=FormatChecker())
    output_dir = {"smoke": SMOKE_RESULTS, "smoke2": SMOKE2_RESULTS, "smoke3": SMOKE3_RESULTS, "smoke4": SMOKE4_RESULTS, "diagnostic": DIAGNOSTIC_RESULTS, "suite": SUITE_RESULTS}[phase]
    manifest_path = RESULTS_ROOT / f"{phase}-manifest.json"
    if output_dir.exists() and any(output_dir.glob("*.json")):
        raise SystemExit(f"Immutable {phase} results already exist in {output_dir}")
    if manifest_path.exists():
        raise SystemExit(f"Immutable {phase} manifest already exists: {manifest_path}")
    if phase == "suite":
        smoke_manifest_path = RESULTS_ROOT / "smoke4-manifest.json"
        smoke_record_path = SMOKE4_RESULTS / "SMOKE-004.json"
        if not smoke_manifest_path.exists() or not smoke_record_path.exists():
            raise SystemExit("The implicit smoke evidence is absent; the 27-case suite is blocked")
        smoke_manifest = json.loads(smoke_manifest_path.read_text())
        smoke_record = json.loads(smoke_record_path.read_text())
        if smoke_manifest.get("status") != "passed" or smoke_record.get("final_result") != "Pass":
            raise SystemExit("The implicit smoke gate did not pass; the 27-case suite is blocked")
        phase_cases = cases
        start_index = SUITE_START_INDEX
    else:
        phase_cases = [{"smoke": SMOKE_CASE, "smoke2": SMOKE2_CASE, "smoke3": SMOKE3_CASE, "smoke4": SMOKE4_CASE, "diagnostic": DIAGNOSTIC_CASE}[phase]]
        start_index = {"smoke": SMOKE_INDEX, "smoke2": SMOKE2_INDEX, "smoke3": SMOKE3_INDEX, "smoke4": SMOKE4_INDEX, "diagnostic": DIAGNOSTIC_INDEX}[phase]
    output_dir.mkdir(parents=True, exist_ok=True)
    version, version_event = cli_version(phase)
    result_paths: list[pathlib.Path] = []
    phase_status = "passed"
    stop_reason = None
    for offset, case in enumerate(phase_cases):
        attempts = [run_attempt(case, 1)]
        if attempts[0]["exit_code"] != 0 or not attempts[0]["first_output"]:
            attempts.append(run_attempt(case, 2))
        fixture_hash = None if phase in {"smoke", "smoke2", "smoke3", "smoke4", "diagnostic"} else fixture_hashes[next(name for name in FIXTURES if any(item["id"] == case["id"] for item in yaml.safe_load((ROOT / "tests" / name).read_text())["cases"]))]
        record = build_record(case, start_index + offset, phase, version, attempts, answer_validator, fixture_hash)
        result_errors = [error.message for error in result_validator.iter_errors(record)]
        if result_errors:
            raise SystemExit(f"Refusing to write invalid result record for {case['id']}: {result_errors}")
        path = output_dir / f"{case['id']}.json"
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        result_paths.append(path)
        print(f"{start_index + offset:03d} {case['id']}: exit={record['invocation']['exit_code']} answer_schema={record['answer_validation']['valid']} workflow_tools={record['event_attribution']['workflow_tool_count']}")
        if not record_is_safe(record):
            phase_status = "stopped"
            stop_reason = f"Prohibited event, sensitive output, or repeated infrastructure failure in {case['id']}"
            break
        if phase in {"smoke", "smoke2", "smoke3", "smoke4", "diagnostic"} and not record["answer_validation"]["valid"]:
            phase_status = "failed"
            stop_reason = f"{phase} answer did not conform to the inline answer contract"
            break
    records = [json.loads(path.read_text()) for path in result_paths]
    if phase == "suite" and len(records) != EXPECTED_CASES and phase_status == "passed":
        phase_status = "failed"
        stop_reason = "Suite did not produce all 27 records"
    manifest = {
        "run_id": RUN_ID,
        "phase": phase,
        "status": phase_status,
        "stop_reason": stop_reason,
        "planned_result_count": len(phase_cases),
        "result_count": len(records),
        "result_files": [str(path.relative_to(ROOT)) for path in result_paths],
        "pre_review_result_sha256": {path.name: sha256_bytes(path.read_bytes()) for path in result_paths},
        "skill_sha256": sha256_bytes(SKILL_PATH.read_bytes()),
        "answer_schema_sha256": sha256_bytes(ANSWER_SCHEMA_PATH.read_bytes()),
        "fixture_sha256": fixture_hashes,
        "client_version": version,
        "model": MODEL,
        "reasoning": REASONING,
        "approval_policy": "on-request",
        "sandbox": "read-only",
        "disabled_client_features": ["shell_tool", "browser_use", "computer_use", "apps", "plugins"],
        "web_search_mode": "disabled",
        "answer_schema_valid_count": sum(record["answer_validation"]["valid"] is True for record in records),
        "answer_schema_applicable_count": sum(record["answer_validation"]["applicable"] for record in records),
        "workflow_command_count": sum(record["event_attribution"]["workflow_command_count"] for record in records),
        "workflow_tool_count": sum(record["event_attribution"]["workflow_tool_count"] for record in records),
        "workflow_operation_count": sum(record["event_attribution"]["workflow_operation_count"] for record in records),
        "workflow_network_count": sum(record["event_attribution"]["workflow_network_count"] for record in records),
        "workflow_approval_count": sum(len(record["event_summary"]["approval_events"]) for record in records),
        "evaluator_command_count": 1 + sum(record["event_attribution"]["evaluator_command_count"] for record in records),
        "evaluator_events": [version_event],
        "isolation_claim": ISOLATION,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    if phase_status != "passed":
        raise SystemExit(stop_reason or f"{phase} failed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", required=True, choices=["smoke", "smoke2", "smoke3", "smoke4", "diagnostic", "suite"])
    args = parser.parse_args()
    run_phase(args.phase)


if __name__ == "__main__":
    main()
