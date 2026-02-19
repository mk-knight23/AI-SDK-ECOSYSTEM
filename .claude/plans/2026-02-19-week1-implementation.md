# Week 1 Sprint Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Scaffold 10 AI SDK SaaS projects in parallel using git worktrees and tmux, with each reaching "Hello World" deployed status.

**Architecture:** Git worktrees provide isolation for 10 parallel agents. MCP server coordinates via task lists and messaging. Shared templates ensure consistency. tmux provides visual orchestration.

**Tech Stack:** tmux, claude-code-teams-mcp, Docker, GitHub Actions, Node.js, Python, Go, .NET

---

## Phase 1: Infrastructure Setup (Lead Agent)

### Task 1: Install claude-code-teams-mcp Server

**Files:**
- Create: `.mcp.json`

**Step 1: Create MCP configuration**

```json
{
  "mcpServers": {
    "claude-teams": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/cs50victor/claude-code-teams-mcp@v0.1.1", "claude-teams"],
      "env": {
        "CLAUDE_TEAMS_BACKENDS": "claude"
      }
    }
  }
}
```

**Step 2: Verify MCP server loads**

Run: `claude` (restart to load MCP)
Expected: No MCP errors in startup

**Step 3: Commit**

```bash
git add .mcp.json
git commit -m "chore: add claude-code-teams-mcp server config"
```

---

### Task 2: Create Infrastructure Templates Directory

**Files:**
- Create: `infrastructure/templates/docker/Dockerfile.node`
- Create: `infrastructure/templates/docker/Dockerfile.python`
- Create: `infrastructure/templates/docker/Dockerfile.go`
- Create: `infrastructure/templates/docker/Dockerfile.dotnet`

**Step 1: Create Node.js Dockerfile**

```dockerfile
# infrastructure/templates/docker/Dockerfile.node
FROM node:20-alpine AS base

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

**Step 2: Create Python Dockerfile**

```dockerfile
# infrastructure/templates/docker/Dockerfile.python
FROM python:3.12-slim AS base

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Step 3: Create Go Dockerfile**

```dockerfile
# infrastructure/templates/docker/Dockerfile.go
FROM golang:1.23-alpine AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -o main .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/main .

EXPOSE 8080

CMD ["./main"]
```

**Step 4: Create .NET Dockerfile**

```dockerfile
# infrastructure/templates/docker/Dockerfile.dotnet
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src
COPY . .
RUN dotnet restore
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .
EXPOSE 8080
ENTRYPOINT ["dotnet", "app.dll"]
```

**Step 5: Commit**

```bash
git add infrastructure/
git commit -m "chore: add Docker templates for all tech stacks"
```

---

### Task 3: Create CI/CD Workflow Template

**Files:**
- Create: `infrastructure/templates/.github/workflows/ci.yml`

**Step 1: Create reusable CI workflow**

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
        if: ${{ inputs.language == 'node' }}

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
        if: ${{ inputs.language == 'python' }}

      - name: Install dependencies
        run: npm ci
        if: ${{ inputs.language == 'node' }}

      - name: Lint
        run: npm run lint || echo "No lint script"

      - name: Type check
        run: npm run typecheck || echo "No typecheck script"

      - name: Test
        run: npm test || echo "No tests yet"

      - name: Build
        run: npm run build

      - name: Docker build
        run: docker build -t test-app .

  deploy:
    needs: quality
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        run: echo "Deploy step - platform specific"
```

**Step 2: Commit**

```bash
git add infrastructure/templates/.github/
git commit -m "chore: add CI/CD workflow template"
```

---

### Task 4: Create README Template

**Files:**
- Create: `infrastructure/templates/README.md`

**Step 1: Create README template**

```markdown
# {{PROJECT_NAME}}

{{PROJECT_TAGLINE}}

## Tech Stack

{{TECH_BADGES}}

## Quick Start

\`\`\`bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
\`\`\`

## Deployment

{{DEPLOYMENT_INSTRUCTIONS}}

## Architecture

![Architecture](docs/architecture.png)

## License

MIT
```

