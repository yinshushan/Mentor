# Mentor

Mentor 是一个面向社会学与人文学术研究的开源 Codex 插件。它把 Codex 配置成一个可复用的研究助理，用来建立 Obsidian 文献知识库、批量精读论文、生成结构化研究笔记，并辅助论文修改。

当前版本：v2.0.0

## 这个插件是做什么的

Mentor 不是一个普通的摘要工具，而是一套“Codex + Obsidian”的社会学研究工作流。它适合需要长期阅读文献、整理概念、比较理论、积累研究材料和修改论文的人使用。

它包含两个主要技能：

- `$mentor`：初始化项目规则、Obsidian 文献知识库、笔记模板、索引文件和论文修改工作区。
- `$du-wen-xian`：批量读取一个文献文件夹，把论文整理成可复用的 Obsidian 笔记、概念卡、比较笔记和索引。

它可以帮助你完成：

- 建立社会学文献知识库。
- 批量处理 PDF 文献。
- 为每篇论文生成结构化单篇笔记。
- 提取核心概念、理论传统、方法、材料和论证。
- 比较多篇文献之间的理论、方法和证据差异。
- 生成概念卡、研究空白 memo 和文献综述材料。
- 把正式阅读成果写入 Obsidian，而不是只停留在聊天记录里。
- 为论文修改建立独立工作区，避免文献笔记和改稿材料混在一起。

项目还包含 `.codex-plugin/plugin.json`，可用于支持 Codex 插件导入的环境。

## v2.0 更新：全文精读模式

Mentor v2.0 在原有“读文献 1.0”基础上，新增“全文精读模式（full-paper close reading mode）”。这次更新主要解决一个问题：读文献流程不能只抓取 abstract、introduction、metadata 或 findings 的表层信息，然后把它们改写成“全文总结”。

v2.0 明确禁止：

- 只根据摘要总结全文。
- abstract 改写。
- introduction 改写。
- 跳过正文。
- 假装已经读完整篇文章。
- 用“几点发现”替代真正的精读。
- 用泛化语言代替具体材料分析。

新的全文精读模式要求：

- 先扫描全文结构，识别理论核心、经验核心和真正的论证推进部分。
- 再逐节阅读正文，分析每一节的功能、核心观点和与上一节的关系。
- 重点阅读田野材料、访谈片段、案例叙事、discussion 和理论分析部分。
- 主动识别重复出现的概念、情感、关系结构和叙事模式。
- 每个重要判断都说明正文依据。
- 长文采用“分段递进式精读”，而不是退化成摘要模式。
- PDF 解析不完整时，必须说明哪些部分读取成功、哪些部分可能缺失。

## 如何使用

安装或导入 Mentor 后，先运行 `$mentor` 初始化研究系统：

```text
Use $mentor to initialize my sociology literature system.
PROJECT_ROOT: ~/Documents/Mentor
LIT_VAULT_ROOT: ~/Documents/Obsidian/社会学文献库
EDIT_ROOT: ~/Documents/Obsidian/改论文
```

然后用 `$du-wen-xian` 处理文献文件夹：

```text
Use $du-wen-xian to process my literature folder.
```

技能会先询问：

```text
文献所在文件夹的位置在哪？
```

v2.0 的单篇笔记会比 v1.0 更强调正文结构、逐节分析、材料依据和阅读边界。输出中应包含全文结构地图、逐节精读记录、重复主题、正文证据和 PDF 解析/缺失说明。

## 为什么对质性研究特别重要

质性研究论文的核心论证往往不在摘要里，而隐藏在田野叙事、访谈片段、案例展开、作者解释经验材料的方式，以及 discussion 中对概念和理论的回收之中。

如果只读 abstract 或 introduction，很容易错过作者真正的经验发现、关系结构、情感线索和理论推进。全文精读模式的目标不是“快速总结论文”，而是帮助读者真正进入作者的田野、经验与论证过程，完成社会学意义上的精读。

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

## Privacy Note

This package installs instructions, templates, and local setup scripts. It does not upload a user's papers or notes anywhere by itself.

## 版本迭代记录

| 版本 | 发布时间 | 主要内容 |
| --- | --- | --- |
| v2.0.0 | 2026-05-16 | 新增全文精读模式；强制扫描全文结构、逐节阅读正文、标注正文证据；增加长文分段递进式精读和 PDF 解析缺失提示；强化对质性研究中田野材料、访谈片段、案例叙事和理论分析的阅读。 |
| v1.0.0 | 2026-05-07 | 初始开源版本；提供 `$mentor` 初始化技能和 `$du-wen-xian` 读文献技能；支持 Obsidian 文献知识库、模板、索引、批次阅读和论文修改工作区。 |
