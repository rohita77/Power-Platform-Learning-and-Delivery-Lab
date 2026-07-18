# OpenAI Adapter

## Status

**ChatGPT Work: active mandatory test target.**

This adapter is a thin client note for the portable
[skill](../../SKILL.md). It does not add product facts, weaken stop conditions,
or imply that runtime golden tests have passed.

## Adaptation

- Use the portable `name` and `description` front matter for discovery.
- Load the skill body only after it triggers; load references and templates as
  the workflow requires.
- Use available public-web/document retrieval only for live first-party
  evidence.
- Emit the required report fields and validate machine output against
  [the schema](../../tests/output-schema.json) when the client supports
  structured output.
- Record ChatGPT plan/workspace, model/runtime, date, sources, output, score,
  deviations, and reviewer for every test.

## Permissions and boundary

Allow public read-only retrieval only. Do not enable organisational tenant
apps, connectors, confidential knowledge, credentials, environment access, or
cross-zone synchronization for this skill. Connected-source availability does
not authorize its use.

Do not add a M365 Copilot or Copilot Studio runtime here. Those adaptations
belong to separately approved organisational-zone implementations.

## Required evaluation

Execute the parity subset in [the test contract](../../tests/README.md).
Until recorded, status remains **active target, not yet runtime-tested for
v0.1.0**.
