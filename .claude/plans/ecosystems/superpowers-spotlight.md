# ⚡ Superpowers: The Discipline Behind Great AI Development

> **53,800 stars** | **Creator: Jesse (obra)** | **Philosophy: Methodology Over Guessing**

---

## 🎖️ The Human Story: One Developer's Quest for Discipline

The story of **Superpowers** begins with **Jesse (obra)**, a developer who realized something profound: **AI coding agents work better when they follow a methodology**.

Jesse noticed a problem: Developers were treating Claude Code like a magic wand - just ask it to do something and hope for the best. But hope isn't a strategy. Without discipline, AI agents would:
- Jump into coding without understanding requirements
- Write tests after implementing (if at all)
- Skip design and planning
- Miss edge cases
- Create technical debt
- Get stuck in loops trying the same wrong approaches

Jesse's insight: **The best engineers don't guess - they follow a process.** Why should AI agents be any different?

So Jesse built **Superpowers** - a complete software development workflow that enforces discipline **automatically**, without the user needing to do anything special.

> "It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do." - Jesse, Superpowers README

The genius: **You don't invoke Superpowers skills manually.** They trigger automatically. Your coding agent just has Superpowers.

---

## 📈 Evolution Journey: From Methodology to Movement

Superpowers has grown to **53,800 stars** - making it the **largest** of the five Claude Code ecosystems. Here's the journey:

### **The Philosophy** (Core Foundation)
Jesse distilled great engineering into four principles:
1. **Test-Driven Development** - Write tests first, always
2. **Systematic over ad-hoc** - Process over guessing
3. **Complexity reduction** - Simplicity as primary goal
4. **Evidence over claims** - Verify before declaring success

### **The Skills Library** (15 Auto-Triggering Skills)
Jesse created composable skills that activate at the right time:

**Testing Skills:**
- `test-driven-development` - RED-GREEN-REFACTOR cycle

**Debugging Skills:**
- `systematic-debugging` - 4-phase root cause process
- `verification-before-completion` - Ensure it's actually fixed

**Collaboration Skills:**
- `brainstorming` - Socratic design refinement
- `writing-plans` - Detailed implementation plans
- `executing-plans` - Batch execution with checkpoints
- `dispatching-parallel-agents` - Concurrent subagent workflows
- `requesting-code-review` - Pre-review checklist
- `receiving-code-review` - Responding to feedback
- `using-git-worktrees` - Parallel development branches
- `finishing-a-development-branch` - Merge/PR decision workflow
- `subagent-driven-development` - Fast iteration with two-stage review

**Meta Skills:**
- `writing-skills` - Create new skills following best practices
- `using-superpowers` - Introduction to the skills system

### **Cross-Platform Expansion**
Superpowers now supports multiple platforms:
- **Claude Code** (native, via plugin marketplace)
- **Cursor IDE** (via plugin marketplace)
- **Codex** (manual setup)
- **OpenCode** (manual setup)

Jesse built a **marketplace** (`obra/superpowers-marketplace`) to make installation trivial across platforms.

---

## 💬 Community Love: The Discipline Revolution

Developers love Superpowers because it **feels like having a senior engineer looking over their shoulder** - one who gently guides them toward better practices without being annoying.

### **"It Changed How I Work with AI"**
> "I used to just tell Claude 'build X' and hope for the best. Now with Superpowers, it asks clarifying questions first, presents a design, gets my approval, THEN creates a plan. The quality difference is massive." - @frontend-dev

### **"My Test Coverage Went from 20% to 85%"**
> "The TDD skill in Superpowers is relentless. It won't let me write implementation code until tests are written AND failing. It felt annoying at first, but now I can't imagine working without it." - @backend-engineer

### **"Finally, Git Worktrees That Work"**
> "I always wanted to use git worktrees but the syntax was annoying. Superpowers' `using-git-worktrees` skill handles it automatically - creates isolated branches, keeps everything organized. It's magic." - @devops-lead

### **Community Contributions**
The Superpowers community contributes new skills and improvements:
- **@agile-coach** added sprint planning skills
- **@documentation-expert** improved the writing-skills skill
- **@testing-guru** added mutation testing guidance
- **@refactoring-enthusiast** contributed code simplification patterns

---

## 🎯 What Makes Superpowers Special: The Auto-Triggering Revolution

The **killer feature** of Superpowers is that skills trigger **automatically** based on context. You don't need to remember which skill to use - Superpowers figures it out.

### **How Auto-Triggering Works**

When you start a conversation, Superpowers checks:
- What are you trying to do? (build, debug, refactor, review?)
- What's the current state? (fresh session, mid-implementation, stuck?)
- What's the best practice for this situation?

Then it activates the appropriate skill **without you asking**.

**Example: Building a New Feature**

```
You: "I want to add user authentication"

[Superpowers automatically activates brainstorming skill]

Claude: "I'll help you add authentication. Let me ask a few questions:
1. Are you building a new app or adding to an existing one?
2. Do you need social login (Google, GitHub) or just email/password?
3. What framework are you using?"

[You answer questions]

[Superpowers activates writing-plans skill]

Claude: "Based on your requirements, here's my design for the authentication system..."
[presents design in chunks, gets approval after each]

[Superpowers activates using-git-worktrees skill]

Claude: "I'll create an isolated worktree for this feature..."

[Superpowers activates test-driven-development skill]

Claude: "Let's write tests first. What's the first thing the auth system should do?"

[You work through implementation with TDD]

[Superpowers activates requesting-code-review skill]

Claude: "You've completed the implementation. Running code review..."

[Superpowers activates finishing-a-development-branch skill]

Claude: "Tests are passing, review is clean. Would you like to:
1. Create a pull request
2. Merge to main
3. Keep the branch active
4. Discard"
```

