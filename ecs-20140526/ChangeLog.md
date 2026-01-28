2026-01-28 Version: 7.5.2
- Generated python 2014-05-26 for Ecs.

2026-01-08 Version: 7.5.1
- Update API RunInstances: add request parameters NetworkInterface.$.SecondaryPrivateIpAddressCount.


2026-01-05 Version: 7.5.0
- Support API DescribeLockedSnapshots.
- Support API LockSnapshot.
- Support API UnlockSnapshot.
- Update API DescribeInstanceAutoRenewAttribute: add response parameters Body.InstanceRenewAttributes.$.EnableExpectedRenewDay.


2025-12-24 Version: 7.4.2
- Update API CreateAutoProvisioningGroup: add request parameters ExecutionMode.


2025-12-19 Version: 7.4.1
- Update API DescribeManagedInstances: add request parameters Connected.


2025-12-03 Version: 7.4.0
- Support API DisableNetworkInterfaceQoS.
- Support API EnableNetworkInterfaceQoS.
- Update API DescribeNetworkInterfaceAttribute: add response parameters Body.QoSConfig.


2025-12-01 Version: 7.3.0
- Support API OpenSnapshotService.
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.SecurityOptions.


2025-10-29 Version: 7.2.5
- Update API ReleaseDedicatedHost: add request parameters TerminateSubscription.


2025-10-17 Version: 7.2.4
- Update API CreateImagePipeline: add request parameters ImportImageOptions.Description.
- Update API CreateImagePipeline: add request parameters ImportImageOptions.ImageName.
- Update API CreateImagePipeline: add request parameters ImportImageOptions.ImportImageTags.
- Update API CreateImagePipeline: add request parameters ImportImageOptions.RetentionStrategy.
- Update API CreateImagePipeline: add request parameters ImportImageOptions.RoleName.
- Update API CreateImagePipeline: add request parameters ImportImageOptions.Features.ImdsSupport.
- Update API DescribeImagePipelines: add response parameters Body.ImagePipeline.$.ImportImageOptions.Description.
- Update API DescribeImagePipelines: add response parameters Body.ImagePipeline.$.ImportImageOptions.ImageName.
- Update API DescribeImagePipelines: add response parameters Body.ImagePipeline.$.ImportImageOptions.ImportImageTags.
- Update API DescribeImagePipelines: add response parameters Body.ImagePipeline.$.ImportImageOptions.RetentionStrategy.
- Update API DescribeImagePipelines: add response parameters Body.ImagePipeline.$.ImportImageOptions.RoleName.
- Update API DescribeImagePipelines: add response parameters Body.ImagePipeline.$.ImportImageOptions.Features.ImdsSupport.


2025-10-10 Version: 7.2.3
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.CpuOptions.
- Update API DescribeManagedInstances: add request parameters MachineId.


2025-10-10 Version: 7.2.3
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.CpuOptions.
- Update API DescribeManagedInstances: add request parameters MachineId.


2025-10-10 Version: 7.2.3
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.CpuOptions.
- Update API DescribeManagedInstances: add request parameters MachineId.


2025-09-18 Version: 7.2.2
- Update API CreateLaunchTemplate: add request parameters SecurityOptions.
- Update API CreateLaunchTemplateVersion: add request parameters SecurityOptions.
- Update API DescribeImages: add response parameters Body.Images.$.LicenseType.
- Update API DescribeInstanceHistoryEvents: add response parameters Body.InstanceSystemEventSet.$.ExtendedAttribute.MetricName.
- Update API DescribeInstanceHistoryEvents: add response parameters Body.InstanceSystemEventSet.$.ExtendedAttribute.MetricValue.
- Update API DescribeLaunchTemplateVersions: add response parameters Body.LaunchTemplateVersionSets.$.LaunchTemplateData.SecurityOptions.
- Update API StartTerminalSession: add request parameters EncryptionOptions.


2025-08-25 Version: 7.2.1
- Generated python 2014-05-26 for Ecs.

2025-08-19 Version: 7.2.0
- Support API ModifyInstanceClockOptions.
- Update API DescribeSecurityGroupAttribute: add request parameters Attribute.
- Update API DescribeSecurityGroupAttribute: add response parameters Body.SnapshotPolicyIds.


2025-08-06 Version: 7.1.3
- Update API RunInstances: add request parameters ClockOptions.


