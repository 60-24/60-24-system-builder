"""Command-line entry point."""
from __future__ import annotations

import argparse
from pathlib import Path

from .core import generate, load_intent


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate files from a validated JSON intent.")
    parser.add_argument("intent", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    manifest = generate(load_intent(args.intent), args.output)
    print(f"Generated {len(manifest['files'])} file(s) in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