**Step 2: Commit**

```bash
git add infrastructure/templates/README.md
git commit -m "chore: add README template"
```

---

### Task 5: Create CLAUDE.md Template

**Files:**
- Create: `infrastructure/templates/CLAUDE.md`

**Step 1: Create CLAUDE.md template**

```markdown
# {{PROJECT_NAME}}

**Project:** {{PROJECT_NAME}} ({{SDK_FOCUS}} SaaS)
**SDK Focus:** {{SDK_DESCRIPTION}}
**Tech Stack:** {{TECH_STACK}}

## MANDATORY WORKFLOW

1. Superpowers → Brainstorm → Plan → TDD
2. ECC → /plan → /tdd → /code-review → /security-scan
3. UI/UX Pro Max → Apply design system
4. Claude-Tips → /dx:handoff before end of session

## AGENTS TO USE

- /architect for system design
- /tdd-guide for test-first implementation
- /security-reviewer before API key usage

## CURRENT SPRINT: Week {{WEEK}}

{{SPRINT_TASKS}}

## Deployment Target

{{DEPLOY_TARGET}}

## API Keys (Doppler)

{{API_KEYS}}
```

**Step 2: Commit**

```bash
git add infrastructure/templates/CLAUDE.md
git commit -m "chore: add CLAUDE.md template"
```

---

### Task 6: Create Bootstrap Script

**Files:**
- Create: `scripts/bootstrap.sh`

**Step 1: Create bootstrap script**

```bash
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
```

**Step 2: Make executable**

Run: `chmod +x scripts/bootstrap.sh`
Expected: No output (success)

**Step 3: Commit**

```bash
git add scripts/bootstrap.sh
git commit -m "feat: add bootstrap script for 10 project worktrees"
```

---

### Task 7: Create tmux Setup Script

**Files:**
- Create: `scripts/tmux-setup.sh`

**Step 1: Create tmux setup script**

```bash
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
```

**Step 2: Make executable**

Run: `chmod +x scripts/tmux-setup.sh`
Expected: No output (success)

**Step 3: Commit**

```bash
git add scripts/tmux-setup.sh
git commit -m "feat: add tmux setup script for agent orchestration"
```

---

### Task 8: Execute Bootstrap

**Step 1: Run bootstrap script**

Run: `./scripts/bootstrap.sh`
Expected: "All worktrees created!" message

**Step 2: Verify worktrees**

Run: `git worktree list`
Expected: 10 entries for projects/01-* through projects/10-*

**Step 3: Run tmux setup**

Run: `./scripts/tmux-setup.sh`
Expected: "tmux session 'ai-sdk-projects' created"

**Step 4: Commit bootstrap state**

```bash
git add .
git commit -m "chore: bootstrap 10 project worktrees"
```

---

### Task 9: Create Team via MCP

**Step 1: Create team**

Use tool: `team_create`
- team_name: "ai-sdk-projects"
- description: "10 AI SDK SaaS projects parallel scaffold"

**Step 2: Verify team created**

Use tool: `read_config`
Expected: Config shows team with no members yet

---

## Phase 2: Parallel Agent Scaffold (10 Agents)

### Task 10: Spawn Agent-01 (VentureGraph)

**Context:** Agent-01 works in `projects/01-venture-graph/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-01"
- agent_type: "full-stack"
- cwd: "projects/01-venture-graph"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold VentureGraph (Next.js 15 + FastAPI)"
- description: "Create Next.js 15 frontend, FastAPI backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Railway."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-01"
- content: "Start Task 1: Scaffold VentureGraph. Stack: Next.js 15 + FastAPI. Deploy to Railway. Report progress via task_update."

---

### Task 11: Spawn Agent-02 (OmniDesk)

**Context:** Agent-02 works in `projects/02-omni-desk/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-02"
- agent_type: "full-stack"
- cwd: "projects/02-omni-desk"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold OmniDesk (React 19 + FastAPI)"
- description: "Create React 19 frontend, FastAPI backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Render."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-02"
- content: "Start Task 2: Scaffold OmniDesk. Stack: React 19 + FastAPI. Deploy to Render. Report progress via task_update."

