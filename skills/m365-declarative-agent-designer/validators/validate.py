#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from validators.common import load_json
    from validators.attestation import create_attestation, validate_attestation
    from validators.package import validate_package
    from validators.request import validate_request
    from validators.result import validate_result
else:
    from .common import load_json
    from .attestation import create_attestation, validate_attestation
    from .package import validate_package
    from .request import validate_request
    from .result import validate_result


def emit(findings: list[dict[str, str]]) -> int:
    payload = {"valid": not findings, "findings": findings}
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if not findings else 1


def used_attestation_ids(path: str | None) -> set[str]:
    if path is None:
        return set()
    value: Any = load_json(path)
    if isinstance(value, list):
        return {item for item in value if isinstance(item, str)}
    if isinstance(value, dict):
        items = value.get("used_attestation_ids", [])
        return {item for item in items if isinstance(item, str)}
    return set()


def run_suite() -> int:
    test_file = Path(__file__).resolve().parents[1] / "tests/run_tests.py"
    spec = importlib.util.spec_from_file_location("designer_tests", test_file)
    if spec is None or spec.loader is None:
        return emit([{"code": "DAD-TEST-LOAD", "path": "/tests", "message": "Test suite could not be loaded."}])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main()


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline deterministic designer validator")
    subparsers = parser.add_subparsers(dest="command", required=True)
    request_parser = subparsers.add_parser("request")
    request_parser.add_argument("document")
    request_parser.add_argument("--as-of", default=date.today().isoformat())
    result_parser = subparsers.add_parser("result")
    result_parser.add_argument("document")
    result_parser.add_argument("--request")
    result_parser.add_argument("--attestation")
    result_parser.add_argument("--as-of", default=date.today().isoformat())
    attestation_parser = subparsers.add_parser("attestation")
    attestation_parser.add_argument("document")
    attestation_parser.add_argument("--request", required=True)
    attestation_parser.add_argument("--used-attestations")
    attestation_parser.add_argument("--as-of", default=date.today().isoformat())
    attest_parser = subparsers.add_parser("attest")
    attest_parser.add_argument("request")
    attest_parser.add_argument("--attestation-id", required=True)
    attest_parser.add_argument("--as-of", default=date.today().isoformat())
    subparsers.add_parser("package")
    subparsers.add_parser("suite")
    args = parser.parse_args()
    if args.command == "request":
        return emit(validate_request(load_json(args.document), date.fromisoformat(args.as_of)))
    if args.command == "result":
        request = load_json(args.request) if args.request else None
        attestation = load_json(args.attestation) if args.attestation else None
        return emit(validate_result(load_json(args.document), date.fromisoformat(args.as_of), request, attestation))
    if args.command == "attestation":
        request = load_json(args.request)
        return emit(
            validate_attestation(
                load_json(args.document),
                request,
                date.fromisoformat(args.as_of),
                used_attestation_ids(args.used_attestations),
            )
        )
    if args.command == "attest":
        request = load_json(args.request)
        as_of = date.fromisoformat(args.as_of)
        findings = validate_request(request, as_of)
        if findings:
            return emit(findings)
        attestation = create_attestation(request, args.attestation_id)
        findings = validate_attestation(attestation, request, as_of)
        if findings:
            return emit(findings)
        print(json.dumps(attestation, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    if args.command == "package":
        return emit(validate_package())
    return run_suite()


if __name__ == "__main__":
    raise SystemExit(main())
