# Internal Linking Prompt — SEOForge

> Prompt Type: Strategy
> Used By: Outline Agent
> Phase: 5 — Internal Link Planning

---

## Prompt Template

```
TASK: Analyze the topical map and article context to generate strategic internal link recommendations.

CURRENT ARTICLE:
- Title: {{article_title}}
- Primary Keyword: {{primary_keyword}}
- Category: {{category}}
- Search Intent: {{search_intent}}

TOPICAL MAP:
{{topical_map}}

PUBLISHED ARTICLES DATABASE:
{{published_articles}}

ANALYSIS REQUIRED:

1. TOPICAL POSITION ANALYSIS
Identify:
- Where this article sits in the topical hierarchy
- Parent page (pillar/hub it belongs to)
- Sibling pages (same cluster level)
- Child pages (deeper subtopics)
- Supporting pages (related but different cluster)

2. INTERNAL LINK RECOMMENDATIONS
For each recommended link, provide:

{
  "target_title": "string — title of the page to link to",
  "target_url": "string — URL of the target page",
  "anchor_text": {
    "primary": "string — best anchor text (3-7 words)",
    "alternatives": ["string — backup options"]
  },
  "placement": {
    "section": "string — which outline section to place in",
    "position": "intro | body | faq | conclusion",
    "context_sentence": "string — example sentence containing the link"
  },
  "priority": "high | medium | low",
  "link_type": "pillar | sibling | child | supporting | reference",
  "reasoning": "string — why this link adds value"
}

3. LINK DISTRIBUTION RULES
- Minimum 3, maximum 8 internal links
- First link within first 300 words
- Maximum 1 link per 200 words
- Links distributed across sections (not clustered)
- Pillar page link is mandatory (highest priority)
- At least 2 sibling/child links

4. ANCHOR TEXT GUIDELINES
- Descriptive, keyword-rich (3-7 words)
- Contains target page's primary keyword when natural
- Reads naturally in context
- Never "click here," "read more," or "learn more"
- Never the bare URL
- Varied (don't use the same anchor text for different links)

5. TOPICAL MAP GAPS
Identify missing pages that should exist:
- Topics that would strengthen the topical cluster
- Questions that deserve their own page
- Comparison/alternative pages that are missing
- Supporting content needed for authority

OUTPUT FORMAT:
{
  "topical_position": { ... },
  "internal_links": [ ... array of link recommendations ... ],
  "link_distribution": {
    "total": number,
    "by_section": { "intro": number, "body": number, "faq": number, "conclusion": number }
  },
  "topical_gaps": [ ... missing pages that should be created ... ],
  "pillar_link": {
    "target_url": "string",
    "anchor_text": "string",
    "placement": "string"
  }
}
```

---

## Variable Reference

| Variable | Description | Source |
|----------|-------------|--------|
| `{{article_title}}` | Current article title | Outline Agent |
| `{{primary_keyword}}` | Main keyword | User input |
| `{{category}}` | Content category | Outline Agent |
| `{{search_intent}}` | Intent classification | Research Agent |
| `{{topical_map}}` | Full topical map JSON | User configuration |
| `{{published_articles}}` | List of published articles (title, URL, keyword) | Database |
