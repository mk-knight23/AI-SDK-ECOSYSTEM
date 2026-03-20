#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RUNNER="$ROOT/ecosystem_runner.py"

for fw in langchain langgraph openai; do
  echo "=== ecosystem:$fw ==="
  python3 "$RUNNER" --framework "$fw" | sed -n '1,10p'
done

echo "Ecosystem smoke checks passed."
