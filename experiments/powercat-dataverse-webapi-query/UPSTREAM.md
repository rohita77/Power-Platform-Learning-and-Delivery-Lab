# Upstream pin and proposed register entry

## Pin comparison

| Item | Value |
| --- | --- |
| Upstream | `microsoft/power-cat-skills` |
| Registered pin | `f4bb4ad5bf55e2d50076292bd6301f6337d38083` |
| Current inspected pin | `33bc38456abb83f27daad968b748c8085f2a78ef` |
| Original path | `plugins/powercat-dataverse/skills/dataverse-webapi-query/dataverse-webapi-query.md` |
| Skill blob at both pins | `8791590eeca8b1c697856c8a5cca9fbab3ef12b6` |
| License | MIT |
| Inspected on | 2026-07-19 |

`git diff --exit-code` across `plugins/powercat-dataverse` is empty between the registered and inspected pins. The selected skill blob is identical at both pins. The only repository difference is the top-level `README.md`, which changes the documented marketplace clients and installation guidance from Claude-oriented wording to Microsoft Scout and GitHub Copilot CLI. That change is material to compatibility metadata, but not to the selected skill's instructions, plugin metadata, dependencies, or security behavior. The Phase 1 stop condition was therefore not triggered.

## Proposed local register update

This table records the experiment-local basis for the canonical entry published at experiment closure.

| Upstream | Official supported clients recorded by upstream | Installed/evaluation status | Version or commit | Lab test status | Data boundary |
| --- | --- | --- | --- | --- | --- |
| `microsoft/power-cat-skills` / `powercat-dataverse` / `dataverse-webapi-query` | Microsoft Scout and GitHub Copilot CLI; Codex support unclaimed | Not installed; isolated repository adaptation | `33bc38456abb83f27daad968b748c8085f2a78ef` | Codex explicit-0.3.1 passed 28/28; Work parity passed 3/3; repository-level approved, explicit invocation only | Public upstream and synthetic inputs only; tenant/authentication/operational use prohibited |

## Revalidation

Revalidate before any install, upgrade, authentication, tenant-connected test, repository promotion, or after a material upstream change. The first scheduled review remains 2026-08-01.

## Remediation evidence

Public upstream `main` was rechecked immediately before remediation and still resolved to `33bc38456abb83f27daad968b748c8085f2a78ef`. No selected-subtree, dependency, permission, telemetry, or security delta was found.

- `remediation-0.2.0`: complete 27-case Codex run; 0/24 applicable outputs met the exact answer contract; no tools or approvals.
- `remediation-0.2.1`: stopped after its first case; the answer met the contract, but two prohibited `command_execution` events were recorded.
- `remediation-0.2.2`: the self-contained adaptation's implicit smoke exited zero but failed the answer contract and performed three distinct web searches (six lifecycle events); zero command executions and approvals occurred, and the 27-case suite remained blocked.
- `remediation-0.2.2` corrected smoke: after using the documented `web_search="disabled"` setting and front-loading unresolved-query triggers, a second exact-prompt invocation emitted zero workflow commands, tools, approvals, or network events but still failed to apply the inline contract. The suite remained blocked.
- `remediation-0.2.2` selection controls: an explicit `$dataverse-webapi-query` invocation passed the answer contract with zero workflow events; two further exact-prompt implicit smokes remained zero-tool but failed the contract even after mandatory trigger wording and repository routing. Implicit compatibility remains unproved.
- `explicit-0.3.0`: all 27 exact fixture payloads ran with explicit repository-skill selection. Workflow operations were zero and result-schema validity was 27/27, but answer-schema validity and the reviewed scorecard were 26/27 because `GOLDEN-005` emitted an object where `choice_or_status_values` requires strings.
- `explicit-0.3.1`: the unchanged `GOLDEN-005` smoke passed, followed by a 28/28 suite including retained `REG-004`. All 29 answers and result records validate; workflow operations remain zero.
- `evidence-contract-0.3.2`: preserved the Work download and historical invalid self-hashing manifest, added strict Codex/Work v3 profiles, validated Codex 29/29, Work 3/3, answers 32/32, parity 3/3, and zero workflow-operation failures without changing adapter behavior.
- Current decision: **Repository-level approved — explicit invocation only**. The canonical register now publishes the restricted adapter status. Owner: Rohit. Next revalidation: 2026-08-01 and before any install, upgrade, authentication, MCP registration, tenant-connected test, material upstream change, or promotion.
