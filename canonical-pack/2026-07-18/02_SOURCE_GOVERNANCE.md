# Source Governance

**Pack version:** 1.0  
**Verified:** 2026-07-18  
**Purpose:** Keep the lab current without turning old answers into product authority

## Recommendation

| Decision | Standard |
|---|---|
| Product truth | Current first-party product documentation plus tenant evidence |
| Historical chats/GPT outputs | Context, decisions, hypotheses, and test-case donors only |
| Status claims | Quote the source’s status label; never infer GA from a working tenant |
| Licensing | Use current licensing/credit guides and contract terms; label estimates |
| Geography | Record environment geography, cloud, language, processing location, and required consent |
| Conflicts | Prefer the more specific and more recently updated first-party source; record unresolved conflict |
| Revalidation | Risk-based expiry plus event-triggered review |

## 1. Authority levels

| Level | Source | Permitted use |
|---|---|---|
| A1 | Microsoft Learn limits, licensing/admin/security docs, licensing guides, release plans | Product behavior, status, prerequisites, limits, governance, capacity |
| A2 | Official OpenAI/GitHub/VS Code/Anthropic/Agent Skills docs | Behavior of those platforms and portability adapters |
| A3 | Official product release notes, “What’s new,” Message Center, product blogs/repos | Rollout, change detection, direction, examples; validate material behavior against A1/A2 where possible |
| B | Microsoft MVP or recognized community material | Practical technique or test hypothesis only after first-party validation |
| C | Lab experiment evidence | Confirmed behavior for the recorded tenant, region, license, build, and date; not universal product proof |
| D | Chats, GPT outputs, screenshots, decks, course notes, copied web text | Historical context, decision rationale, backlog seeds, and evaluation cases only |

## 2. Claim record

Every material claim should be representable as:

```yaml
claim_id: PP-AREA-0001
statement: ""
evidence_label: Confirmed | Preview | Announced | Inference | Recommendation | Assumption | Open | Superseded
authority_level: A1 | A2 | A3 | B | C | D
product: ""
capability: ""
release_status: GA | production-ready preview | public preview | experimental | planned | deprecated | unknown
cloud: Commercial | GCC | GCC High | DoD | Sovereign | all-confirmed
geography: ""
language: ""
license_entitlement: ""
meter_capacity: ""
limitations: []
security_governance: []
source_url: ""
source_last_updated: YYYY-MM-DD | unknown
verified_on: YYYY-MM-DD
verified_by: ""
valid_until: YYYY-MM-DD
supersedes: []
notes: ""
```

## 3. Verification procedure

1. Define the exact claim and decision it affects.
2. Find the most specific current A1/A2 source.
3. Check page last-updated date, explicit status banner, prerequisites, supported geographies/languages, license/metering, limits, and security notes.
4. Cross-check release notes or release plans when rollout/status is material.
5. For licensing, distinguish list-price examples, entitlement rules, capacity rates, tenant contract terms, and zero-rated scenarios.
6. For geography, distinguish tenant location, environment region, data at rest, inference/processing location, disaster recovery, and connected-service location.
7. Record known limitations and what was not confirmed.
8. Where risk warrants, run a tenant experiment and record the full context.
9. Assign a validity window and owner.
10. Update dependent patterns, skills, experiments, and backlog items if the claim changes.

## 4. Conflict resolution

When sources disagree:

1. Prefer product documentation over marketing and blogs.
2. Prefer a capability-specific page over a general overview.
3. Prefer a current licensing guide over remembered pricing or a community calculator.
4. Prefer an explicit status banner over an inferred status from availability.
5. Prefer current tenant evidence only for that tenant/configuration; it does not override public contractual documentation.
6. Record both sources, the conflict, the chosen working position, and confidence.
7. Escalate unresolved licensing, residency, or regulated-control questions to the Microsoft account team, legal/compliance, or the relevant administrator.

## 5. Revalidation intervals

| Risk/volatility | Examples | Maximum age |
|---|---|---:|
| Very high | Preview features, Copilot Credit rates, model availability, regional rollout | 14 days |
| High | Licensing, security controls, DLP, identity, ALM limitations | 30 days |
| Medium | GA product behavior and limits | 90 days |
| Low | Architectural principles and internal delivery standards | 180 days |

Revalidate immediately after a Message Center notice, release-plan status change, deprecation, major model/runtime change, security incident/advisory, licensing guide update, or a tenant test that contradicts the register.

## 6. Status language

- **GA:** Use only when the official source says generally available or the applicable release-plan status is GA.
- **Production-ready preview:** Preserve Microsoft’s exact label; it remains preview and may lack classic features or migration.
- **Public preview:** Not the default production dependency; require an exit plan and explicit acceptance.
- **Experimental:** Lab-only unless an approved exception exists.
- **Planned:** Backlog/research only; do not design a committed production dependency around it.
- **Deprecated:** Stop new adoption and create a migration plan.
- **Unknown:** Treat as not approved until verified.

## 7. Licensing and capacity rules

- Do not treat a maker license, runtime entitlement, capacity pack, connector entitlement, and end-user right as interchangeable.
- Record who/what is licensed: maker, end user, flow, process, bot/agent, environment, tenant, or Azure meter.
- Separate included/zero-rated Microsoft 365 Copilot employee usage from autonomous/event-triggered or unlicensed-user usage.
- Estimate the complete path: orchestration + grounding + tool/prompt + flow actions + external services.
- Record enforcement behavior, not only cost. For example, exhausted agent-flow prepaid capacity blocks new agent-flow runs.
- Mark prices and rates “verify before purchase/production.” Contract terms override public summaries.

## 8. Geography and security rules

For Singapore and other regulated deployments, record:

- Microsoft Entra tenant home location and Power Platform environment region;
- customer data at-rest location;
- AI inference/processing location and cross-region consent state;
- Bing, Microsoft 365 service, external-model, and connector processing paths;
- data classification, sensitivity labels, retention, eDiscovery/audit expectations;
- agent/flow identity, credential mode, least-privilege roles, endpoint controls, and DLP grouping;
- human approval for writes, external communication, financial/customer decisions, privilege changes, or destructive actions.

Microsoft currently documents Singapore-hosted Power Platform environments as using Azure OpenAI in-region or in the United States, depending on capacity and configuration. Treat this as a design input and confirm the tenant’s exact controls before using sensitive data.

## 9. Minimum evidence for production recommendations

A production recommendation is incomplete without:

- current first-party status and license evidence;
- applicable cloud/region/language confirmation;
- documented limitations and preview dependencies;
- threat/data-flow analysis and DLP/identity design;
- ALM/deployment/rollback path;
- representative functional, security, reliability, and AI evaluation evidence;
- operational owner, monitoring, capacity alerts, and revalidation date.

## 10. Seed authoritative sources

- [M365 Copilot extensibility release notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)
- [M365 Copilot extensibility — what’s new](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new)
- [Copilot Studio — what’s new](https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new)
- [Copilot Studio billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management)
- [Power Platform release plans](https://learn.microsoft.com/en-us/power-platform/release-plan/)
- [Power Platform licensing overview](https://learn.microsoft.com/en-us/power-platform/admin/pricing-billing-skus)
- [Power Automate limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config)
- [Power Platform generative AI geography](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot)
- [OpenAI Work mode admin FAQ](https://developers.openai.com/codex/enterprise/work-admin-faq)
- [OpenAI build skills](https://developers.openai.com/codex/build-skills)
- [GitHub Copilot Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)
- [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills)

