from __future__ import annotations

from typing import Any

from .common import CONTRACT_VERSION, duplicate_id_findings, finding, normalize


POSITION_KEYS = [
    "confirmed_decisions",
    "assumptions",
    "open_items",
    "rejected_decisions",
    "superseded_chronology",
]


def validate_request_carry_forward(request: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    carry = request.get("carry_forward")
    if not isinstance(carry, dict):
        return findings
    if carry.get("contract_version") != CONTRACT_VERSION:
        findings.append(
            finding("DAD-INCOMPATIBLE-CARRY-FORWARD", "/carry_forward/contract_version", "The carry-forward contract version is incompatible.")
        )
    if request.get("request_id") in carry.get("request_ids", []):
        findings.append(
            finding("DAD-REPLAYED-REQUEST", "/request_id", "The request identifier has already been processed.")
        )
    continuation = request.get("continuation", {})
    if continuation.get("expected_state_id") != carry.get("state_id") or continuation.get("expected_sequence") != carry.get("sequence"):
        findings.append(
            finding("DAD-STALE-CARRY-FORWARD", "/continuation", "The supplied carry-forward state is stale or mismatched.")
        )
    findings.extend(
        duplicate_id_findings((f"/carry_forward/{key}", carry.get(key, [])) for key in POSITION_KEYS)
    )
    return normalize(findings)


def validate_result_carry_forward(result: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    carry = result.get("carry_forward")
    if not isinstance(carry, dict):
        return findings
    if carry.get("contract_version") != CONTRACT_VERSION:
        findings.append(
            finding("DAD-INCOMPATIBLE-CARRY-FORWARD", "/carry_forward/contract_version", "The carry-forward contract version is incompatible.")
        )
    request_ids = carry.get("request_ids", [])
    result_ids = carry.get("result_ids", [])
    sequence = carry.get("sequence")
    if not request_ids or request_ids[-1] != result.get("request_id"):
        findings.append(
            finding("DAD-BROKEN-REFERENCE", "/carry_forward/request_ids", "Carry-forward lineage must end with the current request.")
        )
    if not result_ids or result_ids[-1] != result.get("result_id"):
        findings.append(
            finding("DAD-BROKEN-REFERENCE", "/carry_forward/result_ids", "Carry-forward lineage must end with the current result.")
        )
    if sequence == 0 and carry.get("previous_result_id") is not None:
        findings.append(
            finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/previous_result_id", "Initial state cannot name a previous result.")
        )
    if sequence == 0 and (len(request_ids) != 1 or len(result_ids) != 1):
        findings.append(
            finding("DAD-STALE-CARRY-FORWARD", "/carry_forward", "Initial lineage must contain exactly one request and one result.")
        )
    if isinstance(sequence, int) and sequence > 0 and (
        len(result_ids) < 2 or carry.get("previous_result_id") != result_ids[-2]
    ):
        findings.append(
            finding("DAD-BROKEN-REFERENCE", "/carry_forward/previous_result_id", "Previous result must resolve as the immediately prior result in lineage.")
        )
    if isinstance(sequence, int) and (
        len(request_ids) != len(result_ids) or sequence != len(result_ids) - 1
    ):
        findings.append(
            finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/sequence", "Sequence and chronological lineage lengths are inconsistent.")
        )
    findings.extend(
        duplicate_id_findings((f"/carry_forward/{key}", carry.get(key, [])) for key in POSITION_KEYS)
    )
    return normalize(findings)
