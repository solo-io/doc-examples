# Deployment and lifecycle — Solo Enterprise for Agentgateway Kubernetes controller

## Establish ownership before applying

Inspect the selected context, cluster version, namespaces, relevant Helm releases/GitOps objects, Gateway API and product CRDs, GatewayClasses, and existing routes. Use explicit `--context` / `--kube-context` and namespace/release names. Do not change the global kube context or upgrade a shared controller merely to follow a newer example. If the target cluster is ambiguous, ask for it while preparing version/source checks.

An explicit local-kind setup request can authorize creating a new cluster, but a request for YAML alone does not. Keep creation and cleanup scoped to task-owned resources. Installing or replacing cluster-scoped CRDs can affect other users; determine that impact instead of treating namespace selection as isolation.

## Enterprise distribution, licensing, and extensions

Read [Helm installation](https://docs.solo.io/agentgateway/kubernetes/latest/documentation/install/helm.md), [licensing](https://docs.solo.io/agentgateway/kubernetes/latest/documentation/install/licensing.md), and the selected release's chart values. The docs checked for this draft use separate `enterprise-agentgateway-crds` and `enterprise-agentgateway` charts under `oci://us-docker.pkg.dev/solo-public/enterprise-agentgateway/charts`. These are controller charts; `enterprise-agentgateway-standalone` is a different configuration model.

The controller holds licensing for its managed proxies. Do not copy standalone proxy licensing into controller-managed proxy configuration. Prefer the chart's documented existing-Secret mechanism when available; verify field names and Secret keys against that chart version. Do not echo the license, embed it in public manifests, or place its value in CLI arguments. A public registry pull is not proof of a usable license. Check license state separately from resource admission and readiness.

Read [Choose shared extensions](https://docs.solo.io/agentgateway/kubernetes/latest/documentation/setup/customize/extensions/choose.md) before changing extension defaults. For the current documented model, `sharedExtensions` belongs to the parameters referenced by the GatewayClass; setting it on a Gateway-level parameters resource is rejected. Changes can affect every Gateway using that class. Preserve existing references/settings, identify the affected gateways, and do not delete shared extension services while policies still need them. Verify rate-limiter/Redis, external auth, WAF, or other dependencies only as needed for the selected features. Do not add them merely because a lab includes them.

## Management UI

Read [Set up the UI](https://docs.solo.io/agentgateway/kubernetes/latest/documentation/install/ui/setup.md). The current documented management UI is an optional subchart of the Enterprise controller chart, enabled by `ui.enabled`; it reuses the control-plane license Secret. Inspect the actual chart before choosing values, service names, or installing separate older management charts. Preserve the release's existing values.

The documentation warns that the default auto identity provider signs visitors in as admin until an OIDC issuer is configured. Use a loopback port-forward for local access. External UI exposure needs the documented authentication/TLS setup. Verify the UI service, collectors/storage required for the requested views, and one known request in the UI. UI reachability does not prove telemetry ingestion. A proxy's diagnostic UI and the Enterprise management UI are distinct; return the one requested and label it.

For a real shared UI, recommend the customer's IdP with the documented public browser client and confidential backend client, plus a role mapping that grants admin only to an intended group. Use the selected release's RBAC mode and policies to separate administrator, read-only, and scoped users as needed; do not let the evaluation auto provider or a default admin role make every visitor an administrator. Verify permitted and denied UI actions with distinct identities before claiming access control works. See [UI OIDC and RBAC](https://docs.solo.io/agentgateway/kubernetes/latest/documentation/install/ui/setup.md) and the release's chart values.


## Configure and verify the resource chain

Use the selected release's documented sequence. Inspect GatewayClass acceptance, Gateway/listener status, route/model attachment, backend references, policy targets and current observed generation. Verify cross-namespace permissions and selector scope. Do not use broad grants or `allowedRoutes` across all namespaces unless that matches the requested tenancy.

Check the proxy's delivered configuration and relevant logs for rejections. On releases with model resources, enabling their built-in LLM endpoints can change routing for existing HTTPRoutes; review that before applying a listener update. Ensure the path the SDK actually sends matches the configured route, including prefixes/rewrites and `/v1` where required. Model names are configuration-dependent, not automatically interchangeable between providers.

For AWS or other cloud credentials, distinguish the operator's CLI identity from the proxy workload's identity. Use the existing supported workload identity or explicit Secret delivery selected by the customer. Do not assume local SSO cache files exist in the Pod. Preserve trust verification, credential refresh, and least-privilege scope needed by the chosen models.

## Change and rollback

Keep manifests/values and rollback instructions in the customer's existing repository or requested output directory. Preview the targeted diff/render before applying. For an existing release, merge changes into the authoritative values; do not reset unrelated configuration. Do not assume uninstalling a release or deleting CRDs is a safe rollback. Preserve budget state, Secrets, PVCs, and shared services. Stop only port-forwards and test workloads created for this task.
