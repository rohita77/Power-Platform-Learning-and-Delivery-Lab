# Upstream Skills and Plugins Register

**Pack version:** 1.1
**Verified:** 2026-07-18
**Owner:** Rohit (lab); Microsoft repository maintainers (upstream source)
**Revalidation:** 2026-08-01 and before every install, upgrade, authentication, MCP registration, or tenant-connected test

## 1. Operating baseline

- **Active OpenAI runtimes:** Personal ChatGPT Pro, ChatGPT Work, and Codex/VS Code.
- **Installed upstream:** Microsoft Dataverse plugin v1.6.0 in Codex.
- **Not subscribed:** Claude Code, GitHub Copilot, and Cursor. Compatibility notes for them are reference-only and **untested**.
- **Separate confidential environment:** Microsoft 365 Copilot and the organisational Power Platform tenant.
- **Boundary rule:** No direct data sharing or automatic synchronization exists or is permitted between the personal OpenAI environment and the organisational Microsoft environment.
- **Installation is not authorization:** An installed plugin may not authenticate to, inspect, export from, or modify the organisational tenant unless a separate organisational approval and in-zone execution plan explicitly authorizes it.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| Installed | Package is present in the named client; no runtime capability is implied |
| Installation-only | Presence/version inspected, but no authenticated or capability test executed |
| Static-review-only | Public repository documentation/source reviewed without installing or running it |
| Tested | Named client, version/commit, inputs, permissions, outputs, and result were recorded from an executed test |
| Untested | No executed evidence on the named client; structural compatibility is not runtime proof |
| Prohibited under baseline | Execution would cross the two-zone boundary or use an unavailable/unsubscribed client |

## 3. Portfolio register

