2025-07-16 Version: 6.8.2
- Generated python 2021-07-01 for eas.

2025-06-13 Version: 6.8.1
- Update API DescribeGateway: add response parameters Body.ChargeType.
- Update API ListGatewayDomains: add response parameters Body.CustomDomains.$.CertificateEndDate.
- Update API ListGatewayDomains: add response parameters Body.CustomDomains.$.CertificateName.
- Update API ListGatewayDomains: add response parameters Body.CustomDomains.$.CertificateStartDate.
- Update API ListGatewayDomains: add response parameters Body.CustomDomains.$.CertificateStatus.
- Update API ListGatewayDomains: add response parameters Body.CustomDomains.$.CreateTime.
- Update API ListGatewayDomains: add response parameters Body.CustomDomains.$.UpdateTime.
- Update API ListGatewayIntranetLinkedVpcPeer: add response parameters Body.PeerVpcList.$.PeerVpcs.$.Status.


2025-05-12 Version: 6.8.0
- Support API UpdateGroup.


2025-04-27 Version: 6.7.5
- Update API ListServices: add request parameters ResourceAliasName.
- Update API ListServices: add request parameters ResourceId.


2025-04-23 Version: 6.7.4
- Update API CreateResource: add request parameters body.ResourceName.


2025-04-23 Version: 6.7.3
- Update API CreateGatewayIntranetLinkedVpc: add request parameters AccountId.
- Update API ListGatewayIntranetLinkedVpc: add response parameters Body.IntranetLinkedVpcList.$.AccountId.


2025-04-08 Version: 6.7.2
- Update API ListServices: add request parameters IncludeNoWorkspace.


2025-04-08 Version: 6.7.2
- Update API ListServices: add request parameters IncludeNoWorkspace.


2025-04-01 Version: 7.0.0
- Update API DescribeGroupEndpoints: update response parameters Body.Endpoints' type has changed.
- Update API DescribeGroupEndpoints: delete response parameters Body.Endpoints.
- Update API DescribeServiceEndpoints: update response parameters Body.Endpoints' type has changed.
- Update API DescribeServiceEndpoints: delete response parameters Body.Endpoints.


2025-03-27 Version: 6.7.0
- Support API DescribeRegions.
- Update API CreateGatewayIntranetLinkedVpc: add request parameters EnableAuthoritativeDns.
- Update API ListGatewayIntranetLinkedVpc: add response parameters Body.IntranetLinkedVpcList.$.AuthoritativeDnsEnabled.
- Update API ListServices: add request parameters ResourceType.


2025-02-25 Version: 6.6.0
- Support API DescribeMachineSpec.


2025-02-05 Version: 6.5.0
- Support API DeleteResourceInstanceLabel.
- Support API UpdateResourceInstanceLabel.
- Update API CreateResource: update param body.
- Update API CreateResourceInstances: update param body.
- Update API CreateVirtualResource: update param body.
- Update API DescribeVirtualResource: update response param.
- Update API ListResourceInstanceWorker: add param WorkerName.
- Update API ListResourceInstances: add param Label.
- Update API ListResourceInstances: update response param.
- Update API ListResources: add param Order.
- Update API ListResources: add param ResourceStatus.
- Update API ListResources: add param Sort.
- Update API ListVirtualResource: update response param.
- Update API ReleaseService: update param body.
- Update API UpdateVirtualResource: update param body.


2025-01-13 Version: 6.4.1
- Update API ReleaseService: update param body.


2024-12-26 Version: 6.4.0
- Support API DescribeServiceSignedUrl.


2024-12-25 Version: 6.3.0
- Support API DescribeGroupEndpoints.
- Support API DescribeServiceEndpoints.


2024-12-10 Version: 6.2.0
- Support API ListGatewayIntranetSupportedZone.
- Update API DescribeGateway: update response param.
- Update API DescribeResource: update response param.
- Update API ListGateway: update response param.
- Update API UpdateGateway: update param body.


2024-11-04 Version: 6.1.0
- Support API AttachGatewayDomain.
- Support API CreateGatewayIntranetLinkedVpcPeer.
- Support API CreateVirtualResource.
- Support API DeleteGatewayIntranetLinkedVpcPeer.
- Support API DeleteVirtualResource.
- Support API DescribeVirtualResource.
- Support API DetachGatewayDomain.
- Support API ListGatewayDomains.
- Support API ListGatewayIntranetLinkedVpcPeer.
- Support API ListVirtualResource.
- Support API UpdateVirtualResource.


