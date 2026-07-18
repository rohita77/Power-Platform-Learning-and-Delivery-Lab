# Skill Design Standard

**Pack version:** 1.0  
**Verified:** 2026-07-18  
**Applies to:** Reusable Power Platform/M365 Copilot expertise and its platform adapters

## Recommendation

| Layer | Standard | Rule |
|---|---|---|
| Portable core | Agent Skills-compatible folder where supported | Put the stable workflow and reusable resources here |
| Live product facts | Versioned references/source register, not frozen prose | Reverify before consequential decisions |
| Tool/data access | MCP or supported platform tool/connector | Explicit auth, allow-list, schemas, least privilege, approvals |
| Platform behavior | Thin adapter | Do not fork the domain workflow unless the target cannot support it |
| Quality | Golden cases + platform-specific integration/security tests | A skill is not reusable until tests pass |
| Distribution | Versioned package/plugin/repository | Include changelog, compatibility, update, and rollback |

## 1. When to create a skill

Create a skill when the lab has a repeatable workflow with a stable trigger, clear output, and evaluation criteria. Good candidates include design reviews, source verification, licensing assessment, build-brief creation, and production-readiness checks.

Do not create a skill for:

- one answer or one client-specific decision;
- unverified preview behavior;
- a large agent persona containing unrelated workflows;
- knowledge that should be retrieved live from authoritative sources;
- privileged actions without an approved tool/security design.

## 2. Required structure

```text
skill-name/
  SKILL.md                 # required: metadata, trigger boundary, workflow
  references/              # authority hierarchy, stable domain rules, source pointers
  templates/               # outputs/contracts/checklists
  scripts/                 # optional deterministic helpers
  examples/                # positive, negative, edge examples
  tests/                   # golden cases, security, integration, regression
  adapters/
    openai/
    claude/
    github-copilot/
    m365-declarative-agent/
    copilot-studio/
  changelog.md
```

For OpenAI/Codex, the minimal skill directory contains `SKILL.md`; optional `scripts`, `references`, and `assets` are supported. Keep the portable core within the open Agent Skills conventions and isolate platform extensions in adapters.

## 3. SKILL.md contract

### Front matter

```yaml
---
name: lowercase-hyphenated-name
description: >-
  What the skill does, when it must trigger, and the material exclusions.
version: 0.1.0
owner: team-or-role
last_verified: YYYY-MM-DD
---
```

Only `name` and `description` are universally safe assumptions for the portable core. Put platform-specific metadata in the adapter, not in shared front matter unless the target standard explicitly supports it.

### Required body sections

1. Outcome and non-goals.
2. Trigger and do-not-trigger conditions.
3. Required inputs and bounded assumptions.
4. Source authority and revalidation rule.
5. Workflow with decision points.
6. Output contract.
7. Security, privacy, geography, licensing/capacity, and approval rules.
8. Failure and stop conditions.
9. Evaluation/tests to run.
10. Carry-forward/change-log behavior.

## 4. Design rules

### Small and composable

One skill should own one coherent outcome. Prefer composition:

`current-feature-verifier → component-selector → build-brief → production-review`

Avoid a single “Power Platform Expert” skill that tries to research, architect, build, deploy, support, and train every product.

### Progressive disclosure

- Put trigger-critical guidance in the description.
- Keep `SKILL.md` concise enough to load safely.
- Move detailed product matrices, templates, and scripts to referenced files.
- Load only the reference required for the current path.

### Explicit state labels

Require `Confirmed`, `Preview/Announced`, `Inference`, `Recommendation`, `Assumption`, `Open`, and `Superseded`. Never let an adapter drop these labels.

### Deterministic interfaces

When a skill feeds automation, define a schema. Example:

```json
{
  "recommendation": "string",
  "status": "GA|PREVIEW|PLANNED|DEPRECATED|UNKNOWN",
  "verifiedOn": "YYYY-MM-DD",
  "licenseCapacity": ["string"],
  "geography": ["string"],
  "limitations": ["string"],
  "securityGovernance": ["string"],
  "sources": [{"title": "string", "url": "https://..."}],
  "openQuestions": ["string"]
}
```

Validate the schema and define a safe error path. Do not repair malformed output invisibly when downstream action is consequential.

## 5. Source and currency standard

