# Durable Test Results

Store executed evidence here without changing the canonical test input:

```text
results/
  codex/
  chatgpt-work/
  human-review/
  result-record.schema.json
```

Use one JSON file per case, runtime, and execution date:

`<case-id>-<yyyy-mm-dd>-<runtime>.json`

Validate each record against
[result-record.schema.json](result-record.schema.json). Every record must
contain:

- case ID and skill version;
- runtime/client;
- model and reasoning setting where available;
- execution date;
- exact unchanged test input;
- source URLs and verification dates;
- generated output;
- schema-validation result;
- scoring;
- deviations;
- reviewer;
- final `Pass` or `Fail`.

For dimension-complete golden scoring, each case-defined scoring dimension
records its exact name, numeric score, evidence, deviation, and `Pass` or
`Fail` result. A result record in a dated Codex directory resolves
`../../../output-schema.json` relative to its own file location.

Use `null` for model or reasoning setting only when the client does not expose
the value. Do not omit the field. Store no credentials, confidential tenant
evidence, customer data, environment exports, private URLs, or cross-zone
content. A sanitized conclusion with public sources is allowed.

Codex executed all cases on 2026-07-18; its durable records are stored under
`codex/2026-07-18/`, with administrative scoring remediation applied to
GOLD-001, GOLD-002, and GOLD-005. Authoritative ChatGPT Work findings report
that GOLD-001, GOLD-002, and GOLD-005 executed and passed on 2026-07-18.

Named human expert review is **Pass** in
[the signed GOLD-005 review](human-review/GOLD-005-rohit-review-2026-07-18.md),
dated 2026-07-18. The review closes the named expert gate while preserving the
tenant-specific `Open` result and `production_recommendation: false`.
