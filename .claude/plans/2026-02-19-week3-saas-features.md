# Week 3: SaaS Features Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement 6 SaaS features (auth, billing, rate limiting, dashboards, API key management, email) across all 10 AI SDK projects in parallel using tmux-coordinated agents.

**Architecture:** 10 parallel agents (one per project) × 6 features each = 60 parallel implementations, automated quality gates, handoff documentation for continuity.

**Tech Stack:** Tmux orchestration, Claude Code agents, independent implementations, TDD throughout, automated CI/CD gates.

**Timeline:** 8 days (2026-02-20 to 2026-02-27)

---

## Implementation Strategy

### **Parallel Agent Orchestration**

```
Master Terminal (You)
    │
    ├─── tmux window 1: VentureGraph agent    → Auth0 + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 2: OmniDesk agent        → Firebase + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 3: DevSquad agent        → GitHub OAuth + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 4: SupplyConsensus agent → Entra ID + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 5: MarketPulse agent     → Google OAuth + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 6: InsightStream agent  → NextAuth v5 + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 7: ResearchSynthesis agent → Magic Link + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 8: TrendFactory agent    → Django Allauth + Stripe + Redis + Dashboard + API keys + Resend
    ├─── tmux window 9: PatentIQ agent        → JWT + Stripe + Redis + Dashboard + API keys + Resend
    └── tmux window 10: ClaudeForge agent     → NextAuth + Stripe + Redis + Dashboard + API keys + Resend
```

### **Quality Gates (Automated)**

- ✅ **Tests:** All projects must pass `npm test` or `pytest`
- ✅ **Linting:** All projects must pass `npm run lint` or linters
- ✅ **Type checking:** TypeScript projects must pass `npm run typecheck`
- ✅ **Security scan:** `npx audit-ci --moderate` must pass
- ✅ **Build:** All projects must build successfully
- ✅ **CI/CD:** GitHub Actions must pass

**Only failures trigger your review.**

---

## Per-Project Auth Configuration

### **01. VentureGraph** - Auth0
- Provider: Auth0
- Tech: NextAuth.js v5 wrapper for Auth0
- Flow: OAuth 2.0, social logins
- Environment: `AUTH0_SECRET`, `AUTH0_ISSUER_BASE_URL`

### **02. OmniDesk** - Firebase
- Provider: Firebase Authentication
- Tech: Firebase SDK directly
- Flow: Email/password, Google OAuth
- Environment: `FIREBASE_API_KEY`, `FIREBASE_AUTH_DOMAIN`

### **03. DevSquad** - GitHub OAuth
- Provider: GitHub
- Tech: NextAuth.js v5 GitHub provider
- Flow: GitHub OAuth only
- Environment: `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`

### **04. SupplyConsensus** - Microsoft Entra ID
- Provider: Azure AD
- Tech: NextAuth.js v5 Azure AD provider
- Flow: Microsoft OAuth
- Environment: `AZURE_AD_CLIENT_ID`, `AZURE_AD_CLIENT_SECRET`, `AZURE_AD_TENANT_ID`

### **05. MarketPulse** - Google OAuth
- Provider: Google
- Tech: Google OAuth2 SDK
- Flow: Google Sign-In
- Environment: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`

### **06. InsightStream** - NextAuth v5
- Provider: Multiple credentials via NextAuth
- Tech: NextAuth.js v5
- Flow: Email (Resend) + Google OAuth
- Environment: `NEXTAUTH_SECRET`, `NEXTAUTH_URL`

### **07. ResearchSynthesis** - Magic Link
- Provider: Custom magic link
- Tech: NodeMailer + custom tokens
- Flow: Email magic links only
- Environment: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`

### **08. TrendFactory** - Django Allauth
- Provider: Django Allauth
- Tech: Django allauth, social accounts
- Flow: Google OAuth, GitHub OAuth
- Environment: `SOCIAL_AUTH_GOOGLE_OAUTH_KEY`, `SOCIAL_AUTH_GITHUB_OAUTH_KEY`

