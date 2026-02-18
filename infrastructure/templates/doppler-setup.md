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
doppler projects create dev-squad
doppler projects create supply-consensus
doppler projects create market-pulse
doppler projects create insight-stream
doppler projects create research-synthesis
doppler projects create trend-factory
doppler projects create patent-iq
doppler projects create claude-forge

# Setup environment
cd projects/01-venture-graph
doppler setup

# Add secrets
doppler secrets set OPENAI_API_KEY=sk-your-key

# Verify secrets are set
doppler secrets --project venture-graph

# Get specific secret
doppler secrets get OPENAI_API_KEY --project venture-graph
```

## Environment Configuration

Create environments for each project:
```bash
doppler environments create dev --project venture-graph
doppler environments create prod --project venture-graph
```

## Secret Rotation

To rotate a compromised key:
```bash
doppler secrets set OPENAI_API_KEY=new-key --project venture-graph
```

## Local Development

Export secrets to .env (ensure .env is gitignored):
```bash
doppler secrets download --format env --no-file > .env
```

## Security Best Practices

- Enable 2FA on your Doppler account
- Restrict production secrets to authorized team members only
- Never commit actual API keys to version control
- Rotate keys immediately if compromised
- Use separate keys for dev/staging/prod environments
