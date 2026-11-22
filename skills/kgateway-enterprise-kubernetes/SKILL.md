---
name: kgateway-enterprise-kubernetes
description: Configure, deploy, troubleshoot, and verify Solo Enterprise for kgateway on Kubernetes with release-matched Gateway API and Enterprise resources. Covers licensed gateway services and developer portal; excludes OSS-only installations and Agentgateway AI routing.
---

# Solo Enterprise for kgateway on Kubernetes

Help the customer reach a working, verifiable API gateway outcome using their Solo Enterprise for kgateway installation and licensed capabilities. This public skill needs no internal support system or other installed skill. Keep this folder and its references together.

## Resolve the target

For a change request, inspect the authorized clusters and project, prepare artifacts, apply permitted changes, and verify behavior. A draft or review stays at its requested scope. State **Solo Enterprise for kgateway | Kubernetes contexts and namespaces | installed and proposed releases | license entitlement to confirm | Helm or GitOps owner**. Use explicit `kubectl --context` and Helm `--kube-context` for every cluster operation. Preserve existing release ownership, GatewayClasses, CRDs, routes, certificates, and traffic unless the task calls for changing them. A missing license blocks runtime verification of licensed behavior, not a reviewable plan.

The Envoy-based gateway handles API traffic. The [kgateway AI Gateway page](https://kgateway.dev/docs/envoy/latest/ai/) sends LLM, MCP, and agent connectivity work to agentgateway.dev. For such work, identify whether the customer wants Agentgateway as well; do not fabricate Enterprise kgateway AI resources.

## Research the selected release

Start at the [Solo Enterprise for kgateway documentation index](https://docs.solo.io/kgateway/llms.txt). Read [sources.md](references/sources.md), then retrieve the selected line's full task pages during this run. Check release-matched chart values, CRDs, Gateway API compatibility, and entitlement before writing executable fields. Existing deployments retain their release line unless an upgrade is requested or required by a documented dependency. Do not use a moving `latest` page as proof about an older installation.

For runnable patterns, consult the public [FE Enterprise kgateway workshop](https://github.com/solo-io/fe-enterprise-kgateway-workshop). Check its pinned versions, topology, charts, and fields against the chosen release. The optional `https://search.solo.io/mcp` server can find public docs when configured; check the full version-matched source page and configure the server only on request.

Read [deployment.md](references/deployment.md) for installation and policy decisions. Prefer standard Gateway API resources for ordinary routes. Use Enterprise kinds only when the requested behavior and selected release require them. Some OSS resources remain valid under the Enterprise controller; do not replace them solely because Enterprise is installed. The [Enterprise feature comparison](https://docs.solo.io/kgateway/latest/about/overview/) distinguishes built-in rate limiting and external auth, WAF, staged transformations, and developer portal from features also available in OSS. Check the requested feature's actual license and dependencies; do not equate a pullable image with entitlement.

When the developer portal or an administrative surface is requested, use the selected release's [portal identity guidance](https://docs.solo.io/kgateway/latest/portal/overview/). Prefer an external IdP and mapped roles for shared access. Do not expose a shared portal with every user as an administrator. Keep license keys, IdP secrets, and client credentials out of chat, source control, process arguments, and rendered examples; prefer documented Secret or mounted-file references.

## Verify and hand over

Read [verification.md](references/verification.md). Separate static validation, Kubernetes admission and status, controller/proxy/extension readiness, license state, observed traffic, and portal login or RBAC checks. Return exact contexts, namespaces, versions, changed files, observed outcomes, unrun checks, protected credential locations, source links, and scoped rollback. A ready Pod or accepted route alone does not establish that traffic or policy works.
