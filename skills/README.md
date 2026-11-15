# Enterprise Agentgateway skills

These public skill folders are the source for the Enterprise Agentgateway assistant guides on docs.solo.io. Choose the deployment mode that matches the gateway you want to manage:

| Skill | Configuration model |
| --- | --- |
| [agentgateway-enterprise-standalone](agentgateway-enterprise-standalone/SKILL.md) | Standalone configuration on a host or in a container, including standalone Helm hosting |
| [agentgateway-enterprise-kubernetes](agentgateway-enterprise-kubernetes/SKILL.md) | Kubernetes controller, Gateway API, and CRDs |

From a project directory, install one skill for your assistant:

```sh
npx skills add https://github.com/solo-io/doc-examples --skill agentgateway-enterprise-standalone --agent codex
npx skills add https://github.com/solo-io/doc-examples --skill agentgateway-enterprise-kubernetes --agent codex
```

For Claude Code, use `--agent claude-code`. The installer places the selected complete folder in the project's skill directory. Installing a skill does not install or configure Agentgateway.

The skills read current public documentation for the selected runtime. Keep `SKILL.md`, `references/`, `scripts/`, and `package.json` together if installing manually. No private repository or internal support system is required by a customer.

Keep the published skills client-neutral. Do not add optional `agents/openai.yaml` metadata to these or future skill packages.

## Maintaining the packages

Edit the source files in this repo. After a content change, refresh and check the content fingerprints:

```sh
python3 scripts/refresh-agentgateway-skill-metadata.py
python3 scripts/refresh-agentgateway-skill-metadata.py --check
```

The CI check also verifies skill names, relative references, and package contents. The docs guides should point to this repo for installation, so publishing a content change does not require rebuilding docs-hosted ZIP files.
