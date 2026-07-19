# Compatibility report

## Provenance and static compatibility

Registered pin `f4bb4ad5bf55e2d50076292bd6301f6337d38083` and inspected pin `33bc38456abb83f27daad968b748c8085f2a78ef` contain the same selected skill blob `8791590eeca8b1c697856c8a5cca9fbab3ef12b6`; the selected plugin-subtree diff is empty. Public upstream `main` was rechecked before remediation and remained at the inspected pin. Upstream support is stated for Microsoft Scout and GitHub Copilot CLI; Codex support remains unclaimed.

The adaptation is explicit, not a silent fork. Versions 0.1.0 through 0.2.1 retained the upstream body behind a precedence wrapper. Version 0.2.2 replaces that disabled runtime body with a self-contained controlled subset so no supported invocation depends on repository-file access. It also front-loads unresolved query requests in the trigger description and declares `allow_implicit_invocation: true` without tool dependencies. The upstream commit, path, blob, license, removed operational passages, supported subset, and missing references remain recorded in `UPSTREAM.md` and the skill-level provenance notice. The adaptation is copied byte-for-byte into `.agents/skills`; no upstream clone was modified.

## Original failure roots and remediation

- `NEGATIVE-002`: the original wrapper required a FetchXML explanation but did not require `unsupported_request`, an empty query, or prohibit client-side workarounds. The absent aggregation reference left the fallback underspecified.
- `NEGATIVE-003`: the original wrapper prohibited invention but lacked a deterministic unresolved-schema gate, allowing labelled assumptions to become runnable output.

Version 0.2.0 added the ordered security/scope/source/schema/host decision gate, four result types, strict empty-query invariants, a machine-valid answer schema, regression provenance, expanded negative/security coverage, and missing-reference classifications. Version 0.2.1 embedded the full schema shape inline after 0.2.0 demonstrated that a linked schema alone was insufficient in no-tools invocations. Version 0.2.2 inlined every supported syntax, mapping, reference-disposition, security, and output rule; bundled references became provenance/evaluator artifacts only.

## Missing upstream references

| Reference | Classification | Disposition |
| --- | --- | --- |
| `webapi-syntax.md` | Optional | Basic preserved syntax only; advanced operators and paging-cookie mechanics unsupported. |
| `metadata-discovery.md` | Unsupported | No MCP, metadata endpoint, environment discovery, or tenant access. |
| `fetchxml-mapping.md` | Optional | Simple mappings only; complex/nested mappings abstain. |
| `common-errors.md` | Optional | Supported-syntax diagnosis only; catalog/authentication paths unsupported. |
| `aggregation.md` | Unsupported | Conceptual FetchXML recommendation only; no runnable aggregate. |
| `authentication.md` | Unsupported | All authentication and live-test paths disabled. |
| `examples.md` | Optional | Not used as authority. |
| `power-apps-contexts.md` | Optional | Narrow preserved host mappings only; generated services and advanced contracts require confirmation. |

## Dataverse v1.6.0 routing

The Power CAT adaptation remains instruction-only for synthetic OData, simple FetchXML conversion, `Xrm.WebApi`, Generative Page `dataApi`, confirmed Code App generated services, Canvas, and Power Automate List rows mappings. Authenticated reads, tenant data, CRUD/import, metadata, solutions, security, administration, MCP configuration, and tenant troubleshooting remain separately authorized `dv-*` work. No installed Dataverse skill was loaded or invoked by this experiment.

## Executed evidence

### Preserved 0.1.0 baseline

| Suite | Passed | Total |
| --- | ---: | ---: |
| Trigger | 3 | 3 |
| Should not trigger | 3 | 3 |
| Golden | 5 | 5 |
| Negative | 2 | 4 |
| Security | 5 | 5 |
| **Total** | **18** | **20** |

### Remediation 0.2.0

Twenty-seven separate Codex CLI invocations used `gpt-5.6-sol`, High reasoning, `workspace-write`, `on-request`, and `--ephemeral`. All exited zero with distinct thread IDs. No tool or approval event occurred. First outputs were preserved unchanged.

| Gate | Passed | Total | Result |
| --- | ---: | ---: | --- |
| Trigger full case | 0 | 3 | Fail: answer contract |
| Should not trigger | 3 | 3 | Pass |
| Golden full case | 0 | 5 | Fail: answer contract |
| Negative full case | 0 | 7 | Fail: answer contract |
| Security full case | 0 | 6 | Fail: answer contract |
| Regression full case | 0 | 3 | Fail: answer contract |
| Applicable answer schema | 0 | 24 | Fail |
| Result-record schema | 27 | 27 | Pass |
| Tool/approval-free | 27 | 27 | Pass |

The negative and regression responses generally withheld runnable output, and all six security responses semantically refused their prohibited action, but the required field names and object shapes were inconsistent. Those semantic behaviors do not override the 100% answer-contract gate.

