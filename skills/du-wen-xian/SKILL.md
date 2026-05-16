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

## 全文精读强制规则 / Full-Paper Close Reading Mode

【全文精读强制规则】

我发现你在阅读文献时，经常只抓取：
- abstract
- introduction
- metadata
- findings 的表层总结

然后生成回答。

这是禁止的。

从现在开始，你必须执行“全文精读模式（full-paper close reading mode）”。

【禁止行为】

禁止：
- 只根据摘要总结全文
- abstract 改写
- introduction 改写
- 用“几点发现”替代精读
- 跳过正文
- 假装已经读完整篇文章
- 只提取结论
- 用泛化语言代替具体分析

如果你的分析主要来自：
- abstract
- introduction
- metadata

你必须明确说明：

“当前分析主要来自摘要或前言，正文尚未充分读取。”

禁止伪装成已经完成全文精读。

【强制全文阅读流程】

Step 1：
先扫描全文结构。

识别：
- 文章有几个部分
- 每部分的功能
- 哪部分是理论核心
- 哪部分是经验核心
- 哪部分是真正的论证推进

不要立刻总结。

Step 2：
逐节阅读正文。

必须逐节分析：
- 本节核心观点
- 与上一节的逻辑关系
- 作者如何推进论证
- 作者如何组织材料
- 作者如何解释经验

不要跳读。

Step 3：
重点阅读：
- 田野材料
- 访谈片段
- 案例叙事
- discussion
- 理论分析部分

因为质性研究真正重要的内容，往往隐藏在正文深处，而不是摘要。

Step 4：
识别全文中的重复主题。

请主动寻找：
- 重复出现的概念
- 重复出现的情感
- 重复出现的关系结构
- 重复出现的叙事模式

这些通常才是作者真正的核心论点。

Step 5：
最后才能生成总结。

总结必须建立在“已经阅读正文”的基础上。

【正文证据要求】

每一个重要判断必须说明来自：
- 哪一部分正文
- 哪一种材料
- 哪一个案例
- 哪一段论述

不要生成没有依据的判断。

【长文处理规则】

如果文章较长，不要偷懒只看前几页。

请采用“分段递进式精读”：

1. 先建立全文结构地图
2. 再逐节阅读
3. 再汇总概念
4. 再识别隐藏论证
5. 最后整体分析

不要因为文章长而退化为摘要模式。

【PDF 特别规则】

如果 PDF 解析失败，请明确说明：
- 哪部分读取成功
- 哪部分可能缺失
- 是否只读取到了摘要
- 是否正文未完整解析

不要假装已经完整阅读。

【真正目标】

你的目标不是“快速总结论文”。

而是“真正进入作者的田野、经验与论证过程，完成社会学意义上的精读”。

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
4. For each paper, run full-paper close reading mode before summarizing: scan the article structure, read body sections progressively, prioritize fieldwork/interview/case/discussion/theory sections, and collect body evidence for each major judgment.
5. Mark partial reads, OCR gaps, failed PDF parsing, or missing sections honestly.
6. Write one note per paper under `02_单篇笔记/batch_xx/`.
7. Create concept cards under `03_概念卡/` when concepts recur across body evidence.
8. Create comparison notes under `04_模板与比较笔记/` after 3 to 6 papers share a theme.
9. Update the navigation and index files after each batch.

## Single Paper Note Sections

Each note should include:
1. bibliographic note
2. full-text structure map
3. section-by-section close reading log
4. 150-300 word summary
5. core argument
6. main concepts
7. repeated concepts, emotions, relationship structures, and narrative patterns
8. theoretical tradition
9. methods/data
10. key findings
11. body evidence for major judgments
12. strengths
13. weaknesses
14. useful quotations or paraphrasable points
15. relationship to the user's research
16. PDF parsing and missing-section note
17. tags

## Minimum Successful Run

A successful pilot run should leave:
- one updated paper inventory
- one navigation page
- one workflow note
- one pilot batch folder
- at least 5 single-paper notes
- full-paper close reading status and body evidence boundaries in each note
- at least one concept card or comparison note
