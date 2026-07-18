# Learning Backlog

**Pack version:** 1.0  
**Baseline verified:** 2026-07-18  
**Planning horizon:** 12 weeks for Wave 1; rolling quarterly thereafter

## Recommended sequence

| Wave | Outcome | Priority |
|---|---|---|
| 1 | Establish source governance, tenant guardrails, evaluation harness, and three comparison labs | P0 |
| 2 | Build one governed SDLC workbench slice using a declarative agent, Copilot Studio, and deterministic automation | P0 |
| 3 | Test Plans/Vibe productionisation, AI Builder credit transition, and Power Apps MCP supervision | P1 |
| 4 | Package proven practices into cross-platform skills and adapters | P1 |

## Definition of done for a learning item

An item is done only when it has:

- a current first-party source record with status, license/capacity, geography, limits, and security/ALM notes;
- a comparison with adjacent capabilities;
- a reproducible experiment with environment/region/license context;
- expected and actual results with evidence;
- at least one negative/security/cost test;
- a decision or explicit “not yet proven” conclusion;
- an update to a pattern, checklist, skill, or backlog;
- a revalidation date and owner.

## Shared Wave 1 foundation

| ID | Item | Experiment/output | Acceptance evidence |
|---|---|---|---|
| LAB-FND-01 | Create a source-register workflow | Apply `03_SOURCE_REGISTER_TEMPLATE.md` to 10 live claims | All mandatory metadata populated; stale/conflicting claim workflow exercised |
| LAB-FND-02 | Define tenant learning zones | Developer/sandbox, governed test, production boundary; DLP and region map | Approved environment/identity/DLP matrix and no preview feature in production path |
| LAB-FND-03 | Create common agent evaluation set | 30 cases: answer quality, abstention, source authority, permission trimming, prompt injection, tool selection, write approval | Versioned test set with deterministic + LLM + human scoring |
| LAB-FND-04 | Establish cost telemetry | Copilot Credits, Power Automate requests, AI Builder/Copilot fallback, external model cost | Dashboard/export and alert thresholds demonstrated |
| LAB-FND-05 | Establish ALM baseline | Solution boundaries, env vars, connection refs, managed deployment, rollback | Dev→Test deployment and rollback evidence |

---

## A. Microsoft 365 Copilot and declarative agents

### Current baseline

**Confirmed:** Declarative agents tailor Microsoft 365 Copilot using instructions, knowledge, and actions. Agent Builder suits quick/simple agents; Agents Toolkit or Copilot Studio provides deeper integration/ALM. Existing Microsoft 365 permissions remain the data-access boundary.

**Licensing/capacity:** Microsoft 365 Copilot licensed employee usage has included scenarios. Copilot Chat users can incur usage-based Copilot Credits when agents access shared tenant data. Instructions/public web grounding can be non-metered; recheck the knowledge-source matrix before design.

**Geography/limits:** Host, cloud, language, and capability availability varies. Agent Builder has known mobile, Teams Chat, auto-sharing, Lockbox, and Customer Managed Key limitations. Government capability differs across GCC, GCCH, and DoD.

**Security/governance:** Use Microsoft 365 admin controls, existing ACLs, Purview/DLP/retention, audit, trusted knowledge/actions, prompt-injection defenses, and human approval for sensitive actions.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| DA-01 | P0 | Compare Agent Builder, Agents Toolkit, Copilot Studio declarative publishing, and SharePoint agents | Implement the same read-only policy agent in each viable tool | Tool decision matrix; authoring/ALM/governance differences |
| DA-02 | P0 | Design source authority and permission behavior | Ground one agent on approved SharePoint sources; test users with three permission profiles | Permission-trimming evidence; stale/conflicting source test |
| DA-03 | P0 | Instruction and knowledge separation | Run 20 prompts against instruction-only, broad knowledge, and scoped knowledge variants | Groundedness, citation quality, abstention, latency |
| DA-04 | P0 | Secure actions/API plugins | Add a read tool, then a write tool with confirmation and idempotency | Threat model; approval and audit tests; tool-selection accuracy |
| DA-05 | P1 | M365 Copilot licensing paths | Compare licensed user, Copilot Chat + PAYG, and unsupported configuration | Consumption evidence and decision tree |
| DA-06 | P1 | Government/sovereign differences | Document GCC/GCCH/DoD support from current sources; no tenant test unless available | Cloud applicability matrix |
| DA-07 | P1 | SDLC workbench pattern | Build “requirements discovery” agent with controlled sources and structured output | Evaluation set for actors, NFRs, security, exclusions, open questions |

Sources: [declarative agent overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent), [tool comparison](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-tool-comparison), [knowledge sources](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources), [security](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security), [cost considerations](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations).

---

## B. Copilot Studio

### Current baseline

