2025-05-21 Version: 9.0.8
- Update API DescribeDisks: add response parameters Body.Disks.$.Tags.


2025-05-20 Version: 9.0.7
- Update API CreateNetworkAclEntry: add request parameters DestinationCidrBlock.
- Update API DescribeNetworkAcls: add response parameters Body.NetworkAcls.$.IngressAclEntries.$.DestinationCidrBlock.


2025-05-20 Version: 9.0.7
- Update API CreateNetworkAclEntry: add request parameters DestinationCidrBlock.
- Update API DescribeNetworkAcls: add response parameters Body.NetworkAcls.$.IngressAclEntries.$.DestinationCidrBlock.


2025-05-20 Version: 9.0.7
- Update API CreateNetworkAclEntry: add request parameters DestinationCidrBlock.
- Update API DescribeNetworkAcls: add response parameters Body.NetworkAcls.$.IngressAclEntries.$.DestinationCidrBlock.


2025-05-08 Version: 9.0.6
- Update API CreateARMServerInstances: add request parameters Tag.
- Update API CreateDisk: add request parameters InstanceBillingCycle.
- Update API CreateSnapshot: add request parameters InstanceBillingCycle.
- Update API DescribeARMServerInstances: add response parameters Body.Servers.$.Tags.
- Update API RunInstances: add request parameters Ipv6AddressCount.


2025-04-25 Version: 9.0.5
- Update API DescribeEnsEipAddresses: add response parameters Body.EipAddresses.$.Tags.$.Key.
- Update API DescribeEnsEipAddresses: add response parameters Body.EipAddresses.$.Tags.$.Value.
- Update API DescribeNatGateways: add response parameters Body.NatGateways.$.Tags.$.Key.
- Update API DescribeNatGateways: add response parameters Body.NatGateways.$.Tags.$.Value.
- Update API DescribeNetworks: add response parameters Body.Networks.$.Tags.$.Key.
- Update API DescribeNetworks: add response parameters Body.Networks.$.Tags.$.Value.
- Update API DescribeVSwitches: add response parameters Body.VSwitches.$.Tags.$.Key.
- Update API DescribeVSwitches: add response parameters Body.VSwitches.$.Tags.$.Value.
- Update API ModifyInstanceChargeType: add request parameters BillingCycle.


2025-04-10 Version: 9.0.4
- Update API DescribeEnsEipAddresses: add response parameters Body.EipAddresses.$.Tags.
- Update API DescribeNatGateways: add response parameters Body.NatGateways.$.Tags.
- Update API DescribeNetworks: add response parameters Body.Networks.$.Tags.
- Update API DescribeVSwitches: add response parameters Body.VSwitches.$.Tags.


2025-04-10 Version: 9.0.4
- Update API DescribeEnsEipAddresses: add response parameters Body.EipAddresses.$.Tags.
- Update API DescribeNatGateways: add response parameters Body.NatGateways.$.Tags.
- Update API DescribeNetworks: add response parameters Body.Networks.$.Tags.
- Update API DescribeVSwitches: add response parameters Body.VSwitches.$.Tags.


2025-04-08 Version: 9.0.3
- Generated python 2017-11-10 for Ens.

2025-04-07 Version: 9.0.2
- Update API CreateNatGateway: add request parameters InstanceBillingCycle.


2025-04-01 Version: 9.0.1
- Update API CreateARMServerInstances: add request parameters Cidr.
- Update API DescribeFileSystems: add response parameters Body.FileSystems.$.Description.


2025-03-27 Version: 9.0.0
- Support API DescribeInstanceBootConfiguration.
- Support API ImportImage.
- Delete API AddDeviceInternetPort.
- Delete API DeleteDeviceInternetPort.
- Delete API GetDeviceInternetPort.
- Delete API ResetDeviceInstance.
- Delete API RestartDeviceInstance.
- Update API CreateImage: add request parameters WithDataDisks.
- Update API DescribeEnsEipAddresses: add request parameters EnsRegionIds.
- Update API DescribeHaVips: add request parameters EnsRegionIds.
- Update API DescribeSecondaryPublicIpAddresses: add request parameters EnsRegionIds.


