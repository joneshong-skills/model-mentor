# Model Catalog (Paid Providers Only)

> **last_updated**: 2026-02-11
> **next_review**: 2026-03-11
> **scope**: Anthropic, OpenAI, Google only (user has paid subscriptions for all three)

## Anthropic Claude

### Claude Opus 4.6
- **Tier**: Flagship
- **Input**: $5.00/1M (≤200K) · $10.00/1M (>200K)
- **Output**: $25.00/1M (≤200K) · $37.50/1M (>200K)
- **Context**: 200K tokens
- **Cost tier**: $$$
- **Latency**: Slow
- **Strengths**: Best-in-class code generation, complex multi-step reasoning, agentic tasks, instruction following, creative writing, nuanced analysis
- **Weaknesses**: Expensive, high latency, overkill for simple tasks
- **Best for**: Production-critical code, architecture decisions, long-form writing, complex agentic workflows
- **Batch API**: 50% off

### Claude Sonnet 4.5
- **Tier**: Mid-range (best value)
- **Input**: $3.00/1M
- **Output**: $15.00/1M
- **Context**: 200K tokens
- **Cost tier**: $$
- **Latency**: Medium
- **Strengths**: Excellent code quality (close to Opus), fast enough for interactive use, good instruction following, strong reasoning
- **Weaknesses**: Slightly less nuanced than Opus on edge cases, creative writing slightly below Opus
- **Best for**: Daily coding, PR reviews, debugging, general development tasks, RAG applications
- **Batch API**: 50% off
- **Note**: The CP-value king of the Claude family. Covers 80%+ of coding tasks at 60% the cost of Opus.

### Claude Haiku 4.5
- **Tier**: Lightweight
- **Input**: $1.00/1M
- **Output**: $5.00/1M
- **Context**: 200K tokens
- **Cost tier**: $
- **Latency**: Fast
- **Strengths**: Very fast responses, cost-effective for high volume, good for classification and simple Q&A
- **Weaknesses**: Noticeably less capable on complex reasoning, code quality drops on large tasks
- **Best for**: Classification, routing, simple Q&A, high-throughput pipelines, quick summaries

---

## OpenAI

### o3
- **Tier**: Reasoning specialist
- **Input**: $0.40/1M (estimated, reasoning model pricing varies)
- **Output**: $1.60/1M
- **Context**: 200K tokens
- **Cost tier**: $ (but reasoning tokens can inflate actual cost)
- **Latency**: Variable (depends on reasoning depth)
- **Strengths**: Exceptional at math, logic puzzles, scientific reasoning, step-by-step problem solving
- **Weaknesses**: Reasoning token overhead can make actual cost unpredictable, not ideal for creative tasks, can be slow on deep reasoning chains
- **Best for**: Math competitions, scientific analysis, complex logic problems, formal verification
- **Note**: Actual cost depends heavily on reasoning token usage. Simple queries are cheap; complex reasoning can be expensive.

### GPT-4.1
- **Tier**: General-purpose flagship
- **Input**: $2.00/1M
- **Output**: $8.00/1M
- **Context**: 1M tokens
- **Cost tier**: $$
- **Latency**: Medium
- **Strengths**: Most mature function calling/tool use, excellent structured output (JSON), good translation, broad knowledge base, largest context in OpenAI lineup
- **Weaknesses**: Code quality slightly below Claude Sonnet, can be verbose, sometimes "lazy" on long outputs
- **Best for**: API integrations, tool use workflows, structured data extraction, translation, enterprise applications
- **Cached input**: $0.50/1M (75% off)

### GPT-4.1 mini
- **Tier**: Budget general-purpose
- **Input**: $0.40/1M
- **Output**: $1.60/1M
- **Context**: 1M tokens
- **Cost tier**: $
- **Latency**: Fast
- **Strengths**: Same API as GPT-4.1 at much lower cost, good for moderate-complexity tasks, function calling support
- **Weaknesses**: Quality noticeably drops on complex reasoning and nuanced tasks
- **Best for**: Budget-friendly API calls, moderate-complexity structured output, quick tool use

### GPT-4o
- **Tier**: Multimodal flagship
- **Input**: $2.50/1M
- **Output**: $10.00/1M
- **Context**: 128K tokens
- **Cost tier**: $$
- **Latency**: Medium
- **Strengths**: Strong multimodal (image + audio), real-time voice mode, good general performance
- **Weaknesses**: Pricing higher than GPT-4.1 for text-only tasks, 128K context is smaller
- **Best for**: Image analysis, voice applications, multimodal workflows