2025-07-31 Version: 7.1.2
- Update API DescribeInvocationResults: add response parameters Body.Invocation.InvocationResults.$.OssOutputDelivery.
- Update API DescribeInvocationResults: add response parameters Body.Invocation.InvocationResults.$.OssOutputStatus.
- Update API DescribeInvocationResults: add response parameters Body.Invocation.InvocationResults.$.OssOutputUri.
- Update API DescribeInvocations: add response parameters Body.Invocations.$.OssOutputDelivery.
- Update API DescribeInvocations: add response parameters Body.Invocations.$.InvokeInstances.$.OssOutputStatus.
- Update API DescribeInvocations: add response parameters Body.Invocations.$.InvokeInstances.$.OssOutputUri.
- Update API InvokeCommand: add request parameters OssOutputDelivery.
- Update API RunCommand: add request parameters OssOutputDelivery.


2025-07-30 Version: 7.1.1
- Update API DescribePrice: add request parameters SchedulerOptions.DeploymentSetStrategy.


2025-07-28 Version: 7.1.0
- Support API DescribeAutoSnapshotPolicyAssociations.
- Support API ModifyInstanceNetworkOptions.
- Update API CancelAutoSnapshotPolicy: add request parameters autoSnapshotPolicyId.
- Update API DescribeInstanceAttribute: add response parameters Body.NetworkOptions.BandwidthWeighting.
- Update API RunInstances: add request parameters NetworkOptions.BandwidthWeighting.


2025-07-24 Version: 7.0.17
- Update API DescribeDeploymentSets: add response parameters Body.DeploymentSets.$.AccountId.


2025-07-18 Version: 7.0.16
- Update API DescribeCloudAssistantSettings: add response parameters Body.SessionManagerConfig.
- Update API ModifyCloudAssistantSettings: add request parameters SessionManagerConfig.


2025-07-16 Version: 7.0.15
- Generated python 2014-05-26 for Ecs.

2025-07-14 Version: 7.0.14
- Update API DescribeInstances: add response parameters Body.Instances.$.ClockOptions.


2025-07-08 Version: 7.0.13
- Update API DescribeDedicatedHosts: add request parameters QueryInventory.
- Update API DescribeDedicatedHosts: add response parameters Body.DedicatedHosts.$.Capacity.AvailableInstanceTypes.


2025-06-27 Version: 7.0.12
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.SchedulerOptions.


2025-06-27 Version: 7.0.11
- Update API CreateLaunchTemplate: add request parameters ImageOptions.
- Update API CreateLaunchTemplateVersion: add request parameters ImageOptions.
- Update API DescribeLaunchTemplateVersions: add response parameters Body.LaunchTemplateVersionSets.$.LaunchTemplateData.ImageOptions.


2025-06-13 Version: 7.0.10
- Update API DescribeDiskDefaultKMSKeyId: add request parameters OwnerId.
- Update API DescribeDiskEncryptionByDefaultStatus: add request parameters OwnerId.
- Update API DisableDiskEncryptionByDefault: add request parameters OwnerId.
- Update API ModifyDiskDefaultKMSKeyId: add request parameters OwnerId.
- Update API ResetDiskDefaultKMSKeyId: add request parameters OwnerId.


2025-06-12 Version: 7.0.9
- Update API DescribeTerminalSessions: add response parameters Body.Sessions.$.Connections.$.FailedDetail.
- Update API StartTerminalSession: add request parameters PasswordName.


2025-05-29 Version: 7.0.8
- Update API DescribeInstanceAttribute: add response parameters Body.NetworkOptions.


2025-05-29 Version: 7.0.8
- Update API DescribeInstanceAttribute: add response parameters Body.NetworkOptions.


2025-05-29 Version: 7.0.8
- Update API DescribeInstanceAttribute: add response parameters Body.NetworkOptions.


2025-05-27 Version: 7.0.7
- Update API CreateLaunchTemplate: add request parameters SystemDisk.KMSKeyId.
- Update API CreateLaunchTemplate: add request parameters DataDisk.$.KMSKeyId.
- Update API CreateLaunchTemplateVersion: add request parameters SystemDisk.KMSKeyId.
- Update API CreateLaunchTemplateVersion: add request parameters DataDisk.$.KMSKeyId.
- Update API CreateStorageSet: add request parameters ResourceGroupId.
- Update API DescribeLaunchTemplateVersions: add response parameters Body.LaunchTemplateVersionSets.$.LaunchTemplateData.SystemDisk.KMSKeyId.
- Update API DescribeLaunchTemplateVersions: add response parameters Body.LaunchTemplateVersionSets.$.LaunchTemplateData.DataDisks.$.KMSKeyId.


2025-05-23 Version: 7.0.6
- Update API DescribeInstanceTypes: add response parameters Body.InstanceTypes.$.Clock.