- Store durable methodology in the skill; retrieve volatile product facts at runtime or from an expiry-controlled register.
- Each current capability claim must carry verification date, status, license/capacity, geography/language, limitations, and security/governance.
- If authoritative sources are unavailable or conflict materially, return `Open` and stop before a production recommendation.
- Community examples can inform tests or implementation technique but cannot establish license, status, data residency, or contractual behavior.

## 6. Security standard

Before installation or publishing, review:

- instructions for prompt injection, data exfiltration, hidden side effects, and scope escalation;
- scripts/dependencies for provenance, pinning, secrets, filesystem/network access, destructive operations, and supply-chain risk;
- MCP servers/connectors for authentication, tool inventory, input/output schema, endpoint restriction, least privilege, tenancy, logging, rate limiting, and revocation;
- consequential actions for approval, idempotency, confirmation, rollback, and audit;
- references/examples for confidential data and retention;
- adapter permissions separately—portable instructions do not imply portable authorization.

Default rules:

- Read-only first.
- Explicit tool allow-list.
- User identity for user-delegated access unless an approved service identity is necessary.
- Separate read and write tools.
- Human confirmation for external messages, financial/customer decisions, deployments, permission changes, and destructive writes.
- No production secrets or customer data in skill packages or golden tests.

## 7. Test standard

Every skill needs:

| Test class | Minimum |
|---|---|
| Trigger | 3 should-trigger and 3 should-not-trigger cases |
| Golden functional | 5 representative success cases |
| Negative | Missing/ambiguous input, unsupported capability, stale source, conflicting evidence |
| Security | Prompt injection, tool poisoning, unauthorized source/action, secret request |
| Output contract | Schema/required-section validation |
| Cross-platform | Same three golden cases on every claimed adapter |
| Regression | Previously fixed failure retained as a test |
| Human review | At least one expert-reviewed case for architecture/licensing/security skills |

Record platform, model/runtime, skill version, date, inputs, outputs, score, deviations, and reviewer.

Suggested release gates:

- no critical security or scope failures;
- 100% valid output contracts;
- 100% correct abstention on unsupported/insufficient-evidence cases;
- at least 90% golden-case pass rate before pilot;
- no platform adapter claims without integration evidence.

## 8. Adapter standard

| Target | Adapter approach | Current caution |
|---|---|---|
| ChatGPT Work / Codex | Agent Skill; plugin when distributing skills/connectors | Admin enablement, sandbox, approvals, plan/surface availability |
| Claude Code | Agent Skill plus Claude-specific invocation/subagent/context controls if needed | Keep extensions out of portable core |
| GitHub Copilot / VS Code | Repository or user Agent Skill; add repo instructions only for repo-wide conventions | Availability differs by surface; test cloud and IDE paths separately |
| M365 declarative agent | Translate workflow into instructions, knowledge, actions, manifest, and evals | It is not a `SKILL.md` runtime; honor M365 permissions/admin controls |
| Copilot Studio | Translate into agent instructions, tools, prompts, flows/workflows, or preview skill assets | New experience/skills are preview; ALM and feature gaps require testing |

An adapter must document unsupported semantics and must not silently omit approval, security, or evidence rules.

## 9. Versioning and change management

Use semantic versioning:

- PATCH: wording, examples, or nonbehavioral source refresh.
- MINOR: backward-compatible workflow/test/adapter capability.
- MAJOR: trigger, output contract, security model, or decision behavior changes.

Changelog entry:

```text
Version/date:
Reason/source change:
Behavior changed:
Adapters affected:
Tests added/updated:
Migration/rollback:
Next revalidation:
```

Deprecate rather than delete when consumers may still depend on a skill. State replacement, end date, and migration tests.

## 10. Review checklist

- [ ] Narrow outcome and exclusions.
- [ ] Clear trigger description.
- [ ] Required inputs and bounded assumptions.
- [ ] Current-source and expiry rules.
- [ ] Status/license/geography/limits/security included where relevant.
- [ ] Deterministic output contract.
- [ ] Safe failure/abstention path.
- [ ] Tool/MCP permissions and approval boundary.
- [ ] Golden, negative, security, and regression tests.
- [ ] Each adapter tested and gaps documented.
- [ ] Owner, version, changelog, rollback, revalidation.

## Official sources

- [OpenAI: Build skills](https://developers.openai.com/codex/build-skills)
- [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [GitHub Copilot Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [Copilot Studio skills overview (preview)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview)
- [Copilot Studio MCP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp)

