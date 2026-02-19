#!/bin/bash
# scripts/week3-bootstrap.sh
# Bootstrap Week 3: Start all 10 agents in tmux

PROJECTS=(
  "01-venture-graph"
  "02-omni-desk"
  "03-dev-squad"
  "04-supply-consensus"
  "05-market-pulse"
  "06-insight-stream"
  "07-research-synthesis"
  "08-trend-factory"
  "09-patent-iq"
  "10-claude-forge"
)

# Kill existing session if exists
tmux kill-session -t week3-saas 2>/dev/null

# Create new session
tmux new-session -d -s week3-saas -n orchestrator

# Create window for each project
for i in "${!PROJECTS[@]}"; do
  WINDOW=$((i + 1))
  PROJECT="${PROJECTS[$i]}"

  # Create new window
  tmux new-window -t week3-saas:$WINDOW -n $PROJECT

  # Navigate to project
  tmux send-keys -t week3-saas:$WINDOW "cd projects/$PROJECT && clear" Enter

  # Start Claude Code with environment
  tmux send-keys -t week3-saas:$WINDOW "export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1" Enter
  tmux send-keys -t week3-saas:$WINDOW "claude" Enter

  # Wait for Claude to start
  sleep 3
done

# Attach to session
tmux attach -t week3-saas

echo "Week 3 Agent Team started!"
echo "Switch between agents: Ctrl+B then window number (1-10)"
echo "Broadcast to all: Ctrl+B then :setw synchronize-panes on"
