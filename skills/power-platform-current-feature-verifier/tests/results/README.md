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

Use `null` for model or reasoning setting only when the client does not expose
the value. Do not omit the field. Store no credentials, confidential tenant
evidence, customer data, environment exports, private URLs, or cross-zone
content. A sanitized conclusion with public sources is allowed.

The empty directories are intentional. No golden, parity, or human-review
result has been executed or recorded for v0.1.0 yet.