2025-05-21 Version: 7.0.5
- Update API CreateNetworkInterface: add request parameters EnhancedNetwork.VirtualFunctionQuantity.
- Update API CreateNetworkInterface: add request parameters EnhancedNetwork.VirtualFunctionTotalQueueNumber.
- Update API DescribeNetworkInterfaceAttribute: add response parameters Body.EnhancedNetwork.VirtualFunctionQuantity.
- Update API DescribeNetworkInterfaceAttribute: add response parameters Body.EnhancedNetwork.VirtualFunctionTotalQueueNumber.
- Update API ModifyNetworkInterfaceAttribute: add request parameters EnhancedNetwork.VirtualFunctionQuantity.
- Update API ModifyNetworkInterfaceAttribute: add request parameters EnhancedNetwork.VirtualFunctionTotalQueueNumber.


2025-05-16 Version: 7.0.4
- Update API DescribeSnapshotLinks: add request parameters MaxResults.
- Update API DescribeSnapshotLinks: add request parameters NextToken.
- Update API DescribeSnapshotLinks: add response parameters Body.NextToken.


2025-05-15 Version: 7.0.3
- Update API CreateStorageSet: add request parameters Tag.
- Update API DescribeStorageSets: add request parameters Tag.
- Update API DescribeStorageSets: add response parameters Body.StorageSets.$.ResourceGroupId.
- Update API DescribeStorageSets: add response parameters Body.StorageSets.$.Tags.
- Update API InvokeCommand: add request parameters WorkingDir.


2025-04-29 Version: 7.0.2
- Update API CopyImage: add request parameters ClientToken.
- Update API CopyImage: add request parameters DryRun.
- Update API CreateImage: add request parameters DryRun.
- Update API DeleteImage: add request parameters DryRun.
- Update API ExportImage: add request parameters DryRun.
- Update API ModifyImageAttribute: add request parameters DryRun.
- Update API ModifyImageSharePermission: add request parameters DryRun.


2025-04-21 Version: 7.0.1
- Update API CreatePrefixList: add request parameters ResourceGroupId.
- Update API CreatePrefixList: add request parameters Tag.
- Update API DescribePrefixLists: add request parameters ResourceGroupId.
- Update API DescribePrefixLists: add request parameters Tag.
- Update API DescribePrefixLists: add response parameters Body.PrefixLists.$.ResourceGroupId.
- Update API DescribePrefixLists: add response parameters Body.PrefixLists.$.Tags.


2025-04-16 Version: 7.0.0
- Support API CreatePortRangeList.
- Support API DeletePortRangeList.
- Support API DescribePortRangeListAssociations.
- Support API DescribePortRangeListEntries.
- Support API DescribePortRangeLists.
- Support API ModifyPortRangeList.
- Delete API CreateDemand.
- Delete API DeleteDemand.
- Delete API DescribeDemands.
- Delete API ModifyDemand.
- Update API AuthorizeSecurityGroup: add request parameters Permissions.$.PortRangeListId.
- Update API AuthorizeSecurityGroupEgress: add request parameters Permissions.$.PortRangeListId.
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.ImageOptions.
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.SpotDuration.
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.SpotInterruptionBehavior.
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.DataDisk.$.AutoSnapshotPolicyId.
- Update API CreateAutoProvisioningGroup: add request parameters LaunchConfiguration.SystemDisk.AutoSnapshotPolicyId.
- Update API DeleteInstance: add request parameters ForceStop.
- Update API DeleteInstances: add request parameters ForceStop.
- Update API DescribeInstanceAttribute: add response parameters Body.EnableNetworkEncryption.
- Update API DescribeInstanceTypes: add response parameters Body.InstanceTypes.$.Attributes.
- Update API DescribeInstances: add response parameters Body.Instances.$.EnableNVS.
- Update API DescribeInstances: add response parameters Body.Instances.$.CpuOptions.EnableVISST.
- Update API DescribeInstances: add response parameters Body.Instances.$.CpuOptions.EnableVRDT.
- Update API DescribeInstances: add response parameters Body.Instances.$.CpuOptions.TurboMode.
- Update API DescribeSecurityGroupAttribute: add response parameters Body.Permissions.$.PortRangeListId.
- Update API DescribeSecurityGroupAttribute: add response parameters Body.Permissions.$.PortRangeListName.
- Update API ModifyInstanceAttribute: add request parameters EnableNetworkEncryption.
- Update API ModifySecurityGroupEgressRule: add request parameters PortRangeListId.
- Update API ModifySecurityGroupRule: add request parameters PortRangeListId.
- Update API RevokeSecurityGroup: add request parameters Permissions.$.PortRangeListId.
- Update API RevokeSecurityGroupEgress: add request parameters Permissions.$.PortRangeListId.
- Update API RunInstances: add request parameters NetworkOptions.EnableNetworkEncryption.
- Update API StartTerminalSession: add request parameters ConnectionType.


