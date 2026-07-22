# Packaged Source Governance Baseline

## Provenance and packaged authority

This self-contained reference is derived from the Power Platform Learning Lab
canonical source `canonical-pack/2026-07-18/02_SOURCE_GOVERNANCE.md` (canonical
pack v1.1, verified 2026-07-18). The canonical file remains the provenance and
maintenance source. This local file is the runtime reference when the skill is
packaged without the host repository.

The packaged skill must not require the canonical repository path to exist.
Reconcile this local baseline with the canonical source when preparing a new
skill release.

## Stable governance rules

1. Verify every current or consequential claim live from an applicable
   first-party source. Package content, memory, examples, and prior results are
   research context only.
2. Prefer capability-specific Microsoft product, admin, licensing, limits,
   security, geography, and ALM documentation for Microsoft claims. Use
   official OpenAI documentation for current OpenAI and Codex claims.
3. Use release plans, release notes, What's new, and official repositories to
   cross-check rollout and change, not to override a more specific current
   product or contractual source without clear applicability.
4. Record the exact claim, source URL, authority level, source last-updated
   date when available, verification date, applicability, and supported claim.
5. Separate evidence confidence from product release status. Never infer GA,
   entitlement, residency, security approval, or production suitability from
   tenant visibility or a successful demonstration.
6. Preserve material conflicts. If current applicable licensing, capacity,
   geography, status, or security evidence is absent, stale, ambiguous, or
   conflicting, label the result `Open` and stop before production advice.
7. Apply the packaged revalidation policy and re-open expired claims. Use the
   shortest applicable validity window and any earlier change trigger.
8. In personal ChatGPT/Codex, use public, synthetic, and approved
   non-confidential material only. Keep tenant evidence, credentials, exports,
   logs, screenshots, Message Center content, and configuration in the
   organisational zone with no automatic cross-zone synchronization.

See [source authority](source-authority.md),
[claim status language](claim-status-language.md), and
[revalidation policy](revalidation-policy.md) for the operational method.
