# Doppler API Key Setup

## Projects and Required Keys

| Project | Keys Needed |
|---------|-------------|
| 01-venture-graph | OPENAI_API_KEY |
| 02-omni-desk | OPENAI_API_KEY |
| 03-dev-squad | OPENAI_API_KEY |
| 04-supply-consensus | OPENAI_API_KEY |
| 05-market-pulse | GOOGLE_API_KEY |
| 06-insight-stream | OPENAI_API_KEY |
| 07-research-synthesis | OPENAI_API_KEY |
| 08-trend-factory | OPENAI_API_KEY |
| 09-patent-iq | OPENAI_API_KEY |
| 10-claude-forge | ANTHROPIC_API_KEY |

## Setup Commands

```bash
# Install Doppler CLI
curl -sLf https://cli.doppler.com/install.sh | sh

# Login
doppler login

# Create project for each
doppler projects create venture-graph
doppler projects create omni-desk
# ... etc

# Setup environment
cd projects/01-venture-graph
doppler setup

# Add secrets
doppler secrets set OPENAI_API_KEY=sk-your-key
```
