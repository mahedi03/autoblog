# Topical Map Configuration — SEOForge

> Config: Topical Map Interpretation & Management Rules
> Applies to: Outline Agent (Phase 5), Writing Agent (internal links)
> Version: 1.0.0

---

## 1. TOPICAL MAP STRUCTURE

### What is a Topical Map?

A topical map is a hierarchical representation of all content on a website organized by topic clusters. It establishes **topical authority** by showing Google that the site comprehensively covers a subject area.

### Node Types

```
PILLAR PAGE (Hub)
├── The main page for a broad topic
├── Links to all cluster and supporting pages
├── Comprehensive overview (3000-5000 words)
├── Targets high-volume, competitive keywords
└── Example: "Keyword Research — The Complete Guide"

CLUSTER PAGE
├── Covers a specific subtopic of the pillar
├── Links back to pillar page
├── Links to sibling cluster pages
├── Moderate depth (1500-3000 words)
├── Targets medium-competition keywords
└── Example: "Long-Tail Keywords: How to Find and Use Them"

SUPPORTING PAGE
├── Deep dive into a very specific topic
├── Links back to parent cluster or pillar
├── May link to related supporting pages
├── Focused depth (1000-2000 words)
├── Targets low-competition, long-tail keywords
└── Example: "How to Find Long-Tail Keywords with Ahrefs"
```

### Hierarchy Visualization

```
                    PILLAR
                   /      \
            CLUSTER 1    CLUSTER 2    CLUSTER 3
           /    \        /    \        /    \
        SUP 1  SUP 2  SUP 3  SUP 4  SUP 5  SUP 6
```

---

## 2. TOPICAL MAP SCHEMA

### Input Format (topical-map.json)

```json
{
  "topical_map": {
    "name": "string — map name",
    "root_topic": "string — main niche/topic",
    "website_url": "string — base URL",
    "nodes": [
      {
        "id": "string — unique identifier (e.g., 'km-001')",
        "title": "string — page title",
        "slug": "string — URL slug",
        "url": "string — full URL (if published)",
        "type": "pillar | cluster | supporting",
        "status": "published | draft | planned",
        "parent_id": "string | null — ID of parent node",
        "keywords": {
          "primary": "string — main keyword",
          "secondary": ["string array — supporting keywords"]
        },
        "category": "string — content category",
        "search_intent": "informational | commercial | transactional | navigational",
        "priority": "high | medium | low",
        "word_count_target": "number",
        "internal_links": [
          {
            "target_id": "string — target node ID",
            "anchor_text": "string",
            "context": "string — where to place",
            "priority": "high | medium | low"
          }
        ]
      }
    ]
  }
}
```

---

## 3. TOPICAL MAP ANALYSIS RULES

### When Creating a New Article

The Outline Agent must perform this analysis:

```
STEP 1: IDENTIFY POSITION
├── Find this article's node in the topical map
├── Determine its type (pillar/cluster/supporting)
├── Note its parent, siblings, and children
└── If not in map, suggest where it should be added

STEP 2: FIND PARENT PAGE
├── Identify the direct parent node
├── If cluster → parent is the pillar page
├── If supporting → parent is the cluster page
├── MANDATORY: Link to parent page in the article
└── Place parent link in introduction or first body section

STEP 3: FIND CHILD PAGES
├── Identify all child nodes of current article
├── Only applicable for pillar and cluster pages
├── Suggest links TO child pages from relevant sections
└── Priority: published children > draft > planned

STEP 4: FIND SIBLING PAGES
├── Identify all nodes with the same parent_id
├── These are thematically related articles
├── Suggest 2-3 sibling links in body content
└── Prioritize by relevance to current topic

STEP 5: FIND SUPPORTING PAGES
├── Identify nodes in related clusters
├── These add cross-cluster linking
├── Suggest 1-2 supporting page links
└── Place in FAQ or body where contextually relevant

STEP 6: GENERATE LINK SUGGESTIONS
├── For each suggested link, provide:
│   ├── Target URL
│   ├── Recommended anchor text (3-7 words)
│   ├── Alternative anchor options
│   ├── Suggested placement section
│   ├── Context sentence example
│   ├── Priority (high/medium/low)
│   └── Link type (parent/child/sibling/supporting)
└── Minimum 3, maximum 8 total links
```