2024-10-11 Version: 6.0.1
- Update API CreateAclPolicy: update param AclPolicyList.
- Update API CreateGateway: update param body.
- Update API ListAclPolicy: update param ClusterId.
- Update API ListAclPolicy: update param GatewayId.
- Update API ListGateway: add param ResourceName.
- Update API ListGateway: update response param.
- Update API ListServices: add param Role.


2024-09-02 Version: 6.0.0
- Update API ListAclPolicy: update response param.


2024-08-28 Version: 5.1.0
- Support API ListTenantAddons.
- Support API ReinstallTenantAddon.


2024-08-28 Version: 5.0.0
- Support API CreateAclPolicy.
- Support API DeleteAclPolicy.
- Support API ListAclPolicy.
- Support API ListGateway.
- Update API CloneService: add param Labels.
- Update API CloneService: update param body.
- Update API CreateGateway: update param body.
- Update API DescribeGateway: update response param.
- Update API ListResourceServices: update response param.
- Update API ListServices: add param Gateway.
- Update API UpdateGateway: update param body.


2024-07-19 Version: 4.2.1
- Update API CreateResourceLog: update param body.
- Update API DescribeServiceCronScaler: update param ClusterId.
- Update API DescribeServiceCronScaler: update param ServiceName.
- Update API DescribeSpotDiscountHistory: update param InstanceType.
- Update API ListServiceContainers: update param ClusterId.
- Update API ListServiceContainers: update param ServiceName.
- Update API ListServiceContainers: update param InstanceName.


2024-04-18 Version: 4.2.0
- Support API DescribeSpotDiscountHistory.


2024-04-09 Version: 4.1.0
- Support API CloneService.
- Update API ListResourceInstanceWorker: update response param.
- Update API ListServiceVersions: update response param.
- Update API ListServices: add param QuotaId.
- Update API UpdateAppService: update param body.
- Update API UpdateService: add param UpdateType.


2024-04-09 Version: 4.1.0
- Support API CloneService.
- Update API ListResourceInstanceWorker: update response param.
- Update API ListServiceVersions: update response param.
- Update API ListServices: add param QuotaId.
- Update API UpdateAppService: update param body.
- Update API UpdateService: add param UpdateType.


2024-01-26 Version: 4.0.1
- Update API ListResourceInstanceWorkerupdate response param.
- Update API ListServiceVersionsupdate response param.
- Update API ListServicesadd QuotaId param.
- Update API UpdateAppServiceupdate body param.
- Update API UpdateServiceadd UpdateType param.


2023-11-17 Version: 4.0.0
- Generated python 2021-07-01 for eas.

2023-11-17 Version: 3.0.0
- Generated python 2021-07-01 for eas.

2023-08-24 Version: 2.1.1
- Generated python 2021-07-01 for eas.

2023-07-20 Version: 2.1.0
- Add diagnosis api.

2023-05-17 Version: 2.0.4
- Update autoscaler api.

2023-02-10 Version: 2.0.3
- Add service label api.

2022-11-30 Version: 2.0.2
- Add safety lock api.

2022-11-02 Version: 2.0.1
- Add new api for benchmark test.

2022-08-15 Version: 1.1.7
- Fix bug.

2022-08-11 Version: 1.1.6
- Add some missing field.

2022-08-05 Version: 1.1.5
- Fix AutoScaler API bug.

2022-07-28 Version: 1.1.4
- Fix bug.

2022-07-18 Version: 1.1.3
- Add chargetype in list resource instance api.

2022-04-07 Version: 1.1.2
- Add DescribeRegion api.

2022-02-24 Version: 1.1.1
- Add cron scaler related api.

2022-02-22 Version: 1.1.0
- Add cron scaler related api.

2021-12-09 Version: 1.0.3
- Add accesstoken to service struct.

2021-12-09 Version: 1.0.2
- Add accesstoken to describe service api.

2021-12-08 Version: 1.0.1
- Add accesstoken to describe service api.

2021-11-30 Version: 1.0.0
- The first version for eas openapi v2.

