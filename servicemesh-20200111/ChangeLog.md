2025-11-24 Version: 3.4.0
- Support API DescribeMeshMultiClusterNetwork.
- Support API ModifyPilotEipResource.
- Support API UpdateGuestClusterConfig.
- Support API UpdateMeshMultiClusterNetwork.
- Update API AddClusterIntoServiceMesh: add request parameters DiscoveryOnly.
- Update API AddClusterIntoServiceMesh: add request parameters Kubeconfig.
- Update API CreateServiceMesh: add request parameters CertChain.
- Update API CreateServiceMesh: add request parameters EnableACMG.
- Update API CreateServiceMesh: add request parameters PlaygroundScene.
- Update API CreateSwimLaneGroup: add request parameters IngressGatewayNamespace.
- Update API DescribeCCMVersion: add response parameters Body.CCMVersions.SLBGracefulDrainSupported.
- Update API DescribeClusterGrafana: add request parameters ReAddPrometheusIntegration.
- Update API DescribeClustersInServiceMesh: add response parameters Body.Clusters.$.GuestClusterConfig.
- Update API DescribeMetadata: add response parameters Body.MetaData.CompatibilityInfoList.
- Update API DescribeMetadata: add response parameters Body.MetaData.PlaygroundScene.
- Update API DescribeNamespaceScopeSidecarConfig: add response parameters Body.ConfigPatches.RuntimeValues.
- Update API DescribeNamespaceScopeSidecarConfig: add response parameters Body.ConfigPatches.SMCConfiguration.
- Update API DescribeNamespaceScopeSidecarConfig: add response parameters Body.ConfigPatches.ScaledSidecarResource.
- Update API DescribeReusableSlb: add request parameters LbType.
- Update API DescribeReusableSlb: add request parameters ServiceMeshId.
- Update API DescribeServiceMeshAdditionalStatus: add response parameters Body.ClusterStatus.CanaryPilotEIPStatus.
- Update API DescribeServiceMeshAdditionalStatus: add response parameters Body.ClusterStatus.PilotEIPStatus.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Endpoints.IntranetCanaryPilotEndpoint.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Endpoints.PublicCanaryPilotEndpoint.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.LoadBalancer.ApiServerPublicEipId.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.LoadBalancer.CanaryPilotLoadBalancerId.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.LoadBalancer.CanaryPilotPublicEipId.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.LoadBalancer.PilotPublicEipId.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.MeshConfig.ExtraConfiguration.IstiodExtraConfiguration.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.MeshConfig.ExtraConfiguration.Playground.
- Update API DescribeServiceMeshDetail: add response parameters Body.ServiceMesh.Spec.MeshConfig.LocalityLB.FailoverPriority.
- Update API DescribeServiceMeshes: add response parameters Body.ServiceMeshes.$.Spec.MeshConfig.ExtraConfiguration.
- Update API GetSwimLaneDetail: add response parameters Body.ValidationMessage.
- Update API GetSwimLaneDetail: add response parameters Body.WeightedIngressDestination.
- Update API GetSwimLaneGroupList: add response parameters Body.SwimLaneGroupList.$.IngressRoutingStrategy.
- Update API GetSwimLaneGroupList: add response parameters Body.SwimLaneGroupList.$.ServiceLevelFallbackTarget.
- Update API GetSwimLaneGroupList: add response parameters Body.SwimLaneGroupList.$.WeightedIngressRule.
- Update API GetSwimLaneList: add response parameters Body.SwimLaneList.$.ValidationMessage.
- Update API GetSwimLaneList: add response parameters Body.SwimLaneList.$.WeightedIngressDestinatin.
- Update API UpdateMeshFeature: add request parameters CertChain.
- Update API UpdateMeshFeature: add request parameters ExistingCaCert.
- Update API UpdateMeshFeature: add request parameters ExistingCaKey.
- Update API UpdateMeshFeature: add request parameters ExistingRootCaCert.
- Update API UpdateMeshFeature: add request parameters LabelsForOffloadedWorkloads.
- Update API UpdateMeshFeature: add request parameters PilotEnableQuicListeners.
- Update API UpdateMeshFeature: add request parameters SMCEnabled.
- Update API UpdateMeshFeature: add request parameters TracingOnExtZipkinReplicaCount.
- Update API UpdateNamespaceScopeSidecarConfig: add request parameters RuntimeValues.
- Update API UpdateNamespaceScopeSidecarConfig: add request parameters SMCEnabled.
- Update API UpdateNamespaceScopeSidecarConfig: add request parameters ScaledSidecarResource.
- Update API UpdateSwimLaneGroup: add request parameters IngressRoutingStrategy.
- Update API UpdateSwimLaneGroup: add request parameters ServiceLevelFallbackTarget.
- Update API UpdateSwimLaneGroup: add request parameters WeightedIngressRule.


