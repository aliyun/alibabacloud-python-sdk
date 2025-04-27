2025-04-27 Version: 11.3.0
- Support API AcceptRCInquiredSystemEvent.
- Support API DescribeRCInstanceDdosCount.
- Support API DescribeRCInstanceHistoryEvents.
- Support API DescribeRCInstanceIpAddress.


2025-04-17 Version: 11.2.0
- Support API SwitchOverMajorVersionUpgrade.
- Update API DescribeUpgradeMajorVersionPrecheckTask: add response parameters Body.Items.$.UpgradeMode.
- Update API DescribeUpgradeMajorVersionTasks: add response parameters Body.Items.$.cutOver.
- Update API DescribeUpgradeMajorVersionTasks: add response parameters Body.Items.$.totalLogicRepDelayTime.
- Update API DescribeUpgradeMajorVersionTasks: add response parameters Body.Items.$.totalLogicRepLatencyMB.
- Update API DescribeUpgradeMajorVersionTasks: add response parameters Body.Items.$.zeroDownTimeConnectionString.
- Update API DescribeUpgradeMajorVersionTasks: add response parameters Body.Items.$.zeroDownTimePort.
- Update API ModifyRCInstance: add request parameters RebootTime.
- Update API ModifyRCInstance: add request parameters RebootWhenFinished.
- Update API UpgradeDBInstanceMajorVersionPrecheck: add request parameters UpgradeMode.


2025-04-10 Version: 11.1.1
- Update API DescribeDBProxyPerformance: add response parameters Body.PerformanceKeys.$.Node.


2025-04-09 Version: 11.1.0
- Support API DescribeRCInstanceTypeFamilies.
- Support API DescribeRCInstanceTypes.
- Support API ModifyRCDiskSpec.
- Update API DescribeDBInstanceAttribute: add response parameters Body.Items.$.ReadOnlyStatus.
- Update API DescribeRCInstanceAttribute: add response parameters Body.AutoRenew.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.Cpu.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.DeploymentSetId.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.ExpiredTime.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.ImageId.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.Memory.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.VpcAttributes.


2025-03-26 Version: 11.0.0
- Support API DescribeRCSecurityGroupList.
- Support API MigrateDBNodes.
- Support API RebootRCInstances.
- Support API StartRCInstances.
- Support API StopRCInstances.
- Support API SwitchReplicationLink.
- Update API AuthorizeRCSecurityGroupPermission: update request parameters SecurityGroupPermissions.$.Priority' type has changed.
- Update API AuthorizeRCSecurityGroupPermission: update request parameters SecurityGroupPermissions.$.Priority' format has changed.
- Update API CreateDdrInstance: add request parameters BackupSetRegion.
- Update API CreateRCDisk: add request parameters InstanceId.
- Update API CreateReplicationLink: add request parameters TargetAddress.
- Update API DescribeRCImageList: add response parameters Body.Images.$.DiskDeviceMappings.
- Update API DescribeRCInstanceAttribute: add response parameters Body.CreateMode.
- Update API DescribeRCInstances: add request parameters HostIp.
- Update API DescribeRCInstances: add request parameters InstanceIds.
- Update API DescribeRCInstances: add request parameters PublicIp.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.InstanceType.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.InstanceTypeFamily.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.PublicIp.
- Update API DescribeRCInstances: add response parameters Body.RCInstances.$.SecurityGroupId.
- Update API DescribeRCMetricList: add request parameters Dimensions.
- Update API DescribeRCSecurityGroupPermission: add response parameters Body.SecurityGroupPermissions.$.CreateTime.
- Update API MigrateToOtherZone: add request parameters DBInstanceStorageType.
- Update API ModifyRCInstanceChargeType: add request parameters AutoRenew.
- Update API ModifyRCInstanceChargeType: add request parameters AutoUseCoupon.
- Update API ModifyRCInstanceChargeType: add request parameters BusinessInfo.
- Update API ModifyRCInstanceChargeType: add request parameters ClientToken.
- Update API ModifyRCInstanceChargeType: add request parameters InstanceId.
- Update API ModifyRCInstanceChargeType: add request parameters PayType.
- Update API ModifyRCInstanceChargeType: add request parameters Period.
- Update API ModifyRCInstanceChargeType: add request parameters PromotionCode.
- Update API ModifyRCInstanceChargeType: add request parameters UsedTime.
- Update API ModifyRCInstanceChargeType: add response parameters Body.ChargeType.
- Update API ModifyRCInstanceChargeType: add response parameters Body.ExpiredTime.
- Update API ModifyRCInstanceChargeType: add response parameters Body.InstanceIds.
- Update API RunRCInstances: add request parameters UserDataInBase64.
- Update API RunRCInstances: add request parameters DataDisk.$.Device.
- Update API RunRCInstances: add request parameters DataDisk.$.SnapshotId.


