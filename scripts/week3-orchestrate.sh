#!/bin/bash
# scripts/week3-orchestrate.sh
# Broadcast commands to all 10 agent tmux windows

SESSION="week3-saas"

case "$1" in
  "start-auth")
    echo "🔐 Broadcasting: Start authentication implementation..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start implementing authentication feature now" Enter
    done
    ;;

  "start-stripe")
    echo "💳 Broadcasting: Start Stripe billing..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start Stripe billing implementation now" Enter
    done
    ;;

  "start-ratelimit")
    echo "⚡ Broadcasting: Start rate limiting..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start rate limiting implementation now" Enter
    done
    ;;

  "start-dashboard")
    echo "📊 Broadcasting: Start user dashboards..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start user dashboard implementation now" Enter
    done
    ;;

  "start-apikeys")
    echo "🔑 Broadcasting: Start API key management..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start API key management implementation now" Enter
    done
    ;;

  "start-email")
    echo "📧 Broadcasting: Start email integration..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start email integration now" Enter
    done
    ;;

  "run-tests")
    echo "🧪 Broadcasting: Run all tests..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "npm test && npm run lint && npm run typecheck" Enter
    done
    ;;

  "handoff")
    echo "📝 Broadcasting: Create handoff documents..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "/dx:handoff" Enter
      sleep 2
    done
    ;;

  "status")
    echo "📊 Agent Status Check:"
    for i in {1..10}; do
      PROJECT=$(tmux display -p '#S - #W "#{=window_name}"' | grep "^$i:" | cut -d: -f2)
      STATUS=$(tmux capture-pane -t $SESSION:$i -p | tail -5)
      echo "Window $i ($PROJECT): $STATUS"
    done
    ;;

  *)
    echo "Usage: $0 {start-auth|start-stripe|start-ratelimit|start-dashboard|start-apikeys|start-email|run-tests|handoff|status}"
    exit 1
    ;;
esac
