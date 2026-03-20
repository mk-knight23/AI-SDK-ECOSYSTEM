#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
MISSION="orchestrate secure build and deployment"

adapters=(
  AI-SDK-LANGCHAIN
  AI-SDK-LANGGRAPH
  AI-SDK-LAMA-INDEX
  AI-SDK-OPENAI
  AI-SDK-ANTHROPIC
  AI-SDK-AUTOGEN
  AI-SDK-CREWAI
  AI-SDK-HAYSTACK
  AI-SDK-SEMANTIC-KERNEL
)

for a in "${adapters[@]}"; do
  echo "=== smoke:$a ==="
  python3 "$ROOT/$a/runner.py" --mission "$MISSION" >/tmp/${a}.log 2>&1 || {
    cat /tmp/${a}.log
    exit 1
  }
  sed -n '1,8p' /tmp/${a}.log
  if ! grep -Eq "verification|Verification" /tmp/${a}.log; then
    echo "Missing verification output for $a"
    exit 1
  fi
done

echo "All python adapter smoke checks passed."