2025-02-28 Version: 10.1.0
- Support API AuthorizeRCSecurityGroupPermission.
- Support API DescribeDBInstanceReplication.
- Support API DescribeRCSecurityGroupPermission.
- Support API ModifyRCInstanceNetworkSpec.
- Support API ModifyRCSecurityGroupPermission.
- Support API RenewRCInstance.
- Support API RevokeRCSecurityGroupPermission.
- Update API CreateDdrInstance: update param DBInstanceClass.
- Update API CreateDdrInstance: update param DBInstanceStorage.
- Update API CreateMaskingRules: add param DBName.
- Update API CreateRCDisk: update param DiskCategory.
- Update API CreateRCDisk: update param Size.
- Update API CreateRCDisk: update param ZoneId.
- Update API CreateRCNodePool: add param UserData.
- Update API DeleteMaskingRules: add param DBName.
- Update API DescribeAccountMaskingPrivilege: add param DBName.
- Update API DescribeDBProxyEndpoint: update response param.
- Update API DescribeMaskingRules: add param DBName.
- Update API ModifyAccountMaskingPrivilege: add param DBName.
- Update API ModifyDBProxyEndpoint: add param CausalConsistReadTimeout.
- Update API ModifyDBProxyEndpoint: add param VpcId.
- Update API ModifyDBProxyInstance: update param MigrateAZ.
- Update API ModifyMaskingRules: add param DBName.
- Update API ModifyRCInstanceAttribute: add param SecurityGroupId.
- Update API RunRCInstances: add param UserData.


2025-01-14 Version: 10.0.1
- Update API CheckServiceLinkedRole: update response param.
- Update API CreateRCNodePool: update param SystemDisk.
- Update API DescribeRCImageList: add param InstanceType.
- Update API DescribeRCImageList: update response param.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API DescribeRCNodePool: update response param.
- Update API DescribeResourceUsage: update response param.


2025-01-07 Version: 10.0.0
- Support API CreateRCNodePool.
- Support API DeleteRCNodePool.
- Support API DescribeRCNodePool.
- Support API ModifyDBInstanceReplicationSwitch.
- Delete API DescribeDiagnosticReportList.
- Update API DescribeRCClusters: add param Profile.
- Update API DescribeRCClusters: update response param.
- Update API DescribeRCDeploymentSets: update param PageNumber.
- Update API DescribeRCDeploymentSets: update param PageSize.
- Update API RunRCInstances: add param CreateAckEdgeParam.
- Update API RunRCInstances: add param CreateExtraParam.
- Update API RunRCInstances: add param SupportCase.


2024-12-24 Version: 9.1.0
- Support API AssociateEipAddressWithRCInstance.
- Support API SyncRCSecurityGroup.
- Support API UnassociateEipAddressWithRCInstance.
- Update API CreateDBInstance: add param OptimizedWrites.
- Update API DescribeDBInstanceAttribute: update response param.
- Update API DescribeRCDeploymentSets: update response param.
- Update API DescribeRCInstanceAttribute: add param PrivateIpAddress.
- Update API DescribeRCInstanceAttribute: update param InstanceId.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API DescribeRCInstances: update response param.
- Update API ModifyDBInstanceConfig: add param SwitchTime.
- Update API ModifyDBInstanceConfig: add param SwitchTimeMode.
- Update API ModifyDBInstanceSpec: add param CompressionMode.
- Update API ModifyDBInstanceSpec: add param OptimizedWrites.
- Update API ModifyResourceGroup: add param ResourceType.
- Update API RunRCInstances: update param SystemDisk.


