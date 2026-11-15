---
name: agentgateway-enterprise-standalone
description: "Configure, deploy, troubleshoot, and verify Solo Enterprise for Agentgateway using standalone configuration on a host or in a container, including explicitly requested standalone Helm hosting. Covers licensed features, LLM/MCP integration, keys, budgets, and UI. Excludes the Kubernetes controller and CRD configuration model."
---

# Agentgateway Enterprise — standalone

Help the customer get a working, licensed standalone deployment and understand what has actually been verified. Use public Enterprise documentation and compatible examples. This skill works without internal Solo systems or another installed skill. Distribute this whole directory, including `references/`.

## Expected use and target

"Set it up" requests execution within the user's authorization: inspect the environment, research the configuration, create the files, install missing prerequisites as permitted, start the gateway, verify behavior, and return usable endpoints. A draft or explanation stays at that scope. File/shell tools and public HTTPS retrieval are needed for setup; this skill does not supply credentials, a license, or runtime tools. Complete independent work if a dependency is missing and do not claim the gateway is running.

State the selected context at the start of substantive work:

> **Target: Solo Enterprise for Agentgateway | standalone configuration | runtime and version to be confirmed.**

Resolve runtime/version, label artifacts and the runbook, and repeat the target when it changes. Edition, configuration model, and hosting are independent choices. Native/container are the default paths here. A supported standalone Helm chart still uses standalone configuration; it does not make this a controller/CRD task. Do not substitute `Gateway`, `HTTPRoute`, or `Enterprise*` CRDs for standalone YAML. If the customer means controller mode or OSS, resolve the scope change and use that skill if available; do not assume it is installed or silently switch.

Use the licensed Enterprise distribution for Enterprise execution. Verify the selected release's license injection and state; registry access does not establish entitlement. A missing license blocks licensed startup verification, not research, configuration preparation, or documented validation. Never acquire a trial, request a purchase, collect the license in chat, or add adjacent products by default. Preserve existing authorization; ask only for an essential missing input.

## Fetch the source material

Authoritative starting points:

