# Verification and diagnosis

Use the selected release's `istioctl` and explicit kube context. Record what each check proves.

1. **Static and ownership:** lint Helm values, render the selected charts, validate manifests against matching CRDs, and review changes to cluster-scoped resources. For existing installations, compare `helm get values` and the rendered diff with the current owner.
2. **Control plane and data plane:** inspect Helm status, `istiod`, CNI, ztunnel, revision tags, and relevant Gateway/waypoint readiness. `istioctl analyze` can reveal configuration problems, but a clean result is not an end-to-end proof.
3. **Enrollment:** inspect namespace/pod labels and sidecar state. Use release-matched `istioctl ztunnel-config` or equivalent status and sanitized logs to show that the intended workload is captured.
4. **Traffic:** send a bounded request from an enrolled source to the intended destination. Verify service identity and [mTLS](https://ambientmesh.io/docs/security/verify-mtls/) with a supported method; a successful plaintext-looking application response alone does not prove encryption on the wire. For a waypoint, confirm the request traverses it before claiming L7 enforcement or telemetry.
5. **Policy:** test one intended allowed request and one intended denied request from representative identities. Check the result and the enforcing proxy's evidence. Do not remove auth or broaden selectors merely to make a test green.

For failures, localize the layer: enrollment and CNI, ztunnel and HBONE, waypoint and route attachment, policy target, Gateway entry, or application. The [troubleshooting guide](https://ambientmesh.io/docs/operations/troubleshooting/) is the first diagnostic source. Report unrun checks and why they remain unrun.
