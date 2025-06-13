2025-06-13 Version: 5.8.0
- Support API DescribeHALogs.
- Support API ReactivateDBClusterBackup.


2025-05-14 Version: 5.7.0
- Support API CreateGlobalDataNetwork.
- Support API DeleteGlobalDataNetwork.
- Support API DescribeGlobalDataNetworkList.
- Update API CreateGlobalDatabaseNetwork: add request parameters GDNVersion.
- Update API DescribeGlobalDatabaseNetwork: add response parameters Body.Labels.
- Update API DescribeGlobalDatabaseNetworks: add response parameters Body.Items.$.Labels.
- Update API RemoveDBClusterFromGDN: add request parameters Force.


2025-05-14 Version: 5.7.0
- Support API CreateGlobalDataNetwork.
- Support API DeleteGlobalDataNetwork.
- Support API DescribeGlobalDataNetworkList.
- Update API CreateGlobalDatabaseNetwork: add request parameters GDNVersion.
- Update API DescribeGlobalDatabaseNetwork: add response parameters Body.Labels.
- Update API DescribeGlobalDatabaseNetworks: add response parameters Body.Items.$.Labels.
- Update API RemoveDBClusterFromGDN: add request parameters Force.


2025-05-06 Version: 5.6.1
- Update API ModifyMaskingRules: add request parameters DefaultAlgo.
- Update API ModifyMaskingRules: add request parameters MaskingAlgo.


2025-03-25 Version: 5.6.0
- Support API DescribeHistoryTasks.
- Update API DescribeDBClusterAttribute: add response parameters Body.DBNodes.$.SubGroupDescription.


2025-03-20 Version: 5.5.3
- Update API DescribeDBClusterAttribute: update response param.


2025-03-15 Version: 5.5.2
- Generated python 2017-08-01 for polardb.

2025-03-14 Version: 5.5.1
- Generated python 2017-08-01 for polardb.

2025-03-14 Version: 5.5.0
- Support API ModifyDBClusterArch.
- Update API CreateAccount: add param NodeType.
- Update API CreateDBCluster: update param DBNodeClass.
- Update API CreateDBCluster: update param StorageSpace.
- Update API DeleteMaskingRules: add param InterfaceVersion.
- Update API DescribeAccounts: add param NodeType.
- Update API DescribeAccounts: update response param.
- Update API DescribeDBClusterEndpoints: update response param.
- Update API DescribeMaskingRules: add param InterfaceVersion.
- Update API ModifyDBCluster: update param FaultInjectionType.
- Update API ModifyDBCluster: update param FaultSimulateMode.
- Update API ModifyMaskingRules: add param InterfaceVersion.
- Update API ModifyMaskingRules: update param RuleConfig.
- Update API ModifyMaskingRules: update param RuleName.


2025-02-06 Version: 5.4.1
- Update API DescribeActivationCodes: add param MacAddress.
- Update API DescribeActivationCodes: add param SystemIdentifier.


2025-01-20 Version: 5.4.0
- Support API ModifyDBClusterStoragePerformance.
- Update API DescribeDBClusterAttribute: update response param.
- Update API ModifyDBCluster: add param ModifyRowCompression.
- Update API ModifyDBCluster: add param TableMeta.


2024-12-31 Version: 5.3.2
- Update API CreateDBCluster: add param StorageEncryption.
- Update API CreateDBCluster: add param StorageEncryptionKey.
- Update API DescribeDBClusterTDE: update response param.
- Update API DescribeUserEncryptionKeyList: update param AccessKeyId.
- Update API DescribeUserEncryptionKeyList: update param DBClusterId.
- Update API DescribeUserEncryptionKeyList: update param TDERegion.


2024-12-26 Version: 5.3.1
- Update API CreateDBCluster: add param StorageEncryption.
- Update API CreateDBCluster: add param StorageEncryptionKey.
- Update API DescribeDBClusterTDE: update response param.
- Update API DescribeUserEncryptionKeyList: update param AccessKeyId.
- Update API DescribeUserEncryptionKeyList: update param DBClusterId.
- Update API DescribeUserEncryptionKeyList: update param TDERegion.


2024-12-19 Version: 5.3.0
- Support API CancelActiveOperationTasks.
- Support API DescribeActiveOperationTasks.
- Support API ModifyActiveOperationTasks.
- Update API CreateAccount: update param AccessKeyId.
- Update API CreateAccount: update param AccountPassword.
- Update API CreateBackup: update param AccessKeyId.
- Update API CreateDBCluster: update param HotStandbyCluster.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterSSL: update param AccessKeyId.
- Update API DescribeDBClusterSSL: update response param.
- Update API ModifyDBClusterAndNodesParameters: add param StandbyClusterIdListNeedToSync.
- Update API ModifyDBClusterAndNodesParameters: update param AccessKeyId.
- Update API RestoreTable: update param AccessKeyId.
- Update API RestoreTable: update param SecurityToken.


2024-12-02 Version: 5.2.3
- Update API CreateDBCluster: add param TargetMinorVersion.


