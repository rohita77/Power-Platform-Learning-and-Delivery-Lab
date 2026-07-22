from __future__ import annotations

from typing import Any

from .common import finding, normalize


def validate_contradictions(result: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    known_findings = {item.get("id") for item in result.get("findings", []) if isinstance(item, dict)}
    abstained = {
        ref: item.get("reason")
        for item in result.get("abstentions", [])
        if isinstance(item, dict)
        for ref in item.get("contradiction_ids", [])
    }
    for index, item in enumerate(result.get("contradictions", [])):
        if not isinstance(item, dict):
            continue
        for ref_index, ref in enumerate(item.get("finding_ids", [])):
            if ref not in known_findings:
                findings.append(
                    finding("DAD-BROKEN-REFERENCE", f"/contradictions/{index}/finding_ids/{ref_index}", "The finding reference does not resolve.")
                )
        if item.get("status") == "unresolved":
            if abstained.get(item.get("id")) != "contradictory-evidence" or result.get("status") == "Complete":
                findings.append(
                    finding("DAD-UNRESOLVED-CONTRADICTION", f"/contradictions/{index}", "An unresolved contradiction requires Open status and a contradictory-evidence abstention.")
                )
        elif item.get("status") == "resolved" and not item.get("resolution"):
            findings.append(
                finding("DAD-UNRESOLVED-CONTRADICTION", f"/contradictions/{index}/resolution", "A resolved contradiction requires a resolution statement.")
            )
    return normalize(findings)
