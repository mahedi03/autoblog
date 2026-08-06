# Metadata Generation Prompt — SEOForge

> Prompt Type: Technical SEO
> Used By: Publisher Agent
> Phase: 8 — Metadata Generation

---

## Prompt Template

```
TASK: Generate optimized metadata for SEO and social sharing.

ARTICLE TITLE (H1): {{article_title}}
PRIMARY KEYWORD: {{primary_keyword}}
ARTICLE SUMMARY: {{article_summary}}
SITE/BRAND NAME: {{site_name}}
SITE URL: {{site_url}}
AUTHOR: {{author_name}}
CATEGORY: {{category}}

GENERATE:

1. META TITLE (50-60 characters)
Rules:
- Front-load primary keyword (within first 30 chars)
- Include power word or modifier (Complete, Ultimate, Proven, Expert, Best)
- Add year if time-sensitive
- Append brand name with | separator (if fits within limit)
- Must be different from H1 (variation, not duplicate)
- Must be compelling for SERP click-through

Generate 3 options ranked by quality.

2. META DESCRIPTION (120-160 characters)
Rules:
- Include primary keyword naturally
- Include a benefit or value proposition
- Include a soft CTA (Learn, Discover, Find out, Get, Compare)
- Front-load important information
- No quotes (truncated in SERP)
- Match the search intent

Generate 3 options ranked by quality.

3. URL SLUG
Rules:
- Lowercase, hyphens only
- Include primary keyword
- Remove stop words (a, an, the, is, of, in, for, to, with, at, by, on)
- Under 60 characters
- Readable and descriptive
- No year unless URL structure supports it

Generate the optimal slug.

4. OPEN GRAPH TAGS
Generate all required OG properties:
- og:title (can be slightly different from meta title, max 60 chars)
- og:description (can be different from meta desc, max 200 chars)
- og:type (article)
- og:url (canonical URL)
- og:image (featured image URL placeholder)
- og:image:width (1200)
- og:image:height (630)
- og:image:alt (descriptive alt text)
- og:site_name
- og:locale
- article:published_time
- article:modified_time
- article:author
- article:section
- article:tag (array)

5. TWITTER CARD TAGS
Generate all required Twitter properties:
- twitter:card (summary_large_image)
- twitter:title (max 70 chars)
- twitter:description (max 200 chars)
- twitter:image
- twitter:image:alt
- twitter:site (@handle if configured)

6. CANONICAL URL
- Full absolute URL
- Lowercase
- Consistent trailing slash behavior
- Self-referencing

7. ADDITIONAL META
- robots: "index, follow"
- language meta tag
- viewport (for responsive)

OUTPUT FORMAT:
{
  "meta_title": {
    "primary": "string",
    "alternatives": ["string", "string"],
    "character_count": number
  },
  "meta_description": {
    "primary": "string",
    "alternatives": ["string", "string"],
    "character_count": number
  },
  "slug": "string",
  "canonical_url": "string",
  "open_graph": { ... all OG tags ... },
  "twitter_card": { ... all Twitter tags ... },
  "additional_meta": { ... robots, language, etc. ... },
  "html_output": "string — all meta tags as HTML"
}
```

---

## Variable Reference

| Variable | Description | Source |
|----------|-------------|--------|
| `{{article_title}}` | H1 heading | Writing Agent |
| `{{primary_keyword}}` | Main keyword | User input |
| `{{article_summary}}` | Brief content summary | Writing Agent |
| `{{site_name}}` | Brand/site name | User configuration |
| `{{site_url}}` | Website base URL | User configuration |
| `{{author_name}}` | Author name | AI Memory |
| `{{category}}` | Content category | Outline Agent |
