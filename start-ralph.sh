#!/bin/bash
# Ralph Loop Startup Script
# Run this from terminal (NOT from Claude Code session)

set -e

echo "🚀 Starting Ralph Loop - Autonomous AI Developer"
echo "==============================================="
echo ""

cd "$(dirname "$0")"

# Check we're not in a Claude Code session
if [ -n "$CLAUDECODE" ]; then
    echo "❌ ERROR: Cannot start Ralph from within Claude Code session"
    echo "   Please run this script from a standard terminal"
    echo ""
    echo "   Exit Claude Code and run:"
    echo "   ./start-ralph.sh"
    exit 1
fi

# Verify Ralph is installed
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
    mkdir -p .ralph
    # (PROMPT.md already created, this is just a check)
fi

# Check if tmux is installed (required for --monitor flag)
if ! command -v tmux &> /dev/null; then
    echo "⚠️  WARNING: tmux not found, running without --monitor flag"
    echo "   Install tmux for session monitoring:"
    echo "   brew install tmux"
    echo ""
    MONITOR_FLAG=""
else
    MONITOR_FLAG="--monitor"
fi

echo "✅ Environment checks passed"
echo ""
echo "Starting Ralph Loop with:"
echo "  - Prompt: .ralph/PROMPT.md"
echo "  - Monitor: $([ -n "$MONITOR_FLAG" ] && echo "enabled (tmux)" || echo "disabled")"
echo "  - Live output: enabled"
echo "  - Verbose: enabled"
echo ""
echo "Ralph will now begin autonomous execution:"
echo "  1. Environment setup (Doppler, platforms)"
echo "  2. Monorepo bootstrap (worktrees, GitHub)"
echo "  3. Parallel scaffolding (all 10 projects)"
echo "  4. CI/CD setup"
echo "  5. Deployments (20 Hello World apps)"
echo "  6. Finalization (handoffs, docs)"
echo ""
echo "📊 Monitor progress:"
echo "   - Status:  cat .ralph/status.json | jq"
echo "   - Logs:    tail -f .ralph/logs/ralph.log"
echo "   - Tmux:    tmux attach -t ai-sdk-projects (if tmux enabled)"
echo ""
echo "💡 To stop Ralph:"
echo "   - Press Ctrl+C (graceful shutdown after current loop)"
echo "   - Or: pkill -f 'ralph --prompt'"
echo ""
echo "▶️  Starting Ralph Loop..."
echo "══════════════════════════════════════════"
echo ""

# Start Ralph
ralph --live --verbose $MONITOR_FLAG --prompt .ralph/PROMPT.md

# If Ralph exits, show status
echo ""
echo "══════════════════════════════════════════"
echo "Ralph Loop stopped"
echo ""
echo "Final status:"
cat .ralph/status.json 2>/dev/null || echo "No status file found"
echo ""
echo "Check handoffs: ls -la .ralph/handoffs/"
