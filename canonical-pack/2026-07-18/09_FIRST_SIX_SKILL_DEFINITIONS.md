# First Six Reusable Skill Definitions

**Pack version:** 1.0  
**Defined:** 2026-07-18  
**Status:** Design definitions; implement one at a time after source/tenant prerequisites are available

## Portfolio recommendation

| # | Skill | Primary outcome | First implementation priority |
|---:|---|---|---:|
| 1 | `power-platform-current-feature-verifier` | Evidence-backed current product position | P0 |
| 2 | `m365-declarative-agent-designer` | Governed declarative-agent design and experiment | P0 |
| 3 | `copilot-studio-design-review` | Production/readiness review with findings | P0 |
| 4 | `agentic-automation-selector` | Choose Agent flow, preview Workflow, Power Automate, prompt/tool, or code | P0 |
| 5 | `power-apps-ai-productioniser` | Turn Plans/Vibe output into a supported production slice | P1 |
| 6 | `power-platform-incremental-delivery` | Shape and deliver the next vertical Power Platform/D365 slice | P0 |

The six skills are composable. Skill 1 verifies volatile product facts; skills 2–5 apply domain workflows; skill 6 manages the delivery increment.

---

## 1. `power-platform-current-feature-verifier`

### Scope

Verify a current Microsoft 365 Copilot, Copilot Studio, Power Platform, D365, or related cross-platform feature and return a decision-ready source record. It owns current status, license/capacity, geography/language, limitations, security/governance, ALM, and source conflict handling.

### Trigger / exclusions

Trigger for “is this GA/current/supported,” licensing/capacity, regional availability, limit, deprecation, or current comparison claims. Do not trigger for pure implementation that already has a fresh approved source pack unless a material claim has expired.

### Inputs

- exact capability/claim and decision it affects;
- tenant cloud/environment region and user geography;
- intended users/channel and production/experiment classification;
- current license/contract facts if available;
- required verification date/risk tolerance.

### Workflow

1. Convert the question into atomic claims.
2. Search A1/A2 first-party sources in the project authority order.
3. Record source updated date and explicit status banner.
4. Extract license/entitlement/meter/enforcement separately.
5. Extract cloud/region/language and data-processing implications.
6. Extract limitations, dependencies, security, governance, and ALM.
7. Resolve conflicts using `02_SOURCE_GOVERNANCE.md` or label `Open`.
8. Produce source-register rows and a revalidation date.

### Outputs

- recommendation table;
- confirmed/preview/inference/recommendation/assumption/open labels;
- source-register row(s) matching `03_SOURCE_REGISTER_TEMPLATE.md`;
- impact on existing decisions/skills/experiments;
- practical tenant experiment where documentation is insufficient.

### Sources

Microsoft Learn/licensing/release plans and the relevant official external-platform docs. Never use project chats as product authority.

### Tests

- Plans GA vs Vibe preview distinction;
- Workspace Agents research-preview correction;
- Copilot Studio new agent experience vs classic;
- Singapore cross-region AI processing case;
- conflicting licensing-page scenario must abstain/escalate;
- stale source (> validity window) must not be reported as current without refresh.

### Security and stop conditions

No production recommendation when license, residency, status, or a critical control remains materially unresolved. Do not infer contractual rights from a working tenant.

### Adapters

- **OpenAI/Codex, Claude, GitHub Copilot:** Portable Agent Skill with web/docs retrieval instructions and structured output validator.
- **M365 declarative agent:** Read-only research assistant; actions limited to approved sources; output to structured register through a controlled tool.
- **Copilot Studio:** Instructions + approved knowledge/tools/agent flow; DLP and source allow-list; evaluation cases mirror portable tests.

---

## 2. `m365-declarative-agent-designer`

### Scope

Design a Microsoft 365 Copilot declarative agent from outcome through experiment, including tool choice (Agent Builder, Agents Toolkit, Copilot Studio, or SharePoint path), instructions, knowledge, actions, permissions, admin controls, evaluation, deployment, and support.

### Trigger / exclusions

Trigger for an agent that should run in Microsoft 365 Copilot and primarily use M365 work context/UX. Do not use for a custom model/orchestrator requirement that needs a custom-engine agent, or for deterministic automation with no conversational need.

### Inputs

- business outcome, personas, host/channel, and measurable success;
- knowledge sources and source authority;
- required actions and consequence level;
- M365 Copilot/Copilot Chat license mix;
- tenant cloud/region, data classification, Purview/DLP, sharing and admin constraints;
- ALM/source-control requirement.

