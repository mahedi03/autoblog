# Content Gap Analysis Prompt — SEOForge

> Prompt Type: Research
> Used By: Research Agent
> Phase: 3 — Content Gap Identification

---

## System Context

You are analyzing top-ranking content to find gaps and opportunities that will make new content superior to everything currently ranking.

---

## Prompt Template

```
TASK: Identify content gaps by analyzing what the top 10 Google results for this keyword are MISSING.

PRIMARY KEYWORD: {{primary_keyword}}
SEARCH INTENT: {{search_intent}}

TOP 10 COMPETITOR ANALYSIS DATA:
{{serp_analysis_data}}

ENTITIES IDENTIFIED:
{{entities}}

PAA QUESTIONS:
{{paa_questions}}

ANALYZE AND IDENTIFY:

1. MISSING QUESTIONS (5-10)
Questions that searchers likely have but NO top result adequately answers.
For each: question, source (PAA/Reddit/forum/analysis), priority, why it matters.

2. MISSING ENTITIES (5-8)
Important entities related to this topic that competitors don't mention.
For each: entity name, type, why to include, priority.

3. MISSING COMPARISONS (2-5)
Comparisons that would help the reader make decisions.
For each: what to compare, recommended format (table/prose/list), why important.

4. MISSING SECTIONS (3-7)
Subtopics that competitors cover poorly or not at all.
For each: topic, suggested heading, coverage in competitors (X/10), why to add, estimated words.

5. MISSING FAQs (5-8)
FAQ questions from PAA that no competitor addresses.
For each: question, answer direction, source.

6. MISSING STATISTICS (3-5)
Data points that would strengthen the content.
For each: stat type needed, context for usage, potential sources.

7. MISSING EXAMPLES (2-4)
Real-world examples, case studies, or walkthroughs that competitors lack.
For each: example type, what it should demonstrate, where to place.

8. MISSING MEDIA (2-3)
Visual elements that would enhance understanding.
For each: media type (table/chart/diagram/infographic), what it shows, placement.

RULES:
- Only flag genuinely missing content, not minor variations
- Prioritize gaps that align with search intent
- Focus on gaps that add unique value (not just more words)
- Missing sections should be substantial (not one-sentence topics)
- Missing questions should be questions real users would ask
- Statistics should be from findable, credible sources

OUTPUT FORMAT: JSON matching the content_gaps schema from SYSTEM.md Section 12.1.
```

---

## Variable Reference

| Variable | Description | Source |
|----------|-------------|--------|
| `{{primary_keyword}}` | Main keyword | User input |
| `{{search_intent}}` | Classified intent | Phase 1 output |
| `{{serp_analysis_data}}` | Top 10 analysis | Phase 2 output |
| `{{entities}}` | Identified entities | Phase 1 output |
| `{{paa_questions}}` | PAA questions | Phase 1 output |

---

## Quality Criteria

A good content gap analysis:
- Identifies gaps that are genuinely absent from ALL top results
- Prioritizes gaps by impact on ranking potential
- Provides actionable suggestions (not vague observations)
- Connects gaps to search intent fulfillment
- Includes enough detail for the Outline Agent to act on
