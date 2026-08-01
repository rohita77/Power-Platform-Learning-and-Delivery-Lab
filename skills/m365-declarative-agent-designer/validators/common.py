from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker, RefResolver


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_ROOT = PACKAGE_ROOT / "schemas"
CONTRACT_VERSION = "0.1.0"
PACKAGE_VERSION = "0.2.0-rc4"


def finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path or "/", "message": message}


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def load_json(path: Path | str) -> Any:
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas = {
        "finding-provenance": load_json(SCHEMA_ROOT / "finding-provenance.schema.json"),
        "design-request": load_json(SCHEMA_ROOT / "design-request.schema.json"),
        "design-result": load_json(SCHEMA_ROOT / "design-result.schema.json"),
        "host-validation-attestation": load_json(SCHEMA_ROOT / "host-validation-attestation.schema.json"),
    }
    return schemas


def check_schema_documents() -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for name, schema in load_schemas().items():
        try:
            Draft202012Validator.check_schema(schema)
        except Exception:
            findings.append(
                finding("DAD-SCHEMA-META-INVALID", f"/schemas/{name}", "Schema meta-validation failed.")
            )
    return findings


def _json_path(parts: Iterable[Any]) -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped) if escaped else "/"


def schema_findings(document: Any, schema_name: str) -> list[dict[str, str]]:
    schemas = load_schemas()
    schema = schemas[schema_name]
    store = {item["$id"]: item for item in schemas.values()}
    resolver = RefResolver.from_schema(schema, store=store)
    validator = Draft202012Validator(
        schema, resolver=resolver, format_checker=FormatChecker()
    )
    findings: list[dict[str, str]] = []
    for error in sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path)):
        path = _json_path(error.absolute_path)
        code = "DAD-SCHEMA-INVALID"
        message = "The value does not conform to the canonical contract."
        if error.validator == "required":
            missing = "required field"
            if "'" in error.message:
                missing = error.message.split("'", 2)[1]
            path = (path.rstrip("/") + "/" + missing) if path != "/" else "/" + missing
            code = "DAD-MISSING-FIELD"
            message = "A required field is missing."
        elif error.validator == "const" and path.endswith("contract_version"):
            code = "DAD-SCHEMA-VERSION"
            message = "The contract version is unsupported."
        elif path.endswith("/classification") or path.endswith("/zone") or path.endswith("/cross_zone_transfer"):
            code = "DAD-INVALID-CLASSIFICATION"
            message = "The classification or zone boundary is invalid."
        findings.append(finding(code, path, message))
    return normalize(findings)


def walk(value: Any, path: str = "") -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key in sorted(value):
            child = f"{path}/{str(key).replace('~', '~0').replace('/', '~1')}"
            yield child, value[key]
            yield from walk(value[key], child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child = f"{path}/{index}"
            yield child, item
            yield from walk(item, child)


def duplicate_id_findings(groups: Iterable[tuple[str, list[dict[str, Any]]]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    findings: list[dict[str, str]] = []
    for base, items in groups:
        for index, item in enumerate(items):
            identifier = item.get("id") if isinstance(item, dict) else None
            if isinstance(identifier, str):
                if identifier in seen:
                    findings.append(
                        finding("DAD-DUPLICATE-ID", f"{base}/{index}/id", "A stable identifier is duplicated.")
                    )
                seen.add(identifier)
    return findings


def normalize(findings: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    unique = {(item["code"], item["path"], item["message"]): item for item in findings}
    return [unique[key] for key in sorted(unique)]
