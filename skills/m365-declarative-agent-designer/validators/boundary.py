from __future__ import annotations

import re
from typing import Any

from .common import finding, normalize, walk


FORBIDDEN_KEYS = {
    "password",
    "secret",
    "client_secret",
    "access_token",
    "refresh_token",
    "api_key",
    "connection_string",
    "tenant_url",
    "tenant_id",
    "environment_url",
}

FORBIDDEN_PATTERNS = [
    re.compile(r"(?i)\b(?:install|invoke|run|execute)\b.{0,40}\b(?:agents toolkit|toolkit|\batk\b|work iq|npm|pip|package manager|shell|subprocess)\b"),
    re.compile(r"(?i)\b(?:authenticate|sign in|log in|access|discover|inspect|query|connect)\b.{0,50}\b(?:tenant|microsoft 365|power platform|work iq|connector|mcp)\b"),
    re.compile(r"(?i)\b(?:provision|sideload|deploy|publish)\b"),
    re.compile(r"(?i)\b(?:ignore|override|bypass|replace|weaken)\b.{0,50}\b(?:security|orchestration|evidence|status|tool|output contract|schema|approval)\b"),
    re.compile(r"(?i)https://[a-z0-9.-]+\.(?:sharepoint\.com|crm\d*\.dynamics\.com)"),
]


def validate_boundary(document: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(document, dict):
        return [finding("DAD-SCHEMA-INVALID", "/", "The request must be a JSON object.")]
    if document.get("classification") not in {"public", "synthetic"}:
        findings.append(
            finding("DAD-INVALID-CLASSIFICATION", "/classification", "Only public or synthetic input is permitted.")
        )
    if document.get("zone") != "personal-openai":
        findings.append(
            finding("DAD-INVALID-CLASSIFICATION", "/zone", "Only the personal-openai zone is permitted.")
        )
    if document.get("cross_zone_transfer") != "prohibited":
        findings.append(
            finding("DAD-PROHIBITED-OPERATION", "/cross_zone_transfer", "Cross-zone transfer is prohibited.")
        )
    for path, value in walk(document):
        key = path.rsplit("/", 1)[-1].lower()
        if key in FORBIDDEN_KEYS:
            findings.append(
                finding("DAD-PROHIBITED-OPERATION", path, "A prohibited credential or tenant field is present.")
            )
        if isinstance(value, str) and any(pattern.search(value) for pattern in FORBIDDEN_PATTERNS):
            findings.append(
                finding("DAD-PROHIBITED-OPERATION", path, "The request contains a prohibited operation or policy override.")
            )
    return normalize(findings)
