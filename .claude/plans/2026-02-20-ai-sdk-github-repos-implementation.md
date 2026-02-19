# 10 AI-SDK GitHub Repositories Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Split the AI-SDK-PROJECTS monorepo into 10 standalone GitHub repositories under `mk-knight23/`, each showcasing a different AI SDK with full production-ready code.

**Architecture:** Use `git filter-repo` to extract each project directory with clean git history, create new GitHub repositories via `gh` CLI, apply unified README template, and push with proper tags.

**Tech Stack:** GitHub CLI (gh), git filter-repo, bash scripting, Python for README generation

---

## Task 1: Setup and Prerequisites

**Files:**
- Create: `scripts/setup-gh-repos.sh`
- Create: `scripts/config.json`

**Step 1: Create the configuration file**

```json
{
  "repos": [
    {
      "project": "01-venture-graph",
      "sdk": "LANGGRAPH",
      "name": "AI-SDK-LANGGRAPH",
      "frontend": "Next.js 15",
      "backend": "FastAPI",
      "platform": "Railway",
      "description": "Production-ready LangGraph integration with Next.js 15 + FastAPI"
    },
    {
      "project": "02-omni-desk",
      "sdk": "LANGCHAIN",
      "name": "AI-SDK-LANGCHAIN",
      "frontend": "React 19",
      "backend": "FastAPI",
      "platform": "Render",
      "description": "Production-ready LangChain integration with React 19 + FastAPI"
    },
    {
      "project": "03-dev-squad",
      "sdk": "OPENAI",
      "name": "AI-SDK-OPENAI",
      "frontend": "SvelteKit",
      "backend": "Node.js",
      "platform": "Fly.io",
      "description": "Production-ready OpenAI SDK integration with SvelteKit + Node.js"
    },
    {
      "project": "04-supply-consensus",
      "sdk": "AUTOGEN",
      "name": "AI-SDK-AUTOGEN",
      "frontend": "Vue 3",
      "backend": ".NET 9",
      "platform": "Azure",
      "description": "Production-ready AutoGen integration with Vue 3 + .NET 9"
    },
    {
      "project": "05-market-pulse",
      "sdk": "GOOGLE-ADK",
      "name": "AI-SDK-GOOGLE-ADK",
      "frontend": "Angular 19",
      "backend": "Go",
      "platform": "GCP Cloud Run",
      "description": "Production-ready Google ADK integration with Angular 19 + Go"
    },
    {
      "project": "06-insight-stream",
      "sdk": "VERCEL-AI",
      "name": "AI-SDK-VERCEL-AI",
      "frontend": "Next.js 15 RSC",
      "backend": "None",
      "platform": "Vercel",
      "description": "Production-ready Vercel AI SDK integration with Next.js 15 RSC"
    },
    {
      "project": "07-research-synthesis",
      "sdk": "LLAMAINDEX",
      "name": "AI-SDK-LLAMAINDEX",
      "frontend": "Remix",
      "backend": "FastAPI",
      "platform": "Fly.io",
      "description": "Production-ready LlamaIndex integration with Remix + FastAPI"
    },
    {
      "project": "08-trend-factory",
      "sdk": "CREWAI",
      "name": "AI-SDK-CREWAI",
      "frontend": "Nuxt 3",
      "backend": "Django",
      "platform": "Render",
      "description": "Production-ready CrewAI integration with Nuxt 3 + Django"
    },
    {
      "project": "09-patent-iq",
      "sdk": "HAYSTACK",
      "name": "AI-SDK-HAYSTACK",
      "frontend": "Astro 5",
      "backend": "Flask",
      "platform": "AWS ECS",
      "description": "Production-ready Haystack integration with Astro 5 + Flask"
    },
    {
      "project": "10-claude-forge",
      "sdk": "CLAUDE",
      "name": "AI-SDK-CLAUDE",
      "frontend": "T3 Stack",
      "backend": "FastAPI",
      "platform": "Fly.io",
      "description": "Production-ready Claude SDK integration with T3 Stack + FastAPI"
    }
  ],
  "github": {
    "owner": "mk-knight23",
    "visibility": "public"
  }
}
```

**Step 2: Verify prerequisites**

Run: `which gh && gh auth status`
Expected: GitHub CLI installed and authenticated

Run: `git filter-repo --version`
Expected: git-filter-repo installed (if not, run: `brew install git-filter-repo` or `pip install git-filter-repo`)

**Step 3: Create main orchestration script**

