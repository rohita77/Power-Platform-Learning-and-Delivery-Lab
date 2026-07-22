#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import date
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from validators.common import load_json
    from validators.package import validate_package
    from validators.request import validate_request
    from validators.result import validate_result
else:
    from .common import load_json
    from .package import validate_package
    from .request import validate_request
    from .result import validate_result


def emit(findings: list[dict[str, str]]) -> int:
    payload = {"valid": not findings, "findings": findings}
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if not findings else 1


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
    result_parser.add_argument("--as-of", default=date.today().isoformat())
    subparsers.add_parser("package")
    subparsers.add_parser("suite")
    args = parser.parse_args()
    if args.command == "request":
        return emit(validate_request(load_json(args.document), date.fromisoformat(args.as_of)))
    if args.command == "result":
        request = load_json(args.request) if args.request else None
        return emit(validate_result(load_json(args.document), date.fromisoformat(args.as_of), request))
    if args.command == "package":
        return emit(validate_package())
    return run_suite()


if __name__ == "__main__":
    raise SystemExit(main())
