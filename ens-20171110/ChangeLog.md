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