### Workflow

1. Use skill 1 to verify current authoring-tool/status/license choices.
2. Separate discovery, elicitation, conceptualisation, authoring, and assurance.
3. Select the simplest authoring tool that meets action/ALM/control needs.
4. Define identity, concise instructions, knowledge scope, citations/abstention, actions, and output contracts.
5. Threat-model oversharing, prompt injection, untrusted action data, and write side effects.
6. Define admin acquisition/sharing, ACL, Purview/DLP/retention/audit, and support.
7. Create a 20–30 case evaluation set and one small experiment.

### Outputs

- tool-selection table and recommended architecture;
- agent design canvas: purpose, users, instructions, knowledge, actions, state, approval, evaluation;
- source/data-flow and permission matrix;
- manifest/instruction/action design where applicable;
- experiment/build brief and deployment/governance checklist.

### Current source baseline

[Declarative agents](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent), [tool comparison](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-tool-comparison), [knowledge matrix](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources), [security](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security), [costs](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations).

### Tests

- correct tool selection for simple knowledge, API action, ALM-heavy, and custom-engine cases;
- three user permission profiles return only authorized content;
- Restricted SharePoint Search and unavailable-source behavior;
- malicious source content cannot trigger sensitive action without approval;
- licensed vs Copilot Chat metered scenarios distinguished;
- government-cloud differences labeled.

### Adapters

- **Portable core:** Design/review methodology and templates.
- **M365 adapter:** Manifest/instructions/knowledge/actions/evaluation package.
- **Copilot Studio adapter:** Low-code declarative publishing when supported; solution/pipeline/DLP artifacts.
- **OpenAI/Claude/GitHub:** Use as architect/reviewer; they do not replace the M365 runtime manifest or admin controls.

---

## 3. `copilot-studio-design-review`

### Scope

Review a Copilot Studio agent, design, exported solution, or build brief against outcome, architecture, orchestration, knowledge, tools, identity, DLP, AI quality, Copilot Credits, geography, reliability, operations, and ALM gates.

### Trigger / exclusions

Trigger for architecture/readiness review, production gate, or remediation prioritization. Diagnose evidence; do not modify the agent unless implementation is separately authorized.

### Inputs

- current agent experience (classic/new), solution/export/screenshots/configuration;
- users/channels/triggers and data classification;
- instructions/topics/knowledge/tools/prompts/flows/other agents;
- identity/connection/credential model and DLP policies;
- test sets, analytics, consumption, environments, deployment process;
- known issues and accepted risk.

### Workflow

1. Reconstruct the current agreed position and label evidence gaps.
2. Verify preview/GA/licensing/geography claims using skill 1.
3. Review orchestration/tool descriptions and deterministic boundaries.
4. Review knowledge authority, permissions, freshness, citation, abstention, and injection risk.
5. Review tools/actions: schema, validation, auth, least privilege, approval, idempotency, failure/retry.
6. Review DLP, channel, event trigger, MCP, identity, and data-processing controls.
7. Recalculate the full Copilot Credit path and enforcement risk.
8. Review test set/variance/security/red-team/human review.
9. Review solution, env vars, connection refs, pipeline, post-deploy, rollback, monitoring, and ownership.
10. Report Blocker/High/Medium/Low findings and smallest safe remediation.

### Outputs

- gate verdict and executive recommendation table;
- evidence-backed findings with severity, impact, evidence, remediation, owner;
- status/license/geography/capacity appendix;
- missing evaluation cases;
- next build-ready remediation slice.

### Current source baseline

[Classic vs new](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/classic-vs-new), [orchestration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions), [DLP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention), [billing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management), [ALM](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/alm), [evaluation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro).

### Tests

- detect new-experience preview/migration risk;
- detect unauthenticated channel and blocked connector conflict;
- detect free-form output feeding a write action;
- detect missing M365 Copilot inclusion condition for event-triggered flow;
- detect missing negative/security tests and personal-owner continuity risk;
- do not invent a finding without artifact evidence.

### Adapters

- **OpenAI/Claude/GitHub:** Review skill consumes exported/configuration artifacts and emits findings schema.
- **Copilot Studio:** Optional read-only review agent/tooling; never self-approve deployment.
- **M365 declarative agent:** Surface approved review summaries only; it is not the design authority.

---