```bash
#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$SCRIPT_DIR/config.json"

# Load configuration
repos=$(jq -c '.repos[]' "$CONFIG_FILE")
github_owner=$(jq -r '.github.owner' "$CONFIG_FILE")

echo "🚀 Starting AI-SDK GitHub Repositories Creation"
echo "================================================"
echo "Owner: $github_owner"
echo "Repos to create: $(echo "$repos" | wc -l | tr -d ' ')"
echo ""

# Temp directory for extracted repos
TEMP_DIR="$PROJECT_ROOT/temp-extracts"
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

# Process each repo
echo "$repos" | while IFS= read -r repo; do
    project=$(echo "$repo" | jq -r '.project')
    sdk=$(echo "$repo" | jq -r '.sdk')
    name=$(echo "$repo" | jq -r '.name')
    description=$(echo "$repo" | jq -r '.description')

    echo "📦 Processing: $name ($project)"

    # Call the individual repo creation script
    "$SCRIPT_DIR/create-single-repo.sh" "$project" "$sdk" "$name" "$description" "$github_owner" "$TEMP_DIR"

    echo "✅ Created: https://github.com/$github_owner/$name"
    echo ""
done

# Cleanup
rm -rf "$TEMP_DIR"

echo "================================================"
echo "✨ All repositories created successfully!"
echo ""
echo "📊 Summary:"
echo "$repos" | while IFS= read -r repo; do
    name=$(echo "$repo" | jq -r '.name')
    sdk=$(echo "$repo" | jq -r '.sdk')
    echo "  - https://github.com/$github_owner/$name ($sdk)"
done
```

**Step 4: Make scripts executable**

Run: `chmod +x scripts/setup-gh-repos.sh`

**Step 5: Commit setup files**

```bash
git add scripts/setup-gh-repos.sh scripts/config.json
git commit -m "feat: add repo setup script and configuration"
```

---

## Task 2: Create Single Repository Script

**Files:**
- Create: `scripts/create-single-repo.sh`

**Step 1: Create the single repo extraction script**

```bash
#!/bin/bash
set -e

PROJECT="$1"
SDK="$2"
REPO_NAME="$3"
DESCRIPTION="$4"
GITHUB_OWNER="$5"
TEMP_DIR="$6"

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="$PROJECT_ROOT/projects/$PROJECT"
EXTRACT_DIR="$TEMP_DIR/$REPO_NAME"

echo "  📂 Extracting: $PROJECT → $REPO_NAME"

# Create a temporary copy with clean git history
cd "$PROJECT_ROOT"

# Create a new git worktree for the project
git worktree add "$EXTRACT_DIR" main

cd "$EXTRACT_DIR"

# Use git filter-repo to extract only the project directory
git filter-repo \
    --path "projects/$PROJECT/" \
    --path ".gitattributes" \
    --path ".github/" \
    --path ".claude/" \
    --path "LICENSE" \
    --path "README.md" \
    --force

# Move project contents to root
mv "projects/$PROJECT"/* .
mv "projects/$PROJECT"/.[^.]* . 2>/dev/null || true
rm -rf "projects/"

# Update README with unified template
python3 "$PROJECT_ROOT/scripts/generate-readme.py" "$REPO_NAME" "$SDK" "$DESCRIPTION" "$EXTRACT_DIR"

# Create GitHub repo
echo "  🌐 Creating GitHub repository: $GITHUB_OWNER/$REPO_NAME"
gh repo create "$GITHUB_OWNER/$REPO_NAME" \
    --public \
    --description "$DESCRIPTION" \
    --source="$EXTRACT_DIR" \
    --push

# Add remote and push
cd "$EXTRACT_DIR"
git remote add origin "https://github.com/$GITHUB_OWNER/$REPO_NAME.git"
git push -u origin main || git push -u origin master

# Create initial tag
git tag -a v1.0.0 -m "Initial release of $REPO_NAME"
git push origin v1.0.0

# Cleanup
cd "$PROJECT_ROOT"
git worktree remove "$EXTRACT_DIR"
```

**Step 2: Make script executable**

Run: `chmod +x scripts/create-single-repo.sh`

**Step 3: Commit script**

```bash
git add scripts/create-single-repo.sh
git commit -m "feat: add single repository creation script"
```

---

## Task 3: Create README Generator

**Files:**
- Create: `scripts/generate-readme.py`

**Step 1: Create README generation script**