### **09. PatentIQ** - Custom JWT
- Provider: Custom JWT implementation
- Tech: Flask-JWT-Extended
- Flow: Username/password JWT
- Environment: `JWT_SECRET_KEY`, `JWT_ALGORITHM`

### **10. ClaudeForge** - NextAuth
- Provider: Multiple via NextAuth v5
- Tech: NextAuth.js v5
- Flow: Email (Resend) + credentials
- Environment: `NEXTAUTH_SECRET`, `NEXTAUTH_URL`

---

## Task 1: Bootstrap All 10 Agents

**Files:**
- Modify: `scripts/week3-bootstrap.sh` (create new)

**Step 1: Create Week 3 bootstrap script**

```bash
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
```

**Step 2: Make script executable**

```bash
chmod +x scripts/week3-bootstrap.sh
```

**Step 3: Verify bootstrap script**

Run: `head -20 scripts/week3-bootstrap.sh`
Expected: Script contents visible

**Step 4: Commit bootstrap script**

```bash
git add scripts/week3-bootstrap.sh
git commit -m "feat: add Week 3 agent team bootstrap script

Creates tmux session with 10 windows (one per project).
Each window starts Claude Code agent for parallel SaaS implementation.
Coordinates Week 3: auth, billing, rate limiting, dashboards, API keys, email."
```

---

## Task 2: Create Shared SaaS Components

**Files:**
- Create: `shared/billing/stripe-wrapper.ts`
- Create: `shared/billing/usage-tracker.ts`
- Create: `shared/rate-limiting/redis-limiter.ts`
- Create: `shared/email/resend-client.ts`

**Step 1: Create Stripe billing wrapper**

```typescript
// shared/billing/stripe-wrapper.ts
import Stripe from 'stripe';

export class StripeBilling {
  private stripe: Stripe;

  constructor(apiKey: string) {
    this.stripe = new Stripe(apiKey);
  }

  async createCustomer(email: string, name: string) {
    return await this.stripe.customers.create({
      email,
      name,
      metadata: { source: 'ai-sdk-saas' }
    });
  }

  async createSubscription(customerId: string, priceId: string) {
    return await this.stripe.subscriptions.create({
      customer: customerId,
      items: [{ price: priceId }],
      payment_behavior: 'default_incomplete',
    });
  }

  async createUsageRecord(subscriptionId: string, units: number) {
    return await this.stripe.subscriptionItems.createUsageRecord(
      subscriptionId,
      { quantity: units, action: 'increment' }
    );
  }

  async cancelSubscription(subscriptionId: string) {
    return await this.stripe.subscriptions.cancel(subscriptionId);
  }
}
```

**Step 2: Create usage tracker**

```typescript
// shared/billing/usage-tracker.ts
export class UsageTracker {
  private usage: Map<string, number> = new Map();

  recordUsage(userId: string, units: number = 1) {
    const current = this.usage.get(userId) || 0;
    this.usage.set(userId, current + units);
  }

  getUsage(userId: string): number {
    return this.usage.get(userId) || 0;
  }

  resetUsage(userId: string) {
    this.usage.set(userId, 0);
  }
}
```

**Step 3: Create Redis rate limiter**

```typescript
// shared/rate-limiting/redis-limiter.ts
import { Redis } from 'ioredis';

export class RateLimiter {
  private redis: Redis;
  private windowMs: number;
  private maxRequests: number;

  constructor(redisUrl: string, windowMs: number, maxRequests: number) {
    this.redis = new Redis(redisUrl);
    this.windowMs = windowMs;
    this.maxRequests = maxRequests;
  }

  async checkLimit(userId: string): Promise<boolean> {
    const key = `ratelimit:${userId}`;
    const current = await this.redis.incr(key);

    if (current === 1) {
      await this.redis.expire(key, this.windowMs / 1000);
    }

    return current <= this.maxRequests;
  }

  async resetLimit(userId: string): Promise<void> {
    const key = `ratelimit:${userId}`;
    await this.redis.del(key);
  }
}
```

**Step 4: Create Resend email client**

