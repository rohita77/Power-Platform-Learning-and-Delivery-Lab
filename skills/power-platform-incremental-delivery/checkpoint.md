# Power Platform Incremental Delivery v0.2.0-rc1 Checkpoint

**Checkpoint date:** 2026-07-20
**Status:** Checkpointed — all Codex release gates passed
**Adoption:** Experiment approved pending ChatGPT Work parity and expert review
**Power CAT publication prerequisite:** `ea9708b`

## Outcome

`power-platform-incremental-delivery` v0.2.0-rc1 implements the portable
three-stage delegation protocol:

1. Skill 6 emits a validated, sanitized specialist request.
2. The user, evaluator, or host executes the specialist explicitly in a fresh
   thread using only the narrowed payload.
3. Skill 6 resumes with a preserved result and verifies identity, register,
   boundary, classification, source path, SHA-256, answer schema, operation
   evidence, and untrusted content before consuming it.

Skill 6 never depends on deterministic nested skill invocation and never
authenticates, accesses a tenant, invokes `dv-*`, uses MCP, deploys, commits,
or pushes as part of its workflow.

## Root cause and correction

RC3 passed the complete 686-character Skill 6 build-brief input to Power CAT
instead of a narrowed specialist payload. That input has SHA-256
`d3b75bbb4bcb6322a7981124145adeefb6a8fe47c4296d985bf57e201afd8b14`.

The corrected specialist-only payload has SHA-256
`cfe0035670a2c16613f359f61fa2228fba9f20e0bf45145236147ce13451201f`.
An isolated exact 0.3.1 Power CAT control passed before implementation.
`DEL-001` now emits an `Open` delegation request, `GOLD-005` consumes a frozen
independently validated result, and `CHAIN-001` proves the full external
handoff and resume sequence.

The diagnostic full-suite pass also exposed one status defect: `NEG-002`
preserved the settled server-side owner but returned `Open`. The final contract
keeps an already complete supplied brief `Ready` after rejecting an unsupported
reopening request. The targeted and complete suites were rerun after that
correction.

## Evaluation result

- Isolated Power CAT control: pass; answer schema valid; zero operations.
- Targeted gate: 8/8 cases passed across nine Skill 6 invocations and one
  evaluator-owned Power CAT invocation.
- Trigger routing: 9/9.
- Golden: 5/5.
- Negative: 6/6.
- Security: 7/7.
- Delegation: 9/9.
- Complete suite: 36/36 in 36 distinct Codex threads.
- Skill 6 output schema: 45/45.
- Codex result-record v3 profile: 44/44.
- Power CAT answer schema: 3/3.
- Delegation schema fixtures: 2/2 valid accepted and 6/6 invalid rejected.
- Skill 6 and Power CAT workflow operations: zero.
- Prohibited authentication, tenant, MCP, `dv-*`, network, deployment,
  commit, push, secret, and confidential-data activity: zero.

## Evidence boundary

Immutable evidence is retained under:

- `tests/results/codex/v0.1.0-rc1/`;
- `tests/results/codex/v0.1.0-rc2/`;
- `tests/results/codex/v0.1.0-rc3/`; and
- `tests/results/codex/v0.2.0-rc1/`.

The RC1-RC3 checksum manifests remain unchanged and valid. The canonical skill
and `.agents` publication are recursively byte-identical, contain no symlinks,
and pass structural validation. The Power CAT experiment source and
repository-root publication remain byte-identical and unmodified.

This checkpoint proves local source, deterministic schema, preserved evaluator
evidence, and Codex runtime behavior only. It does not prove ChatGPT Work
parity, expert approval, tenant configuration, deployment, activation, or
production runtime behavior.

## Continuing position

1. Keep v0.2.0-rc1 at experiment approval, not production approval.
2. Run exactly the three unchanged parity cases in ChatGPT Work without
   creating Codex-only requirements.
3. Obtain the required expert review before broader adoption.
4. Preserve all versioned evidence and use a new immutable candidate for any
   behavioral change.
5. Keep Power CAT execution external, explicit, synthetic/public only, and
   configuration-gated by the canonical register.

## Repository state at checkpoint

The intended commit contains only
`skills/power-platform-incremental-delivery/` and its byte-identical
`.agents/skills/power-platform-incremental-delivery/` publication. The Power
CAT repository publication remains the separate `ea9708b` prerequisite.
Canonical-pack replacement work, the current-feature-verifier publication, and
all other unrelated worktree changes remain outside this checkpoint. No push
is authorized.
