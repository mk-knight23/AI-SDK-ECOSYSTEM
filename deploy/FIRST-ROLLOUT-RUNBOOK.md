# First Rollout Runbook (LangGraph + OpenAI Agents)

## Preconditions
- GitHub Actions enabled on repository.
- Repository secrets configured:
  - OPENAI_API_KEY
  - ANTHROPIC_API_KEY
  - DEPLOY_KUBECONFIG_B64
- Kubernetes cluster has network ingress configured for services.

## Step 1: Build and Push Images
Trigger workflow: `adapters-build-push`.
- Wait for successful completion.
- Capture image tag from workflow output (`sha-...` recommended).

## Step 2: Deploy LangGraph to Staging
Trigger workflow: `adapters-deploy-manual` with:
- adapter: `langgraph`
- environment: `staging`
- image_tag: `<sha-tag>`

Validate:
- `kubectl get pods -n staging | grep kazi-agents-langgraph`
- `kubectl rollout status deploy/kazi-agents-langgraph -n staging`

## Step 3: Deploy OpenAI Agents to Staging
Trigger workflow: `adapters-deploy-manual` with:
- adapter: `openai_agents`
- environment: `staging`
- image_tag: `<sha-tag>`

Validate:
- `kubectl get pods -n staging | grep kazi-agents-openai_agents`
- `kubectl rollout status deploy/kazi-agents-openai_agents -n staging`

## Step 4: Runtime Checks
Port-forward and test:

```bash
kubectl port-forward svc/kazi-agents-langgraph 18001:80 -n staging
curl http://localhost:18001/health
curl -X POST http://localhost:18001/run -H 'content-type: application/json' -d '{"mission":"orchestrate secure deploy"}'

kubectl port-forward svc/kazi-agents-openai_agents 18002:80 -n staging
curl http://localhost:18002/health
curl -X POST http://localhost:18002/run -H 'content-type: application/json' -d '{"mission":"build incident response workflow"}'
```

## Step 5: Promote to Production
Repeat steps 2-4 with `environment=production`.

## Rollback
```bash
kubectl rollout undo deploy/kazi-agents-langgraph -n production
kubectl rollout undo deploy/kazi-agents-openai_agents -n production
```
