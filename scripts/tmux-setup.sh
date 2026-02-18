#!/bin/bash
# scripts/tmux-setup.sh - Setup tmux session for parallel agents

SESSION="ai-sdk-projects"

# Kill existing session if exists
tmux kill-session -t $SESSION 2>/dev/null || true

# Create new session
tmux new-session -d -s $SESSION -n orchestrator

# Create windows for each project
for i in {1..10}; do
  tmux new-window -t $SESSION:$i -n "agent-$i"
done

# Select window 0
tmux select-window -t $SESSION:0

echo "tmux session '$SESSION' created with 11 windows"
echo "Attach with: tmux attach -t $SESSION"
echo "Switch windows: Ctrl+B [number]"
