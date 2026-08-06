# SEO Rules — SEOForge Configuration

> Config: On-Page SEO Constraints & Technical Requirements
> Applies to: All Agents
> Version: 1.0.0

---

## 1. ON-PAGE SEO REQUIREMENTS

### Title Tag (Meta Title)

| Rule | Specification |
|------|---------------|
| Length | 50-60 characters (hard limit) |
| Primary keyword | Must be present, front-loaded preferred |
| Brand name | Append with " \| Brand" if room |
| Uniqueness | Must be unique across all pages on site |
| Click-worthy | Include power word or modifier |
| Year | Include if topic is time-sensitive |

### Meta Description

| Rule | Specification |
|------|---------------|
| Length | 120-160 characters |
| Primary keyword | Must be present naturally |
| CTA | Include action word (Learn, Discover, Find, Get) |
| Uniqueness | Must be unique across all pages |
| Matching intent | Must match the search intent |
| No quotes | Avoid " characters (get truncated) |

### URL Slug

| Rule | Specification |
|------|---------------|
| Format | lowercase-with-hyphens |
| Length | Under 60 characters |
| Keywords | Include primary keyword |
| Stop words | Remove (a, an, the, is, in, for, etc.) |
| Readability | Should be human-readable |
| Consistency | Match site's URL structure |

---

## 2. HEADING STRUCTURE

```
HEADING HIERARCHY RULES:

1. EXACTLY 1 H1 per page
2. H1 must contain primary keyword naturally
3. H1 must NOT be identical to meta title
4. Never skip levels (H1 → H3 without H2 is invalid)
5. Minimum 4 H2 sections
6. Minimum 3 H3 sections total
7. H4 sections optional (for very detailed content)
8. Each H2 covers a distinct subtopic
9. At least 1 H2 contains the primary keyword
10. Secondary keywords distributed across H2/H3
11. Heading text under 70 characters
12. No duplicate heading text
13. Question-format headings for FAQ sections
14. Never use H1 formatting for non-H1 content
```

---

## 3. KEYWORD OPTIMIZATION

### Keyword Density Targets

| Keyword Type | Density Range | Measurement |
|-------------|---------------|-------------|
| Primary keyword | 0.5-3.0% | (count / total words) * 100 |
| Secondary keywords (each) | 0.3-1.5% | Same calculation |
| Semantic keywords | No target | Natural occurrence |
| NLP keywords | No target | Natural occurrence |

### Keyword Placement Requirements

```
PRIMARY KEYWORD must appear in:
☐ H1 heading (natural placement)
☐ First 100 words of the article
☐ At least 1 H2 heading
☐ Meta title (front-loaded preferred)
☐ Meta description
☐ URL slug
☐ At least 1 image alt text
☐ Conclusion/summary section

SECONDARY KEYWORDS should appear in:
☐ H2/H3 headings (≥ 2 different keywords)
☐ Body paragraphs (distributed, not clustered)
☐ FAQ answers (where relevant)
```

### Anti-Stuffing Rules

```
STUFF-001: If primary keyword density > 3%, reduce usage
STUFF-002: Never use exact keyword match more than once per paragraph
STUFF-003: Never put the keyword in more than 50% of H2 headings
STUFF-004: Don't use keyword at the start of consecutive paragraphs
STUFF-005: Use keyword variations (plural, synonyms) to distribute naturally
STUFF-006: If keyword placement feels forced, leave it out
STUFF-007: Never add invisible/hidden keywords
STUFF-008: Don't stack keywords in image alt text
```

---

## 4. LINK STRATEGY

### Internal Links

```
INT-LINK-001: Minimum 3 internal links per article
INT-LINK-002: Maximum 1 internal link per 200 words
INT-LINK-003: First internal link within 300 words
INT-LINK-004: Descriptive anchor text (3-7 words, contains target keyword)
INT-LINK-005: Contextually relevant placement
INT-LINK-006: Distributed across sections (not clustered)
INT-LINK-007: Link to pillar page (mandatory)
INT-LINK-008: Link to 2+ related cluster/sibling pages
INT-LINK-009: No duplicate targets (same URL linked max 2x)
INT-LINK-010: Same-tab opening (no target="_blank")
```

### External Links

```
EXT-LINK-001: Minimum 2 external links per article
EXT-LINK-002: Maximum 5 external links
EXT-LINK-003: Link to authoritative sources (studies, official docs, .edu, .gov)
EXT-LINK-004: Never link to direct competitors
EXT-LINK-005: Descriptive anchor text
EXT-LINK-006: Use for source citations when referencing data
EXT-LINK-007: Open in new tab when linking externally
EXT-LINK-008: Consider rel="nofollow" for sponsored/commercial links
EXT-LINK-009: Verify links are live and accessible
```

---

## 5. IMAGE OPTIMIZATION

```
IMG-001: Every article should have at least 1 image
IMG-002: Every image must have alt text
IMG-003: Alt text must be descriptive (not "image1.jpg")
IMG-004: Include primary keyword in 1 alt text (if natural)
IMG-005: Keep alt text under 125 characters
IMG-006: Don't start alt text with "Image of" or "Picture of"
IMG-007: Featured image dimensions: 1200x630 (OG standard)
IMG-008: Use descriptive filenames (keyword-research-tools.png not IMG_001.png)
IMG-009: Compress images for fast loading
IMG-010: Use WebP format when possible
```

---

## 6. SCHEMA MARKUP REQUIREMENTS

### Required Schema Types

| Schema | When Required |
|--------|--------------|
| Article (or BlogPosting) | Every article |
| FAQPage | Every article with FAQ section |
| BreadcrumbList | Every article |
| Person (Author) | When author is configured |
| LocalBusiness | Local SEO workflow only |
| Product | E-commerce workflow only |
| SoftwareApplication | SaaS workflow only |

### Schema Quality Rules

```
SCHEMA-001: All JSON-LD must be valid JSON
SCHEMA-002: All required properties must be present
SCHEMA-003: No empty strings for required fields
SCHEMA-004: URLs must be absolute (https://)
SCHEMA-005: Dates must be ISO 8601 format
SCHEMA-006: FAQ schema answers must match article FAQ
SCHEMA-007: Each schema in a separate <script> block
SCHEMA-008: @context must be "https://schema.org"
SCHEMA-009: Test with Google Rich Results Test
SCHEMA-010: No misleading schema (must match page content)
```

---

## 7. TECHNICAL SEO CHECKLIST

Every published page must have:

```
☐ Unique meta title (50-60 chars)
☐ Unique meta description (120-160 chars)
☐ Canonical URL (self-referencing)
☐ Open Graph tags (title, desc, image, type, url)
☐ Twitter Card tags (card, title, desc, image)
☐ JSON-LD Article schema
☐ JSON-LD FAQ schema (if FAQ present)
☐ JSON-LD Breadcrumb schema
☐ Proper heading hierarchy (H1 > H2 > H3)
☐ Mobile-responsive layout
☐ Fast page load (< 3 seconds)
☐ Robots tag (index, follow)
☐ Language tag
☐ Proper URL structure (clean, readable)
☐ Internal links (≥ 3)
☐ External links (≥ 2)
☐ Image alt text (all images)
☐ Sitemap inclusion
```
