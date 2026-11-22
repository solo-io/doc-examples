# Verification

1. **Static:** render selected charts and resources; validate API versions and fields against release-matched CRDs. Review shared CRDs, admission webhooks, RBAC, GatewayClasses, and license handling.
2. **Kubernetes:** inspect explicit-context controller, proxy, auth/rate-limit service, Gateway listener, route parent, policy, and backend status. Verify the installed license state through the selected release's documented method without printing its value.
3. **Traffic:** send bounded requests through the actual listener from the expected client identity. Verify routing and, when requested, successful and denied authentication, policy, or rate-limit behavior. Use logs or metrics to identify the enforcing component when needed.
4. **Portal, if requested:** test the reachable URL, IdP login, and separate reader/admin permissions. Test an API subscription or generated credential only when requested and safe to create.
5. **Handover:** distinguish completed checks from unrun checks, identify required secrets and infrastructure without exposing values, and give rollback commands limited to the task's resources.

Use the selected line's [operations guidance](https://docs.solo.io/kgateway/latest/operations/) to isolate failures among exposure, listener, route, policy, extension, license, portal identity, or application.
