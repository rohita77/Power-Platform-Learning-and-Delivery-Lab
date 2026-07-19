# Power CAT Dataverse Web API Compatibility Experiment Checkpoint

**Checkpoint date:** 2026-07-19
**Status:** Closed
**Adoption:** Repository-level approved — explicit invocation only
**Closure commit:** `62561a97b4e914508df35c403039d36e3dcaf864`

## Outcome

The `dataverse-webapi-query` repository adapter is approved for explicit use through `$dataverse-webapi-query`. Implicit invocation remains unproved, unsupported, and outside the operating contract. Microsoft does not claim upstream Codex support for the Power CAT marketplace.

The canonical decision is published in `canonical-pack/2026-07-18/10_UPSTREAM_SKILLS_REGISTER.md`. The tested adapter behavior and immutable result evidence were not changed during closure.

## Evidence boundary

- Codex `explicit-0.3.1`: 28/28 full-suite cases passed.
- ChatGPT Work parity: `GOLDEN-001`, `NEGATIVE-004`, and `SECURITY-006` passed 3/3.
- Evidence-contract remediation `0.3.2`: strict Codex profile 29/29, strict Work profile 3/3, and answer schema 32/32.
- Recorded workflow-operation failures: zero.
- Provenance, SHA-256, immutable-evidence, schema, fixture, placeholder, secret-scan, package, and copy-equality gates passed.
- Both `git diff --check` and the staged-diff whitespace gate passed before closure commit.
- No authentication, tenant access, token handling, live metadata, MCP, `dv-*` invocation, plugin installation, confidential-data access, Dataverse operation, external write, or push occurred.

This evidence proves the recorded repository-level explicit-invocation contract only. It does not prove implicit selection, user-level installation, authentication, tenant capability, operational Dataverse work, or general upstream Codex compatibility.

## Enforced restrictions

Skill 6 may delegate to this specialist only when all of the following hold:

1. Select `$dataverse-webapi-query` explicitly; never rely on implicit discovery.
2. Limit work to public or synthetic OData, narrow supported FetchXML conversion, and supported host-specific query construction.
3. Preserve the inline JSON answer contract, deterministic schema resolution, and abstention when a material schema or host fact is unresolved.
4. Prohibit authentication, tenant access, tokens, live metadata, MCP, confidential data, plugin installation, and operational Dataverse changes.
5. Route authenticated reads, writes, metadata, solution, security, administration, and other tenant operations separately to explicitly authorized Microsoft Dataverse `dv-*` skills under their own controls.
6. Revalidate by 2026-08-01 and before any material upstream change, installation, upgrade, authentication, MCP registration, tenant-connected test, or adapter promotion.

## Repository state at checkpoint

The closure commit contains only the canonical upstream-register change and the complete experiment evidence package. Pre-existing unrelated worktree changes remain outside the closure and checkpoint scope. This checkpoint and its paired prompt log are the only files intended for the follow-up checkpoint commit. No push is authorized.
