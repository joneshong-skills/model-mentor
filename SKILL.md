---
name: model-mentor
description: >-
  This skill should be used when the user asks to "recommend a model",
  "推薦模型", "哪個模型適合", "which model should I use",
  "模型比較", "model comparison", "最新模型有哪些",
  "我要做 X 用什麼模型", "推薦 CLI", "哪個 CLI 好用",
  mentions choosing an LLM or coding CLI tool, or discusses
  selecting AI models or CLI tools for specific tasks.
version: 0.1.1
tools: Read, WebSearch
argument-hint: <task description or "update" to refresh catalog>
---

# Model Mentor

Recommend the most cost-effective LLM model or coding CLI tool for a given task.
Recommendations balance capability, price, speed, and task fit — not just raw benchmarks or lowest cost.
Covers both API models (for building applications) and CLI tools (for developer workflows).

## Agent Delegation

Delegate model comparison research and catalog refresh tasks to the `researcher` agent to keep main context lean during multi-model lookups.

```
Main context (task classification + final recommendation)
  └─ Task(subagent_type: researcher, prompt: "Search for the latest benchmarks and pricing for {model A} vs {model B} as of 2026. Return ONLY a comparison table: pricing, context window, key strengths, key weaknesses.")
  └─ Task(subagent_type: researcher, prompt: "Find new LLM model announcements from Anthropic, OpenAI, and Google in the last 30 days. Return ONLY model name, release date, and one-line capability summary per model.")
```

## Core Philosophy

- **CP Value First**: The best model is not the most expensive or the fastest — it is the one
  that delivers the required quality at the lowest total cost for the specific task.
- **No Absolutes**: Always present a primary recommendation with 1-2 alternatives.
  Different contexts (budget, latency, privacy) can shift the best choice.
- **Fresh Data**: Model landscape changes rapidly. When uncertain about latest models or pricing,
  perform a web search before recommending.

## Workflow

### Mode A: Task Recommendation (Default)

When the user describes a task (e.g., "我要寫一個 REST API", "幫我分析 100 頁 PDF"):

1. **Classify the task** into one or more categories from the Quick Reference table below.
2. **Read the model catalog** at `references/model-catalog.md` for current model data.
3. **Select primary recommendation** based on:
   - Task category match (which models excel here)
   - CP value tier (prefer mid-tier if quality is sufficient)
   - Context window needs (long doc → need large context)
   - Latency requirements (real-time chat → need fast model)
   - Multimodal needs (image/video/audio input → need multimodal model)
4. **Present the recommendation** using this format:

```
### Recommendation: [Primary Model]

**Why**: [1-2 sentence reason tied to the specific task]
**Estimated cost tier**: [$ / $$ / $$$]
**Latency**: [Fast / Medium / Slow]

#### Alternatives
| Model | When to prefer | Trade-off |
|-------|---------------|-----------|
| Alt 1 | [scenario]    | [what changes] |
| Alt 2 | [scenario]    | [what changes] |

> Note: [any caveats or context-dependent factors]
```

5. **If uncertain about a model's current capability or pricing**, run a quick web search
   before finalizing the recommendation. Do NOT guess pricing.

### Mode B: Catalog Update

When the user says "update", "更新模型資料", "check latest models", or similar:

1. **Search for latest model releases** using web search:
   - Query: `"latest LLM model releases 2026"` or `"新 AI 模型發布 2026"`
   - Query: `"[provider] new model announcement"` for specific providers
2. **Compare findings** against `references/model-catalog.md`.
3. **Update the catalog** with new models, pricing changes, or capability updates.
4. **Summarize changes** to the user.

### Mode C: Model Comparison

When the user asks to compare specific models (e.g., "Claude Sonnet vs GPT-4o"):

1. Read catalog data for both models.
2. If data is stale or missing, web search for latest benchmarks and pricing.
3. Present a side-by-side comparison table covering:
   - Pricing (input/output per 1M tokens)
   - Context window
   - Key strengths
   - Key weaknesses
   - Best use cases
4. End with a situational recommendation, not a blanket winner.

### Mode D: CLI Tool Recommendation

When the user asks about coding CLI tools (e.g., "我該用哪個 CLI", "Claude Code 還是 Codex"):

