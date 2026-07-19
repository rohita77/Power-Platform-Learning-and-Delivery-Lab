# Changelog

## 0.3.2-evidence-contract-remediation - 2026-07-19

- Preserved the three ChatGPT Work records and final parity summary byte-for-byte under `tests/results/chatgpt-work/2026-07-19/raw/`; retained the invalid 0.3.1 self-hashing manifest separately as historical evidence.
- Left both `SKILL.md` copies, the answer schema, every input, all prior result records, and adapter behavior unchanged.
- Retained result-record v2 unchanged for historical Codex evidence and added result-record v3 with strict discriminated Codex and ChatGPT Work profiles.
- Created three deterministic Work v3 derivatives with immutable raw hashes, exact inputs and first outputs, explicit normalization mappings, separate forbidden-behavior scoring, evaluator-operation counts, and hash-bound Codex parity evidence.
- Validated unchanged Codex 0.3.1 evidence 29/29, Work evidence 3/3, all included answers 32/32, Work functional parity 3/3, and zero workflow-operation failures.
- Rebuilt the parity package with a manifest that excludes itself, the ZIP, and temporary files; both checksum and ZIP integrity gates pass.
- Decision: **Repository-level approved — explicit invocation only**. Implicit invocation and upstream Codex support remain unclaimed; tenant, authentication, MCP, token, confidential-data, and operational Dataverse use remain prohibited.
- Closed the experiment by publishing the restricted adapter decision to the canonical upstream register. Skill 6 may delegate only through explicit `$dataverse-webapi-query` selection; all operational Dataverse work remains separately authorized `dv-*` routing.

## 0.3.1-explicit-remediation - 2026-07-19

- Strengthened only the inline serialization instruction: `resolved_schema.choice_or_status_values` must contain flat string items, with rationale routed to the existing explanatory fields. The answer schema remained byte-unchanged.
- Added `REG-004`, bound to the immutable explicit-0.3.0 `GOLDEN-005` record SHA-256 `46216cf49922631d41d96770ac96713ea50717ed1944347a210b70fc1ce256eb`, first-output SHA-256 `1dab8f1d0dd85b091706ce6ebbeaac1bf50a2c056dd168144dd1f033278dbfaf`, and exact schema error.
- Ran the unchanged `GOLDEN-005` input first. The smoke passed answer and result schemas, emitted `"statecode=0 (Active)"`, preserved equivalent query behavior, and recorded zero workflow operations.
- Ran 28 separate explicit suite invocations with no retries. Trigger passed 3/3, forced scope routing 3/3, Golden 5/5, Negative 7/7, Security 6/6, and Regression 4/4.
- Answer-schema and result-schema validity are 29/29 across smoke plus suite. Workflow commands, tools, distinct operations, network events, and approvals are zero; 31 evaluator commands are recorded separately.
- Decision: **Experiment approved pending ChatGPT Work parity**. Implicit invocation remains unproved and outside the local contract; upstream Codex support remains unclaimed. The canonical register, commit history, and remote were untouched.

## 0.3.0-explicit-evaluation - 2026-07-19

- Froze the unchanged repository adapter at SHA-256 `3676edda1b2a65b1ca1a2303851dae69cf4c5e0aba54325cadd52a47d0da05c2` and evaluated only explicit `$dataverse-webapi-query` selection.
- Preserved all 27 YAML task payloads byte-for-byte on stdin, recorded the selector separately, and disclosed the 21 payloads that already contained the legacy selector.
- Ran 27 separate `codex-cli 0.144.5` invocations with `gpt-5.6-sol`, High reasoning, read-only sandboxing, disabled web search and client tools, and no retries.
- Recorded zero workflow commands, tools, distinct operations, network events, or approvals; 28 evaluator commands were recorded separately.
- Passed trigger 3/3, should-not-trigger 3/3, negative 7/7, security 6/6, and regression 3/3. Golden passed 4/5.
- Preserved `GOLDEN-005` unchanged after it emitted an object in `choice_or_status_values`, whose frozen answer schema requires string items. Answer-schema validity is 26/27; result-schema validity is 27/27.
- Decision remains **Reference only**. Implicit invocation remains unproved and outside the local contract; Work parity is not the only remaining gate. The canonical register, commit history, and remote were untouched.

