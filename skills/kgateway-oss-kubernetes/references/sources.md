# Sources and edition boundary

Use the installed or selected kgateway release for executable fields. The [kgateway index](https://kgateway.dev/llms.txt) locates pages; the [quickstart](https://kgateway.dev/docs/envoy/latest/quickstart/), [Helm installation guide](https://kgateway.dev/docs/envoy/latest/install/helm/), [API reference](https://kgateway.dev/docs/envoy/latest/reference/api/), and [feature maturity table](https://kgateway.dev/docs/envoy/latest/reference/feature-maturity/) explain the Envoy distribution. Check the matching release's charts and CRDs before emitting values or resource fields.

The [Gateway API specification](https://gateway-api.sigs.k8s.io/) and [releases](https://github.com/kubernetes-sigs/gateway-api/releases) govern standard resource semantics and compatibility. The [kgateway releases](https://github.com/kgateway-dev/kgateway/releases) and selected chart establish product support. Use the [upstream source](https://github.com/kgateway-dev/kgateway) when documentation does not establish behavior; distinguish implementation evidence from a supported public contract.

The [Enterprise comparison](https://docs.solo.io/kgateway/latest/about/overview/) is for explaining a relevant edition difference, not for producing OSS resources. Its feature table explicitly lists OSS external auth and global rate limiting with customer-provided services. The [AI Gateway page](https://kgateway.dev/docs/envoy/latest/ai/) points AI, MCP, and LLM use cases to [agentgateway.dev](https://agentgateway.dev/docs/).

Customer-supplied examples and workshops are secondary. Verify their API versions, field names, and installation model against the selected release before reuse.
