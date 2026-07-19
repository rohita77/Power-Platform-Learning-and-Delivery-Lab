# Power CAT Dataverse Web API Query Codex Experiment

This public-source, synthetic-data experiment evaluates a repository-level Codex adaptation of Microsoft Power CAT `dataverse-webapi-query`. It does not install the Power CAT marketplace, invoke the installed Dataverse plugin, authenticate, access a tenant, handle tokens, or make live Dataverse calls. Upstream Codex support remains unclaimed.

## Layout and evidence

- `adapted-skill/dataverse-webapi-query/` is the reviewed adaptation source.
- `.agents/skills/dataverse-webapi-query/` is its byte-identical discovery copy.
- `tests/results/codex/*.json` contains the untouched original 20-case baseline.
- `tests/results/codex/remediation-0.2.0/` contains the complete 27-case first remediation run.
- `tests/results/codex/remediation-0.2.1/` contains the single stopped follow-up invocation.
- `tests/results/codex/remediation-0.2.2/smoke/` contains the immutable initial implicit-discovery smoke failure.
- `tests/results/codex/remediation-0.2.2/smoke-2/`, `smoke-3/`, and `smoke-4/` contain separately preserved zero-tool implicit smoke failures.
- `tests/results/codex/remediation-0.2.2/diagnostic/` contains the passing explicit-skill control; no 0.2.2 suite directory was created.
- `tests/results/codex/explicit-0.3.0/` contains the immutable 27-case explicit-invocation evaluation and manifest.
- `tests/results/codex/explicit-0.3.1/` contains the passing `GOLDEN-005` smoke, complete 28-case remediation suite, and separate immutable manifests.
- `tests/results/chatgpt-work/2026-07-19/raw/` contains the four byte-unchanged downloaded Work artifacts; `v3/` contains three deterministic host-profile derivatives.
- `tests/result-record-v2.schema.json` remains the immutable historical Codex-specific contract. `tests/result-record-v3.schema.json` adds strict discriminated Codex and ChatGPT Work profiles.
- `powercat-dataverse-work-parity-0.3.2.zip` is the corrected deterministic cross-host evidence package; its manifest excludes itself, the ZIP, and temporary files.
- Run manifests bind each remediation run to exact skill and answer-schema hashes.

The 0.2.0 run preserved 27 exit-zero outputs with no tool or approval events, but none of the 24 applicable answers satisfied the exact answer schema. Version 0.2.1 embedded the full contract inline; its first output was schema-valid, but the invocation emitted two `command_execution` events. Version 0.2.2 made the runtime body self-contained and added detailed event attribution. Its initial implicit smoke produced an invalid answer and three distinct web searches. The documented search control then eliminated all workflow events. An explicit `$dataverse-webapi-query` control produced a valid abstention with zero workflow events, proving the skill body can execute safely. Three natural-prompt smokes using corrected metadata and repository routing still bypassed the inline contract. All outputs remain preserved and hash-bound; the 27-case suite was not started.

Version 0.3.0 evaluates a different local contract: repository-level use requires explicit `$dataverse-webapi-query` selection, and implicit natural-prompt selection is outside the contract. All 27 exact fixture payloads ran in separate explicit Codex CLI invocations. Twenty-six passed full review, all 27 result records validate, and workflow commands, tools, operations, network events, and approvals were zero. `GOLDEN-005` failed the answer schema because `choice_or_status_values` contained an object rather than the required string item; its first output is preserved unchanged.

Version 0.3.1 adds only a flat-string serialization instruction and retained `REG-004`. The gated `GOLDEN-005` smoke passed, followed by a 28/28 explicit suite. All 29 new answers and result records validate, workflow operations are zero, no retry occurred, and the answer schema is byte-unchanged.

Version 0.3.2 changes no adapter instruction, answer contract, input, first output, or prior result. It preserves the Work parity download, adds a strict cross-host evidence schema, and creates three deterministic Work derivatives whose unavailable Codex-only execution fields are absent rather than fabricated. The v3 Codex profile validates the unchanged 0.3.1 smoke and suite 29/29; the Work profile validates 3/3; all 32 included answers validate; functional parity passes 3/3; and workflow-operation failures are zero.

## Missing-reference boundary