2024-12-18 Version: 9.0.0
- Support API AssociateEipAddressWithRCInstance.
- Support API SyncRCSecurityGroup.
- Support API UnassociateEipAddressWithRCInstance.
- Update API CreateDBInstance: add param OptimizedWrites.
- Update API DescribeDBInstanceAttribute: update response param.
- Update API DescribeRCDeploymentSets: update response param.
- Update API DescribeRCInstanceAttribute: add param PrivateIpAddress.
- Update API DescribeRCInstanceAttribute: update param InstanceId.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API DescribeRCInstances: update response param.
- Update API ModifyDBInstanceConfig: add param SwitchTime.
- Update API ModifyDBInstanceConfig: add param SwitchTimeMode.
- Update API ModifyDBInstanceSpec: add param OptimizedWrites.
- Update API ModifyResourceGroup: add param ResourceType.


2024-12-02 Version: 8.0.1
- Update API CreateRCDisk: update param InstanceChargeType.
- Update API DescribeDBProxyEndpoint: update response param.
- Update API DescribeRCClusters: add param VpcId.
- Update API DescribeRCClusters: update response param.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API DescribeRCInstances: update response param.
- Update API ModifyDBProxyEndpoint: add param DbEndpointMinSlaveCount.
- Update API RunRCInstances: add param SpotStrategy.


2024-11-25 Version: 8.0.0
- Support API AttachRCDisk.
- Support API AttachRCInstances.
- Support API CreateRCDisk.
- Support API CreateRCSnapshot.
- Support API DeleteRCClusterNodes.
- Support API DeleteRCDisk.
- Support API DeleteRCSnapshot.
- Support API DescribeRCClusterConfig.
- Support API DescribeRCClusterNodes.
- Support API DescribeRCClusters.
- Support API DescribeRCDisks.
- Support API DescribeRCInstanceVncUrl.
- Support API DescribeRCSnapshots.
- Support API DetachRCDisk.
- Support API ModifyRCInstanceAttribute.
- Support API ModifyRCInstanceDescription.
- Support API ModifyRCInstanceKeyPair.
- Support API ReplaceRCInstanceSystemDisk.
- Delete API CreateDiagnosticReport.
- Update API CheckAccountNameAvailable: update response param.
- Update API CreateDBInstance: add param AutoUseCoupon.
- Update API CreateDBInstance: add param PromotionCode.
- Update API CreateRCDeploymentSet: add param Tag.
- Update API CreateReadOnlyDBInstance: add param AutoUseCoupon.
- Update API CreateReadOnlyDBInstance: add param PromotionCode.
- Update API CreateReadOnlyDBInstance: update param Category.
- Update API DescribeAccounts: update response param.
- Update API DescribeDBInstanceTDE: update response param.
- Update API DescribeDBProxyPerformance: add param Dimension.
- Update API DescribeDBProxyPerformance: update response param.
- Update API DescribeRCDeploymentSets: add param Tag.
- Update API DescribeRCDeploymentSets: update response param.
- Update API DescribeRCImageList: add param ImageId.
- Update API DescribeRCImageList: add param ImageName.
- Update API DescribeRCImageList: update response param.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API DescribeRCInstances: update response param.
- Update API DescribeUpgradeMajorVersionPrecheckTask: update response param.
- Update API DescribeUpgradeMajorVersionTasks: update response param.
- Update API ImportUserBackupFile: add param DBInstanceId.
- Update API ModifyDBInstanceSpec: add param PromotionCode.
- Update API RenewInstance: add param AutoUseCoupon.
- Update API RenewInstance: add param PromotionCode.
- Update API ResizeRCInstanceDisk: add param DiskId.
- Update API RunRCInstances: update param Amount.
- Update API RunRCInstances: update param SystemDisk.
- Update API TransformDBInstancePayType: add param AutoUseCoupon.
- Update API TransformDBInstancePayType: add param PromotionCode.


2024-10-24 Version: 7.3.1
- Update API DescribeRCImageList: update param Type.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API DescribeRCInstances: add param AccessKeyId.
- Update API DescribeRCInstances: add param Tag.
- Update API DescribeRCInstances: update response param.
- Update API ModifyDBInstanceSpec: add param ReadOnlyDBInstanceClass.
- Update API RunRCInstances: add param CreateMode.
- Update API RunRCInstances: add param HostName.
- Update API RunRCInstances: add param ResourceGroupId.
- Update API RunRCInstances: add param Tag.
- Update API RunRCInstances: update param InstanceChargeType.