2024-11-15 Version: 5.2.2
- Update API CreateDBCluster: add param BurstingEnabled.
- Update API CreateDBCluster: update param DBNodeNum.
- Update API DescribeBackups: update param AccessKeyId.
- Update API DescribeBackups: update response param.
- Update API DescribeClassList: update param AccessKeyId.
- Update API DescribeClassList: update response param.
- Update API DescribeDBClusterAttribute: update response param.
- Update API ModifyDBNodeHotReplicaMode: update param AccessKeyId.


2024-10-29 Version: 5.2.1
- Update API DescribeAITaskStatus: update param AccessKeyId.
- Update API DescribeAITaskStatus: update response param.
- Update API DescribeCharacterSetName: update param AccessKeyId.
- Update API DescribeDBClusterAvailableResources: update param AccessKeyId.
- Update API EvaluateRegionResource: update param AccessKeyId.


2024-10-25 Version: 5.2.0
- Support API CreateActivationCode.
- Support API CreateOrGetVirtualLicenseOrder.
- Support API DescribeActivationCodeDetails.
- Support API DescribeActivationCodes.
- Support API DescribeLicenseOrderDetails.
- Support API DescribeLicenseOrders.
- Update API CreateDBCluster: update param AccessKeyId.
- Update API DescribeAutoRenewAttribute: update param AccessKeyId.
- Update API DescribeDBClusterAccessWhitelist: update param AccessKeyId.
- Update API DescribeDBClusterAttribute: update param AccessKeyId.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterMigration: update param AccessKeyId.
- Update API DescribeDBClusterTDE: update param AccessKeyId.
- Update API DescribeDBClusterTDE: update response param.
- Update API DescribeDBClusters: update param AccessKeyId.
- Update API DescribeRegions: update param AccessKeyId.
- Update API DescribeScheduleTasks: update param AccessKeyId.
- Update API DescribeScheduleTasks: update response param.
- Update API ModifyDBCluster: add param ImciAutoIndex.
- Update API ModifyDBCluster: update param AccessKeyId.
- Update API ModifyDBClusterServerlessConf: add param CrontabJobId.
- Update API ModifyDBClusterServerlessConf: add param TaskId.
- Update API ModifyDBClusterServerlessConf: update param AccessKeyId.
- Update API ModifyDBClusterTDE: add param EnableAutomaticRotation.
- Update API ModifyDBClusterTDE: update param AccessKeyId.
- Update API RefreshDBClusterStorageUsage: update param AccessKeyId.
- Update API TempModifyDBNode: update param AccessKeyId.


2024-09-25 Version: 5.1.13
- Update API DeleteDBCluster: update param AccessKeyId.
- Update API DeleteDBCluster: update param BackupRetentionPolicyOnClusterDeletion.
- Update API DescribeSlowLogRecords: update param AccessKeyId.
- Update API DescribeSlowLogRecords: update response param.


2024-08-29 Version: 5.1.12
- Update API CreateGlobalDatabaseNetwork: add param EnableGlobalDomainName.
- Update API DescribeGlobalDatabaseNetwork: update response param.
- Update API DescribeScheduleTasks: update response param.
- Update API ModifyDBNodeClass: add param PlannedFlashingOffTime.
- Update API ModifyDBNodesClass: add param PlannedFlashingOffTime.
- Update API ModifyGlobalDatabaseNetwork: add param EnableGlobalDomainName.
- Update API ModifyGlobalDatabaseNetwork: update param GDNDescription.


2024-08-27 Version: 5.1.11
- Update API DescribeDBProxyPerformance: add param DBNodeId.


2024-08-20 Version: 5.1.10
- Update API DescribeDBClusterAttribute: update response param.
- Update API FailoverDBCluster: add param TargetZoneType.


2024-08-08 Version: 5.1.9
- Update API FailoverDBCluster: add param TargetZoneType.


2024-07-30 Version: 5.1.8
- Update API CreateDBClusterEndpoint: add param PolarSccTimeoutAction.
- Update API CreateDBClusterEndpoint: add param PolarSccWaitTimeout.
- Update API CreateDBClusterEndpoint: add param SccMode.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterEndpoints: update response param.
- Update API DescribeDBClusterServerlessConf: update response param.
- Update API DescribeGlobalDatabaseNetworks: update response param.
- Update API ModifyDBClusterEndpoint: add param PolarSccTimeoutAction.
- Update API ModifyDBClusterEndpoint: add param PolarSccWaitTimeout.
- Update API ModifyDBClusterEndpoint: add param SccMode.


2024-07-24 Version: 5.1.7
- Update API DescribeDBClusters: update response param.


2024-07-11 Version: 5.1.6
- Update API DescribeAccounts: update response param.
- Update API DescribeDBClusterPerformance: add param Type.
- Update API DescribeDBClusters: update response param.


2024-06-28 Version: 5.1.5
- Generated python 2017-08-01 for polardb.

2024-06-25 Version: 5.1.4
- Update API DescribeDBClusters: update response param.
- Update API DescribeSlowLogRecords: add param NodeId.


