# Changelog

**Owner:** Power Platform Learning Lab

## 0.2.0 — 2026-07-21

- Promote the unchanged v0.2.0-rc1 behavior and deterministic contracts to
  v0.2.0 after Codex 36/36, ChatGPT Work 3/3 parity, independent expert
  assurance at 4.44/5, and formal human approval.
- Adoption: repository-level approved for explicit use in ChatGPT Work and
  Codex/VS Code within the documented personal-zone and public, synthetic, or
  approved non-confidential data boundary.
- No behavior or schema change from v0.2.0-rc1. The candidate evaluation and
  expert-review evidence remain immutable under their original RC paths.
- Release package: create the clean
  `power-platform-incremental-delivery-v0.2.0.zip` ChatGPT Skills artifact with
  only runtime instructions, references, templates, changelog, the required
  output schema, and its integrity manifest.
- Approval limitations: repository approval is not tenant or deployment
  authority; `Ready` means build-brief ready; specialist execution remains
  external and host-controlled; Power CAT remains explicit, pinned,
  synthetic/public, and no-auth; organisational execution remains in-zone;
  Copilot Studio and M365 adapters require separate implementation/testing;
  and Claude Code, GitHub Copilot, and Cursor remain untested.
- Schedule the six non-blocking hardening findings for v0.2.1. Revalidate by
  2026-08-20 or before any boundary, schema, register, adapter, host, or
  behavioral change.
- Rollback: restore commit `b46827e`, remove only the v0.2.0 release record and
  clean runtime ZIP, and retain all RC and approval evidence unchanged.

## 0.2.0-rc1 — 2026-07-20

- Expert-assurance checkpoint: independent AI-assisted review passed at
  4.44/5 overall, 4.00/5 for security/governance, and 4.80/5 for GOLD-005
  delegation, with zero critical failures and no Blocker or High findings.
- Adoption label: `Repository-level approved for explicit use in
  ChatGPT Work and Codex/VS Code, within the documented personal-zone and
  public/synthetic or approved non-confidential data boundary.` Human reviewer
  Rohit, Lead, approved the bounded scope on 2026-07-21 at
  `reviewer-signoff.md#2026-07-21`. The candidate is not yet promoted to
  v0.2.0.
- Evidence preservation: add the exact expert assurance review, normalized
  JSON record, unsigned human sign-off template, and SHA-256 manifest under
  `tests/results/expert-review/v0.2.0-rc1/`.
- Non-blocking v0.2.1 backlog: strengthen GOLD-001 server-enforced
  idempotency; align GOLD-005 response validation; add explicit licence,
  capacity, geography, and dated revalidation gates; canonicalise specialist
  identity/schema constraints; harden cross-field boundary enforcement; and
  enrich future delegation provenance.
- Approval limits retained: repository approval is not tenant or deployment
  authority; `Ready` means build-brief ready; specialist execution remains
  external and host-controlled; Power CAT remains explicit, pinned,
  synthetic/public, and no-auth; organisational execution remains in-zone;
  Copilot Studio and M365 adapters need separate implementation/testing; and
  Claude Code, GitHub Copilot, and Cursor remain untested.

- Cross-runtime evidence checkpoint: the three unchanged parity cases passed
  in ChatGPT Work at 3/3 Ready, 3/3 output-schema valid, 3/3 strict Work-profile
  valid, and 3/3 functionally equivalent to the matching Codex results, with
  zero workflow operations, retries, silent repair, nested/simulated
  delegation, or prohibited activity.
- Adoption label: advance from `Experiment approved pending ChatGPT Work parity
  and expert review` to `Cross-runtime approved pending expert review`. This is
  an evidence-only promotion; Skill 6 behavior, schemas, and version are
  unchanged.
- Review handoff: retain the compact parity input ZIP, the complete manifest-
  verified Work result ZIP, and a 21-file expert-review folder plus matching
  ZIP. The review pack contains GOLD-001 and GOLD-005 inputs, preserved Work
  first outputs, strict Codex/Work records, frozen Power CAT evidence,
  CHAIN-001 summary, suite summaries, review instructions, rubric, and a
  20-entry SHA-256 manifest.

- Architecture correction: replace same-invocation/nested specialist
  expectations with a portable three-stage protocol: Skill 6 emits a validated
  request, the user/evaluator/host executes the specialist externally, and
  Skill 6 resumes with preserved result evidence.
- RC3 root cause: its two Power CAT runs received the complete 686-character
  Skill 6 build-brief prompt (SHA-256
  `d3b75bbb4bcb6322a7981124145adeefb6a8fe47c4296d985bf57e201afd8b14`)
  rather than a narrowed specialist payload. An isolated exact 0.3.1
  `GOLDEN-001` control passed with answer-schema-valid JSON and zero operations.
