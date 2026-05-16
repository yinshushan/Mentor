# Mentor

Mentor is a portable Codex package for building a sociology literature system and paper-revision workspace.

Current version: v2.0.0

It includes:
- `$mentor`: initializes the project instructions, Obsidian literature vault, templates, indexes, and revision workspace
- `$du-wen-xian`: batch-reads a folder of papers into reusable Obsidian notes with full-paper close reading mode
- `.codex-plugin/plugin.json`: plugin metadata for Codex environments that support plugin import

## v2.0 更新：全文精读模式

Mentor v2.0 adds a mandatory full-paper close reading mode to the original `读文献 1.0` workflow. This update exists because the 1.0 reading flow could degrade into abstract-level or introduction-level summaries when PDFs were long, partially parsed, or difficult to process.

The new mode forbids summarizing a paper only from the abstract, introduction, metadata, or surface-level findings. It requires the reader to scan the full article structure first, read the body section by section, prioritize fieldwork materials, interview fragments, case narratives, discussion, and theoretical analysis, and then generate the final summary only after body evidence has been gathered.

To use it, run the normal reading skill:

```text
Use $du-wen-xian to process my literature folder.
```

The output now includes a full-text structure map, a section-by-section close reading log, repeated concepts/emotions/relationship structures/narrative patterns, body evidence for major judgments, and a clear PDF parsing or missing-section note. If only the abstract, introduction, or metadata was read, the skill must say that the body text has not been sufficiently read.

This is especially useful for qualitative sociology, where the real argument often appears in fieldwork passages, interview excerpts, case narratives, and late-stage theoretical discussion rather than in the abstract.

## One-Click Codex Import

If your Codex supports importing a plugin from a GitHub repository, import:

```text
https://github.com/yinshushan/Mentor
```

Then restart Codex and run:

```text
Use $mentor to initialize my sociology literature system.
```

## Skill Installer Fallback

If your Codex uses the built-in skill installer, ask Codex:

```text
Use $skill-installer to install skills from https://github.com/yinshushan/Mentor/tree/main/skills/mentor and https://github.com/yinshushan/Mentor/tree/main/skills/du-wen-xian.
```

Or run the installer script directly:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo yinshushan/Mentor \
  --path skills/mentor skills/du-wen-xian \
  --method git
```

Restart Codex after installation.

## First Setup Prompt

After import, use:

```text
Use $mentor to initialize my sociology literature system.
PROJECT_ROOT: ~/Documents/Mentor
LIT_VAULT_ROOT: ~/Documents/Obsidian/社会学文献库
EDIT_ROOT: ~/Documents/Obsidian/改论文
```

## Reading Papers

After setup, use:

```text
Use $du-wen-xian to process my literature folder.
```

The skill will first ask:

```text
文献所在文件夹的位置在哪？
```

## Privacy Note

This package installs instructions, templates, and local setup scripts. It does not upload a user's papers or notes anywhere by itself.
