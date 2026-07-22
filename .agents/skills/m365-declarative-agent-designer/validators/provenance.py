from __future__ import annotations

from datetime import date
from typing import Any

from .common import finding, normalize


def validate_provenance(result: dict[str, Any], as_of: date) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    provenance = result.get("provenance", [])
    known = {item.get("id") for item in provenance if isinstance(item, dict)}
    expired: set[str] = set()
    for item in provenance:
        if not isinstance(item, dict):
            continue
        try:
            revalidate = date.fromisoformat(item.get("revalidate_on", ""))
        except ValueError:
            continue
        if item.get("status") == "expired" or revalidate < as_of:
            identifier = item.get("id")
            if isinstance(identifier, str):
                expired.add(identifier)
    stale_abstentions = {
        ref
        for item in result.get("abstentions", [])
        if isinstance(item, dict) and item.get("reason") == "stale-evidence"
        for ref in item.get("provenance_ids", [])
    }
    for index, item in enumerate(result.get("findings", [])):
        if not isinstance(item, dict):
            continue
        for ref_index, ref in enumerate(item.get("provenance_ids", [])):
            if ref not in known:
                findings.append(
                    finding("DAD-BROKEN-REFERENCE", f"/findings/{index}/provenance_ids/{ref_index}", "The provenance reference does not resolve.")
                )
            if item.get("evidence_label") == "Confirmed" and ref in expired:
                findings.append(
                    finding("DAD-EXPIRED-PROVENANCE", f"/findings/{index}/provenance_ids/{ref_index}", "A Confirmed finding cannot rely on expired provenance.")
                )
    for index, item in enumerate(provenance):
        identifier = item.get("id") if isinstance(item, dict) else None
        if identifier in expired and identifier not in stale_abstentions:
            findings.append(
                finding("DAD-EXPIRED-PROVENANCE", f"/provenance/{index}/revalidate_on", "Expired provenance requires an Open finding and stale-evidence abstention.")
            )
    return normalize(findings)
