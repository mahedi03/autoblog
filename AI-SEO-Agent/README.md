# SEOForge — AI SEO Content Agent System

## Overview

SEOForge is a multi-agent AI system designed for professional-grade, automated SEO content creation. Instead of a single monolithic prompt, it uses **5 specialized agents**, each an expert in their domain, orchestrated through defined workflows to produce consistently high-quality, Google-compliant content.

## Architecture

```
User Input (Keyword)
       │
       ▼
┌─────────────────────┐
│   Research Agent     │  ← SERP analysis, entities, NLP keywords
│   (Phase 1-3)       │     content gaps, search intent
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   Outline Agent      │  ← Heading hierarchy, FAQ plan, CTA
│   (Phase 4-5)        │     topical map analysis, internal links
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   Writing Agent      │  ← Full article, semantic SEO, entity SEO
│   (Phase 6)          │     human tone, rich formatting
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   SEO Review Agent   │  ← Audit, readability, EEAT, scoring
│   (Phase 7)          │     feedback loop → Writing Agent
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   Publisher Agent     │  ← Schema, metadata, OG tags, CMS push
│   (Phase 8-9)        │     slug, featured image, JSON-LD
└─────────────────────┘
```

## Directory Structure

```
AI-SEO-Agent/
│
├── SYSTEM.md                    # Master system prompt — global rules
├── README.md                    # This file
│
├── AGENTS/                      # Specialized agent definitions
│   ├── research-agent.md        # SERP + keyword + entity research
│   ├── outline-agent.md         # Content outline generation
│   ├── writing-agent.md         # Article writing
│   ├── seo-review-agent.md      # SEO audit + quality check
│   └── publisher-agent.md       # Publishing + metadata
│
├── PROMPTS/                     # Reusable prompt templates
│   ├── keyword-analysis.md      # Keyword research
│   ├── content-gap.md           # Gap analysis
│   ├── outline.md               # Outline generation
│   ├── article.md               # Article writing
│   ├── faq.md                   # FAQ generation
│   ├── schema.md                # JSON-LD schema
│   ├── metadata.md              # Meta titles/descriptions
│   └── internal-linking.md      # Internal link suggestions
│
├── WORKFLOWS/                   # End-to-end pipelines
│   ├── standard-workflow.md     # Standard blog post
│   ├── local-seo.md             # Local business pages
│   ├── ecommerce.md             # Product/category SEO
│   └── saas.md                  # SaaS content
│
└── CONFIG/                      # Shared configuration
    ├── writing-rules.md         # Style + formatting
    ├── seo-rules.md             # On-page SEO rules
    ├── eeat.md                  # E-E-A-T framework
    ├── helpful-content.md       # Google HCU alignment
    └── topical-map.md           # Topical map rules
```

## How It Works

### 1. Input

Provide the system with:
- **Primary keyword** (required)
- **Secondary keywords** (optional)
- **Target country/language** (default: US/English)
- **Website URL** (for internal linking)
- **Topical map** (`topical-map.json` — for topical authority)
- **Brand voice settings** (from AI Memory)

### 2. Pipeline Execution

The system executes 9 phases sequentially:

| Phase | Agent | Action |
|-------|-------|--------|
| 1 | Research | Keyword analysis — intent, difficulty, entities, NLP/LSI |
| 2 | Research | SERP analysis — top 10 competitor breakdown |
| 3 | Research | Content gap — missing topics, questions, entities |
| 4 | Outline | Outline generation — H1→H4, FAQ, CTA, sections |
| 5 | Outline | Topical map analysis — internal links, anchor text |
| 6 | Writer | Article writing — full content with semantic SEO |
| 7 | Review | SEO audit — score, readability, EEAT, improvements |
| 8 | Publisher | Metadata — schema, OG, slug, featured image |
| 9 | Publisher | CMS publishing — API payload, publish to platform |

### 3. Quality Loop

If the SEO Review Agent scores the article below 80/100, it sends specific feedback to the Writing Agent for revision. This loop continues until the score meets the threshold.

### 4. Output

The final output includes:
- Complete article (Markdown + HTML)
- SEO metadata (meta title, description, slug)
- JSON-LD schemas (Article, FAQ, Author, Breadcrumb)
- Open Graph + Twitter Card tags
- Internal link map
- Featured image generation prompt
- CMS-ready API payload
- SEO score report

## LLM Provider Support

The system is designed to work with multiple LLM providers:

| Provider | Models | Best For |
|----------|--------|----------|
| OpenAI | GPT-4o, GPT-4o-mini | Primary writing, research |
| Google | Gemini 2.0 Flash, Gemini 2.0 Pro | Fast research, long context |
| Anthropic | Claude Opus 4, Claude Sonnet 4 | Deep analysis, review |
| Perplexity | Sonar, Sonar Pro | Real-time research |

Each agent can be configured to use a different provider based on the task requirements.

## Configuration

### Brand Voice (AI Memory)

The system maintains persistent memory of:
- Brand voice and tone
- Target audience
- Products/services
- Forbidden words
- Internal link rules
- Custom SEO rules
- Author personas

### Workflows

Choose the right workflow for your content type:
- **Standard** — Blog posts, guides, how-tos
- **Local SEO** — Location pages, service area pages
- **E-commerce** — Product pages, category pages, buying guides
- **SaaS** — Comparison pages, alternative pages, landing pages

## Integration

This prompt system is designed to be integrated into the SEOForge web application (Next.js 15) where:
1. The orchestrator reads these markdown files as system prompts
2. Each agent is instantiated with its specific prompt + CONFIG rules
3. The workflow engine chains agents in the correct sequence
4. Results are stored in PostgreSQL and presented in the admin dashboard
5. Publishing is handled via CMS API integrations

## Quality Standards

Every article produced by this system must meet:
- **SEO Score**: ≥ 80/100
- **Readability**: Flesch-Kincaid Grade 6-8
- **Keyword Density**: 0.5-3.0%
- **Unique Content**: 100% original (no competitor copying)
- **E-E-A-T Compliance**: Expert-level, trustworthy content
- **Helpful Content**: Aligns with Google's Helpful Content System
- **Schema Coverage**: Article + FAQ + Author + Breadcrumb
- **Internal Links**: ≥ 3 contextual links from topical map
- **External Citations**: ≥ 2 authoritative sources
