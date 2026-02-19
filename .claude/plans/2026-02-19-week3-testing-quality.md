# Week 3: Testing & Quality Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Achieve 80%+ test coverage across all 10 projects with comprehensive unit, integration, and E2E tests, plus security audits and performance benchmarks.

**Architecture:** Standardized testing approach across all projects - Jest for JavaScript/TypeScript, pytest for Python, Go testing for Go. Shared test utilities and patterns. Parallel test execution with coverage reporting.

**Tech Stack:** Jest, pytest, Playwright, k6, coverage.py, nyc, go test, security-scan tools

---

## Phase 1: Testing Infrastructure (Lead Agent)

### Task 1: Create Shared Test Configuration

**Files:**
- Create: `infrastructure/templates/jest.config.js`
- Create: `infrastructure/templates/pytest.ini`
- Create: `infrastructure/templates/.github/workflows/test.yml`

**Step 1: Create Jest config for JavaScript/TypeScript projects**

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  coverageDirectory: './coverage',
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  collectCoverageFrom: [
    'src/**/*.{ts,js}',
    '!src/**/*.d.ts',
    '!src/**/__tests__/**'
  ],
  testMatch: ['**/__tests__/**/*.test.ts', '**/?(*.)+(spec|test).ts']
};
```

**Step 2: Create pytest config for Python projects**

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --cov=app
    --cov-report=term-missing
    --cov-report=html
    --cov-fail-under=80
    -v
```

**Step 3: Create unified test workflow**

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test-javascript:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        project: [01-venture-graph, 02-omni-desk, 03-dev-squad, 06-insight-stream, 10-claude-forge]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd projects/${{ matrix.project }} && npm ci
      - run: cd projects/${{ matrix.project }} && npm test -- --coverage
      - uses: actions/upload-artifact@v4
        with:
          name: coverage-${{ matrix.project }}
          path: projects/${{ matrix.project }}/coverage

  test-python:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        project: [01-venture-graph, 02-omni-desk, 07-research-synthesis, 09-patent-iq, 10-claude-forge]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: cd projects/${{ matrix.project }}/backend && pip install -r requirements.txt pytest pytest-cov
      - run: cd projects/${{ matrix.project }}/backend && pytest --cov=app --cov-fail-under=80
```

**Step 4: Commit**

```bash
git add infrastructure/templates/
git commit -m "chore: add shared test configuration templates"
```

---

### Task 2: Create Test Utilities

**Files:**
- Create: `infrastructure/templates/tests/utils/mock-openai.ts`
- Create: `infrastructure/templates/tests/utils/fixtures.py`

**Step 1: Create OpenAI mock utility**

```typescript
// tests/utils/mock-openai.ts
export class MockOpenAI {
  private responses: Map<string, any> = new Map();

  setResponse(prompt: string, response: any) {
    this.responses.set(prompt, response);
  }

  async createChatCompletion(params: any) {
    const prompt = params.messages?.[params.messages.length - 1]?.content;
    const response = this.responses.get(prompt) || {
      choices: [{ message: { content: 'Mock response' } }]
    };
    return response;
  }
}

export const mockOpenAI = new MockOpenAI();
```

**Step 2: Create Python test fixtures**

```python
# tests/utils/fixtures.py
import pytest
from unittest.mock import Mock, MagicMock

@pytest.fixture
def mock_openai_response():
    return {
        "choices": [{"message": {"content": "Test response"}}]
    }

@pytest.fixture
def sample_venture_idea():
    return {
        "idea": "AI-powered sustainable farming platform",
        "market": "Agriculture technology",
        "target_customers": "Small to medium farms"
    }

@pytest.fixture
def mock_chroma_db():
    mock_db = MagicMock()
    mock_db.similarity_search.return_value = [
        MagicMock(page_content="Test document 1", metadata={"source": "test1"}),
        MagicMock(page_content="Test document 2", metadata={"source": "test2"})
    ]
    return mock_db
