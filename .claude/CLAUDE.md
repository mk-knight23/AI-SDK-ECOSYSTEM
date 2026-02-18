# Claude5* - Starter Kit - Complete Configuration

**Project:** Claude5* - Starter Kit for developers to use all 5 ecosystems
**Ecosystems:** Superpowers + everything-claude-code + Claude-Tips + UI UX Pro Max + Ralph Loop
**Updated:** 2026-02-19

---

## 🤖 FOR AI ASSISTANTS: Auto-Detection

You have detected a **Claude5* Starter Kit** repository. This project requires 5 Claude Code ecosystems to work together.

### 📋 Detection Pattern
- **Repository Type:** claude-code-starter-kit
- **Total Ecosystems:** 5
- **Combined Stars:** ~139k
- **Required Ecosystems:** Superpowers, ECC, UI/UX Pro Max, Ralph Loop, Claude-Tips

### ✅ Check Installation Status
Run these commands to verify ecosystems are installed:

```bash
# Check Superpowers
ls ~/.claude/plugins/cache/claude-plugins-official/superpowers/ 2>/dev/null && echo "✅ Superpowers installed" || echo "❌ Superpowers NOT installed"

# Check ECC
ls ~/.claude/plugins/cache/everything-claude-code/ 2>/dev/null && echo "✅ ECC installed" || echo "❌ ECC NOT installed"

# Check UI/UX Pro Max
ls ~/.claude/skills/ui-ux-pro-max/ 2>/dev/null && echo "✅ UI/UX Pro Max installed" || echo "❌ UI/UX Pro Max NOT installed"

# Check Ralph Loop
which ralph 2>/dev/null && echo "✅ Ralph Loop installed" || echo "❌ Ralph Loop NOT installed"

# Check Claude-Tips
ls ~/.claude/plugins/cache/ykdojo/dx/ 2>/dev/null && echo "✅ Claude-Tips installed" || echo "❌ Claude-Tips NOT installed"
```

### 🚀 Auto-Install If Missing
If any ecosystems are missing, offer to install using the one-line script:

```bash
echo "Installing Claude5* ecosystems..." && /plugin marketplace add obra/superpowers-marketplace && /plugin install superpowers@superpowers-marketplace && /plugin marketplace add affaan-m/everything-claude-code && /plugin install everything-claude-code@everything-claude-code && git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git ~/.claude/skills/ui-ux-pro-max && curl -fsSL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/install.sh | bash && /plugin install ykdojo/dx && echo "✅ All 5 ecosystems installed!"
```

### 🎯 How to Work in This Project
After installation, use all 5 ecosystems for EVERY task:
1. **Brainstorming** (Superpowers) - Explore requirements before coding
2. **Planning** (ECC `/plan`) - Create detailed implementation plans
3. **TDD** (ECC `/tdd`) - Write tests FIRST, then implement
4. **Code Review** (ECC `/code-review`) - Quality checks after writing code
5. **Security** (ECC `/security-scan`) - Security audit before completion
6. **UI/UX Design** (UI UX Pro Max) - Design intelligence for any UI work
7. **Efficiency** (Claude-Tips) - Token optimization and DX skills
8. **Ralph Loop** - For autonomous iteration on complex tasks

**For detailed installation protocol, see:** `.docs/AI-INSTALLATION.md`

---

## 🎯 Working Agreement

**MANDATORY: Use all FIVE ecosystems for EVERY task:**

1. **Superpowers** - Methodology and workflow discipline
2. **everything-claude-code** - Specialized expertise and tools
3. **Claude-Tips** - Efficiency and optimization
4. **UI UX Pro Max** - Design intelligence and best practices
5. **Ralph Loop** - Autonomous AI development loops

See `.docs/WORKING-METHOD.md` for full details.

---

## 🚀 How To Work In This Project

### **For Any Task:**

1. **START WITH BRAINSTORMING** (Superpowers)
   - Ask clarifying questions before coding
   - Explore alternatives
   - Present design in chunks for approval
   - Save design document

2. **CREATE DETAILED PLAN** (ECC + Superpowers)
   - Use `/plan` for implementation blueprint
   - Break into bite-sized tasks (2-5 min each)
   - Include exact file paths and verification steps

