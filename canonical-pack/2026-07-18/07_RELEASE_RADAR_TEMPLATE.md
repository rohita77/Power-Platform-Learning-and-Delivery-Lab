# Weekly Power Platform Release Radar — Template

**Pack version:** 1.1
**Verified:** 2026-07-18  
**Recommended schedule:** Friday, 8:00 AM Asia/Singapore  
**Reporting window:** Previous seven days plus newly discovered future-dated changes

## Run instruction

```text
Every Friday at 8:00 AM Singapore time, summarize material Microsoft 365
Copilot, Copilot Studio, Power Automate, AI Builder, Power Apps, Dataverse,
Power Platform ALM/governance, OpenAI skills/plugins, and tracked Microsoft
upstream skill/plugin changes.

Use current first-party sources. For each material item record what changed,
verification date, release status, rollout geography/cloud/language, licensing
or capacity impact, limitations, security/governance/ALM impact, and which lab
claims, experiments, patterns, or skills need revalidation. Separate confirmed
changes from announced/planned changes. Do not use old project chats as product
authority.

Run public-source research in the personal OpenAI zone. Review confidential
tenant rollout evidence only in the organisational Microsoft zone. Never
automatically synchronize Message Center, tenant, environment, or customer
content into the personal-zone report.
```

## Executive summary

**Week ending:** YYYY-MM-DD  
**Prepared:** YYYY-MM-DD HH:mm SGT  
**Overall signal:** Green / Amber / Red

| Decision/action | Why it matters | Owner | Due |
|---|---|---|---|
|  |  |  |  |

## Material changes

| ID | Product/capability | What changed | Status | Rollout/geo/language | License/capacity | Limits | Security/governance/ALM | Source and updated date | Lab impact | Action |
|---|---|---|---|---|---|---|---|---|---|---|
| RAD-YYYY-WW-01 |  |  | GA/preview/planned/deprecated |  |  |  |  |  |  |  |

## Status transitions

| Capability | Previous status | New status | Evidence | Production decision |
|---|---|---|---|---|
|  |  |  |  |  |

## Licensing and capacity watch

Track at minimum:

- Copilot Credit rate or enforcement changes;
- Microsoft 365 Copilot included/zero-rated boundaries;
- AI Builder 2026 credit transition and contract guidance;
- Power Automate Premium/Process/RPA/request limits;
- Managed Environment/pipeline rights;
- model/BYOM/external-service charges;
- trial/developer environment restrictions.

| Change | Effective date | Affected workloads | Forecast variance | Decision/mitigation |
|---|---|---|---|---|
|  |  |  |  |  |

## Geography, privacy, and security watch

| Change | Cloud/region/language | Data at rest / processing impact | DLP/identity/audit impact | Required review |
|---|---|---|---|---|
|  |  |  |  |  |

## Deprecations and deadlines

| Deadline | Product/change | Current dependency | Replacement | Owner | Status |
|---|---|---|---|---|---|
| 2026-11-01 | Seeded AI Builder credits end, subject to contract terms |  | Copilot Credits/active add-on/architecture change |  |  |

## Project revalidation queue

| Claim/pattern/skill ID | Trigger | Risk | Required work | Owner | Due |
|---|---|---|---|---|---|
|  |  | High/Medium/Low |  |  |  |

## Upstream skills and plugins watch

Reconcile each item with `10_UPSTREAM_SKILLS_REGISTER.md`. Record a new exact commit/version before adopting an update.

| Repository | Previous pin | Current upstream | Client/support change | Prerequisite/tool/telemetry/permission change | Boundary impact | Test required | Owner |
|---|---|---|---|---|---|---|---|
| `microsoft/Dataverse-skills` |  |  |  |  |  | ChatGPT Work/Codex or static only |  |
| `microsoft/power-platform-skills` |  |  |  |  |  | ChatGPT Work/Codex or static only |  |
| `microsoft/power-cat-skills` |  |  |  |  |  | ChatGPT Work/Codex or static only |  |
| `microsoft/skills-for-copilot-studio` |  |  |  |  |  | ChatGPT Work/Codex or static only |  |

## Experiments to add or rerun

| Experiment | Hypothesis/change | Environment/region/license | Acceptance evidence | Priority |
|---|---|---|---|---|
|  |  |  |  |  |

## No-material-change areas

List checked sources/product areas with no material change. This proves coverage and prevents silence from being misread as “not reviewed.”

## Required source sweep

- [Microsoft 365 Copilot release notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)
- [M365 Copilot extensibility — what’s new](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new)
- [M365 Copilot extensibility known issues](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/known-issues)
- [Copilot Studio — what’s new](https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new)
- [Copilot Studio billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management)
- [Copilot Studio quotas and limits](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas)
- [Power Platform release plans](https://learn.microsoft.com/en-us/power-platform/release-plan/)
- [Power Platform licensing overview](https://learn.microsoft.com/en-us/power-platform/admin/pricing-billing-skus)
- [Power Automate limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config)
- [AI Builder credit transition](https://learn.microsoft.com/en-us/ai-builder/endofaibcredits)
- [Power Apps Plans](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/plan-designer)
- [Power Apps Vibe](https://learn.microsoft.com/en-us/power-apps/vibe/overview)
- [Power Platform governance guidance — what’s new](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/whats-new)
- [OpenAI skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [OpenAI build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI plugins](https://learn.chatgpt.com/docs/plugins)
- [Microsoft Dataverse skills](https://github.com/microsoft/Dataverse-skills)
- [Microsoft Power Platform skills](https://github.com/microsoft/power-platform-skills)
- [Microsoft Power CAT skills](https://github.com/microsoft/power-cat-skills)
- [Microsoft skills for Copilot Studio](https://github.com/microsoft/skills-for-copilot-studio)
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/)
- [Claude Code release notes](https://docs.anthropic.com/en/release-notes/claude-code)

GitHub and Claude sources are reference-adapter change signals only; those clients are not subscribed or mandatory test dependencies. For tenant-specific rollout, separately review Microsoft 365 Message Center and the Power Platform admin center inside the organisational Microsoft zone. Record sanitized Message Center IDs when approved, but do not copy confidential tenant content into the personal-zone report or a public skill package.

## Quality gate

- [ ] Every material claim has a first-party link and verification date.
- [ ] Release status and rollout are explicit.
- [ ] License/capacity and enforcement—not only price—are covered.
- [ ] Geography, security, governance, and ALM impact are assessed.
- [ ] Affected source-register entries and skills are named.
- [ ] Upstream pins, telemetry, permissions, supported clients, and test status are reconciled.
- [ ] Personal/organisational zone boundary is recorded; no automatic synchronization occurred.
- [ ] Planned/preview items are not described as GA.
- [ ] “No change” coverage is recorded.
- [ ] Owners and deadlines are assigned.