1. **Read the CLI comparison** at `references/cli-comparison.md`.
2. **Identify the user's primary workflow**:
   - Interactive coding with frequent back-and-forth → Claude Code
   - Long autonomous tasks, set-and-forget → Codex CLI
   - Large codebase exploration, budget-constrained → Gemini CLI
   - Heavy MCP/tool integrations → Claude Code
3. **Present recommendation** with the same format as Mode A.
4. **Note**: CLI tools and API models are different concerns. A user may use Claude Code (CLI)
   but call Gemini API for long-document analysis. Recommend combinations when appropriate.

## Task Categories Quick Reference

Common patterns — for full cost data and CP value analysis, see `references/model-catalog.md`.

| Category | Primary Pick | Budget Pick |
|----------|-------------|-------------|
| **Code Gen / Review / Debug** | Claude Sonnet 4.5 | Gemini 2.5 Flash |
| **Math / Reasoning** | o3 | GPT-4.1 mini |
| **Long Doc / Image / Video** | Gemini 2.5 Pro | Gemini 2.5 Flash |
| **Creative Writing** | Claude Opus 4.6 | Claude Sonnet 4.5 |
| **Real-time Chat** | GPT-4o-mini | Gemini 2.5 Flash |
| **Agentic / Multi-step** | Claude Opus 4.6 | Claude Sonnet 4.5 |
| **Structured Output / JSON** | GPT-4.1 | GPT-4.1-mini |

## Decision Factors

When the quick reference table does not clearly resolve the choice, apply these tiebreakers:

1. **Budget constrained** → Lean toward Flash/Haiku/mini models. Often 90% of the quality at 10% of the cost.
2. **Latency critical** → Prefer Flash/Haiku/mini. Larger models add seconds of latency.
3. **Accuracy critical** → Upgrade to the Power Pick. The cost difference is worth it for high-stakes tasks.
4. **Privacy / Compliance** → Check provider data policies. Some enterprises require specific providers.
5. **Context window** → If input exceeds 128K tokens, Gemini (1M-2M) is often the only viable option.
6. **Multimodal input** → Gemini leads in video; all three handle images well.
7. **Tool use / Function calling** → OpenAI has the most mature function calling API; Claude is catching up.

## Pricing Awareness

Do NOT memorize exact pricing — it changes frequently. Instead:

- Maintain approximate tiers in `references/model-catalog.md`
- When a recommendation hinges on pricing, verify via web search
- Always frame cost as relative tiers ($/$$/$$$$) rather than exact numbers

## Freshness Policy

The model catalog (`references/model-catalog.md`) should be refreshed:

- When the user explicitly asks for updates
- When making a recommendation and the catalog's `last_updated` date is older than 30 days
- When the user mentions a model not in the catalog

To refresh, use the smart-search skill or direct web search to find:
1. New model announcements from Anthropic, OpenAI, and Google
2. Pricing changes
3. Notable community benchmarks or evaluations
4. CLI tool updates (Claude Code, Codex CLI, Gemini CLI)

## Important Notes

- The catalog in `references/model-catalog.md` is a living document — update it as new data arrives.
- Recommendations are guidance, not gospel. Always mention that the user's specific context matters.
- For niche tasks (e.g., medical, legal, specific languages), note that specialized fine-tuned models may outperform general-purpose ones.
- When a task spans multiple categories, weight the most demanding subtask highest.

## Continuous Improvement

This skill evolves with each use. After every invocation:

1. **Reflect** — Identify what worked, what caused friction, and any unexpected issues
2. **Record** — Append a concise lesson to `lessons.md` in this skill's directory
3. **Refine** — When a pattern recurs (2+ times), update SKILL.md directly

### lessons.md Entry Format

```
### YYYY-MM-DD — Brief title
- **Friction**: What went wrong or was suboptimal
- **Fix**: How it was resolved
- **Rule**: Generalizable takeaway for future invocations
```

Accumulated lessons signal when to run `/skill-optimizer` for a deeper structural review.

## Additional Resources

### Reference Files
- **`references/model-catalog.md`** — Detailed model catalog with capabilities, pricing tiers, context windows, and last-updated timestamps
- **`references/cli-comparison.md`** — Claude Code, Codex CLI, Gemini CLI feature comparison, strengths, weaknesses, and CP-value recommendations
