#!/usr/bin/env python3
"""Bootstrap the portable Mentor Codex workspace."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable


VERSION = "0.1.0"
LIT_DIRS = [
    "00_导航",
    "01_工作流与规范",
    "02_单篇笔记",
    "03_概念卡",
    "04_模板与比较笔记",
    "06_索引与清单",
]
EDIT_TEMPLATE_DIRS = [
    "原文",
    "01_论文正文",
    "02_文献",
    "03_概念",
    "04_理论",
    "05_材料与资料",
    "06_论证",
    "07_Codex修改",
    "08_版本",
    "09_投稿",
    "10_模板",
    "11_附件",
]


def expand_path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def write_text(path: Path, text: str, *, force: bool = False) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return f"skipped existing {path}"
    path.write_text(text, encoding="utf-8")
    return f"wrote {path}"


def read_template(name: str) -> str:
    template_dir = Path(__file__).resolve().parents[1] / "assets" / "templates"
    return (template_dir / name).read_text(encoding="utf-8")


def mkdirs(paths: Iterable[Path]) -> list[str]:
    results = []
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
        results.append(f"ensured {path}")
    return results


def config_json(project_root: Path, lit_vault_root: Path, edit_root: Path) -> str:
    return json.dumps(
        {
            "mentor_version": VERSION,
            "project_root": str(project_root),
            "lit_vault_root": str(lit_vault_root),
            "edit_root": str(edit_root),
            "skills": ["mentor", "du-wen-xian"],
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Mentor Codex workspace.")
    parser.add_argument("--project-root", required=True, help="Project root for AGENTS.md and workflow files.")
    parser.add_argument("--lit-vault-root", required=True, help="Obsidian literature vault root.")
    parser.add_argument("--edit-root", required=True, help="Paper-revision workspace root.")
    parser.add_argument("--paper-project-name", default=None, help="Optional paper project folder to create under edit root.")
    parser.add_argument("--write-codex-config", action="store_true", help="Also write ~/.codex/mentor/config.json.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files.")
    args = parser.parse_args()

    project_root = expand_path(args.project_root)
    lit_vault_root = expand_path(args.lit_vault_root)
    edit_root = expand_path(args.edit_root)

    results: list[str] = []
    results += mkdirs([project_root, lit_vault_root, edit_root])
    results += mkdirs(lit_vault_root / rel for rel in LIT_DIRS)

    results.append(write_text(project_root / "AGENTS.md", read_template("AGENTS.md"), force=args.force))
    results.append(write_text(project_root / "README_workflow.md", read_template("README_workflow.md"), force=args.force))
    results.append(write_text(project_root / "mentor_config.json", config_json(project_root, lit_vault_root, edit_root), force=True))

    results.append(write_text(lit_vault_root / "01_工作流与规范" / "AGENTS.md", read_template("AGENTS.md"), force=args.force))
    results.append(write_text(lit_vault_root / "01_工作流与规范" / "README_workflow.md", read_template("README_workflow.md"), force=args.force))
    results.append(write_text(lit_vault_root / "00_导航" / "知识库导航.md", read_template("知识库导航.md"), force=args.force))
    results.append(write_text(lit_vault_root / "06_索引与清单" / "paper_inventory.csv", read_template("paper_inventory.csv"), force=args.force))
    results.append(write_text(lit_vault_root / "06_索引与清单" / "concepts_index.md", read_template("concepts_index.md"), force=args.force))

    for template in [
        "single_paper_note_template.md",
        "comparative_literature_review_template.md",
        "draft_editing_report_template.md",
        "research_gap_memo_template.md",
    ]:
        results.append(
            write_text(
                lit_vault_root / "04_模板与比较笔记" / template,
                read_template(template),
                force=args.force,
            )
        )

    edit_readme = (
        "# 改论文工作区\n\n"
        "这里存放草稿、编辑报告、结构修改、论证修改、审稿回复和投稿材料。\n\n"
        "原则：不要把这些执行性文件混入 Obsidian 文献知识库。\n"
    )
    results.append(write_text(edit_root / "README.md", edit_readme, force=args.force))

    template_root = edit_root / "_论文项目模板"
    results += mkdirs(template_root / rel for rel in EDIT_TEMPLATE_DIRS)
    if args.paper_project_name:
        results += mkdirs(edit_root / args.paper_project_name / rel for rel in EDIT_TEMPLATE_DIRS)

    if args.write_codex_config:
        codex_home = Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()
        results.append(write_text(codex_home / "mentor" / "config.json", config_json(project_root, lit_vault_root, edit_root), force=True))

    print("\n".join(results))
    print("\nMentor initialized.")
    print(f"PROJECT_ROOT={project_root}")
    print(f"LIT_VAULT_ROOT={lit_vault_root}")
    print(f"EDIT_ROOT={edit_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