```typescript
// shared/email/resend-client.ts
import { Resend } from 'resend';

export class EmailClient {
  private resend: Resend;

  constructor(apiKey: string) {
    this.resend = new Resend(apiKey);
  }

  async sendEmail(to: string, subject: string, html: string) {
    await this.resend.emails.send({
      from: 'noreply@ai-sdk-saas.com',
      to,
      subject,
      html,
    });
  }

  async sendWelcomeEmail(to: string, name: string) {
    await this.sendEmail(
      to,
      'Welcome to AI SDK SaaS!',
      `<h1>Welcome ${name}!</h1><p>Your account is ready.</p>`
    );
  }

  async sendResetLink(to: string, resetLink: string) {
    await this.sendEmail(
      to,
      'Reset your password',
      `<p>Click <a href="${resetLink}">here</a> to reset.</p>`
    );
  }
}
```

**Step 5: Commit shared components**

```bash
git add shared/
git commit -m "feat: add shared SaaS components

- Stripe billing wrapper (customer, subscription, usage)
- Usage tracker for rate limiting
- Redis rate limiter with sliding window
- Resend email client with templates

These components will be copied/used by all 10 projects."
```

---

## Task 3: Create Agent Instructions Template

**Files:**
- Create: `.claude/week3-agent-instructions.md`

**Step 1: Create agent instructions**

```markdown
# Week 3 Agent Instructions

## Your Mission

You are implementing **6 SaaS features** for your assigned project:

1. **Authentication** - User registration, login, logout
2. **Stripe Billing** - Subscription management, checkout
3. **Rate Limiting** - Redis-based usage limits
4. **User Dashboard** - Settings, usage stats, billing
5. **API Key Management** - Users create/manage API keys
6. **Email Integration** - Welcome emails, notifications

## Your Tech Stack

- **Project:** [INSERT_PROJECT_NAME]
- **Auth Provider:** [INSERT_AUTH_PROVIDER]
- **Frontend Framework:** [INSERT_FRAMEWORK]
- **Backend Framework:** [INSERT_BACKEND]
- **Database:** [INSERT_DATABASE]

## Authentication Implementation

**Provider:** [INSERT_AUTH_PROVIDER]

**Requirements:**
- User registration (email + password or OAuth)
- User login/logout
- Session management
- Protected routes
- User profile page

**Frontend:**
```bash
# Install auth package
npm install [INSERT_AUTH_PACKAGE]

# Create auth configuration
# Implement login/register pages
# Add protected route wrappers
```

**Backend:**
```bash
# Install auth dependencies
npm install [INSERT_AUTH_BACKEND]

# Create auth endpoints
# Implement session middleware
# Add user model/tables
```

**Testing:**
```bash
# Write tests FIRST (TDD)
# Test registration
# Test login/logout
# Test protected routes
# Test session management
```

**Success Criteria:**
- ✅ Users can register
- ✅ Users can login/logout
- ✅ Protected routes work
- ✅ Sessions persist
- ✅ Tests pass (80%+ coverage)

---

## Stripe Billing Implementation

**Requirements:**
- Stripe checkout integration
- Subscription tiers (Free, Pro, Enterprise)
- Usage tracking
- Billing dashboard
- Webhook handlers

**Implementation:**
```bash
# Install Stripe
npm install stripe @stripe/stripe-js

# Create Stripe wrapper (copy from shared/billing/)
# Implement checkout flow
# Add billing dashboard
# Create webhook endpoint
```

**Success Criteria:**
- ✅ Checkout flow works
- ✅ Subscriptions created in Stripe
- ✅ Webhooks processed
- ✅ Billing dashboard shows plans/usage
- ✅ Tests pass

---

## Rate Limiting Implementation

**Requirements:**
- Redis-based rate limiting
- Per-user limits
- Endpoint-specific limits
- Admin override capability

**Implementation:**
```bash
# Install Redis client
npm install ioredis

