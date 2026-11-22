# Verify the requested mesh behavior

Use explicit contexts and release-matched `istioctl` for every cluster. Keep this sequence proportional to the request; report a stage as unrun when the required access is absent.

1. **Artifact checks:** render the matching chart and validate values and resource kinds against its CRDs. Review a diff with the current Helm/GitOps owner and identify cluster-scoped changes.
2. **Admission and distribution:** inspect resource status, events, Istio analysis, and the control plane's delivered configuration. A valid manifest or `Accepted` condition is not proof that the intended proxy enforces it.
3. **Runtime:** check istiod and relevant ztunnel/CNI/waypoint or sidecar health, version skew, and the installed license state. The [licensing guide](https://docs.solo.io/istio/latest/about/images/licensing/) documents `istioctl license` and its meaning; confirm it on the selected release. Do not print the key.
4. **Traffic:** send a bounded request from the relevant source identity to the destination. Verify the expected route, service identity, and [mTLS](https://docs.solo.io/istio/latest/security/verify-mtls/) or mode-specific equivalent. Check the enforcing proxy's metrics or logs when claiming policy, waypoint, or sidecar behavior. For authorization, test intended allow and deny requests.
5. **Multicluster and UI, when requested:** test discovery and traffic from each cluster, including intended failover behavior where safe. For the UI, check the real address, TLS, login, cluster views, and permissions of mapped RBAC roles. A reachable login page is not proof that telemetry or RBAC works.

On failure, localize the layer before editing: Helm/CRD, CNI or injection, identity and trust, control-plane distribution, ztunnel or sidecar, waypoint/Gateway routing, policy attachment, or UI. Change one evidenced factor and repeat the bounded check. Preserve the customer's current certificates, license and UI data, and mesh ownership.
