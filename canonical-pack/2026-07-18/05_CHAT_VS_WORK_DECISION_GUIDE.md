# Chat vs Work Decision Guide

**Pack version:** 1.1
**Verified:** 2026-07-18  
**Default:** Chat + Medium

## Recommendation table

| Desired outcome | Mode | Reasoning | Example prompt |
|---|---|---|---|
| Definition, syntax, or quick explanation | Chat | Instant | “Explain agent flows in five points.” |
| Current feature summary | Chat | Medium | “Verify the current status and limits of Plans in Power Apps.” |
| Compare two or three options | Chat | Medium | “Compare a declarative agent with a Copilot Studio agent for this scenario.” |
| Licensing, capacity, security, or architecture decision | Chat | High | “Recommend the licensed architecture and show trade-offs and open questions.” |
| Review one design/prompt/flow specification | Chat | High | “Review this design against security, ALM, cost, and failure-mode gates.” |
| Produce one reusable checklist or brief | Work | Medium | “Create a build brief with acceptance criteria and rollback.” |
| Multi-source current research plus a reusable file | Work | High | “Research current official sources and create a source-backed decision pack.” |
| Multiple related artifacts, implementation, or recurring workflow | Work | High | “Build and verify the lab pack, then save the deliverables.” |
| Regulated, multi-system, high-failure-cost design | Work | Extra High or Pro | “Create an evidence-backed target architecture, threat model, controls, and validation plan.” |
| Short follow-up to completed work | Chat | Medium | “Explain why option B was rejected.” |

## Selection rule

This guide assumes Personal ChatGPT Pro, ChatGPT Work, and Codex/VS Code are the active OpenAI runtimes. Claude Code, GitHub Copilot, and Cursor are not mandatory or available test dependencies.

Use **Chat** when the user primarily needs thought, explanation, comparison, or a short draft.

Use **Work** when the user needs a clear, reviewable outcome that requires multiple sources/tools/steps, file creation, implementation, recurring execution, or longer autonomous progress.

Complexity alone does not require Work. A difficult architecture discussion can remain in Chat; a modest ten-file pack belongs in Work because it produces a reusable outcome.

## Reasoning rule

- **Instant:** Fast, low-risk, familiar questions.
- **Medium:** Normal analysis and most feature explanations/comparisons.
- **High:** Conflicting evidence, licensing, architecture, security, governance, or important reviews.
- **Extra High:** Especially demanding multi-step reasoning with significant consequences.
- **Pro:** Difficult, long-running, high-impact work where maximum capability is worth higher usage.

The picker names and availability vary by plan, workspace setting, and rollout. The current official model guidance maps Instant to fast everyday work and Medium/High/Extra High/Pro to increasing reasoning effort/capability, but the lab should recommend an effort—not promise that the user’s plan exposes it.

## Prompt frame for Chat

```text
Goal:
Decision/question:
Scenario and constraints:
What is already known:
Current official sources required: yes/no
Output: recommendation table + trade-offs + next experiment
```

## Prompt frame for Work

```text
Outcome and audience:
Files/deliverables required:
Sources and authority policy:
Current artifacts to preserve:
In-scope changes:
Explicit exclusions:
License, region, security, and ALM constraints:
Acceptance criteria and tests:
Where to save the result:
Review the files before finishing and report open questions.
```

## When to use a Workspace Agent

Use a Workspace Agent only when a **repeatable organizational workflow** benefits from persistent instructions, skills, approved apps, scheduling, sharing, and managed permissions—such as a weekly release radar or recurring customer-meeting brief.

Do not make it the default handoff step for every Power Platform task. Current official OpenAI material still labels Workspace Agents a **research preview** for Business, Enterprise, and Edu. Validate plan access, RBAC, connector action controls, approval behavior, audit/compliance scope, and failure handling before operational adoption.

## When to use Codex/VS Code

Use repository-aware coding tools for:

- inspecting solution/source state and local instructions;
- implementing PCF, plugins, Azure Functions, scripts, tests, CI/CD, and skill packages;
- unpacking/packing and validating solution artifacts;
- making controlled diffs and running tests.

Use Chat/Work to frame architecture, produce briefs, research current behavior, and review evidence. Do not copy a chat’s proposed implementation into production without reconciling it with the actual repository and solution state.

The Microsoft Dataverse plugin v1.6.0 is installed in Codex, but this guide does not authorize `dv-connect`, tenant authentication, or environment changes. Use installation/static inspection only until a separate approved boundary and tenant test plan exists.

## Personal vs organisational work

| Work/content | Use | Boundary rule |
|---|---|---|
| Public research, synthetic labs, reusable non-confidential methods, repository documentation | Personal ChatGPT/Work and Codex/VS Code | Keep sources public or explicitly approved for the personal zone |
| Confidential tenant records, solution exports, M365 documents, Message Center evidence, environment logs, credentials | Organisational M365 Copilot/Power Platform tools | Keep inside organisational controls; do not paste, upload, connect, or sync to the personal OpenAI zone |
| A reusable method needed in both zones | Separately install/recreate the sanitized skill or template in each zone | Share only the non-confidential definition; never synchronize runtime data or state automatically |

If a task requires evidence from both zones, split it into two independently executed steps. Carry across only an approved, minimized, non-confidential result with an owner and audit trail.

## Governance for Work and agents

- Connected systems keep their own permissions; Work does not grant new source-system access.
- No connector, MCP server, plugin, script, or schedule may automatically synchronize the personal OpenAI and organisational Microsoft zones.
- Keep write actions, external messages, deployments, financial/customer decisions, privilege changes, and destructive operations behind explicit approvals or approved controls.
- Use least privilege, per-tool action controls, scoped sources, and audit/telemetry.
- Treat generated deliverables as drafts until their acceptance criteria pass.
- Record source dates because a long-running task can outlive a rapidly changing preview claim.

## Current official sources

- [OpenAI pricing and surfaces](https://learn.chatgpt.com/docs/pricing)
- [OpenAI skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [OpenAI build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI plugins](https://learn.chatgpt.com/docs/plugins)
- [Workspace Agents cookbook](https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep)