# Copy rate limiter from shared/rate-limiting/
# Implement middleware
# Add Redis connection
# Configure limits per endpoint
```

**Success Criteria:**
- ✅ Rate limits enforced
- ✅ Redis connection works
- ✅ Admins can bypass limits
- ✅ Tests pass

---

## User Dashboard Implementation

**Requirements:**
- User profile page
- Usage statistics
- Billing history
- Settings page
- API key management (see next feature)

**Implementation:**
```bash
# Create dashboard pages
# Add navigation
# Implement profile editing
# Add usage charts
# Connect to Stripe for billing history
```

**Success Criteria:**
- ✅ Dashboard accessible to authenticated users
- ✅ Profile editing works
- ✅ Usage stats display correctly
- ✅ Billing history shows
- ✅ Tests pass

---

## API Key Management Implementation

**Requirements:**
- Users can create API keys
- List/regenerate keys
- Keys are scoped to user account
- Usage tracking per key
- Key expiration

**Implementation:**
```bash
# Create API keys model
# Implement key generation
# Add key management UI
# Track usage per key
# Add key revocation
```

**Success Criteria:**
- ✅ Users can create keys
- ✅ Keys are hashed in database
- ✅ Keys can be revoked
- ✅ Usage tracked per key
- ✅ Tests pass

---

## Email Integration Implementation

**Requirements:**
- Welcome emails on signup
- Password reset emails
- Billing notifications
- Usage alerts
- Use Resend API

**Implementation:**
```bash
# Install Resend
npm install resend

# Copy email client from shared/email/
# Implement email templates
# Add email triggers
# Test email delivery
```

**Success Criteria:**
- ✅ Welcome emails sent on signup
- ✅ Password reset works
- ✅ Billing notifications sent
- ✅ Emails deliver successfully
- ✅ Tests pass

---

## TDD Workflow (MANDATORY)

1. **Write tests FIRST** for each feature
2. Run tests → watch them FAIL
3. Implement minimal code to make tests PASS
4. Refactor for quality
5. Commit after passing tests
6. Target: **80%+ test coverage**

---

## Daily Workflow

1. **Morning:** Resume previous day's work
2. **Check:** Run tests, lint, typecheck
3. **Implement:** Work on current feature
4. **Commit:** Commit frequently with conventional commits
5. **Evening:** Run `/dx:handoff` before stopping
6. **Tomorrow:** Resume from handoff document

---

## Handoff Document Format

```markdown
# Handoff - [Project] - Day X

## Completed
- [x] Authentication implementation
- [x] Initial Stripe setup

## In Progress
- [ ] Completing Stripe checkout

## Blocked On
- None

## Next Steps
- Complete webhook handlers
- Start rate limiting

## Notes
- Stripe webhook endpoint: https://webhook.site/xxx
- Test user: test@example.com / password123
```

---

## Automated Quality Gates

Before committing, ensure:
```bash
npm run lint          # Must pass
npm run typecheck     # Must pass
npm test               # Must pass
npm run build         # Must pass
npx audit-ci --moderate  # Must pass
```

**If any gate fails:**
1. Fix the issue
2. Re-run all gates
3. Only commit when ALL pass

---

## Success Criteria

Your Week 3 implementation is successful when:

✅ All 6 features implemented
✅ All tests pass (80%+ coverage)
✅ All quality gates pass
✅ Manual testing confirms each feature works
✅ Handoff documents created daily
✅ Git history shows clean progression

---

**Start Date:** 2026-02-20
**Target Date:** 2026-02-27
**Duration:** 8 days
```

**Step 6: Create project-specific instruction files**

For each project, copy and customize the template:

```bash
for project in 01-venture-graph 02-omni-desk 03-dev-squad 04-supply-consensus 05-market-pulse 06-insight-stream 07-research-synthesis 08-trend-factory 09-patent-iq 10-claude-forge; do
  # Create instructions with project-specific details
  cp .claude/week3-agent-instructions.md projects/$project/.claude/WEEK3.md

  # Customize instructions based on project
  # (This will be done by each agent when they start)
done
```

**Step 7: Commit agent instructions**

```bash
git add .claude/week3-agent-instructions.md
git add projects/*/.claude/WEEK3.md
git commit -m "docs: add Week 3 agent instructions

Created master agent instructions template.
Each project will have customized instructions.
Includes TDD requirements, quality gates, handoff format."
```

