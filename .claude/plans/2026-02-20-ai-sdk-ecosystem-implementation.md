# AI-SDK Ecosystem Transformation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform the monorepo `claude5-starter-kit` into an AI SDK showcase ecosystem with 10 independent GitHub repositories.

**Architecture:**
1. Rename current repo to `AI-SDK-ECOSYSTEM` - serves as showcase hub
2. Create 10 independent GitHub repos named after AI frameworks (LANGCHAIN, CREWAI, etc.)
3. Build single-page HTML showcase with card grid linking to all repos
4. Each project copied to its corresponding repo, completely independent

**Tech Stack:** GitHub CLI, shell scripts, vanilla HTML/CSS/JS, GitHub Pages

---

## Phase 1: Repository Preparation

### Task 1: Rename Current Repository

**Step 1: Rename the repository**
```bash
gh repo rename AI-SDK-ECOSYSTEM
```

**Step 2: Verify rename**
```bash
gh repo view --json name,url
```

**Step 3: Commit**
```bash
git add . && git commit -m "chore: rename repository to AI-SDK-ECOSYSTEM" && git push
```

---

### Task 2: Create 10 GitHub Repositories

**Step 1-10: Create all repositories**
```bash
gh repo create AI-SDK-LANGCHAIN --public --description "LangChain Framework SDK - Production-ready AI agent stack with Next.js + FastAPI" --clone
gh repo create AI-SDK-CREWAI --public --description "CrewAI Agent Framework SDK - Multi-agent orchestration with React 19 + FastAPI" --clone
gh repo create AI-SDK-LANGGRAPH --public --description "LangGraph SDK - Stateful agent workflows with SvelteKit + Node.js" --clone
gh repo create AI-SDK-AUTOGEN --public --description "Microsoft AutoGen SDK - Multi-agent framework with Vue 3 + .NET 9" --clone
gh repo create AI-SDK-OPENAI --public --description "OpenAI SDK - Assistants API & GPT integration with Angular 19 + Go" --clone
gh repo create AI-SDK-VERCEL-AI --public --description "Vercel AI SDK - React/Next.js AI integration with Next.js 15" --clone
gh repo create AI-SDK-ANTHROPIC --public --description "Anthropic Claude SDK - Claude API integration with Remix + FastAPI" --clone
gh repo create AI-SDK-HAYSTACK --public --description "Haystack SDK - Deepset NLP framework with Nuxt 3 + Django" --clone
gh repo create AI-SDK-SEMANTIC-KERNEL --public --description "Microsoft Semantic Kernel SDK with Astro 5 + Flask" --clone
gh repo create AI-SDK-LAMA-INDEX --public --description "LlamaIndex SDK - Data framework for LLMs with T3 Stack + FastAPI" --clone
```

**Step 11: Verify all repos created**
```bash
gh repo list | grep "AI-SDK-"
```

---

## Phase 2: Project Migration

### Tasks 3-12: Migrate Each Project

For each project, execute:

**Step 1: Copy files** (exclude node_modules, build artifacts)
```bash
rsync -av --exclude='node_modules' --exclude='.git' --exclude='__pycache__' \
  projects/XX-PROJECT-NAME/ ../AI-SDK-XXX/
```

**Step 2: Update README with new naming**
```bash
sed -i '' 's/XX-ProjectName/AI-SDK-XXX/g' README.md
```

**Step 3: Update package.json name**
```bash
jq '.name = "ai-sdk-xxx"' package.json > package.json.tmp && mv package.json.tmp package.json
```

**Step 4: Commit and push**
```bash
git add . && git commit -m "feat: initial SDK implementation" && git push -u origin main
```

---

## Phase 3: Build Showcase

### Task 13: Create Showcase index.html

**Step 1: Create index.html with card grid**
- Single HTML file with embedded CSS
- GitHub API integration for live stats
- Responsive 3-column grid (1-column mobile)
- Dark mode styling

**Step 2: Commit**
```bash
git add index.html && git commit -m "feat: add AI-SDK ecosystem showcase"
```

---

### Task 14: Enable GitHub Pages

**Step 1: Enable Pages**
```bash
gh api -X POST repos/mk-knight23/AI-SDK-ECOSYSTEM/pages -f source=main -f path=/
```

**Step 2: Verify deployment**
```bash
gh api repos/mk-knight23/AI-SDK-ECOSYSTEM/pages
```

---

## Phase 4: Documentation Updates

### Task 15: Update Main README

Replace README with ecosystem showcase content:
- Links to all 10 repos
- Architecture diagram
- Tech stack coverage table

### Task 16: Clean Up Old Files

```bash
rm -rf projects/ coverage/ htmlcov/ e2e/ logs/ node_modules/
git add . && git commit -m "chore: remove old project files"
```

### Task 17: Add Ecosystem Badges

Add badge to all 10 repo READMEs:
```markdown
[![AI-SDK Ecosystem](https://img.shields.io/badge/AI--SDK-ECOSYSTEM-part%20of-blue)](https://github.com/mk-knight23/AI-SDK-ECOSYSTEM)
```

### Task 18: Final Verification

```bash
# Verify all repos exist
gh repo list | grep "AI-SDK-"

# Verify showcase is live
curl -s -o /dev/null -w "%{http_code}" https://mk-knight23.github.io/AI-SDK-ECOSYSTEM/

# Push final updates
git push
```

---

## Success Criteria

- [x] Repository renamed to AI-SDK-ECOSYSTEM
- [x] 10 independent repos created on GitHub
- [x] All projects migrated to respective repos
- [x] Showcase index.html displays all 10 projects
- [x] GitHub Pages deployed and accessible
- [x] All READMEs updated with ecosystem badges
- [x] No cross-repo dependencies