## 0.2.2-experiment - 2026-07-19

- Replaced the disabled-but-retained upstream runtime body with a self-contained controlled subset; bundled references are now provenance/evaluator artifacts only.
- Added smoke-first execution, read-only sandboxing, disabled shell/browser/computer/app/plugin/search features, detailed workflow/evaluator event attribution, immutable fixture hashes, and a new versioned result directory.
- Ran an initial implicit repository-discovery smoke with `gpt-5.6-sol`, High reasoning, `on-request`, and `--ephemeral`. It exited zero but failed the inline contract and performed three distinct web searches represented by six lifecycle events.
- Used the current official Codex manual and model-visible prompt debugger to identify two harness/trigger defects: the supported search control is top-level `web_search="disabled"`, and the previous description excluded unresolved prompts from implicit selection.
- Corrected both defects, added explicit implicit-invocation metadata, and preserved a second smoke using the exact same prompt under a new case ID and thread. It emitted zero commands, tools, approvals, or network events, but still did not apply the inline contract.
- Added a separately recorded explicit `$dataverse-webapi-query` control. It returned the exact schema-valid Open abstention with zero workflow events, proving safe body execution when selected explicitly.
- Strengthened the frontmatter trigger and repository routing, then preserved two further exact-prompt implicit smokes. Both remained zero-tool but bypassed the inline contract.
- Preserved all smoke and diagnostic first outputs, applied separate hash-bound reviews, and kept the 27-case suite blocked.
- Decision remains Reference only. Repository-level approval and ChatGPT Work parity were not reached; the canonical register, commit history, and remote were untouched.
- Migration impact: the client configuration demonstrably removes web search and explicit skill execution passes, but this Codex CLI did not implicitly select the repository skill for the natural prompt. Future work requires a client/runtime implicit-selection change or separately authorized experiment version, not another output-format repair.
- Rollback: retain all evidence directories and restore the preceding adaptation only in a separately versioned change.
- Upstream pin: `33bc38456abb83f27daad968b748c8085f2a78ef`.

## 0.2.1-experiment - 2026-07-19

- Embedded the complete answer contract in `SKILL.md` after 0.2.0 proved that the no-tools runtime could not reliably reproduce the referenced schema shape.
- Corrected conditional JSON Schema rules and explicitly authorized standard synthetic assumptions in the affected golden fixtures.
- Preserved the exact 0.2.0 outputs and bound both runs to skill/schema hashes.
- Stopped after the first 0.2.1 case emitted two prohibited `command_execution` events; no retry or remaining invocation ran.
- Migration impact: consumers must use the complete structured contract and strict schema/host abstention rules.
- Rollback: restore the 0.1.0 adaptation and its byte-identical discovery copy; retain all result directories as evidence.
- Upstream pin: `33bc38456abb83f27daad968b748c8085f2a78ef`.
- Next revalidation: 2026-08-01 or before any new run, install, authentication, or promotion.
- Decision remains Reference only; no canonical-register edit, commit, or push.

## 0.2.0-experiment - 2026-07-19

- Added strict unresolved-schema and host-context abstention, four result types, answer/result schemas, missing-reference classifications, seven negative cases, six security cases, and three regressions.
- Revised the Code App golden fixture to confirm its generated service name and preserved the original baseline prompt/output.
- Ran 27 separate Codex CLI invocations: all exited zero, no tools/approvals occurred, but all 24 applicable outputs failed the exact answer schema.
- Preserved every first output unchanged and recorded the failure as a contract-delivery defect.

## 0.1.0-experiment - 2026-07-19

- Pinned and compared the selected Power CAT skill at registered and current commits.
- Added a Codex-compatible, public/synthetic safety wrapper and repository discovery copy.
- Recorded missing upstream references and disabled live authentication, MCP, browser, and tenant paths.
- Added trigger, golden, negative, security, result-schema, runner, and validation assets.
- Executed 20 separate Codex CLI invocations: 18 passed and 2 negative cases failed.
- Recorded the first-experiment adoption decision as Reference only.
- No plugin installation, authentication, tenant access, live Dataverse call, canonical-register update, or commit.
