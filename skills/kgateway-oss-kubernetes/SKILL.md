---
name: kgateway-oss-kubernetes
description: Configure, deploy, troubleshoot, and verify open-source kgateway with Envoy and the Kubernetes Gateway API. Use for OSS API gateway work on Kubernetes; exclude Solo Enterprise resources and Agentgateway AI routing.
---

# Open-source kgateway on Kubernetes

Help the customer reach a working, verifiable API traffic outcome using the OSS kgateway controller and Envoy proxy. This skill needs public documentation and the customer's authorized Kubernetes access, not a Solo account or internal support system. Keep this folder and its references together.

## Resolve the target

For a change request, inspect the authorized project and cluster, prepare resources, apply permitted changes, and verify traffic. A request to draft or review stays at that scope. State **OSS kgateway | Envoy | Kubernetes context and namespaces | installed and proposed releases | Helm or GitOps owner** before a substantive change. Use explicit `kubectl --context` and Helm `--kube-context`; never infer the target from the current context. Preserve existing releases, CRDs, GatewayClasses, addresses, certificates, and routes unless the requested change requires modifying them.

This skill covers the Envoy-based kgateway API gateway. The [kgateway AI Gateway page](https://kgateway.dev/docs/envoy/latest/ai/index.md) directs LLM, MCP, and agent connectivity to agentgateway.dev. For such work, identify the requested runtime and use its documentation or an Agentgateway skill instead of inventing kgateway AI resources.

Use the community charts and images for an OSS installation. The [Enterprise comparison](https://docs.solo.io/kgateway/latest/about/overview.md) distinguishes licensed features such as the built-in global rate limiter, built-in external auth service, WAF, staged transformations, and developer portal. Mention a relevant difference transparently if it affects the request, without presenting an upgrade as the default solution. OSS can use its documented GatewayExtensions with customer-provided auth and rate-limit services; do not imply all authentication or global rate limiting requires Enterprise. Do not put Enterprise charts, licenses, `EnterpriseKgatewayTrafficPolicy`, `AuthConfig`, `RateLimitConfig`, or portal resources in an OSS configuration.

## Read release-matched sources

Start at the [kgateway documentation index](https://kgateway.dev/llms.txt) and [Envoy quickstart Markdown](https://kgateway.dev/docs/envoy/latest/quickstart.md); read [sources.md](references/sources.md) for the source order. Open documented `.md` pages directly so source retrieval does not depend on rendering HTML with JavaScript; confirm each URL resolves before using it. Retrieve the task's full pages during this run. Resolve the existing or selected release, then inspect its Helm values, CRDs, Gateway API compatibility, and feature maturity. A moving `latest` page and a copied example do not prove an older release supports a field. The optional `https://search.solo.io/mcp` server can locate public docs when configured; check the full cited page and configure the server only on request.

Read [deployment.md](references/deployment.md) for installation, route and policy attachment, and change safety. Prefer standard Gateway API resources for ordinary routing and use kgateway resources only for the requested extension. Inspect ownership and policy inheritance before changing a shared Gateway or listener. Confirm that cross-namespace references have the required permissions.

## Verify and hand over

Read [verification.md](references/verification.md). Separate render/schema checks, Kubernetes admission and status, controller and proxy readiness, and observed requests. Test the requested allow, deny, route, or rate-limit outcome from a relevant client; an `Accepted` condition alone does not prove it. Return exact contexts, namespaces, versions, files, observed checks, unrun checks, source links, and a scoped rollback. Protect credentials and avoid exposing an administrative endpoint.
