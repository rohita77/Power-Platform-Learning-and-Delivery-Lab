# M365 Declarative Agent Designer v0.2.0-rc4 Checkpoint

**Checkpoint date:** 2026-08-01
**Status:** `implemented-pending-runtime-evaluation`
**Canonical contract version:** `0.1.0`
**RC4 external inferences:** `0`
**Next gate:** `chatgpt-work-gold-001-unique-installed-skill-rc4`

## Outcome

`m365-declarative-agent-designer` v0.2.0-rc4 is the narrow remediation of the
unique installed-skill ChatGPT Work RC3 output-contract failure. The skill now
places a complete schema-valid DesignResult skeleton before design reasoning,
requires placeholder-only value replacement, makes every canonical nested
shape directly model-visible, and prohibits narrative alternative structures.

The canonical skill, byte-identical `.agents` publication, deterministic
regression surface, preserved Work evidence, and private RC4 evaluation ZIP
are complete. No RC4 runtime inference was performed.

## RC3 evidence and root cause

The unique RC3 evaluation skill was selected, so stale installation was not
the root cause. Its first output passed the exact 16-root-key set, prohibited
alternative-root check, request and attestation identity, contradiction,
abstention, and referential-integrity validation. It failed because the model
generated noncanonical nested objects and two prohibited operational phrases.

The immutable RC3 evaluation remains `WORK-OUTPUT-CONTRACT-FAIL` with 88
findings:

- `DAD-MISSING-FIELD`: 60
- `DAD-SCHEMA-INVALID`: 24
- `DAD-PROHIBITED-OPERATION`: 2
- `DAD-INCOMPATIBLE-CARRY-FORWARD`: 1
- `DAD-SCHEMA-VERSION`: 1

Preserved hashes:

- RC2 installed-skill first output:
  `6eb1726d079e40c169024f799d138653d08a76868e2b695df6cd620a511a6266`
- RC3 installed-skill first output:
  `f6f3bc36873495fffd274daa57a4d5319f17601d65bcf0f64331ead541e55c14`
- RC3 unique installed-skill first output:
  `3c072ac89c0fc0b62415c4445701ab8a0c9d9afb21f5f5027863e853c2057810`
- RC3 offline validation:
  `3b18c9079d5fcc47b6d54dbcc76a65acabc90a9ec07ea23448af1954f0a5d4b2`
- RC3 evaluation record:
  `2aca48e26d506a8747d14aa4bce09b92d3b2a947eb223cebfe2441ca1bc9216f`

No prior output or evaluation record was repaired, normalized, or replaced.

## RC4 contract changes

- Candidate version is `0.2.0-rc4`; the DesignRequest and DesignResult
  contracts remain `0.1.0`.
- `SKILL.md` begins its model-visible output section with the schema-first
  copy-and-replace sequence.
- The embedded neutral skeleton contains all 16 root properties and complete
  valid shapes for disclaimers, five ordered modes, requirements, findings,
  provenance, contradictions, abstentions, initial carry-forward, and
  evaluation metadata.
- Nested objects prohibit alternative properties and object/array type
  substitutions.
- Work evaluation metadata remains
  `pending-external-validation` with unmeasured `duration_ms: 0`.
- Free text must use neutral conceptual wording; commands and procedural
  descriptions of operational activity remain prohibited.
- The security scanner was not weakened.

## Validation

- Skill quick validation: pass for canonical and publication copies.
- Draft 2020-12 meta-validation: 4/4 schemas pass unchanged.
- Canonical deterministic suite: 90/90 cases pass.
- `.agents` deterministic suite: 90/90 cases pass.
- Each suite includes 6 trigger, 5 golden, 13 attestation, 11 negative,
  11 security, 13 result-invariant, 6 generation-shape, 9 focused nested
  contract, 15 regression, and 1 rollback case.
- Model-visible contract assertions: 76/76.
- Schema-first visibility assertions: 15/15.
- Trigger metadata assertions: 8/8.
- Neutral skeleton request, boundary, attestation, DesignResult schema,
  provenance, contradiction, abstention, carry-forward, and combined result
  checks: pass with zero findings.
- RC3 regression: all 88 exact normalized findings remain required.
- Package validation and allowlist: pass with zero findings.
- Canonical/publication recursive byte equality: pass.
- Symlink scan: zero.
- Secret scan: zero findings.
- `git diff --check`: pass.

## Evaluation packages

- RC2 Work smoke ZIP:
  `5383b79026a47bcb5d223c053da100c80a8d071225a49214f185e85012fc614a`
- RC3 evaluation ZIP:
  `d1f2db14c2370aa3d4605ef22d1c3746752a12b964868f90e7738b1002e12170`
- RC4 evaluation ZIP:
  `8c95e749666e098b3615c8c67c6676ed01dd3beccadccac291cef82c3632c70e`

The RC4 ZIP contains exactly seven allowed files and the unique marker
`RC4-EVAL-CANONICAL-NESTED-CONTRACT`. Its six-entry manifest passes. It
excludes tests, validators, evidence, expected outputs, repository history,
tenant content, credentials, and secrets.

## Evidence boundary and next gate

This checkpoint proves local source, schema, deterministic-test, publication,
and package integrity only. It does not prove ChatGPT Work RC4 behavioral
conformance, Microsoft runtime compatibility, tenant fitment, deployment
authorization, or production readiness.

The next evaluator may run exactly one fresh ChatGPT Work GOLD-001 invocation
using the unique RC4 evaluation package. It must preserve the first response
unchanged and validate it offline without repair, normalization, or semantic
retry.

No authentication, tenant access, connector, MCP, Work IQ, Toolkit,
deployment, publication, push, credential handling, or confidential-data
operation occurred.
