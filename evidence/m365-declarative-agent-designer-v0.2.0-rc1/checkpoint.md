# M365 Declarative Agent Designer v0.2.0-rc1 Checkpoint

**Checkpoint date:** 2026-07-23
**Status:** `implemented-pending-runtime-evaluation`
**Codex status:** `blocked-by-host-tool-isolation`
**Package defect identified:** `false`
**Codex CLI evaluated:** `0.144.5`
**Callable tools exposed:** `4`
**External inferences:** `0`
**Next gate:** `chatgpt-work-feasibility-smoke`

## Outcome

`m365-declarative-agent-designer` v0.2.0-rc1 implements the narrow
host-validation-attestation remediation for the v0.1.0 RC3 request-digest
failure. Static, deterministic, package, regression, and publication-copy
checks passed. No package defect was identified.

The strict Codex smoke did not run. The Codex CLI 0.144.5 preflight preserved
the exact GOLD-001 input and approved five-item context allowlist, but the
outbound envelope still exposed four callable tools: `exec`, `wait`,
`request_user_input`, and `collaboration`, with `tool_choice: auto`. The
evaluator therefore stopped before external inference.

## Evidence boundary

- Canonical and `.agents` publication copies are byte-identical.
- The deterministic suite passed 5 golden, 13 attestation, 11 negative,
  11 security, and 14 regression cases with zero failures.
- The exact GOLD-001 request digest is
  `30acb68ccd1cd7521d07e7b57a93973dd5243d43c5f23ccaa52785cb8c9fb6d6`.
- The validated host-attestation SHA-256 is
  `8c51b4acfe539e5b341bed393baab90c69b34c82c3be8db77f0d0bb113c3dfb5`.
- Expected-output exposure, workflow operations, output repairs, retries, and
  prohibited activity were zero.
- External model inferences were zero; no first output exists for this
  candidate.
- All prior v0.1.0 implementation, RC1, RC2, contaminated-diagnostic, and RC3
  evidence remains unchanged.

The immutable evaluator record is retained under
`evidence/m365-declarative-agent-designer-v0.1.0/runtime-results/codex/v0.2.0-rc1/`.
This checkpoint does not upgrade the stopped preflight into runtime evidence.

## Continuing position

1. Keep adoption at `implemented-pending-runtime-evaluation`.
2. Do not classify the Codex host-isolation failure as a package defect.
3. Do not spend an external inference unless the evaluator can prove that all
   callable model tools are absent from the outbound envelope.
4. Run the next controlled gate as a ChatGPT Work feasibility smoke using the
   unchanged request, attestation, contract, no-repair rule, and immutable
   first-output handling.
5. Preserve this candidate and all earlier evidence; any behavioral change
   requires new versioned evidence.

## Repository state at checkpoint

This checkpoint adds only its checkpoint and paired prompt-log artifacts.
It does not change the skill package, adapters, schemas, validators, fixtures,
or runtime evidence. No authentication, tenant access, MCP, connector,
Toolkit, Work IQ, deployment, commit, or push occurred.
