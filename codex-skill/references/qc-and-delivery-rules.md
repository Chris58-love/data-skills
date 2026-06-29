# QC and Delivery Rules

Every non-trivial stage must produce:

- An output artifact.
- A QC or validation artifact.
- A run log that lists inputs, outputs, row counts, major assumptions, and completion status.

Final delivery must include:

- Final report or final analysis package.
- Delivery index listing files, purpose, audience, and status.
- QC report with pass/fail rows.
- Evidence map for claims or a documented reason it is not applicable.
- Pending-confirmation list when business judgment is required.

Blocking failures:

- Missing required input.
- Missing final output.
- Missing QC report or run log.
- Unresolved placeholders such as `{n_total}` or `[TODO]`.
- Untraceable exclusions or filters.
- Unsupported strong claims.
- Main-flow overwrite during a branch rerun.

Warnings:

- Small sample size.
- Weak-signal-only evidence.
- Manual review incomplete.
- Data type conversion lossy but documented.
- Optional presentation assets missing.