2024-10-18 Version: 7.3.0
- Support API CancelActiveOperationTasks.
- Update API CloneDBInstance: add param DBInstanceDescription.
- Update API CreateDBInstance: update param Period.
- Update API DescribeAvailableClasses: update param DBInstanceStorageType.
- Update API DescribeDBInstanceAttribute: update response param.
- Update API DescribeDBProxy: update response param.
- Update API DescribeDBProxyEndpoint: update response param.
- Update API DescribeModifyParameterLog: update response param.
- Update API ListClasses: add param Engine.
- Update API ListClasses: update response param.
- Update API ModifyAccountMaskingPrivilege: add param RegionId.
- Update API ModifyDBProxy: add param DBProxyNodes.
- Update API ModifyDBProxyEndpoint: add param EffectiveSpecificTime.
- Update API ModifyDBProxyEndpoint: add param EffectiveTime.
- Update API ModifyDBProxyEndpoint: add param VSwitchId.
- Update API ModifyDBProxyInstance: add param DBProxyNodes.
- Update API ModifyDBProxyInstance: add param MigrateAZ.
- Update API ModifyMaskingRules: add param RegionId.
- Update API SyncRCKeyPair: add param SyncMode.


2024-09-10 Version: 7.2.0
- Support API ModifyAccountCheckPolicy.
- Support API ModifyAccountSecurityPolicy.
- Update API CopyDatabase: add param DBInstanceName.
- Update API CopyDatabase: add param DstDBName.
- Update API CopyDatabase: add param ReserveAccount.
- Update API CopyDatabase: add param SrcDBName.


2024-09-09 Version: 7.1.4
- Update API CreateAccount: add param CheckPolicy.
- Update API DescribeAccounts: update response param.
- Update API DescribeRCInstanceAttribute: update response param.
- Update API ModifyDBInstanceSpec: add param AllowMajorVersionUpgrade.
- Update API ModifyDBInstanceSpec: add param VSwitchId.
- Update API ModifyDBInstanceSpec: add param ZoneIdSlave1.
- Update API RunRCInstances: add param DryRun.


2024-09-04 Version: 7.1.3
- Update API DescribeBackupPolicy: update response param.
- Update API DescribeDBInstanceAttribute: update response param.
- Update API DescribePostgresExtensions: update response param.
- Update API TransformDBInstancePayType: update response param.


2024-08-27 Version: 7.1.2
- Update API CreateDBInstance: update param InstanceNetworkType.
- Update API CreateDdrInstance: add param EncryptionKey.
- Update API CreateDdrInstance: add param RoleARN.
- Update API CreateDdrInstance: update response param.
- Update API CreateReadOnlyDBInstance: update param InstanceNetworkType.


2024-08-27 Version: 7.1.2
- Update API CreateDBInstance: update param InstanceNetworkType.
- Update API CreateDdrInstance: add param EncryptionKey.
- Update API CreateDdrInstance: add param RoleARN.
- Update API CreateDdrInstance: update response param.
- Update API CreateReadOnlyDBInstance: update param InstanceNetworkType.


2024-08-23 Version: 7.1.1
- Update API RunRCInstances: update param AutoPay.
- Update API RunRCInstances: update param SecurityGroupId.
- Update API UpgradeDBInstanceMajorVersion: add param UpgradeMode.


2024-08-21 Version: 7.1.0
- Support API CreateRCDeploymentSet.
- Support API CreateReplicationLink.
- Support API DeleteRCDeploymentSet.
- Support API DeleteRCInstance.
- Support API DeleteRCInstances.
- Support API DeleteReplicationLink.
- Support API DescribeRCDeploymentSets.
- Support API DescribeRCImageList.
- Support API DescribeRCInstanceAttribute.
- Support API DescribeRCInstances.
- Support API DescribeRCMetricList.
- Support API DescribeReplicationLinkLogs.
- Support API ModifyRCInstance.
- Support API ModifyRCInstanceChargeType.
- Support API RebootRCInstance.
- Support API RebuildReplicationLink.
- Support API ResizeRCInstanceDisk.
- Support API RunRCInstances.
- Support API StartRCInstance.
- Support API StopRCInstance.
- Support API SyncRCKeyPair.
- Update API QueryRecommendByCode: update param ResourceOwnerId.


