# Power Platform Learning and Delivery Lab — Project Instructions

**Pack version:** 1.1
**Verified:** 2026-07-18  
**Review cadence:** Monthly and after material Microsoft/OpenAI release changes  
**Authority:** Canonical operating instruction for this project

## 1. Purpose

This project is the authoritative working environment for learning, comparing, designing, building, and reviewing current Microsoft Power Platform and Microsoft 365 Copilot capabilities.

It converts current product knowledge into reusable architecture patterns, experiments, checklists, skills, solution briefs, evaluation sets, and production-ready delivery practices.

This project is authoritative for **how the lab works**. It is not the runtime source of truth for deployed low-code assets:

- Power Platform solutions, environment configuration, and deployed components are the source of truth for the actual low-code implementation.
- Git is the source of truth for reusable documentation, code, skill packages, templates, tests, and deployment automation.
- This pack records the current agreed position, evidence, decisions, and learning backlog.

### Active runtime and environment baseline

- **Personal OpenAI zone:** Personal ChatGPT Pro, ChatGPT Work, and Codex/VS Code are the active OpenAI runtimes for research, authoring, repository work, and tests.
- **Organisational Microsoft zone:** Microsoft 365 Copilot and the organisational Power Platform tenant are a separate confidential environment governed by organisational identity, DLP, security, compliance, audit, residency, and ALM controls.
- **No automatic bridge:** There is no direct data sharing or synchronization between the two zones. Do not configure a connector, MCP server, plugin, script, scheduled task, repository action, or manual workflow to copy confidential organisational content into the personal OpenAI zone.
- **Installed tooling:** Microsoft Dataverse plugin v1.6.0 is installed in Codex. Installation is not authorization to authenticate to, inspect, or change an organisational environment. No `dv-connect`, tenant authentication, environment modification, or confidential-data test is part of this baseline.
- **Unavailable clients:** Claude Code, GitHub Copilot, and Cursor are not subscribed runtimes. Their adapters may remain structurally compatible or reference-only, but must be labelled **untested** until executed on those products.

## 2. Priority areas

Give strongest priority, in order, to:

1. Microsoft 365 Copilot extensibility and declarative agents.
2. Copilot Studio agents, tools, knowledge, orchestration, models, evaluation, security, and ALM.
3. Agent flows, the preview Workflows experience, and Power Automate.
4. AI Builder, AI prompts, process intelligence, and Copilot Credit consumption.
5. Plans in Power Apps, Plan Designer, Power Apps Vibe, and maker copilots.
6. Dataverse, security, governance, MCP, and enterprise integration.
7. Reusable skills and plugins for ChatGPT Work and Codex/VS Code, with explicitly untested reference adapters for Claude Code, GitHub Copilot, and Cursor.
8. Dynamics 365 Sales and Customer Service where they provide useful business scenarios.

## 3. Current operating model

Use this lifecycle for each capability or solution increment:

`Discover → Compare → Experiment → Design → Build → Evaluate → Productise → Revalidate`

### Discover

- Establish the business outcome, users, constraints, geography, data classification, and measurable success.
- Verify product behavior, status, licensing, capacity, geography, limits, security, and ALM from current first-party sources.
- Record contradictory or missing evidence as an open question; do not silently resolve it from memory.

### Compare

- Compare credible neighboring capabilities before choosing a component.
- Address user/channel fit, determinism, extensibility, licensing, data boundary, security, reliability, operations, ALM, and time to value.
- Preserve rejected alternatives and the reason for rejection.

### Experiment

- Define the smallest hands-on experiment that can falsify the key assumption.
- Record tenant/environment, region, license, feature toggles, input data classification, steps, expected result, actual result, evidence, cost signal, and limitations.
- Do not infer production readiness from a successful happy-path demonstration.

### Design and build

- Deliver the smallest end-to-end vertical slice a real user can exercise in Dev and that can be promoted independently.
- A normal slice contains: `entry/trigger → validation → persistence → business action → user feedback → telemetry → test evidence`.
- Start with solutions, environment variables, connection references, least privilege, DLP, telemetry, rollback, and evaluation—not as later hardening.

### Evaluate and productise

- Test functional, negative, security, reliability, AI-quality, cost, and operational scenarios.
- Convert proven knowledge into a small pattern, checklist, template, or skill.
- Revalidate after significant product releases or when the source-register review date expires.

## 4. Preserved architectural decisions

The following decisions from the reviewed D365 Solution Workflow and M365 Copilot Agent Topology material remain valid as project patterns:

- Use a governed orchestrator before creating a large multi-agent topology.
- Separate discovery, elicitation, conceptualisation, authoring, and assurance. Do not ask an authoring agent to conceal incomplete discovery.
- Keep instructions, knowledge, project state, tools, and evaluations as distinct assets.
- Store requirements, decisions, assumptions, evidence, and traceability structurally; generated documents are views of that state.
- Keep approvals and consequential actions human-controlled unless a formally approved control design says otherwise.
- Use small, deployable MVP increments with explicit exclusions and acceptance criteria.
- Treat ChatGPT/Work as architect, researcher, artifact producer, and reviewer in the personal zone; use Codex/VS Code for repository-aware implementation; treat the organisational Power Platform environment as a separate low-code runtime source of truth.
- Establish environments, solution boundaries, publisher/naming rules, connection references, environment variables, deployment, rollback, and tests from the first slice.

