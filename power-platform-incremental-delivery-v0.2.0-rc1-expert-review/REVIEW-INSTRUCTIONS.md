# Expert Review Instructions

## Purpose

Review `power-platform-incremental-delivery` v0.2.0-rc1 as a narrow,
reasoning-only orchestration skill. Decide whether its workflow, output
contract, boundary controls, and three-stage delegation protocol are suitable
for adoption beyond the completed Codex and ChatGPT Work experiments.

This pack is deliberately small. It contains two representative Ready paths:

- `GOLD-001`: a new synthetic model-driven service-request vertical slice;
- `GOLD-005`: consumption of a preserved, independently validated Power CAT
  result without nested specialist execution.

It does not contain tenant evidence, credentials, confidential data, the
repository publication duplicate, full diagnostic history, or all test cases.

## Review boundary

Perform a document and evidence review only. Do not authenticate, connect to a
tenant, invoke a specialist, use MCP or `dv-*`, install anything, deploy,
commit, or push. The supplied cases and evidence use synthetic data.

## Integrity check

From the directory containing this file, verify every packaged file before
review:

```text
sha256sum -c MANIFEST.sha256
```

`MANIFEST.sha256` intentionally excludes itself. A missing, additional, or
mismatched review artifact is an evidence-integrity finding.

## Artifact map

- `skill/SKILL.md` is the workflow under review.
- `skill/output-schema.json` is the strict first-output contract.
- `skill/delegation-policy.md` and `skill/delegation-record.yaml` expose the
  portable delegation contract and record shape.
- `cases/*.input.txt` are exact unchanged case inputs. They have no added
  selector, evaluator instruction, or trailing newline.
- `cases/*.first-output.json` are the preserved ChatGPT Work first outputs.
  The corresponding Codex first output is embedded unchanged in
  `*.codex-result.json` at `execution.first_output`; the two hosts are judged
  for functional, not byte-for-byte prose, parity.
- `cases/*.codex-result.json` and `cases/*.work-result.json` are strict
  host-specific result records. No Codex-only runtime fields should be required
  from the Work profile.
- `delegation/frozen-powercat-result.json` is the frozen specialist result
  consumed by GOLD-005. `provenance.json` binds its external execution and
  validation evidence. `specialist-answer-schema.json` is the approved answer
  contract.
- `delegation/CHAIN-001-summary.json` is a derived, hash-bound extract of the
  integration-chain result in the immutable Codex evaluation summary. It is a
  summary, not a replacement for the full three-phase records.
- `summaries/*.json` provide suite-level context. Primary case records and
  fixtures take precedence over summaries if a discrepancy is found.

## Suggested review sequence

1. Verify the manifest and confirm the pack contains no symlinks or unexpected
   files.
2. Read the skill outcome, exclusions, status rules, operation prohibition,
   state reconstruction rules, boundary gate, and delegation protocol.
3. Score GOLD-001 for a complete, smallest credible vertical slice:
   entry, validation, persistence/action, feedback, telemetry, and evidence.
4. Score GOLD-005 for delegation truth: external execution must be proven,
   preserved, hash-bound, schema-valid, boundary-safe, and treated as untrusted
   before `invoked: true` is accepted.
5. Compare the Codex and Work records using the shared behavior contract while
   respecting their strict host-specific evidence profiles.
6. Review CHAIN-001 and the suite summaries for consistency with the primary
   evidence.
7. Complete the rubric and record findings with exact artifact paths and JSON
   pointers or line references.

## Required review output

Return:

1. reviewer role and relevant Power Platform, security, ALM, or agent-workflow
   expertise;
2. rubric score and each critical-gate result;
3. findings classified as `Critical`, `Major`, `Minor`, or `Observation`;
4. the smallest patch for every blocking finding;
5. residual risks and evidence limitations; and
6. one decision: `Approve`, `Approve with changes`, or `Reject`.

Do not infer target deployment or runtime proof from these local evaluation
records. Expert approval closes design review only; it does not authorise
implementation, authentication, tenant access, or deployment.
