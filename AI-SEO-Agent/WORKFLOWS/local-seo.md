# Local SEO Workflow — SEOForge

> Workflow: Local Business SEO Content Pipeline
> Based on: Standard Workflow (with local modifications)
> Content Types: Location pages, service area pages, local guides

---

## Overview

The Local SEO workflow is a specialized variant of the standard pipeline, optimized for local business content that targets geographic keywords and Google Local Pack results.

---

## Key Differences from Standard Workflow

| Aspect | Standard | Local SEO |
|--------|----------|-----------|
| Keywords | Generic topic keywords | Geo-modified keywords (keyword + city/region) |
| Intent | Informational/Commercial | Transactional/Local |
| Schema | Article + FAQ | LocalBusiness + Service + FAQ + GeoCoordinates |
| Entities | Topic entities | Local businesses, landmarks, neighborhoods |
| Internal Links | Topical cluster links | Service area cross-links |
| Content Focus | Education/information | Services, trust, local expertise |

---

## Modified Phase Instructions

### Phase 1: Local Keyword Research

Additional keyword types to extract:

```
- "[service] + [city]"
- "[service] + near me"
- "[service] + [neighborhood]"
- "[service] + [city] + cost/price"
- "best [service] + [city]"
- "[service] + [city] + reviews"
- "[city] + [service] + hours"
```

Additional entity types:
- Local competitors
- Local landmarks and neighborhoods
- Local regulations or permits
- Local review platforms
- Community organizations

### Phase 2: Local SERP Analysis

Additional analysis:
- Google Local Pack results (top 3 map results)
- Google Business Profile signals
- Local review aggregators (Yelp, Angi, etc.)
- Local directory listings
- Competitor GBP completeness

### Phase 4: Local Outline Structure

```
H1: [Service] in [City] — [Value Proposition]
├── Introduction (local context)
├── H2: Our [Service] in [City]
│   ├── H3: What We Offer
│   └── H3: Service Areas in [Region]
├── H2: Why Choose [Brand] for [Service] in [City]
│   ├── H3: Local Experience
│   └── H3: Customer Reviews
├── H2: [Service] Process / How It Works
├── H2: [Service] Cost in [City]
│   └── [Pricing table]
├── H2: Service Areas
│   └── [List of neighborhoods/zip codes served]
├── H2: FAQ
├── H2: Contact / Get a Quote
└── CTA: Call/Schedule/Quote
```

### Phase 8: Local Schema Markup

Additional schemas:

```json
{
  "@type": "LocalBusiness",
  "name": "string",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "string",
    "addressLocality": "string (city)",
    "addressRegion": "string (state)",
    "postalCode": "string",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "number",
    "longitude": "number"
  },
  "telephone": "string",
  "url": "string",
  "openingHours": ["string array"],
  "priceRange": "string ($$)",
  "areaServed": [
    {
      "@type": "City",
      "name": "string"
    }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "number",
    "reviewCount": "number"
  }
}
```

Service schema:
```json
{
  "@type": "Service",
  "name": "string",
  "description": "string",
  "provider": { "@type": "LocalBusiness" },
  "areaServed": { "@type": "City", "name": "string" },
  "serviceType": "string"
}
```

---

## Local SEO Configuration

```json
{
  "workflow": "local-seo",
  "settings": {
    "min_word_count": 1000,
    "max_word_count": 3000,
    "include_pricing_table": true,
    "include_service_areas": true,
    "include_local_schema": true,
    "include_review_signals": true,
    "geo_modifier": "{{city}}, {{state}}",
    "service_area_radius": "30 miles",
    "include_map_embed": true,
    "include_contact_cta": true,
    "nap_consistency": true
  }
}
```