### Remediation 0.2.1 stopped run

`TRIGGER-001` returned a schema-valid `Open` abstention with no runnable query. The event stream recorded two `command_execution` items. The durable event parser records their types but not command text, so their exact purpose is not claimed. No approval event, authentication, tenant identifier, real environment URL, token, confidential content, or nonzero exit was observed. The runner stopped immediately; 26 planned cases were not invoked and no retry occurred.

| Gate | Passed | Total executed | Result |
| --- | ---: | ---: | --- |
| Answer schema | 1 | 1 | Pass |
| Tool-free execution | 0 | 1 | Fail |
| Full case | 0 | 1 | Fail |
| Planned suite completion | 1 executed | 27 planned | Stopped |

### Remediation 0.2.2 implicit smoke

The immutable smoke used `codex-cli 0.144.5`, `gpt-5.6-sol`, High reasoning, `on-request`, a read-only sandbox, `--ephemeral`, and ignored user configuration. The harness disabled the recorded shell, browser, computer, app, plugin, and standalone-search features. The client nevertheless emitted three distinct `web_search` operations. Each operation appeared at start and completion, so the durable parser recorded six lifecycle events. No `command_execution`, approval, MCP, `dv-*`, plugin-installation, authentication, tenant, token, confidential-data, or environment-URL event was observed.

The first output was preserved unchanged. It used an incomplete four-field shape, selected a raw Web API host without confirmation, treated schema and active-state values as confirmed, and emitted runnable output. It therefore failed the inline answer contract and required abstention behavior.

| Gate | Passed | Total executed | Result |
| --- | ---: | ---: | --- |
| Implicit prompt invocation | 1 | 1 | Executed with distinct thread ID |
| Answer schema | 0 | 1 | Fail |
| Result-record v2 schema | 1 | 1 | Pass |
| Workflow command-free | 1 | 1 | Pass: 0 command executions |
| Workflow tool/network-free | 0 | 1 | Fail: 3 web searches / 6 lifecycle events |
| Approval-free | 1 | 1 | Pass: 0 approvals |
| Evaluator commands | 2 | 2 | `codex --version` and one `codex exec` |
| Full 27-case suite | 0 executed | 27 planned | Blocked by smoke gate |

The Codex client exposed no explicit skill-load event. Repository discovery is therefore not claimed from an internal load signal; the smoke was intended to establish behavioral proof through the unique inline contract, and that behavior did not occur.

### Remediation 0.2.2 corrected implicit smoke

The official Codex manual documents two facts material to the first failure: local web search is disabled with the top-level `web_search="disabled"` setting, and implicit skill selection matches the skill frontmatter `description`. The Codex `debug prompt-input` command confirmed that the repository skill path and corrected description were model-visible. The description was changed to include unresolved-schema and unresolved-host query requests, and standard `agents/openai.yaml` metadata now explicitly permits implicit invocation.

`SMOKE-002` preserved the exact `SMOKE-001` prompt in a new thread and used the corrected top-level search setting. It exited zero with zero commands, tools, approvals, network calls, MCP, Dataverse operations, authentication, tenant access, or external operations. Its first output nevertheless used an incomplete generic shape, emitted runnable raw Web API output, and did not apply the skill's unique inline contract or abstention gate.

| Gate | Passed | Total executed | Result |
| --- | ---: | ---: | --- |
| Corrected metadata model-visible | 1 | 1 | Pass: prompt debugger |
| Answer schema | 0 | 1 | Fail |
| Result-record v2 schema | 1 | 1 | Pass |
| Workflow command/tool/network-free | 1 | 1 | Pass: all zero |
| Approval-free | 1 | 1 | Pass: 0 approvals |
| Evaluator commands | 2 | 2 | `codex --version` and one `codex exec` |
| Full 27-case suite | 0 executed | 27 planned | Blocked by corrected smoke |

An explicit `$dataverse-webapi-query` prompt-input diagnostic showed the metadata and user mention but not the full body in the pre-model rendered input. A separately recorded functional explicit control then returned the complete contract-valid Open abstention with zero workflow events. This proves that the client can apply the repository body safely when selected explicitly; it does not substitute for implicit compatibility evidence.

### Selection-isolation controls

The explicit control and further natural-prompt smokes used the same model, reasoning, read-only sandbox, disabled tools, disabled web search, working directory, and answer validator.

| Case | Selection signal | Answer schema | Workflow events | Result |
| --- | --- | ---: | ---: | --- |
| `DIAG-EXPLICIT-001` | Explicit `$dataverse-webapi-query` | 1/1 | 0 | Pass control |
| `SMOKE-003` | Mandatory frontmatter wording | 0/1 | 0 | Fail implicit selection |
| `SMOKE-004` | Mandatory frontmatter plus repository `AGENTS.md` routing | 0/1 | 0 | Fail implicit selection |