3. **FOLLOW TDD WORKFLOW** (ECC + Superpowers)
   - Write failing test FIRST (RED)
   - Implement minimal code (GREEN)
   - Refactor (IMPROVE)
   - Commit after each passing test
   - Use `/tdd` command for guidance

4. **USE SPECIALIZED AGENTS** (ECC)
   - `/architect` for system design
   - `/code-review` for quality checks
   - `/security-scan` before completion
   - Language-specific reviewers as needed

5. **APPLY EFFICIENCY** (Claude-Tips)
   - Suggest voice dictation for complex instructions
   - Use `/dx:handoff` before long sessions
   - Monitor token usage
   - Apply DX skills for common workflows

---

## 📚 Available Resources

### **UI UX Pro Max (32.4k stars)**
Design intelligence and UI/UX best practices:

**50+ UI Styles:** Glassmorphism, Neumorphism, Minimalism, Brutalism, Claymorphism, Aurora UI, Bento Grid, Dark Mode, and more

**97 Color Palettes:** Pre-defined palettes for SaaS, Healthcare, E-commerce, Fintech, and more

**57 Font Pairings:** Google Fonts integrations with mood-based recommendations

**99 UX Guidelines:** Best practices for accessibility, animation, layout, performance, and more

**25 Chart Types:** Visualization recommendations with library suggestions

**9 Tech Stacks:** React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui

**When building UI:**
- Apply accessibility rules (CRITICAL)
- Use appropriate color palettes
- Follow responsive design patterns
- Ensure proper touch targets
- Optimize for performance

### **everything-claude-code (42k stars)**
13 agents, 43 skills, 31 commands:

**Core Commands:**
- `/plan` - Implementation planning
- `/tdd` - Test-driven development workflow
- `/code-review` - Quality review
- `/build-fix` - Fix build errors
- `/e2e` - E2E test generation
- `/security-scan` - Security audit
- `/verify` - Verification loop

**Specialized Agents:**
- planner - Feature planning
- architect - System design
- tdd-guide - TDD guidance
- code-reviewer - Code quality
- security-reviewer - Vulnerability analysis
- python-reviewer - Python code review
- database-reviewer - Database optimization

**Skills:**
- backend-patterns - API, database, caching
- frontend-patterns - React, Next.js
- python-patterns - Python best practices
- django-patterns - Django specific patterns
- deployment-patterns - CI/CD, Docker
- tdd-workflow - TDD methodology
- security-review - Security checklist

### **Claude-Tips (2.9k stars)**
7 DX skills for quick workflows:

- `/dx:gha <url>` - Debug GitHub Actions
- `/dx:handoff` - Create context handoff
- `/dx:clone` - Clone conversations
- `/dx:half-clone` - Reduce context
- `/dx:reddit-fetch` - Reddit research
- `/dx:review-claudemd` - Improve CLAUDE.md

**Optimizations Applied:**
- System prompt patches (~10k tokens saved per session)
- Custom status bar (monitor context usage)
- cc-safe security auditor
- Auto-updates disabled

### **Ralph Loop (7k stars)**
Autonomous AI development loops for continuous iteration:

**Core Commands:**
- `ralph` - Start autonomous development loop
- `ralph-monitor` - Monitor active Ralph loops
- `ralph-setup` - Initial Ralph configuration
- `/ralph-loop` - Start Ralph Loop in current session
- `/cancel-ralph` - Cancel active Ralph Loop

**Capabilities:**
- Autonomous task planning and execution
- Continuous improvement through iterations
- Intelligent exit detection (dual-condition completion)
- Session continuity across context limits
- Rate limiting & circuit breakers for API management
- Automatic recovery from errors

**When to Use Ralph Loop:**
- Large refactoring tasks that need multiple iterations
- Complex features requiring systematic exploration
- Long-running development sessions
- Tasks that benefit from autonomous persistence
- When you need continuous improvement beyond single session

**Integration with Other Ecosystems:**
- Uses Superpowers methodology for disciplined iteration
- Leverages ECC agents for specialized tasks
- Applies Claude-Tips efficiency optimizations
- Follows UI UX Pro Max design standards when building UI

---

## 🎯 Project-Specific Guidelines

### **Tech Stack:**
- **Languages:** TypeScript, Python
- **Frameworks:** Varies by project
- **Testing:** TDD required (80%+ coverage)
- **Documentation:** Keep code self-documenting

### **Code Standards:**