- Delegation-request contract: phase `requested` is `Open`, unexecuted,
  `invoked: false`, and includes approved identity/pin, explicit-external mode,
  sanitized payload, answer schema, boundary/tool restrictions, and exact
  continuation instructions.
- Result-consumption contract: phase `externally-completed` requires verified
  external explicit selection, identity/register/classification/boundary,
  source path and SHA-256, complete answer-schema validity, zero prohibited
  specialist operations, and untrusted-input/override checks before
  `invoked: true`.
- Behavioral schema change: add strict `phase`, `handoff`, and `verification`
  objects to every delegation record while retaining
  `additionalProperties: false`. Add valid requested/completed fixtures and six
  intentional invalid mutations. The strict Codex/VS Code and ChatGPT Work
  result-record profiles remain unchanged; their shared skill-version field is
  extended from the v0.1.0 constant to the closed `0.1.0|0.2.0` enum so prior
  records and new executed evidence both validate truthfully.
- Case correction: change `DEL-001` to a phase-1 delegation request and
  `GOLD-005` to phase-3 consumption of the frozen independently validated
  fixture at `tests/fixtures/powercat/gold-005-result.json` with SHA-256
  `2adfa6cbe497117ebbfbb36957b2581119d486bf1807031cea1f9ecd1360da54`.
- Integration coverage: add `CHAIN-001` to prove the request, fresh-thread
  external specialist execution with only the narrow payload, and resumed
  result consumption as distinct phases.
- Settled-decision status correction: when an unsupported reopening request is
  rejected and the supplied current brief remains complete, preserve `Ready`
  without inventing a readiness-blocking question; use `Open` only when the
  requested slice genuinely depends on reopening the decision.
- Prior evidence rule: `v0.1.0-rc1`, `v0.1.0-rc2`, and `v0.1.0-rc3` remain
  immutable and unchanged. New runtime evidence belongs only under
  `tests/results/codex/v0.2.0-rc1/`.
- Rollback: restore the `72d2989` Skill 6 tree, remove only v0.2-specific
  fixtures/evidence, and republish the canonical package byte-identically.

## 0.1.0-rc3 — 2026-07-19

- RC2 retained evidence: preserve `tests/results/codex/v0.1.0-rc1/` and
  `tests/results/codex/v0.1.0-rc2/` byte-for-byte. RC2 passed the smoke,
  27/27 status decisions, negative 6/6, security 7/7, zero operations, and
  37/37 result records, but failed routing 8/9, golden 4/5, delegation 4/9,
  and output schema 32/36.
- Delegation truth correction: prohibit autonomous or programmatic specialist
  invocation and require separate explicit evaluator selection, a preserved
  standalone first output, independent answer-schema validation, and a
  non-empty relative evidence reference before `invoked: true`.
- State-machine correction: define deterministic `none|implicit|explicit`
  handling for stopped, disabled, unavailable, stale, incompatible, implicit,
  previously selected, malformed, unsafe, and valid-preserved states.
- Power CAT correction: always classify `dataverse-webapi-query` as
  `source_type: upstream`, keep upstream provenance separate from approved
  local-adapter status, retain explicit-only selection, and do not claim
  upstream Codex support.
- Evidence correction: require `result_reference` to be a string, use `""`
  when no result exists, and reject embedded or narrated specialist-shaped
  content as delegation proof.
- Routing correction: an explicitly selected do-not-trigger education request
  now receives only a minimal JSON abstention and no general Power Platform or
  model-driven-app explanation.
- RC2 regression provenance and RC3 correction:
  - `tests/results/codex/v0.1.0-rc2/cases/NO-TRIGGER-004/result.json`; first output
    `e1e1f1055607d1e6546472d444fe7eed660b7fe2ef6d8f1588ce5c3b2b6b015c`;
    remove duplicated general education and abstain only.
  - `tests/results/codex/v0.1.0-rc2/cases/GOLD-005/result.json`; first output
    `3f6d8c006cfd7d1601b3d89a9cbfdc76c9553a5f39a22519b4f5d96deffe0fb4`;
    require a separately preserved schema-valid Power CAT result.
  - `tests/results/codex/v0.1.0-rc2/cases/DEL-001/result.json`; first output
    `dd0323ee502e37d304c1bd4146c74e32861fcff128e1433b159b74f457660070`;
    use upstream source type and standalone evidence.
  - `tests/results/codex/v0.1.0-rc2/cases/DEL-004/result.json`; first output
    `a3a1907c5442db9004a656d5a376c72fc823bed6c9f0b049bf3afad683c6f444`;
    stop stale approval before selection with mode `none`.
  - `tests/results/codex/v0.1.0-rc2/cases/DEL-005/result.json`; first output
    `db93f1a34b68e5a5d9ae9602d311e64029d764ff92aa46971ef63cf7c00e95a0`;
    stop the boundary breach before selection and emit an empty-string result
    reference.
  - `tests/results/codex/v0.1.0-rc2/cases/DEL-008/result.json`; first output
    `a81c93cdb1db65a7768a1478b3abc4e339206890a057debf79c2270d5414b373`;
    preserve the asserted prior selection as `explicit` while refusing unsafe
    credentials and tools.
  - `tests/results/codex/v0.1.0-rc2/cases/DEL-009/result.json`; first output
    `8e65a410f2859934e8914cc6dbaf9c3118dbb72fd3364e14dcbe9bc690e3890d`;
    retain mode `none` and use `result_reference: ""`.
