# M365 Declarative Agent Designer v0.2.0-rc2 Checkpoint

**Checkpoint date:** 2026-07-25
**Status:** `implemented-pending-runtime-evaluation`
**Package defect identified:** `false`
**RC2 external inferences:** `0`
**Next gate:** `chatgpt-work-gold-001-rc2-smoke`

## Outcome

`m365-declarative-agent-designer` v0.2.0-rc2 implements the narrow
contract-visibility remediation identified by the preserved ChatGPT Work
GOLD-001 smoke-003 result. The candidate makes initial and continuation
lineage, status selection, and model-authored evaluation metadata explicit in
the model-visible contract and enforces them through Draft 2020-12 schema
conditions and deterministic validators.

The package, canonical publication copy, focused regression surface, and
individual-file Work handoff are complete. No RC2 runtime inference was
performed because this session did not provide a ChatGPT Work execution
surface.

## Contract changes

- Initial results require carry-forward sequence `0`, a null previous result,
  and current request/result identifiers only.
- Continuations require the prior sequence plus one, the actual supplied prior
  result identifier, and preserved chronological lineage.
- Stale or incompatible continuation state remains `Open`.
- Non-empty abstentions prohibit `Complete`; a retained GOLD-001 host-fit
  abstention requires `Open`.
- Model-authored `validator_outcome` is
  `pending-external-validation`; model-authored `duration_ms: 0` is explicitly
  unmeasured.
- Actual schema, validator, and duration results remain evaluator-owned.

The DesignRequest and host-validation-attestation schemas remain unchanged.
DesignRequest and DesignResult contract versions remain `0.1.0`.

## Validation

- Skill quick validation: pass.
- Draft 2020-12 meta-validation for all four schemas: pass.
- Canonical deterministic suite: pass.
- `.agents` publication deterministic suite: pass.
- Each suite passed 5 golden pairs, 13 attestation cases, 11 negative cases,
  11 security cases, 13 result-invariant cases, 15 regression cases, and one
  rollback dry-run with zero failures.
- Package validation and allowlist: pass with zero findings.
- Canonical/publication byte equality: pass.
- Symlink scan: zero.
- Secret scan: zero findings.
- RC2 Work handoff manifest: pass.
- `git diff --check`: pass.

The unchanged Work smoke-003 output is retained as a regression fixture and
continues to hash to
`a2cc08f4a187011fcc15078c7d418f878f62685c500a9766950b7d37de97264e`.
The regression now detects broken prior-result resolution, invalid
`Complete` status with abstentions, stale initial carry-forward state, and the
premature model-authored validation claim.

## Work handoff

The individual-file package is
`m365-declarative-agent-designer-work-smoke-rc2/`. It contains only the revised
SKILL.md, DesignResult and directly referenced schemas, the ChatGPT Work
adapter, the unchanged GOLD-001 input, the unchanged independently validated
host attestation, and its SHA-256 manifest.

- GOLD-001 input SHA-256:
  `f2e73f81911fc08d5a7711bfcd3823e5dc5c88f438613c2462bfd921620bd1dd`
- Host-attestation SHA-256:
  `8c51b4acfe539e5b341bed393baab90c69b34c82c3be8db77f0d0bb113c3dfb5`
- Work RC2 manifest SHA-256:
  `20f8fcea08cf10bb8fc422efd97c4a1fb2213c4c9457731aced51d7dbd8aa6c0`

The handoff excludes tests, expected outputs, validators, prior evidence,
runtime results, repository history, Microsoft artifacts, and tenant or
organisational content.

## Evidence boundary and adoption

All prior Codex RC1, RC2 and RC3 evidence, the contaminated diagnostic, Work
archive-isolation attempt, Work input-missing abstention,
attestation-metadata-incomplete output, Work smoke-003 first response, and its
offline/evaluation records remain unchanged.

Static and deterministic proof does not establish ChatGPT Work behavioral
conformance. Adoption remains `implemented-pending-runtime-evaluation`.
The next gate is exactly one isolated GOLD-001 Work inference using the RC2
individual-file package, with immutable first-output handling and no repair,
normalization, or retry.

No authentication, tenant access, connector, MCP, Work IQ, Toolkit,
deployment, or push occurred.