2024-08-15 Version: 7.0.0
- Delete API CancelImport.
- Delete API ModifyDBInstanceConnectionMode.
- Delete API ModifyDBInstanceProxyConfiguration.
- Delete API SwitchGuardToMasterInstance.
- Update API CloneDBInstance: add param ClientToken.
- Update API CreateBackup: delete param ResourceGroupId.
- Update API CreateDatabase: delete param ResourceGroupId.
- Update API CreateMaskingRules: add param RegionId.
- Update API CreateYouhuiForOrder: update param ResourceOwnerId.
- Update API DeleteMaskingRules: add param RegionId.
- Update API DescribeAccountMaskingPrivilege: add param RegionId.
- Update API DescribeBackups: delete param ResourceGroupId.
- Update API DescribeBackups: update response param.
- Update API DescribeDatabases: delete param ResourceGroupId.
- Update API DescribeDatabases: update response param.
- Update API DescribeMaskingRules: add param RegionId.


2024-07-23 Version: 6.0.1
- Update API CreateDBInstance: add param AutoCreateProxy.
- Update API CreateReadOnlyDBInstance: add param AutoCreateProxy.


2024-07-23 Version: 6.0.0
- Update API DescribePrice: update response param.


2024-07-03 Version: 5.1.0
- Support API CreateDBInstanceSecurityGroupRule.
- Support API DeleteDBInstanceSecurityGroupRule.
- Support API DescribeDBInstanceSecurityGroupRule.
- Support API ModifyDBInstanceSecurityGroupRule.
- Update API DescribeBackups: update response param.
- Update API DescribeDBInstanceAttribute: update response param.
- Update API DescribeParameters: update response param.


2024-06-27 Version: 5.0.4
- Update API DescribeDBInstanceAttribute: update response param.
- Update API DescribeParameters: update response param.


2024-06-27 Version: 5.0.3
- Update API ModifyDBInstanceSpec: update param ServerlessConfiguration.


2024-06-18 Version: 5.0.2
- Update API DescribeDiagnosticReportList: update param AccessKeyId.


2024-05-23 Version: 5.0.1
- Update API DescribeDBInstanceAttribute: update response param.


2024-04-30 Version: 5.0.0
- Support API CreateMaskingRules.
- Support API DeleteMaskingRules.
- Support API DescribeAccountMaskingPrivilege.
- Support API DescribeMaskingRules.
- Support API ModifyAccountMaskingPrivilege.
- Support API ModifyMaskingRules.
- Update API CreateTempDBInstance: update param BackupId.
- Update API DescribeMetaList: update param BackupSetID.


2024-04-25 Version: 4.0.6
- Update API CreateDBInstance: add param WhitelistTemplateList.
- Update API ModifyDBProxyInstance: add param VSwitchIds.


2024-04-25 Version: 4.0.5
- Update API AttachWhitelistTemplateToInstance: add param RegionId.
- Update API CloneParameterGroup: update param ParameterGroupDesc.
- Update API CreateDBNodes: update param DBNode.
- Update API DescribeAllWhitelistTemplate: add param RegionId.
- Update API DescribeInstanceLinkedWhitelistTemplate: add param RegionId.
- Update API DescribeWhitelistTemplate: add param RegionId.
- Update API DescribeWhitelistTemplateLinkedInstance: add param RegionId.
- Update API DetachWhitelistTemplateToInstance: add param RegionId.
- Update API ModifyWhitelistTemplate: add param RegionId.


2024-04-11 Version: 4.0.4
- Update API DescribePrice: update response param.


2024-04-09 Version: 4.0.3
- Generated python 2014-08-15 for Rds.

2024-04-09 Version: 4.0.2
- Generated python 2014-08-15 for Rds.