| Upstream | Official supported clients recorded by upstream | Installed/evaluation status | Version or commit pinned on 2026-07-18 | Update mechanism | Lab test status | Data-boundary classification |
|---|---|---|---|---|---|---|
| [`microsoft/Dataverse-skills`](https://github.com/microsoft/Dataverse-skills) | GitHub Copilot, Claude Code, Codex app/CLI, Cursor | **Installed** in Codex; installation-only | Installed plugin **v1.6.0**; upstream `main` commit [`2e651c7226dbe57a7c364e475f1849a99576e99a`](https://github.com/microsoft/Dataverse-skills/commit/2e651c7226dbe57a7c364e475f1849a99576e99a) | Codex marketplace upgrade; re-pin and review before accepting | Codex installation/version confirmed; no `dv-connect`, auth, MCP registration, tenant query, write, admin, or security test | Public upstream source allowed in personal zone; organisational Dataverse connection is **prohibited under current baseline** |
| [`microsoft/power-platform-skills`](https://github.com/microsoft/power-platform-skills) | Claude Code and GitHub Copilot CLI in the upstream README | Not installed; static-review-only | `main` commit [`54dbb6c6f903f4987440828a6548d72117813697`](https://github.com/microsoft/power-platform-skills/commit/54dbb6c6f903f4987440828a6548d72117813697); no repository release published | Upstream installer can enable auto-update for its supported clients; manual marketplace install/update also documented | Not executed on ChatGPT Work or Codex; Claude/GitHub paths untested and unavailable | Public source review allowed; tenant-connected tools and solution content stay in organisational zone |
| [`microsoft/power-cat-skills`](https://github.com/microsoft/power-cat-skills) | Microsoft Scout and GitHub Copilot CLI | Not installed; static-review-only | `main` commit [`f4bb4ad5bf55e2d50076292bd6301f6337d38083`](https://github.com/microsoft/power-cat-skills/commit/f4bb4ad5bf55e2d50076292bd6301f6337d38083); no repository release published | Add/update the upstream marketplace on a supported client; re-pin after review | Not executed; Microsoft Scout/GitHub Copilot unavailable; Codex compatibility not claimed by upstream | Public source review allowed; admin, Dataverse, Canvas, solution, and tenant evidence remain organisational-zone only |
| [`microsoft/skills-for-copilot-studio`](https://github.com/microsoft/skills-for-copilot-studio) | Claude Code, GitHub Copilot CLI, and VS Code with the Copilot Studio extension | Not installed; static-review-only | `main` commit [`d68d1a25cd3e6bdd80f8e046913a055c98a005fd`](https://github.com/microsoft/skills-for-copilot-studio/commit/d68d1a25cd3e6bdd80f8e046913a055c98a005fd) | Marketplace auto-update for Claude; manual GitHub Copilot update; VS Code extension auto-update when enabled | Not executed; supported AI clients are unavailable/unsubscribed; VS Code presence alone is not a test | Public YAML/templates may be reviewed; clone/pull/push/sync against organisational Copilot Studio is **prohibited from the personal zone** |

Supported-client statements describe what each upstream repository documents; they do not expand this lab’s subscriptions, permissions, or test matrix.

## 4. `microsoft/Dataverse-skills`

### Scope and local status

Provides `dv-overview`, `dv-connect`, `dv-query`, `dv-data`, `dv-metadata`, `dv-solution`, `dv-security`, and `dv-admin`, routing work across Dataverse MCP, Dataverse CLI/Python SDK, PAC CLI, and other documented fallbacks. Version 1.6.0 is installed in Codex, but only package presence is confirmed.

### Prerequisites and tools/MCP

- Dataverse environment and an entitled user/environment.
- `dv-connect` can install/check Dataverse CLI, Python SDK, and PAC CLI, authenticate, and register a `dataverse-<orgname>` MCP server.
- MCP access requires developer authentication, tenant admin consent, and per-environment allowlisting; SDK/PAC paths authenticate separately.
- Skills include read, write, solution lifecycle, security, and administrative operations, so the requested skill and consequence level must be explicit.

### Telemetry and permissions

- Upstream documents application-level metadata on outbound Dataverse requests, including plugin/version/skill/agent labels; it states prompts, tool arguments, and record data are not included in that telemetry.
- Server-side Dataverse security roles remain authoritative; the plugin cannot exceed the authenticated user’s rights.
- Credentials are documented as OS-credential-store or in-memory values rather than external-service payloads.
- Destructive, privilege, solution import/export, bulk-data, and admin operations require explicit confirmation and organisational controls.

### Local adaptation and test plan

- Keep `dv-connect` disabled under the current personal/organisational separation.
- Use public documentation and synthetic schemas only in the personal zone.
- The orchestrator may reference Dataverse skill contracts, but must not call tenant tools or infer successful installation means tenant readiness.
- First permitted test, if organisational approval is later granted, must occur in an approved organisational development environment with synthetic/non-confidential data, least privilege, telemetry review, explicit read-only scope, and rollback evidence.

**Test status:** Codex installation-only; all authenticated capabilities untested.

**Local owner:** Rohit.
**Revalidate:** 2026-08-01.

## 5. `microsoft/power-platform-skills`

### Scope and local status

Marketplace of Power Pages, model-apps, MCP-apps, code-apps-preview, mobile-app, canvas-apps, and Power Automate plugins. The upstream README currently targets Claude Code and GitHub Copilot CLI; neither is subscribed. Do not claim Codex support merely because the packaging resembles an open plugin format.

### Prerequisites and tools/MCP

- Requirements vary by plugin and can include PAC CLI, Node.js, .NET 10, Azure CLI, Power Apps Wrap, connectors, and authenticated Power Platform environments.
- Canvas Apps uses the Canvas Authoring MCP server.
- Power Automate uses a FlowAgent MCP server and documents Node.js 18+ plus Azure CLI.
- Plugins can edit files, run shell/PAC/build commands, and invoke MCP servers.

### Telemetry and permissions

- Upstream documents 1DS anonymous usage telemetry for adopting plugins, currently `power-pages`; it is default-on with per-plugin command and environment-variable opt-out mechanisms.
- Permission guidance warns that auto-approval gives the agent the user’s access and recommends narrowly scoped tool allow-lists.
- Each selected plugin still requires a separate script/dependency/network/authentication review; marketplace membership is not blanket approval.

### Local adaptation and test plan

- Do not run the upstream auto-installer in this baseline; it targets unavailable clients and enables auto-update.
- Evaluate one narrow plugin at a time against an exact commit and copy no tenant data into the personal zone.
- A local wrapper must add the two-zone stop condition, explicit telemetry decision, approved command allow-list, and synthetic fixture tests.

**Test status:** Static-review-only; no active-client execution.

**Local owner:** Rohit.
**Revalidate:** 2026-08-01.

## 6. `microsoft/power-cat-skills`

### Scope and local status

Power CAT-curated plugins cover adoption/storytelling, Canvas analysis and migration, code apps, Dataverse Web API queries, developer-environment governance, pro-code evaluation, admin digest, Power Automate solution review, and Power Pages review. Upstream support is stated for Microsoft Scout and GitHub Copilot CLI, neither an active runtime for this lab.

### Prerequisites and tools/MCP

- Some plugins require a companion foundation plugin from `microsoft/power-platform-skills`.
- Canvas scenarios require Canvas Authoring MCP configuration.
- Individual skills can require PAC, solution archives, local HTML/viewer assets, environment administration, or external/public status sources.

### Telemetry and permissions

- No repository-wide telemetry statement was found in the reviewed top-level README; telemetry is therefore **unknown per plugin** until its manifest/scripts are inspected.
- Upstream warns that plugins can edit files, run shell commands, and invoke MCP, and recommends narrow approvals rather than allow-all modes.
- Governance/admin skills can create environments or inspect operational information; those actions require organisational-zone authorization.

### Local adaptation and test plan

- Retain as a reference catalog until a narrow capability is selected.
- Do not install a companion plugin implicitly; register and approve every transitive dependency first.
- Prefer static analysis of synthetic solution packages for an initial active-client experiment; exclude admin digest and tenant-management operations under the current boundary.

**Test status:** Static-review-only; supported clients unavailable; Codex path unclaimed and untested.

**Local owner:** Rohit.
**Revalidate:** 2026-08-01.

## 7. `microsoft/skills-for-copilot-studio`

### Scope and local status

Provides YAML authoring, validation, templates, patterns, test/evaluation support, and manage/author/test/advisor agents for Copilot Studio. The manage capability can clone, pull, push, and synchronize local files with cloud agents, making the data boundary material.

### Prerequisites and tools/MCP

- Node.js 18+.
- Claude Code, GitHub Copilot CLI, or VS Code as documented by upstream.
- VS Code Copilot Studio extension is required for push/pull/clone operations.
- Local filesystem, shell/scripts, YAML schemas/templates, test endpoints, and tenant authentication may be used depending on the selected workflow.

### Telemetry and permissions

- No top-level telemetry statement was found in the reviewed README; inspect manifests, hooks, scripts, dependencies, and extension privacy terms before installation.
- Clone/pull/push/sync can expose confidential agent instructions, knowledge references, action metadata, variables, and test evidence. Least privilege, source control, secret handling, and confirmation are mandatory.

### Local adaptation and test plan

- Do not use cloud synchronization from the personal OpenAI zone.
- Public schemas/templates may inform a sanitized local adapter; tenant agent assets must stay in the organisational zone.
- Because the documented supported AI clients are unavailable/unsubscribed, keep the adapter reference-only and untested. VS Code being installed does not establish the required agent-plugin runtime or tenant authorization.

**Test status:** Static-review-only; no install, YAML runtime test, tenant auth, or sync.

**Local owner:** Rohit.
**Revalidate:** 2026-08-01.

## 8. Evaluation and upgrade gate

Before any install or upgrade:

- [ ] Exact version/commit and upstream change log recorded.
- [ ] Official supported client matches an active, licensed client; otherwise status remains reference-only/untested.
- [ ] Transitive plugins, CLIs, SDKs, MCP servers, extensions, and minimum versions identified.
- [ ] Scripts, package dependencies, network endpoints, telemetry defaults/opt-outs, credential handling, and update behavior reviewed.
- [ ] Read/write/admin/destructive tools and required permissions documented; least-privilege allow-list approved.
- [ ] Personal vs organisational zone selected; automatic cross-zone synchronization absent.
- [ ] Synthetic/non-confidential test fixture, expected output contract, negative/security cases, and rollback defined.
- [ ] ChatGPT Work and Codex/VS Code test evidence captured where those clients are supported; no Claude/GitHub/Cursor execution claim without actual evidence.
- [ ] Owner, adoption decision, local adaptations, unresolved questions, and next revalidation date recorded.

## Official sources

- [Microsoft Dataverse skills](https://github.com/microsoft/Dataverse-skills)
- [Microsoft Power Platform skills](https://github.com/microsoft/power-platform-skills)
- [Microsoft Power CAT skills](https://github.com/microsoft/power-cat-skills)
- [Microsoft skills for Copilot Studio](https://github.com/microsoft/skills-for-copilot-studio)
- [OpenAI skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [OpenAI build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI plugins](https://learn.chatgpt.com/docs/plugins)
