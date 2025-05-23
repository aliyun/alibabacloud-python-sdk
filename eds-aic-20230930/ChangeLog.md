2025-05-23 Version: 4.7.1
- Update API DescribeAndroidInstances: add request parameters AppManagePolicyId.
- Update API DescribeAndroidInstances: add response parameters Body.InstanceModel.$.AppManagePolicy.


2025-05-14 Version: 4.7.0
- Support API DescribeDisplayConfig.
- Support API ModifyDisplayConfig.
- Update API DescribeAndroidInstances: add request parameters QosRuleIds.
- Update API DescribeAndroidInstances: add response parameters Body.InstanceModel.$.QosRuleId.


2025-04-27 Version: 4.6.1
- Generated python 2023-09-30 for eds-aic.

2025-04-25 Version: 4.6.0
- Support API UpdateInstanceImage.
- Update API CreatePolicyGroup: add request parameters Watermark.
- Update API ListPolicyGroups: add response parameters Body.PolicyGroupModel.$.Watermark.
- Update API ModifyPolicyGroup: add request parameters Watermark.
- Update API RenewCloudPhoneNodes: add request parameters AutoPay.


2025-04-17 Version: 4.5.4
- Update API DescribeAndroidInstances: add request parameters AuthorizedUserId.
- Update API ListPolicyGroups: add response parameters Body.PolicyGroupModel.$.PolicyRelatedResources.


2025-04-17 Version: 4.5.4
- Update API DescribeAndroidInstances: add request parameters AuthorizedUserId.
- Update API ListPolicyGroups: add response parameters Body.PolicyGroupModel.$.PolicyRelatedResources.


2025-04-16 Version: 4.5.3
- Update API ModifyPolicyGroup: add request parameters NetRedirectPolicy.Rules.


2025-04-11 Version: 4.5.2
- Update API CreateApp: add request parameters SignApk.
- Update API DescribeApps: add request parameters AppType.
- Update API DescribeApps: add response parameters Body.Data.$.AppType.


2025-04-10 Version: 4.5.1
- Update API DescribeAndroidInstances: add request parameters OfficeSiteIds.


2025-04-09 Version: 4.5.0
- Support API ChangeCloudPhoneNode.
- Support API ExpandDataVolume.


2025-04-07 Version: 4.4.2
- Update API RebootAndroidInstancesInGroup: add request parameters SaleMode.
- Update API ResetAndroidInstancesInGroup: add request parameters SaleMode.
- Update API StartAndroidInstance: add request parameters SaleMode.
- Update API StopAndroidInstance: add request parameters SaleMode.


2025-04-03 Version: 4.4.1
- Update API CreateCloudPhoneNode: add request parameters DisplayConfig.
- Update API CreatePolicyGroup: add request parameters PolicyType.
- Update API DescribeAndroidInstances: add response parameters Body.InstanceModel.$.DisplayConfig.
- Update API DescribeCloudPhoneNodes: add response parameters Body.NodeModel.$.InstanceType.
- Update API ListPolicyGroups: add request parameters PolicyType.


2025-03-31 Version: 4.4.0
- Support API CreateCloudPhoneNode.
- Support API DeleteCloudPhoneNodes.
- Support API DescribeCloudPhoneNodes.
- Support API ModifyCloudPhoneNode.
- Support API RenewCloudPhoneNodes.


2025-03-14 Version: 4.3.2
- Update API DescribeAndroidInstanceGroups: update response param.
- Update API DescribeAndroidInstances: update response param.
- Update API DescribeImageList: update response param.
- Update API DescribeSpec: update response param.
- Update API SendFile: add param TargetFileName.


2025-03-13 Version: 4.3.1
- Generated python 2023-09-30 for eds-aic.

2025-03-13 Version: 4.3.0
- Support API ModifyInstanceChargeType.


2025-02-26 Version: 4.2.0
- Support API DisconnectAndroidInstance.
- Support API EndCoordination.
- Support API GenerateCoordinationCode.


