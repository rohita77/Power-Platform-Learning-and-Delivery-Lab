+# Power Platform Incremental Delivery v0.1.0 Prompt Log

**Workstream:** Build, evaluate, and remediate
`power-platform-incremental-delivery`
**Checkpointed:** 2026-07-20
**Final candidate:** v0.1.0-rc3
**Adoption:** Reject

## Request sequence

1. Design the smallest reusable orchestration skill that reconstructs the
   agreed delivery position and produces the next deployable Power Platform or
   Dynamics 365 vertical-slice build brief.
2. Apply source governance, the skill design standard, the upstream register,
   the approved Power CAT Dataverse adapter experiment, the personal/OpenAI
   versus organisational/Microsoft boundary, and explicit specialist routing.
3. Publish the approved `dataverse-webapi-query` adapter byte-identically to
   the repository root as a separable prerequisite; do not install or alter its
   behavior incidentally.
4. Implement v0.1.0 with deterministic JSON output, carry-forward state,
   vertical-slice structure, abstention, delegation configuration gates, and
   immutable tests.
5. Evaluate RC1 across the defined suites without tenant access, tools,
   authentication, deployment, output repair, commit, or push.
6. Create RC2 to remediate the smoke failure, preserve RC1, and rerun the suite.
7. Create RC3 to correct delegation truthfulness, deterministic
   `selection_mode`, Power CAT `source_type`, string
   `result_reference`, do-not-trigger abstention, and the seven recorded RC2
   failures.
8. Execute the seven-case RC3 gate first, stop on failure, retain the exact
   outputs, and report adoption honestly.
9. Checkpoint and commit the completed local work without pushing.

## Delivered result

- Skill source and repository publication are recursively byte-identical and
  contain no symlinks.
- The Power CAT publication prerequisite is separately committed as
  `ea9708b` (`Publish approved Dataverse query skill`).
- RC3 targeted evaluation: 5/7.
- Skill 6 output schema: 7/7.
- Codex result-record profile: 7/7.
- Standalone Power CAT answer schema: 0/2.
- Full suite: not run because the targeted 7/7 gate failed.
- Adoption: Reject.
- RC1, RC2, and RC3 evidence is preserved under versioned immutable result
  directories.
- No push was performed.

## Failure and continuation

`GOLD-005` and `DEL-001` require successful explicit Power CAT execution.
The separately executed specialist outputs were preserved unchanged but were
prose rather than one schema-valid JSON object and each attempted one rejected
tool operation. Skill 6 correctly returned `Open`, recorded
`invoked: false`, used `source_type: upstream`, and did not reconstruct or
simulate a specialist result.

Continuation must address the Power CAT runtime output/operation defect,
create a new immutable candidate, rerun the seven exact targeted inputs, and
run the full 36 cases only after 7/7 targeted success. ChatGPT Work parity and
expert review remain pending.

## Boundaries retained

Do not broaden this checkpoint into implicit skill selection, autonomous
delegation, tenant access, authentication, live metadata, MCP, tokens,
confidential data, operational Dataverse work, deployment, or general Power
Platform expertise. Preserve the separation between evaluator configuration
and exact test input, and never overwrite prior evidence.
