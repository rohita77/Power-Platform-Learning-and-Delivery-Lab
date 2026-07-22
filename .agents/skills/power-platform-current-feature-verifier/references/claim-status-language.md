# Claim Status Language

Keep evidence confidence, release status, and recommendation separate. A claim
can have strong evidence that a capability is preview, deprecated, unavailable,
or unknown.

## Evidence labels

| Label | Meaning and permitted use |
|---|---|
| Confirmed | Directly supported by current, applicable first-party evidence |
| Preview | Current first-party evidence explicitly identifies preview behavior; preserve the source's exact preview label |
| Announced | Officially announced or planned but not established as currently available |
| Inference | Reasoned conclusion from identified evidence; state the reasoning and uncertainty |
| Recommendation | Advice based on separately labelled evidence and constraints |
| Assumption | Unverified input used only to bound analysis; never close a material gate |
| Open | Evidence is absent, stale, ambiguous, conflicting, inapplicable, or prohibited to retrieve |
| Superseded | Historical claim replaced by a newer identified claim record |

Use one overall label representing the weakest material dependency. Record
different labels per atomic claim when the evidence differs.

## Release status

Use these normalized values while also quoting the source's exact wording in
the claim record:

| Value | Rule |
|---|---|
| GA | Use only when current applicable first-party evidence says generally available or an applicable release status is GA |
| PRODUCTION_READY_PREVIEW | Preserve the exact label; it remains preview and requires an exit plan and explicit risk acceptance |
| PUBLIC_PREVIEW | Do not make it a default production dependency; require an experiment and exit plan |
| EXPERIMENTAL | Lab-only unless an approved exception exists |
| PLANNED | Research/backlog only; do not commit a production dependency |
| DEPRECATED | Stop new adoption and create a migration plan |
| UNKNOWN | Treat as not approved until verified |

Do not infer GA from a working tenant, UI visibility, a blog post, a demo, or
the absence of a preview banner.

## Recommendation language

For resolved claims, lead with a bounded decision:

> Recommendation: Use for the stated experiment, subject to the listed license,
> geography, security, limitations, and ALM controls.

For a material gap or conflict, use:

> Recommendation: Open — no production recommendation. Resolve the listed
> licensing, residency, status, or security evidence before proceeding.

Never use `Confirmed` as a synonym for recommended, production-ready,
licensed, or compliant. Never use `Preview` alone to state whether a feature
is suitable for an approved experiment.

## Atomic-claim example

A question such as “Can we use this agent feature in Singapore production?”
contains separate claims:

- the capability and its exact release status;
- rollout to the applicable cloud/region/language;
- maker and runtime entitlements;
- metering/capacity and exhaustion behavior;
- data-at-rest and AI-processing locations;
- required consent and connected-service paths;
- identity, DLP, audit, retention, and approval controls;
- solution, deployment, rollback, and monitoring support.

Confirming one claim does not resolve the others.
