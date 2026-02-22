#!/usr/bin/env python3
"""Load model catalog and check freshness.

Usage:
  python3 load_catalog.py --check          # Check if catalog is stale (>30 days)
  python3 load_catalog.py --list           # List all models
  python3 load_catalog.py --recommend TASK # Quick task→model lookup
"""

import argparse
import os
import re
import sys
from datetime import date, datetime

CATALOG_PATH = os.path.expanduser(
    "~/.claude/skills/model-mentor/references/model-catalog.md"
)
CLI_PATH = os.path.expanduser(
    "~/.claude/skills/model-mentor/references/cli-comparison.md"
)
STALENESS_DAYS = 30

# Task keyword → (primary_model, reason)
QUICK_RECOMMEND_MAP = {
    # Coding & development
    "code": ("Claude Sonnet 4.5", "Best code quality per dollar; covers 80%+ coding tasks"),
    "coding": ("Claude Sonnet 4.5", "Best code quality per dollar; covers 80%+ coding tasks"),
    "debug": ("Claude Sonnet 4.5", "Strong reasoning + code quality; ideal for debugging"),
    "refactor": ("Claude Sonnet 4.5", "Excellent multi-file understanding"),
    "review": ("Claude Sonnet 4.5", "Strong instruction following + reasoning"),
    "architecture": ("Claude Opus 4.6", "Complex multi-step reasoning; non-negotiable quality"),
    "security": ("Claude Opus 4.6", "Critical tasks — best-in-class analysis"),
    # Reasoning & math
    "math": ("o3", "Unmatched on math/logic; purpose-built reasoning model"),
    "logic": ("o3", "Best at formal logic and step-by-step problem solving"),
    "reasoning": ("o3", "Exceptional reasoning chains; low base cost"),
    "science": ("o3", "Scientific analysis and formal verification"),
    # Long documents & context
    "long": ("Gemini 2.5 Pro", "2M token context — no other model comes close"),
    "document": ("Gemini 2.5 Pro", "Ultra-long document analysis at reasonable cost"),
    "video": ("Gemini 2.5 Pro", "Best-in-class video understanding"),
    "multimodal": ("GPT-4o", "Strong image + audio; real-time voice mode"),
    "image": ("GPT-4o", "Strong multimodal performance with image analysis"),
    "voice": ("GPT-4o", "Real-time voice mode support"),
    # Structured output & API
    "tool": ("GPT-4.1", "Most mature function calling / tool use ecosystem"),
    "function": ("GPT-4.1", "Best structured output and JSON reliability"),
    "api": ("GPT-4.1", "Enterprise-grade API integrations; 1M context"),
    "json": ("GPT-4.1", "Best structured data extraction"),
    "translation": ("GPT-4.1", "Broad knowledge base; reliable translation"),
    # Classification & high-volume
    "classify": ("GPT-4o-mini", "Cheapest quality option; fast classification at scale"),
    "classification": ("GPT-4o-mini", "Cheapest quality option; fast at scale"),
    "summarize": ("Gemini 2.5 Flash", "Cost-effective + 1M context for long doc summaries"),
    "summary": ("Gemini 2.5 Flash", "Cost-effective + 1M context for long doc summaries"),
    "routing": ("Claude Haiku 4.5", "Very fast; cost-effective for routing pipelines"),
    "pipeline": ("Claude Haiku 4.5", "High-throughput; cost-effective for pipelines"),
    # Writing
    "writing": ("Claude Opus 4.6", "Best creative writing; nuanced long-form"),
    "creative": ("Claude Opus 4.6", "Best creative writing and nuanced analysis"),
    "essay": ("Claude Sonnet 4.5", "Strong writing at lower cost than Opus"),
    # Budget
    "budget": ("Gemini 2.5 Flash", "Ties with GPT-4o-mini as cheapest quality option"),
    "cheap": ("GPT-4o-mini", "Lowest cost per token at $0.75/1M in+out"),
    "free": ("Gemini CLI (free tier)", "1000 requests/day free — best for experimentation"),
}


def _read_file(path):
    """Read a file and return its content, or None on failure."""
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _parse_last_updated(content):
    """Extract last_updated date from markdown frontmatter-style comment.

    Looks for lines like:
        > **last_updated**: 2026-02-11
        last_updated: 2026-02-11

    Returns:
        date | None
    """
    patterns = [
        r"\*\*last_updated\*\*[:\s]+(\d{4}-\d{2}-\d{2})",
        r"last_updated[:\s]+(\d{4}-\d{2}-\d{2})",
    ]
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            try:
                return datetime.strptime(match.group(1), "%Y-%m-%d").date()
            except ValueError:
                continue
    return None


