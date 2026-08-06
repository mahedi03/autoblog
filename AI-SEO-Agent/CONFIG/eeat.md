# E-E-A-T Compliance Framework — SEOForge Configuration

> Config: Experience, Expertise, Authoritativeness, Trustworthiness
> Applies to: Writing Agent, SEO Review Agent
> Version: 1.0.0
> Reference: Google Search Quality Rater Guidelines

---

## 1. EXPERIENCE (E)

### What Google Looks For

Content demonstrates the creator has **necessary first-hand or life experience** for the topic.

### How to Demonstrate Experience

| Signal | Implementation | Example |
|--------|---------------|---------|
| Practical advice | Include tips that only come from doing the thing | "In practice, the biggest mistake is starting with too many keywords. Focus on 3-5 first." |
| Specific scenarios | Reference real situations and challenges | "When we migrated from WordPress to Next.js, the biggest challenge was..." |
| Process insights | Share what actually happens vs. theory | "The textbook says to aim for 2% keyword density, but in our tests, 1-1.5% performed better." |
| Tool/method references | Name specific tools used in practice | "We use Ahrefs for competitor analysis and Clearscope for content optimization." |
| Common mistakes | Share pitfalls learned from experience | "A common mistake is choosing keywords based on volume alone. Search intent matters more." |
| Lessons learned | Share what worked and what didn't | "After testing 50+ articles, we found that longer isn't always better..." |

### Experience Phrases to Include

```
Natural signals (USE):
- "In our experience..."
- "In practice, what works is..."
- "A common mistake we've seen is..."
- "After testing [specific thing]..."
- "What most people don't realize is..."
- "One thing we've learned is..."
- "The reality is..."
- "Here's what actually happens..."

Forced signals (AVOID):
- "As an expert, I can tell you..."
- "With my 20 years of experience..."
- "Trust me when I say..."
- "I've personally verified this..."
```

### Minimum Experience Requirements

```
☐ At least 1 practical tip per major H2 section
☐ At least 2 "common mistakes" or "what to avoid" items per article
☐ At least 1 specific tool/method recommendation
☐ At least 1 "what actually works" vs. "what theory says" comparison
☐ No generic advice that anyone could give without experience
```

---

## 2. EXPERTISE (E)

### What Google Looks For

Content demonstrates **formal expertise, skill, or deep knowledge** about the topic.

### How to Demonstrate Expertise

| Signal | Implementation |
|--------|---------------|
| Correct terminology | Use industry-specific terms correctly |
| Nuanced discussion | Acknowledge trade-offs, exceptions, edge cases |
| Depth of coverage | Cover subtopics comprehensively |
| Framework references | Cite established methodologies |
| Data interpretation | Don't just present data, analyze it |
| Technical accuracy | All facts, figures, and claims must be verifiable |
| Structured thinking | Organize information logically and hierarchically |

### Expertise Depth Levels

| Level | Description | When to Use |
|-------|-------------|-------------|
| **Beginner-friendly** | Explain concepts simply, define terms | Informational intent, broad audience |
| **Intermediate** | Assume basic knowledge, go deeper | How-to guides, tutorials |
| **Advanced** | Technical detail, no hand-holding | Developer docs, professional guides |
| **Expert** | Cutting-edge insights, original analysis | Industry reports, thought leadership |

Match expertise depth to the **search intent** and **target audience**.

### Minimum Expertise Requirements

```
☐ Correct use of all industry terminology
☐ At least 1 framework/methodology reference per article
☐ At least 1 nuanced discussion (trade-offs, exceptions)
☐ No factual errors
☐ Data cited with sources
☐ Technical claims are accurate and verifiable
☐ Depth matches audience expectation
```

---

## 3. AUTHORITATIVENESS (A)

### What Google Looks For

The creator/site is a recognized, **authoritative source** for the topic.

### How to Demonstrate Authoritativeness

| Signal | Implementation |
|--------|---------------|
| Source citations | Link to authoritative external sources |
| Expert references | Quote or reference recognized experts |
| Industry reports | Reference industry studies and data |
| Internal depth | Link to related articles (topical authority) |
| Author credentials | Show author expertise via bio and schema |
| Original analysis | Present unique data or perspectives |
| Awards/recognition | Reference relevant certifications or accolades |

