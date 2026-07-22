# Revalidation Policy

Use risk-based expiry plus event-triggered review. A source pointer in this
package is never proof that a current claim remains true.

## Maximum validity

| Risk and volatility | Examples | Maximum age |
|---|---|---:|
| Very high | Preview/experimental features, model availability, regional rollout, credit/rate changes | 14 days |
| High | Licensing, entitlement, capacity, security controls, DLP, identity, residency, ALM limitations | 30 days |
| Medium | GA behavior, supported limits, cloud/language availability | 90 days |
| Low | Stable verification methodology and internal delivery rules | 180 days |

For a claim spanning multiple classes, use the shortest interval. Set:

`revalidation_date = min(verified_date + shortest_interval, known_earlier_event)`

If the source's last-updated date is unknown, do not automatically reject it,
but cross-check the claim with another current first-party source and shorten
the validity window when the uncertainty is material.

## Immediate revalidation events

Revalidate before the recorded date after:

- a release-plan, status-banner, What's new, or Message Center change;
- a licensing guide, rate, entitlement, capacity, or enforcement change;
- a regional rollout, model-hosting, residency, or consent change;
- a deprecation, migration, security advisory, DLP, identity, or ALM change;
- a major client/model/runtime change;
- a dated tenant or lab observation that contradicts the claim record.

## Stale-source behavior

A claim is stale when its verified date exceeds the maximum applicable age or
an immediate event is known. A stale record is a research lead only.

When a stale material claim cannot be refreshed live:

1. retain the old source and date for traceability;
2. label the current claim `Open`;
3. set release status to `UNKNOWN` unless another current source establishes it;
4. set `production_recommendation` to `false`;
5. list the live source or owner required;
6. set the revalidation date to the current verification date so the claim
   remains visibly due.

## Record hygiene

Record `verified_date` as the date the verifier actually inspected the source,
not the report-generation date copied from an older record. Record source
last-updated separately. Mark replaced claims `Superseded` and link their
successors; do not rewrite historical verification dates.