| Reference | Classification | Controlled boundary |
| --- | --- | --- |
| `webapi-syntax.md` | Optional | Basic preserved operators only; advanced lambdas, paging-cookie mechanics, and undocumented operators are unsupported. |
| `metadata-discovery.md` | Unsupported | MCP, `EntityDefinitions`, environment discovery, and live metadata access are prohibited. |
| `fetchxml-mapping.md` | Optional | Simple entity/filter and single-link mappings only; complex or nested mappings abstain. |
| `common-errors.md` | Optional | Only errors directly attributable to supported syntax; catalog/authentication diagnosis is unsupported. |
| `aggregation.md` | Unsupported | Conceptual FetchXML fallback only; no runnable aggregate or client-side workaround. |
| `authentication.md` | Unsupported | Authentication, token, browser, Postman, MSAL, and live-test paths are prohibited. |
| `examples.md` | Optional | Not an authority and not required for narrow supported cases. |
| `power-apps-contexts.md` | Optional | Narrow preserved host mappings only; advanced contracts abstain and generated service names must be confirmed. |

## Proof boundary and decision

Static checks cover structure, provenance, copy equality, schemas, unchanged fixture hashes, links, placeholder hygiene, preserved evidence, and package integrity. Executed Codex evidence covers only the recorded CLI/model/configuration with shared repository and machine state. ChatGPT Work evidence covers the host-exposed functional output and evaluator events; it does not invent a CLI version, sandbox, approval policy, thread ID, or process-isolation claim. Neither surface proves implicit selection, live tenant, authentication, operational Dataverse use, or user-level installation. Upstream Power CAT Codex support remains unclaimed.

Current adoption decision: **Repository-level approved — explicit invocation only**. The permitted scope is synthetic OData, simple FetchXML conversion, and supported host-specific query construction. Explicit `$dataverse-webapi-query` selection is mandatory. Implicit selection is unsupported; authentication, tenant access, live metadata, MCP, tokens, confidential data, and operational Dataverse actions remain prohibited. Authenticated Dataverse work routes separately to authorized `dv-*` skills. The canonical upstream register records this restricted status, so Skill 6 may delegate only through the explicit selector and these boundaries.

## Validation

From this directory:

```bash
python3 tests/apply_review.py
python3 tests/apply_review.py --run-id remediation-0.2.1 --review tests/remediation-review-0.2.1.yaml
python3 tests/apply_review.py --run-id remediation-0.2.2 --review tests/remediation-review-0.2.2-smoke.yaml --results tests/results/codex/remediation-0.2.2/smoke
python3 tests/apply_review.py --run-id remediation-0.2.2 --review tests/remediation-review-0.2.2-smoke-2.yaml --results tests/results/codex/remediation-0.2.2/smoke-2
python3 tests/apply_review.py --run-id remediation-0.2.2 --review tests/remediation-review-0.2.2-smoke-3.yaml --results tests/results/codex/remediation-0.2.2/smoke-3
python3 tests/apply_review.py --run-id remediation-0.2.2 --review tests/remediation-review-0.2.2-smoke-4.yaml --results tests/results/codex/remediation-0.2.2/smoke-4
python3 tests/apply_review.py --run-id remediation-0.2.2 --review tests/remediation-review-0.2.2-diagnostic.yaml --results tests/results/codex/remediation-0.2.2/diagnostic
python3 tests/apply_review.py --run-id explicit-0.3.0 --review tests/explicit-review-0.3.0.yaml --results tests/results/codex/explicit-0.3.0
python3 tests/apply_review.py --run-id explicit-0.3.1 --review tests/explicit-review-0.3.1-smoke.yaml --results tests/results/codex/explicit-0.3.1/smoke
python3 tests/apply_review.py --run-id explicit-0.3.1 --review tests/explicit-review-0.3.1-suite.yaml --results tests/results/codex/explicit-0.3.1/suite
python3 tests/build_evidence_contract_032.py
python3 tests/validate_experiment.py
python3 tests/build_parity_package_032.py
unzip -t powercat-dataverse-work-parity-0.3.2.zip
```

All review commands have already been applied and only reproduce the same hash-bound scoring. The validator reports structural evidence as passing, Codex v3 at 29/29, Work v3 at 3/3, answer validity at 32/32, Work parity at 3/3, and zero workflow failures. Result directories are immutable evidence; configure a new run ID for any later behavior or evidence-contract revision rather than overwriting them.
