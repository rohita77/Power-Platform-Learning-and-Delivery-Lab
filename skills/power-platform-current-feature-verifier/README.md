# Power Platform Current Feature Verifier

**Owner:** Rohit Acharya, Power Platform Learning Lab

**Version:** 0.1.0

Version 0.1.0 is a narrow Agent Skills-compatible package for verifying current
Power Platform, M365 Copilot, Copilot Studio, Dynamics 365, OpenAI/Codex,
licensing, capacity, geography/language, limits, release status, security,
governance, and ALM claims.

It verifies method, not facts: every current claim requires live applicable
first-party evidence. Examples, tests, canonical-pack baselines, old reports,
tenant visibility, and memory are never permanent product authority.

## Dependencies

**Upstream skill/plugin runtime dependencies for v0.1.0: none.**

Public first-party documentation is a source dependency retrieved at
verification time; it is not an installed plugin dependency. The package does
not depend on or authorize the installed Dataverse plugin.

Local development validation uses Python 3.12.3, PyYAML 6.0.1, and jsonschema
4.10.3. Python must already be available. The Python packages must either be
available in the approved development environment or be installed into an
isolated development environment from
[requirements-dev.txt](requirements-dev.txt) with separately authorized package
feed/network access. Running the skill never installs dependencies.

## Package map

- [SKILL.md](SKILL.md): portable trigger, workflow, output, security, and stop
  contract.
- [references](references/source-governance.md): self-contained source
  governance, source hierarchy, claim language, and revalidation methodology.
- [templates](templates/verification-report.md): human report and YAML claim
  record.
- [examples](examples/positive-examples.md): positive and abstention behavior.
- [tests](tests/README.md): trigger, five golden, negative, security, parity,
  regression, result-record, and schema cases.
- [OpenAI adapter](adapters/openai/README.md) and
  [Codex adapter](adapters/codex/README.md): active test-target boundaries.
- [deferred clients](adapters/deferred-clients.md): untested Claude Code,
  GitHub Copilot, Cursor, and future organisational adaptations.
- [changelog](changelog.md): versioned behavior and remaining release evidence.

## Safety boundary

Personal ChatGPT Work and Codex may use public and synthetic information and
approved non-confidential repository artifacts. They must not authenticate to
an organisational tenant, access confidential tenant data, invoke the installed
Dataverse plugin, install a plugin, access an environment, request secrets, or
automatically synchronize content across zones.

If material licensing, capacity, residency, geography, release status, or
security evidence is absent, stale, ambiguous, or conflicting, the skill
returns `Open` and stops before a production recommendation.

## Compatibility and evidence

| Target | v0.1.0 position |
|---|---|
| ChatGPT Work | GOLD-001, GOLD-002, and GOLD-005 executed and passed on 2026-07-18 per the authoritative ChatGPT Work evaluation findings |
| Codex/VS Code | Full Codex case suite executed on 2026-07-18; administrative scoring remediation applied to GOLD-001, GOLD-002, and GOLD-005 |
| Claude Code | Untested deferred adapter |
| GitHub Copilot | Untested deferred adapter |
| Cursor | Untested deferred adapter |
| M365 Copilot | Future organisational-zone adaptation only; no runtime adapter |
| Copilot Studio | Future organisational-zone adaptation only; no runtime adapter |

See [the test contract](tests/README.md) for deterministic local checks and the
honest runtime proof boundary.

Named human expert review for GOLD-005 is **Pass**, signed by Rohit Acharya on
2026-07-18 in
[the GOLD-005 review record](tests/results/human-review/GOLD-005-rohit-review-2026-07-18.md).
The tenant-specific production decision remains `Open` with
`production_recommendation: false`.
