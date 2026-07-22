from __future__ import annotations

from typing import Any

from .common import finding, normalize


def validate_abstentions(result: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if result.get("status") == "Complete" and result.get("abstentions"):
        findings.append(
            finding("DAD-INVALID-ABSTENTION", "/status", "A Complete result cannot contain abstentions.")
        )
    known = {
        "finding_ids": {item.get("id") for item in result.get("findings", []) if isinstance(item, dict)},
        "provenance_ids": {item.get("id") for item in result.get("provenance", []) if isinstance(item, dict)},
        "contradiction_ids": {item.get("id") for item in result.get("contradictions", []) if isinstance(item, dict)},
    }
    for index, item in enumerate(result.get("abstentions", [])):
        if not isinstance(item, dict):
            continue
        total_refs = sum(len(item.get(key, [])) for key in known)
        if total_refs == 0:
            findings.append(
                finding("DAD-INVALID-ABSTENTION", f"/abstentions/{index}", "An abstention requires supporting references.")
            )
        for key, identifiers in known.items():
            for ref_index, ref in enumerate(item.get(key, [])):
                if ref not in identifiers:
                    findings.append(
                        finding("DAD-BROKEN-REFERENCE", f"/abstentions/{index}/{key}/{ref_index}", "The abstention reference does not resolve.")
                    )
        if item.get("reason") == "contradictory-evidence" and not item.get("contradiction_ids"):
            findings.append(
                finding("DAD-INVALID-ABSTENTION", f"/abstentions/{index}/contradiction_ids", "Contradictory-evidence abstention requires a contradiction reference.")
            )
        if item.get("reason") == "stale-evidence" and not item.get("provenance_ids"):
            findings.append(
                finding("DAD-INVALID-ABSTENTION", f"/abstentions/{index}/provenance_ids", "Stale-evidence abstention requires a provenance reference.")
            )
    return normalize(findings)