2023-11-13 Version: 3.3.1
- Generated python 2020-01-11 for servicemesh.

2023-11-08 Version: 3.3.0
- Generated python 2020-01-11 for servicemesh.

2023-09-12 Version: 3.2.1
- Generated python 2020-01-11 for servicemesh.

2023-08-31 Version: 3.2.0
- Generated python 2020-01-11 for servicemesh.

2023-08-22 Version: 3.1.1
- Generated python 2020-01-11 for servicemesh.

2023-08-16 Version: 3.1.0
- Generated python 2020-01-11 for servicemesh.

2023-08-11 Version: 3.0.2
- Generated python 2020-01-11 for servicemesh.

2023-08-09 Version: 3.0.1
- Generated python 2020-01-11 for servicemesh.

2023-07-27 Version: 3.0.0
- Support setting revision for UpdateIstioInjectionConfig.
- Remove DescribeIngressGateways.

2023-05-08 Version: 2.0.27
- Support setting TPROXY mode.

2022-12-01 Version: 2.0.26
- Support setting TPROXY mode.

2022-11-24 Version: 2.0.25
- Update ASM APIs.

2022-11-02 Version: 2.0.24
- UpdateMeshFetaure support additional global Sidecar config.

2022-10-14 Version: 2.0.23
- DescribeGuestClusterNamespaces support show namespace labels.

2022-09-08 Version: 2.0.22
- UpdateCRAggregation support using public API Server endpoint of ASM.

2022-08-31 Version: 2.0.21
- DescribeServiceMeshDetail support service mesh auto diagnosis feature.

2022-08-25 Version: 2.0.20
- UpdateMeshFeature support modify service mesh auto diagnosis feature.

2022-08-17 Version: 2.0.19
- UpdateMeshFeature support modify service mesh auto diagnosis feature.

2022-07-11 Version: 2.0.18
- Add UpdateASMNamespaceFromGuestCluster API.

2022-05-26 Version: 2.0.17
- Update servicemesh api.

2022-04-28 Version: 2.0.16
- Update servicemesh api.

2022-04-20 Version: 2.0.15
Update servicemesh apis

2022-04-07 Version: 2.0.14
- New build from amp.


2022-04-06 Version: 2.0.13
- New build from amp.


2022-03-29 Version: 2.0.12
- New build from amp.


2022-03-29 Version: 2.0.11
- New build from amp.


2022-03-16 Version: 2.0.9
- New build from amp.


2022-03-16 Version: 2.0.8
- New build from amp.


2022-02-22 Version: 2.0.7
- New build from amp.


2022-02-17 Version: 2.0.6
- New build from amp.


2022-01-27 Version: 2.0.5
- New build from amp.


2022-01-04 Version: 2.0.4
- New build from amp.


2021-12-28 Version: 2.0.3
- New build from amp.


2021-05-25 Version: 1.1.3
- New build from amp.


2021-03-23 Version: 1.1.2
- New build from amp.


2021-03-13 Version: 1.1.1
- AMP Version Change.

2021-03-12 Version: 1.1.0
- New build from amp.


2021-02-19 Version: 1.0.12
- Generated python 2020-01-11 for servicemesh.

2021-01-25 Version: 1.0.11
- Generated python 2020-01-11 for servicemesh.

2021-01-14 Version: 1.0.10
- Generated python 2020-01-11 for servicemesh.

2020-12-29 Version: 2.0.1
- AMP Version Change.

2020-12-28 Version: 2.0.0
- AMP Version Change.

2020-12-17 Version: 1.0.9
- Generated python 2020-01-11 for servicemesh.

2020-11-20 Version: 1.0.8
- Generated python 2020-01-11 for servicemesh.

2020-09-08 Version: 1.0.7
- Support adding or removing vm app to mesh.

