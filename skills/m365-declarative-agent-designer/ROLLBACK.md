# Rollback

Rollback is local and package-level only. This candidate has no tenant, runtime,
deployment, or persisted organisational state to reverse.

## Triggers

- a schema or validator accepts prohibited input or output;
- canonical and adapter contracts diverge;
- provenance, contradiction, abstention, or lineage integrity fails;
- model-authored output claims external validation success;
- a forbidden Microsoft artifact or operation enters the package; or
- a behavior change breaks an accepted synthetic fixture.

## Procedure

1. Stop candidate evaluation and mark the candidate unavailable.
2. Restore SKILL.md, schemas, validators, adapters, fixtures, tests, changelog,
   and this rollback record as one complete set from the last accepted file
   inventory.
3. Never mix carry-forward state or contract files from different versions.
4. Re-run the complete offline suite and recursive publication-copy comparison.
5. Require human review before returning the package to candidate status.

## Data

No hidden persistence exists. Synthetic fixtures can be restored from the
accepted package. User-controlled DesignResult and carry-forward objects must
be rejected if their contract version is incompatible; do not silently migrate
or reinterpret them.
