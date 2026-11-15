# Verification — Solo Enterprise for Agentgateway Kubernetes controller

Start with the package/runtime version check in [verification helpers](verification-helpers.md). The same reference provides tested MCP-response and controlled-masking checks; use them only for the relevant evidence.

Select checks for the actual task; do not require a separate test cluster or full POC for a small edit. Preserve the distinction between prepared artifacts and executed work.

| Evidence | Check | Does not prove |
| --- | --- | --- |
| Source/static | Release/mode, Helm render, YAML, CRD schema and reference consistency. | Kubernetes acceptance or runtime support. |
| Admission | Server-side dry-run where authorized and schemas/admission exist; namespace/RBAC and object acceptance. | Controller attachment, config delivery, or enforcement. |
| Reconciliation | Current observed generations; relevant GatewayClass/Gateway/listener/route/model/policy conditions; proxy config and rejection logs. | A successful end-to-end transaction. |
| Functional | Real client requests through the gateway and negative cases for requested controls. | Real cloud integration from a mock, or production capacity from a smoke test. |

For each success criterion record the command/client action, expected outcome, observed outcome, and pass/fail/not-run status. Never use example output as captured evidence. Do not dump Secrets, licenses, raw bearer tokens, or customer prompt data.

## Behavior checks

- Routing: use the actual host/path/protocol/model, verify the intended upstream and transformations, and test streaming if promised. Missing model prefixes and HTTPRoute/model-listener conflicts are routing failures, not provider credential failures.
- MCP: initialize, discover, and invoke a representative tool with the documented transport/session headers. Distinguish HTTP success from JSON-RPC errors or a tool result with `isError`. For authorization, also invoke a forbidden tool directly and prove it did not execute upstream.
- Authentication: test a valid identity and relevant missing/invalid/expired/wrong-issuer/wrong-audience cases. Strict auth must cover every exposed route that needs it. Passing a JWT as an SDK API key only supplies the Bearer header; it does not obtain/refresh the token or configure gateway verification. Use a token issued for the gateway's configured trust requirements, and keep upstream provider auth separate.
- Keys and budgets: follow [llm-setup.md](llm-setup.md). Check independent authenticated identities, routing/pricing coverage, enforcement scope, reset semantics, and shared/persistent counters where promised. Verify that exhausting one test key does not consume another's allowance. Token estimates and Audit mode are not USD blocking.
- Telemetry/PII: generate a known request and inspect its actual destination. For redaction use synthetic data, check the relevant request/response and streaming path, and ensure the sensitive value did not leak through a different configured signal. Do not claim comprehensive detection from a few samples.

Match a masking check to the configured detector. Built-in PII detectors can return entity tokens such as `<EMAIL_ADDRESS>`; custom regex replacements use `<masked>`. Verify the selected Enterprise release's actual token instead of requiring the custom-regex marker for every detector. Pair a known-sensitive upstream response with a benign control: a model omitting an email is not proof that the gateway masked it.

- UI: verify the correct proxy or management UI from the user's host while the documented port-forward is running. Report HTTP reachability separately from interactive functionality and telemetry views.
- Enterprise-specific MCP, when in scope: test a new session for tool mode changes, allowed/denied identities through meta-tools or code execution, pipeline inputs/step failures, and the output actually produced. A declared mode or accepted backend is not proof of behavior.
- Lifecycle: verify delivery of a changed resource and preserve previous configuration and state for rollback. Restart/persistence tests must be within the authorized test scope; do not restart a shared production service just to complete a checklist.

## Diagnose by layer

For a shared-budget claim across replicas, use distinct Pod endpoints and a fresh isolated test identity. Debit that identity through Pod A only, wait for accounting to settle, then inspect its counter or test rejection through Pod B before spending that identity's allowance there. Verify a second identity remains permitted. Alternating requests until both Pods reject can exhaust two independent counters and falsely appear to prove sharing. Keep the test within one budget window and distinguish shared counters from restart durability; neither follows from two Ready replicas.

Start at cluster access/version/CRD/admission, then controller ownership/reconciliation, listener/network/TLS, route/model matching, identity/policy, dependency services/storage, and upstream protocol/IAM. Collect the precise version and minimal sanitized failure, form a specific hypothesis, and rerun only the relevant check after a change. A policy's positive status can coexist with a different policy winning or with config delivery failing; inspect effective behavior.

If a needed test requires an unavailable license, credential, cluster, or out-of-scope change, finish the independent work and name the unmet requirement. Do not turn a limited mock/static check into a claim of a complete deployment.