**Confirmed:** Classic Copilot Studio remains the mature feature baseline. Generative orchestration can select topics, tools, knowledge, and other agents. Solutions, environment variables, connection references, pipelines, DLP, evaluation, analytics, and security controls form the production delivery path.

**Preview:** The new agent experience is a production-ready preview and uses enhanced orchestration. There is no migration path between classic and new agent formats. Deep reasoning and some model/evaluation/skill features have their own preview status.

**Licensing/capacity:** Copilot Credits are the common currency. Verified rates include classic answer 1, generative answer 2, agent action 5, tenant graph grounding 10, agent-flow actions 13/100, plus AI-tool and reasoning token charges. Qualifying employee-facing M365 Copilot usage can be zero-rated; autonomous/event-triggered scenarios differ.

**Geography/security:** Data location, cross-region processing, language, and channel support must be checked per capability. DLP can block unauthenticated chat, knowledge types, connectors, HTTP, skills, channels, and event triggers.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| CS-01 | P0 | Classic vs new agent experience | Build identical read-only triage agent in both | Feature-gap, status, ALM, evaluation, and migration matrix |
| CS-02 | P0 | Generative vs classic orchestration | Use same intents/tools and compare deterministic topic routing with generative selection | Tool/topic selection precision, latency, cost, failure modes |
| CS-03 | P0 | Knowledge architecture | Compare SharePoint, Dataverse, uploaded files, public web, and tenant graph grounding | Source-quality and permission test pack |
| CS-04 | P0 | Tools vs prompts vs agent flows vs connected agents | Implement one classification-and-action scenario four ways | Selection pattern and cost model |
| CS-05 | P0 | DLP and authentication | Apply a restrictive policy, endpoint filtering, and authenticated channel | Policy enforcement evidence and maker error guide |
| CS-06 | P0 | Evaluation/CI gate | Build 30-case test set and trigger it in deployment workflow where supported | Baseline score, variance, false-pass review, release threshold |
| CS-07 | P1 | Child vs connected agent topology | Split discovery, authoring, and assurance only where independent ALM/ownership helps | Topology decision record; handoff and failure tests |
| CS-08 | P1 | Entra Agent IDs and credentials | Inspect automatically created identities; compare user, maker-provided, and service identities | Least-privilege identity matrix and runbook |
| CS-09 | P1 | MCP onboarding | Connect one approved read-only MCP server; test tool discovery and injection defenses | MCP threat model, allow-list, audit evidence |
| CS-10 | P1 | Capacity enforcement | Configure allocation/agent limits and intentionally reach a safe lab threshold | Alert/enforcement runbook |

Sources: [classic vs new](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/classic-vs-new), [generative orchestration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions), [billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management), [DLP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention), [ALM guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm), [evaluation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro).

---

## C. Agent flows and Workflows

### Current baseline

**Confirmed:** Agent flows are deterministic, solution-aware automations created/managed through Copilot Studio and billed through Copilot Studio capacity. A Power Automate cloud flow can be converted one way to an agent flow when prerequisites are met.

**Preview:** The new Workflows format belongs to the new Copilot Studio experience and is public preview. It is distinct from the classic Workflows page that hosts agent flows. There is no conversion from Power Automate cloud flow to the new workflow format.

**Licensing/capacity:** Agent-flow actions consume 13 Copilot Credits per 100 actions. A qualifying “When an agent calls the flow” run for an authenticated M365 Copilot user can be included; other triggers consume capacity. New runs are blocked when applicable prepaid capacity is exhausted.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| AF-01 | P0 | Agent flow vs cloud flow boundary | Build the same deterministic approval helper both ways | Licensing, ownership, trigger, ALM, monitoring, recovery matrix |
| AF-02 | P0 | Agent-called flow contract | Define validated JSON input/output, timeout, retry, and error envelope | Contract tests and malformed-input cases |
| AF-03 | P0 | Capacity math | Execute known action counts through agent-called and event-triggered variants | Measured vs forecast consumption |
| AF-04 | P1 | New Workflows preview | Rebuild a noncritical lab workflow and compare editing/runtime/ALM gaps | Preview decision and exit plan |
| AF-05 | P1 | Human/AI approvals | Test multistage approval preview only in sandbox with low-risk data | False approval/rejection and escalation evaluation |
| AF-06 | P1 | Conversion behavior | Convert a disposable solution-aware cloud flow to agent flow | One-way conversion checklist and rollback alternative |

Source: [Agent flows overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview), [billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management), [advanced approvals preview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals).

---

## D. Power Automate

### Current baseline

**Confirmed:** Cloud flows remain the broad deterministic automation service. Licensing depends on users, process/flow context, premium connectors, RPA, and seeded rights. Limits vary by performance profile and connector/API. Solution-aware flows support ALM; service-principal ownership is available for supported contexts.

