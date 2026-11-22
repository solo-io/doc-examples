# Customer skills

These public skill folders are the source for customer-facing assistant guides. Choose the product and configuration mode that match the work:

| Skill | Scope |
| --- | --- |
| [agentgateway-enterprise-standalone](agentgateway-enterprise-standalone/SKILL.md) | Enterprise Agentgateway standalone configuration on a host or in a container, including standalone Helm hosting |
| [agentgateway-enterprise-kubernetes](agentgateway-enterprise-kubernetes/SKILL.md) | Enterprise Agentgateway Kubernetes controller, Gateway API, and CRDs |
| [istio-oss-ambient](istio-oss-ambient/SKILL.md) | Community Istio in ambient mode on Kubernetes |
| [istio-enterprise-kubernetes](istio-enterprise-kubernetes/SKILL.md) | Solo Enterprise for Istio on Kubernetes, in ambient or sidecar mode |
| [kgateway-oss-kubernetes](kgateway-oss-kubernetes/SKILL.md) | Open-source kgateway with Envoy and Gateway API on Kubernetes |
| [kgateway-enterprise-kubernetes](kgateway-enterprise-kubernetes/SKILL.md) | Solo Enterprise for kgateway with licensed gateway services and portal |

From a project directory, install the skill you need. For example:

```sh
npx skills add https://github.com/solo-io/doc-examples --skill agentgateway-enterprise-standalone --agent codex
npx skills add https://github.com/solo-io/doc-examples --skill agentgateway-enterprise-kubernetes --agent codex
npx skills add https://github.com/solo-io/doc-examples --skill istio-oss-ambient --agent codex
npx skills add https://github.com/solo-io/doc-examples --skill istio-enterprise-kubernetes --agent codex
npx skills add https://github.com/solo-io/doc-examples --skill kgateway-oss-kubernetes --agent codex
npx skills add https://github.com/solo-io/doc-examples --skill kgateway-enterprise-kubernetes --agent codex
```

For Claude Code, use `--agent claude-code`. The installer places the selected complete folder in the project's skill directory. Installing a skill does not install the product.

The skills read current public documentation for the selected runtime. Keep each complete skill folder together if installing manually. No private repository or internal support system is required by a customer.

Keep the published skills client-neutral. Do not add optional `agents/openai.yaml` metadata to these or future skill packages.

## Maintaining the packages

Edit the source files in this repo. After a content change, refresh and check the content fingerprints:

```sh
python3 scripts/refresh-skill-metadata.py
python3 scripts/refresh-skill-metadata.py --check
```

The original `refresh-agentgateway-skill-metadata.py` command remains available as a compatibility entry point.

The CI check also verifies skill names, relative references, and package contents. The docs guides should point to this repo for installation, so publishing a content change does not require rebuilding docs-hosted ZIP files.
