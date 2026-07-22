# Codex Adapter

## Status

**Codex/VS Code: full case suite executed on 2026-07-18.**

Use the portable [skill](../../SKILL.md) as a repository or user Agent Skill.
This file documents host boundaries only; it does not fork the workflow.

## Adaptation

- Discover the skill from portable `name` and `description` front matter.
- Prefer read-only public retrieval and repository inspection.
- Use local deterministic validation for YAML, JSON, Markdown links, front
  matter, required sections, test coverage, and schema fixtures.
- Require explicit approval for repository writes outside the requested scope.
- Record Codex host/runtime, sandbox, date, sources, output, score, deviations,
  and reviewer for every golden run.

## Permissions and boundary

Do not invoke the installed Dataverse plugin, run `dv-connect`, authenticate,
register a tenant MCP server, install plugins, query an environment, request
credentials, or transfer organisational content. Installation-only plugin
status is neither authorization nor evidence.

Public and synthetic data are allowed. Confidential tenant data, exports,
screenshots, Message Center content, logs, and configuration remain in the
organisational zone with no automatic sync.

## Required evaluation

Run local package checks plus the parity subset in
[the test contract](../../tests/README.md). Local static checks do not by
themselves establish current product facts or ChatGPT Work parity. The Codex
results are recorded under `tests/results/codex/2026-07-18/`; administrative
scoring remediation preserves every named dimension for GOLD-001, GOLD-002,
and GOLD-005. Explicit loading was used, so automatic project-skill discovery
remains outside the evidence established by those records.
