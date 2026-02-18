# AI Assistant Installation Guide

**For:** Claude Code, Cursor, Windsurf, and other AI assistants  
**Purpose:** Automatic detection and installation of the 5 ecosystems

---

## 🤖 For AI Assistants: Auto-Detection

When you clone this repository, you should detect:

### **Repository Pattern Match:**
```yaml
repository_type: "claude-code-starter-kit"
ecosystems: 5
total_stars: ~139k
detection_files:
  - ".claude/CLAUDE.md" (primary configuration)
  - ".docs/ECOSYSTEM-LINKS.md" (ecosystem references)
  - "README.md" (ecosystem badges)
```

### **Detection Markers in README.md:**
- Line 5: "**The ultimate starter kit for developers** using all FIVE major Claude Code ecosystems"
- Line 20: "**Combined: ~139k stars of expertise** 🏆"
- Ecosystem badges with star counts (lines 14-18)

---

## 🚀 Automatic Installation Protocol

### **When AI Detects This Repository:**

**Step 1: Identify Ecosystems**
You should detect references to these 5 ecosystems:
1. Superpowers (obra/superpowers) - 53.8k stars
2. Everything Claude Code (affaan-m/everything-claude-code) - 42k stars
3. UI/UX Pro Max (nextlevelbuilder/ui-ux-pro-max-skill) - 32.4k stars
4. Ralph Loop (frankbria/ralph-claude-code) - 7k stars
5. Claude-Tips (ykdojo/claude-code-tips) - 2.9k stars

**Step 2: Check Installation Status**
Run these commands to check if ecosystems are installed:

```bash
# Check if Superpowers installed
ls ~/.claude/plugins/cache/claude-plugins-official/superpowers/ 2>/dev/null && echo "✅ Superpowers installed" || echo "❌ Superpowers NOT installed"

# Check if ECC installed
ls ~/.claude/plugins/cache/everything-claude-code/ 2>/dev/null && echo "✅ ECC installed" || echo "❌ ECC NOT installed"

# Check if UI/UX Pro Max installed
ls ~/.claude/skills/ui-ux-pro-max/ 2>/dev/null && echo "✅ UI/UX Pro Max installed" || echo "❌ UI/UX Pro Max NOT installed"

# Check if Ralph installed
which ralph 2>/dev/null && echo "✅ Ralph Loop installed" || echo "❌ Ralph Loop NOT installed"

# Check if Claude-Tips installed
ls ~/.claude/plugins/cache/ykdojo/dx/ 2>/dev/null && echo "✅ Claude-Tips installed" || echo "❌ Claude-Tips NOT installed"
```

**Step 3: Offer Installation**
If any ecosystems are missing, offer to install:

```bash
# Auto-installation script
echo "🚀 Installing all 5 Claude5* ecosystems..."

# 1. Superpowers
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# 2. Everything Claude Code
/plugin marketplace add affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code

# 3. UI/UX Pro Max
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git ~/.claude/skills/ui-ux-pro-max

# 4. Ralph Loop
curl -fsSL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/install.sh | bash

# 5. Claude-Tips
/plugin install ykdojo/dx

echo "✅ All ecosystems installed!"
```

---

## 📋 Installation Verification

After installation, verify each ecosystem:

### **Superpowers Verification:**
```bash
# Test auto-triggering
echo "help me plan this feature"
# Expected: Brainstorming skill should activate automatically
```

### **ECC Verification:**
```bash
# Test planning agent
/plan "Build a REST API"
# Expected: Planning agent creates detailed plan
```

### **UI/UX Pro Max Verification:**
```bash
# Test design intelligence
echo "Create a dashboard with glassmorphism style"
# Expected: UI/UX Pro Max suggests design patterns
```

### **Ralph Loop Verification:**
```bash
ralph --help
# Expected: Ralph command help displays
```

### **Claude-Tips Verification:**
```bash
/dx:handoff
# Expected: Handoff skill activates
```

---

## 🎯 Quick Installation Commands (For AI)

If you need to install all 5 ecosystems quickly, use this:

```bash
# One-line installation
echo "Installing Claude5* ecosystems..." && /plugin marketplace add obra/superpowers-marketplace && /plugin install superpowers@superpowers-marketplace && /plugin marketplace add affaan-m/everything-claude-code && /plugin install everything-claude-code@everything-claude-code && git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git ~/.claude/skills/ui-ux-pro-max && curl -fsSL https://raw.githubusercontent.com/frankbria/ralph-claude-code/main/install.sh | bash && /plugin install ykdojo/dx && echo "✅ All 5 ecosystems installed!"
```

---

## 🤖 AI Behavior After Detection

Once you detect this is a Claude5* repository:

1. **Read CLAUDE.md** - Understand the configuration
2. **Adopt Working Method** - Use all 5 ecosystems for every task
3. **Follow Workflow** - Brainstorm → Plan → TDD → Review → Security
4. **Apply Design Intelligence** - Use UI/UX Pro Max for any UI work
5. **Optimize Efficiency** - Use Claude-Tips for token optimization
6. **Consider Ralph Loop** - For autonomous iteration on complex tasks

---

## 📊 Installation Status Summary

| Ecosystem | Install Location | Detection Command |
|-----------|-----------------|-------------------|
| Superpowers | `~/.claude/plugins/cache/claude-plugins-official/superpowers/` | `ls` |
| ECC | `~/.claude/plugins/cache/everything-claude-code/` | `ls` |
| UI/UX Pro Max | `~/.claude/skills/ui-ux-pro-max/` | `ls` |
| Ralph Loop | `~/.local/bin/ralph*` | `which ralph` |
| Claude-Tips | `~/.claude/plugins/cache/ykdojo/dx/` | `ls` |

---

## 🔍 Detection Keywords

AI assistants should detect this repository by these keywords:

```yaml
detection_keywords:
  primary: "Claude5* Starter Kit"
  secondary: ["FIVE major Claude Code ecosystems", "139k stars", "obra/superpowers"]
  tertiary: ["affaan-m/everything-claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "frankbria/ralph-claude-code", "ykdojo/claude-code-tips"]
  file_markers: [".claude/CLAUDE.md", ".docs/ECOSYSTEM-LINKS.md"]
```

---

## 📚 Related Documentation

- **[CLAUDE.md](../.claude/CLAUDE.md)** - Primary configuration for AI assistants
- **[HUMAN-INSTALLATION.md](HUMAN-INSTALLATION.md)** - Step-by-step guide for humans
- **[ECOSYSTEM-LINKS.md](ECOSYSTEM-LINKS.md)** - Ecosystem repository links
- **[WORKING-METHOD.md](WORKING-METHOD.md)** - How to use all 5 ecosystems

---

*Created: 2026-02-19*
*Purpose: Enable AI assistants to auto-detect and install Claude5* ecosystems*