## 4. `agentic-automation-selector`

### Scope

Select and design the deterministic/agentic boundary among Copilot Studio agent flow, preview Workflow, Power Automate cloud/desktop flow, AI prompt/tool, connector/custom connector, MCP, plugin/Azure Function, or human task.

### Trigger / exclusions

Trigger when the question is “what should execute this work?” or when agent reasoning is being used for a rule-based task. Do not use product popularity as a selection criterion.

### Inputs

- trigger, inputs/outputs, user interaction, rules/ambiguity, frequency/volume/latency;
- connectors/systems, premium requirements, identity, data classification, region;
- error/retry/idempotency/transaction and human-approval needs;
- current licenses/capacity and ALM/operations constraints.

### Decision principles

- Deterministic rules, retries, approvals, and system integration normally belong in a flow/service.
- Use agent reasoning for ambiguous interpretation, planning, source selection, or natural-language interaction—then validate before action.
- Use an agent flow when it is owned/observed in Copilot Studio and Copilot Credit billing/trigger conditions fit.
- Use Power Automate for broad deterministic automation, enterprise ownership, connectors, RPA, and Power Automate licensing/operations.
- Use the new Workflow format only for an approved preview experiment with an exit plan.
- Use MCP as a governed tool boundary, not as a substitute for authorization or workflow reliability.
- Use custom code when transactional, performance, protocol, testing, or control needs exceed low-code fit.

### Outputs

- option/recommendation table;
- end-to-end execution sequence and ownership boundary;
- license/capacity calculation and enforcement behavior;
- input/output/error schemas, approval, retry, idempotency, telemetry;
- solution/ALM/deployment/rollback brief;
- smallest comparative experiment when evidence is insufficient.

### Sources

[Agent flows](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview), [billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management), [Power Automate limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config), [Power Automate licensing FAQ](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-flow-licensing-faq), [Copilot Studio MCP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp).

### Tests

- shared business-critical premium flow selects correct ownership/license path;
- agent-called flow vs event-triggered flow inclusion is distinguished;
- deterministic classification with fixed rules is not needlessly agentic;
- ambiguous document extraction uses structured AI + validation + human exception;
- preview Workflow is rejected for production-critical dependency;
- timeout/duplicate event/partial write produces a recovery design.

### Adapters

Portable decision skill for OpenAI/Claude/GitHub; Copilot Studio adapter can generate a build brief but not deploy; M365 agent adapter provides read-only design guidance and routes builds to governed tools.

---

## 5. `power-apps-ai-productioniser`

### Scope

Review and convert a solution generated or prototyped with Plans in Power Apps, Plan Designer, Power Apps Vibe, or maker Copilot into a supported, secure, accessible, performant, testable, ALM-managed vertical slice.

### Trigger / exclusions

Trigger after AI-generated plans/data/apps/flows/agents or for a production-readiness review. Do not declare preview output production-ready because it works in preview.

### Inputs

- original business outcome/requirements and generated plan;
- environment/region/license, solution, app/data/flow/agent artifacts;
- users/roles/data classification/integrations;
- performance, accessibility, offline/mobile, audit/retention, ALM constraints;
- known deviations and test evidence.

### Workflow

1. Verify Plans/Vibe current status, region, language, and limitations with skill 1.
2. Trace requirements to generated artifacts; identify omissions and hallucinated requirements.
3. Review Dataverse model, ownership, keys, relationships, states, audit, retention, and security.
4. Review UX, accessibility, responsive behavior, delegation/query performance, errors/empty/loading states.
5. Review flow/agent logic, contracts, identity, DLP, capacity, exception handling, and human review.
6. Move/confirm assets in explicit solutions; configure env vars/connection refs/publisher/naming.
7. Remove unsupported preview dependencies or document an approved exception/exit plan.
8. Create functional, security, performance, accessibility, deployment, and rollback tests.
9. Define the next smallest production-ready slice.

### Outputs

- generated-vs-required traceability matrix;
- production gap findings and prioritized remediation;
- target component/data/security design;
- build brief, tests, deployment/rollback, and documentation updates;
- record of what AI generated vs what humans validated/changed.

### Current source baseline

