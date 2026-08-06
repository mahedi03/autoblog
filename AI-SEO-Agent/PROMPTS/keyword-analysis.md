# Keyword Analysis Prompt — SEOForge

> Prompt Type: Research
> Used By: Research Agent
> Phase: 1 — Keyword Research

---

## System Context

You are performing deep keyword analysis for SEO content creation. Your goal is to extract maximum intelligence from a single keyword to inform content strategy.

---

## Prompt Template

```
TASK: Perform comprehensive keyword analysis for SEO content creation.

PRIMARY KEYWORD: {{primary_keyword}}
SECONDARY KEYWORDS: {{secondary_keywords}}
TARGET COUNTRY: {{country}}
TARGET LANGUAGE: {{language}}
WEBSITE NICHE: {{niche}}

ANALYSIS REQUIRED:

1. SEARCH INTENT CLASSIFICATION
Classify the search intent as one of:
- Informational (user wants to learn)
- Navigational (user wants to find a specific page)
- Transactional (user wants to buy/act)
- Commercial Investigation (user is comparing before buying)

Provide:
- Intent type
- Confidence level (high/medium/low)
- Evidence supporting the classification
- Secondary intent (if mixed)

2. KEYWORD DIFFICULTY ASSESSMENT
Evaluate based on:
- Likely domain authority of ranking pages
- Content quality requirements
- SERP feature saturation
- Content freshness requirements
Rate as: easy | medium | hard | very_hard

3. ENTITY EXTRACTION
Identify all relevant entities:
- People (experts, founders, authors)
- Organizations (companies, institutions)
- Products/Services (tools, software)
- Concepts (methodologies, frameworks)
- Places (if location relevant)

For each entity provide: name, type, relevance (high/medium/low), context for inclusion.

4. KEYWORD EXPANSION
Generate:
- 20-30 NLP keywords (terms an NLP model associates with this topic)
- 15-25 Semantic keywords (synonyms, related concepts)
- 10-20 LSI keywords (co-occurring terms)
- 10-15 Related searches (what users also search for)
- 8-15 People Also Ask questions (actual questions users ask)
- 3-5 Trending topics (current trends related to this keyword)

5. CONTENT ANGLE RECOMMENDATION
Based on the analysis, recommend:
- The best content angle to take
- What makes this angle unique vs competitors
- Recommended content format (guide, listicle, comparison, tutorial, etc.)
- Target word count
- Key differentiators to emphasize

OUTPUT FORMAT: JSON matching the keyword_data schema from SYSTEM.md Section 12.1.

IMPORTANT RULES:
- Be specific and actionable, not generic
- NLP keywords should be topic-specific, not generic terms
- PAA questions should be real questions users would search
- Entity relevance must be justified
- Content angle must be differentiated from obvious approaches
```

---

## Variable Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `{{primary_keyword}}` | The main keyword to analyze | Yes | — |
| `{{secondary_keywords}}` | Supporting keywords | No | [] |
| `{{country}}` | Target country (ISO 3166-1) | No | US |
| `{{language}}` | Target language (ISO 639-1) | No | en |
| `{{niche}}` | Website niche/industry | No | General |

---

## Expected Output Quality

- Intent classification with evidence (not just a label)
- At least 20 NLP keywords specific to the topic
- At least 8 genuine PAA questions
- Entities categorized and rated by relevance
- Content angle that isn't the obvious "complete guide" approach
- Actionable keyword lists (not padded with irrelevant terms)

---

## Usage

This prompt is used by the Research Agent as the first step in the research pipeline. The output feeds into SERP analysis and content gap analysis.
