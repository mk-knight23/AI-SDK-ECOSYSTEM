#!/bin/bash
# Security scan script for all projects

echo "Running security scans..."
echo "========================="

# Python projects - Bandit
for project in 01-venture-graph 02-omni-desk 07-research-synthesis 09-patent-iq 10-claude-forge; do
  echo "Scanning $project with bandit..."
  if [ -d "projects/$project/backend" ]; then
    cd "projects/$project/backend" 2>/dev/null || continue
    pip install bandit safety -q 2>/dev/null
    bandit -r app/ -f json -o bandit-report.json 2>/dev/null || true
    safety check 2>/dev/null || true
    cd ../../..
  fi
done

# JavaScript projects - npm audit
for project in 01-venture-graph 02-omni-desk 03-dev-squad 06-insight-stream 10-claude-forge; do
  echo "Auditing $project with npm..."
  if [ -d "projects/$project" ]; then
    cd "projects/$project" 2>/dev/null || continue
    npm audit --audit-level=moderate 2>/dev/null || true
    cd ../..
  fi
done

echo "========================="
echo "Security scans complete!"
