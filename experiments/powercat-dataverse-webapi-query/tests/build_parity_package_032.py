#!/usr/bin/env python3
"""Build the deterministic 0.3.2 cross-host evidence package."""

from __future__ import annotations

import hashlib
import json
import pathlib
import shutil
import tempfile
import zipfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "tests" / "results" / "chatgpt-work" / "2026-07-19"
PACKAGE_NAME = "powercat-dataverse-work-parity-0.3.2"
ZIP_PATH = ROOT / f"{PACKAGE_NAME}.zip"
SIDECAR_MANIFEST = EVIDENCE / "package-0.3.2-MANIFEST.sha256"
SIDECAR_PROVENANCE = EVIDENCE / "package-0.3.2-provenance.json"
FIXED_ZIP_TIME = (2026, 7, 19, 0, 0, 0)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def copy_file(package_root: pathlib.Path, source: pathlib.Path, destination: str) -> None:
    target = package_root / destination
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_tree(package_root: pathlib.Path, source: pathlib.Path, destination: str) -> None:
    shutil.copytree(source, package_root / destination)


def write_manifest(package_root: pathlib.Path) -> tuple[pathlib.Path, int]:
    manifest_path = package_root / "MANIFEST.sha256"
    files = sorted(
        path for path in package_root.rglob("*")
        if path.is_file() and path.name != "MANIFEST.sha256" and not path.name.endswith(".zip")
    )
    lines = [f"{sha256(path.read_bytes())}  ./{path.relative_to(package_root).as_posix()}" for path in files]
    manifest_path.write_text("\n".join(lines) + "\n")
    return manifest_path, len(files)


def write_zip(package_root: pathlib.Path) -> None:
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(package_root.rglob("*")):
            if not path.is_file():
                continue
            arcname = f"{PACKAGE_NAME}/{path.relative_to(package_root).as_posix()}"
            info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="powercat-parity-032-") as temporary:
        package_root = pathlib.Path(temporary) / PACKAGE_NAME
        package_root.mkdir()

        for name in ["README.md", "compatibility-report.md", "changelog.md"]:
            copy_file(package_root, ROOT / name, name)
        copy_tree(package_root, ROOT / "adapted-skill" / "dataverse-webapi-query", "skill")
        for name in [
            "answer-output.schema.json",
            "result-record-v2.schema.json",
            "result-record-v3.schema.json",
            "golden-cases.yaml",
            "negative-cases.yaml",
            "security-cases.yaml",
        ]:
            source = ROOT / "tests" / name
            if name == "answer-output.schema.json":
                source = ROOT / "adapted-skill" / "dataverse-webapi-query" / "references" / name
            copy_file(package_root, source, f"tests/{name}")

        copy_tree(package_root, ROOT / "tests" / "results" / "codex" / "explicit-0.3.1", "codex-results/explicit-0.3.1")
        copy_tree(package_root, EVIDENCE / "raw", "chatgpt-work/raw")
        copy_tree(package_root, EVIDENCE / "v3", "chatgpt-work/v3")
        copy_tree(package_root, EVIDENCE / "historical", "chatgpt-work/historical")
        copy_file(package_root, EVIDENCE / "README.md", "chatgpt-work/README.md")
        copy_file(package_root, EVIDENCE / "raw-copy-provenance.json", "chatgpt-work/raw-copy-provenance.json")
        copy_file(package_root, EVIDENCE / "v3-manifest.json", "chatgpt-work/v3-manifest.json")

        validation_summary = {
            "evidence_contract_version": "0.3.2",
            "adapter_version": "0.3.1",
            "adapter_behavior_changed": False,
            "codex_v3_profile": {"valid": 29, "total": 29},
            "chatgpt_work_v3_profile": {"valid": 3, "total": 3},
            "answer_schema": {"valid": 32, "total": 32},
            "work_functional_parity": {"valid": 3, "total": 3},
            "workflow_operation_failures": 0,
            "adoption_decision": "Repository-level approved — explicit invocation only",
        }
        (package_root / "validation-summary.json").write_text(json.dumps(validation_summary, indent=2) + "\n")

        manifest_path, entry_count = write_manifest(package_root)
        manifest_bytes = manifest_path.read_bytes()
        SIDECAR_MANIFEST.write_bytes(manifest_bytes)
        write_zip(package_root)

    provenance = {
        "package": ZIP_PATH.name,
        "evidence_contract_version": "0.3.2",
        "manifest_entry_count": entry_count,
        "manifest_sha256": sha256(SIDECAR_MANIFEST.read_bytes()),
        "manifest_exclusions": ["MANIFEST.sha256", ZIP_PATH.name, "temporary files"],
        "zip_sha256": sha256(ZIP_PATH.read_bytes()),
        "zip_size_bytes": ZIP_PATH.stat().st_size,
        "deterministic_zip_timestamp": "2026-07-19T00:00:00",
    }
    SIDECAR_PROVENANCE.write_text(json.dumps(provenance, indent=2) + "\n")
    print(f"Created {ZIP_PATH.name} with {entry_count} manifest entries; ZIP SHA-256 {provenance['zip_sha256']}")


if __name__ == "__main__":
    main()