```

**Step 3: Commit**

```bash
git add infrastructure/templates/tests/
git commit -m "chore: add test utilities and fixtures"
```

---

## Phase 2: Unit Tests (Parallel by Project)

### Task 3: VentureGraph Unit Tests

**Context:** Agent-01 implements tests in `projects/01-venture-graph/`

**Files:**
- Create: `projects/01-venture-graph/backend/tests/test_graph.py`
- Create: `projects/01-venture-graph/backend/tests/test_main.py`

**Test Coverage Required:**
- Graph node functions (analyze_market, design_business_model, create_pitch_deck)
- State transitions
- API endpoints (/health, /plan)
- Error handling

---

### Task 4: OmniDesk Unit Tests

**Context:** Agent-02 implements tests in `projects/02-omni-desk/`

**Files:**
- Create: `projects/02-omni-desk/backend/tests/test_rag.py`
- Create: `projects/02-omni-desk/backend/tests/test_main.py`

**Test Coverage Required:**
- EnterpriseRAG class (add_documents, query)
- ChromaDB integration
- API endpoints (/health, /documents, /query)
- Empty state handling

---

### Task 5-12: Remaining Projects Unit Tests

**Context:** Agents 03-10 implement tests in their respective projects

Each agent creates:
- Unit tests for AI SDK integration
- API endpoint tests
- Mock external API calls
- 80%+ coverage target

---

## Phase 3: Integration Tests (Lead Agent)

### Task 13: Create Integration Test Suite

**Files:**
- Create: `tests/integration/test-ai-workflows.py`

**Step 1: Create integration tests**

```python
# tests/integration/test-ai-workflows.py
import pytest
import requests
import time

BASE_URLS = {
    "venture-graph": "http://localhost:8000",
    "omni-desk": "http://localhost:8001",
    "dev-squad": "http://localhost:5173",
    "supply-consensus": "http://localhost:8003",
    "market-pulse": "http://localhost:8080",
    "insight-stream": "http://localhost:3000",
    "research-synthesis": "http://localhost:8006",
    "trend-factory": "http://localhost:8007",
    "patent-iq": "http://localhost:5009",
    "claude-forge": "http://localhost:8010"
}

class TestAIWorkflows:
    def test_venture_graph_plan(self):
        """Test venture planning workflow end-to-end"""
        response = requests.post(
            f"{BASE_URLS['venture-graph']}/plan",
            json={"idea": "AI productivity tool"},
            timeout=30
        )
        assert response.status_code == 200
        data = response.json()
        assert "market_analysis" in data
        assert "business_model" in data
        assert "pitch_deck" in data

    def test_omni_desk_rag(self):
        """Test RAG document query workflow"""
        # Add documents
        requests.post(
            f"{BASE_URLS['omni-desk']}/documents",
            json={"documents": ["Company founded in 2020", "HQ in San Francisco"]}
        )

        # Query
        response = requests.post(
            f"{BASE_URLS['omni-desk']}/query",
            json={"question": "When was the company founded?"},
            timeout=10
        )
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "sources" in data
```

**Step 2: Commit**

```bash
git add tests/
git commit -m "test: add AI workflow integration tests"
```

---

## Phase 4: E2E Tests with Playwright

### Task 14: Setup Playwright E2E Tests

**Files:**
- Create: `e2e/playwright.config.ts`
- Create: `e2e/tests/venture-graph.spec.ts`

**Step 1: Create Playwright config**

```typescript
// e2e/playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
```

**Step 2: Create E2E test example**

```typescript
// e2e/tests/venture-graph.spec.ts
import { test, expect } from '@playwright/test';

test.describe('VentureGraph E2E', () => {
  test('user can create venture plan', async ({ page }) => {
    await page.goto('http://localhost:8000');

    // Fill in venture idea
    await page.fill('[data-testid="venture-idea"]', 'AI-powered fitness app');

    // Submit
    await page.click('[data-testid="submit-btn"]');

    // Wait for results
    await page.waitForSelector('[data-testid="market-analysis"]', { timeout: 30000 });

    // Verify sections exist
    await expect(page.locator('[data-testid="market-analysis"]')).toBeVisible();
    await expect(page.locator('[data-testid="business-model"]')).toBeVisible();
    await expect(page.locator('[data-testid="pitch-deck"]')).toBeVisible();
  });
});
```

**Step 3: Commit**

```bash
git add e2e/
git commit -m "test: add Playwright E2E test setup"
```

---

## Phase 5: Security Audit

### Task 15: Run Security Scans

**Step 1: Create security scan script**

```bash
#!/bin/bash
# scripts/security-scan.sh

