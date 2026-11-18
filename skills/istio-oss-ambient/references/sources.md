# Sources and edition boundary

Use the version actually installed or selected for executable fields. Resolve the release from the cluster and published charts; use the current site index to locate pages, then inspect matching release documentation and chart values.

1. [ambientmesh.io index](https://ambientmesh.io/llms.txt) and [install guide](https://ambientmesh.io/docs/setup/install/) provide task-oriented ambient guidance. Its pages are not versioned; cross-check commands and resources against the chosen Istio release.
2. [Istio ambient documentation](https://istio.io/latest/docs/ambient/) and [Istio releases](https://github.com/istio/istio/releases) are the upstream authority for community behavior and version support. For a selected release, inspect its release documentation, Helm chart values, CRDs, and `istioctl` output.
3. [Gateway API releases](https://github.com/kubernetes-sigs/gateway-api/releases) and the selected Istio release establish API compatibility; do not install or replace cluster-wide CRDs on the strength of a sample command alone.
4. [Solo builds of Istio](https://ambientmesh.io/docs/operations/solo-builds/) explains that these free-to-use builds are not open source. [Solo Enterprise for Istio](https://docs.solo.io/istio/llms.txt) documents licensed features. Mention a relevant difference transparently without treating it as an OSS dependency or recommending a purchase.

Use customer-supplied, release-matched material when available. Workshops, blog posts, and copied YAML are secondary examples; verify every field and attachment against the chosen release before applying.