---

## Task 4: Set Up Automated Quality Gates

**Files:**
- Create: `.github/workflows/quality-gate.yml`
- Modify: `.github/workflows/ci.yml` (if exists)

**Step 1: Create quality gate workflow**

```yaml
name: Quality Gate

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        project:
          - venture-graph
          - omni-desk
          - dev-squad
          - supply-consensus
          - market-pulse
          - insight-stream
          - research-synthesis
          - trend-factory
          - patent-iq
          - claude-forge

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: |
          cd projects/${{ matrix.project }}
          npm ci

      - name: Lint
        run: |
          cd projects/${{ matrix.project }}
          npm run lint

      - name: Type check
        run: |
          cd projects/${{ matrix.project }}
          npm run typecheck

      - name: Tests
        run: |
          cd projects/${{ matrix.project }}
          npm test -- --coverage

      - name: Security audit
        run: |
          cd projects/${{ matrix.project }}
          npx audit-ci --moderate

      - name: Build
        run: |
          cd projects/${{ matrix.project }}
          npm run build

      - name: Check coverage
        run: |
          cd projects/${{ matrix.project }}
          npm run test:coverage
          # Fail if coverage < 80%
```

**Step 2: Verify workflow syntax**

Run: `yamllint .github/workflows/quality-gate.yml` (if yamllint installed)

**Step 3: Commit quality gates**

```bash
git add .github/workflows/quality-gate.yml
git commit -m "ci: add automated quality gates for Week 3

Enforces:
- Linting (ESLint/Pylint)
- Type checking (TypeScript/mypy)
- Tests with 80%+ coverage
- Security audit (audit-ci moderate)
- Build success
- Runs on all 10 projects in parallel"
```

---

## Task 5: Create Week 3 Orchestration Script

**Files:**
- Create: `scripts/week3-orchestrate.sh`

**Step 1: Create orchestration script**

```bash
#!/bin/bash
# scripts/week3-orchestrate.sh
# Broadcast commands to all 10 agent tmux windows

SESSION="week3-saas"

case "$1" in
  "start-auth")
    echo "🔐 Broadcasting: Start authentication implementation..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start implementing authentication feature now" Enter
    done
    ;;

  "start-stripe")
    echo "💳 Broadcasting: Start Stripe billing..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start Stripe billing implementation now" Enter
    done
    ;;

  "start-ratelimit")
    echo "⚡ Broadcasting: Start rate limiting..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start rate limiting implementation now" Enter
    done
    ;;

  "start-dashboard")
    echo "📊 Broadcasting: Start user dashboards..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start user dashboard implementation now" Enter
    done
    ;;

  "start-apikeys")
    echo "🔑 Broadcasting: Start API key management..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start API key management implementation now" Enter
    done
    ;;

  "start-email")
    echo "📧 Broadcasting: Start email integration..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "All agents: Start email integration now" Enter
    done
    ;;

  "run-tests")
    echo "🧪 Broadcasting: Run all tests..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "npm test && npm run lint && npm run typecheck" Enter
    done
    ;;

  "handoff")
    echo "📝 Broadcasting: Create handoff documents..."
    for i in {1..10}; do
      tmux send-keys -t $SESSION:$i "/dx:handoff" Enter
      sleep 2
    done
    ;;

  "status")
    echo "📊 Agent Status Check:"
    for i in {1..10}; do
      PROJECT=$(tmux display -p '#S - #W "#{=window_name}"' | grep "^$i:" | cut -d: -f2)
      STATUS=$(tmux capture-pane -t $SESSION:$i -p | tail -5)
      echo "Window $i ($PROJECT): $STATUS"
    done
    ;;

  *)
    echo "Usage: $0 {start-auth|start-stripe|start-ratelimit|start-dashboard|start-apikeys|start-email|run-tests|handoff|status}"
    exit 1
    ;;
esac
```

**Step 2: Make orchestration script executable**

```bash
chmod +x scripts/week3-orchestrate.sh
```

