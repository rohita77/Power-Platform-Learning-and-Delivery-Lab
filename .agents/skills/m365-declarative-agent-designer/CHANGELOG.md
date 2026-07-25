# Changelog

## 0.2.0-rc2 — 2026-07-25

- Made initial and continuation carry-forward lineage rules directly
  model-visible and deterministically enforceable.
- Added the status decision table and prohibited `Complete` when abstentions
  remain.
- Required model-authored validation metadata to remain
  `pending-external-validation` with an unmeasured zero-duration placeholder.
- Added the preserved Work smoke-003 output as an immutable regression fixture
  and added focused initial, continuation, status, and metadata cases.
- Preserved the 0.1.0 DesignRequest, DesignResult, provenance, and host
  attestation contract versions.

## 0.2.0-rc1 — 2026-07-22

- Added a strict, single-inference host-validation attestation contract.
- Required the host to validate the exact request and supply its canonical
  digest separately from user input before inference.
- Required the model to copy the attested request ID and digest without
  computing, guessing, replacing, zero-filling, or normalizing them.
- Added deterministic attestation, replay, authority, request-match, and
  output-match validation while preserving the 0.1.0 DesignRequest and
  DesignResult contracts.
- Kept Codex and ChatGPT Work adapter policy and authority boundaries aligned.

## 0.1.0 — 2026-07-22

- Added the portable five-mode requirements-discovery methodology.
- Added canonical Draft 2020-12 DesignRequest, DesignResult, finding,
  provenance, contradiction, abstention, and carry-forward contracts.
- Added fail-closed offline validators and synthetic trigger, golden, negative,
  security, regression, package, adapter, and rollback evaluation.
- Limited Codex and ChatGPT Work to identical canonical adapter contracts with
  runtime evaluation explicitly untested.
- Excluded Toolkit, Work IQ, Microsoft runtime artifacts, tenant access,
  connectors, MCP, workflows, deployment, publication, operational telemetry,
  and hidden persistence.