2025-03-13 Version: 6.1.0
- Support API DescribeElasticityAssuranceAutoRenewAttribute.
- Support API ModifyElasticityAssuranceAutoRenewAttribute.
- Update API AllocateDedicatedHosts: update response param.
- Update API CreateElasticityAssurance: add param RecurrenceRules.
- Update API CreateImagePipeline: add param ImageOptions.
- Update API CreateImagePipeline: update param AdvancedOptions.
- Update API CreateImagePipeline: update param ImageFamily.
- Update API CreateImagePipeline: update param ImageName.
- Update API CreateImagePipeline: update param ImportImageOptions.
- Update API CreateImagePipeline: update param NvmeSupport.
- Update API CreateLaunchTemplate: update param NetworkInterface.
- Update API CreateLaunchTemplateVersion: update param NetworkInterface.
- Update API DescribeCommands: update response param.
- Update API DescribeElasticityAssurances: add param PackageType.
- Update API DescribeElasticityAssurances: update response param.
- Update API DescribeImagePipelines: update response param.
- Update API DescribeInstanceAttribute: update response param.
- Update API DescribeLaunchTemplateVersions: update response param.
- Update API DescribePrice: add param RecurrenceRules.
- Update API DescribePrice: add param StartTime.
- Update API ModifyElasticityAssurance: add param RecurrenceRules.
- Update API ModifyInstanceAttachmentAttributes: update response param.
- Update API PurchaseReservedInstancesOffering: update response param.
- Update API PurchaseStorageCapacityUnit: add param ResourceGroupId.
- Update API RenewDedicatedHosts: update response param.
- Update API RunInstances: update param SpotDuration.


2025-02-17 Version: 6.0.0
- Support API EndTerminalSession.
- Support API ModifySnapshotCategory.
- Delete API ModifyAutoSnapshotPolicy.
- Update API CreateAutoProvisioningGroup: add param LaunchConfiguration.
- Update API CreateAutoProvisioningGroup: add param PrePaidOptions.
- Update API CreateAutoProvisioningGroup: update param DefaultTargetCapacityType.
- Update API CreateElasticityAssurance: add param AutoRenew.
- Update API CreateElasticityAssurance: add param AutoRenewPeriod.
- Update API CreateImagePipeline: add param AdvancedOptions.
- Update API CreateImagePipeline: add param ImportImageOptions.
- Update API CreateImagePipeline: add param NvmeSupport.
- Update API CreateImagePipeline: update param BaseImage.
- Update API CreateKeyPair: update response param.
- Update API DescribeImagePipelines: update response param.
- Update API DescribeRenewalPrice: update response param.
- Update API RenewElasticityAssurances: add param AutoRenew.
- Update API RenewElasticityAssurances: add param AutoRenewPeriod.


2025-01-13 Version: 5.0.2
- Update API CreateImagePipeline: add param AdvancedOptions.
- Update API CreateImagePipeline: add param ImportImageOptions.
- Update API CreateImagePipeline: add param NvmeSupport.
- Update API CreateImagePipeline: update param BaseImage.
- Update API CreateKeyPair: update response param.
- Update API DescribeImagePipelines: update response param.


2025-01-09 Version: 5.0.1
- Update API CreateNetworkInterface: update param EnhancedNetwork.
- Update API DescribeInstanceTypes: update response param.
- Update API DescribeNetworkInterfaceAttribute: update response param.
- Update API DescribePrefixLists: add param PrefixListId.
- Update API DescribePrefixLists: update param PrefixListId.
- Update API ModifyDiskSpec: add param DestinationZoneId.
- Update API ModifyNetworkInterfaceAttribute: update param EnhancedNetwork.


2024-12-26 Version: 5.0.0
- Update API DescribeImages: update response param.
- Update API ModifyInstanceAttribute: add param CpuOptions.Core.
- Update API ModifyInstanceAttribute: add param CpuOptions.ThreadsPerCore.


2024-12-19 Version: 4.4.11
- Update API DescribeInstanceModificationPrice: update response param.
- Update API DescribePrice: update param DataDisk.
- Update API StartImagePipelineExecution: add param Tag.
- Update API StartImagePipelineExecution: update param TemplateTag.
- Update API StartImagePipelineExecution: update response param.


2024-12-16 Version: 4.4.10
- Update API CreateImage: add param Features.
- Update API DescribeImages: update response param.
- Update API DescribeInstances: update response param.
- Update API ImportImage: update param Features.
- Update API ModifyImageAttribute: update param Features.


2024-11-29 Version: 4.4.9
- Update API CreateAutoProvisioningGroup: update param LaunchTemplateConfig.
- Update API CreateSavingsPlan: add param InstanceTypeFamilyGroup.
- Update API DescribeSavingsPlanEstimation: add param EstimationResource.
- Update API DescribeSavingsPlanEstimation: add param InstanceTypeScope.
- Update API DescribeSavingsPlanEstimation: update response param.
- Update API DescribeSavingsPlanPrice: add param InstanceTypeFamilyGroup.