2024-04-09 Version: 4.0.1
- Update API DescribeDBInstances: update response param.
- Update API DescribeDatabases: update response param.
- Update API DescribeKmsAssociateResources: update param ResourceOwnerId.
- Update API ModifyDBInstanceSpec: update param DBInstanceStorage.


2024-04-02 Version: 4.0.0
- Delete API ImportDatabaseBetweenInstances.
- Update API DescribeDBInstances: update response param.


2024-03-23 Version: 3.2.1
- Update API CreateDBNodes: update param DBNode.
- Update API CreateOrderForCreateDBNodes: update param DBNode.
- Update API PreCheckCreateOrderForCreateDBNodes: update param DBNode.


2024-03-20 Version: 3.2.0
- Support API DescribeKmsAssociateResources.
- Update API CreateOrderForCreateDBNodes: update param BusinessInfo.
- Update API CreateOrderForDeleteDBNodes: update param BusinessInfo.
- Update API DescribeDBInstanceNetInfo: update response param.
- Update API DescribeGadInstances: update response param.
- Update API ModifyDBInstanceSSL: add param Certificate.
- Update API ModifyDBInstanceSSL: add param PassWord.
- Update API ModifyDBProxyEndpoint: update param DBProxyEndpointId.
- Update API UpgradeDBInstanceMajorVersion: update param PayType.


2024-02-28 Version: 3.1.0
- Support API DescribeKmsAssociateResources.
- Update API DescribeDBInstanceNetInfo: update response param.
- Update API ModifyDBInstanceSSL: add param Certificate.
- Update API ModifyDBInstanceSSL: add param PassWord.


2024-02-27 Version: 3.0.6
- Update API DescribeDBInstanceNetInfo: update response param.
- Update API ModifyDBInstanceSSL: add param Certificate.
- Update API ModifyDBInstanceSSL: add param PassWord.


2024-01-31 Version: 3.0.5
- Update API DescribeBackupPolicyupdate response param.


2024-01-23 Version: 3.0.4
- Generated python 2014-08-15 for Rds.

2024-01-22 Version: 3.0.3
- Generated python 2014-08-15 for Rds.

2024-01-05 Version: 3.0.2
- Generated python 2014-08-15 for Rds.

2023-12-20 Version: 3.0.1
- Generated python 2014-08-15 for Rds.

2023-12-15 Version: 3.0.0
- Generated python 2014-08-15 for Rds.

2023-11-23 Version: 2.5.6
- Generated python 2014-08-15 for Rds.

2023-11-23 Version: 2.5.5
- Generated python 2014-08-15 for Rds.

2023-11-21 Version: 2.5.4
- Generated python 2014-08-15 for Rds.

2023-11-15 Version: 2.5.3
- Generated python 2014-08-15 for Rds.

2023-11-10 Version: 2.5.2
- Generated python 2014-08-15 for Rds.

2023-11-07 Version: 2.5.1
- Generated python 2014-08-15 for Rds.

2023-11-03 Version: 2.5.0
- Generated python 2014-08-15 for Rds.

2023-10-21 Version: 2.4.0
- Generated python 2014-08-15 for Rds.

2023-09-14 Version: 2.3.0
- Generated python 2014-08-15 for Rds.

2023-08-08 Version: 2.2.33
- Generated python 2014-08-15 for Rds.

2023-08-06 Version: 2.2.32
- Generated python 2014-08-15 for Rds.

2023-08-05 Version: 2.2.31
- Generated python 2014-08-15 for Rds.

2023-08-04 Version: 2.2.30
- Generated python 2014-08-15 for Rds.

2023-07-31 Version: 2.2.29
- Fix bug ram.
- Add minor version error.
- Support to select the minor version of the kernel when the modify instance error reports that the kernel version does not support it.

2023-07-30 Version: 2.2.28
- Fix bug ram.
- Add minor version error.
- Support to select the minor version of the kernel when the modify instance error reports that the kernel version does not support it.

2023-07-29 Version: 2.2.27
- Fix bug ram.
- Add minor version error.
- Support to select the minor version of the kernel when the modify instance error reports that the kernel version does not support it.

2023-07-28 Version: 2.2.26
- Fix bug ram.
- Add minor version error.
- Support to select the minor version of the kernel when the modify instance error reports that the kernel version does not support it.

