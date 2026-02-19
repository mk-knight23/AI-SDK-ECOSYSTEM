#!/bin/bash
# Generate coverage report for all projects

echo "Generating coverage report..."
echo "==========================="

coverage_data=""

for project_dir in projects/*/; do
  name=$(basename "$project_dir")
  coverage="N/A"

  # Check for JavaScript coverage
  if [ -f "$project_dir/coverage/lcov-report/index.html" ]; then
    coverage=$(grep -o '>[0-9]\+%' "$project_dir/coverage/lcov-report/index.html" | head -1 | tr -d '>%')
    coverage="${coverage}%"
  # Check for Python coverage
  elif [ -f "$project_dir/backend/htmlcov/index.html" ]; then
    coverage=$(grep -o '[0-9]\+%' "$project_dir/backend/htmlcov/index.html" | head -1)
  elif [ -f "$project_dir/htmlcov/index.html" ]; then
    coverage=$(grep -o '[0-9]\+%' "$project_dir/htmlcov/index.html" | head -1)
  fi

  coverage_data="${coverage_data}  $name: ${coverage}\n"
  echo "  $name: ${coverage}"
done

echo ""
echo "==========================="

# Generate COVERAGE.md
cat > COVERAGE.md << EOF
# Test Coverage Report

Generated: $(date)

## Project Coverage

| Project | Coverage | Status |
|---------|----------|--------|
EOF

# Add table rows
for project_dir in projects/*/; do
  name=$(basename "$project_dir")
  coverage="N/A"
  status="⚪"

  if [ -f "$project_dir/coverage/lcov-report/index.html" ]; then
    coverage=$(grep -o '>[0-9]\+%' "$project_dir/coverage/lcov-report/index.html" | head -1 | tr -d '>%')
    if [ "$coverage" -ge 80 ]; then
      status="✅"
    else
      status="⚠️"
    fi
    coverage="${coverage}%"
  elif [ -f "$project_dir/backend/htmlcov/index.html" ]; then
    coverage=$(grep -o '[0-9]\+%' "$project_dir/backend/htmlcov/index.html" | head -1)
    cov_num=$(echo "$coverage" | tr -d '%')
    if [ "$cov_num" -ge 80 ]; then
      status="✅"
    else
      status="⚠️"
    fi
  fi

  echo "| $name | $coverage | $status |" >> COVERAGE.md
done

cat >> COVERAGE.md << EOF

## Summary

- **Target:** 80%+ coverage for all projects
- **Status:** See individual project results above

## Running Tests

\`\`\`bash
# Run all tests
./scripts/test-all-ai.sh

# Generate coverage report
./scripts/generate-coverage-report.sh
\`\`\`
EOF

echo "Coverage report generated: COVERAGE.md"
