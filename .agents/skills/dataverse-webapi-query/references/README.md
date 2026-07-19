# Reference integrity notice

This directory is provenance and evaluator material only. The runtime skill is
self-contained and must not access any file in this directory during an
invocation.

The pinned upstream skill names these references, but none exists in the inspected repository tree:

- `webapi-syntax.md`
- `metadata-discovery.md`
- `fetchxml-mapping.md`
- `common-errors.md`
- `aggregation.md`
- `authentication.md`
- `examples.md`
- `power-apps-contexts.md`

Do not invent their contents or imply they were reviewed. The supported runtime
boundary is fully stated inline in `SKILL.md`. Evaluators use this notice to
verify provenance and the declared unsupported cases.

## Experiment disposition

| Reference | Classification | Controlled boundary |
| --- | --- | --- |
| `webapi-syntax.md` | Optional | Basic operators explicitly preserved in `SKILL.md` remain supported. Advanced lambdas, paging-cookie mechanics, and undocumented operators are unsupported. |
| `metadata-discovery.md` | Unsupported | MCP, `EntityDefinitions`, environment discovery, and live metadata access are prohibited. |
| `fetchxml-mapping.md` | Optional | Simple entity/filter and single-link mappings remain supported. Complex or nested mappings require abstention. |
| `common-errors.md` | Optional | Explain errors directly attributable to supported syntax. Catalog-dependent and authentication-related diagnosis is unsupported. |
| `aggregation.md` | Unsupported | Explain the conceptual FetchXML fallback for grouped aggregates, but emit no runnable OData, FetchXML, or client-side workaround. |
| `authentication.md` | Unsupported | Authentication, browser-session, token, Postman, MSAL, and live-test paths are prohibited. |
| `examples.md` | Optional | Its absence does not establish authority or block the narrow supported cases. |
| `power-apps-contexts.md` | Optional | Only the narrow host mappings preserved in `SKILL.md` are supported. Advanced host contracts require abstention, and generated service names must be confirmed. |