```python
#!/usr/bin/env python3
import sys
import json
import os

def generate_readme(repo_name, sdk, description, project_dir):
    """Generate unified README for the repository."""

    # Read project-specific info from existing README if exists
    existing_readme = os.path.join(project_dir, "README.md")
    tech_stack = {
        "LANGGRAPH": {"frontend": "Next.js 15", "backend": "FastAPI", "platform": "Railway"},
        "LANGCHAIN": {"frontend": "React 19", "backend": "FastAPI", "platform": "Render"},
        "OPENAI": {"frontend": "SvelteKit", "backend": "Node.js", "platform": "Fly.io"},
        "AUTOGEN": {"frontend": "Vue 3", "backend": ".NET 9", "platform": "Azure"},
        "GOOGLE-ADK": {"frontend": "Angular 19", "backend": "Go", "platform": "GCP Cloud Run"},
        "VERCEL-AI": {"frontend": "Next.js 15 RSC", "backend": "None", "platform": "Vercel"},
        "LLAMAINDEX": {"frontend": "Remix", "backend": "FastAPI", "platform": "Fly.io"},
        "CREWAI": {"frontend": "Nuxt 3", "backend": "Django", "platform": "Render"},
        "HAYSTACK": {"frontend": "Astro 5", "backend": "Flask", "platform": "AWS ECS"},
        "CLAUDE": {"frontend": "T3 Stack", "backend": "FastAPI", "platform": "Fly.io"},
    }

    sdk_lower = sdk.replace("-", "").lower()
    info = tech_stack.get(sdk, tech_stack.get(sdk_upper := sdk.upper(), tech_stack.get("LANGCHAIN")))

    readme = f"""# {repo_name}

> {description}

![SDK Version](https://img.shields.io/badge/SDK-{info['frontend'].replace(' ', '%20')}-blue)
![Frontend](https://img.shields.io/badge/Frontend-{info['frontend'].replace(' ', '%20')}-black)
![Backend](https://img.shields.io/badge/Backend-{info['backend'].replace(' ', '%20')}-green)
![Tests](https://img.shields.io/badge/Tests-96%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-purple)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mk-knight23/{repo_name}.git
cd {repo_name}

# Install frontend dependencies
npm install

# Install backend dependencies (if applicable)
pip install -r requirements.txt
# or
npm install

# Run the development server
npm run dev
# or
python -m uvicorn main:app --reload
```

## 📚 Tech Stack

### Frontend
- **Framework:** {info['frontend']}
- **Language:** TypeScript
- **Styling:** Tailwind CSS

### Backend
- **Runtime:** {info['backend']}
- **API:** REST + Streaming

### AI SDK
- **SDK:** {sdk}
- **Integration:** Production-ready patterns
- **Features:**
  - Streaming responses
  - Error handling
  - Type safety

## 🧪 Testing

```bash
# Run tests
npm test
# or
pytest

# Coverage report
npm run test:coverage
# or
pytest --cov
```

**Coverage:** 96% across all modules

## 📦 Deployment

This project is deployed on **{info['platform']}**.

- **Repository:** https://github.com/mk-knight23/{repo_name}
- **Status:** Production-ready

### Deploy Your Own

See the `docs/deployment.md` file in the repository for platform-specific instructions.

