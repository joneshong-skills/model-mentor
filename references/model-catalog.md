# Model Catalog

> **last_updated**: 2026-02-11
> **next_review**: 2026-03-11

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

### Gemini 2.0 Flash
- **Tier**: Previous generation (still available)
- **Input**: ~$0.10/1M
- **Output**: ~$0.40/1M
- **Context**: 1M tokens
- **Cost tier**: $
- **Latency**: Fast
- **Strengths**: Even cheaper than 2.5 Flash
- **Weaknesses**: Superseded by 2.5 Flash in most benchmarks
- **Best for**: Legacy workloads, extreme cost optimization where quality is secondary

---

## Open Source / Alternative Providers

### DeepSeek R1
- **Tier**: Reasoning specialist (open-source)
- **Input**: $0.55/1M
- **Output**: $2.19/1M
- **Context**: 128K tokens
- **Cost tier**: $
- **Latency**: Variable
- **Strengths**: Strong chain-of-thought reasoning, competitive with o3 on many benchmarks, can self-host
- **Weaknesses**: Inconsistent on creative tasks, limited multimodal, self-hosting requires significant GPU resources
- **Best for**: Cost-effective reasoning tasks, self-hosted inference, math and logic

### DeepSeek V3.2
- **Tier**: General-purpose (open-source)
- **Input**: $0.28/1M
- **Output**: $0.42/1M
- **Context**: 128K tokens
- **Cost tier**: $ (cheapest quality option)
- **Latency**: Fast
- **Strengths**: Extremely cheap, surprisingly good quality for price, can self-host
- **Weaknesses**: Less reliable on complex tasks, limited tool use support
- **Best for**: Budget bulk processing, self-hosted deployment, cost-sensitive applications

### Meta Llama 4 Maverick
- **Tier**: Open-source flagship
- **Input**: $0.27/1M (via providers)
- **Output**: $0.85/1M
- **Context**: 1M tokens
- **Cost tier**: $
- **Latency**: Fast (provider-dependent)
- **Strengths**: Open-source, 1M context, 400B parameters, can self-host, strong community
- **Weaknesses**: Requires significant compute to self-host, quality varies by provider
- **Best for**: Self-hosted enterprise, privacy-sensitive applications, large-context budget option

### Mistral Medium 3
- **Tier**: European mid-range
- **Input**: $0.40/1M
- **Output**: $2.00/1M
- **Context**: 131K+ tokens
- **Strengths**: EU data residency, sliding window attention, competitive quality
- **Weaknesses**: Smaller ecosystem, less community tooling
- **Best for**: EU compliance requirements, moderate-complexity tasks

---

## Embeddings Models

| Model | Price/1M tokens | Dimensions | Notes |
|-------|----------------|------------|-------|
| text-embedding-3-large (OpenAI) | $0.13 | 3072 | Best quality from OpenAI |
| text-embedding-3-small (OpenAI) | $0.02 | 1536 | Budget option |
| Voyage 3.5 (Voyage AI) | $0.06 | 1024 | Excellent for code search |
| Gemini text-embedding-004 | Free tier available | 768 | Good for getting started |

---

## Cost Comparison Matrix (1M input + 1M output)

| Model | Total Cost | Quality Tier | Speed |
|-------|-----------|-------------|-------|
| DeepSeek V3.2 | $0.70 | Good | Fast |
| GPT-4o-mini | $0.75 | Good | Fast |
| Gemini 2.5 Flash | $0.75 | Good | Fast |
| Llama 4 Maverick | $1.12 | Good | Fast |
| GPT-4.1 mini | $2.00 | Good+ | Fast |
| o3 (base) | $2.00 | Excellent (reasoning) | Variable |
| DeepSeek R1 | $2.74 | Good+ (reasoning) | Variable |
| Gemini 2.5 Pro | $11.25 | Excellent | Medium |
| GPT-4o | $12.50 | Excellent | Medium |
| GPT-4.1 | $10.00 | Excellent | Medium |
| Claude Sonnet 4.5 | $18.00 | Excellent | Medium |
| Claude Opus 4.6 | $30.00 | Best | Slow |

---

## Changelog

### 2026-02-11
- Initial catalog creation
- Added all major providers: Anthropic, OpenAI, Google, DeepSeek, Meta, Mistral
- Pricing verified via official documentation and aggregators
