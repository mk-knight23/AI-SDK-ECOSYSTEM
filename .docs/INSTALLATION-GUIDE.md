# Claude5* - Complete Installation Guide

**Date:** 2026-02-18
**Purpose:** Step-by-step installation of all 5 ecosystems

---

## 🎯 Overview

Claude5* combines 5 major Claude Code ecosystems. This guide shows you how to install all of them.

**Total time:** ~15-20 minutes
**Difficulty:** Easy
**Requirements:** Claude Code installed

---

## 📦 Installation Steps

### Step 1: Install Superpowers

**What it does:** Workflow automation with auto-triggering skills

**Installation:**
```bash
# Register the Superpowers marketplace
/plugin marketplace add obra/superpowers-marketplace

# Install Superpowers plugin
/plugin install superpowers@superpowers-marketplace
```

**Verify:** Start a new session and say "help me plan this feature" - Superpowers should activate automatically.

**Repository:** https://github.com/obra/superpowers
**Stars:** 53.8k

---

### Step 2: Install Everything Claude Code

**What it does:** 13 specialized agents, 43 skills, 31 commands

**Installation:**
```bash
# Install via plugin marketplace
/plugin install affaan-m/everything-claude-code
```

**Verify:** Try the command `/plan` - you should see the planning agent activate.

**Repository:** https://github.com/affaan-m/everything-claude-code
**Stars:** 42k

---

### Step 3: Install UI UX Pro Max

**What it does:** Design intelligence with 50+ styles, 97 palettes, 57 fonts

**Installation:**
```bash
# Clone the skill to your Claude skills directory
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git ~/.claude/skills/ui-ux-pro-max
```

**Verify:** Say "build a login page with glassmorphism style" - UI UX Pro Max should suggest design patterns.

**Repository:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
**Stars:** 32.4k

---

### Step 4: Install Ralph Loop

**What it does:** Autonomous AI development loops

**Installation:**
```bash
# Download and run the installer
curl -fsSL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/install.sh | bash
```

**This installs commands:**
- `ralph` - Start autonomous loop
- `ralph-setup` - Initialize Ralph in a project
- `ralph-monitor` - Watch active loops
- `ralph-enable` - Enable Ralph for a project

**Verify:** Run `ralph --help` - you should see Ralph command options.

**Repository:** https://github.com/frankbria/ralph-claude-code
**Stars:** 7k

---

### Step 5: Install Claude Code Tips

**What it does:** 7 DX skills, system prompt patches, custom status bar

**Installation:**
```bash
# Install the dx plugin
/plugin install ykdojo/dx
```

**Verify:** Try `/dx:handoff` - you should see the handoff skill activate.

**Repository:** https://github.com/ykdojo/claude-code-tips
**Stars:** 2.9k

---

## ✅ Verification

After installing all 5 ecosystems, verify they're working:

### Test Superpowers
```
Say: "I want to add user authentication"
Expected: Superpowers activates brainstorming skill
```

### Test ECC
```
Run: /plan "Build a REST API"
Expected: Planning agent creates detailed plan
```

### Test UI UX Pro Max
```
Say: "Create a dashboard with dark mode"
Expected: Design intelligence provides patterns
```

### Test Ralph
```
Run: ralph --help
Expected: Ralph command help displays
```

### Test Claude Code Tips
```
Run: /dx:handoff
Expected: Handoff skill activates
```

---

## 🎯 What You Get After Installation

| Ecosystem | Stars | What It Provides |
|-----------|-------|------------------|
| **Superpowers** | 53.8k | Auto-triggering workflow skills |
| **ECC** | 42k | 13 agents, 43 skills, 31 commands |
| **UI UX Pro Max** | 32.4k | 50+ styles, 97 palettes, 57 fonts |
| **Ralph Loop** | 7k | Autonomous development loops |
| **Claude-Tips** | 2.9k | 7 DX skills, token optimization |

**Total: ~139k stars of combined expertise!**

---

## 🚀 Next Steps

### 1. Use Claude5* Starter Kit

```bash
# Clone the starter kit
git clone https://github.com/YOUR_USERNAME/claude5-starter-kit.git my-project
cd my-project

# Start working - the .claude/CLAUDE.md configures everything
# Just state your intent and all 5 ecosystems will work together!
```

### 2. Try a Complete Workflow

```
You: "I want to build a todo app with authentication"

What happens automatically:
1. ✅ Superpowers activates brainstorming
2. ✅ ECC architect agent designs system
3. ✅ ECC creates detailed plan
4. ✅ TDD workflow enforces tests
5. ✅ UI UX Pro Max provides design patterns
6. ✅ Code reviewer checks quality
7. ✅ Security reviewer validates
```

---

## 📚 Additional Resources

### Superpowers
- Repository: https://github.com/obra/superpowers
- Documentation: https://obra.github.io/superpowers-for-claude-code/

### Everything Claude Code
- Repository: https://github.com/affaan-m/everything-claude-code
- 13 agents, 43 skills, 31 commands

### UI UX Pro Max
- Repository: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Design database with 50+ styles, 97 palettes

### Ralph Loop
- Repository: https://github.com/frankbria/ralph-claude-code
- Autonomous development loops

### Claude-Tips
- Repository: https://github.com/ykdojo/claude-code-tips
- DX skills and optimization tips

---

## 💡 Key Concepts

### Global Installation

All 5 ecosystems are installed **once globally**:
- Superpowers: `~/.claude/plugins/cache/claude-plugins-official/superpowers/`
- ECC: `~/.claude/plugins/cache/everything-claude-code/`
- UI UX Pro Max: `~/.claude/skills/ui-ux-pro-max/`
- Ralph Loop: `~/.ralph/` and `~/.local/bin/ralph*`
- Claude-Tips: `~/.claude/plugins/cache/ykdojo/dx/`

### Project Configuration

Each Claude5* project contains `.claude/CLAUDE.md` which tells Claude:
- HOW to use the 5 ecosystems together
- WHEN to trigger each ecosystem
- WHAT workflow to follow

### One-Time Setup

Install ecosystems once, use them in ALL projects:
```bash
# Install once (global)
/install ecosystems

# Use everywhere (per project)
git clone claude5-starter-kit project1
git clone claude5-starter-kit project2
git clone claude5-starter-kit project3
```

---

## ❓ FAQ

**Q: Do I need to reinstall ecosystems for each project?**
A: No! Install once globally, use everywhere.

**Q: Can I use ecosystems without Claude5* starter kit?**
A: Yes, but Claude5* provides the configuration to make them work TOGETHER effectively.

**Q: How much disk space do they take?**
A: About 100-200MB total for all 5 ecosystems.

**Q: Can I install just some ecosystems?**
A: Yes, but you'll get the most value from all 5 working together.

**Q: Do I need to update the ecosystems?**
A: They'll update automatically via their respective install methods.

---

**Installation Guide Complete!**

You now have all 5 ecosystems installed and ready to use with Claude5* starter kit.

Next: [Learn how to use Claude5*](WORKING-METHOD.md)

---

*Last updated: 2026-02-18*
*Claude5* Starter Kit*