### Link Priority Rules

```
PRIORITY 1 (MANDATORY):
├── Link to parent (pillar/cluster) page
└── This is the most important structural link

PRIORITY 2 (STRONGLY RECOMMENDED):
├── Link to 2 sibling pages
└── Strengthens the cluster

PRIORITY 3 (RECOMMENDED):
├── Link to 1 child page (if applicable)
├── Link to 1 cross-cluster supporting page
└── Extends the topical web

PRIORITY 4 (NICE TO HAVE):
├── Additional sibling or supporting links
└── Only if contextually natural
```

---

## 4. ANCHOR TEXT STRATEGY

### Anchor Text Rules

```
ANCHOR-001: 3-7 words, descriptive
ANCHOR-002: Contains target page's primary keyword (when natural)
ANCHOR-003: Reads naturally in the sentence
ANCHOR-004: Varied — don't use the same anchor for different links
ANCHOR-005: Never "click here," "read more," "learn more"
ANCHOR-006: Never the bare URL
ANCHOR-007: Not the exact page title (variations are better)
ANCHOR-008: Matches the context of the surrounding paragraph
```

### Anchor Text Examples

| Target Page | Good Anchor | Bad Anchor |
|-------------|-------------|------------|
| "Keyword Research Guide" | "keyword research process" | "click here" |
| "Best SEO Tools 2026" | "top SEO tools for analysis" | "this article" |
| "How to Build Backlinks" | "effective link building strategies" | "read more about backlinks" |
| "Content Marketing Strategy" | "developing a content strategy" | "https://site.com/content-strategy" |

---

## 5. TOPICAL MAP MAINTENANCE

### Adding New Nodes

When a new article is created:

```json
{
  "new_node": {
    "id": "auto-generated",
    "title": "string — from article title",
    "slug": "string — from published slug",
    "url": "string — from published URL",
    "type": "determined by keyword competition and depth",
    "status": "published",
    "parent_id": "determined by topical analysis",
    "keywords": {
      "primary": "string — from research",
      "secondary": ["from research"]
    }
  }
}
```

### Gap Identification

After analyzing the topical map, identify:

```json
{
  "topical_gaps": [
    {
      "suggested_title": "string",
      "suggested_keyword": "string",
      "type": "cluster | supporting",
      "parent_id": "string — where it should connect",
      "priority": "high | medium | low",
      "reasoning": "string — why this page should exist",
      "estimated_traffic_opportunity": "string"
    }
  ]
}
```

### Health Checks

```
MAP-HEALTH-001: Every cluster has at least 3 supporting pages
MAP-HEALTH-002: Every supporting page links back to its cluster parent
MAP-HEALTH-003: Every cluster links back to its pillar page
MAP-HEALTH-004: No orphan pages (pages with zero internal links to them)
MAP-HEALTH-005: No broken internal links
MAP-HEALTH-006: Pillar pages link to ALL published cluster pages
MAP-HEALTH-007: Cross-cluster linking exists (not siloed clusters)
MAP-HEALTH-008: All planned pages have keywords assigned
```

---

## 6. TOPICAL AUTHORITY METRICS

Track these metrics over time:

| Metric | Target | Description |
|--------|--------|-------------|
| Topic coverage | > 80% | % of planned pages published |
| Cluster completeness | > 70% | % of clusters with ≥ 3 supporting pages |
| Internal link ratio | ≥ 3/page | Average internal links per page |
| Orphan pages | 0 | Pages with no internal links pointing to them |
| Cross-cluster links | ≥ 1/cluster | Links between different clusters |
| Content freshness | < 12 months | Average age of published content |
