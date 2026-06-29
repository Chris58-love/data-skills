#!/usr/bin/env python3
"""Small final gate for staged business data analysis projects."""
from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path


PLACEHOLDER_RE = re.compile(r"(\{[A-Za-z_][A-Za-z0-9_]*\}|\[TODO[^\]]*\]|TODO:)")


def load_config(root: Path) -> dict:
    path = root / "pipeline_config.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def find_files(root: Path, patterns: list[str]) -> list[Path]:
    out: list[Path] = []
    for pattern in patterns:
        out.extend(root.rglob(pattern))
    return sorted(set(out))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "final_report.md").write_text("done", encoding="utf-8")
            (root / "R1_run_log.md").write_text("done", encoding="utf-8")
            (root / "final_qc_report.xlsx").write_text("placeholder", encoding="utf-8")
            (root / "final_delivery_index.xlsx").write_text("placeholder", encoding="utf-8")
            assert main_for_root(root) == 0
            (root / "final_report.md").write_text("{n_total}", encoding="utf-8")
            assert main_for_root(root) == 1
        print("OK self-test passed")
        return 0
    if args.project_root is None:
        parser.error("project_root is required unless --self-test is used")
    return main_for_root(args.project_root)


def main_for_root(project_root: Path) -> int:
    root = project_root.resolve()
    if not root.exists():
        print(f"ERROR project root does not exist: {root}")
        return 2

    config = load_config(root)
    final_report = config.get("final_report")
    reports = [root / final_report] if final_report else find_files(root, ["*final_report*.md", "*final*.md"])
    reports = [p for p in reports if p.exists()]
    qc_files = find_files(root, ["*qc*.xlsx", "*validation*.xlsx", "*quality*.xlsx"])
    logs = find_files(root, ["*run_log*.md", "*log*.md"])
    delivery = find_files(root, ["*delivery_index*.xlsx", "*delivery*.xlsx"])

    errors: list[str] = []
    warnings: list[str] = []

    if not reports:
        errors.append("missing final report markdown")
    if not qc_files:
        errors.append("missing QC or validation workbook")
    if not logs:
        errors.append("missing run log")
    if not delivery:
        warnings.append("missing delivery index")

    for report in reports:
        text = report.read_text(encoding="utf-8", errors="ignore")
        matches = sorted(set(m.group(0) for m in PLACEHOLDER_RE.finditer(text)))
        if matches:
            errors.append(f"{report.relative_to(root)} has placeholders: {', '.join(matches[:10])}")

    for item in errors:
        print(f"ERROR {item}")
    for item in warnings:
        print(f"WARN {item}")
    if not errors and not warnings:
        print("OK deliverables look complete")
    elif not errors:
        print("OK with warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