2024-11-25 Version: 4.4.8
- Update API DescribeInstanceTypes: update response param.
- Update API RedeployDedicatedHost: add param MigrationType.
- Update API RunInstances: update param NetworkInterface.
- Update API RunInstances: update param SecurityGroupId.
- Update API RunInstances: update param SecurityGroupIds.


2024-11-15 Version: 4.4.7
- Update API ImportImage: add param ClientToken.


2024-11-13 Version: 4.4.6
- Update API DescribeInstanceHistoryEvents: add param MaxResults.
- Update API DescribeInstanceHistoryEvents: add param NextToken.
- Update API DescribeInstanceHistoryEvents: update response param.


2024-11-05 Version: 4.4.5
- Update API CreateNetworkInterface: add param SourceDestCheck.
- Update API CreateNetworkInterface: update response param.
- Update API RunInstances: update param NetworkInterface.


2024-11-04 Version: 4.4.4
- Update API CreateAutoProvisioningGroup: add param ResourcePoolOptions.
- Update API CreateCommand: add param Launcher.
- Update API CreateLaunchTemplate: add param HttpEndpoint.
- Update API CreateLaunchTemplate: add param HttpPutResponseHopLimit.
- Update API CreateLaunchTemplate: add param HttpTokens.
- Update API CreateLaunchTemplateVersion: add param HttpEndpoint.
- Update API CreateLaunchTemplateVersion: add param HttpPutResponseHopLimit.
- Update API CreateLaunchTemplateVersion: add param HttpTokens.
- Update API DescribeCommands: update response param.
- Update API DescribeElasticityAssurances: update response param.
- Update API DescribeInstanceTypes: update param InstanceTypes.
- Update API DescribeInstanceTypes: update response param.
- Update API DescribeInstances: update response param.
- Update API DescribeLaunchTemplateVersions: update response param.
- Update API ModifyCommand: add param Launcher.
- Update API PurchaseElasticityAssurance: add param Action.
- Update API PurchaseElasticityAssurance: add param OwnerAccount.
- Update API PurchaseElasticityAssurance: add param OwnerId.
- Update API PurchaseElasticityAssurance: add param ResourceOwnerAccount.
- Update API PurchaseElasticityAssurance: add param ResourceOwnerId.
- Update API PurchaseElasticityAssurance: update param RegionId.


2024-10-12 Version: 4.4.3
- Update API CreateLaunchTemplate: add param HttpEndpoint.
- Update API CreateLaunchTemplate: add param HttpPutResponseHopLimit.
- Update API CreateLaunchTemplate: add param HttpTokens.
- Update API CreateLaunchTemplateVersion: add param HttpEndpoint.
- Update API CreateLaunchTemplateVersion: add param HttpPutResponseHopLimit.
- Update API CreateLaunchTemplateVersion: add param HttpTokens.
- Update API DescribeLaunchTemplateVersions: update response param.
- Update API PurchaseElasticityAssurance: add param Action.
- Update API PurchaseElasticityAssurance: add param OwnerAccount.
- Update API PurchaseElasticityAssurance: add param OwnerId.
- Update API PurchaseElasticityAssurance: add param ResourceOwnerAccount.
- Update API PurchaseElasticityAssurance: add param ResourceOwnerId.
- Update API PurchaseElasticityAssurance: update param RegionId.


2024-10-10 Version: 4.4.2
- Update API CreateImageComponent: add param ComponentVersion.
- Update API CreateImagePipeline: add param ImageFamily.
- Update API CreateImagePipeline: add param RepairMode.
- Update API CreateImagePipeline: add param TestContent.
- Update API CreateImagePipeline: update response param.
- Update API DescribeImageComponents: add param ComponentType.
- Update API DescribeImageComponents: add param ComponentVersion.
- Update API DescribeImageComponents: add param SystemType.
- Update API DescribeImageComponents: update response param.
- Update API DescribeImagePipelines: update response param.


2024-10-09 Version: 4.4.1
- Update API DescribeInstanceTypes: update param InstanceTypes.
- Update API ImportImage: add param DryRun.
- Update API ImportImage: add param Features.


2024-09-29 Version: 4.4.0
- Support API PurchaseElasticityAssurance.
- Update API DescribeNetworkInterfaceAttribute: update response param.
- Update API DescribeNetworkInterfaces: update response param.
- Update API DescribeSecurityGroups: update response param.
- Update API ModifyElasticityAssurance: add param ClientToken.
- Update API ModifyElasticityAssurance: add param InstanceAmount.
- Update API ModifyNetworkInterfaceAttribute: add param SourceDestCheck.


