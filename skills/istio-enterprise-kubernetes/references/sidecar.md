# Enterprise sidecar mode

Use the selected release's [sidecar installation guide](https://docs.solo.io/istio/latest/sidecar/setup/install/manual/) and [service mesh options](https://docs.solo.io/istio/latest/sidecar/about/overview/). Establish existing chart or operator ownership, Istio revision, injection labels, proxy and control-plane versions, certificate roots, Gateway installation, and application rollout constraints. Preserve the current sidecar mode unless a migration is explicitly requested. Do not install ztunnel or apply ambient enrollment labels as a sidecar setup step.

For routing or policy, trace source sidecar → destination sidecar or gateway and verify which proxy receives the configuration. Use the selected release's sidecar traffic-management and security pages for `VirtualService`, `DestinationRule`, `AuthorizationPolicy`, `PeerAuthentication`, and `RequestAuthentication` behavior; do not transplant ambient waypoint `targetRefs` or L4 ztunnel assumptions. Check namespace/revision selectors before a rollout, and validate that newly created Pods receive the intended proxy.

For multicluster, use the selected release's [sidecar multicluster guide](https://docs.solo.io/istio/latest/sidecar/setup/multicluster/default/manual/). Record each context, cluster identity, network, certificates, remote secrets, gateways, and routing scope. Verify the license tier and cross-cluster trust before modifying links. Avoid treating a healthy single-cluster sidecar as proof of a working multicluster mesh.

If the customer requests a UI, consult the selected release's [Gloo UI guidance](https://docs.solo.io/istio/latest/ui/gloo-ui/) for sidecar meshes. Do not apply the ambient Solo UI installation guide to a sidecar setup.

For an explicitly requested migration to ambient, read the release-matched [migration guide](https://docs.solo.io/istio/latest/setup/install/migrate/) and plan coexistence and rollback. Test representative traffic through every phase before removing sidecars or legacy policy.
