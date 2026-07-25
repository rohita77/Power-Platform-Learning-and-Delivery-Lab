# M365 Declarative Agent Designer v0.2.0-rc2 Prompt Log

**Workstream:** Work GOLD-001 deterministic-contract remediation
**Checkpointed:** 2026-07-25
**Status:** `implemented-pending-runtime-evaluation`
**Next gate:** `chatgpt-work-gold-001-rc2-smoke`

## Request sequence

1. Preserve the complete v0.1.0 Codex and ChatGPT Work evidence chain and all
   first outputs unchanged.
2. Diagnose and evaluate strict Codex context isolation without treating a
   contaminated schema pass as independent runtime evidence.
3. Stop the strict Codex attempt when the host could not prove a zero-tool
   outbound envelope.
4. Prepare the minimal individual-file ChatGPT Work package containing only
   the selected skill, directly required schemas and adapter, exact GOLD-001
   input, independently validated host attestation, and manifest.
5. Preserve the first ChatGPT Work smoke-003 output unchanged and validate it
   offline without normalization, repair, or retry.
6. Classify its deterministic failures as package contract-visibility defects:
   initial sequence `1`, unresolved prior-result lineage, `Complete` with a
   host-fit abstention, and model-authored validation success.
7. Create v0.2.0-rc2 as a narrow remediation, without changing DesignRequest
   or host-attestation contracts.
8. Add model-visible initial/continuation lineage rules, a status decision
   table, and pending external-validation metadata.
9. Enforce the invariants through schema, deterministic validators, valid and
   invalid fixtures, and an immutable Work smoke-003 regression fixture.
10. Run the static gate, preserve canonical/publication equality, and prepare
    a new isolated RC2 Work handoff.
11. Stop before runtime inference because no ChatGPT Work execution surface
    was available.
12. Checkpoint and commit the complete scoped m365 designer history without
    pushing or including unrelated worktree files.

## Delivered result

- Candidate: `m365-declarative-agent-designer` v0.2.0-rc2.
- Canonical and publication suites: pass.
- Result-invariant cases: 13/13.
- Regression cases: 15/15.
- Package, schema, parity, symlink, secret, manifest, and diff gates: pass.
- Work RC2 individual-file package: prepared.
- RC2 external inference: not run.
- Package defect remaining after static validation: none identified.
- Adoption: implemented pending runtime evaluation.

## Boundaries retained

This checkpoint records package implementation and offline deterministic proof.
It does not claim ChatGPT Work behavioral conformance, cross-host parity,
Microsoft runtime compatibility, tenant fitment, deployment authorization, or
production readiness. The next evaluator must expose no tests, validators,
expected output, prior evidence, or model tools and must preserve the first
response byte-for-byte.
