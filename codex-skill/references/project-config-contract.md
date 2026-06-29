# Project Config Contract

Use a project-level `pipeline_config.json` when the data type, stages, report outputs, or branch rules vary.

Minimum shape:

```json
{
  "project_name": "business analysis project",
  "input_root": "data/input",
  "raw_archive_root": "00_input_original",
  "data_types": ["reviews", "survey", "sales"],
  "stages": ["profile", "standardize", "clean", "classify", "analyze", "package", "review", "finalize"],
  "final_report": "final_report.md",
  "no_overwrite": true,
  "required_checks": ["input_inventory", "qc_report", "run_log", "delivery_index", "no_placeholders"]
}
```

Optional keys:

- `branch_name`: Short branch name such as `brand_excluded`, `survey_only`, or `region_refresh`.
- `exclusion_rules`: List of field and keyword rules for branch reruns.
- `source_contracts`: Expected sheets, columns, primary keys, and row-count ranges per input file.
- `report_rules`: Project-specific wording rules, forbidden claims, and required caveats.
- `delivery_files`: Final files that must exist before handoff.

Prefer JSON because Python can validate it with the standard library. Do not require YAML unless the project already uses it.