### GPT-4o-mini
- **Tier**: Budget multimodal
- **Input**: $0.15/1M
- **Output**: $0.60/1M
- **Context**: 128K tokens
- **Cost tier**: $
- **Latency**: Fast
- **Strengths**: Extremely cheap, fast, decent quality for simple tasks, multimodal support
- **Weaknesses**: Quality drops significantly on complex tasks, weaker reasoning
- **Best for**: High-volume simple tasks, chatbots, quick image descriptions, classification at scale

---

## Google Gemini

### Gemini 2.5 Pro
- **Tier**: Flagship
- **Input**: $1.25/1M (<200K) · $2.50/1M (≥200K)
- **Output**: $10.00/1M
- **Context**: 2M tokens (largest in industry)
- **Cost tier**: $$
- **Latency**: Medium-Slow
- **Strengths**: Massive 2M context window, best-in-class video understanding, strong image analysis, native Google Search integration, competitive code generation
- **Weaknesses**: Instruction following can be inconsistent on complex prompts, higher hallucination rate in some benchmarks, API ecosystem less mature than OpenAI
- **Best for**: Ultra-long document analysis, video understanding, multimodal analysis, large codebase comprehension
- **Note**: The go-to model when context window size matters. Nothing else offers 2M tokens.

### Gemini 2.5 Flash
- **Tier**: Fast & efficient
- **Input**: $0.15/1M
- **Output**: $0.60/1M
- **Context**: 1M tokens
- **Cost tier**: $
- **Latency**: Fast
- **Strengths**: Extremely cost-effective, fast, 1M context, good multimodal support, surprisingly capable for its price
- **Weaknesses**: Less accurate on complex reasoning, creative writing quality lower
- **Best for**: High-volume processing, data extraction, classification, quick summaries, budget-friendly long-document analysis
- **Note**: Ties with GPT-4o-mini as the cheapest quality option. 1M context gives it an edge for long docs.

---

## Embeddings Models

| Model | Price/1M tokens | Dimensions | Notes |
|-------|----------------|------------|-------|
| text-embedding-3-large (OpenAI) | $0.13 | 3072 | Best quality |
| text-embedding-3-small (OpenAI) | $0.02 | 1536 | Budget option |
| Gemini text-embedding-004 | Free tier available | 768 | Good for getting started |

---

## Cost Comparison Matrix (1M input + 1M output)

| Model | Total Cost | Quality Tier | Speed | Best CP Value For |
|-------|-----------|-------------|-------|-------------------|
| GPT-4o-mini | $0.75 | Good | Fast | High-volume simple tasks |
| Gemini 2.5 Flash | $0.75 | Good | Fast | Long docs on a budget |
| GPT-4.1 mini | $2.00 | Good+ | Fast | Structured output on a budget |
| o3 (base) | $2.00* | Excellent (reasoning) | Variable | Math & logic (*reasoning tokens extra) |
| Claude Haiku 4.5 | $6.00 | Good+ | Fast | Classification & routing |
| GPT-4.1 | $10.00 | Excellent | Medium | Tool use & structured output |
| Gemini 2.5 Pro | $11.25 | Excellent | Medium | Ultra-long docs & video |
| GPT-4o | $12.50 | Excellent | Medium | Multimodal (image+audio) |
| Claude Sonnet 4.5 | $18.00 | Excellent | Medium | Code quality & daily dev |
| Claude Opus 4.6 | $30.00 | Best | Slow | Critical code & complex reasoning |

### CP Value Sweet Spots (Recommended defaults)

- **Cheapest usable**: GPT-4o-mini / Gemini 2.5 Flash ($0.75) — pick Flash if context > 128K
- **Best all-rounder**: Claude Sonnet 4.5 ($18) — highest code quality per dollar
- **Best for long docs**: Gemini 2.5 Pro ($11.25) — 2M context, no contest
- **Best for reasoning**: o3 ($2 base) — unmatched on math/logic
- **Best for tool use**: GPT-4.1 ($10) — most mature function calling
- **When quality is non-negotiable**: Claude Opus 4.6 ($30) — best overall but pricey

---

## Changelog

### 2026-02-11
- Initial catalog creation (full version on main branch)
- Overfit to paid providers: Anthropic, OpenAI, Google only
- Added CP Value Sweet Spots section
- Removed: DeepSeek, Meta Llama, Mistral, Voyage AI