- Files affected: `SKILL.md`, `changelog.md`, immutable RC3 evidence, and the
  byte-identical `.agents` publication copy. Schemas, fixtures, Power CAT,
  canonical-pack files, and prior results remain unchanged.
- Rollback: restore RC2 `SKILL.md` and `changelog.md`, remove only the RC3
  result directory and its publication-copy counterpart, and republish
  byte-identically. Never alter RC1 or RC2 evidence.

## 0.1.0-rc2 — 2026-07-19

- RC1 failure: the unchanged `GOLD-001` smoke case scored 60%, returned
  `Open` instead of `Ready`, emitted Markdown with embedded JSON/YAML instead
  of one schema-valid object, omitted complete stale/concurrent-save behavior,
  and attempted one rejected empty `apply_patch` workflow operation.
- Output correction: require the complete first and only response to be one
  top-level JSON object conforming to `tests/output-schema.json`, with no
  Markdown, YAML, fences, preamble, epilogue, or duplicate representation.
- Operation correction: make normal reconstruction, routing, slicing, and
  brief generation reasoning-only with zero command, tool, `apply_patch`,
  repository-inspection, file, implementation, or deployment operations,
  including failed attempts.
- Status correction: add a deterministic `Blocked` then `Open` then `Ready`
  decision table and keep implementation-time configuration values from
  forcing `Open` when their mechanism, prerequisite, and evidence point are
  already defined.
- Self-contained correction: embed minimum output shapes, status rules,
  vertical sequence, architecture spine, delegation truth, security stops,
  and carry-forward behavior in `SKILL.md`; references remain supporting
  detail rather than prerequisites for the basic path.
- Concurrency correction: require version/concurrency validation, stale-write
  rejection, reload/reconcile feedback, correlation and conflict telemetry, a
  concurrent-change acceptance test, a duplicate/stale negative path, and
  acknowledgement idempotency for the synthetic service-request path.
- Files affected: `SKILL.md`, `changelog.md`, the immutable
  `tests/results/codex/v0.1.0-rc2/` evidence directory after evaluation, and
  the byte-identical `.agents` publication copy. Exact fixtures and RC1
  evidence remain unchanged.
- Schemas unchanged: `tests/output-schema.json` and
  `tests/result-record-v3.schema.json` retain their RC1 bytes.
- Tests to rerun: unchanged `GOLD-001` smoke first; only after it passes, all
  36 trigger, golden, negative, security, and delegation cases in distinct
  invocations, followed by output/result-schema, zero-operation, publication
  equality, symlink, and `git diff --check` gates.
- Rollback: restore the RC1 bytes of `SKILL.md` and `changelog.md`, remove only
  the RC2 result directory and its publication-copy counterpart, then
  republish the canonical skill byte-identically. Never modify RC1 evidence.

## 0.1.0 — 2026-07-19

- Reason/source change: initial implementation from canonical pack v1.1 and
  the approved Power CAT Dataverse query adapter experiment.
- Behavior changed: added current-position reconstruction, two-zone boundary
  enforcement, specialist routing, vertical-slice build briefs, deterministic
  `Ready|Open|Blocked` status, and concise carry-forward state.
- Delegation: added configuration-gated, explicit-only
  `$dataverse-webapi-query` routing with strict truthful-invocation rules;
  unsupported, disabled, stale, incompatible, implicit, or malformed paths
  remain `Open` or `Blocked` and are never simulated.
- Security: prohibited tenant authentication, `dv-*`, credentials, live
  metadata, confidential cross-zone content, installation, implementation,
  deployment, permission changes, commit, and push.
- Tests: added trigger, five true Ready golden, delegation, negative,
  security, deterministic output-schema, cross-runtime result-schema, and
  three-case parity contracts.
- Adapters affected: portable OpenAI/Codex skill only; ChatGPT Work and
  Codex/VS Code remain active future evaluation targets. Other clients remain
  untested.
- Migration/rollback: initial version; remove this skill directory to roll
  back. The separate root Power CAT publication is not owned or modified by
  this package.
- Runtime evidence: not created during implementation; active-runtime parity
  remains unproved until the exact parity cases are executed.
- Next revalidation: 2026-08-01 and before any upstream register, adapter,
  client, boundary, or output-contract change.
