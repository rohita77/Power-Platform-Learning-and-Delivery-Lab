from __future__ import annotations

import re
from datetime import date
from typing import Any

from .abstentions import validate_abstentions
from .carry_forward import validate_result_carry_forward
from .common import canonical_digest, duplicate_id_findings, finding, normalize, schema_findings, walk
from .contradictions import validate_contradictions
from .provenance import validate_provenance


ARTIFACT_PATTERNS = [
    re.compile(r"(?i)\bappPackage/"),
    re.compile(r"(?i)\bmanifest\.json\b"),
    re.compile(r"\bcopilotAgents\b"),
    re.compile(r"\bRemoteMCPServer\b"),
    re.compile(r"\bstatic_template\b"),
    re.compile(r"(?i)\b(?:run|execute|invoke)\s+atk\b"),
]

OUTPUT_BOUNDARY_PATTERNS = [
    re.compile(r"(?i)\b(?:authenticate|sign in|log in|access|discover|inspect|query|connect|invoke|use)\b.{0,60}\b(?:tenant|microsoft 365|power platform|work iq|connector|mcp)\b"),
    re.compile(r"(?i)\b(?:install|run|execute)\b.{0,40}\b(?:agents toolkit|toolkit|\batk\b|work iq|npm|pip|package manager|shell|subprocess)\b"),
    re.compile(r"(?i)\b(?:provision|sideload|deploy|publish)\b.{0,80}\b(?:agent|package|artifact|tenant|environment|microsoft 365|power platform)\b"),
    re.compile(r"(?i)\bbearer\s+[a-z0-9._~+/-]{12,}={0,2}\b"),
    re.compile(r"(?i)\b(?:client_secret|access_token|refresh_token|api_key|password)\s*[:=]\s*\S+"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

PORTABILITY_PATTERNS = [
    re.compile(r"(?i)\b(?:openai|codex) agent skill can be deployed unchanged\b"),
    re.compile(r"(?i)\btoolkit project automatically converts\b"),
    re.compile(r"(?i)\bcopilot studio skills? (?:is|are) the same runtime contract\b"),
    re.compile(r"(?i)\brenam(?:e|ing).{0,60}\b(?:declarative-agent package|microsoft 365 package)\b"),
    re.compile(r"(?i)\bstructural (?:file )?compatibility proves runtime compatibility\b"),
]


def validate_result(document: Any, as_of: date, request: dict[str, Any] | None = None) -> list[dict[str, str]]:
    findings = schema_findings(document, "design-result")
    if not isinstance(document, dict):
        return normalize(findings)
    groups = [
        ("/findings", document.get("findings", [])),
        ("/provenance", document.get("provenance", [])),
        ("/contradictions", document.get("contradictions", [])),
        ("/abstentions", document.get("abstentions", [])),
    ]
    findings.extend(duplicate_id_findings(groups))
    known_findings = {item.get("id") for item in document.get("findings", []) if isinstance(item, dict)}
    for mode_index, mode in enumerate(document.get("modes", [])):
        if not isinstance(mode, dict):
            continue
        for ref_index, ref in enumerate(mode.get("finding_ids", [])):
            if ref not in known_findings:
                findings.append(
                    finding("DAD-BROKEN-REFERENCE", f"/modes/{mode_index}/finding_ids/{ref_index}", "The mode finding reference does not resolve.")
                )
    findings.extend(validate_provenance(document, as_of))
    findings.extend(validate_contradictions(document))
    findings.extend(validate_abstentions(document))
    findings.extend(validate_result_carry_forward(document))
    for path, value in walk(document):
        if not isinstance(value, str):
            continue
        if any(pattern.search(value) for pattern in ARTIFACT_PATTERNS):
            findings.append(
                finding("DAD-FORBIDDEN-MICROSOFT-ARTIFACT", path, "The result contains a forbidden Microsoft runtime artifact or command.")
            )
        if any(pattern.search(value) for pattern in PORTABILITY_PATTERNS):
            findings.append(
                finding("DAD-UNSUPPORTED-PORTABILITY", path, "The result contains an unsupported portability claim.")
            )
        if any(pattern.search(value) for pattern in OUTPUT_BOUNDARY_PATTERNS):
            findings.append(
                finding("DAD-PROHIBITED-OPERATION", path, "The result contains prohibited operational or secret-bearing content.")
            )
    if request is not None:
        if document.get("request_id") != request.get("request_id"):
            findings.append(
                finding("DAD-BROKEN-REFERENCE", "/request_id", "The result does not reference the supplied request.")
            )
        if document.get("request_digest") != canonical_digest(request):
            findings.append(
                finding("DAD-BROKEN-REFERENCE", "/request_digest", "The request digest does not match the canonical request.")
            )
        prior = request.get("carry_forward")
        current = document.get("carry_forward")
        if isinstance(prior, dict) and isinstance(current, dict):
            expected_previous = prior.get("result_ids", [])[-1] if prior.get("result_ids") else None
            if current.get("state_id") != prior.get("state_id"):
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/state_id", "Carry-forward state identity changed."))
            if current.get("sequence") != prior.get("sequence", -1) + 1:
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/sequence", "Carry-forward sequence did not advance exactly once."))
            if current.get("previous_result_id") != expected_previous:
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/previous_result_id", "Carry-forward previous result is inconsistent."))
            if current.get("request_ids") != prior.get("request_ids", []) + [request.get("request_id")]:
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/request_ids", "Complete request lineage was not preserved."))
            if current.get("result_ids") != prior.get("result_ids", []) + [document.get("result_id")]:
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/result_ids", "Complete result lineage was not preserved."))
            if not set(prior.get("evidence_refs", [])).issubset(set(current.get("evidence_refs", []))):
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward/evidence_refs", "Prior evidence lineage was removed."))
            for key in (
                "confirmed_decisions",
                "assumptions",
                "open_items",
                "rejected_decisions",
                "superseded_chronology",
            ):
                prior_items = {item.get("id"): item for item in prior.get(key, []) if isinstance(item, dict)}
                current_items = {item.get("id"): item for item in current.get(key, []) if isinstance(item, dict)}
                for identifier, item in prior_items.items():
                    if current_items.get(identifier) != item:
                        findings.append(
                            finding("DAD-STALE-CARRY-FORWARD", f"/carry_forward/{key}", "Prior carry-forward state was removed or changed without evidence.")
                        )
        elif prior is None and isinstance(current, dict):
            if current.get("sequence") != 0 or current.get("previous_result_id") is not None:
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward", "Initial carry-forward state is inconsistent."))
            if current.get("request_ids") != [request.get("request_id")] or current.get("result_ids") != [document.get("result_id")]:
                findings.append(finding("DAD-STALE-CARRY-FORWARD", "/carry_forward", "Initial lineage must contain only the current request and result."))
    return normalize(findings)
