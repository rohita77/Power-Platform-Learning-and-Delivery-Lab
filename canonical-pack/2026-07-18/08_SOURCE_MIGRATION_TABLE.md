# Existing Source Migration Table

**Pack version:** 1.1
**Reviewed:** 2026-07-18  
**Scope note:** Based on the supplied audit and available project context. Exact duplicate-file hashes and Library inventory were not provided, so destructive removal requires a separate identity/content check.

## Recommendation

| Source/artifact | Decision | Destination/use | Reason and safeguards |
|---|---|---|---|
| Current revised project instructions | **Retain and replace with canonical file** | `01_PROJECT_INSTRUCTIONS.md` | Most required policy was already present. This pack removes duplication and adds current corrections. Preserve project settings until the canonical file is adopted. |
| Three currently retained `D365 Solution Workflow` extracts; four uploads were originally observed | **Merge, then archive confirmed duplicates** | Architectural decisions in `01_PROJECT_INSTRUCTIONS.md`; orchestration detail in skill definition 6 | Retain incremental delivery, explicit scope/acceptance, solution-aware ALM, deployment/rollback, and ChatGPT-as-architect/reviewer. The current inventory is three retained extracts; preserve the historical note that four uploads were originally observed. Do not delete until exact content and identity are confirmed. |
| M365 Copilot Agent Topology material | **Retain as dated pattern** | Future `patterns/sdlc-workbench/` | Strong governed-orchestration and artifact-lifecycle decisions; too narrow to be the master project architecture. Product claims must be reverified. |
| Supplied audit (`Pasted markdown.md`) | **Retain as migration evidence, then archive** | Historical source supporting this pack | Useful inventory and intent, but several current-product statements required correction. It is not product authority. |
| Raw project chats | **Retain as context/history** | Decision rationale, examples, test cases, unresolved-question mining | Do not use as current status/licensing authority. Avoid bulk retrieval conflicts by consolidating durable decisions. |
| Pinned GPT: Prompt Engineering | **Extract, test, then unpin if redundant** | Future `prompt-and-output-contract-review` skill | Keep prompt patterns, structured-output contracts, evaluation rubrics, and anti-patterns; discard stale answers/personality dependence. |
| Pinned GPT: Power Apps Prod | **Extract, test, then unpin if redundant** | `power-apps-ai-productioniser` skill (definition 5) | Retain production, ALM, performance, accessibility, security, delegation, and review checks. Reverify product details. |
| Pinned GPT: Copilot Studio Expert | **Extract, test, then unpin if redundant** | `copilot-studio-design-review` skill (definition 3) | Retain architecture, grounding, tools, evaluation, DLP, licensing, and ALM checks. Reverify preview and credit behavior. |
| Screenshots, course decks, old copied documentation | **Demote/archive** | Examples or UI history only | UI, limits, licensing, region, and preview status age quickly. Record original date and never cite as current authority. |
| Microsoft Learn product docs and licensing guides | **Retain as live authority links** | Source register and release radar | Primary current product evidence; revalidate on the defined cadence. |
| Microsoft release plans, release notes, What’s new, Message Center | **Retain as change-detection authority** | Weekly radar | Best rollout/status-change signals; reconcile planned dates with actual docs/tenant availability. |
| Official OpenAI skills/plugins/Codex docs | **Retain as active-runtime authority** | Chat/Work guide and active skill/plugin adapters | Current authority for Personal ChatGPT Pro, ChatGPT Work, and Codex/VS Code behavior. |
| Official GitHub/VS Code/Anthropic/Cursor docs | **Retain as reference-only where applicable** | Deferred adapter notes | Claude Code, GitHub Copilot, and Cursor are not subscribed; do not treat their documentation as runtime test evidence. |
| Four Microsoft upstream skill/plugin repositories | **Register and pin** | `10_UPSTREAM_SKILLS_REGISTER.md` | Track client support, install/evaluation status, update path, prerequisites, tools/MCP, telemetry, permissions, boundary, adaptations, tests, owner, and revalidation. |
| Personal OpenAI and organisational Microsoft content | **Separate into two zones** | `01_PROJECT_INSTRUCTIONS.md`, section 11 | No automatic sharing or synchronization. Any exceptional transfer requires explicit organisational approval, minimization, ownership, retention, and audit evidence. |
| MVP/community articles and samples | **Selective retain** | Experiment ideas and implementation notes | Must be validated against current first-party docs; label community evidence. |

## Preserved decisions and where they moved

