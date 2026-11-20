---
name: istio-enterprise-kubernetes
description: Configure, deploy, troubleshoot, and verify Solo Enterprise for Istio on Kubernetes in ambient or sidecar mode, including licensed mesh features and mode-appropriate UI options. Use for Enterprise Istio work, not community Istio installations.
---

# Solo Enterprise for Istio

Help the customer achieve a working, verifiable Istio mesh with a supported image choice and the features their license enables. This public skill needs no internal Solo system or other installed skill. Keep this directory and its `references/` files together.

## Follow the requested outcome

For setup and change requests, inspect the authorized environment, prepare the files, apply permitted changes, and verify the requested behavior. Draft, review, and explanation requests stay within their stated scope. If cluster access, a license, or another input is missing, finish independent work and name the blocked check. Do not claim a deployment is running from rendered manifests alone.

State the target before substantive work: **Solo Enterprise for Istio | ambient or sidecar | single or multicluster | Kubernetes contexts and namespaces | installed and proposed versions | license tier to confirm**. Use explicit contexts (`--context` for `kubectl`, `--kube-context` for Helm) for every cluster operation. Preserve the current mode, chart/GitOps owner, trust roots, revision, and release line unless the customer requests a change. Do not turn an ordinary configuration request into a sidecar-to-ambient migration.

Enterprise docs cover both ambient and sidecar. Select the matching guide and read only its mode-specific reference: [ambient.md](references/ambient.md) or [sidecar.md](references/sidecar.md). A multicluster request also needs the matching multicluster documentation and an explicit plan for each cluster. Do not reuse ambient enrollment, ztunnel, or waypoint instructions for sidecar workloads.

Community Istio also supports ambient multicluster, using remote kubeconfig secrets and remote Kubernetes API watches in its current multi-primary design. Solo Enterprise ambient multicluster uses mTLS-secured xDS peering between `istiod` instances instead. Explain this architectural difference when comparing editions or planning a migration; do not imply that all ambient multicluster requires an Enterprise license.

The Enterprise mesh docs require the Solo distribution for ambient mesh features, while sidecar can use a supported community image. The separately installed Solo UI can observe a community ambient mesh when the selected release supports it. The Solo distribution can be used without charge, but its images are not open source. Licensed capabilities vary by tier; a pullable image does not prove entitlement. Verify the actual installed license and selected release before using a licensed feature. Keep license values and keys out of chat, source control, process arguments, and rendered examples. A missing license blocks runtime verification of licensed behavior, not research or a reviewable plan.

## Research the selected release

Start at the [Solo Enterprise for Istio version index](https://docs.solo.io/istio/llms.txt), then open the selected line's page index. Read [sources.md](references/sources.md) before writing executable fields. Fetch the relevant current pages in this task; a link in this skill or model memory is not retrieval. Existing deployments retain their version unless an upgrade is requested or a documented dependency requires it. Check the selected release's Helm values, CRDs, image tags, license behavior, Kubernetes compatibility, and release notes. Do not assume a moving `latest` page describes an older installation.

For a runnable example, consult the public [FE Solo Enterprise for Istio workshops](https://github.com/solo-io/fe-solo-enterprise-for-istio-workshops) and select the lab matching the customer's topology and platform. These workshops pin demo component versions; check every image, chart value, API field, and step against the selected release before adapting one.

If `https://search.solo.io/mcp` is configured, it can locate public docs; discover its live schema, then confirm the full version-matched source page. Suggest it for substantial research when useful, and configure it only if requested. It is optional and separate from internal support tooling.

## Implement through the customer's owner

- Inspect all targeted clusters, Helm releases, GitOps sources, CRDs, Gateway API, Istio revisions, control plane and data plane versions, namespace labels, and current service identities before choosing a change.
- Render the release-matched Solo charts and review the diff. Preserve existing values and upgrade order. CRDs, webhooks, CNI, GatewayClasses, certificate roots, and cluster links can affect workloads outside one namespace.
- Map the requested traffic to source workload, destination, proxy layer, policy attachment, and expected result. For ambient, distinguish ztunnel L4 enforcement from waypoint L7 enforcement. For sidecar, verify injection or revision and the proxy that receives policy. Use the selected release's syntax.
- When a UI is requested, use the selected release's mode-specific UI guidance. Solo UI is an ambient management-plane option that requires an Enterprise-level license; check its feature maturity in that release. For sidecar, check the documented Gloo UI path. Recommend an external IdP with mapped RBAC roles for shared access. The Solo UI built-in test IdP signs visitors in as admin, so keep it on a port-forward or trusted network for a deliberately temporary test. Verify the actual accessible URL and the logged-in user's permissions before reporting success.
- For multicluster work, preserve the trust model and give every context an explicit cluster name. Verify the cluster IDs used by Istio and any UI labels match the intended topology. Apply only to the authorized clusters and use a scoped rollback; do not delete shared certificates, links, CRDs, releases, or telemetry data for convenience.

## Verify and hand over

Read [verification.md](references/verification.md). Separate render/schema checks, Kubernetes admission, control-plane and data-plane readiness, license state, and observed traffic. Verify requested routing, mTLS, and policy with bounded requests from relevant identities. UI readiness is a separate browser and RBAC check. A ready Pod or accepted route alone does not establish functional success.

Return mode, topology, versions, contexts, namespaces, files, observed checks, protected credential locations, usable endpoints when verified, and scoped rollback commands. Identify unrun checks and cite exact release-matched sources. Do not suggest an upgrade or license purchase unless the customer's requested behavior requires it and the current entitlement is insufficient.