---

### Task 12: Spawn Agent-03 (DevSquad)

**Context:** Agent-03 works in `projects/03-dev-squad/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-03"
- agent_type: "full-stack"
- cwd: "projects/03-dev-squad"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold DevSquad (SvelteKit + Node.js)"
- description: "Create SvelteKit frontend/backend, /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Fly.io."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-03"
- content: "Start Task 3: Scaffold DevSquad. Stack: SvelteKit + Node.js. Deploy to Fly.io. Report progress via task_update."

---

### Task 13: Spawn Agent-04 (SupplyConsensus)

**Context:** Agent-04 works in `projects/04-supply-consensus/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-04"
- agent_type: "full-stack"
- cwd: "projects/04-supply-consensus"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold SupplyConsensus (Vue 3 + .NET 9)"
- description: "Create Vue 3 frontend, .NET 9 backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Azure."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-04"
- content: "Start Task 4: Scaffold SupplyConsensus. Stack: Vue 3 + .NET 9. Deploy to Azure. Report progress via task_update."

---

### Task 14: Spawn Agent-05 (MarketPulse)

**Context:** Agent-05 works in `projects/05-market-pulse/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-05"
- agent_type: "full-stack"
- cwd: "projects/05-market-pulse"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold MarketPulse (Angular 19 + Go)"
- description: "Create Angular 19 frontend, Go Fiber backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to GCP Cloud Run."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-05"
- content: "Start Task 5: Scaffold MarketPulse. Stack: Angular 19 + Go. Deploy to GCP Cloud Run. Report progress via task_update."

---

### Task 15: Spawn Agent-06 (InsightStream)

**Context:** Agent-06 works in `projects/06-insight-stream/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-06"
- agent_type: "full-stack"
- cwd: "projects/06-insight-stream"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold InsightStream (Next.js 15 RSC + Vercel AI SDK)"
- description: "Create Next.js 15 RSC frontend with Vercel AI SDK, /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Vercel."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-06"
- content: "Start Task 6: Scaffold InsightStream. Stack: Next.js 15 RSC + Vercel AI SDK. Deploy to Vercel. Report progress via task_update."

---

### Task 16: Spawn Agent-07 (ResearchSynthesis)

**Context:** Agent-07 works in `projects/07-research-synthesis/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-07"
- agent_type: "full-stack"
- cwd: "projects/07-research-synthesis"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold ResearchSynthesis (Remix + Python)"
- description: "Create Remix frontend, Python FastAPI backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Fly.io."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-07"
- content: "Start Task 7: Scaffold ResearchSynthesis. Stack: Remix + Python. Deploy to Fly.io. Report progress via task_update."

---

### Task 17: Spawn Agent-08 (TrendFactory)

**Context:** Agent-08 works in `projects/08-trend-factory/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-08"
- agent_type: "full-stack"
- cwd: "projects/08-trend-factory"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold TrendFactory (Nuxt 3 + Django)"
- description: "Create Nuxt 3 frontend, Django backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Render."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-08"
- content: "Start Task 8: Scaffold TrendFactory. Stack: Nuxt 3 + Django. Deploy to Render. Report progress via task_update."

---

### Task 18: Spawn Agent-09 (PatentIQ)

