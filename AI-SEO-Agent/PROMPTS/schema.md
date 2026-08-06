# Schema Markup Prompt — SEOForge

> Prompt Type: Technical SEO
> Used By: Publisher Agent
> Phase: 8 — Schema Generation

---

## Prompt Template

```
TASK: Generate complete, valid JSON-LD structured data for the article.

ARTICLE DATA:
{{article_output}}

SITE CONFIGURATION:
{{site_config}}

AUTHOR CONFIGURATION:
{{author_config}}

GENERATE THE FOLLOWING SCHEMAS:

1. ARTICLE SCHEMA (@type: Article)
Required properties:
- headline (article title)
- description (meta description)
- image (featured image — ImageObject with url, width, height)
- author (Person with name, url, description, sameAs)
- publisher (Organization with name, logo)
- datePublished (ISO 8601)
- dateModified (ISO 8601)
- mainEntityOfPage (WebPage with @id = canonical URL)
- wordCount
- articleSection (category)
- keywords (array of primary + secondary keywords)
- about (array of Thing entities)
- mentions (array of Thing entities with sameAs URLs)

2. FAQ SCHEMA (@type: FAQPage)
For each FAQ item in the article:
- @type: Question
  - name: exact question text
  - acceptedAnswer:
    - @type: Answer
    - text: plain text answer (no HTML tags)

3. BREADCRUMB SCHEMA (@type: BreadcrumbList)
- Home → Category → Article
- Each item: ListItem with position, name, item (URL)

4. AUTHOR SCHEMA (@type: Person) — if author configured
- name, jobTitle, description, url, image
- sameAs (social profile URLs)
- worksFor (Organization)

VALIDATION RULES:
- All JSON must be valid (parseable by JSON.parse)
- All required properties must be present
- No empty strings for required fields
- Image dimensions must be realistic (e.g., 1200x630)
- Dates must be valid ISO 8601
- URLs must be absolute (https://...)
- sameAs URLs must be real profile patterns (linkedin.com/in/, twitter.com/)
- Schema @context must be "https://schema.org"
- Each schema is a separate JSON-LD block

OUTPUT FORMAT:
{
  "schemas": {
    "article": { ... valid JSON-LD ... },
    "faq": { ... valid JSON-LD ... },
    "breadcrumb": { ... valid JSON-LD ... },
    "author": { ... valid JSON-LD ... }
  },
  "html_output": "string — all schema blocks as <script type='application/ld+json'> tags"
}

TESTING CHECKLIST:
☐ Valid JSON syntax (no trailing commas, proper quotes)
☐ @context is "https://schema.org" in each block
☐ @type is correct for each schema
☐ All required properties present
☐ No placeholder values (replace all with real data)
☐ FAQ answers match article FAQ section exactly
☐ Breadcrumb hierarchy is logical
☐ Image URLs are valid format
☐ Date formats are ISO 8601
```

---

## Variable Reference

| Variable | Description | Source |
|----------|-------------|--------|
| `{{article_output}}` | Complete article with metadata | Writing Agent |
| `{{site_config}}` | Site name, URL, logo | User configuration |
| `{{author_config}}` | Author details | AI Memory |