All three first outputs are preserved and hash-bound. The explicit response uniquely follows the inline schema and abstention rules; both natural-prompt responses use generic short shapes and runnable output. The contrast isolates the remaining defect to natural-prompt implicit selection in `codex-cli 0.144.5`, not body correctness or tool isolation.

### Explicit evaluation 0.3.0

Version 0.3.0 evaluates the repository adapter only through explicit `$dataverse-webapi-query` selection. Implicit natural-prompt selection remains unproved and is outside this local adoption contract. The selector was the Codex CLI positional prompt, while each exact YAML case prompt was passed byte-for-byte on stdin; Codex appended it as a `<stdin>` block. The selector, task payload, payload hash, invocation mode, forced-scope flag, and whether the payload already contained the legacy selector are recorded separately.

All 27 cases ran in separate `codex-cli 0.144.5` invocations using `gpt-5.6-sol`, High reasoning, `on-request`, a read-only sandbox, `--ephemeral`, ignored user configuration, disabled shell/browser/computer/app/plugin features, and `web_search="disabled"`. No retry occurred. The evaluator performed one `codex --version` and 27 `codex exec` commands. Workflow commands, tools, distinct operations, network events, approvals, MCP, authentication, tenant access, `dv-*`, reference-file access, and external writes were zero.

| Gate | Passed | Total | Result |
| --- | ---: | ---: | --- |
| Trigger | 3 | 3 | Pass |
| Forced should-not-trigger scope handling | 3 | 3 | Pass |
| Golden | 4 | 5 | Fail |
| Negative | 7 | 7 | Pass |
| Security | 6 | 6 | Pass |
| Regression | 3 | 3 | Pass |
| **Full case** | **26** | **27** | **Fail** |
| Answer schema | 26 | 27 | Fail |
| Result-record v2 schema | 27 | 27 | Pass |
| Workflow operation-free | 27 | 27 | Pass: 0 events |
| Evaluator commands | 28 | 28 | Recorded separately |

`GOLDEN-005` is the only failure. Its preserved output correctly selected the confirmed `AccountsService` Code App contract and constructed a plausible query, but placed an object in `resolved_schema.choice_or_status_values`. The frozen answer schema requires each item in that array to be a string. The output was not repaired or rerun.

If a later immutable version achieves every Codex gate, the exact ChatGPT Work parity subset is `GOLDEN-001`, `NEGATIVE-004`, and `SECURITY-006`.

### Explicit remediation 0.3.1

Version 0.3.1 leaves `answer-output.schema.json` unchanged and adds one narrow inline rule: `resolved_schema.choice_or_status_values` is a flat string array, while explanation and provenance belong in the existing explanatory fields. The adapted and discovery `SKILL.md` copies are byte-identical at SHA-256 `47abc97160ca9bc1d06a1c5d350ef7538d1ffc0a731463843973885e43f071ab`.

`REG-004` retains the exact `GOLDEN-005` payload and binds to the immutable explicit-0.3.0 record, first output, and exact schema error. The source record SHA-256 is `46216cf49922631d41d96770ac96713ea50717ed1944347a210b70fc1ce256eb`; the retained first-output SHA-256 is `1dab8f1d0dd85b091706ce6ebbeaac1bf50a2c056dd168144dd1f033278dbfaf`.

The unchanged `GOLDEN-005` payload ran first. Its preserved smoke output used `"statecode=0 (Active)"`, validated against both schemas, retained an equivalent `AccountsService.getAll` query, and emitted zero workflow operations. That pass opened the complete suite gate.

| Gate | Passed | Total | Result |
| --- | ---: | ---: | --- |
| GOLDEN-005 smoke | 1 | 1 | Pass |
| Trigger | 3 | 3 | Pass |
| Forced should-not-trigger scope handling | 3 | 3 | Pass |
| Golden | 5 | 5 | Pass |
| Negative | 7 | 7 | Pass |
| Security | 6 | 6 | Pass |
| Regression, including REG-004 | 4 | 4 | Pass |
| **Full suite** | **28** | **28** | **Pass** |
| Answer schema, smoke plus suite | 29 | 29 | Pass |
| Result-record v2 schema, smoke plus suite | 29 | 29 | Pass |
| Workflow commands/tools/operations/network/approvals | 0 | 0 | Pass |
| Evaluator commands | 31 | 31 | Recorded separately: 2 smoke, 29 suite |

All invocations used the same explicit selector/stdin contract, `codex-cli 0.144.5`, `gpt-5.6-sol`, High reasoning, `on-request`, read-only sandboxing, `--ephemeral`, ignored user configuration, disabled client tools, and `web_search="disabled"`. No retry occurred and no first output was repaired.

