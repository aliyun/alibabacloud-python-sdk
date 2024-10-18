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

