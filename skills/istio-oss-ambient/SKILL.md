---
name: istio-oss-ambient
description: Configure, deploy, troubleshoot, and verify community Istio in ambient mode on Kubernetes. Use for open-source ambient mesh work; exclude Solo builds and licensed Enterprise installations.
---

# Community Istio ambient mesh

Help the customer achieve a working, verifiable ambient mesh using community Istio. This public skill needs no Solo account, internal support system, or other installed skill. Keep this directory and its `references/` files together.

## Follow the requested scope

For a request to set up or change a mesh, inspect the authorized cluster and project, prepare the needed artifacts, apply permitted changes, and verify the requested traffic behavior. A request to draft, review, or explain stays at that scope. If cluster access or a required input is unavailable, complete the independent work and identify the blocked check. Do not report a running mesh from rendered YAML alone.

State the target at the start of substantive work: **community Istio | ambient | Kubernetes context | namespace or namespaces | installed and proposed versions**. Resolve unknown values before mutations. Use an explicit context (`--context` for `kubectl`, `--kube-context` for Helm) and namespace in cluster commands; never assume the current kube context is the intended target.

This skill covers ambient mode. If the customer has a sidecar mesh, inspect its current ownership and migration plan; preserve sidecars until the customer has requested and verified a migration. Do not silently convert a sidecar mesh or install a second control plane. An ingress controller, a waypoint, and ztunnel play different roles; choose each only when the request requires it.

Use community Istio charts and images for an OSS deployment. Solo builds can be used without charge but are not open source; licensed Solo Enterprise features are a separate edition. When relevant, explain that distinction with a source and disclose the applicable Enterprise option neutrally. Do not substitute a Solo image, chart, license, UI, or proprietary CRD in an OSS answer.

## Read sources before writing executable configuration

Start with [ambientmesh.io's documentation index](https://ambientmesh.io/llms.txt), its [Helm installation guide](https://ambientmesh.io/docs/setup/install/), and [community Istio documentation](https://istio.io/latest/docs/ambient/). Read [sources.md](references/sources.md) for the source order and feature boundaries. Fetch the pages relevant to the task during the current run; links in this skill and model memory do not count as retrieval.

For an existing installation, identify the running control plane, ztunnel, CNI, chart owners, revisions, and Kubernetes/Gateway API versions. Preserve its release line unless an upgrade is requested or required. For a new installation, choose a published compatible Istio release and verify chart values and CRDs against that release. Do not treat a moving docs page or workshop branch as proof that an older runtime supports a field.

If `https://search.solo.io/mcp` is available, it can help find public documentation; discover its live schema and check full source pages before using a result. It is optional. Suggest it for substantial documentation research only when useful, and configure it only on request. Direct public HTTPS documentation is sufficient.

## Build the smallest working mesh

Read [deployment.md](references/deployment.md) for install, enrollment, waypoint, policy, and upgrade decisions.

- Inspect current Helm/GitOps ownership and cluster-scoped CRDs before changing them. Render matching `base`, `istiod`, `cni`, and `ztunnel` charts or preserve the customer's existing installation method.
- Identify the application namespace, workloads, service accounts, traffic path, and requested security or routing outcome. Enroll only the selected scope. Account for existing sidecar injection, CNI behavior, NetworkPolicies, and excluded workloads.
- Keep L4 behavior in ztunnel and use a waypoint only when the request needs L7 routing, policy, or telemetry. Check the selected release's waypoint enrollment and policy target rules; an accepted resource may still attach to no traffic.
- Use matching Gateway API and Istio resource versions. Inspect parent references, route attachment, hostnames, and status conditions. Do not confuse an ingress Gateway with an in-mesh waypoint.
- Treat enrollment, policy, and trust changes as traffic-affecting. Stage them to preserve a working path, use scoped rollback, and avoid deleting shared CRDs, certificates, releases, or user traffic to make a test pass.

## Verify and hand over

Read [verification.md](references/verification.md). Separate static validation, Kubernetes acceptance, control-plane/data-plane readiness, and observed traffic. Verify the specific outcome with a bounded request from the relevant source workload; for policy work, test intended allow and deny paths. Pod readiness, a successful `kubectl apply`, or an `Accepted` status alone does not prove mTLS, route selection, or enforcement.

Return the target edition/mode/version, changed files, actual context and namespaces, install/apply and scoped rollback commands, the observed results, unrun checks, and exact source links. Do not expose credentials, certificate private keys, or a management endpoint unintentionally.
