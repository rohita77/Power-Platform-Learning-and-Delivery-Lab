from __future__ import annotations

from datetime import date
from typing import Any

from .boundary import validate_boundary
from .carry_forward import validate_request_carry_forward
from .common import duplicate_id_findings, finding, normalize, schema_findings


def validate_request(document: Any, as_of: date) -> list[dict[str, str]]:
    findings = validate_boundary(document)
    findings.extend(schema_findings(document, "design-request"))
    if not isinstance(document, dict):
        return normalize(findings)
    groups = [("/sources", document.get("sources", []))]
    groups.extend(
        (f"/{key}", document.get(key, []))
        for key in ("settled_decisions", "assumptions", "open_questions")
    )
    findings.extend(duplicate_id_findings(groups))
    source_ids = {item.get("id") for item in document.get("sources", []) if isinstance(item, dict)}
    for key in ("settled_decisions", "assumptions", "open_questions"):
        for index, item in enumerate(document.get(key, [])):
            if not isinstance(item, dict):
                continue
            for ref_index, ref in enumerate(item.get("evidence_refs", [])):
                if isinstance(ref, str) and ref.startswith("PRV-") and ref not in source_ids:
                    findings.append(
                        finding("DAD-BROKEN-REFERENCE", f"/{key}/{index}/evidence_refs/{ref_index}", "The evidence reference does not resolve.")
                    )
    findings.extend(validate_request_carry_forward(document))
    return normalize(findings)
