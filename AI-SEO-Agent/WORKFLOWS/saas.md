# SaaS Workflow — SEOForge

> Workflow: SaaS Content SEO Pipeline
> Based on: Standard Workflow (with SaaS modifications)
> Content Types: Comparison pages, alternative pages, landing pages, feature pages, integration pages

---

## Overview

The SaaS workflow targets software-as-a-service content strategies. It focuses on bottom-of-funnel commercial keywords, competitor comparison pages, alternative pages, and feature-focused content that drives signups.

---

## Key Differences from Standard Workflow

| Aspect | Standard | SaaS |
|--------|----------|------|
| Keywords | Informational | "[competitor] alternative," "[A] vs [B]," "best [category] software" |
| Intent | Learn | Compare and convert |
| Schema | Article + FAQ | SoftwareApplication + FAQ + Review |
| CTA | Generic | Free trial, demo, signup |
| Content Focus | Education | Differentiation, features, pricing |
| EEAT | General expertise | Product expertise, user testimonials |

---

## SaaS Content Type Templates

### Alternative Page ("[Competitor] Alternatives")

```
H1: [N] Best [Competitor] Alternatives in [Year]
├── Why Look for [Competitor] Alternatives?
│   ├── Common pain points with [Competitor]
│   └── What to look for in an alternative
├── Quick Comparison Table
│   └── [Name | Best For | Starting Price | Key Differentiator]
├── H2: 1. [Your Product] — Best Overall Alternative
│   ├── Why it's the best alternative
│   ├── Key features comparison
│   ├── Pricing
│   └── CTA: Start free trial
├── H2: 2-N. [Other Alternatives]
├── H2: [Competitor] vs Top Alternatives (Detailed)
│   └── [Feature-by-feature table]
├── H2: How to Switch from [Competitor]
│   └── Migration steps
├── H2: FAQ
└── CTA: Try [Your Product] Free
```

### Versus Page ("[Product A] vs [Product B]")

```
H1: [Product A] vs [Product B] — Honest Comparison ([Year])
├── Quick Verdict
├── H2: Overview Comparison
│   └── [Side-by-side table: features, pricing, ratings]
├── H2: Features Comparison
│   ├── H3: [Feature Category 1]
│   ├── H3: [Feature Category 2]
│   └── H3: [Feature Category 3]
├── H2: Pricing Comparison
│   └── [Tier-by-tier table]
├── H2: User Experience & Interface
├── H2: Customer Support
├── H2: Integrations
├── H2: Who Should Choose [A] vs [B]
├── H2: FAQ
└── CTA: Try [Your Product]
```

### Feature Page

```
H1: [Feature Name] — [Benefit Statement]
├── What is [Feature]?
├── H2: How [Feature] Works
│   └── Step-by-step walkthrough
├── H2: Key Benefits
├── H2: Use Cases
│   ├── H3: Use Case 1
│   └── H3: Use Case 2
├── H2: [Feature] vs Competitors
├── H2: Getting Started with [Feature]
├── H2: FAQ
└── CTA: Try it free
```

---

## SaaS Schema Markup

### SoftwareApplication Schema

```json
{
  "@type": "SoftwareApplication",
  "name": "string",
  "description": "string",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "url": "string",
  "offers": {
    "@type": "Offer",
    "price": "number or 0 for free",
    "priceCurrency": "USD"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "number",
    "reviewCount": "number",
    "bestRating": 5
  },
  "screenshot": "string — URL",
  "featureList": ["string array of key features"]
}
```

---

## SaaS-Specific SEO Rules

```
SAAS-001: Include pricing information (even if "starts at" or "contact sales")
SAAS-002: Include feature comparison tables (minimum 5 features, 3 products)
SAAS-003: Include "who it's best for" sections
SAAS-004: Include migration/switching information when relevant
SAAS-005: Include integration lists where applicable
SAAS-006: Reference G2, Capterra, or TrustPilot ratings when available
SAAS-007: Don't disparage competitors — compare objectively
SAAS-008: Include free trial/demo CTA (not just "buy now")
SAAS-009: Include customer testimonials or case study references
SAAS-010: Update pricing and feature data regularly (mark with date)
SAAS-011: If your product is mentioned, be transparent about bias
SAAS-012: Include scalability and enterprise considerations
```

---

## Configuration

```json
{
  "workflow": "saas",
  "settings": {
    "min_word_count": 2000,
    "max_word_count": 4000,
    "include_pricing_table": true,
    "include_feature_comparison": true,
    "include_software_schema": true,
    "include_ratings": true,
    "competitor_context": true,
    "cta_type": "free_trial | demo | signup | contact_sales",
    "product_name": "{{product_name}}",
    "product_url": "{{product_url}}",
    "is_own_product_mentioned": true,
    "bias_disclosure": true
  }
}
```