2024-09-07 Version: 4.3.0
- Support API DescribeDiskDefaultKMSKeyId.
- Support API DescribeDiskEncryptionByDefaultStatus.
- Support API DisableDiskEncryptionByDefault.
- Support API EnableDiskEncryptionByDefault.
- Support API ModifyDiskDefaultKMSKeyId.
- Support API ResetDiskDefaultKMSKeyId.


2024-08-23 Version: 4.2.0
- Support API RenewElasticityAssurances.
- Update API ResizeDisk: update response param.


2024-08-21 Version: 4.1.13
- Update API PurchaseReservedInstancesOffering: add param StartTime.


2024-08-12 Version: 4.1.12
- Update API DescribeInstanceHistoryEvents: update response param.
- Update API DescribeInstances: update response param.
- Update API DescribeNetworkInterfaces: update response param.
- Update API ModifyInstanceAttribute: add param PrivateDnsNameOptions.
- Update API RunInstances: add param PrivateDnsNameOptions.


2024-08-08 Version: 4.1.11
- Update API DescribeInstances: update response param.
- Update API DescribeNetworkInterfaces: update response param.
- Update API ModifyInstanceAttribute: add param PrivateDnsNameOptions.
- Update API RunInstances: add param PrivateDnsNameOptions.


2024-08-01 Version: 4.1.10
- Update API DescribeInvocationResults: update response param.
- Update API DescribeInvocations: update response param.
- Update API InvokeCommand: add param Launcher.
- Update API ModifyDiskSpec: update param ProvisionedIops.
- Update API RunCommand: add param Launcher.


2024-07-23 Version: 4.1.9
- Update API CopyImage: update param KMSKeyId.
- Update API CopySnapshot: add param ClientToken.
- Update API CopySnapshot: update param KMSKeyId.
- Update API CreateDisk: update param KMSKeyId.
- Update API CreateInstance: update param DataDisk.
- Update API CreateLaunchTemplate: add param AutoRenew.
- Update API CreateLaunchTemplate: add param AutoRenewPeriod.
- Update API CreateLaunchTemplate: add param PeriodUnit.
- Update API CreateLaunchTemplateVersion: add param AutoRenew.
- Update API CreateLaunchTemplateVersion: add param AutoRenewPeriod.
- Update API CreateLaunchTemplateVersion: add param PeriodUnit.
- Update API CreateNetworkInterface: add param EnhancedNetwork.
- Update API CreateNetworkInterface: update param SecurityGroupIds.
- Update API CreateSnapshotGroup: add param ClientToken.
- Update API DescribeInstanceTypes: update response param.
- Update API DescribeLaunchTemplateVersions: update response param.
- Update API DescribeNetworkInterfaceAttribute: update response param.
- Update API DescribePrice: update response param.
- Update API DescribeSnapshots: update response param.
- Update API ModifyInstanceAttribute: update param SecurityGroupIds.
- Update API ModifyInstanceVpcAttribute: update param SecurityGroupId.
- Update API ModifyNetworkInterfaceAttribute: add param EnhancedNetwork.
- Update API ModifyNetworkInterfaceAttribute: update param SecurityGroupId.
- Update API ReplaceSystemDisk: update param KMSKeyId.
- Update API RunInstances: update param DataDisk.
- Update API RunInstances: update param NetworkInterface.
- Update API RunInstances: update param SecurityGroupIds.
- Update API RunInstances: update param SystemDisk.


2024-05-22 Version: 4.1.8
- Update API DescribeSnapshots: update response param.


2024-05-21 Version: 4.1.7
- Update API DescribeSecurityGroupAttribute: add param MaxResults.
- Update API DescribeSecurityGroupAttribute: add param NextToken.
- Update API DescribeSecurityGroupAttribute: update response param.


2024-05-21 Version: 4.1.7
- Update API DescribeSecurityGroupAttribute: add param MaxResults.
- Update API DescribeSecurityGroupAttribute: add param NextToken.
- Update API DescribeSecurityGroupAttribute: update response param.


2024-05-17 Version: 4.1.6
- Update API CreateImage: update response param.
- Update API CreateNetworkInterface: add param NetworkInterfaceTrafficConfig.
- Update API DescribeInvocationResults: update response param.
- Update API DescribeInvocations: update response param.
- Update API DescribeNetworkInterfaceAttribute: update response param.
- Update API DetachDisk: update response param.
- Update API InvokeCommand: add param TerminationMode.
- Update API ModifyNetworkInterfaceAttribute: add param NetworkInterfaceTrafficConfig.
- Update API RunCommand: add param TerminationMode.


2024-05-15 Version: 4.1.5
- Update API CreateImage: update response param.
- Update API DescribeInvocationResults: update response param.
- Update API DescribeInvocations: update response param.
- Update API DetachDisk: update response param.
- Update API InvokeCommand: add param TerminationMode.
- Update API RunCommand: add param TerminationMode.