### Citation Quality Hierarchy

```
Tier 1 (Strongest — prefer these):
├── Academic research papers (peer-reviewed)
├── Government sources (.gov)
├── Official documentation
├── Industry standards bodies
└── Major research firms (Gartner, Forrester, etc.)

Tier 2 (Strong):
├── Industry publications (HBR, TechCrunch, etc.)
├── Educational institutions (.edu)
├── Major news outlets
├── Published books by recognized authors
└── Official company blogs/reports

Tier 3 (Acceptable):
├── Industry blogs with strong reputation
├── Expert personal sites with credentials
├── Survey results with methodology
└── Conference presentations

Tier 4 (Weak — use sparingly):
├── Social media posts
├── Forum discussions
├── Wikipedia (cite the original source instead)
└── Unattributed statistics
```

### Minimum Authoritativeness Requirements

```
☐ At least 2 external citations from Tier 1-2 sources
☐ At least 1 expert/organization reference
☐ At least 3 internal links (topical authority signal)
☐ Author attribution with credentials (if configured)
☐ Article schema with proper author markup
☐ Published date and last-updated date
```

---

## 4. TRUSTWORTHINESS (T)

### What Google Looks For

The content and site are **reliable, honest, and safe** for users.

### How to Demonstrate Trustworthiness

| Signal | Implementation |
|--------|---------------|
| Balanced perspective | Present pros AND cons, not just positives |
| Transparency | Disclose affiliations, sponsorships, limitations |
| Accuracy | All facts are verifiable, no fabrication |
| Freshness | Content is current, dates are visible |
| Source attribution | Cite everything that's not original insight |
| Error-free | Grammar, spelling, formatting are professional |
| User safety | No misleading claims, especially for YMYL topics |

### Trust Phrases to Include

```
Balanced view signals:
- "However, there are some limitations..."
- "On the other hand..."
- "It's worth noting that this doesn't work for every situation..."
- "The trade-off is..."
- "While this approach works well for [X], it may not be ideal for [Y]..."

Transparency signals:
- "Disclaimer: [disclosure]"
- "As of [date], [information]"
- "According to [source]..."
- "Note: Prices and features may change"
- "[Full disclosure: we are/aren't affiliated with...]"
```

### YMYL (Your Money or Your Life) Considerations

For topics related to health, finance, safety, or legal matters:

```
YMYL-001: Extra scrutiny on factual accuracy
YMYL-002: Must cite authoritative sources (medical journals, financial regulators)
YMYL-003: Include disclaimers ("This is not medical/financial/legal advice")
YMYL-004: Author must have relevant credentials
YMYL-005: Content must not cause potential harm
YMYL-006: Present conservative, evidence-based recommendations
YMYL-007: Include "consult a professional" guidance where appropriate
```

### Minimum Trustworthiness Requirements

```
☐ Balanced perspective (pros AND cons where applicable)
☐ At least 1 limitation/caveat acknowledged
☐ Published date visible
☐ All data attributed to sources
☐ No fabricated quotes, statistics, or studies
☐ Professional formatting (no errors)
☐ Disclosure of any affiliations (if applicable)
☐ YMYL disclaimer if topic warrants
```

---

## 5. EEAT SCORING

### Scoring Matrix (per SYSTEM.md Section 4)

| Signal | Points | Assessment Method |
|--------|--------|-------------------|
| First-hand experience demonstrated | 15 | Count practical tips, real scenarios |
| Correct terminology and depth | 15 | Check terms, verify accuracy |
| Credible sources cited | 10 | Count and quality of citations |
| Comprehensive topic coverage | 15 | Subtopic coverage percentage |
| Unique insights/analysis | 10 | Original perspectives present |
| Expert tips/pro tips | 5 | Count expert tip blocks |
| Author attribution | 5 | Author bio and schema |
| Structured data present | 5 | Schema types present |
| Internal links (topical depth) | 10 | Count and relevance |
| Transparent about limitations | 5 | Balanced view present |
| Professional formatting | 5 | Error-free, well-structured |
| **Total** | **100** | **Minimum pass: 70** |