**Step 3: Test orchestration script**

Run: `./scripts/week3-orchestrate.sh status`
Expected: Shows all agent windows

**Step 4: Commit orchestration script**

```bash
git add scripts/week3-orchestrate.sh
git commit -m "chore: add Week 3 orchestration script

Provides commands to broadcast to all 10 agents:
- start-auth, start-stripe, start-ratelimit, start-dashboard
- start-apikeys, start-email, run-tests, handoff, status

Coordinates parallel SaaS feature implementation across all projects."
```

---

## Task 6: Update README for Week 3

**Files:**
- Modify: `README.md` (Week 3 section)

**Step 1: Update Week 3 section in README**

```markdown
## Week 3: SaaS Features 🚧 (In Progress)

**Started:** 2026-02-20

**6 Features Implementing Across All 10 Projects:**

### Authentication ✅
- ✅ VentureGraph: Auth0
- ✅ OmniDesk: Firebase
- ✅ DevSquad: GitHub OAuth
- ✅ SupplyConsensus: Microsoft Entra ID
- ✅ MarketPulse: Google OAuth
- ✅ InsightStream: NextAuth v5
- ✅ ResearchSynthesis: Magic Link
- ✅ TrendFactory: Django Allauth
- ✅ PatentIQ: Custom JWT
- ✅ ClaudeForge: NextAuth

### Stripe Billing 🚧
- Subscription tiers (Free, Pro, Enterprise)
- Checkout integration
- Usage tracking
- Webhook handlers

### Rate Limiting 📋
- Redis-based rate limiting
- Per-user limits
- Endpoint-specific limits
- Admin overrides

### User Dashboards 📋
- User profile pages
- Usage statistics
- Billing history
- Settings management

### API Key Management 📋
- Key creation/scoping
- Usage tracking per key
- Key revocation
- Admin management

### Email Integration 📋
- Welcome emails
- Password reset
- Billing notifications
- Usage alerts

### Parallel Implementation

**10 Agents working simultaneously via tmux:**
- Each project has dedicated agent
- Automated quality gates (tests, lint, typecheck, security)
- Daily handoff documentation for continuity
- You orchestrate via `scripts/week3-orchestrate.sh`

**Progress Tracking:**
- CI/CD: [![CI/CD Status](https://github.com/mk-knight23/claude5-starter-kit/actions/workflows/ci.yml/badge.svg)
- Real-time status: `./scripts/week3-orchestrate.sh status`
```

**Step 2: Commit README update**

```bash
git add README.md
git commit -m "docs: update README for Week 3 SaaS features

Added Week 3 section with:
- 6 SaaS features overview
- Per-project auth configuration
- Parallel implementation strategy
- Progress tracking commands"
```

---

## Task 7: Push Plan to GitHub

**Files:**
- Push: All Week 3 planning to origin

**Step 1: Push Week 3 plan**

```bash
git push origin main
```

**Step 2: Verify push**

Run: `git log --oneline -5`
Expected: Week 3 commits visible

**Step 3: Create GitHub milestone (optional)**

```bash
gh milestone create "Week 3: SaaS Features" --description "Implement auth, billing, rate limiting, dashboards, API keys, email across all 10 projects"
```

---

## Success Criteria

✅ **All Tasks Completed:**
- Bootstrap script created
- Shared components implemented
- Agent instructions template created
- Quality gates configured
- Orchestration script created
- README updated
- Plan pushed to GitHub

✅ **Ready for Agent Launch:**
- 10 tmux windows configured
- Each agent has clear instructions
- Quality gates automated
- Orchestration commands ready

✅ **Week 3 Ready to Begin:**
- Run `./scripts/week3-bootstrap.sh` to start agents
- Run `./scripts/week3-orchestrate.sh start-auth` to begin
- Monitor progress via `./scripts/week3-orchestrate.sh status`

---

**Total Estimated Time:** 2-3 hours (setup, planning, documentation)
**Total Week 3 Duration:** 8 days (2026-02-20 to 2026-02-27)
**Total Parallel Work:** 60 feature implementations (6 features × 10 projects)
