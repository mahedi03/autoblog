# Writing Rules — SEOForge Configuration

> Config: Writing Style & Formatting Rules
> Applies to: Writing Agent, SEO Review Agent
> Version: 1.0.0

---

## 1. VOICE & TONE

### Default Voice Profile

```json
{
  "voice": {
    "primary_tone": "professional-casual",
    "personality": "Knowledgeable friend who is also an expert. Confident without arrogance. Helpful without being patronizing.",
    "formality": "semi-formal",
    "perspective": "second-person (you/your)",
    "contractions": true,
    "humor": "subtle, occasional, never forced",
    "empathy": "acknowledge reader's challenges before offering solutions"
  }
}
```

### Tone Presets

| Preset | Description | Use Case |
|--------|-------------|----------|
| **professional** | Authoritative, data-driven, minimal personality | B2B, enterprise, technical |
| **casual** | Friendly, conversational, relatable | B2C, lifestyle, community |
| **authoritative** | Expert-level, comprehensive, academic-leaning | Medical, legal, financial |
| **friendly** | Warm, encouraging, supportive | Education, personal development |
| **technical** | Precise, detailed, specification-focused | Developer docs, engineering |
| **conversational** | Like talking to a friend, informal | Social media, culture |

---

## 2. SENTENCE RULES

```
SEN-001: Maximum sentence length: 25 words (hard limit for most sentences)
SEN-002: Average sentence length: 15-20 words
SEN-003: Mix short (5-10 words) with medium (15-20 words)
SEN-004: Occasional long sentence allowed (25-30 words) for complex ideas
SEN-005: Never start 2 consecutive sentences with the same word
SEN-006: Never start 3 paragraphs with the same word
SEN-007: Active voice for ≥ 80% of sentences
SEN-008: One idea per sentence
SEN-009: Strong verbs over weak verb + adverb combinations
SEN-010: Specific nouns over vague pronouns
```

### Sentence Variety Patterns

```
Good variety:
"Short statement. This adds context with a medium-length follow-up. 
Then elaborate further."

Bad (monotonous):
"This is an important topic. This requires careful consideration. 
This involves multiple factors. This demands attention."
```

---

## 3. PARAGRAPH RULES

```
PAR-001: Maximum 3 sentences per paragraph
PAR-002: Average 2 sentences per paragraph is ideal
PAR-003: Single-sentence paragraphs are powerful for emphasis (use sparingly)
PAR-004: Each paragraph should contain ONE main idea
PAR-005: Paragraphs must flow logically from one to the next
PAR-006: Visual variety — alternate 1, 2, and 3-sentence paragraphs
PAR-007: Never have 4+ consecutive paragraphs without a visual break
```

Visual breaks include: headings, lists, tables, blockquotes, images, horizontal rules.

---

## 4. TRANSITION GUIDELINES

### Natural Transitions (USE)

```
Between topics:
- "That brings us to..."
- "On a related note..."
- "Here's where it gets interesting..."
- "Speaking of [topic]..."
- "This connects directly to..."

Contrasting:
- "But here's the thing..."
- "However, [contrast]"
- "On the other hand..."
- "The opposite is also true..."
- "That said..."

Building on:
- "What makes this even better is..."
- "Taking this further..."
- "Building on that..."
- "Here's why this matters..."
- "The real insight is..."

Providing examples:
- "For example..."
- "Consider this..."
- "Here's what that looks like in practice..."
- "A good example is..."
- "Take [specific example]..."
```

### Mechanical Transitions (AVOID)

```
- "Moreover,"
- "Furthermore,"
- "Additionally,"
- "Subsequently,"
- "Consequently,"
- "In addition to the above,"
- "As mentioned earlier,"
- "Moving on to the next point,"
- "With that in mind,"
```

---

## 5. FORMATTING RULES

### Bold Text

```
BOLD-001: Bold key terms on FIRST mention only
BOLD-002: Bold important takeaways or definitions
BOLD-003: Bold product/tool names on first mention
BOLD-004: Never bold entire sentences
BOLD-005: Maximum 1-2 bold phrases per paragraph
```

