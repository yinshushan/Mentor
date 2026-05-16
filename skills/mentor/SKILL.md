---
name: mentor
description: "Initialize or reproduce the Mentor Codex system: a sociology literature knowledge base, Obsidian-first workflow, paper revision workspace, AGENTS.md project instructions, templates, and companion reading skill configuration. Use when the user asks to install, import, bootstrap, reproduce, initialize, or set up Mentor, a sociology research assistant, an academic writing mentor, a literature vault, or a Codex reproduction package."
---

# Mentor

Mentor is a portable Codex setup workflow for sociology literature reading, Obsidian knowledge-base construction, and paper revision.

Current version: v2.0.0, with full-paper close reading mode for the `$du-wen-xian` literature-reading skill.

## What This Skill Does

Use this skill to:
- create a project-level `AGENTS.md`
- create a project-level `README_workflow.md`
- create an Obsidian-first literature vault structure
- create note templates, indexes, and navigation files
- create the v2.0 full-paper close reading rule note in the workflow directory
- create a separate paper-revision workspace
- write a reusable Mentor config that `$du-wen-xian` can read later

## Required Inputs

Before writing files, resolve these three paths:
- `PROJECT_ROOT`: where the Codex project instructions should live
- `LIT_VAULT_ROOT`: where the Obsidian literature vault should live
- `EDIT_ROOT`: where paper-revision workspaces should live

If the user gives all three paths, proceed. If any are missing, ask for only the missing values.

Suggested portable defaults, only if the user asks you to choose:
- `PROJECT_ROOT`: `~/Documents/Mentor`
- `LIT_VAULT_ROOT`: `~/Documents/Obsidian/社会学文献库`
- `EDIT_ROOT`: `~/Documents/Obsidian/改论文`

## Initialization Workflow

1. Confirm the three paths and expand `~`.
2. Run the bundled bootstrap script:

```bash
python3 <skill_dir>/scripts/bootstrap_mentor.py \
  --project-root "<PROJECT_ROOT>" \
  --lit-vault-root "<LIT_VAULT_ROOT>" \
  --edit-root "<EDIT_ROOT>" \
  --write-codex-config
```

3. Report the created locations and the next prompt the user can run:

```text
Use $du-wen-xian to process my literature folder.
```

## Output Boundaries

- Literature-reading artifacts belong in `LIT_VAULT_ROOT`.
- Paper drafts, revision reports, reviewer-response tables, and submission materials belong in `EDIT_ROOT`.
- Do not mix paper-revision execution files into the literature vault.
- Do not fabricate claims about unread papers.
- Keep author claims, text-based inference, and your evaluation visibly separate.
- Do not summarize a paper from abstract, introduction, or metadata alone; use `$du-wen-xian` full-paper close reading mode for literature notes.

## Reference

For the full reproduction manual, read `references/reproduction_manual.md` only when the user asks for the detailed manual or wants to understand the system design.