2025-03-18 Version: 8.0.0
- Support API DescribeVSwitchAttributes.
- Support API ListProductAbilities.
- Support API ModifyEnsRouteEntry.
- Update API CreateEipInstance: add param ClientToken.
- Update API CreateEnsRouteEntry: add param SourceCidrBlock.
- Update API CreateEnsRouteEntry: update param NextHopType.
- Update API CreateImage: add param TargetOSSRegionId.
- Update API CreateLoadBalancer: add param ClientToken.
- Update API CreateSecurityGroup: add param Permissions.
- Update API CreateSecurityGroup: update param Description.
- Update API CreateSecurityGroup: update param SecurityGroupName.
- Update API CreateSecurityGroup: update response param.
- Update API CreateSnatEntry: add param EipAffinity.
- Update API DeleteNatGateway: add param ForceDelete.
- Update API DescribeCloudDiskAvailableResourceInfo: update response param.
- Update API DescribeElbAvailableResourceInfo: update response param.
- Update API DescribeEnsRouteEntryList: update param NextHopType.
- Update API DescribeEnsRouteEntryList: update param RouteTableId.
- Update API DescribeEnsRouteEntryList: update response param.
- Update API DescribeEnsRouteTables: add param AssociateType.
- Update API DescribeEnsRouteTables: add param EnsRegionIds.
- Update API DescribeEnsRouteTables: add param RouteTableName.
- Update API DescribeEnsRouteTables: add param Type.
- Update API DescribeEnsRouteTables: update param PageSize.
- Update API DescribeEnsRouteTables: update response param.
- Update API DescribeImageInfos: update response param.
- Update API DescribeImageSharePermission: update response param.
- Update API DescribeImages: update response param.
- Update API DescribeLoadBalancerAttribute: update response param.
- Update API DescribeLoadBalancerListeners: add param Description.
- Update API DescribeLoadBalancerListeners: add param ListenerPort.
- Update API DescribeLoadBalancerListeners: update response param.
- Update API DescribeLoadBalancers: add param EnsRegionIds.
- Update API DescribeNatGateways: add param EnsRegionIds.
- Update API DescribeNatGateways: add param NatGatewayIds.
- Update API DescribeNatGateways: update response param.
- Update API DescribeNetworkAttribute: update response param.
- Update API DescribeNetworkInterfaces: add param EnsRegionIds.
- Update API DescribeNetworkInterfaces: add param NetworkInterfaceIds.
- Update API DescribeNetworkInterfaces: update param Ipv6Address.
- Update API DescribeNetworkInterfaces: update param Ipv6Address.
- Update API DescribeNetworks: add param EnsRegionIds.
- Update API DescribeNetworks: add param NetworkIds.
- Update API DescribeNetworks: update response param.
- Update API DescribeSecurityGroups: update param PageNumber.
- Update API DescribeSecurityGroups: update param PageSize.
- Update API DescribeSecurityGroups: update param SecurityGroupId.
- Update API DescribeSecurityGroups: update param SecurityGroupName.
- Update API DescribeSecurityGroups: update response param.
- Update API DescribeSelfImages: update response param.
- Update API DescribeSnatAttribute: update response param.
- Update API DescribeSnatTableEntries: add param SnatIps.
- Update API DescribeSnatTableEntries: update response param.
- Update API DescribeVSwitches: add param EnsRegionIds.
- Update API DescribeVSwitches: add param VSwitchIds.
- Update API DescribeVSwitches: delete param OrderByParams.
- Update API DescribeVSwitches: update param EnsRegionId.
- Update API DescribeVSwitches: update param NetworkId.
- Update API DescribeVSwitches: update param PageNumber.
- Update API DescribeVSwitches: update param PageSize.
- Update API DescribeVSwitches: update param VSwitchId.
- Update API DescribeVSwitches: update param VSwitchName.
- Update API DescribeVSwitches: update response param.
- Update API ModifyForwardEntry: add param ExternalIp.
- Update API ModifyForwardEntry: add param ExternalPort.
- Update API ModifyForwardEntry: add param InternalIp.
- Update API ModifyForwardEntry: add param InternalPort.
- Update API ModifyForwardEntry: add param IpProtocol.
- Update API ModifySnatEntry: add param EipAffinity.
- Update API ModifySnatEntry: add param SnatIp.
- Update API PutBucket: update param BucketAcl.
- Update API PutBucket: update param BucketName.
- Update API PutBucket: update param Comment.
- Update API PutBucket: update param DispatchScope.
- Update API PutBucket: update param EnsRegionId.
- Update API PutBucket: update param LogicalBucketType.
- Update API ReleaseInstance: update response param.
- Update API UnAssociateEnsEipAddress: add param Force.


2024-12-25 Version: 7.7.0
- Support API DeleteEip.
- Update API GetBucketAcl: update param BucketName.


2024-12-02 Version: 7.6.0
- Support API ModifySnatEntry.
- Update API CreateSnatEntry: add param IspAffinity.
- Update API DescribeInstances: add param ServiceStatus.
- Update API DescribeInstances: update response param.
- Update API DescribeSnatAttribute: update response param.
- Update API DescribeSnatTableEntries: update response param.