**Security/governance:** Use solutions, connection references, environment variables, secure inputs/outputs, managed identities/service principals where supported, DLP, least privilege, idempotency, retry/dead-letter patterns, and monitoring. Personal-owner flows are a continuity risk.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| PA-01 | P0 | License selector | Model user-triggered, shared business process, unattended RPA, and D365-context cases | License decision tree with owner/trigger/connector rules |
| PA-02 | P0 | Reliable cloud-flow skeleton | Build idempotent Dataverse event processor with correlation ID and retry/dead-letter | Load, duplicate-event, timeout, and recovery tests |
| PA-03 | P0 | Ownership and connection strategy | Compare user-owned and service-principal-owned solution-aware flows | Offboarding and least-privilege evidence |
| PA-04 | P1 | Copilot designer quality | Generate flow from natural language, then review against production checklist | Defect taxonomy and maker prompt pattern |
| PA-05 | P1 | Process mining | Run a small sanitized event log through discovery/analysis | License/storage estimate and actionable finding |
| PA-06 | P1 | Flow observability | Establish alerts, run-history retention/export, and support ownership | Operations runbook and SLO |

Sources: [Power Automate limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config), [licensing FAQ](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-flow-licensing-faq), [service-principal flows](https://learn.microsoft.com/en-us/power-automate/service-principal-support).

---

## E. AI Builder

### Current baseline

**Confirmed/announced:** AI Builder supports prompts and prebuilt/custom models across Power Apps and Power Automate; agent/agent-flow use is metered in Copilot Credits. Seeded AI Builder credits end 2026-11-01, subject to contract protections. There is no automatic credit conversion.

**Capacity behavior:** In Power Apps/Power Automate contexts, eligible AI Builder credits are consumed first, then Copilot Credits. In agents and agent flows, prompts/models consume Copilot Credits under the documented rules. Training a custom model does not itself consume these runtime credits; published model use does.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| AIB-01 | P0 | Credit-transition inventory | Catalogue current AI Builder workloads, licenses, contracts, monthly consumption, and fallback | November 2026 migration/capacity plan |
| AIB-02 | P0 | Prompt output contract | Build a structured JSON classification prompt with schema validation and error path | Accuracy, malformed output, injection, token/cost tests |
| AIB-03 | P0 | Document processing comparison | Compare prebuilt/custom document model, prompt-based extraction, and human review | Accuracy-by-field, page cost, confidence/exception pattern |
| AIB-04 | P1 | Model lifecycle | Train, publish, version, and promote a small custom model | Dataset/version/rollback/evaluation runbook |
| AIB-05 | P1 | Responsible AI and privacy | Test sensitive-data redaction, retention, access, and failure logging | Data-flow and risk assessment |
| AIB-06 | P1 | Process intelligence | Compare AI Builder extraction signals with process-mining opportunity | Productised SMB experiment brief |

Sources: [AI Builder licensing](https://learn.microsoft.com/en-us/ai-builder/administer-licensing), [credit transition](https://learn.microsoft.com/en-us/ai-builder/endofaibcredits), [Copilot Credits rules](https://learn.microsoft.com/en-us/ai-builder/message-management), [credit management](https://learn.microsoft.com/en-us/ai-builder/credit-management).

---

## F. Power Apps Plans and Vibe

### Current baseline

**Confirmed:** Plans in Power Apps are GA, require Dataverse, and can propose/generate tables, apps, pages, flows, and agents. Generated assets still require normal licensing, security, solution, testing, and ALM review.

**Preview:** Power Apps Vibe is preview, currently limited to US, Australia, Asia, and India and English, and unavailable in default environments. Current limitations include one app per plan, no coauthoring, constraints around existing apps/app types and direct code editing, and plan disconnect behavior after some external edit/redeploy paths.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| PAP-01 | P0 | Plans production-readiness gap | Generate a simple service-request solution, then review every artifact | Gap report: data, security, UX, logic, tests, ALM, licensing |
| PAP-02 | P0 | Requirement prompt pattern | Compare vague, structured, and artifact-grounded requirements | Repeatability and missing-requirement score |
| PAV-01 | P1 | Vibe prototype benchmark | Generate same app in Vibe and GA Plans | Speed/quality/maintainability/ALM comparison |
| PAV-02 | P1 | Productionisation path | Rebuild a selected Vibe prototype using supported production components | Traceability and parity test; preview dependency removed |
| PAP-03 | P1 | External editing and source control | Test supported export/unpack/redeploy workflow on disposable solution | Identity/plan linkage and diff quality evidence |
| PAP-04 | P1 | Accessibility/performance/security | Review generated app using production checklist | WCAG/usability, delegation/performance, role/field-security findings |

Sources: [Plans overview](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/plan-designer), [Plans FAQ](https://learn.microsoft.com/en-us/power-apps/maker/common/faq-plan-designer), [Vibe overview](https://learn.microsoft.com/en-us/power-apps/vibe/overview), [Vibe FAQ](https://learn.microsoft.com/en-us/power-apps/maker/common/faq-vibe).

---

## G. Dataverse, MCP, and ALM

### Current baseline

**Confirmed:** Dataverse supplies secure table-based data, business logic, roles, audit, and solution-aware configuration. Power Platform pipelines are the recommended native ALM path; pipeline targets are managed environments and require premium use rights.

**Preview distinction:** The documented Power Apps MCP Server currently supports agent tools and human supervision/agent-feed patterns in model-driven apps through Copilot Studio. Do not generalize it into an unrestricted “Dataverse MCP server.”

**Security/geography:** Apply role/team/field security, least privilege, audit, DLP, environment strategy, region/data boundary, and maker-provided credential controls. The agent feed currently has a broad visibility caveat based on Agent Task table access.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| DV-01 | P0 | Secure requirements/decision store | Model Requirement, Actor, NFR, Decision, Evidence, Test Case, Finding, Artifact Version | Schema, role matrix, audit/retention, traceability views |
| DV-02 | P0 | Environment/pipeline baseline | Dev→Test managed deployment with env vars, connection refs, approval, rollback | Deployment evidence and recovery time |
| MCP-01 | P1 | Power Apps MCP supervision | Use a low-risk autonomous agent to create a review task in a model-driven app | Feed visibility, role, credential, human-review tests |
| MCP-02 | P1 | External MCP security boundary | Connect approved read-only server; test tool poisoning, excessive permissions, schema errors | Threat model and onboarding checklist |
| ALM-01 | P0 | Solution segmentation | Compare one large solution vs feature/platform boundaries | Dependency and deployment decision record |
| ALM-02 | P1 | Git integration | Unpack solution, review meaningful diffs, build, validate, and deploy | Repo structure and CI quality gate |
| ALM-03 | P1 | Deprecation migration | Replace ALM Accelerator assumptions with pipelines/native or approved DevOps path | Migration checklist |

Sources: [Dataverse overview](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro), [pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines), [Power Apps MCP Server](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/power-apps-mcp-server), [agent feed](https://learn.microsoft.com/en-us/power-apps/user/supervise-agents-with-agent-feed), [ALM guidance update](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/whats-new).

---

## H. Cross-platform Agent Skills

### Current baseline

**Confirmed:** OpenAI Codex/ChatGPT Work distribution, Claude Code, and GitHub Copilot support Agent Skills-style packages containing instructions/resources/scripts. Each platform adds its own paths, invocation, sandbox, admin, and distribution behavior.

**Preview:** Copilot Studio skills in the new agent experience are preview and require an adapter; a `SKILL.md` package must not be assumed to import unchanged. M365 declarative agents use manifests/instructions/knowledge/actions rather than an Agent Skills folder as the runtime unit.

| ID | Priority | Learning item | Hands-on experiment | Output/evaluation |
|---|---:|---|---|---|
| SKL-01 | P0 | Portable core | Implement `power-platform-current-feature-verifier` in Agent Skills format | Runs in Codex, Claude Code, and GitHub Copilot with same golden tests |
| SKL-02 | P0 | Adapter contract | Map core instruction, references, templates, scripts, tests, and tools to five targets | Adapter matrix and unsupported-feature rules |
| SKL-03 | P0 | Security review | Scan skill scripts/dependencies, network/tool permissions, secret handling, and prompt injection | Install approval checklist and threat model |
| SKL-04 | P1 | Copilot Studio adapter | Recreate one skill in preview Copilot Studio skills or supported tools/instructions | Functional parity and gap report |
| SKL-05 | P1 | M365 declarative adapter | Convert read-only skill knowledge/instructions into declarative-agent assets | Manifest/instruction/evaluation package |
| SKL-06 | P1 | Regression/evaluation harness | Run golden cases across platforms and compare output contracts | Cross-platform scorecard and changelog rule |
| SKL-07 | P1 | Distribution/versioning | Package OpenAI plugin, Claude plugin/skill, GitHub repository skill, and docs adapters | Version matrix, install/update/rollback instructions |

Sources: [OpenAI build skills](https://developers.openai.com/codex/build-skills), [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills), [GitHub Copilot Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills), [Copilot Studio skills preview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview).

## Wave 1 exit criteria

- Source register contains at least 25 active claims with owners and expiry dates.
- Tenant learning zones, DLP baseline, region/processing map, and ALM pipeline are approved.
- Common 30-case evaluation set runs against at least one declarative agent and one Copilot Studio agent.
- Agent flow vs Power Automate and Plans vs Vibe comparison labs are complete.
- AI Builder November 2026 workload inventory and capacity forecast is complete.
- First portable skill passes golden tests on at least two supported Agent Skills platforms.

