#!/bin/bash
# Ralph Loop Startup Script - z.ai API (GLM 4.7 Compatible)
# Uses custom Anthropic base URL and API key

set -e

echo "🚀 Starting Ralph Loop with z.ai API"
echo "======================================="
echo ""

# Unset CLAUDECODE environment variable to allow spawning Claude Code
unset CLAUDECODE
unset CLAUDE_CODE_ENTRYPOINT

# z.ai API Configuration
export ANTHROPIC_BASE_URL="https://api.z.ai/api/anthropic"
export ANTHROPIC_API_KEY="b58d7ad0c5544e0da85fa8c63e5a8519.S8lpuYo8dCMjcUlU"

echo "✅ Configured z.ai API endpoint:"
echo "   Base URL: $ANTHROPIC_BASE_URL"
echo "   API Key: ${ANTHROPIC_API_KEY:0:20}..."
echo ""

cd "$(dirname "$0")"

# Verify API key is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ERROR: ANTHROPIC_API_KEY not set"
    exit 1
fi

# Check if Ralph is installed
if ! command -v ralph &> /dev/null; then
    echo "❌ ERROR: Ralph Loop not found"
    echo "   Install it first:"
    echo "   curl -fsSL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/install.sh | bash"
    exit 1
fi

# Verify PROMPT.md exists
if [ ! -f ".ralph/PROMPT.md" ]; then
    echo "❌ ERROR: .ralph/PROMPT.md not found"
    exit 1
fi

# Check if tmux is installed
if command -v tmux &> /dev/null; then
    MONITOR_FLAG="--monitor"
    echo "✅ tmux found, monitoring enabled"
else
    echo "⚠️  WARNING: tmux not found, running without --monitor flag"
    MONITOR_FLAG=""
fi

echo "✅ Environment checks passed"
echo ""
echo "Starting Ralph Loop with:"
echo "  - Prompt: .ralph/PROMPT.md"
echo "  - Monitor: $([ -n "$MONITOR_FLAG" ] && echo "enabled (tmux)" || echo "disabled")"
echo "  - Live output: enabled"
echo "  - Verbose: enabled"
echo "  - API: z.ai (GLM 4.7 compatible)"
echo "  - Base URL: $ANTHROPIC_BASE_URL"
echo ""

# Test API connection
echo "🧪 Testing API connection..."
echo ""

# Start Ralph with z.ai API configuration
env -u CLAUDECODE -u CLAUDE_CODE_ENTRYPOINT \
    ANTHROPIC_BASE_URL="$ANTHROPIC_BASE_URL" \
    ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
    ralph --live --verbose $MONITOR_FLAG --prompt .ralph/PROMPT.md
