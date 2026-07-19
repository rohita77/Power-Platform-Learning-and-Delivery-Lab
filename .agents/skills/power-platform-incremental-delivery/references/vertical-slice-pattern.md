# Vertical-Slice Pattern

## Definition

A vertical slice proves one observable user or operational outcome through the
minimum necessary experience, rules, state change or action, feedback,
telemetry, and evidence. It is not a horizontal component inventory.

Every slice must follow:

`entry -> validation -> persistence/action -> feedback -> telemetry -> evidence`

## Required sections

### Outcome

State one measurable result for one primary persona. Name the host surface and
journey. If no observable outcome exists, return `Open`.

### Entry

Define the initiating UI action, event, request, command, or scheduled trigger.
Identify the actor and authorization context.

### Validation

Define required fields, schema checks, business rules, duplicate/idempotency
checks, permission checks, and the failure contract before action.

### Persistence or action

Identify the authoritative owner of every write, message, integration call, or
lifecycle transition. Reuse existing paths and prevent duplicate handlers.

### Feedback

Define success, validation error, permission error, processing failure,
disabled, stale, retry, and concurrent-action behavior visible to the actor.

### Telemetry

Define events, correlation identifiers, failure signals, operational owner,
alerts, and privacy-safe retention. Telemetry must not capture secrets or
confidential payloads unnecessarily.

### Evidence

Define the exact source, test, build, package, deployment, readback, and runtime
evidence required. State the highest level actually available.

## Architecture spine

Include only decisions needed for the slice:

- **Experience:** persona, host, UI states, accessibility, responsive behavior.
- **Data:** tables, keys, relationships, ownership, lifecycle, audit, retention.
- **Integration:** contracts, identity, retry, idempotency, failure isolation.
- **AI:** model purpose, grounded inputs, validated output, abstention, human
  review, evaluation, capacity.
- **Security:** least privilege, roles, field access, DLP, classification,
  approvals, audit.
- **Operations:** support owner, monitoring, alerts, capacity, replay, runbook.
- **ALM:** solution ownership, configuration, dependencies, environment path,
  deployment checks, rollback.

Use an empty array for a dimension that is demonstrably not required. Do not
invent components to make every dimension non-empty.

## Acceptance criteria

Write independently observable criteria with IDs and explicit evidence. Cover:

- valid happy path;
- required validation failure;
- permission or security failure;
- duplicate, retry, or concurrent action where applicable;
- user-visible feedback;
- telemetry and operational evidence;
- deployment/readback evidence; and
- rollback trigger and verification.

## Horizontal-plan rejection

Reject plans such as "create all tables", "build all flows", or "configure the
whole security model" when they do not connect entry to evidence. Preserve any
reusable design as context, select the smallest end-to-end outcome, and return
`Open` if that outcome is not supplied.

## Synthetic golden pattern

For the synthetic model-driven service-request scenario:

- **Outcome:** an authorised service agent creates one valid synthetic service
  request and can observe its persisted status.
- **Entry:** model-driven app create action and main form.
- **Validation:** required synthetic title, category, priority, and permitted
  owner; reject missing or invalid values before save.
- **Persistence:** one solution-owned Dataverse service-request table and the
  platform save path; no duplicate custom writer.
- **Feedback:** save confirmation, validation errors, permission failure, and
  stale/concurrent update handling.
- **Telemetry:** privacy-safe create/failure signal, correlation reference,
  audit decision, and operational owner.
- **Evidence:** source review, schema/form/role checks, automated checks where
  feasible, solution artifact integrity, target import/readback, and runtime
  create/failure proof kept as distinct levels.

Do not add unrelated tables, flows, agents, integrations, or AI features to
this first slice.
