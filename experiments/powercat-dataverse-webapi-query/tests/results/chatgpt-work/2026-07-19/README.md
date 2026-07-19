# ChatGPT Work parity evidence — 2026-07-19

This directory closes evidence-contract remediation 0.3.2 without changing the tested adapter, inputs, first outputs, or prior evidence.

- `raw/` contains the three downloaded Work result records and final 0.3.1 Work summary byte-for-byte.
- `historical/` retains the original invalid self-hashing 0.3.1 package manifest.
- `raw-copy-provenance.json` records source and destination SHA-256 values.
- `v3/` contains deterministic Work derivatives under the strict ChatGPT Work profile in `tests/result-record-v3.schema.json`.
- `v3-manifest.json` binds the derivatives to their hashes and scorecard.
- `package-0.3.2-MANIFEST.sha256` is the corrected package manifest sidecar; it excludes the manifest itself, the ZIP, and temporary files.
- `package-0.3.2-provenance.json` records the final deterministic ZIP hash and manifest design.

Result: Work v3 3/3, functional parity 3/3, all Work answers 3/3 valid, and zero workflow operations. Together with the unchanged Codex 0.3.1 evidence, the included cross-host total is 32/32 answer-valid and 32/32 v3-valid.

Adoption: **Repository-level approved — explicit invocation only**. Public/synthetic query construction only; no authentication, tenant access, live metadata, MCP, tokens, confidential data, plugin installation, or operational Dataverse actions.