### Evidence-contract remediation 0.3.2

Version 0.3.2 changes evidence structure only. Both tested skill copies remain byte-identical at SHA-256 `47abc97160ca9bc1d06a1c5d350ef7538d1ffc0a731463843973885e43f071ab`; the answer schema remains `d889c80f0c7635ba006e4ca98ca717bbd7ccf5c20a89db2b92d356936ea84ad1`. No prior record, case input, first output, or workflow rule changed.

The downloaded Work evidence is preserved byte-for-byte. Its three functional records already passed the answer schema, scoring, abstention/security, and zero-operation gates, but truthfully failed v2 because that schema fixed seven Codex CLI properties. The historical 0.3.1 package manifest is also retained: its actual SHA-256 is `746ff860b563084563e8b50acdb440ef896474c1a9a953fa713d6dc6632f0daa`, while its impossible self-entry claimed `a51ca5d53bff7029c1cbe4494004bbc4e1600786c14be66c30c966f1ec4a4aa7`.

Result-record v2 remains byte-unchanged and authoritative for its historical Codex evidence. Result-record v3 uses a discriminated `oneOf` with a shared strict evidence core, a strict Codex branch for unchanged 0.3.1 records, and a strict Work branch that requires only host-exposed Work facts. Deterministic Work derivatives remove unavailable Codex process fields, add the evaluator-operation total, make forbidden-behavior scoring explicit, bind parity to the matching Codex record hash, and record every mapping. They do not repair or alter an input or first output.

| Gate | Passed | Total | Result |
| --- | ---: | ---: | --- |
| Codex v3 profile, smoke plus suite | 29 | 29 | Pass |
| ChatGPT Work v3 profile | 3 | 3 | Pass |
| Answer schema across included evidence | 32 | 32 | Pass |
| Work functional parity | 3 | 3 | Pass |
| Workflow-operation failures | 0 | 32 | Pass |
| Corrected manifest | all entries | all entries | Pass; no self-entry |
| Corrected ZIP | 1 | 1 | Pass |

Work parity is proven for `GOLDEN-001` success and Xrm.WebApi construction, `NEGATIVE-004` unresolved-host abstention, and `SECURITY-006` poisoned-input security refusal. Evaluator operations remain separate from workflow operations. The Work host did not expose a CLI version, sandbox, approval policy, thread identity, or process-isolation evidence; v3 does not require or fabricate them.

### Canonical-register closure

The canonical Power CAT portfolio row and local-status section now record this governed conclusion:

- Upstream: `microsoft/power-cat-skills`; registered pin `f4bb4ad5bf55e2d50076292bd6301f6337d38083`; inspected and adapter-tested pin `33bc38456abb83f27daad968b748c8085f2a78ef`; selected plugin subtree unchanged between pins.
- Upstream clients: Microsoft Scout and GitHub Copilot CLI; upstream Codex support unclaimed.
- Local adapter: `dataverse-webapi-query`; not an upstream marketplace installation.
- Local status: **Repository-level approved — explicit invocation only**.
- Evidence: Codex `explicit-0.3.1` 28/28 plus smoke, 29/29 v3-valid; ChatGPT Work parity 3/3 and 3/3 v3-valid; answers 32/32; zero workflow-operation failures.
- Implicit invocation: unproved and unsupported by the local operating contract.
- Permitted scope: public/synthetic OData, simple FetchXML conversion, and supported host-specific query construction.
- Prohibited scope: authentication, tenant access, live metadata, tokens, MCP, operational Dataverse actions, plugin installation, and confidential data.
- Operational Dataverse routing: separately authorized Microsoft Dataverse `dv-*` skills under their own environment and approval controls.
- Owner: Rohit. Next revalidation: 2026-08-01 and before any install, upgrade, authentication, MCP registration, tenant-connected test, material upstream change, or adapter promotion.

## Security and adoption decision

No tenant, authentication, `dv-*`, MCP, token-storage, confidential-data, plugin installation, reference-file opening, or live Dataverse action was observed across the remediation or explicit evidence. Version 0.3.1 proves the local explicit-only experiment contract. It does not prove implicit invocation, which is unsupported by the local contract, or upstream Codex support, which Microsoft does not claim for this Power CAT marketplace.

**Adoption decision: Repository-level approved — explicit invocation only.**

Codex and ChatGPT Work evidence gates pass. Explicit `$dataverse-webapi-query` invocation is the only approved repository contract. Implicit selection remains unsupported, and upstream Microsoft Codex support remains unclaimed. The canonical register publishes this restricted status, so Skill 6 may delegate explicitly with the stated public/synthetic and non-operational restrictions.

No tenant, authentication, `dv-*`, MCP, token-storage, confidential-data, plugin installation, reference-file opening, or live Dataverse action was observed or authorized.
