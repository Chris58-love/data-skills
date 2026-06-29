---
name: business-data-analysis-pipeline
description: Standardize multi-source business data analysis workflows into staged, auditable deliverables. Use when Codex needs to build, inspect, repair, or run a low-code business analysis pipeline over changing data types such as reviews, surveys, interviews, sales tables, CRM exports, competitive intelligence, social content, operational spreadsheets, or mixed Excel/CSV files, especially when outputs need fixed folders, QC reports, run logs, evidence-backed conclusions, conservative report wording, or branch reruns that must not overwrite the main workflow.
---

# Business Data Analysis Pipeline

## Core Rule

Treat the skill as a workflow standard, not a fixed comments-analysis template. First inspect the live project and data contract, then choose the smallest staged flow that creates traceable outputs, QC, logs, and a final delivery index.

## Decision Tree

1. If the user only asks for a plan or design, describe the recommended pipeline and stop.
2. If a project already has round folders, infer the current round from files and logs before writing anything.
3. If inputs are new, create or ask for a minimal `pipeline_config.json` using `references/project-config-contract.md`.
4. If the task is a branch rerun, write to a new branch round or output folder and do not modify the main round outputs.
5. If the task creates a final report, run the deliverable checker script before declaring completion.

## Standard Stages

Use these stages as defaults. Rename round numbers to match the project, but keep the contracts.

1. Profile: inventory files, sheets, fields, row counts, keys, risks, and manual confirmations.
2. Standardize: normalize fields into analysis-ready tables while preserving raw input copies.
3. Clean: deduplicate, parse types, handle missing values, and record exclusions.
4. Classify: tag, code, segment, map entities, or derive business dimensions appropriate to the data type.
5. Analyze: calculate metrics, weighted records, segments, comparisons, opportunities, or diagnostic tables.
6. Package: create report draft, analysis package, chart data, evidence map, and limitations.
7. Review: prepare human review questions, risk audit, and presentation assets.
8. Finalize: apply confirmed decisions, generate final report, delivery index, QC report, and run log.

Skip stages that do not apply, but record the skip and reason in the run log.

## Data Type Routing

Read `references/data-type-routing.md` when the input is not the original project shape or mixes data types. Select only the relevant routes.

Use `references/qc-and-delivery-rules.md` for required validation gates.
Use `references/report-expression-rules.md` before writing user-facing conclusions.
Use `references/project-config-contract.md` when creating or repairing `pipeline_config.json`.
Use `references/trae-ai-adapter.md` when the workflow must be handed to Trae AI or another agent that cannot load Codex skills.

## Branch Reruns

For exclusions, scenario reruns, period refreshes, source additions, or audience-specific reports:

- Keep main outputs read-only.
- Create a new named branch folder or round.
- Write exclusion rules, filtered inputs, recomputed analysis tables, comparison table, report, QC, and run log.
- State that differences reflect the branch sample or scenario, not market-wide causality, unless external evidence supports that claim.

## Required Final Checks

Before final response for any generated deliverable:

```powershell
py -3 <skill>/scripts/check_deliverables.py <project-root>
```

Fix any `ERROR` result unless the user explicitly accepts the limitation. Warnings may pass if documented in the final response.

## Trae AI Handoff

When asked to make this usable in Trae AI, provide the single-file prompt from `references/trae-ai-adapter.md` or a project-specific copy of it. Trae should receive self-contained instructions, not Codex-only skill metadata.