2024-11-27 Version: 7.5.0
- Support API AttachInstanceSDG.
- Support API DescribeInstanceSDGStatus.
- Support API DetachInstanceSDG.
- Support API MountInstanceSDG.
- Support API UnmountInstanceSDG.


2024-11-27 Version: 7.4.2
- Generated python 2017-11-10 for Ens.

2024-11-26 Version: 7.4.1
- Update API DescribeSDGDeploymentStatus: update response param.
- Update API DescribeSnapshots: add param EnsRegionIds.
- Update API DescribeSnapshots: add param SnapshotName.
- Update API ExportImage: update param OSSPrefix.


2024-11-18 Version: 7.4.0
- Support API CreateNetworkInterface.
- Support API DeleteNetworkInterfaces.
- Update API DescribeDisks: update response param.


2024-11-15 Version: 7.3.0
- Support API CreateHaVip.
- Support API DeleteHaVips.
- Update API PreloadRegionSDG: update param RedundantNum.


2024-11-06 Version: 7.2.0
- Support API DescribeEnsRouteTables.


2024-11-05 Version: 7.1.1
- Update API CreateARMServerInstances: add param EnvironmentVar.
- Update API CreateEnsRouteEntry: update param NextHopType.
- Update API DescribeEnsRouteEntryList: update param NextHopType.
- Update API DescribeEnsRouteEntryList: update response param.


2024-10-25 Version: 7.1.0
- Support API AttachNetworkInterface.
- Support API CreateCluster.
- Support API DescribeCluster.
- Support API DescribeClusterKubeConfig.
- Support API DescribeDiskIopsList.
- Support API DescribeInstanceBandwidthDetail.
- Support API DescribeLoadBalancerListenMonitor.
- Support API DescribeLoadBalancerListeners.
- Support API DescribeSecondaryPublicIpAddresses.
- Support API DescribeServerLoadBalancerListenMonitor.
- Support API DescribeServerLoadBalancerMonitor.
- Support API DetachNetworkInterface.
- Support API ModifyInstanceBootConfiguration.
- Support API ModifyNetworkInterfaceAttribute.
- Update API CreateDisk: add param Tag.
- Update API CreateEipInstance: add param Tag.
- Update API CreateNatGateway: add param Tag.
- Update API CreateNetwork: add param Tag.
- Update API CreateSnatEntry: add param IdleTimeout.
- Update API CreateVSwitch: add param Tag.
- Update API DescribeCloudDiskTypes: add param EnsRegionIds.
- Update API DescribeDisks: update response param.
- Update API DescribeImageInfos: update response param.
- Update API DescribeImages: update response param.
- Update API DescribeInstances: update response param.
- Update API DescribeSelfImages: update response param.
- Update API DescribeSnatAttribute: update response param.
- Update API DescribeSnatTableEntries: update response param.
- Update API GetBucketAcl: update response param.
- Update API ListTagResources: update param ResourceType.
- Update API TagResources: update param ResourceType.
- Update API UntagResources: update param ResourceType.


2024-09-13 Version: 7.0.0
- Support API AssociateHaVip.
- Support API CreateStorageVolume.
- Support API DeleteStorageVolume.
- Support API DescribeHaVips.
- Support API DescribeStorageGateway.
- Support API DescribeStorageVolume.
- Support API ModifyHaVipAttribute.
- Support API PrepareUpload.
- Support API UnassociateHaVip.
- Delete API DescribeApplicationResourceSummary.
- Delete API DescribeEipAddresses.
- Update API CreateLoadBalancerHTTPListener: add param BackendServerPort.
- Update API CreateLoadBalancerHTTPSListener: add param BackendServerPort.
- Update API CreateLoadBalancerHTTPSListener: update param ServerCertificateId.
- Update API CreateLoadBalancerUDPListener: add param EstablishedTimeout.
- Update API CreateNetwork: update param EnsRegionId.
- Update API DescribeInstances: update response param.
- Update API DescribeLoadBalancerHTTPListenerAttribute: update response param.
- Update API DescribeLoadBalancerHTTPSListenerAttribute: update response param.
- Update API DescribeLoadBalancerUDPListenerAttribute: update response param.
- Update API DescribeNetworkInterfaces: add param Ipv6Address.
- Update API DescribeNetworkInterfaces: update response param.
- Update API DescribeSDGDeploymentStatus: add param DeploymentType.
- Update API DescribeSDGDeploymentStatus: add param InstanceIds.
- Update API DescribeSDGDeploymentStatus: add param RegionIds.
- Update API DescribeSDGDeploymentStatus: add param Status.
- Update API DescribeSDGDeploymentStatus: update param PageNumber.
- Update API DescribeSDGDeploymentStatus: update param PageSize.
- Update API DescribeSelfImages: update response param.
- Update API PutBucketLifecycle: update response param.
- Update API RunInstances: add param SpotDuration.
- Update API RunInstances: update param IpType.
- Update API SetLoadBalancerUDPListenerAttribute: add param EstablishedTimeout.


