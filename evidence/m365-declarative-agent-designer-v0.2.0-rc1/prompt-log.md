# M365 Declarative Agent Designer v0.2.0-rc1 Prompt Log

**Workstream:** Host-validation-attestation remediation and isolated runtime evaluation
**Checkpointed:** 2026-07-23
**Status:** `implemented-pending-runtime-evaluation`
**Next gate:** `chatgpt-work-feasibility-smoke`

## Request sequence

1. Preserve all v0.1.0 implementation, Codex RC1, Codex RC2,
   contaminated-diagnostic, and Codex RC3 evidence unchanged.
2. Create v0.2.0-rc1 as a narrow remediation of the RC3 all-zero
   `request_digest` failure.
3. Add a strict Draft 2020-12 host-validation-attestation contract binding the
   exact request ID, canonical digest, passed validation, permitted boundary,
   public or synthetic classification, and single-inference scope.
4. Require the host to supply the validated attestation separately from user
   input and require the model to copy the request ID and digest exactly.
5. Update both host adapters and deterministic validators without adding an
   external dependency or claiming Microsoft runtime, tenant, Toolkit,
   Work IQ, or deployment compatibility.
6. Add valid and invalid attestation fixtures and retain the RC3 all-zero
   result as a deterministic regression.
7. Run the static and deterministic gates, then attempt a single GOLD-001
   smoke only if the evaluator first proves an exact allowlist, zero expected-
   result exposure, no response format, and no callable model tools.
8. Stop before inference when the Codex CLI 0.144.5 preflight exposes four
   callable tools with `tool_choice: auto`.
9. Record the candidate as implemented pending runtime evaluation, with no
   package defect identified and ChatGPT Work feasibility as the next gate.
10. Create this checkpoint and paired prompt log without modifying package or
    prior evidence and without committing or pushing.

## Delivered result

- Candidate: `m365-declarative-agent-designer` v0.2.0-rc1.
- Package remediation: implemented and deterministically valid.
- Canonical/publication parity: pass.
- Package defect identified: false.
- Codex CLI evaluated: 0.144.5.
- Strict Codex isolation: blocked by four callable tools.
- External inferences: zero.
- First output: none.
- Adoption: implemented pending runtime evaluation.
- Next gate: ChatGPT Work feasibility smoke.

## Boundaries retained

The checkpoint records local source and deterministic evidence only. It is not
a successful runtime smoke and does not prove ChatGPT Work feasibility,
cross-host parity, Microsoft runtime behavior, tenant fitment, deployment,
activation, or production use. The next gate must preserve the exact input and
first output, expose no expected result or evaluator implementation, perform no
repair or retry, and stop on any isolation, parsing, schema, semantic, or
validator failure.