2024-06-06 Version: 5.1.3
- Update API DescribeDBClusterAttribute: update response param.
- Update API ModifyDBCluster: add param DBNodeCrashList.
- Update API ModifyDBCluster: add param FaultInjectionType.


2024-06-06 Version: 5.1.3
- Update API DescribeDBClusterAttribute: update response param.
- Update API ModifyDBCluster: add param DBNodeCrashList.
- Update API ModifyDBCluster: add param FaultInjectionType.


2024-05-28 Version: 5.1.2
- Update API DescribeDBClusterAvailableResources: update response param.
- Update API DescribeDBClusterVersion: update response param.
- Update API UpgradeDBClusterVersion: add param TargetProxyRevisionVersionCode.


2024-05-17 Version: 5.1.1
- Update API DescribeDBClusterServerlessConf: update response param.
- Update API DescribeDBClusters: update response param.
- Update API ModifyDBClusterServerlessConf: add param ServerlessRuleCpuEnlargeThreshold.
- Update API ModifyDBClusterServerlessConf: add param ServerlessRuleCpuShrinkThreshold.
- Update API ModifyDBClusterServerlessConf: add param ServerlessRuleMode.


2024-04-24 Version: 5.1.0
- Support API RestartDBLink.


2024-04-18 Version: 5.0.8
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusters: update response param.


2024-04-09 Version: 5.0.7
- Update API DescribeDBClusters: update response param.


2024-03-14 Version: 5.0.6
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterParameters: update response param.
- Update API DescribeDBClusterPerformance: add param Interval.
- Update API DescribeDBClusterVersion: update response param.
- Update API DescribeDBNodePerformance: add param Interval.
- Update API DescribeDBNodePerformance: add param Type.
- Update API DescribeDBProxyPerformance: add param Interval.
- Update API DescribeDBProxyPerformance: add param Type.
- Update API ModifyAccountPassword: add param PasswordType.
- Update API ModifyDBClusterPrimaryZone: add param ZoneType.


2024-03-13 Version: 5.0.5
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterParameters: update response param.
- Update API DescribeDBClusterPerformance: add param Interval.
- Update API DescribeDBClusterVersion: update response param.
- Update API DescribeDBNodePerformance: add param Interval.
- Update API DescribeDBProxyPerformance: add param Interval.
- Update API ModifyAccountPassword: add param PasswordType.
- Update API ModifyDBClusterPrimaryZone: add param ZoneType.


2024-02-29 Version: 5.0.4
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterParameters: update response param.
- Update API DescribeDBClusterPerformance: add param Interval.
- Update API DescribeDBClusterVersion: update response param.
- Update API ModifyDBClusterPrimaryZone: add param ZoneType.


2024-02-27 Version: 5.0.3
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterVersion: update response param.
- Update API ModifyDBClusterPrimaryZone: add param ZoneType.


2024-02-22 Version: 5.0.2
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterVersion: update response param.


2024-02-21 Version: 5.0.1
- Generated python 2017-08-01 for polardb.

2024-02-04 Version: 5.0.0
- Delete API UpgradeDBClusterMinorVersion.
- Update API DescribeDBProxyPerformanceadd DBEndpointId param.


2024-01-24 Version: 4.1.3
- Generated python 2017-08-01 for polardb.

2024-01-05 Version: 4.1.2
- Generated python 2017-08-01 for polardb.

2024-01-05 Version: 4.1.1
- Generated python 2017-08-01 for polardb.

2023-12-27 Version: 4.1.0
- Generated python 2017-08-01 for polardb.

2023-11-16 Version: 4.0.1
- Generated python 2017-08-01 for polardb.

2023-11-07 Version: 4.0.0
- Generated python 2017-08-01 for polardb.

2023-10-30 Version: 3.2.1
- Generated python 2017-08-01 for polardb.

2023-10-12 Version: 3.2.0
- Generated python 2017-08-01 for polardb.

2023-10-12 Version: 3.2.0
- Generated python 2017-08-01 for polardb.

2023-09-25 Version: 3.1.0
- Generated python 2017-08-01 for polardb.

2023-09-22 Version: 3.0.3
- Generated python 2017-08-01 for polardb.

2023-09-18 Version: 3.0.2
- Generated python 2017-08-01 for polardb.

2023-09-12 Version: 3.0.1
- Generated python 2017-08-01 for polardb.

2023-09-07 Version: 3.0.0
- Generated python 2017-08-01 for polardb.

2022-12-05 Version: 2.0.11
- Support GDN feature.

2022-10-10 Version: 2.0.10
- Support serverless feature.

2022-09-09 Version: 2.0.9
- Support new feature.

2022-08-04 Version: 2.0.8
- Support new feature.

2022-08-01 Version: 2.0.7
- Support new feature.

2022-04-24 Version: 2.0.6
- Support new feature.

2022-02-22 Version: 2.0.5
 - Support RefreshProxyLevel.

2022-02-09 Version: 2.0.4
- Supported the latested feature.

2021-07-07 Version: 2.0.3
- Generated python 2017-08-01 for polardb.

2021-03-31 Version: 2.0.2
- Generated python 2017-08-01 for polardb.

2021-02-16 Version: 2.0.1
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