2024-07-04 Version: 6.2.1
- Generated python 2017-11-10 for Ens.

2024-07-04 Version: 6.2.0
- Support API CreateStorageGateway.
- Support API DeleteStorageGateway.


2024-07-03 Version: 6.1.0
- Support API DeployInstanceSDG.
- Support API DescribeSDG.
- Support API ListTagResources.
- Support API PreloadRegionSDG.
- Support API RemoveInstanceSDG.
- Support API TagResources.
- Support API UnloadRegionSDG.
- Support API UntagResources.
- Update API CreateEipInstance: update param InternetChargeType.
- Update API CreateEnsSaleControl: add param CustomAccount.
- Update API CreateEnsSaleControl: update param AliUidAccount.
- Update API CreateForwardEntry: update param InternalIp.
- Update API DeleteEnsSaleConditionControl: add param CustomAccount.
- Update API DeleteEnsSaleConditionControl: update param AliUidAccount.
- Update API DeleteEnsSaleControl: add param CustomAccount.
- Update API DeleteEnsSaleControl: update param AliUidAccount.
- Update API DeleteSDG: update response param.
- Update API DescribeInstances: add param InstanceType.
- Update API DescribeLoadBalancerHTTPListenerAttribute: update response param.
- Update API PutBucket: add param DispatchScope.
- Update API SetLoadBalancerHTTPListenerAttribute: add param XForwardedFor.
- Update API UpdateEnsSaleControl: add param CustomAccount.
- Update API UpdateEnsSaleControl: update param AliUidAccount.


2024-05-22 Version: 6.0.0
- Support API CreateSDG.
- Support API DeleteSDG.
- Support API DescribeSDGs.
- Support API RemoveSDG.
- Support API SaveSDG.
- Delete API DescribeWorkflow.
- Delete API DescribeWorkflowActivity.
- Delete API RestartWorkflow.
- Delete API RetryWorkflow.
- Delete API RollbackWorkflow.
- Delete API TerminateWorkflow.
- Update API CreateARMServerInstances: update param InstanceType.
- Update API CreateARMServerInstances: update param ServerType.
- Update API CreateImage: update response param.
- Update API DeleteBucket: update response param.
- Update API DeleteBucketLifecycle: update response param.
- Update API DescribeApplication: add param ResourceSelector.
- Update API DescribeInstances: update response param.
- Update API GetBucketLifecycle: update response param.
- Update API PutBucketAcl: update response param.
- Update API PutBucketLifecycle: update response param.
- Update API ResetAICInstance: delete param InstanceIds.
- Update API RunInstances: add param AutoReleaseTime.
- Update API RunInstances: add param SpotStrategy.
- Update API UpgradeApplication: update response param.


2024-02-06 Version: 5.0.0
- Generated python 2017-11-10 for Ens.

2023-12-18 Version: 4.0.0
- Generated python 2017-11-10 for Ens.

2023-07-20 Version: 3.0.18
- Support clouddisk API.

2023-06-13 Version: 3.0.17
- Support AIC API.

2023-06-01 Version: 3.0.16
- Support SNAT API.

2023-05-16 Version: 3.0.15
- Support RunInstances API.

2023-03-28 Version: 3.0.14
- Support ARM API.

2023-03-09 Version: 3.0.13
- Support Disk API.

2023-03-02 Version: 3.0.12
- Support Snapshot API.

2022-12-27 Version: 3.0.11
- Support Snapshot API.

2022-11-29 Version: 3.0.10
- Support DescribeARMServerInstances.
- Support DeleteInstances.

2022-10-13 Version: 3.0.9
- Support DescribeAICImages.

2022-09-22 Version: 3.0.8
- Support ipv4-network.

2022-08-09 Version: 3.0.7
- Support API ARMInstance.
- Support Control ARM API.

2022-07-26 Version: 3.0.6
- Support API ARMInstance.
- Support Control ARM API.

2022-07-14 Version: 3.0.5
- Support API ARMInstance.

2022-06-21 Version: 3.0.4
- Support API NetWork.

2022-05-12 Version: 3.0.3
- Support API DeleteImage.

2022-04-08 Version: 3.0.2
- Support API CreateInstance Use Param PasswordInherit.

2022-03-29 Version: 3.0.1
- Support cloud disk.

2022-01-28 Version: 3.0.0
- Support cloud disk.

2021-02-20 Version: 2.0.0
- AMP Version Change.

2020-10-22 Version: 1.0.1
- Publish Ens share image apis.

2020-10-15 Version: 1.0.0
- Publish Ens apis first version.

