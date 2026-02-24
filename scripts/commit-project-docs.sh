#!/bin/bash
# Commit documentation changes to each project repository

PROJECTS=(
  "AI-SDK-LANGCHAIN"
  "AI-SDK-LANGGRAPH"
  "AI-SDK-AUTOGEN"
  "AI-SDK-CREWAI"
  "AI-SDK-LAMA-INDEX"
  "AI-SDK-HAYSTACK"
  "AI-SDK-SEMANTIC-KERNEL"
  "AI-SDK-OPENAI"
  "AI-SDK-ANTHROPIC"
  "AI-SDK-VERCEL-AI"
)

for proj in "${PROJECTS[@]}"; do
  if [ -d "$proj/.git" ]; then
    echo "=== Committing to $proj ==="
    cd "$proj"
    
    # Add documentation files
    git add README.md CONTRIBUTING.md docs/ 2>/dev/null
    
    # Commit if there are changes
    if git diff --cached --quiet; then
      echo "  No documentation changes to commit"
    else
      git commit -m "docs: generate comprehensive documentation

- Enhanced README with Architecture, API, and Troubleshooting sections
- Added docs/API.md with complete API reference
- Added docs/DEPLOYMENT.md with platform deployment guides
- Added docs/TESTING.md with testing strategies
- Updated CONTRIBUTING.md with development workflow

Part of AI-SDK Ecosystem documentation generation (Phase 3)"
      echo "  ✓ Committed documentation changes"
    fi
    
    cd ..
  fi
done

echo ""
echo "All documentation changes committed!"
