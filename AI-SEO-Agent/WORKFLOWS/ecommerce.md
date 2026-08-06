# E-commerce Workflow — SEOForge

> Workflow: E-commerce SEO Content Pipeline
> Based on: Standard Workflow (with e-commerce modifications)
> Content Types: Product pages, category pages, buying guides, product comparisons

---

## Overview

The E-commerce workflow is optimized for content that drives product sales. It emphasizes commercial intent keywords, product schema markup, comparison tables, and conversion-focused CTAs.

---

## Key Differences from Standard Workflow

| Aspect | Standard | E-commerce |
|--------|----------|------------|
| Keywords | Informational keywords | Commercial + transactional keywords |
| Intent | Learn/understand | Compare/buy |
| Schema | Article + FAQ | Product + Review + Offer + FAQ + BreadcrumbList |
| Content Focus | Education | Purchase decision support |
| CTA | Generic | Buy/Add to cart/Compare/Get deal |
| Tables | Optional | Required (product comparisons) |
| Pricing | Not typical | Required where possible |

---

## Content Type Templates

### Product Review Page

```
H1: [Product Name] Review ([Year]) — Is It Worth It?
├── TL;DR / Quick Verdict
│   └── Rating, Best For, Price, Buy Link
├── H2: [Product] at a Glance
│   └── [Quick specs table]
├── H2: What We Like (Pros)
├── H2: What We Don't Like (Cons)
├── H2: Key Features
│   ├── H3: Feature 1
│   ├── H3: Feature 2
│   └── H3: Feature 3
├── H2: Performance / Testing
├── H2: Pricing & Plans
│   └── [Pricing comparison table]
├── H2: [Product] vs Alternatives
│   └── [Comparison table]
├── H2: Who Should Buy [Product]?
├── H2: FAQ
└── Verdict + Buy CTA
```

### Category / Buying Guide

```
H1: Best [Category] in [Year] — [Modifier]
├── Quick Picks Summary
│   └── [Top 3 picks table: Name | Best For | Price]
├── H2: How We Tested / Our Methodology
├── H2: 1. [Product] — Best Overall
│   ├── Specs, Pros/Cons, Rating
│   └── Buy CTA
├── H2: 2. [Product] — Best Value
│   └── (same structure)
├── H2: 3-7. [Additional Products]
├── H2: Buying Guide — How to Choose
│   ├── H3: Key Factor 1
│   ├── H3: Key Factor 2
│   └── H3: Key Factor 3
├── H2: FAQ
└── Final Recommendation + CTA
```

### Product Comparison (vs.)

```
H1: [Product A] vs [Product B] — Which Is Better? ([Year])
├── Quick Comparison Table
├── H2: Overview
│   ├── H3: [Product A] Overview
│   └── H3: [Product B] Overview
├── H2: Feature Comparison
│   └── [Detailed comparison table]
├── H2: Pricing Comparison
├── H2: Pros & Cons
│   ├── H3: [Product A] Pros & Cons
│   └── H3: [Product B] Pros & Cons
├── H2: Use Cases — When to Choose Which
├── H2: User Reviews & Reputation
├── H2: FAQ
└── Verdict: Our Recommendation
```

---

## E-commerce Schema Markup

### Product Schema

```json
{
  "@type": "Product",
  "name": "string",
  "description": "string",
  "image": "string",
  "brand": {
    "@type": "Brand",
    "name": "string"
  },
  "offers": {
    "@type": "Offer",
    "price": "number",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "string"
  },
  "review": {
    "@type": "Review",
    "author": { "@type": "Person", "name": "string" },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": "number",
      "bestRating": 5
    },
    "reviewBody": "string"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "number",
    "reviewCount": "number"
  }
}
```

---

## E-commerce SEO Rules

```
ECOM-001: Include price or price range when available
ECOM-002: Include at least 1 comparison table per article
ECOM-003: Include pros and cons for every product mentioned
ECOM-004: Use affiliate disclosure when applicable
ECOM-005: Include "Best For" categorization for each product
ECOM-006: Include star ratings where data is available
ECOM-007: CTA buttons should be specific ("Check Price on Amazon" not "Buy Now")
ECOM-008: Include last-updated date for price accuracy
ECOM-009: Don't make unverifiable claims about product performance
ECOM-010: Include at least 3 products in comparison/best-of articles
```

---

## Configuration

```json
{
  "workflow": "ecommerce",
  "settings": {
    "min_word_count": 2000,
    "max_word_count": 5000,
    "include_pricing": true,
    "include_product_schema": true,
    "include_comparison_tables": true,
    "include_pros_cons": true,
    "include_ratings": true,
    "include_buy_cta": true,
    "affiliate_disclosure": true,
    "price_disclaimer": "Prices may vary. Last updated: {{date}}",
    "rating_source": "aggregated"
  }
}
```