2023-07-27 Version: 2.2.25
- Fix bug ram.
- Add minor version error.
- Support to select the minor version of the kernel when the modify instance error reports that the kernel version does not support it.

2023-07-25 Version: 2.2.24
- Add error code.
- Support System param.

2023-07-24 Version: 2.2.23
- Add error code.
- Add error code for CreateDBNodes.

2023-07-23 Version: 2.2.22
- Fix 500 for CreateOrder.
- Support sts.

2023-07-22 Version: 2.2.21
- Fix 500 for CreateOrder.
- Support sts.

2023-07-21 Version: 2.2.20
- Fix 500 for CreateOrder.
- Support sts.

2023-07-19 Version: 2.2.19
- Add openapis for whitelist template.

2023-07-18 Version: 2.2.18
- Supported RDS PostgreSQL manage extensions.

2023-07-17 Version: 2.2.17
- Add TimeOut.

2023-07-16 Version: 2.2.16
- Add error code.

2023-07-15 Version: 2.2.15
- Add error code.

2023-07-13 Version: 2.2.14
- Support change instance config event for rds.
- Add NodeId param for restart slave.

2023-07-12 Version: 2.2.13
- Add error coede.
- Fix bugs for 500.

2023-07-11 Version: 2.2.12
- Fixed 500 for interface.

2023-07-10 Version: 2.2.11
- Fixed 500 for interface.

2023-07-10 Version: 2.2.10
- Add DescribeClassDetails Api.

2023-07-09 Version: 2.2.9
- Add AutoUseCoupon field.
- Api Offline.

2023-07-08 Version: 2.2.8
- Add AutoUseCoupon field.
- Api Offline.

2023-07-07 Version: 2.2.7
- Add AutoUseCoupon field.
- Api Offline.

2023-07-06 Version: 2.2.6
- Add AutoUseCoupon field.
- Api Offline.

2023-07-05 Version: 2.2.5
- Add AutoUseCoupon field.
- Api Offline.

2023-07-04 Version: 2.2.4
- Fix bugs for  DescribeDedicatedHosts.
- Fixed bugs add ERRORCODE.
- Added serverless config to support serverless price query.

2023-07-04 Version: 2.2.3
- ModifyBackupPolicy API support parameter BackupPriority.
- DescribeBackupPolicy API add return parameters: BackupPriority and SupportModifyBackupPriority.

2023-07-03 Version: 2.2.2
- Fix bugs for  DescribeDedicatedHosts.
- Fixed bugs add ERRORCODE.
- Added serverless config to support serverless price query.

2023-07-02 Version: 2.2.1
- Fixed bugs for lack of regionId.
- Fix error code.

2023-07-01 Version: 2.2.0
- Fixed bugs for lack of regionId.
- Fix error code.

2023-06-30 Version: 2.1.9
- Fixed bugs for lack of regionId.
- Fix error code.

2023-06-30 Version: 2.1.8
- ModifyBackupPolicy API support parameter BackupPriority.
- DescribeBackupPolicy API add return parameters: BackupPriority and SupportModifyBackupPriority.

2023-06-29 Version: 2.1.7
- Support More Open Api.

2023-06-26 Version: 2.1.6
- Support More Open Api.

2023-06-15 Version: 2.1.5
- Support More Open Api.

2023-03-27 Version: 2.1.4
- Support More Open Api.

2023-02-21 Version: 2.1.3
- Support More Open Api.

2022-11-22 Version: 2.1.2
- Support More Open Api.

2022-08-31 Version: 2.1.1
- Support More Open Api.

2022-05-27 Version: 2.1.0
- StartDBInstance parameter change.

2022-05-06 Version: 2.0.6
- StartDBInstance parameter change.

2021-09-16 Version: 2.0.5
- AMP Version Change.

2021-07-28 Version: 2.0.4
- AMP Version Change.

2021-07-05 Version: 2.0.3
- AMP Version Change.

2021-04-29 Version: 2.0.2
- Update AMP API.

2021-01-12 Version: 2.0.1
- Generated python 2014-08-15 for Rds.

2020-12-28 Version: 2.0.0
- AMP Version Change.

2020-11-26 Version: 1.0.1
- Generated python 2014-08-15 for Rds.