### Lists

```
LIST-001: Use bullet lists for 3+ non-sequential items
LIST-002: Use numbered lists for steps, rankings, or priorities
LIST-003: Each list item should be roughly the same length
LIST-004: Bold the lead phrase if items have descriptions
LIST-005: Keep list items under 2 sentences each
LIST-006: Maximum 10 items per list (break into sub-lists if more)
LIST-007: Parallel structure — all items should follow the same grammatical pattern
```

### Tables

```
TABLE-001: Use for comparing 3+ items across 3+ attributes
TABLE-002: Headers should be clear and descriptive
TABLE-003: Sort by most relevant/popular first
TABLE-004: Include a caption sentence before the table
TABLE-005: Minimum 3 rows, 3 columns
TABLE-006: Maximum 10 rows (summarize if more data exists)
TABLE-007: Align numerical data consistently
```

### Blockquotes

```
QUOTE-001: Use for expert quotes (with attribution)
QUOTE-002: Use for important warnings or callouts
QUOTE-003: Use for key statistics or findings
QUOTE-004: Format: > "Quote text" — Attribution
QUOTE-005: Maximum 2 blockquotes per 1000 words
```

---

## 6. WORD CHOICE RULES

### Banned Words (STRICTLY FORBIDDEN)

```
- delve
- landscape
- realm
- crucial
- leverage
- game-changer
- unlock
- seamless
- cutting-edge
- robust
- dynamic
- revolutionize
- elevate
- mastering
- tapestry
- bustling
- vibrant
- moreover
- furthermore
- additionally
- consequently
- subsequently
- notwithstanding
- paradigm shift
- synergy
- holistic approach
- comprehensive solution
- one-stop solution
```

### Preferred Vocabulary

| Instead of | Use |
|-----------|-----|
| delve | explore, examine, analyze, inspect |
| landscape | environment, sector, industry, market |
| realm | area, field, space, category |
| crucial | essential, vital, key, important |
| leverage | use, apply, take advantage of, build on |
| game-changer | major shift, breakthrough, key improvement |
| unlock | enable, reveal, open up, access |
| seamless | smooth, direct, easy, effortless |
| cutting-edge | modern, advanced, latest |
| robust | strong, durable, comprehensive, solid |
| dynamic | active, flexible, changing |
| revolutionize | transform, improve, reshape |
| elevate | raise, boost, improve, enhance |
| mastering | learning, understanding, perfecting |
| utilize | use |
| implement | set up, build, create, add |
| facilitate | help, make easier, enable |
| commence | start, begin |
| terminate | end, stop |
| endeavor | try, attempt |
| subsequently | then, after that, next |
| prior to | before |
| in order to | to |
| due to the fact that | because |
| at this point in time | now |
| the majority of | most |
| a large number of | many |
| the majority of | most |

### Power Words for SEO

```
Engagement: proven, exclusive, essential, critical, insider, expert
Urgency: now, today, immediately, quick, fast, instant
Value: free, save, best, top, ultimate, complete, comprehensive
Trust: tested, verified, research-backed, data-driven, expert-approved
Emotion: surprising, remarkable, incredible, powerful, game-changing (sparingly)
```

---

## 7. CONTENT DENSITY RULES

```
DENSITY-001: Every sentence must add value (no filler)
DENSITY-002: Avoid repeating the same point in different words
DENSITY-003: If information is obvious, skip it
DENSITY-004: Lead with the most important information in each section
DENSITY-005: Cut throat on "throat-clearing" sentences at the start of sections
DENSITY-006: Conclusions should be new insights, not repetition
```

### Filler Detection

These patterns indicate filler — remove or rewrite:

```
- "It is important to understand that..."
- "One thing to keep in mind is..."
- "It goes without saying that..."
- "As you may already know..."
- "It should be noted that..."
- "It is worth pointing out that..."
- "The thing about [topic] is..."
```

Replace with: just state the important thing directly.
