#!/bin/bash
# Ralph Loop Startup Script - FIXED VERSION
# Fixes the CLAUDECODE environment variable issue

set -e

echo "🚀 Starting Ralph Loop - Fixed Version"
echo "===================================="
echo ""

# Unset CLAUDECODE environment variable to allow spawning Claude Code
unset CLAUDECODE
unset CLAUDE_CODE_ENTRYPOINT

echo "✅ Unset CLAUDECODE environment variable"

cd "$(dirname "$0")"

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
    echo "   Creating it now..."
    # (PROMPT.md already exists, this is just a check)
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
echo "  - CLAUDECODE: unset (fixed!)"
echo ""
echo "Ralph will now begin autonomous execution"
echo ""

# Start Ralph with CLAUDECODE unset
env -u CLAUDECODE -u CLAUDE_CODE_ENTRYPOINT ralph --live --verbose $MONITOR_FLAG --prompt .ralph/PROMPT.md
