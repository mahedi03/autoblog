# Standard Workflow — SEOForge

> Workflow: Standard Blog Post Pipeline
> Phases: 1-9 (Full Pipeline)
> Content Types: Blog posts, guides, how-to articles, listicles, explanations

---

## Overview

The standard workflow is the default pipeline for creating SEO-optimized blog content. It executes all 9 phases sequentially with a quality gate feedback loop between the Writing Agent and SEO Review Agent.

---

## Pipeline Flow

```
Phase 1: Keyword Research (Research Agent)
    │
    ├── Search intent classification
    ├── Keyword difficulty assessment
    ├── Entity extraction
    ├── NLP/semantic/LSI keyword discovery
    ├── PAA questions extraction
    └── Content angle recommendation
         │
         ▼
Phase 2: SERP Analysis (Research Agent)
    │
    ├── Top 10 competitor analysis
    ├── SERP feature identification
    ├── Competitive summary
    └── Opportunity assessment
         │
         ▼
Phase 3: Content Gap Analysis (Research Agent)
    │
    ├── Missing questions, entities, sections
    ├── Missing comparisons, FAQs, statistics
    ├── Missing examples, media types
    └── Strategic recommendations
         │
         ▼
Phase 4: Outline Generation (Outline Agent)
    │
    ├── Intent-driven heading hierarchy
    ├── Section planning with content notes
    ├── FAQ section planning
    ├── CTA placement strategy
    ├── EEAT signal planning
    └── Word count distribution
         │
         ▼
Phase 5: Topical Map Analysis (Outline Agent)
    │
    ├── Position in topical hierarchy
    ├── Internal link recommendations
    ├── Anchor text suggestions
    └── Topical map gap identification
         │
         ▼
Phase 6: Article Writing (Writing Agent)
    │
    ├── Full article in Markdown + HTML
    ├── Keyword + entity integration
    ├── Internal + external link placement
    ├── Expert tips, tables, lists, examples
    ├── FAQ section with schema
    ├── CTA placement
    └── Image placeholder specifications
         │
         ▼
Phase 7: SEO Review (SEO Review Agent)
    │
    ├── SEO Technical Audit (40 points)
    ├── Content Quality Audit (30 points)
    ├── EEAT Compliance (15 points)
    ├── Helpful Content Compliance (15 points)
    ├── Forbidden phrase detection
    ├── AI detection assessment
    │
    ├── Score ≥ 80 ──────────────────────▼
    │                              Phase 8
    └── Score < 80 ────┐
                       │
                       ▼
              Revision Instructions
                       │
                       ▼
              Writing Agent (Revision)
                       │
                       ▼
              SEO Review Agent (Re-check)
                       │
              (Max 3 revision cycles)
                       │
                       ▼
Phase 8: Metadata & Schema (Publisher Agent)
    │
    ├── URL slug generation
    ├── Meta title + description
    ├── JSON-LD schemas (Article, FAQ, Breadcrumb, Author)
    ├── Open Graph tags
    ├── Twitter Card tags
    ├── Canonical URL
    ├── Featured image prompt
    └── CMS payload compilation
         │
         ▼
Phase 9: CMS Publishing (Publisher Agent)
    │
    ├── CMS-specific payload formatting
    ├── API call to CMS (WordPress/Webflow/Webhook)
    ├── Image upload (if generated)
    ├── Publishing confirmation
    └── Post-publish logging
```

---

## Phase Timing

| Phase | Agent | Estimated Time | Token Budget |
|-------|-------|---------------|--------------|
| 1 | Research | 15-30s | 4,000-6,000 |
| 2 | Research | 15-30s | 4,000-8,000 |
| 3 | Research | 10-20s | 2,000-4,000 |
| 4 | Outline | 15-30s | 3,000-6,000 |
| 5 | Outline | 5-10s | 1,000-2,000 |
| 6 | Writing | 45-90s | 8,000-16,000 |
| 7 | Review | 15-30s | 3,000-6,000 |
| 8 | Publisher | 10-20s | 2,000-4,000 |
| 9 | Publisher | 5-10s | 500-1,000 |
| **Total** | | **2-5 min** | **25,000-53,000** |

---

## Quality Gates

### Gate 1: Research Completeness (after Phase 3)

```
✓ Search intent classified with evidence
✓ ≥ 20 NLP keywords identified
✓ ≥ 8 PAA questions extracted
✓ ≥ 5 content gaps identified
✓ ≥ 3 entities per category
✓ Content angle recommendation provided
✓ All 10 SERP results analyzed
```

### Gate 2: Outline Completeness (after Phase 5)

```
✓ H1 contains primary keyword
✓ ≥ 4 H2 sections
✓ ≥ 3 H3 sections
✓ FAQ with ≥ 5 questions
✓ CTA plan defined
✓ ≥ 3 internal link opportunities
✓ EEAT plan for each section
✓ Word count targets sum to ≥ 1500
```

### Gate 3: Quality Score (after Phase 7)

```
✓ SEO Score ≥ 80/100
✓ Readability ≤ Grade 8
✓ EEAT Score ≥ 70/100
✓ Helpful Content Score ≥ 75/100
✓ No forbidden phrases
✓ No keyword stuffing
✓ All required schema present
```

### Gate 4: Publishing Readiness (after Phase 8)

```
✓ Meta title 50-60 chars
✓ Meta description 120-160 chars
✓ Valid JSON-LD schemas
✓ OG tags complete
✓ Twitter Card complete
✓ CMS payload formatted
```

---

## Error Handling

| Error | Phase | Action |
|-------|-------|--------|
| API timeout | Any | Retry with backoff, max 3 attempts |
| Research incomplete | 1-3 | Proceed with available data, flag gaps |
| Outline fails validation | 4-5 | Re-generate with additional instructions |
| Article fails quality gate | 7 | Send revision notes to Writing Agent |
| 3 revision cycles exceeded | 7 | Publish as draft, notify user for manual review |
| Schema validation fails | 8 | Re-generate schemas with stricter instructions |
| CMS API error | 9 | Save as draft locally, retry publishing |
| Image generation fails | 8 | Publish without image, queue for later |

---

## Standard Configuration

```json
{
  "workflow": "standard",
  "settings": {
    "min_word_count": 1500,
    "max_word_count": 5000,
    "min_seo_score": 80,
    "max_revisions": 3,
    "include_faq": true,
    "min_faq_questions": 5,
    "include_schema": true,
    "include_og_tags": true,
    "include_twitter_card": true,
    "auto_publish": false,
    "default_status": "draft",
    "generate_featured_image": true,
    "llm_provider": {
      "research": "perplexity",
      "outline": "openai",
      "writing": "anthropic",
      "review": "openai",
      "publishing": "openai"
    }
  }
}
```