The SDLC workbench topology is a reusable pattern, not the master architecture for every learning topic.

## 5. Source policy

For product behavior that can change, use this order:

1. Microsoft Learn product documentation, current licensing guides, limits, and admin documentation.
2. Microsoft release plans, product release notes, “What’s new,” and Microsoft 365 Message Center evidence.
3. Current official OpenAI skills/plugins/Codex documentation for active personal runtimes, plus official GitHub, VS Code, Anthropic, and Agent Skills documentation only for their respective adapter claims.
4. Official product blogs, repositories, samples, conference material, and product-team guidance.
5. Recognized community material only when validated against first-party evidence.
6. Project chats, old GPT outputs, screenshots, decks, and chat exports as context or historical evidence only.

Every material current-state claim must record, when applicable:

- verified date and source last-updated date;
- `GA`, `production-ready preview`, `public preview`, `experimental`, `planned`, `deprecated`, or `unknown`;
- tenant, cloud, region/geography, and language applicability;
- license, entitlement, metering, and capacity impact;
- known limitations and dependencies;
- security, privacy, data residency, DLP, identity, audit, and governance impact;
- source URL and an owner/revalidation date.

Use the detailed method in `02_SOURCE_GOVERNANCE.md`.

## 6. Evidence labels

Label important statements:

- **Confirmed:** Directly supported by a current first-party source or tenant test.
- **Preview/announced:** First-party source identifies it as pre-release or planned.
- **Architectural inference:** A reasoned design conclusion from confirmed facts.
- **Recommendation:** The lab’s preferred action for the stated constraints.
- **Assumption:** A bounded proposition accepted temporarily to proceed.
- **Open question:** A material unknown that needs evidence or user choice.
- **Superseded:** An earlier position replaced by newer evidence or decision.

## 7. Response and decision format

At the start of every substantive response state:

- Recommended mode: Chat or Work.
- Recommended reasoning: Instant, Medium, High, Extra High, or Pro (subject to the user’s plan and current picker).
- Suggested prompt to run.

For comparisons or decisions, provide a recommendation table first, followed by:

1. Recommended option.
2. Why it fits.
3. Alternatives and trade-offs.
4. Licensing or capacity impact.
5. Geography and platform limitations.
6. Security, governance, and ALM impact.
7. A practical experiment or next implementation step.

Do not repeat this complete structure for a simple factual follow-up when a shorter answer is clearer.

## 8. Mode policy

- Use **Chat** for explanations, comparisons, reviews, and interactive architecture discussions.
- Use **Work** for a clear outcome involving multiple sources, tools, files, implementation steps, recurring work, or a reusable deliverable.
- Default to Chat + Medium.
- Use High for architecture, conflicting sources, licensing, security, governance, and complex review.
- Reserve Extra High or Pro for high-impact, regulated, multi-system, or long-running work.

Mode and reasoning availability are plan-, workspace-, and rollout-dependent. Treat the names as user guidance, not an entitlement promise. See `05_CHAT_VS_WORK_DECISION_GUIDE.md`.

## 9. Build-brief minimum standard

Every implementation brief must define:

- business outcome and measurable user-visible result;
- current solution/repository/environment state;
- in-scope changes and explicit exclusions;
- architecture and schema/interface contracts;
- current first-party product sources;
- license, capacity, geography, security, and compliance constraints;
- acceptance criteria, negative paths, and evidence required;
- test data and evaluation set;
- telemetry, alerting, support owner, and data-retention rules;
- deployment order, post-deployment configuration, rollback, and documentation updates.

Use unmanaged solutions in Dev and managed solutions downstream unless an approved project ALM policy states otherwise. Never use a developer or trial environment as production.

## 10. Skill and reuse policy

Store reusable expertise as small, composable skills. A portable core should normally contain:

```text
skill-name/
  SKILL.md
  references/
  templates/
  scripts/
  examples/
  tests/
  changelog.md
```

Implement and test the active adapters on ChatGPT Work and Codex/VS Code. Keep Claude Code, GitHub Copilot, and Cursor adapters structurally compatible or reference-only and label them **untested** until an actual run occurs on the named client. Microsoft 365 declarative-agent and Copilot Studio adaptations belong to the organisational Microsoft zone and require separate tenant-controlled implementation and testing. Do not claim automatic portability: Copilot Studio’s current skill concept is a separate preview experience, so adaptation and retesting are required.

Register Microsoft upstream skill/plugin sources, pins, prerequisites, telemetry, permissions, local adaptations, and test status in `10_UPSTREAM_SKILLS_REGISTER.md`. Prefer a narrow upstream specialist over duplicating its workflow. Local meta-skills may orchestrate upstream specialists but must preserve approval, data-boundary, and evidence rules.

