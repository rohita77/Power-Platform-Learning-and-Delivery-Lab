# Changelog

**Owner:** Rohit Acharya, Power Platform Learning Lab

## 0.1.0 — 2026-07-18

### Release-candidate remediation

- Corrected the SKILL.md OpenAI/Codex workflow sentence.
- Replaced the package-breaking canonical repository link with a concise,
  self-contained source-governance reference that retains canonical Learning
  Lab provenance.
- Corrected all 21 applicable Codex result-record schema paths to resolve the
  packaged output schema from the dated result directory.
- Added dimension-complete Codex scoring for GOLD-001, GOLD-002, and GOLD-005,
  including each named dimension, score, evidence, deviation, and result.
- Reconciled execution status: ChatGPT Work GOLD-001, GOLD-002, and GOLD-005
  executed and passed; the full Codex suite executed with administrative
  scoring remediation applied.
- Retained Claude Code, GitHub Copilot, and Cursor as runtime-untested.
- Recorded Rohit Acharya's signed GOLD-005 named human expert review as Pass on
  2026-07-18 while preserving the tenant-specific `Open` production gate.

### Pre-release corrections

- Declared package owner and version outside portable SKILL.md front matter.
- Declared that v0.1.0 has no upstream skill/plugin runtime dependencies and
  clarified that public first-party documentation is a source dependency.
- Recorded the Python 3.12.3 validation baseline and pinned PyYAML 6.0.1 and
  jsonschema 4.10.3 in `requirements-dev.txt`.
- Added `REG-001` to prevent an `Open` result from carrying
  `production_recommendation: true`.
- Added durable Codex, ChatGPT Work, and human-review result directories plus a
  result-record JSON Schema.
- Recorded dated static structure reviews for Claude Code, GitHub Copilot, and
  Cursor while retaining runtime status as untested.

### Initial package

- Reason/source change: initial implementation from Learning Lab canonical pack
  v1.1.
- Behavior: added narrow current-feature claim verification, atomic claims,
  live first-party source requirement, evidence/release labels, risk-based
  revalidation, and mandatory `Open` abstention for material gaps/conflicts.
- Security: added personal-versus-organisational two-zone boundary; prohibited
  tenant authentication, environment access, Dataverse invocation, plugin
  installation, confidential data, secrets, and cross-zone synchronization.
- Outputs: added decision report, YAML claim record, and JSON Schema contract.
- Tests: added trigger, five golden scenarios, stale/conflict negatives,
  prompt-injection/secret/tenant/cross-zone security cases, and schema fixtures.
- Adapters: ChatGPT Work and Codex are active mandatory test targets; Claude
  Code, GitHub Copilot, and Cursor are untested deferred clients; M365 Copilot
  and Copilot Studio runtime adaptations are deferred.
- Migration/rollback: initial version; remove the package to roll back.
- Next revalidation: 2026-08-17 or earlier after a material Agent Skills,
  client, source-governance, security, or product-documentation change.
- Named expert evidence: GOLD-005 human review passed and was signed on
  2026-07-18. The review does not establish tenant-specific production
  readiness or change `production_recommendation: false`.
