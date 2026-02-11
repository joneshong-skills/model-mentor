[English](README.md) | [繁體中文](README.zh.md)

# Model Mentor

A Claude Code skill that recommends the most cost-effective LLM model or coding CLI tool for a given task — balancing capability, price, speed, and task fit rather than just raw benchmarks.

## What It Does

Model Mentor operates in four modes depending on your request:

| Mode | Trigger | Output |
|---|---|---|
| Task Recommendation | Describe a task | Primary model + 2 alternatives with trade-offs |
| Catalog Update | "update models" | Web search for latest releases, update catalog |
| Model Comparison | "compare X vs Y" | Side-by-side table with situational recommendation |
| CLI Recommendation | "which CLI should I use" | Best CLI tool for your workflow |

**Key design principle:** CP value first. The best model is not the most expensive or the fastest — it is the one that delivers the required quality at the lowest total cost for the specific task.

### Task Categories Quick Reference

| Category | Primary Pick | Budget Pick |
|---|---|---|
| Code Gen / Review / Debug | Claude Sonnet 4.5 | Gemini 2.5 Flash |
| Math / Reasoning | o3 | GPT-4.1 mini |
| Long Doc / Image / Video | Gemini 2.5 Pro | Gemini 2.5 Flash |
| Creative Writing | Claude Opus 4.6 | Claude Sonnet 4.5 |
| Real-time Chat | GPT-4o-mini | Gemini 2.5 Flash |
| Agentic / Multi-step | Claude Opus 4.6 | Claude Sonnet 4.5 |

## Installation

1. Clone this repository into your Claude skills directory:

   ```bash
   git clone https://github.com/joneshong-skills/model-mentor.git ~/.claude/skills/model-mentor
   ```

2. Prerequisites:
   - Web search capability (for verifying latest model pricing and features)

3. The skill activates when you ask for model recommendations, comparisons, or CLI tool advice, or use trigger phrases like "recommend a model", "which model", "compare models", etc.

## Usage

Just ask Claude naturally. Examples:

- *"I need to build a REST API — which model should I use?"*
- *"Compare Claude Sonnet 4.5 vs Gemini 2.5 Pro for code review"*
- *"Which CLI is best for long autonomous coding tasks?"*
- *"Update the model catalog with the latest releases"*

## Project Structure

```
model-mentor/
├── SKILL.md                        # Skill definition, workflow, and decision logic
├── README.md                       # This file
└── references/
    ├── model-catalog.md            # Model capabilities, pricing tiers, and context windows
    └── cli-comparison.md           # Claude Code, Codex CLI, Gemini CLI comparison
```

## License

MIT