[Plans](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/plan-designer), [Plans FAQ](https://learn.microsoft.com/en-us/power-apps/maker/common/faq-plan-designer), [Vibe](https://learn.microsoft.com/en-us/power-apps/vibe/overview), [Vibe FAQ](https://learn.microsoft.com/en-us/power-apps/maker/common/faq-vibe), [pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines).

### Tests

- Vibe preview dependency cannot pass production gate without removal/exception;
- generated table/app/flow security roles and field access reviewed;
- nondelegable/large-data and accessibility defects detected;
- external edit/redeploy/plan-linkage risk recorded;
- environment-specific settings are not hard-coded;
- rollback can restore previous managed version.

### Adapters

OpenAI/Claude/GitHub portable review core; VS Code adapter inspects source/unpacked solution and runs validators; Copilot Studio/M365 adapters cover generated agent components only and defer app/solution source truth to Power Platform.

---

## 6. `power-platform-incremental-delivery`

### Scope

Shape, design, brief, build/review, and carry forward the next deployable Power Platform or Dynamics 365 feature slice while preserving decisions, constraints, evidence, and prior review findings.

### Trigger / exclusions

Trigger for a new solution, continuation, MVP increment, build brief, or iteration after testing. Do not reopen settled decisions without new evidence. Do not build when the request is diagnosis/review only.

### Inputs

- current solution/repository/environment state and prior agreed position;
- business outcome, users, journeys, scope/exclusions, decisions/open questions;
- schema/components/interfaces and established conventions;
- license/capacity/region/security/compliance/ALM constraints;
- review/test evidence and unresolved defects.

### Workflow

1. Reconstruct `Confirmed`, `Assumed`, `Open`, `Rejected`, and `Superseded` state.
2. Verify material current product claims through skill 1.
3. Compare component options before selecting.
4. Define the solution spine: experience, data, integration, AI, security, operations, ALM.
5. Slice the smallest vertical increment: trigger/entry through telemetry and evidence.
6. Produce a self-contained build brief with contracts and exact non-goals.
7. When authorized, implement solution-aware changes and tests only for that slice.
8. Review outcome, traceability, platform fit, data, security, reliability, AI, UX, operations, and ALM gates.
9. Update agreed position, decision log, evidence, backlog, and next slice.

### Outputs

- current agreed position and option decision;
- component/data/integration/security/AI/ALM design proportional to the slice;
- build brief and acceptance/evaluation tests;
- implementation/review findings when authorized;
- deployment/post-deploy/rollback notes;
- concise carry-forward summary.

### Sources

Use capability-specific first-party sources, [Power Platform ALM](https://learn.microsoft.com/en-us/power-platform/alm/), [environment strategy](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/environment-strategy), and relevant D365 documentation. Source dates belong in the build brief.

### Tests

- continuation preserves prior confirmed decisions and unrelated changes;
- no horizontal layer without user-visible end-to-end acceptance;
- license, environment type, DLP, identity, region, capacity, telemetry, and rollback present;
- duplicate/retried integration event is idempotent;
- AI output feeding automation uses a validated contract and exception path;
- review-only request does not modify implementation;
- next session can continue from the carry-forward summary without rereading all chats.

### Adapters

- **ChatGPT Work:** Multi-source project pack/build brief/review and reusable artifact creation.
- **Codex/VS Code:** Repository-aware implementation, tests, solution tooling, CI/CD, controlled diffs.
- **Claude Code/GitHub Copilot:** Same portable delivery workflow with platform-native repo controls.
- **M365 declarative agent:** Read-only project orientation/status assistant; not the deployment authority.
- **Copilot Studio:** Agent-specific solution components, tests, and pipeline artifacts; Power Platform solution remains source of truth.

---

## Shared implementation sequence

1. Implement skill 1 first; all other skills depend on current-source discipline.
2. Implement skill 6 second as the delivery spine.
3. Implement skills 2–4 for the first SDLC workbench experiment.
4. Implement skill 5 when the first Plans/Vibe prototype is available.
5. Run the same three golden cases in Codex, Claude Code, and GitHub Copilot before claiming portability.
6. Add M365/Copilot Studio adapters only after the portable core passes and tenant controls are known.

## Shared release gate

- [ ] Scope and trigger boundaries approved.
- [ ] Source claims current under `02_SOURCE_GOVERNANCE.md`.
- [ ] Required status/license/geography/limits/security/ALM fields produced.
- [ ] Deterministic output contract passes.
- [ ] Negative, abstention, injection, permission, and consequential-action tests pass.
- [ ] Adapter gaps documented; no unsupported portability claim.
- [ ] Owner, version, changelog, rollback, and next revalidation set.

