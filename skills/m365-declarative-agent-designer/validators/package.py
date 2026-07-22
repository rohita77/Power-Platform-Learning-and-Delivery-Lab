from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from .common import PACKAGE_ROOT, check_schema_documents, finding, load_json, normalize


ALLOWED_TOP = {
    "SKILL.md",
    "CHANGELOG.md",
    "ROLLBACK.md",
    "schemas",
    "validators",
    "adapters",
    "tests",
}
FORBIDDEN_NAMES = {
    "appPackage",
    "manifest.json",
    ".env",
    "connections.json",
    "deployment",
    "mcp",
    "copilot-studio",
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\bbearer\s+[a-z0-9._~+/-]{20,}={0,2}\b"),
]


def compare_adapter_contracts(contracts: list[dict]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    semantic_keys = {
        "contract_version",
        "input_schema",
        "output_schema",
        "invocation",
        "mapping",
        "methodology_override",
        "policy_override",
        "network_allowed",
        "official_work_iq_plugin_compatibility",
        "runtime_evaluation_status",
    }
    if {key: contracts[0].get(key) for key in semantic_keys} != {key: contracts[1].get(key) for key in semantic_keys}:
        findings.append(
            finding("DAD-ADAPTER-DIVERGENCE", "/adapters", "Host adapters diverge semantically.")
        )
    required_values = {
        "contract_version": "0.1.0",
        "input_schema": "../schemas/design-request.schema.json",
        "output_schema": "../schemas/design-result.schema.json",
        "invocation": "explicit-user-trigger",
        "mapping": "identity",
        "methodology_override": False,
        "policy_override": False,
        "network_allowed": False,
        "official_work_iq_plugin_compatibility": "not-claimed",
        "runtime_evaluation_status": "untested",
    }
    for index, contract in enumerate(contracts):
        if any(contract.get(key) != value for key, value in required_values.items()):
            findings.append(
                finding("DAD-ADAPTER-DIVERGENCE", f"/adapters/{index}", "Adapter safety values are not fail-closed.")
            )
    return findings


def validate_adapters(root: Path = PACKAGE_ROOT) -> list[dict[str, str]]:
    paths = [root / "adapters/codex.contract.json", root / "adapters/chatgpt-work.contract.json"]
    return compare_adapter_contracts([load_json(path) for path in paths])


def validate_package(root: Path = PACKAGE_ROOT) -> list[dict[str, str]]:
    findings = check_schema_documents()
    top = {path.name for path in root.iterdir() if path.name != "agents"}
    unexpected = sorted(top - ALLOWED_TOP)
    for name in unexpected:
        findings.append(finding("DAD-PACKAGE-ALLOWLIST", f"/{name}", "File or directory is outside the package allowlist."))
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        display = "/" + relative.as_posix()
        if path.is_symlink():
            findings.append(finding("DAD-PACKAGE-SYMLINK", display, "Symlinks are forbidden."))
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix in {".pyc", ".pfx", ".pem", ".key"} or path.name == "__pycache__":
            findings.append(finding("DAD-PACKAGE-FORBIDDEN", display, "A forbidden artifact is present."))
        if not path.is_file():
            continue
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                findings.append(finding("DAD-JSON-PARSE", display, "JSON parsing failed."))
        if path.suffix in {".md", ".py", ".json", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8")
            if any(pattern.search(text) for pattern in SECRET_PATTERNS):
                findings.append(finding("DAD-SECRET-MATERIAL", display, "Potential secret material is present."))
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\n") or "\n---\n" not in skill_text[4:]:
        findings.append(finding("DAD-SKILL-FRONTMATTER", "/SKILL.md", "SKILL frontmatter is missing."))
    else:
        frontmatter = skill_text.split("---", 2)[1]
        parsed = yaml.safe_load(frontmatter)
        if set(parsed or {}) != {"name", "description"}:
            findings.append(finding("DAD-SKILL-FRONTMATTER", "/SKILL.md", "SKILL frontmatter fields are invalid."))
    findings.extend(validate_adapters(root))
    return normalize(findings)
