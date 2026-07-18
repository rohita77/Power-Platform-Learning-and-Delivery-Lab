# Changelog

**Owner:** Rohit Acharya, Power Platform Learning Lab

## 0.1.0 — 2026-07-18

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
- Remaining release evidence: execute and record golden parity on ChatGPT Work
  and Codex/VS Code plus expert review; local static checks are not runtime
  proof.
