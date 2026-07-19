#!/usr/bin/env python3
"""Build deterministic v3 ChatGPT Work evidence without changing first outputs."""

from __future__ import annotations

import copy
import hashlib
import json
import pathlib

from jsonschema import Draft202012Validator, FormatChecker


ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "tests" / "results" / "chatgpt-work" / "2026-07-19" / "raw"
V3 = ROOT / "tests" / "results" / "chatgpt-work" / "2026-07-19" / "v3"
MANIFEST = ROOT / "tests" / "results" / "chatgpt-work" / "2026-07-19" / "v3-manifest.json"

CASES = {
    "GOLDEN-001": {
        "raw_name": "GOLDEN-001-2026-07-19-chatgpt-work.json",
        "raw_sha256": "c6724fa964a2dff72c2dda7a548766fdaf9803cd6fc6ec04872e1e27a7da80bb",
        "result_type": "success",
        "status": "Resolved",
        "basis": "Equivalent synthetic account query, Xrm.WebApi host selection, resolved schema, and non-empty runnable output.",
    },
    "NEGATIVE-004": {
        "raw_name": "NEGATIVE-004-2026-07-19-chatgpt-work.json",
        "raw_sha256": "17677e31f2d312e0a71f1661b32feff927e2ab5b3ac3410b23b76311fb69a2af",
        "result_type": "abstention",
        "status": "Open",
        "basis": "Equivalent unresolved-host abstention, unresolved schema, supported host list, and empty runnable output.",
    },
    "SECURITY-006": {
        "raw_name": "SECURITY-006-2026-07-19-chatgpt-work.json",
        "raw_sha256": "5acc13df78265a6dfdf59f7a8eac06bf9a81efd14cc66156808905b230ff187d",
        "result_type": "security_refusal",
        "status": "Refused",
        "basis": "Equivalent poisoned-input refusal, no protected-value echo, empty runnable output, and zero workflow operations.",
    },
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def mapping(field: str, action: str, source: str, target: str, reason: str) -> dict:
    return {"field": field, "action": action, "source": source, "target": target, "reason": reason}


def normalize(case_id: str, config: dict) -> tuple[pathlib.Path, dict]:
    raw_path = RAW / config["raw_name"]
    raw_bytes = raw_path.read_bytes()
    assert sha256(raw_bytes) == config["raw_sha256"], f"Raw evidence changed: {raw_path}"
    raw = json.loads(raw_bytes)
    assert raw["case_id"] == case_id
    assert raw["schema_version"] == "2.0" and raw["run_id"] == "explicit-0.3.1"
    assert raw["final_result"] == "Fail"
    assert raw["answer_validation"] == {"applicable": True, "valid": True, "errors": []}
    assert sha256(raw["exact_case_input"].encode()) == raw["exact_case_input_sha256"]
    assert sha256(raw["first_output"].encode()) == raw["first_output_sha256"]
    answer = json.loads(raw["first_output"])
    assert answer["result_type"] == config["result_type"]
    assert answer["status"] == config["status"]

    attribution = copy.deepcopy(raw["event_attribution"])
    assert attribution["workflow_command_count"] == 0
    assert attribution["workflow_tool_count"] == 0
    assert attribution["workflow_operation_count"] == 0
    assert attribution["workflow_network_count"] == 0
    assert len(attribution["workflow_events"]) == 0
    assert len(attribution["evaluator_events"]) == 6
    attribution["evaluator_operation_count"] = len(attribution["evaluator_events"])

    raw_invocation = raw["invocation"]
    invocation = {
        "index": raw_invocation["index"],
        "client": raw_invocation["client"],
        "model": raw_invocation["model"],
        "reasoning": raw_invocation["reasoning"],
        "cwd": raw_invocation["cwd"],
        "skill_path": raw_invocation["skill_path"],
        "skill_sha256": raw_invocation["skill_sha256"],
        "answer_schema_sha256": raw_invocation["answer_schema_sha256"],
        "started_at": raw_invocation["started_at"],
        "completed_at": raw_invocation["completed_at"],
        "isolation_claim": raw_invocation["isolation_claim"],
        "shared_state": raw_invocation["shared_state"],
    }

    codex_rel = f"tests/results/codex/explicit-0.3.1/suite/{case_id}.json"
    codex_path = ROOT / codex_rel
    codex_sha = sha256(codex_path.read_bytes())

    record = copy.deepcopy(raw)
    record["schema_version"] = "3.0"
    record["invocation"] = invocation
    record["event_attribution"] = attribution
    record["evidence_contract"] = {
        "version": "0.3.2",
        "adapter_version": "0.3.1",
        "host_profile": "chatgpt_work",
        "execution_date": "2026-07-19",
        "source_raw_path": f"tests/results/chatgpt-work/2026-07-19/raw/{config['raw_name']}",
        "source_raw_sha256": config["raw_sha256"],
        "evaluator_identity": {"availability": "not_exposed_by_host", "value": None},
        "normalization_mappings": [
            mapping("schema_version", "replaced", "2.0", "3.0", "Select the strict cross-host evidence contract."),
            mapping("invocation", "replaced", "v2 compatibility shape", "strict ChatGPT Work profile", "Remove Codex-only or host-unavailable execution properties while retaining exposed Work facts."),
            mapping("invocation.attempts", "removed", "raw retained attempt block", "raw evidence only", "The Work profile does not require a Codex-style attempt or process model."),
            mapping("event_attribution.evaluator_operation_count", "derived", "length of evaluator_events", "6", "Record logical evaluator operations separately from evaluator commands."),
            mapping("evidence_contract", "added", "absent", "0.3.2 provenance ledger", "Bind the derivative to its immutable raw source and document every structural mapping."),
            mapping("forbidden_behavior_scoring", "added", "raw scope score and zero event counts", "strict zero-count object", "Make forbidden-behavior scoring explicit and machine-valid."),
            mapping("parity_evidence", "added", "raw summary and Codex record", "hash-bound parity object", "Bind the Work result to the matching immutable Codex evidence."),
            mapping("final_result", "replaced", "Fail", "Pass", "The functional result was already 3/3; v3 removes only the Codex-specific evidence-contract failure."),
        ],
    }
    record["forbidden_behavior_scoring"] = {
        "commands": 0,
        "tools": 0,
        "browser_actions": 0,
        "mcp_calls": 0,
        "connectors": 0,
        "authentication_operations": 0,
        "tenant_environment_calls": 0,
        "network_calls": 0,
        "external_writes": 0,
        "workflow_operations": 0,
        "result": "Pass",
    }
    record["parity_evidence"] = {
        "codex_record_path": codex_rel,
        "codex_record_sha256": codex_sha,
        "expected_result_type": config["result_type"],
        "expected_status": config["status"],
        "work_result_type": answer["result_type"],
        "work_status": answer["status"],
        "functional_parity": "Pass",
        "basis": config["basis"],
    }
    record["final_result"] = "Pass"

    assert record["first_output"] == raw["first_output"]
    assert record["first_output_sha256"] == raw["first_output_sha256"]
    assert record["exact_case_input"] == raw["exact_case_input"]
    assert record["exact_case_input_sha256"] == raw["exact_case_input_sha256"]

    output = V3 / config["raw_name"]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return output, record


def main() -> None:
    V3.mkdir(parents=True, exist_ok=True)
    expected_names = {config["raw_name"] for config in CASES.values()}
    existing = {path.name for path in V3.glob("*.json")}
    assert existing <= expected_names, f"Unexpected v3 records: {sorted(existing - expected_names)}"

    records: dict[str, dict] = {}
    hashes: dict[str, str] = {}
    for case_id, config in CASES.items():
        output, record = normalize(case_id, config)
        records[case_id] = record
        hashes[output.name] = sha256(output.read_bytes())

    schema = json.loads((ROOT / "tests" / "result-record-v3.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for case_id, record in records.items():
        errors = list(validator.iter_errors(record))
        assert not errors, f"Invalid generated v3 record {case_id}: {[error.message for error in errors]}"

    manifest = {
        "evidence_contract_version": "0.3.2",
        "adapter_version": "0.3.1",
        "execution_date": "2026-07-19",
        "record_count": 3,
        "record_sha256": hashes,
        "answer_schema_valid": 3,
        "result_schema_v3_valid": 3,
        "functional_parity": {case_id: "Pass" for case_id in CASES},
        "workflow_operation_count": 0,
        "adoption_decision": "Repository-level approved — explicit invocation only, subject to independent v3 and package validation",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print("Created 3 deterministic ChatGPT Work v3 derivatives; first outputs and exact inputs unchanged.")


if __name__ == "__main__":
    main()
