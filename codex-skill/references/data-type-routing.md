# Data Type Routing

Choose the smallest route that matches the input. Mixed projects can use multiple routes.

## Reviews and Social Content

Keep raw text, source URL, platform, product/entity, rating, publish time, and anonymized user key when present. Add tags for needs, pain points, sentiment, scenarios, personas, evidence strength, and suspected ads. Use conservative wording for weak signals.

## Surveys

Preserve question IDs, answer options, skip logic, respondent ID, timestamps, segments, and invalid-response flags. Report base size per question. Never merge or reorder questions unless explicitly requested.

## Interviews and Qualitative Notes

Preserve speaker/source, transcript excerpt, code, theme, confidence, and quote eligibility. Separate observed evidence from interpretation. Mark small-n patterns as hypotheses.

## Sales, CRM, and Operations Tables

Preserve entity keys, dates, currency/unit, period definitions, filters, and aggregation grain. Validate totals against source exports. State whether figures are revenue, volume, count, rate, or share.

## Competitive or Market Intelligence

Separate collected facts, inferred comparisons, and external assumptions. Track source date, source type, entity, metric definition, and citation/trace field. Do not turn sample differences into market-share claims without supporting market data.

## Product, Ticket, or Support Data

Preserve ticket IDs, categories, timestamps, severity, status, owner/team, and resolution fields. Avoid PII in deliverables. Use issue frequency plus severity/impact for prioritization.