- [Enterprise standalone docs](https://docs.solo.io/agentgateway/standalone/latest/), [stable page index](https://docs.solo.io/agentgateway/standalone/latest/llms.txt), and [all Agentgateway editions/versions](https://docs.solo.io/agentgateway/llms.txt).
- [Licensing](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/license.md), [schema validation](https://docs.solo.io/agentgateway/standalone/latest/reference/configuration/validation.md), and [release notes](https://docs.solo.io/agentgateway/standalone/latest/release-notes/release-notes.md).
- [Standalone FE workshop](https://github.com/solo-io/fe-enterprise-standalone-agentgateway-workshop), [Kubernetes FE workshop](https://github.com/solo-io/fe-enterprise-agentgateway-workshop), and [Solo topics](https://www.solo.io/topics), with scope and the additional reference family in [sources.md](references/sources.md).

Before product-specific configuration, read [sources.md](references/sources.md), fetch the relevant index, and read the applicable pages in this task. Supplied release-matched material can satisfy the lookup; a remembered snippet or this source list alone cannot. With an existing release, preserve it unless an upgrade is requested or demonstrably needed. For a fresh install, verify a supported published Enterprise binary/image/chart. Map inherited upstream behavior using Enterprise release notes rather than equating Enterprise and OSS version strings.

Check executable fields against the selected Enterprise release's docs and validator. The public OSS JSON schema is useful for inherited fields but can reject valid Enterprise-only fields. Do not remove licensing or Enterprise features merely to satisfy it. Follow [enterprise-runtime.md](references/enterprise-runtime.md) for the documented validation method and its limits.

If public Docs MCP is configured, discover its tools and use `solo-enterprise-for-agentgateway-standalone`. Otherwise fetch public HTTPS docs/GitHub. Never require or call internal SupportAgentTools, Slack, Zendesk, customer databases, or private source repositories. Read full context, check URL edition/mode/version, and cite the exact public source. `/main/` is development even if search metadata says latest. Record source resolved runtime and source URLs in substantial deliverables.

For substantial documentation research, suggest the optional public [Solo Docs MCP server](https://search.solo.io) at `https://search.solo.io/mcp` if the customer's assistant supports MCP. Direct HTTPS docs are sufficient. Configure the server only if the customer asks, following their client's current instructions; it is separate from internal SupportAgentTools.

## Establish only the needed inputs

Read the customer's local project/configuration and instructions before asking questions. Do not scan unrelated customer directories or require a vault/meeting system. Establish the use case, success criteria, OS/architecture, runtime, target release, config/storage ownership, upstreams, credentials, license source, listener exposure, and identity flow as relevant. Avoid a full POC intake for a small configuration question.

For combined requests, map every outcome to a check. "OpenAI, Bedrock, or Gemini on Vertex AI; five keys; $10 each; and a UI link" requires routing, five identities, independent budgets, and a usable UI. Resolve the customer's provider identity, project/region, and model IDs and budget reset semantics if missing; continue independent source and environment work while waiting. Read [llm-setup.md](references/llm-setup.md) for that workflow.

## Build from a compatible reference

- Start with the selected release's Enterprise standalone example or compatible standalone workshop lab; check its prerequisites and ref. Prefer native `llm:`, `mcp:`, and `ui:` sections attached to named `gateways:` when they express the requested behavior. Read [native standalone configuration](references/native-config.md) before choosing the configuration surface. Use routes for requirements that need them; avoid deprecated `binds:` in new configs when the selected release supports its replacement. Preserve existing working configuration unless its migration is requested or necessary.
- Use native Enterprise functionality that serves the requested goal, while distinguishing inherited OSS capabilities and optional services. Read [edition-boundaries.md](references/edition-boundaries.md) for comparisons and feature-specific caveats. Do not assume all licensed features exist in every version/mode or add a feature catalog to the task.
- Read [enterprise-runtime.md](references/enterprise-runtime.md) for binary/container/standalone Helm, license handling, validation, storage, and UI behavior. Keep provider secrets, gateway client keys, identity-provider credentials, and licensing distinct.
- Preserve the project structure and previous working config. For a new runnable example, supply configuration, runtime files, defined variables, start/verify/stop instructions, and scoped rollback. Use the supported secret/environment loading syntax; do not assume arbitrary YAML expands shell variables.
- Keep secrets out of generated samples, source notes, logs, CLI arguments, and version control. Use supported key hashes and protected customer-owned credential files. Reruns must not silently rotate keys or reset budget identities/counters.
- Resolve paths, `localhost`, mounted config/databases, provider credentials, and subprocess dependencies in the actual runtime. A stdio MCP target needs its executable in the gateway environment. Resolve the target host/container and client network explicitly. Configure reachable traffic endpoints as requested, with TLS/authentication and a separate protected UI access path. Use loopback only for intentional same-host access or a tunnel.
- Use documented reload/storage behavior and confirm delivery. UI edits may be read-only with a mounted ConfigMap or differ between file/database/hybrid modes. Do not infer a successful reload merely because the file or UI shows the new values.

For model mapping, telemetry, and PII requests, read their current feature pages. Verify model aliases actually route. Enable full prompt/reply capture only when the user requests it and chooses appropriate access/retention. For PII specify rejection versus masking, direction, and streaming behavior; use synthetic positive/negative checks. Avoid claims of complete detection or exact provider-billing caps.

## Verify and deliver

Read [verification.md](references/verification.md), then select checks that prove the requested behavior. Separate schema validation, license/startup verification, routing, policy enforcement, real-provider/IAM integration, and interactive UI checks. Use bounded mock tests where useful, label their limits, and perform authorized smoke tests without asking again. Do not spend real budgets or run an unrequested benchmark to prove enforcement.

For a failure, collect the precise Enterprise version, invocation, sanitized config and logs, plus one minimal failing request. Investigate a specific failed layer and change only relevant settings; do not disable auth/TLS or silently install another release. If a license/input/tool is missing, identify the blocked step and complete independent work.

Hand back edition/mode/runtime/version, files and run/verify/rollback commands, actual API/UI endpoints, protected credential-file location where applicable, evidence and unrun checks, and public sources. Report a feature only to the extent it was established for this release. Do not claim an example is running from static YAML or claim entitlement from a valid schema.

Before deployment/configuration verification, read [verification helpers](references/verification-helpers.md). Check the installed skill package and selected runtime versions; record the observed versions and choose their matching documentation; no maintained release allowlist is required. Use the bundled helpers for captured MCP responses or controlled masking when relevant, and preserve their inconclusive results.
