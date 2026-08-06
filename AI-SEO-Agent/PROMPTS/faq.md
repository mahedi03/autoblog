# FAQ Generation Prompt — SEOForge

> Prompt Type: Writing
> Used By: Writing Agent (sub-task)
> Phase: 6 — FAQ Section Generation

---

## Prompt Template

```
TASK: Generate a comprehensive FAQ section with schema-ready answers.

PRIMARY KEYWORD: {{primary_keyword}}
SEARCH INTENT: {{search_intent}}

PAA QUESTIONS FROM RESEARCH:
{{paa_questions}}

CONTENT GAP FAQ QUESTIONS:
{{missing_faqs}}

ARTICLE CONTEXT:
{{article_summary}}

GENERATE {{faq_count}} FAQ ENTRIES:

For each FAQ:

1. QUESTION
- Use natural language (how people actually ask)
- Include relevant keywords when natural
- Cover different aspects of the topic
- Mix question types (what, how, why, when, which, can, does)

2. ANSWER
- Start with a direct answer in the first sentence
- Provide supporting context (2-3 additional sentences)
- Include relevant keywords naturally
- Be 50-150 words per answer
- Use simple, clear language
- Add value beyond what's obvious

QUESTION SOURCING PRIORITY:
1. PAA questions (highest priority — these are real user queries)
2. Content gap questions (topics competitors miss)
3. Related search questions
4. Custom questions based on topic analysis

ANSWER QUALITY RULES:
- First sentence MUST directly answer the question
- No generic filler ("Great question!" or "This is a common question")
- Include specific details, numbers, or examples when possible
- Reference the article's main content where relevant
- Each answer should stand alone (understandable without context)

SCHEMA REQUIREMENTS:
- Each Q&A pair must be compatible with FAQPage schema
- Questions must be actual questions (ending with ?)
- Answers must be plain text (no HTML in schema version)
- Keep answers concise for featured snippet eligibility

OUTPUT FORMAT:
{
  "faq_items": [
    {
      "question": "string",
      "answer": "string (markdown version for article)",
      "answer_plain": "string (plain text for schema)",
      "source": "paa | content_gap | related_search | custom",
      "keywords_included": ["string array"],
      "featured_snippet_potential": true/false
    }
  ]
}

FEATURED SNIPPET OPTIMIZATION:
For questions with featured snippet potential:
- Answer in 40-60 words (paragraph snippet sweet spot)
- OR use a 3-8 item list format (list snippet)
- Start with a clear, definitive statement
- Include the keyword in the answer naturally
```

---

## Variable Reference

| Variable | Description | Source |
|----------|-------------|--------|
| `{{primary_keyword}}` | Main keyword | User input |
| `{{search_intent}}` | Intent classification | Research Agent |
| `{{paa_questions}}` | PAA questions from SERP | Research Agent |
| `{{missing_faqs}}` | Gap analysis FAQs | Research Agent |
| `{{article_summary}}` | Brief summary of article content | Writing Agent context |
| `{{faq_count}}` | Number of FAQs to generate (min 5) | Outline Agent |