def check_freshness():
    """Parse last_updated from catalog, compare to today, warn if >30 days.

    Returns:
        dict with keys: last_updated (date|None), days_old (int|None),
                        is_stale (bool), message (str)
    """
    content = _read_file(CATALOG_PATH)
    if content is None:
        return {
            "last_updated": None,
            "days_old": None,
            "is_stale": True,
            "message": "Catalog file not found: {}".format(CATALOG_PATH),
        }

    last_updated = _parse_last_updated(content)
    if last_updated is None:
        return {
            "last_updated": None,
            "days_old": None,
            "is_stale": True,
            "message": "Could not parse last_updated from catalog.",
        }

    today = date.today()
    days_old = (today - last_updated).days
    is_stale = days_old > STALENESS_DAYS

    if is_stale:
        msg = "STALE: Catalog is {} days old (last updated {}). Consider refreshing.".format(
            days_old, last_updated
        )
    else:
        msg = "OK: Catalog is {} days old (last updated {}). Next review in {} days.".format(
            days_old, last_updated, STALENESS_DAYS - days_old
        )

    return {
        "last_updated": last_updated,
        "days_old": days_old,
        "is_stale": is_stale,
        "message": msg,
    }


def _parse_model_table(content):
    """Parse markdown table rows into list of dicts.

    Looks for lines like:
        | Model | Total Cost | Quality Tier | Speed | Best CP Value For |
        | ... | ... | ... | ... | ... |

    Returns:
        list of dict with keys matching table headers (lowercased, spaces→underscores)
    """
    rows = []
    in_table = False
    headers = []

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            in_table = False
            headers = []
            continue

        cells = [c.strip() for c in stripped.split("|") if c.strip()]

        # Separator row (e.g. |---|---|)
        if all(re.match(r"^-+$", c.replace(":", "")) for c in cells):
            continue

        if not headers:
            headers = [re.sub(r"\*+", "", c).strip().lower().replace(" ", "_") for c in cells]
            in_table = True
            continue

        if in_table and len(cells) >= len(headers):
            row = {}
            for i, h in enumerate(headers):
                row[h] = cells[i] if i < len(cells) else ""
            rows.append(row)

    return rows


def list_models():
    """Parse model table from catalog and display as formatted output."""
    content = _read_file(CATALOG_PATH)
    if content is None:
        print("Error: catalog not found: {}".format(CATALOG_PATH), file=sys.stderr)
        sys.exit(1)

    rows = _parse_model_table(content)
    if not rows:
        print("Warning: no table rows found in catalog.", file=sys.stderr)
        return

    # Filter to rows that look like model entries (have a model column)
    model_rows = [r for r in rows if "model" in r and r.get("model", "").strip()]

    if not model_rows:
        # Try a broader parse — just print what we have
        model_rows = rows

    col_widths = {}
    for row in model_rows:
        for k, v in row.items():
            col_widths[k] = max(col_widths.get(k, len(k)), len(v))

    keys = list(model_rows[0].keys()) if model_rows else []
    if not keys:
        print("No model data found.")
        return

    header = "  ".join(k.replace("_", " ").upper().ljust(col_widths[k]) for k in keys)
    print(header)
    print("-" * len(header))
    for row in model_rows:
        print("  ".join(row.get(k, "").ljust(col_widths[k]) for k in keys))


def quick_recommend(task):
    """Lookup task category in quick reference map, return recommendation.

    Args:
        task (str): Task keyword (e.g. 'code', 'math', 'translation').

    Returns:
        tuple(str, str) | None: (model_name, reason) or None if not found.
    """
    key = task.lower().strip()

    # Direct match
    if key in QUICK_RECOMMEND_MAP:
        return QUICK_RECOMMEND_MAP[key]

    # Partial match
    for map_key, value in QUICK_RECOMMEND_MAP.items():
        if key in map_key or map_key in key:
            return value

    return None


def main():
    parser = argparse.ArgumentParser(
        description="Load model catalog and check freshness.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--check",
        action="store_true",
        help="Check if catalog is stale (>30 days)",
    )
    group.add_argument("--list", action="store_true", help="List all models")
    group.add_argument(
        "--recommend",
        metavar="TASK",
        help="Quick task→model lookup (e.g. code, math, translation)",
    )

    args = parser.parse_args()

    if args.check:
        result = check_freshness()
        prefix = "WARNING" if result["is_stale"] else "INFO"
        print("[{}] {}".format(prefix, result["message"]))
        if result["is_stale"]:
            sys.exit(1)

    elif args.list:
        # Print freshness info first
        result = check_freshness()
        if result["is_stale"]:
            print("[WARNING] {}".format(result["message"]))
            print()
        list_models()

    elif args.recommend:
        result = quick_recommend(args.recommend)
        if result is None:
            print("No recommendation found for task: '{}'".format(args.recommend))
            print("Try one of: {}".format(", ".join(sorted(set(QUICK_RECOMMEND_MAP.keys())))))
            sys.exit(1)
        model, reason = result
        print("Task    : {}".format(args.recommend))
        print("Model   : {}".format(model))
        print("Reason  : {}".format(reason))


if __name__ == "__main__":
    main()