2025-02-21 Version: 4.1.0
- Support API SetAdbSecure.
- Update API CreateAndroidInstanceGroup: add param EnableIpv6.
- Update API CreateAndroidInstanceGroup: add param Ipv6Bandwidth.
- Update API CreateAndroidInstanceGroup: add param Tag.
- Update API CreateApp: add param CustomAppInfo.
- Update API DescribeAndroidInstances: update response param.
- Update API SendFile: update param UploadEndpoint.


2025-01-07 Version: 3.2.2
- Generated python 2023-09-30 for eds-aic.

2025-01-07 Version: 3.2.1
- Generated python 2023-09-30 for eds-aic.

2025-01-03 Version: 3.2.0
- Support API OperateApp.
- Update API BackupFile: add param BackupAll.
- Update API DescribeAndroidInstances: update response param.
- Update API DescribeBackupFiles: add param BackupAll.
- Update API DescribeBackupFiles: update response param.
- Update API DescribeTasks: update response param.
- Update API RecoveryFile: add param BackupAll.


2024-12-25 Version: 3.1.0
- Support API BatchGetAcpConnectionTicket.


2024-12-20 Version: 3.0.5
- Update API DescribeAndroidInstances: add param BizRegionId.
- Update API DescribeAndroidInstances: add param Tag.
- Update API DescribeAndroidInstances: update response param.


2024-12-17 Version: 3.0.4
- Update API BackupFile: update response param.
- Update API DescribeApps: add param MD5.
- Update API DescribeApps: update response param.
- Update API DescribeTasks: add param InstanceId.
- Update API DescribeTasks: add param InstanceName.
- Update API DescribeTasks: add param Level.
- Update API DescribeTasks: add param Param.
- Update API DescribeTasks: add param ParentTaskId.
- Update API DescribeTasks: add param TaskStatuses.
- Update API DescribeTasks: add param TaskTypes.
- Update API DescribeTasks: update response param.
- Update API FetchFile: update response param.
- Update API InstallApp: update response param.
- Update API RecoveryFile: update response param.
- Update API SendFile: update response param.
- Update API UninstallApp: add param InstanceIdList.
- Update API UninstallApp: update param InstanceGroupIdList.
- Update API UninstallApp: update response param.


2024-12-06 Version: 3.0.3
- Generated python 2023-09-30 for eds-aic.

2024-12-06 Version: 3.0.2
- Update API BackupFile: add param BackupFileName.
- Update API DescribeAndroidInstanceGroups: update response param.


2024-11-22 Version: 3.0.1
- Update API CheckResourceStock: update param AcpSpecId.


2024-11-21 Version: 3.0.0
- Delete API GetAdbSecure.
- Delete API SetAdbSecure.
- Update API BackupFile: add param SourceAppList.
- Update API BackupFile: update param SourceFilePathList.
- Update API CreateApp: update param AppName.
- Update API CreatePolicyGroup: update param NetRedirectPolicy.
- Update API DescribeBackupFiles: add param StatusList.
- Update API DescribeBackupFiles: update response param.
- Update API DescribeRegions: add param AcceptLanguage.
- Update API DescribeRegions: update response param.
- Update API DescribeTasks: update response param.
- Update API ListPolicyGroups: update response param.
- Update API ModifyPolicyGroup: update param NetRedirectPolicy.


2024-11-04 Version: 2.0.2
- Update API RunCommand: add param ContentEncoding.


2024-10-24 Version: 2.0.1
- Update API CreateAndroidInstanceGroup: add param KeyPairId.