**Context:** Agent-09 works in `projects/09-patent-iq/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-09"
- agent_type: "full-stack"
- cwd: "projects/09-patent-iq"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold PatentIQ (Astro 5 + Flask)"
- description: "Create Astro 5 frontend, Flask backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to AWS ECS."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-09"
- content: "Start Task 9: Scaffold PatentIQ. Stack: Astro 5 + Flask. Deploy to AWS ECS. Report progress via task_update."

---

### Task 19: Spawn Agent-10 (ClaudeForge)

**Context:** Agent-10 works in `projects/10-claude-forge/`

**Step 1: Spawn teammate**

Use tool: `spawn_teammate`
- team_name: "ai-sdk-projects"
- name: "agent-10"
- agent_type: "full-stack"
- cwd: "projects/10-claude-forge"

**Step 2: Assign task**

Use tool: `task_create`
- team_name: "ai-sdk-projects"
- subject: "Scaffold ClaudeForge (T3 Stack + Python)"
- description: "Create T3 Stack (Next.js + tRPC + Tailwind + Prisma) frontend, Python FastAPI backend with /health endpoint, Dockerfile, CI/CD, README, CLAUDE.md. Deploy 'Hello World' to Fly.io."

**Step 3: Message agent**

Use tool: `send_message`
- type: "message"
- recipient: "agent-10"
- content: "Start Task 10: Scaffold ClaudeForge. Stack: T3 Stack + Python. Deploy to Fly.io. Report progress via task_update."

---

## Phase 3: Monitoring & Validation (Lead Agent)

### Task 20: Monitor Agent Progress

**Step 1: Check all task statuses**

Use tool: `task_list`
- team_name: "ai-sdk-projects"

Expected: 10 tasks with various statuses (pending/in_progress/completed)

**Step 2: Check for messages**

Use tool: `read_inbox`

Expected: Status updates from agents or blocker notifications

**Step 3: Broadcast status request**

Use tool: `send_message`
- type: "broadcast"
- content: "Status check: Reply with current task, progress %, and any blockers."

---

### Task 21: Validate Deployments

**Step 1: Create validation checklist**

**Files:**
- Create: `scripts/validate-deployments.sh`

```bash
#!/bin/bash
# scripts/validate-deployments.sh - Validate all 10 deployments

PROJECTS=(
  "venture-graph:Railway"
  "omni-desk:Render"
  "dev-squad:Fly.io"
  "supply-consensus:Azure"
  "market-pulse:GCP"
  "insight-stream:Vercel"
  "research-synthesis:Fly.io"
  "trend-factory:Render"
  "patent-iq:AWS"
  "claude-forge:Fly.io"
)

echo "Validating deployments..."
for proj in "${PROJECTS[@]}"; do
  IFS=':' read -r name platform <<< "$proj"
  echo "Checking $name on $platform..."
  # Platform-specific validation logic here
done
```

**Step 2: Commit validation script**

```bash
git add scripts/validate-deployments.sh
git commit -m "chore: add deployment validation script"
```

---

### Task 22: Final Summary

**Step 1: Generate summary**

Use tool: `task_list`
Count completed tasks

**Step 2: Create Week 1 summary document**

**Files:**
- Create: `docs/week1-summary.md`

```markdown
# Week 1 Sprint Summary

**Date:** 2026-02-XX
**Status:** Complete

## Results

| Project | Stack | Status | URL |
|---------|-------|--------|-----|
| VentureGraph | Next.js + FastAPI | ✅ | https://... |
| OmniDesk | React + FastAPI | ✅ | https://... |
| DevSquad | SvelteKit + Node | ✅ | https://... |
| SupplyConsensus | Vue + .NET | ✅ | https://... |
| MarketPulse | Angular + Go | ✅ | https://... |
| InsightStream | Next.js RSC | ✅ | https://... |
| ResearchSynthesis | Remix + Python | ✅ | https://... |
| TrendFactory | Nuxt + Django | ✅ | https://... |
| PatentIQ | Astro + Flask | ✅ | https://... |
| ClaudeForge | T3 + Python | ✅ | https://... |

## Next: Week 2

Core AI logic implementation for all 10 projects.
```

**Step 3: Final commit**

```bash
git add docs/week1-summary.md
git commit -m "docs: add Week 1 sprint summary"
```

---

## Success Criteria Checklist

- [ ] MCP server installed and configured
- [ ] Infrastructure templates created (Docker, CI/CD, README, CLAUDE.md)
- [ ] Bootstrap script created and executed
- [ ] tmux session created with 11 windows
- [ ] 10 git worktrees created
- [ ] Team "ai-sdk-projects" created via MCP
- [ ] 10 agents spawned and assigned tasks
- [ ] All 10 projects scaffolded
- [ ] All 10 projects deployed
- [ ] Week 1 summary document created

## Total Tasks: 22
