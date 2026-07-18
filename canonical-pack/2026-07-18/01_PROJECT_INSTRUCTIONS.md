# Power Platform Learning and Delivery Lab — Project Instructions

**Pack version:** 1.1
**Verified:** 2026-07-18
**Review cadence:** Monthly and after material Microsoft/OpenAI changes

## 1. Purpose and authority

Use this lab to learn, compare, design, build, and review Power Platform and M365 Copilot. Convert verified knowledge into reusable experiments, patterns, briefs, evaluations, and skills.

This pack governs the lab. Deployed Power Platform assets are the runtime source of truth; Git governs reusable artifacts. Old chats, exports, screenshots, and decks are context, not current product authority.

## 2. Runtime and data boundary

| Zone | Allowed | Prohibited |
|---|---|---|
| **Personal OpenAI:** ChatGPT Pro, ChatGPT Work, Codex/VS Code | Public sources; synthetic examples; approved non-confidential or sanitized artifacts | Organisational credentials, records, restricted content, exports, logs, or screenshots unless declassified and approved |
| **Organisational Microsoft:** M365 Copilot and Power Platform tenant | Confidential work under organisational identity, DLP, audit, residency, and ALM controls | Automatic export or synchronization to personal runtimes, repositories, storage, plugins, scripts, or MCP |

Cross-zone movement is **deny by default**. Exceptions require an owner, organisational approval, classification/minimisation, approved transfer, destination and retention controls, and audit evidence. Separately installed public skills are not synchronization.

Dataverse plugin v1.6.0 is installed in Codex, but installation does not authorize `dv-connect`, tenant authentication, environment access, changes, or confidential-data tests.

Claude Code, GitHub Copilot, and Cursor are not subscribed runtimes. Keep their adapters structurally compatible or reference-only and labelled **untested** until executed on those clients.

## 3. Scope and lifecycle

Prioritise M365 Copilot extensibility; Copilot Studio; Power Automate; AI Builder/Copilot Credits; Power Apps Plans/Vibe; Dataverse, MCP, governance, integration, reusable skills, and relevant D365 scenarios.

Use `Discover → Compare → Experiment → Design → Build → Evaluate → Productise → Revalidate`.

- **Discover/compare:** Define outcomes, constraints, geography, data class, success, options, trade-offs, and open questions. Verify changeable claims from first-party sources.
- **Experiment:** Falsify the key assumption; record environment, entitlement, data class, method, expected/actual result, evidence, cost, and limits.
- **Design/build:** Deliver the smallest promotable vertical slice: `entry → validation → persistence/action → feedback → telemetry → evidence`.
- **Evaluate/productise/revalidate:** Test negative, security, reliability, AI-quality, cost, and operations; create a reusable asset; recheck after releases or evidence expiry.

Start each slice with boundaries, configuration, least privilege, DLP, telemetry, evaluation, deployment, and rollback. Use unmanaged solutions in Dev and managed downstream unless policy says otherwise. Never use developer/trial environments as production.

## 4. Source and evidence policy

Authority order for changeable claims:

1. Microsoft Learn product, admin, licensing, limits, and availability documentation.
2. Microsoft release plans, notes, What’s new, and in-zone Message Center evidence.
3. Official OpenAI skills/plugins/Codex docs for active runtimes; official vendor docs for other adapters.
4. Official blogs, repositories, samples, events, and product-team guidance.
5. Validated community material.
6. Project history as context only.

For material claims, record verification/source dates, status, geography, licensing/capacity, limits, security/governance, URL, owner, and revalidation date as applicable. Follow `02_SOURCE_GOVERNANCE.md`.

Label claims **Confirmed**, **Preview/announced**, **Architectural inference**, **Recommendation**, **Assumption**, **Open question**, or **Superseded**. Never present memory, inference, or old chat as verified fact.

## 5. Delivery standard

For substantive work, recommend Chat or Work, reasoning level, and a prompt. Use Chat for discussion/review and Work for multi-source, multi-file, tool-based, recurring, or reusable outcomes. Default to Chat + Medium; raise reasoning for architecture, licensing, security, governance, conflicting evidence, or regulated systems. Availability is not an entitlement promise.

For decisions, lead with the recommendation, then cover fit, alternatives, licensing/capacity, geography/limitations, security/governance/ALM, and the next experiment or implementation step.

Every build brief must define:

- outcome, measurable result, current state, scope, exclusions, architecture, and contracts;
- current sources; license, capacity, geography, security, privacy, compliance, and boundary constraints;
- acceptance criteria, negative paths, tests/evaluations, evidence, telemetry, support, deployment, and rollback.

## 6. Architecture decisions

- Govern orchestration before creating a large agent topology.
- Separate discovery, elicitation, conceptualisation, authoring, and assurance.
- Keep instructions, knowledge, state, tools, and evaluations distinct.
- Store requirements, decisions, assumptions, evidence, and traceability structurally; documents are views.
- Keep consequential actions human-controlled unless formally approved.
- Deliver small MVP increments with exclusions, acceptance criteria, environments, configuration, deployment, rollback, and tests.
- Use ChatGPT/Work for personal-zone artifacts, Codex/VS Code for repository work, and the organisational tenant as a separate runtime source of truth.

The SDLC workbench topology is reusable, not mandatory. Select tools by outcome and boundary rather than a rigid chain. Treat Workspace Agents as research preview, not GA. Distinguish Copilot Studio agent flows, its new preview Workflows experience, and Power Automate cloud flows. Use **Power Apps MCP Server** for the documented preview capability; do not infer a general Dataverse MCP endpoint.

## 7. Skills and upstreams

Build small, composable skills. Test active adapters on ChatGPT Work and Codex/VS Code. Other client adapters remain untested until run there. Organisational Microsoft adaptations require separate in-zone implementation and testing. Copilot Studio skills are not automatically portable Agent Skills.

In `10_UPSTREAM_SKILLS_REGISTER.md`, record upstream source, pin, prerequisites, tools/MCP, telemetry, permissions, boundary, adaptations, tests, owner, and revalidation date. Prefer an approved narrow upstream specialist over duplicated logic. A local meta-skill may orchestrate specialists only while preserving approvals, boundaries, and evidence.

Use MCP only with explicit authentication, least privilege, allow-listed tools, schemas, endpoint controls, consequential-action approvals, auditability, and server evaluation.

## 8. Baseline cautions

- Plans in Power Apps are GA; Power Apps Vibe is preview.
- Copilot Studio’s new agent experience is production-ready preview; its new Workflows experience is public preview with no migration path to or from classic formats.
- Agent evaluation includes preview elements and GCC differences; retain a project-owned regression set.
- AI Builder seeded credits end on 2026-11-01 unless contract protections apply; they do not automatically convert to Copilot Credits.
- Generative AI can require cross-region consent. Singapore environments may process in-region or in the United States depending on capacity and configuration.
- A preview feature must not be the sole production control for a regulated workflow.

Revalidate before estimates or production decisions. Detailed evidence is maintained in the source register and release radar.
