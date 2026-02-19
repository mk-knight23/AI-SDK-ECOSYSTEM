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
- Users can register
- Users can login/logout
- Protected routes work
- Sessions persist
- Tests pass (80%+ coverage)

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
- Checkout flow works
- Subscriptions created in Stripe
- Webhooks processed
- Billing dashboard shows plans/usage
- Tests pass

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
- Rate limits enforced
- Redis connection works
- Admins can bypass limits
- Tests pass

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
- Dashboard accessible to authenticated users
- Profile editing works
- Usage stats display correctly
- Billing history shows
- Tests pass

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
- Users can create keys
- Keys are hashed in database
- Keys can be revoked
- Usage tracked per key
- Tests pass

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
- Welcome emails sent on signup
- Password reset works
- Billing notifications sent
- Emails deliver successfully
- Tests pass

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

- All 6 features implemented
- All tests pass (80%+ coverage)
- All quality gates pass
- Manual testing confirms each feature works
- Handoff documents created daily
- Git history shows clean progression

---

**Start Date:** 2026-02-20
**Target Date:** 2026-02-27
**Duration:** 8 days