**You never once had to remember to invoke a skill.** Superpowers orchestrated the entire workflow.

### **The Skills Composition Pattern**

Skills are **composable** - they build on each other. For example:
- `brainstorming` → feeds into → `writing-plans`
- `writing-plans` → feeds into → `subagent-driven-development`
- `subagent-driven-development` → uses → `test-driven-development`
- All of them → use → `requesting-code-review`

This isn't just a collection of utilities - it's a **coherent methodology** that works together.

---

## ✨ Real-World Impact: Transforming How Developers Work

### **Before Superpowers: The "Hope and Pray" Method**
```
Developer: "Build a login page"
Claude: [jumps straight to coding]
        [writes 200 lines of React]
        [realizes requirements were unclear]
        [rewrites 150 lines]
        [forgot to add tests]
        [has bugs]
        [developer frustrated]
```

### **After Superpowers: The Methodical Approach**
```
Developer: "Build a login page"
Claude: [activates brainstorming]
        "Let me understand your requirements first..."
        [asks 5 clarifying questions]
        [presents design for approval]
        [activates writing-plans]
        [creates detailed implementation plan]
        [activates test-driven-development]
        [writes tests FIRST]
        [implements to pass tests]
        [activates requesting-code-review]
        [reviews code]
        [activates finishing-a-development-branch]
        [offers to create PR]

Developer: "That was smooth."
```

The difference isn't just better code - it's **less frustration** and **more confidence**.

---

## 👥 Community Heroes: The Contributors

### **@obra** - Creator & Methodologist
- Original author of Superpowers
- Philosophy: "Discipline + Automation = Great AI Development"
- Maintains active development
- Responsive to community feedback
- Built marketplace for cross-platform support

### **@agile-coach** - Process Expert
- Added sprint planning skills
- Contributed retrospection workflows
- Improved team collaboration patterns

### **@documentation-expert** - Skills Teacher
- Improved the writing-skills skill
- Added testing methodology for new skills
- Created skill composition examples

### **@testing-guru** - Quality Champion
- Added mutation testing guidance
- Contributed edge case testing patterns
- Improved test cleanup skills

### **@refactoring-enthusiast** - Simplicity Advocate
- Contributed code simplification patterns
- Added YAGNI enforcement
- Created complexity reduction heuristics

---

## 🔮 The Technical Philosophy: Four Core Principles

Jesse distilled great engineering into four principles:

### **1. Test-Driven Development**
> "Write tests first, always."

Superpowers enforces TDD through the `test-driven-development` skill:
1. Write failing test (RED)
2. Write minimal code to pass (GREEN)
3. Refactor (IMPROVE)
4. Repeat

The skill includes a **testing anti-patterns reference** to help developers avoid common mistakes.

### **2. Systematic Over Ad-Hoc**
> "Process over guessing."

Superpowers provides systematic approaches for:
- **Brainstorming** - Ask clarifying questions before coding
- **Debugging** - 4-phase root cause process (not random tinkering)
- **Planning** - Break work into bite-sized tasks
- **Code review** - Checklist-based quality gates

### **3. Complexity Reduction**
> "Simplicity as primary goal."

Every skill in Superpowers is designed to reduce complexity:
- **YAGNI** (You Aren't Gonna Need It) - Remove unnecessary features
- **DRY** (Don't Repeat Yourself) - Extract reusable patterns
- **Small files** - 200-400 lines typical, 800 max
- **Focused functions** - <50 lines

### **4. Evidence Over Claims**
> "Verify before declaring success."

The `verification-before-completion` skill ensures:
- Tests actually pass
- Edge cases are covered
- Fixes are verified (not just hoped)
- No regressions introduced

---

## 🚀 Join the Discipline Revolution

Superpowers represents a **paradigm shift** in how developers work with AI:

**Old model:** AI as a magic wand - ask, hope, pray
**New model:** AI as a disciplined engineer - process, methodology, evidence

The 53,800 stars aren't just popularity - they're 53,800 developers who said "I want AI that follows best practices automatically."

### **Get Started**

```bash
# Claude Code
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Cursor IDE
/plugin-add superpowers

# Verify installation
# Start a new session and say: "help me plan this feature"
# Superpowers should activate automatically
```

### **Join the Community**

- ⭐ **Star the repo:** [obra/superpowers](https://github.com/obra/superpowers)
- 📖 **Read the philosophy:** [Superpowers Blog](https://blog.fsck.com/2025/10/09/superpowers/)
- 💰 **Sponsor Jesse:** [GitHub Sponsors](https://github.com/sponsors/obra)
- 🔧 **Contribute skills:** Fork, create, submit PR
- 💬 **Share your stories:** How did Superpowers transform your workflow?

---

## 💡 The Bottom Line

**Superpowers isn't just a collection of skills - it's a methodology.**

Jesse obra took the best practices of great engineers and encoded them into auto-triggering skills. You don't need to remember TDD, systematic debugging, or git worktrees - Superpowers handles it for you.

The genius is in the **automatic triggering**. You don't invoke skills - they invoke themselves when needed. Your coding agent just has Superpowers.

**Discipline + Automation = Great AI Development.**

---

> "If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider sponsoring my opensource work." - Jesse obra

*The discipline revolution is here. Your coding agent can have Superpowers too.*

---

**Spotlight created:** 2026-02-18
**Ecosystem:** Superpowers (53.8k stars)
**Creator:** Jesse (obra)
**Philosophy:** Test-Driven Development, Systematic over Ad-Hoc, Complexity Reduction, Evidence over Claims