2024-05-08 Version: 4.1.4
- Update API AttachDisk: add param Force.
- Update API AttachDisk: update response param.
- Update API AttachNetworkInterface: update response param.
- Update API DescribeDisks: update response param.
- Update API ReplaceSystemDisk: update response param.


2024-05-07 Version: 4.1.3
- Update API CreateAutoProvisioningGroup: update param LaunchConfiguration.DataDisk.
- Update API CreateAutoProvisioningGroup: update param LaunchConfiguration.SystemDisk.
- Update API CreateNetworkInterface: add param ConnectionTrackingConfiguration.
- Update API DescribeNetworkInterfaceAttribute: update response param.
- Update API ModifyNetworkInterfaceAttribute: add param ConnectionTrackingConfiguration.


2024-04-24 Version: 4.1.2
- Update API DescribeInstanceTypes: update response param.


2024-04-12 Version: 4.1.1
- Update API DescribeDedicatedHosts: add param MaxResults.
- Update API DescribeDedicatedHosts: add param NextToken.
- Update API DescribeDedicatedHosts: update response param.
- Update API DescribeInstanceTypes: add param CpuArchitectures.
- Update API DescribeInstanceTypes: add param GpuSpecs.
- Update API DescribeInstanceTypes: add param InstanceCategories.
- Update API DescribeInstanceTypes: add param InstanceTypeFamilies.
- Update API DescribeInstanceTypes: add param LocalStorageCategories.
- Update API DescribeInstanceTypes: add param PhysicalProcessorModels.
- Update API DescribeInstanceTypes: update param InstanceCategory.
- Update API DescribeInstanceTypes: update response param.
- Update API InvokeCommand: update param InstanceId.
- Update API RunCommand: update param InstanceId.


2024-04-10 Version: 4.1.0
- Support API DescribeCloudAssistantSettings.
- Support API DescribeTerminalSessions.
- Support API ModifyCloudAssistantSettings.


2024-04-10 Version: 4.0.4
- Update API DescribeAvailableResource: update param SpotDuration.
- Update API ImportImage: add param StorageLocationArn.
- Update API ImportImage: update response param.


2024-03-12 Version: 4.0.3
- Update API CreateAutoProvisioningGroup: add param Tag.
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoProvisioningGroups: add param Tag.
- Update API DescribeAutoProvisioningGroups: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.
- Update API StartTerminalSession: add param Username.


2024-03-12 Version: 4.0.3
- Update API CreateAutoProvisioningGroup: add param Tag.
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoProvisioningGroups: add param Tag.
- Update API DescribeAutoProvisioningGroups: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.
- Update API StartTerminalSession: add param Username.


2024-02-29 Version: 4.0.2
- Update API CreateAutoProvisioningGroup: add param Tag.
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoProvisioningGroups: add param Tag.
- Update API DescribeAutoProvisioningGroups: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.


2024-02-28 Version: 4.0.1
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.