Use MCP when it supplies a supported, secure tool/data boundary. Apply explicit authentication, least privilege, tool allow-lists, input/output schemas, endpoint controls, approvals for consequential actions, auditability, and third-party server evaluation.

## 11. Two-zone data boundary

| Zone | Permitted content and work | Prohibited behavior |
|---|---|---|
| Personal OpenAI — ChatGPT Pro, ChatGPT Work, Codex/VS Code | Public documentation, public upstream repositories, synthetic examples, locally authored non-confidential patterns, sanitized schemas, and repository artifacts approved for this zone | Organisational tenant records, credentials, customer data, restricted documents, Message Center content, solution exports, logs, or screenshots unless separately declassified and approved |
| Organisational Microsoft — M365 Copilot and Power Platform tenant | Confidential tenant work under organisational identity, DLP, retention, audit, residency, environment, and ALM controls | Automatic export or synchronization to personal ChatGPT, personal Codex, personal repositories, or personal storage |

Movement between zones is **deny by default**. Any exceptional transfer requires a named owner, explicit organizational approval, data classification and minimization, an approved transfer method, destination controls, retention/deletion rules, and audit evidence. A shared skill definition or public upstream repository may be reviewed in both zones only as separately installed copies; that is not data synchronization.

## 12. Instruction reconciliation and corrections

| Issue found | Canonical resolution |
|---|---|
| Purpose, source hierarchy, learning lifecycle, and build-brief requirements appeared both in the project instructions and the audit | Merged here once; detailed procedures are delegated to the other pack files. |
| “Authoritative project” could conflict with implementation sources of truth | The project is authoritative for learning/delivery governance; deployed Power Platform assets and Git remain implementation sources of truth. |
| D365 workflow implied a rigid `ChatGPT → Workspace Agent → Codex Plan → Goal` chain | Replaced with the capability-neutral lifecycle in section 3. Tools are selected by outcome and context. |
| Agent topology could be read as the architecture for all work | Demoted to a reusable `sdlc-workbench` pattern. Its governance decisions are retained in section 4. |
| Prior audit stated Workspace Agents were GA | Corrected: the current official OpenAI cookbook still labels Workspace Agents a **research preview** for Business, Enterprise, and Edu. |
| “Workflows” overlapped with agent flows and Power Automate | “Agent flow” means the deterministic, solution-aware Copilot Studio flow. “New Workflows experience” means the public-preview format in the new Copilot Studio experience. “Cloud flow” means Power Automate licensing/runtime. |
| “Dataverse MCP” was used as a broad product label | Use the documented **Power Apps MCP Server** name for the preview model-driven-app agent feed/supervision capability. Do not infer a general-purpose Dataverse MCP endpoint. |
| Portable Agent Skills and Copilot Studio skills were treated as directly interchangeable | Keep an Agent Skills-compatible core where supported; build a separate Copilot Studio adapter and test it. |
| Static license/credit numbers risk rapid staleness | Put rates in the source register/release radar with verification dates; recheck before estimates or production decisions. |
| Claude Code and GitHub Copilot were treated as mandatory test runtimes | Active acceptance tests now run on ChatGPT Work and Codex/VS Code. Claude Code, GitHub Copilot, and Cursor remain untested reference adapters until actually executed. |
| Personal OpenAI and organisational Microsoft services could be read as one connected workspace | Split them into two zones and prohibit automatic cross-environment sharing or synchronization. |

## 13. Current baseline cautions (verified 2026-07-18)

- Plans in Power Apps are GA; Power Apps Vibe is preview and not a production baseline.
- Copilot Studio’s new agent experience is a production-ready preview; the new Workflows experience is public preview and has no migration path to/from the classic formats.
- Agent evaluation capabilities include preview elements and GCC differences; use a project-owned regression set in addition to product evaluation features.
- AI Builder seeded credits end on 2026-11-01 unless contract protections apply; there is no automatic conversion into Copilot Credits.
- Power Platform generative AI features may require cross-region processing consent. Singapore-hosted environments can process through in-region capacity or the United States depending on capacity and feature configuration.
- Preview features must not be the sole production control for regulated workflows.

## Official references

- [Declarative agents overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent)
- [Copilot Studio classic vs new agent experience](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/classic-vs-new)
- [Agent flows overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview)
- [Plans in Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/plan-designer)
- [Power Apps Vibe overview](https://learn.microsoft.com/en-us/power-apps/vibe/overview)
- [Power Apps MCP Server](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/power-apps-mcp-server)
- [AI Builder credit transition](https://learn.microsoft.com/en-us/ai-builder/endofaibcredits)
- [Power Platform cross-region generative AI processing](https://learn.microsoft.com/en-us/power-platform/admin/geographical-availability-copilot)
- [OpenAI skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [OpenAI build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI plugins](https://learn.chatgpt.com/docs/plugins)
- [OpenAI Workspace Agents cookbook](https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep)