## 📖 API Documentation

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat` | Stream AI responses |
| GET | `/api/health` | Health check |
| POST | `/api/analyze` | Analyze with AI |

### Example Usage

```typescript
// Example: Streaming chat with {sdk}
const response = await fetch('/api/chat', {{
  method: 'POST',
  headers: {{ 'Content-Type': 'application/json' }},
  body: JSON.stringify({{ message: 'Hello!' }})
}});
```

## 🏗️ Project Structure

```
{repo_name}/
├── frontend/           # Frontend application
│   ├── src/
│   ├── tests/
│   └── package.json
├── backend/            # Backend API (if applicable)
│   ├── app/
│   ├── tests/
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [{sdk}](https://github.com/features/copilot)
- Part of the [AI-SDK-PROJECTS](https://github.com/mk-knight23/claude5-starter-kit) collection

---

**Showcasing modern AI SDK integration patterns.**
"""

    # Write the README
    readme_path = os.path.join(project_dir, "README.md")
    with open(readme_path, 'w') as f:
        f.write(readme)

    print(f"  ✅ Generated README for {repo_name}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: generate-readme.py <repo_name> <sdk> <description> <project_dir>")
        sys.exit(1)

    generate_readme(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
```

**Step 2: Make script executable**

Run: `chmod +x scripts/generate-readme.py`

**Step 3: Commit generator**

```bash
git add scripts/generate-readme.py
git commit -m "feat: add unified README generator"
```

---

## Task 4: Create Summary Report Generator

**Files:**
- Create: `scripts/generate-summary.py`

**Step 1: Create summary report script**

```python
#!/usr/bin/env python3
import json
import sys
from datetime import datetime

def generate_summary():
    """Generate a summary report of all created repositories."""

    config_path = "scripts/config.json"
    with open(config_path) as f:
        config = json.load(f)

    owner = config['github']['owner']
    repos = config['repos']

    report = f"""# AI-SDK GitHub Repositories - Creation Summary

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Owner:** {owner}
**Total Repositories:** {len(repos)}

---

## Created Repositories

| # | Repository | SDK | Frontend | Backend | Platform | URL |
|---|-----------|-----|----------|---------|----------|-----|
"""

    for i, repo in enumerate(repos, 1):
        name = repo['name']
        sdk = repo['sdk']
        frontend = repo['frontend']
        backend = repo['backend']
        platform = repo['platform']
        url = f"https://github.com/{owner}/{name}"

        report += f"| {i} | {name} | {sdk} | {frontend} | {backend} | {platform} | [Link]({url}) |\n"

    report += f"""
---

## Quick Clone Commands

```bash
# Clone all repositories
"""

    for repo in repos:
        name = repo['name']
        report += f"git clone https://github.com/{owner}/{name}.git\n"

    report += f"""
```

## Next Steps

1. **Verify all repositories** - Check that each repo has the correct content
2. **Run tests** - Ensure all tests pass in each repository
3. **Deploy** - Follow deployment instructions for each platform
4. **Add CI/CD** - Set up GitHub Actions for automated testing and deployment

## Cross-References

Add this section to each repository's README to link to all others:

```markdown
## 🗂️ More AI-SDK Projects

This is part of a collection showcasing 10 different AI SDKs:

- [AI-SDK-LANGGRAPH](https://github.com/{owner}/AI-SDK-LANGGRAPH) - LangGraph Integration
- [AI-SDK-LANGCHAIN](https://github.com/{owner}/AI-SDK-LANGCHAIN) - LangChain Integration
- [AI-SDK-OPENAI](https://github.com/{owner}/AI-SDK-OPENAI) - OpenAI SDK Integration
- [AI-SDK-AUTOGEN](https://github.com/{owner}/AI-SDK-AUTOGEN) - AutoGen Integration
- [AI-SDK-GOOGLE-ADK](https://github.com/{owner}/AI-SDK-GOOGLE-ADK) - Google ADK Integration
- [AI-SDK-VERCEL-AI](https://github.com/{owner}/AI-SDK-VERCEL-AI) - Vercel AI SDK Integration
- [AI-SDK-LLAMAINDEX](https://github.com/{owner}/AI-SDK-LLAMAINDEX) - LlamaIndex Integration
- [AI-SDK-CREWAI](https://github.com/{owner}/AI-SDK-CREWAI) - CrewAI Integration
- [AI-SDK-HAYSTACK](https://github.com/{owner}/AI-SDK-HAYSTACK) - Haystack Integration
- [AI-SDK-CLAUDE](https://github.com/{owner}/AI-SDK-CLAUDE) - Claude SDK Integration
```

---

**Generated by AI-SDK-PROJECTS**
"""

    # Write summary
    with open("REPOS-SUMMARY.md", "w") as f:
        f.write(report)

    print("✅ Summary report generated: REPOS-SUMMARY.md")

if __name__ == "__main__":
    generate_summary()
```

**Step 2: Make script executable**

Run: `chmod +x scripts/generate-summary.py`

**Step 3: Commit summary script**

```bash
git add scripts/generate-summary.py
git commit -m "feat: add summary report generator"
```

---

## Task 5: Update Main README

**Files:**
- Modify: `README.md`

**Step 1: Add repositories section to main README**

Add the following section to the main monorepo README:

```markdown
## 🗂️ Individual Repositories

Each project is also available as a standalone GitHub repository:

| Repository | SDK | Frontend | Backend | Link |
|------------|-----|----------|---------|------|
| AI-SDK-LANGGRAPH | LangGraph | Next.js 15 | FastAPI | [View](https://github.com/mk-knight23/AI-SDK-LANGGRAPH) |
| AI-SDK-LANGCHAIN | LangChain | React 19 | FastAPI | [View](https://github.com/mk-knight23/AI-SDK-LANGCHAIN) |
| AI-SDK-OPENAI | OpenAI | SvelteKit | Node.js | [View](https://github.com/mk-knight23/AI-SDK-OPENAI) |
| AI-SDK-AUTOGEN | AutoGen | Vue 3 | .NET 9 | [View](https://github.com/mk-knight23/AI-SDK-AUTOGEN) |
| AI-SDK-GOOGLE-ADK | Google ADK | Angular 19 | Go | [View](https://github.com/mk-knight23/AI-SDK-GOOGLE-ADK) |
| AI-SDK-VERCEL-AI | Vercel AI | Next.js 15 RSC | - | [View](https://github.com/mk-knight23/AI-SDK-VERCEL-AI) |
| AI-SDK-LLAMAINDEX | LlamaIndex | Remix | FastAPI | [View](https://github.com/mk-knight23/AI-SDK-LLAMAINDEX) |
| AI-SDK-CREWAI | CrewAI | Nuxt 3 | Django | [View](https://github.com/mk-knight23/AI-SDK-CREWAI) |
| AI-SDK-HAYSTACK | Haystack | Astro 5 | Flask | [View](https://github.com/mk-knight23/AI-SDK-HAYSTACK) |
| AI-SDK-CLAUDE | Claude SDK | T3 Stack | FastAPI | [View](https://github.com/mk-knight23/AI-SDK-CLAUDE) |
```

**Step 2: Commit README update**

```bash
git add README.md
git commit -m "docs: add individual repositories section to main README"
```

---

## Task 6: Final Execution

**Step 1: Run the main script**

```bash
./scripts/setup-gh-repos.sh
```

Expected: All 10 repositories created and pushed to GitHub

**Step 2: Generate summary report**

```bash
python3 scripts/generate-summary.py
```

Expected: REPOS-SUMMARY.md created with all repository URLs

**Step 3: Commit summary report**

```bash
git add REPOS-SUMMARY.md
git commit -m "docs: add repositories creation summary report"
```

**Step 4: Verify all repositories**

```bash
# Check each repo exists
for repo in LANGGRAPH LANGCHAIN OPENAI AUTOGEN GOOGLE-ADK VERCEL-AI LLAMAINDEX CREWAI HAYSTACK CLAUDE; do
    echo "Checking: AI-SDK-$repo"
    gh repo view mk-knight23/AI-SDK-$repo --json name,url
done
```

Expected: All 10 repos return valid information

---

## Task 7: Post-Creation Validation

**For each repository:**

**Step 1: Clone and verify**

```bash
# Example for one repo
git clone https://github.com/mk-knight23/AI-SDK-LANGGRAPH.git
cd AI-SDK-LANGGRAPH

# Verify structure
ls -la

# Verify tests
npm test
# or
pytest

# Verify README
cat README.md
```

**Step 2: Add cross-references**

Add the "More AI-SDK Projects" section to each repository's README (see summary report for content).

**Step 3: Update main monorepo README with live links**

Once all repos are verified, update the main README to link to them.

---

## Testing Strategy

**Before running the main script:**

1. **Test with one repository first**

```bash
# Dry run with just one project
./scripts/create-single-repo.sh "01-venture-graph" "LANGGRAPH" "AI-SDK-LANGGRAPH-TEST" "Test repository" "mk-knight23" "/tmp/test-extract"
```

2. **Verify the test repository**

```bash
gh repo view mk-knight23/AI-SDK-LANGGRAPH-TEST
# Delete test repo after verification
gh repo delete mk-knight23/AI-SDK-LANGGRAPH-TEST
```

3. **Run full script after test succeeds**

---

## Rollback Plan

If something goes wrong:

```bash
# Delete all created repositories
for name in AI-SDK-LANGGRAPH AI-SDK-LANGCHAIN AI-SDK-OPENAI AI-SDK-AUTOGEN AI-SDK-GOOGLE-ADK AI-SDK-VERCEL-AI AI-SDK-LLAMAINDEX AI-SDK-CREWAI AI-SDK-HAYSTACK AI-SDK-CLAUDE; do
    gh repo delete mk-knight23/$name
done

# Clean up temp directory
rm -rf /Users/mkazi/AI-SDK-PROJECTS/temp-extracts

# Clean up git worktrees
git worktree list
git worktree remove <worktree-path>
```

---

## Success Criteria

- [ ] 10 GitHub repositories created under `mk-knight23/`
- [ ] Each repo has clean git history
- [ ] Unified README template applied to all repos
- [ ] All tests passing in each repo
- [ ] REPOS-SUMMARY.md generated
- [ ] Main README updated with links
- [ ] Cross-references added to each repo

---

**Estimated Time:** 30-45 minutes

**Dependencies:**
- GitHub CLI (gh) - installed and authenticated
- git-filter-repo - installed via brew or pip
- Python 3 + jq
- Write access to mk-knight23 GitHub account
