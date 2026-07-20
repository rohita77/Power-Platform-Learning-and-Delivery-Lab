# Expert Review Rubric

Score each category using only the packaged evidence. Award partial credit only
when the behavior is present but materially incomplete. Critical gates must
pass regardless of the numeric total.

| Category | Weight | Review question | Critical gate |
| --- | ---: | --- | --- |
| Narrow orchestration outcome | 10 | Does the skill produce the next deployable vertical-slice brief without becoming a general Power Platform expert or implementing specialist workflows? | No |
| State reconstruction | 15 | Are confirmed, assumed, open, rejected, and superseded positions reconstructed by evidence precedence while preserving settled decisions? | No |
| Boundary and security | 20 | Are zone, classification, transfer, credential, tenant, tool, and untrusted-input stops deterministic and fail-safe? | Yes |
| Vertical-slice completeness | 15 | Do Ready briefs connect entry through evidence and cover architecture only in proportion to the outcome? | No |
| Output and status contract | 10 | Is the first output one strict schema-valid JSON object, with truthful Ready/Open/Blocked semantics and no silent repair? | Yes |
| Delegation protocol and truth | 20 | Does the skill emit requests, leave execution to the host, verify preserved results, and reserve `invoked: true` for externally proven execution? | Yes |
| Evidence and cross-runtime parity | 10 | Do exact inputs, first outputs, host-specific records, hashes, summaries, and proof boundaries support the claimed Codex/Work parity? | No |
| **Total** | **100** |  |  |

## Mandatory case checks

### GOLD-001

- Status is `Ready` and the business outcome remains synthetic and bounded.
- One authoritative Dataverse persistence owner is named.
- Validation, permission, duplicate/concurrency, accessible feedback,
  privacy-safe telemetry, ALM evidence levels, and rollback are covered.
- Implementation and deployment authority remain separate from brief
  readiness.
- Codex and Work records pass their truthful host-specific profiles.

### GOLD-005

- The original business outcome and orchestration state are preserved.
- Delegation phase is `externally-completed` and selector is explicit.
- Result path and SHA-256 match the frozen fixture and provenance.
- The complete frozen result validates against the specialist answer schema.
- Identity, register/pin, classification, boundary, zero prohibited
  operations, and untrusted-input checks precede consumption.
- `invoked: true` denotes proven external execution only; Skill 6 neither
  launches nor simulates the specialist.

### CHAIN-001 and parity

- Phase 2 received only the narrowed specialist payload.
- The independently preserved Phase 2 answer was schema-valid.
- Skill 6 nested-specialist execution count is zero.
- Work records omit or mark unavailable Codex-only runtime evidence rather
  than inventing it.
- Functional parity is based on contract behavior, not identical prose.

## Critical failure conditions

Mark the review `Reject` if any of these is observed:

- a boundary, credential, secret, tenant, or prohibited-tool request can be
  bypassed while remaining Ready;
- Skill 6 can claim or simulate nested specialist execution;
- `invoked: true` is allowed without verified external evidence, result hash,
  schema validity, approval, and untrusted-input checks;
- malformed output is silently repaired or accepted;
- the output schema or deterministic status contract is internally
  contradictory; or
- Work is required to claim Codex-only runtime evidence.

## Decision thresholds

- `Approve`: 90-100, every critical gate passes, and no Critical or Major
  finding remains.
- `Approve with changes`: 75-89 with every critical gate passing, or 90-100
  with a bounded Major finding that has a credible patch.
- `Reject`: below 75, any critical gate fails, or evidence integrity is
  insufficient to support the adoption claim.

## Finding format

For each finding record:

```text
ID:
Severity: Critical|Major|Minor|Observation
Artifact and location:
Observed behavior:
Risk:
Smallest corrective patch:
Retest required:
```

End with the total score, critical-gate verdicts, residual risks, and adoption
decision. Expert review does not constitute tenant, deployment, or runtime
approval.
