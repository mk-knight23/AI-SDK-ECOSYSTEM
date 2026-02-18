#!/bin/bash
# Check Ralph Loop Progress

echo "🤖 Ralph Loop Progress Monitor"
echo "==============================="
echo ""

cd "$(dirname "$0")"

# Check if Ralph is running
if pgrep -f "ralph --prompt" > /dev/null; then
    echo "✅ Ralph Loop is RUNNING"
    echo ""
else
    echo "⏸️  Ralph Loop is NOT running"
    echo ""
fi

# Show status
echo "📊 Current Status:"
echo "─────────────────"
if [ -f ".ralph/status.json" ]; then
    cat .ralph/status.json | jq '.' 2>/dev/null || cat .ralph/status.json
else
    echo "No status file found"
fi

echo ""

# Show recent handoffs
echo "📝 Recent Handoffs:"
echo "──────────────────"
if [ -d ".ralph/handoffs" ]; then
    ls -lt .ralph/handoffs/*.md 2>/dev/null | head -5 || echo "No handoffs yet"
else
    echo "No handoffs directory"
fi

echo ""

# Show recent logs
echo "📋 Recent Logs (last 10 lines):"
echo "────────────────────────────────"
if [ -f ".ralph/logs/ralph.log" ]; then
    tail -10 .ralph/logs/ralph.log
else
    echo "No log file found"
fi

echo ""

# Show project status if available
echo "🎯 Project Status:"
echo "──────────────────"
if [ -f ".ralph/status.json" ]; then
    cat .ralph/status.json | jq -r '.projects // "No projects yet"' 2>/dev/null
fi

echo ""
echo "💡 Commands:"
echo "   - Attach to tmux:  tmux attach -t ai-sdk-projects"
echo "   - Watch logs:      tail -f .ralph/logs/ralph.log"
echo "   - Full status:     cat .ralph/status.json | jq"
