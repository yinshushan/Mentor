---
name: du-wen-xian
description: "Read and organize a sociology or humanities literature folder into an Obsidian-first knowledge base. Use when the user asks to read a literature collection, process a folder of papers, build reusable reading notes, create concept cards, compare papers, maintain indexes, or turn a paper library into a structured research system. Before doing substantial work, always ask: 文献所在文件夹的位置在哪？"
---

# 读文献

## Mandatory First Question

Before batch reading, creating notes, or assuming a source location, ask exactly:

`文献所在文件夹的位置在哪？`

If the user already gave the literature folder path in the same request, do not repeat the question.

## Resolve The Output Vault

After the source folder is known, resolve the Obsidian literature vault root in this order:
1. Use `LIT_VAULT_ROOT` if the user gave it directly.
2. Read `~/.codex/mentor/config.json` or `$CODEX_HOME/mentor/config.json` if present.
3. Read `mentor_config.json` from the current project or a parent directory if present.
4. If still unknown, ask: `Obsidian 文献知识库根目录在哪？`

All formal literature-reading artifacts should go into that vault, not only into chat.

## Core Rules

- Work in small batches by default; pilot batch size is 5 papers unless the user says otherwise.
- Never fabricate conclusions, methods, quotations, or contributions from unread papers.
- Clearly distinguish author claims, text-based inference, and your evaluation.
- Literature reading outputs belong in the literature vault.
- Paper drafts, revision reports, reviewer responses, and submission materials belong in the separate edit workspace, not the literature vault.
- If OCR, metadata, methods, or pages are missing, state the exact missing item.

## Vault Structure

Create or reuse:
- `00_导航/`
- `01_工作流与规范/`
- `02_单篇笔记/`
- `03_概念卡/`
- `04_模板与比较笔记/`
- `06_索引与清单/`

If the user already has a different mature structure, follow it instead of forcing a rebuild.

## Workflow

1. Check the source folder exists and summarize file types/counts.
2. Create or update `06_索引与清单/paper_inventory.csv`.
3. Select a pilot batch of 5 papers, explaining why those papers were chosen.
4. Read enough text to support each note. Mark partial reads honestly.
5. Write one note per paper under `02_单篇笔记/batch_xx/`.
6. Create concept cards under `03_概念卡/` when concepts recur.
7. Create comparison notes under `04_模板与比较笔记/` after 3 to 6 papers share a theme.
8. Update the navigation and index files after each batch.

## Single Paper Note Sections

Each note should include:
1. bibliographic note
2. 150-300 word summary
3. core argument
4. main concepts
5. theoretical tradition
6. methods/data
7. key findings
8. strengths
9. weaknesses
10. useful quotations or paraphrasable points
11. relationship to the user's research
12. tags

## Minimum Successful Run

A successful pilot run should leave:
- one updated paper inventory
- one navigation page
- one workflow note
- one pilot batch folder
- at least 5 single-paper notes
- at least one concept card or comparison note
