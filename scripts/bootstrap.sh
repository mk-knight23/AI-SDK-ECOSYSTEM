#!/bin/bash
# scripts/bootstrap.sh - Bootstrap all 10 projects

set -e

PROJECTS=(
  "01:venture-graph:LangGraph venture planning:Next.js 15 + FastAPI"
  "02:omni-desk:LangChain enterprise RAG:React 19 + FastAPI"
  "03:dev-squad:OpenAI SDK dev team:SvelteKit + Node.js"
  "04:supply-consensus:AutoGen supply chain:Vue 3 + .NET 9"
  "05:market-pulse:Google ADK competitor intel:Angular 19 + Go"
  "06:insight-stream:Vercel AI SDK streaming:Next.js 15 RSC"
  "07:research-synthesis:LlamaIndex knowledge graph:Remix + Python"
  "08:trend-factory:CrewAI marketing crew:Nuxt 3 + Django"
  "09:patent-iq:Haystack patent search:Astro 5 + Flask"
  "10:claude-forge:Claude SDK coding agent:T3 Stack + Python"
)

echo "Creating git worktrees..."

for proj in "${PROJECTS[@]}"; do
  IFS=':' read -r num name desc stack <<< "$proj"
  branch="feat/$name"

  # Create branch if doesn't exist
  git branch "$branch" 2>/dev/null || true

  # Create worktree
  git worktree add "projects/$num-$name" "$branch"

  echo "Created: projects/$num-$name"
done

echo "All worktrees created!"
echo "Next: Create tmux session with 'scripts/tmux-setup.sh'"