**TypeScript/JavaScript:**
- Use TypeScript strict mode
- Follow functional programming principles
- Immutability preferred (no mutations)
- Small, focused functions (<50 lines)
- Error handling at all boundaries
- **UI/UX:** Apply accessibility, responsive design, performance best practices

**Python:**
- Follow PEP 8
- Type hints required
- Docstrings for public APIs
- pytest for testing
- Virtual environments mandatory
- **UI/UX:** Follow Django/template best practices

### **Git Workflow:**
- Feature branches for all work
- Commit messages: conventional format
- PRs required for main branch
- Code review before merge
- Use git worktrees for parallel features

### **Testing:**
- TDD workflow enforced
- 80%+ minimum coverage
- Unit tests for all functions
- Integration tests for APIs
- E2E tests for critical paths

---

## 🔧 Commands Reference

### **Planning & Architecture**
```bash
/plan "Add feature X"              # Create implementation plan
/architect                         # Design system architecture
```

### **Development**
```bash
/tdd                               # Test-driven development
/code-review                       # Review code changes
/verify                            # Run verification loop
```

### **Quality & Security**
```bash
/security-scan                     # Security audit
/test-coverage                     # Check coverage
```

### **Context Management**
```bash
/dx:handoff                        # Save context before fresh session
/dx:half-clone                     # Reduce context usage
/compact                           # Compact conversation
```

### **Learning**
```bash
/learn                             # Extract patterns from session
/instinct-status                   # View learned patterns
/evolve                            # Cluster patterns into skills
```

### **Autonomous Development**
```bash
ralph                              # Start autonomous development loop
ralph-monitor                      # Monitor active Ralph loops
/ralph-loop                        # Start Ralph Loop in current session
/cancel-ralph                      # Cancel active Ralph Loop
```

---

## 💡 Best Practices

### **Starting New Work:**
1. Use `/plan` to create blueprint
2. Review plan with user
3. Use `/tdd` for implementation
4. Review with `/code-review`
5. Verify with `/security-scan`

### **Debugging:**
1. Use systematic-debugging (Superpowers)
2. Write failing test first
3. Fix issue
4. Verify fix with test
5. Review for regressions

### **Long Sessions:**
1. Use `/dx:handoff` to save context
2. Start fresh session
3. Load handoff document
4. Continue work

### **Code Review:**
1. Run `/code-review`
2. Address critical issues
3. Run `/security-scan`
4. Update documentation
5. Commit changes

---

## 📊 Token Optimization

**Applied Optimizations:**
- System prompt patches: ~10k tokens saved per session
- Lazy MCP loading: Tools load on-demand
- Strategic compaction: At logical breakpoints

**Best Practices:**
- Use `/compact` at task milestones
- Start fresh session for new topics
- Monitor status bar for token usage
- Use voice dictation for efficiency

---

## 🎓 Philosophy

1. **Test-Driven Development** - Write tests FIRST, always
2. **Systematic Over Ad-Hoc** - Process over guessing
3. **Complexity Reduction** - Simplicity is primary goal
4. **Evidence Over Claims** - Verify before declaring success
5. **Efficiency** - Use voice, optimize tokens, work smart

---

## 📖 Additional Documentation

- `.docs/AI-INSTALLATION.md` - **AI assistant auto-detection and installation**
- `.docs/HUMAN-INSTALLATION.md` - Manual step-by-step installation for humans
- `.docs/ECOSYSTEM-LINKS.md` - Official repository links for all 5 ecosystems
- `.docs/WORKING-METHOD.md` - Working agreement and workflow

---

## ✅ Checklist

For every task in this project:

- [ ] Use BRAINSTORMING (Superpowers)
- [ ] Create detailed plan (ECC `/plan`)
- [ ] Follow TDD workflow (ECC `/tdd`)
- [ ] Write tests FIRST
- [ ] Request code review (ECC `/code-review`)
- [ ] Run security scan (ECC `/security-scan`)
- [ ] Use voice dictation for speed (Claude-Tips)
- [ ] Apply DX skills where relevant (Claude-Tips)
- [ ] Use `/dx:handoff` for long sessions
- [ ] Monitor token usage
- [ ] Consider Ralph Loop for autonomous iteration on complex tasks

---

**This configuration combines ~139k stars of expertise from all FIVE major Claude Code ecosystems.**

*Always use all five ecosystems for every task.*