echo "Running security scans..."

# Python projects - Bandit
for project in 01-venture-graph 02-omni-desk 07-research-synthesis 09-patent-iq 10-claude-forge; do
  echo "Scanning $project..."
  cd "projects/$project/backend" 2>/dev/null || continue
  pip install bandit safety
  bandit -r app/ -f json -o bandit-report.json || true
  safety check || true
  cd ../../..
done

# JavaScript projects - npm audit
for project in 01-venture-graph 02-omni-desk 03-dev-squad 06-insight-stream 10-claude-forge; do
  echo "Auditing $project..."
  cd "projects/$project" 2>/dev/null || continue
  npm audit --audit-level=moderate || true
  cd ../..
done

echo "Security scans complete. Check reports for issues."
```

**Step 2: Commit**

```bash
chmod +x scripts/security-scan.sh
git add scripts/security-scan.sh
git commit -m "chore: add security scan script"
```

---

## Phase 6: Performance Benchmarks

### Task 16: Create Performance Tests

**Files:**
- Create: `tests/performance/load-test.js`

**Step 1: Create k6 load test**

```javascript
// tests/performance/load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 10 },  // Ramp up
    { duration: '5m', target: 10 },  // Steady state
    { duration: '2m', target: 20 },  // Ramp up
    { duration: '5m', target: 20 },  // Steady state
    { duration: '2m', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<2000'], // 95% under 2s
    http_req_failed: ['rate<0.01'],    // <1% errors
  },
};

export default function () {
  const response = http.post('http://localhost:8000/plan', {
    idea: 'AI test idea',
  });

  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 2000ms': (r) => r.timings.duration < 2000,
  });

  sleep(1);
}
```

**Step 2: Commit**

```bash
git add tests/performance/
git commit -m "test: add performance benchmarks with k6"
```

---

## Phase 7: Coverage Report

### Task 17: Generate Coverage Dashboard

**Step 1: Create coverage aggregation script**

```bash
#!/bin/bash
# scripts/generate-coverage-report.sh

echo "Generating coverage report..."

# Run tests for all projects and collect coverage
coverage_data=""

for project in projects/*/; do
  name=$(basename "$project")
  echo "Processing $name..."

  if [ -f "$project/coverage/lcov-report/index.html" ]; then
    coverage=$(grep -o '>[0-9]\+%' "$project/coverage/lcov-report/index.html" | head -1 | tr -d '>%')
    coverage_data="$coverage_data\n$name: ${coverage}%"
  elif [ -f "$project/backend/htmlcov/index.html" ]; then
    coverage=$(grep -o '[0-9]\+%' "$project/backend/htmlcov/index.html" | head -1)
    coverage_data="$coverage_data\n$name: $coverage"
  fi
done

echo -e "# Test Coverage Report\n" > COVERAGE.md
echo -e "$coverage_data" >> COVERAGE.md
echo -e "\n## Summary" >> COVERAGE.md
echo -e "\nTarget: 80%+ for all projects" >> COVERAGE.md
```

**Step 2: Commit and generate report**

```bash
chmod +x scripts/generate-coverage-report.sh
./scripts/generate-coverage-report.sh
git add scripts/generate-coverage-report.sh COVERAGE.md
git commit -m "docs: add coverage dashboard"
```

---

## Success Criteria Checklist

- [ ] Shared test configuration created (Jest, pytest)
- [ ] Test utilities and fixtures created
- [ ] VentureGraph unit tests (80%+ coverage)
- [ ] OmniDesk unit tests (80%+ coverage)
- [ ] DevSquad unit tests (80%+ coverage)
- [ ] SupplyConsensus unit tests (80%+ coverage)
- [ ] MarketPulse unit tests (80%+ coverage)
- [ ] InsightStream unit tests (80%+ coverage)
- [ ] ResearchSynthesis unit tests (80%+ coverage)
- [ ] TrendFactory unit tests (80%+ coverage)
- [ ] PatentIQ unit tests (80%+ coverage)
- [ ] ClaudeForge unit tests (80%+ coverage)
- [ ] Integration tests for AI workflows
- [ ] Playwright E2E tests setup
- [ ] Security scans completed
- [ ] Performance benchmarks created
- [ ] Coverage dashboard generated

## Total Tasks: 17
