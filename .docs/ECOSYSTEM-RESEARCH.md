# Ecosystem Implementation Research

**Date:** 2026-02-18
**Purpose:** Understand how each of the 5 ecosystems implements their approach

---

## 📚 Summary

All 5 ecosystems are **installed globally** and configured via **.claude/CLAUDE.md** in each project.

---

## Installation Commands

### 1. Superpowers
```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### 2. Everything Claude Code  
```bash
/plugin install affaan-m/everything-claude-code
```

### 3. UI UX Pro Max
```bash
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git ~/.claude/skills/ui-ux-pro-max
```

### 4. Ralph
```bash
curl -fsSL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/install.sh | bash
```

### 5. Claude-Tips
```bash
/plugin install ykdojo/dx
```

---

## How They Work

### Superpowers - Auto-Triggering Workflow
- Activates BEFORE tasks (brainstorming, planning)
- Activates DURING tasks (TDD, code review)
- Activates AFTER tasks (verification, cleanup)
- **No manual invocation needed**

### ECC - Specialized Tools
- 13 agents (architect, security-reviewer, etc.)
- 43 skills (backend-patterns, frontend-patterns, etc.)
- 31 commands (/plan, /tdd, /code-review, etc.)
- **Manual invocation - you decide when**

### UI UX Pro Max - Design Intelligence
- 50+ UI styles, 97 color palettes, 57 fonts
- Auto-applies when building UI
- Accessibility rules enforced automatically
- **Works automatically**

### Ralph Loop - Autonomous Loops
- Continuous iteration without intervention
- Session continuity across context limits
- Intelligent exit detection
- **Deploy for long-running tasks**

### Claude-Tips - Efficiency
- 7 DX skills (/dx:handoff, /dx:gha, etc.)
- System prompt patches (~10k tokens saved)
- Custom status bar (token monitoring)
- **Use when needed**

---

## Key Insight

**Claude5* is CONFIGURATION, not a library:**

✅ Includes: .claude/CLAUDE.md (configuration)
✅ Includes: Documentation and guides
✅ Includes: GitHub templates

❌ Does NOT include: Ecosystem files (installed globally)
❌ Does NOT include: Source code (it's a template)

---

*Research completed: 2026-02-18*
