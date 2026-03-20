# Secrets Checklist

## GitHub Repository Secrets
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `DEPLOY_KUBECONFIG_B64` (base64-encoded kubeconfig)

## Optional
- `LANGSMITH_API_KEY`
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

## Validation
Run local validator before triggering deploy:

```bash
./deploy/scripts/validate_env.sh
```
