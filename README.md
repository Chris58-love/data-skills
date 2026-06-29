# Business Data Analysis Pipeline

Reusable workflow assets for standardized, auditable business data analysis.

This repository contains two entry points:

- `codex-skill/`: Codex skill folder. Install by copying this folder into a Codex skills directory, then invoke `$business-data-analysis-pipeline`.
- `trae-ai/trae-ai-business-data-analysis-pipeline-prompt.md`: Single-file prompt for Trae AI or any agent that cannot load Codex skills.

## What It Standardizes

- Multi-source input inventory.
- Field mapping and standardization.
- Cleaning, filtering, classification, and analysis.
- Evidence-backed reports.
- Branch reruns that do not overwrite the main workflow.
- QC reports, run logs, delivery indexes, and placeholder checks.

## Minimal Final Gate

Run this before treating a generated analysis package as done:

```powershell
py -3 .\codex-skill\scripts\check_deliverables.py <project-root>
```

Errors must be fixed before delivery unless explicitly accepted by the project owner.