| Prior decision | Canonical location |
|---|---|
| ChatGPT as architect/reviewer; coding tools as implementation agents | `01_PROJECT_INSTRUCTIONS.md`, sections 3, 4, and 9 |
| Power Platform solutions and Git as implementation sources of truth | `01_PROJECT_INSTRUCTIONS.md`, section 1 |
| Small deployable vertical MVPs | `01_PROJECT_INSTRUCTIONS.md`, sections 3 and 9; skill definition 6 |
| Explicit scope, exclusions, acceptance, tests, deploy/rollback | `01_PROJECT_INSTRUCTIONS.md`, section 9; skill definition 6 |
| Governed orchestrator before many autonomous agents | `01_PROJECT_INSTRUCTIONS.md`, section 4; skill definitions 2 and 3 |
| Separate discovery, elicitation, conceptualisation, authoring, assurance | `01_PROJECT_INSTRUCTIONS.md`, section 4; skill definitions 2, 3, and 6 |
| Instructions, knowledge, state, tools, and evaluations are separate | `01_PROJECT_INSTRUCTIONS.md`, section 4; `06_SKILL_DESIGN_STANDARD.md` |
| Structured requirements/decisions rather than documents only | `04_LEARNING_BACKLOG.md` item DV-01; skill definition 6 |
| Human approval for consequential decisions/actions | All security sections and skill definitions |
| Security, evaluations, and ALM in the first production pilot | Project definition of done, shared foundation, and skill gates |
| Use a delivery spine to coordinate specialist work | `power-platform-incremental-delivery` is now an orchestrator/meta-skill that delegates to skills 1–5 and registered Microsoft upstream specialists |

## Corrected or superseded claims

| Earlier claim/term | 2026-07-18 position | Evidence/action |
|---|---|---|
| Workspace Agents are GA | Official current cookbook labels them **research preview** for Business, Enterprise, and Edu | [OpenAI cookbook](https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep); mark all old GA claims superseded |
| A rigid Workspace Agent → Codex Plan → Goal delivery chain | Not a canonical product workflow | Use outcome-based Chat/Work/Codex/Power Platform selection in `05_CHAT_VS_WORK_DECISION_GUIDE.md` |
| Workflows and agent flows are interchangeable terms | They are distinct current formats/experiences | [Agent flows overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview); new Workflows is public preview |
| Power Apps Vibe can anchor production design | Preview; not the production baseline | [Vibe overview](https://learn.microsoft.com/en-us/power-apps/vibe/overview); require productionisation |
| Plans and Vibe are the same maturity | Plans are GA; Vibe is preview | [Plans](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/plan-designer), [Vibe](https://learn.microsoft.com/en-us/power-apps/vibe/overview) |
| “Dataverse MCP server” as a generic supported endpoint | Use the precise current **Power Apps MCP Server** term for documented preview supervision/feed tools | [Power Apps MCP Server](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/power-apps-mcp-server) |
| Agent Skills packages directly port into Copilot Studio | Agent Skills-compatible core is portable across supporting products; Copilot Studio preview skills require an adapter and tests | [Copilot Studio skills](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview) |
| Static AI Builder seeded capacity is durable | Seeded credits end 2026-11-01, subject to contract protection; no automatic conversion | [AI Builder transition](https://learn.microsoft.com/en-us/ai-builder/endofaibcredits) |
| Old Copilot Studio message-cost assumptions | Current currency is Copilot Credits with feature-specific rates and enforcement | [Billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management) |

## Proposed post-pack information architecture

```text
Power-Platform-Learning-and-Delivery-Lab/
  governance/              # instructions, source governance, decision guide
  backlog/                 # learning backlog and release radar
  patterns/
    sdlc-workbench/        # retained M365 Copilot topology pattern
    declarative-agent/
    copilot-studio-agent/
    automation-selection/
    plans-vibe-productionisation/
    power-apps-mcp-supervision/
  skills/                  # portable cores and adapters
  experiments/             # reproducible lab records and evidence
  templates/
  archive/                 # dated chats/audits/old extracts, clearly non-authoritative
```

The current ten-file pack remains flat for easy adoption. Create the fuller tree only when the first patterns/skills/experiments are implemented.

## Safe migration procedure

1. Adopt `01_PROJECT_INSTRUCTIONS.md` as the only canonical project instruction.
2. Register this pack and its source dates.
3. Materialize/inspect the three currently retained D365 workflow extracts and calculate exact duplicates before any archive/removal; retain the historical record that four uploads were originally observed.
4. Extract unique durable decisions and unresolved questions; map them to the table above.
5. Store the topology as a dated `sdlc-workbench` pattern and label product claims for revalidation.
6. Extract pinned-GPT instructions into candidate skills; create tests before retiring any GPT.
7. Mark old chats/decks/screenshots `historical-context` and exclude them from product-authority retrieval.
8. Run the release radar once; update any already-expired claims.
9. Archive duplicates only after an owner confirms the canonical replacement covers unique content.
10. Reconcile every upstream install/update against `10_UPSTREAM_SKILLS_REGISTER.md` and test active adapters in ChatGPT Work and Codex/VS Code; keep Claude/GitHub/Cursor adapters marked untested.

## Explicit exclusions

- No uploaded file was deleted, renamed, or moved by this pack.
- No pinned GPT was changed.
- No tenant/environment configuration was changed.
- No cross-zone connector, authentication, or synchronization was configured.
- No old source was asserted to be an exact duplicate without byte/content verification.
