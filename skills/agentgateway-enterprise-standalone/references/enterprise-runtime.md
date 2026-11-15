# Enterprise standalone runtime, license, and validation

Read the selected release's installation, license, schema-validation, and storage pages linked below. Resolve the actual runtime and retrieve its applicable documentation during the task.

## Runtime selection

On the selected host or container environment, inspect OS/architecture, existing processes/ports, and available release assets. Prefer a native binary when supported and suitable; use Docker if requested or appropriate. Do not introduce Kubernetes. [Docker installation](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/install/docker.md) documents the public Enterprise image registry and supported architectures. Pulling it requires no registry credentials as described in the current installation documentation; startup licensing is a separate requirement. Verify the actual tag/platform before using it and preserve existing runtimes.

For explicitly requested [standalone Helm](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/install/helm.md), inspect that chart's values and image. Keep standalone configuration; do not install the controller or CRDs. Use an explicit context/namespace/release and persistent storage as required. A mounted ConfigMap is normally not writable by UI edits; use the documented storage mechanism rather than promising file edits survive rollout.

## License handling

[Licensing](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/license.md) states that standalone proxies read `ENTERPRISE_AGENTGATEWAY_LICENSE_KEY` or `config.license.key`, including a documented file-reference form; the environment source wins when both are set. These are standalone settings. A controller-managed proxy takes its license from the controller and follows the Kubernetes installation workflow instead.

Use the customer's existing approved license source. Prefer a supported mounted secret file or secret-store/environment delivery and restrictive local permissions. Never bake a key into an image, a shared ConfigMap, a committed config, a shell command argument, or a report. Do not print full process environments or runtime responses that might include secrets.

Verify license state through the documented sanitized runtime fields rather than merely finding a configured variable. The checked docs describe startup checks and restart implications on expiry. A running process is not proof that a future restart will succeed. Do not encode grace dates/entitlements as permanent defaults or attempt to bypass licensing. If a key is absent, prepare everything that can be prepared and state that licensed startup is not verified.

## Enterprise validation

[Schema validation](https://docs.solo.io/agentgateway/standalone/latest/reference/configuration/validation.md) says the upstream OSS schema omits Enterprise-only fields and can reject valid `config.license` settings. Discover whether a complete public Enterprise schema is available for the selected runtime. Do not invent one or remove supported fields to satisfy the OSS schema.

The current docs provide `agentgateway --validate-only -f config.yaml` using the Enterprise binary. Confirm that option on the selected binary/release before using it. This checks configuration shape; it does not prove entitlement, successful startup, policy enforcement, or upstream connectivity. A configuration can validate without a usable license. Then verify startup/license separately, followed by functional tests. If the validator cannot be run, state the narrower evidence actually gathered.

Map any upstream editor schema to the OSS base version named in the Enterprise [release notes](https://docs.solo.io/agentgateway/standalone/latest/release-notes/release-notes.md). Do not equate an Enterprise calendar version with an upstream semantic version.

## Persistence, networking, and UI

Read [database](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/database.md), [storage](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/storage.md), [update](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/update.md), and [UI](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/ui/launch-ui.md). Keep key identities and counters durable, mount the required writable paths, and distinguish budget accounting from telemetry retention. Verify multi-process accounting before scaling; a local SQLite file is not automatically a shared budget store.

Discover the actual traffic/admin/UI listeners and verify reachability from the host. A loopback listener inside a container is not exposed merely by publishing a port. Expose only the requested interfaces; use loopback for same-host access or a tunnel, and verify reachable hostnames from the intended client network. UI authentication on a gateway listener does not protect the separate raw admin API; keep that admin interface isolated, as described in the [config-resource API guide](https://docs.solo.io/agentgateway/standalone/latest/documentation/operations/config-resources.md). Check the selected storage mode supports the required edits and survives a restart.

The UI can show file contents even when a reload was rejected and the proxy is serving the previous valid configuration. Inspect reload errors/effective behavior rather than using the editor display as delivery proof. When changing MCP tool modes, establish a new client session if required by the selected release. Stop only task-owned processes and restore through the same configuration mechanism.

For editable Helm deployments, inspect the chart's `mode`, `database.postgres.url`, and `replicaCount`. The chart manages nested `config.storage` and `config.database`; do not supply conflicting values inside its standalone config. In hybrid mode, file-owned resources cannot be overwritten by database-owned resources with the same identity. Keep resources intended for UI editing database-owned, with the required baseline sections and strict API-key policy present. The documented PostgreSQL startup logging can include the resolved database password: keep raw startup logs out of shared evidence and restrict their access.

Before scripting config-resource writes, check semantics for the exact resource kind and release. The [API guide](https://docs.solo.io/agentgateway/standalone/latest/documentation/operations/config-resources.md) documents collection upsert for `llm.apiKey`, while the [storage guide](https://docs.solo.io/agentgateway/standalone/latest/documentation/setup/storage.md) describes collection replacement for MCP targets. Do not generalize key upserts to models or targets. Prefer a documented operation on the intended resource; if replacing a collection, preserve the other records and avoid overwriting concurrent UI edits. Test a helper against a pre-existing unrelated resource and on a rerun before claiming it preserves state. An unresolved source conflict is a validation gap, not permission to assume non-destructive behavior.
