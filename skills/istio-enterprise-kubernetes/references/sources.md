# Sources and release selection

The [product index](https://docs.solo.io/istio/llms.txt) identifies the stable and supported documentation lines. Resolve the line for the customer's installation or selected new release, then use that line's `llms.txt` and full `.md` pages. `latest` is useful for discovery, not evidence about an older deployment.

- [Service mesh options](https://docs.solo.io/istio/latest/sidecar/about/overview/) distinguishes ambient and sidecar modes and supported image choices.
- [Solo distributions](https://docs.solo.io/istio/latest/about/images/overview/), [supported versions](https://docs.solo.io/istio/latest/about/images/versions/), and [licensing](https://docs.solo.io/istio/latest/about/images/licensing/) establish images, release support, and entitlement. Check the selected line before encoding fields.
- [Ambient Helm installation](https://docs.solo.io/istio/latest/setup/install/manual/) and [sidecar Helm installation](https://docs.solo.io/istio/latest/sidecar/setup/install/manual/) are different paths. For an existing operator-managed installation, consult the selected line's migration or operator guide before changing ownership. Installation methods can change between documentation lines.
- [Ambient multicluster installation](https://docs.solo.io/istio/latest/multicluster/install/default/manual/) and [sidecar multicluster installation](https://docs.solo.io/istio/latest/sidecar/setup/multicluster/default/manual/) apply only when that topology is requested and supported by the selected license.
- [Solo UI setup](https://docs.solo.io/istio/latest/ui/setup/setup/) and [UI security](https://docs.solo.io/istio/latest/ui/security/) apply only if UI access is part of the request.
- [ambientmesh.io](https://ambientmesh.io/llms.txt) and [community Istio](https://istio.io/latest/docs/) provide useful background, but neither establishes a Solo-specific Helm value or licensed feature. The Solo build is [free to use but not open source](https://ambientmesh.io/docs/operations/solo-builds/).

The public [Istio examples in doc-examples](https://github.com/solo-io/doc-examples/tree/main/istio) can supply installation helpers. Treat them as examples: inspect their current implementation and match it to the customer's release and installation path. Check live chart values, CRDs, and runtime status before applying a copied command.
