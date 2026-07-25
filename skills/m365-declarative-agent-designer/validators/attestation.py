from __future__ import annotations

import re
from datetime import date
from typing import Any, Iterable

from .common import canonical_digest, finding, normalize, schema_findings
from .request import validate_request


ATTESTATION_VERSION = "0.2.0"
VALIDATOR_ID = "m365-declarative-agent-designer-request-validator"
VALIDATOR_VERSION = "0.2.0"
ZERO_DIGEST = "0" * 64
DIGEST_PATTERN = re.compile(r"^[a-f0-9]{64}$")
AUTHORITY_KEYS = {
    "authority",
    "instructions",
    "network",
    "permissions",
    "policy_override",
    "tenant",
    "tool_access",
    "tools",
    "deployment",
}


def create_attestation(request: dict[str, Any], attestation_id: str) -> dict[str, Any]:
    return {
        "attestation_version": ATTESTATION_VERSION,
        "attestation_id": attestation_id,
        "request_id": request.get("request_id"),
        "request_digest": canonical_digest(request),
        "validation_status": "passed",
        "validator_id": VALIDATOR_ID,
        "validator_version": VALIDATOR_VERSION,
        "data_classification": request.get("classification"),
        "boundary_status": "permitted",
        "scope": "single-inference",
    }


def validate_attestation(
    document: Any,
    request: dict[str, Any] | None,
    as_of: date,
    used_attestation_ids: Iterable[str] = (),
) -> list[dict[str, str]]:
    if document is None:
        return [finding("DAD-ATTESTATION-MISSING", "/attestation", "A validated host attestation is required before inference.")]
    findings = schema_findings(document, "host-validation-attestation")
    if not isinstance(document, dict):
        return normalize(findings)
    if document.get("attestation_version") != ATTESTATION_VERSION:
        findings.append(
            finding("DAD-ATTESTATION-VERSION", "/attestation_version", "The host attestation version is unsupported.")
        )
    if document.get("validation_status") != "passed":
        findings.append(
            finding("DAD-ATTESTATION-VALIDATION", "/validation_status", "Request validation must pass before inference.")
        )
    digest = document.get("request_digest")
    if not isinstance(digest, str) or not DIGEST_PATTERN.fullmatch(digest):
        findings.append(
            finding("DAD-ATTESTATION-DIGEST", "/request_digest", "The attested request digest must be lowercase SHA-256.")
        )
    elif digest == ZERO_DIGEST:
        findings.append(
            finding("DAD-ATTESTATION-PLACEHOLDER-DIGEST", "/request_digest", "A placeholder request digest is prohibited.")
        )
    if document.get("data_classification") not in {"public", "synthetic"}:
        findings.append(
            finding("DAD-ATTESTATION-CLASSIFICATION", "/data_classification", "Only public or synthetic data may be attested.")
        )
    if document.get("boundary_status") != "permitted":
        findings.append(
            finding("DAD-ATTESTATION-BOUNDARY", "/boundary_status", "The request boundary must be permitted before inference.")
        )
    if document.get("scope") != "single-inference":
        findings.append(
            finding("DAD-ATTESTATION-SCOPE", "/scope", "The attestation scope must be single-inference.")
        )
    prohibited = sorted(set(document) & AUTHORITY_KEYS)
    for key in prohibited:
        findings.append(
            finding("DAD-ATTESTATION-AUTHORITY", f"/{key}", "Attestation fields cannot grant authority or override policy.")
        )
    if document.get("attestation_id") in set(used_attestation_ids):
        findings.append(
            finding("DAD-ATTESTATION-REPLAY", "/attestation_id", "A single-inference attestation cannot be reused.")
        )
    if request is not None:
        request_findings = validate_request(request, as_of)
        if request_findings:
            findings.append(
                finding("DAD-ATTESTATION-REQUEST-INVALID", "/request", "The attested request failed deterministic validation.")
            )
        if document.get("request_id") != request.get("request_id"):
            findings.append(
                finding("DAD-ATTESTATION-REQUEST-ID", "/request_id", "The attestation does not reference the exact request.")
            )
        if isinstance(digest, str) and digest != canonical_digest(request):
            findings.append(
                finding("DAD-ATTESTATION-DIGEST-MISMATCH", "/request_digest", "The attested digest does not match the canonical request.")
            )
        if document.get("data_classification") != request.get("classification"):
            findings.append(
                finding("DAD-ATTESTATION-CLASSIFICATION", "/data_classification", "The attested classification does not match the request.")
            )
    return normalize(findings)
