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
echo "========================="
echo ""

for proj in "${PROJECTS[@]}"; do
  IFS=':' read -r name platform <<< "$proj"
  echo "Checking $name on $platform..."

  # Check if project directory exists
  proj_dir="projects/*-$name"
  if compgen -G "$proj_dir" > /dev/null 2>&1; then
    echo "  ✓ Project directory exists"

    # Check for key files
    for dir in $proj_dir; do
      if [ -f "$dir/README.md" ]; then
        echo "  ✓ README.md exists"
      fi
      if [ -f "$dir/CLAUDE.md" ]; then
        echo "  ✓ CLAUDE.md exists"
      fi
      if [ -d "$dir/frontend" ]; then
        echo "  ✓ frontend/ directory exists"
      fi
      if [ -d "$dir/backend" ]; then
        echo "  ✓ backend/ directory exists"
      fi
      if [ -f "$dir/Dockerfile" ] || [ -f "$dir/docker-compose.yml" ]; then
        echo "  ✓ Docker configuration exists"
      fi
    done
  else
    echo "  ✗ Project directory not found"
  fi
  echo ""
done

echo "========================="
echo "Validation complete!"
