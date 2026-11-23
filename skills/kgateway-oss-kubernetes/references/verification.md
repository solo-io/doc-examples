# Verification

1. **Static:** render the selected chart and manifests; check API versions against the selected CRDs and Gateway API release. Inspect the diff for shared CRDs, RBAC, admission webhooks, and service exposure.
2. **Kubernetes:** use the explicit context to inspect controller and proxy readiness, GatewayClass ownership, Gateway listener conditions, HTTPRoute parent conditions, resolved references, and policy status. Investigate an accepted resource with no attached routes or a policy targeting the wrong parent.
3. **Traffic:** send bounded requests through the actual listener from a relevant client. Confirm the intended backend and response; for auth, rate limits, or rewrites, test both expected success and failure paths. Logs or metrics should identify the enforcing proxy or extension when the claim depends on it.
4. **Handover:** provide the working endpoint only after reachability is observed. Record tests not run, credentials or infrastructure still required, and a rollback limited to resources changed for the task.

Use [operations and troubleshooting](https://kgateway.dev/docs/envoy/latest/operations/index.md) to localize failures among DNS/load balancer, listener, route attachment, backend, policy, extension, or application.