2024-10-17 Version: 2.0.0
- Update API BackupFile: update response param.
- Update API CheckResourceStock: add param Amount.
- Update API CreatePolicyGroup: add param LockResolution.
- Update API DescribeAndroidInstances: add param ChargeType.
- Update API DescribeAndroidInstances: add param InstanceGroupName.
- Update API DescribeAndroidInstances: update response param.
- Update API DescribeApps: update response param.
- Update API DescribeSpec: add param BizRegionId.
- Update API FetchFile: update response param.
- Update API ListPolicyGroups: update response param.
- Update API ModifyPolicyGroup: add param LockResolution.
- Update API RecoveryFile: update response param.
- Update API RunCommand: update param InstanceIds.
- Update API SendFile: update response param.


2024-08-22 Version: 1.3.5
- Update API CreateAndroidInstanceGroup: add param ClientToken.
- Update API CreateAndroidInstanceGroup: update param Amount.
- Update API CreateAndroidInstanceGroup: update response param.
- Update API CreateCustomImage: add param ClientToken.
- Update API CreateCustomImage: update response param.
- Update API CreatePolicyGroup: add param NetRedirectPolicy.
- Update API DescribeAndroidInstances: add param InstanceGroupIds.
- Update API DescribeTasks: update response param.
- Update API InstallApp: add param InstanceIdList.
- Update API InstallApp: update param InstanceGroupIdList.
- Update API ListPolicyGroups: update response param.
- Update API ModifyPolicyGroup: add param NetRedirectPolicy.


2024-08-19 Version: 1.3.4
- Update API CreateAndroidInstanceGroup: add param ClientToken.
- Update API CreateAndroidInstanceGroup: update param Amount.
- Update API CreateAndroidInstanceGroup: update response param.
- Update API CreateCustomImage: add param ClientToken.
- Update API CreateCustomImage: update response param.
- Update API CreatePolicyGroup: add param NetRedirectPolicy.
- Update API DescribeAndroidInstances: add param InstanceGroupIds.
- Update API InstallApp: add param InstanceIdList.
- Update API InstallApp: update param InstanceGroupIdList.
- Update API ListPolicyGroups: update response param.
- Update API ModifyPolicyGroup: add param NetRedirectPolicy.


2024-08-12 Version: 1.3.3
- Update API RecoveryFile: update param BackupFileId.
- Update API RecoveryFile: update param BackupFilePath.


2024-07-29 Version: 1.3.2
- Update API CheckResourceStock: add param GpuAcceleration.


2024-07-24 Version: 1.3.1
- Update API CreateAndroidInstanceGroup: add param GpuAcceleration.
- Update API DescribeAndroidInstanceGroups: update response param.
- Update API DescribeAndroidInstances: update response param.
- Update API DescribeImageList: update response param.
- Update API UpgradeAndroidInstanceGroup: update response param.


2024-07-03 Version: 1.3.0
- Support API DescribeTasks.
- Update API CreateAndroidInstanceGroup: add param Amount.
- Update API DescribeAndroidInstanceGroups: update response param.
- Update API RebootAndroidInstancesInGroup: add param ForceStop.
- Update API StopAndroidInstance: add param ForceStop.


2024-07-02 Version: 1.2.3
- Update API CreateAndroidInstanceGroup: add param Amount.
- Update API DescribeAndroidInstanceGroups: update response param.
- Update API RebootAndroidInstancesInGroup: add param ForceStop.
- Update API StopAndroidInstance: add param ForceStop.


2024-06-27 Version: 1.2.2
- Update API CreateApp: add param BizRegionId.
- Update API DescribeApps: add param BizRegionId.
- Update API DescribeApps: update response param.


2024-06-26 Version: 1.2.1
- Update API CreateApp: add param BizRegionId.
- Update API DescribeApps: add param BizRegionId.
- Update API DescribeApps: update response param.


2024-06-13 Version: 1.2.0
- Support API DescribeImageList.
- Support API RebootAndroidInstancesInGroup.
- Support API StopAndroidInstance.


2024-06-12 Version: 1.1.0
- Support API CreateAndroidInstanceGroup.
- Support API CreateApp.
- Support API DescribeApps.


2024-06-11 Version: 1.0.0
- Generated python 2023-09-30 for eds-aic.

