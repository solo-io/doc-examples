# Ambient deployment decisions

## Install or preserve

Inspect `helm list`, current Istio CRDs, namespaces, revisions, workloads, and Gateway API before choosing commands. The [ambientmesh.io Helm guide](https://ambientmesh.io/docs/setup/install/) installs Gateway API CRDs where needed, then the community `base`, `istiod` with the ambient profile, `cni` with the ambient profile, and `ztunnel` charts. Pin all charts and images to a compatible published release for a new deployment. Preserve existing Helm/GitOps release names and values on an update; review rendered differences, especially cluster-scoped CRDs, webhook selectors, revisions, CNI, and trust configuration.

Read the [requirements](https://ambientmesh.io/docs/setup/requirements/) and [production readiness](https://ambientmesh.io/docs/setup/production-readiness/) pages for the customer's Kubernetes platform. Do not infer that a working kind example is production-ready on every CNI or cloud.

## Enroll and route

Use [workload enrollment](https://ambientmesh.io/docs/setup/add-workloads/) to select namespaces or pods deliberately. Record existing `istio-injection`, `istio.io/rev`, and `istio.io/dataplane-mode` labels and injected sidecars before changing them. Check whether a restart is needed for the selected change and release. Verify the workloads that ztunnel actually captures.

Ztunnel supplies the ambient L4 path and secure overlay. Add a [waypoint](https://ambientmesh.io/docs/waypoints/configuration/) for L7 behavior, and verify which service or namespace uses it. Check the chosen release's route attachment and policy `targetRefs` behavior. A policy intended for a waypoint must not be assumed to run in ztunnel. For external entry, read [ingress options](https://ambientmesh.io/docs/traffic-management/ingress/overview/) and preserve the customer's chosen Gateway controller.

Read the corresponding [L4 authorization](https://ambientmesh.io/docs/security/ztunnel-authz/) or [L7 authorization](https://ambientmesh.io/docs/security/waypoint-authz/) guide before writing a policy. Map source identities, destinations, paths, ports, and expected allow/deny behavior; account for NetworkPolicy and health probes. Stage restrictive policies with a rollback plan so a bad selector does not interrupt unrelated workloads.

## Multicluster ambient

For community ambient multicluster, follow the selected release's [upstream multicluster index](https://istio.io/latest/docs/ambient/install/multicluster/), [prerequisites](https://istio.io/latest/docs/ambient/install/multicluster/before-you-begin/), and supported topology guide. The current [multi-primary, different-network guide](https://istio.io/latest/docs/ambient/install/multicluster/multi-primary_multi-network/) gives each cluster its own `istiod`, uses a shared root of trust and remote secrets so each control plane can watch the other cluster's Kubernetes API, and routes cross-network workload traffic through ambient east-west gateways. Confirm cluster and network IDs, remote API reachability, certificate roots, gateway reachability, and ownership in every context before changing them. Protect remote kubeconfig secrets as credentials.

The [ambientmesh.io multicluster overview](https://ambientmesh.io/docs/setup/multicluster/) is explicitly about Solo Enterprise for Istio: its xDS control-plane peering and global-service resources are a different architecture. Do not copy those Enterprise steps or describe multicluster itself as unavailable in community Istio.

## Upgrade or migrate

Use the [ambient upgrade guide](https://ambientmesh.io/docs/operations/upgrade/) and the selected release notes. Upgrade the control plane and data plane in their documented order; confirm skew support before starting. For a sidecar mesh, use the [migration guide](https://ambientmesh.io/docs/setup/sidecar-migration/) and protect traffic continuity. Existing certificates, roots of trust, revisions, and GitOps owners are customer state, not disposable test data.
