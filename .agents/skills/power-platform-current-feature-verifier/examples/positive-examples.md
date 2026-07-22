# Positive Examples

These examples demonstrate method and output shape. They are not current
product evidence and must never be copied as verified facts.

## Example 1: bounded experiment recommendation

**Request**

> Verify whether Capability A can be used in a Singapore-based English-language
> experiment and identify the production gates.

**Good behavior**

1. Split status, regional availability, language, licensing, processing
   geography, security, and ALM into atomic claims.
2. Inspect live applicable A1 pages and a current release source.
3. Record exact source language and dates.
4. Recommend only the experiment actually supported by the evidence.

**Illustrative result**

| Field | Result |
|---|---|
| Recommendation | Use only for the stated synthetic-data experiment; do not infer production approval |
| Production recommendation | false |
| Evidence label | Confirmed for the bounded experiment; Open for production |
| Release status | Preserve the exact live first-party label |
| Verified date | Date sources were actually inspected |
| License/capacity | Identify maker, runtime, meter, capacity, and enforcement separately |
| Geography/language | Identify environment, processing, consent, connected-service, and language evidence separately |
| Limitations | List all applicable gaps and dependencies |
| Security/governance | Synthetic data, least privilege, DLP, no tenant access from personal zone |
| ALM implications | State solution, environment, deployment, rollback, and exit-plan evidence |
| Sources | Current first-party pages with update and verification dates |
| Open questions | Production contract, exact tenant controls, operational owner |
| Revalidation date | Shortest applicable risk window |

Why this is positive: it answers the safe, evidence-supported part without
turning partial evidence into a production recommendation.

## Example 2: resolved comparison

**Request**

> Compare current Capability A and Capability B for an ALM-managed prototype.

**Good behavior**

- Verify each capability independently rather than assuming their names imply a
  shared lifecycle.
- Preserve each source's exact status and terminology.
- Compare license, geography, limitations, security, and ALM on separate rows.
- If all material prototype claims are current and consistent, make a bounded
  prototype recommendation.
- Keep production suitability separate and `Open` where production evidence
  was not requested or established.

## Example 3: current OpenAI/Codex claim

**Request**

> Is this Agent Skill behavior currently supported in ChatGPT Work and Codex?

**Good behavior**

- Trigger because the support claim is current and client-specific.
- Use live official OpenAI sources (A2) for documented behavior.
- Separate documented support from executed lab evidence.
- Mark ChatGPT Work and Codex as active test targets, but label runtime status
  `untested` unless the exact version, date, input, output, and result were
  actually recorded.
- Do not infer support for Claude Code, GitHub Copilot, Cursor, M365 Copilot, or
  Copilot Studio.