2024-02-02 Version: 4.0.0
- Support API CreateSavingsPlan.
- Support API DescribeSavingsPlanEstimation.
- Support API DescribeSavingsPlanPrice.
- Support API ModifyInvocationAttribute.
- Delete API DescribeInstanceVncPasswd.
- Delete API ImportSnapshot.
- Update API AuthorizeSecurityGroupupdate Description param.
update DestCidrIp param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourceGroupId param.
update SourceGroupOwnerAccount param.
update SourceGroupOwnerId param.
update SourcePortRange param.
update SourcePrefixListId param.
- Update API AuthorizeSecurityGroupEgressupdate Description param.
update DestCidrIp param.
update DestGroupId param.
update DestGroupOwnerAccount param.
update DestGroupOwnerId param.
update DestPrefixListId param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourcePortRange param.
- Update API CreateAutoProvisioningGroupadd LaunchConfiguration.ImageFamily param.
- Update API CreateNetworkInterfaceadd RxQueueSize param.
add TxQueueSize param.
- Update API DeleteAutoProvisioningGroupupdate TerminateInstances param.
- Update API DeleteInstanceadd DryRun param.
- Update API DeleteLaunchTemplateupdate response param.
- Update API DeregisterManagedInstanceupdate response param.
- Update API DescribeActivationsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeAutoProvisioningGroupsadd ResourceGroupId param.
update response param.
- Update API DescribeAutoSnapshotPolicyExupdate response param.
- Update API DescribeBandwidthLimitationupdate RegionId param.
- Update API DescribeCapacityReservationsupdate response param.
- Update API DescribeCloudAssistantStatusadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeCommandsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeDisksupdate response param.
- Update API DescribeInstanceTypesupdate response param.
- Update API DescribeInstancesupdate response param.
- Update API DescribeInvocationResultsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeInvocationsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeKeyPairsadd IncludePublicKey param.
update response param.
- Update API DescribeManagedInstancesadd MaxResults param.
add NextToken param.
add ResourceGroupId param.
update response param.
- Update API DescribeNetworkInterfaceAttributeupdate response param.
- Update API DescribeNetworkInterfacesupdate PageNumber param.
update PageSize param.
- Update API DescribeSecurityGroupsadd ServiceManaged param.
- Update API DescribeSendFileResultsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeSnapshotsupdate response param.
- Update API InvokeCommandadd ResourceTag param.
update InstanceId param.
- Update API JoinResourceGroupupdate response param.
- Update API ListPluginStatusadd MaxResults param.
add NextToken param.
update response param.
- Update API ModifyInstanceAttributeadd CpuOptions.TopologyType param.
- Update API ModifyInstanceSpecadd DryRun param.
- Update API ModifyNetworkInterfaceAttributeadd RxQueueSize param.
add TxQueueSize param.
- Update API RevokeSecurityGroupupdate Description param.
update DestCidrIp param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourceGroupId param.
update SourceGroupOwnerAccount param.
update SourceGroupOwnerId param.
update SourcePortRange param.
update SourcePrefixListId param.
- Update API RevokeSecurityGroupEgressupdate Description param.
update DestCidrIp param.
update DestGroupId param.
update DestGroupOwnerAccount param.
update DestGroupOwnerId param.
update DestPrefixListId param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourcePortRange param.
- Update API RunCommandadd ResourceTag param.
update InstanceId param.
- Update API RunInstancesadd CpuOptions.TopologyType param.
update NetworkInterface param.


2023-10-24 Version: 3.0.15
- Generated python 2014-05-26 for Ecs.

2023-10-18 Version: 3.0.14
- Generated python 2014-05-26 for Ecs.

2023-10-16 Version: 3.0.13
- Generated python 2014-05-26 for Ecs.

2023-10-09 Version: 3.0.12
- Generated python 2014-05-26 for Ecs.

2023-09-19 Version: 3.0.11
- Generated python 2014-05-26 for Ecs.

2023-09-18 Version: 3.0.10
- Generated python 2014-05-26 for Ecs.

2023-08-09 Version: 3.0.9
- Generated python 2014-05-26 for Ecs.

2023-05-25 Version: 3.0.8
- DescribeDemands add PrivatePoolId.

2023-04-17 Version: 3.0.7
- Add ModifyDiskDeployment.

2023-03-28 Version: 3.0.6
- Change visibility of param ActionType in DescribeImageSupportInstanceTypes.

2023-03-27 Version: 3.0.5
- Suppoort jumbo frame.

2023-02-13 Version: 3.0.4
- Support TagPolicy Verify NoTag.
- Fixed bugs for DescribeDemands error code.
- Add encrypted disk ErrorCode.
- DescribeDedicatedHosts supports SocketDetails param to check socket capacities of specified dedicated hosts.

2023-02-06 Version: 3.0.3
- Add OpenAPI DescribeReservedInstanceAutoRenewAttribute, ModifyReservedInstanceAutoRenewAttribute.

2023-01-11 Version: 3.0.2
- Add error code for ModifyInstanceNetworkSpec.
- Add invalid account buying spot error code.
- Support ip prefix for eni.
- Update the StorageLocationArn to private.
- Security Group Rule support rule id.

2022-10-14 Version: 3.0.1
- Add GPUMemorySize to DescribeInstanceTypes api.

2022-09-27 Version: 3.0.0
- Modify Size type form int32 to int64 of `DescribePriceRequest` `DataDisk` param.

2022-07-15 Version: 2.1.3
- Support Security Group Batch Manager Rules.

2022-07-11 Version: 2.1.2
- Support Storage And Network Features For LaunchTemplate.

2022-04-27 Version: 2.1.1
- Support systemdisk encrypt and arns.

2022-04-13 Version: 4.24.17
- Support throughput for API DescribeDisks.


2021-08-27 Version: 2.1.0
- DescribeSecurityGroups support query by next token.

2021-03-22 Version: 2.0.2
- Generated python 2014-05-26 for Ecs.

2020-12-29 Version: 2.0.1
- AMP Version Change.

2020-12-28 Version: 2.0.0
- AMP Version Change.

2020-11-30 Version: 1.2.0
- Support network interface join or leave security group.

2020-11-16 Version: 1.1.0
- Nat public IP supports the ISP attribute.

2020-10-27 Version: 1.0.2
- Generated python 2014-05-26 for Ecs.

2020-09-02 Version: 1.0.1
- Generated python 2014-05-26 for Ecs.

