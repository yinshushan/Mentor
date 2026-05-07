# Mentor

Mentor is a portable Codex package for building a sociology literature system and paper-revision workspace.

It includes:
- `$mentor`: initializes the project instructions, Obsidian literature vault, templates, indexes, and revision workspace
- `$du-wen-xian`: batch-reads a folder of papers into reusable Obsidian notes
- `.codex-plugin/plugin.json`: plugin metadata for Codex environments that support plugin import

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
