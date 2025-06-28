2025-06-28 Version: 5.0.5
- Update API DescribeSQLPatterns: add request parameters UserName.


2025-06-11 Version: 5.0.4
- Update API CreateDBResourceGroup: add request parameters ClusterMode.
- Update API CreateDBResourceGroup: add request parameters ClusterSizeResource.
- Update API CreateDBResourceGroup: add request parameters Engine.
- Update API CreateDBResourceGroup: add request parameters EngineParams.
- Update API CreateDBResourceGroup: add request parameters MaxClusterCount.
- Update API CreateDBResourceGroup: add request parameters MaxComputeResource.
- Update API CreateDBResourceGroup: add request parameters MinClusterCount.
- Update API CreateDBResourceGroup: add request parameters MinComputeResource.
- Update API DescribeDBClusterNetInfo: add request parameters Engine.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.ClusterMode.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.ClusterSizeResource.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.ConnectionString.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.ElasticMinComputeResource.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.Engine.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.EngineParams.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.MaxClusterCount.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.MaxComputeResource.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.MinClusterCount.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.MinComputeResource.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.Port.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.RunningClusterCount.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.Status.
- Update API ModifyDBResourceGroup: add request parameters ClusterMode.
- Update API ModifyDBResourceGroup: add request parameters ClusterSizeResource.
- Update API ModifyDBResourceGroup: add request parameters EngineParams.
- Update API ModifyDBResourceGroup: add request parameters MaxClusterCount.
- Update API ModifyDBResourceGroup: add request parameters MaxComputeResource.
- Update API ModifyDBResourceGroup: add request parameters MinClusterCount.
- Update API ModifyDBResourceGroup: add request parameters MinComputeResource.


2025-05-27 Version: 5.0.3
- Update API DescribeDBClusters: add request parameters DBClusterVersion.


2025-05-21 Version: 5.0.2
- Update API DescribeEIURange: add response parameters Body.EIUInfo.DefaultReservedNodeSize.
- Update API DescribeEIURange: add response parameters Body.EIUInfo.ReservedNodeSizeRange.
- Update API MigrateDBCluster: add request parameters DryRun.


2025-04-28 Version: 5.0.1
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.ProductForm.
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.ReservedNodeCount.
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.ReservedNodeSize.


2025-04-28 Version: 5.0.0
- Support API DescribeAbnormalPatternDetection.
- Support API DescribeBadSqlDetection.
- Support API DescribeControllerDetection.
- Support API DescribeExecutorDetection.
- Support API DescribeInclinedNodes.
- Support API DescribeOversizeNonPartitionTableInfos.
- Support API DescribeWorkerDetection.
- Support API GetCreateTableSQL.
- Support API ModifyDBClusterShardNumber.
- Update API AttachUserENI: delete request parameters AccessKeyId-copy.
- Update API BindDBResourceGroupWithUser: add request parameters ClientToken.
- Update API BindDBResourcePoolWithUser: add request parameters ClientToken.
- Update API CreateAccount: add request parameters Tag.
- Update API CreateDBResourceGroup: add request parameters ClientToken.
- Update API DescribeAccounts: add request parameters Tags.
- Update API DescribeAccounts: add response parameters Body.AccountList.$.Tags.
- Update API DescribeAvailableResource: add response parameters Body.AvailableZoneList.$.ZoneName.
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.SecondaryVSwitchId.
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.SecondaryZoneId.
- Update API DescribeDBClusterPerformance: add response parameters Body.Performances.$.Series.$.TranslateKey.
- Update API DescribeDBClusterShardNumber: add response parameters Body.AvailableShardNumberList.
- Update API DescribeDBClusterSpaceSummary: delete request parameters OwnerAccount.
- Update API DescribeDBClusterSpaceSummary: delete request parameters OwnerId.
- Update API DescribeDBClusterSpaceSummary: delete request parameters ResourceOwnerAccount.
- Update API DescribeDBClusterSpaceSummary: delete request parameters ResourceOwnerId.
- Update API DescribeEIURange: add request parameters ProductVersion.
- Update API DescribeTableStatistics: add request parameters SchemaName.
- Update API DescribeTableStatistics: add response parameters Body.SchemaNames.
- Update API MigrateDBCluster: add request parameters ProductForm.
- Update API MigrateDBCluster: add request parameters ProductVersion.
- Update API MigrateDBCluster: add request parameters ReservedNodeCount.
- Update API MigrateDBCluster: add request parameters ReservedNodeSize.
- Update API MigrateDBCluster: add request parameters SecondaryVSwitchId.
- Update API MigrateDBCluster: add request parameters SecondaryZoneId.
- Update API ModifyDBResourceGroup: add request parameters ClientToken.
- Update API UnbindDBResourceGroupWithUser: add request parameters ClientToken.
- Update API UnbindDBResourcePoolWithUser: add request parameters ClientToken.


2024-12-10 Version: 4.4.0
- Support API DescribeLogHubAttribute.
- Support API DescribeLogStoreKeys.
- Support API DescribeRdsAnalysisResourceQuotas.
- Update API AllocateClusterPublicConnection: update param AccessKeyId.


2024-12-09 Version: 4.3.0
- Support API CancelActiveOperationTasks.
- Support API CheckServiceLinkedRole.
- Support API CreateServiceLinkedRole.
- Support API DescribeActiveOperationMaintainConf.
- Support API DescribeActiveOperationTasks.
- Support API DescribeHistoryEventsStat.
- Support API DescribeKmsKeys.
- Support API DescribeLoghubDetail.
- Support API DescribeRegionsMixed.
- Support API DescribeSyncAvailableDBClusterList.
- Support API DescribeSyncJobList.
- Support API DescribeVSwitchs.
- Support API DescribeVpcs.
- Support API ModifyActiveOperationMaintainConf.
- Support API ModifyActiveOperationTasks.
- Support API ModifyDBClusterVip.
- Support API ModifyLogHubStatus.
- Support API ModifySyncJob.
- Support API OperateLogHub.
- Update API AttachUserENI: add param AccessKeyId-copy.
- Update API AttachUserENI: update param AccessKeyId.
- Update API DescribeDiagnosisTasks: update response param.
- Update API UpgradeKernelVersion: update param DBVersion.
- Update API UpgradeKernelVersion: update param SwitchMode.


2024-11-08 Version: 4.2.1
- Update API DescribeDBClusterPerformance: update response param.
- Update API DescribeDBClusterShardNumber: update response param.


2024-10-31 Version: 4.2.0
- Support API DeleteBackups.


2024-10-28 Version: 4.1.1
- Update API DescribeDBClusterSSL: add param RegionId.


2024-10-25 Version: 4.1.0
- Support API DescribeDBClusterShardNumber.
- Update API DescribeInclinedTables: update param PageSize.


2024-10-23 Version: 4.0.0
- Support API DescribeDBClusterSSL.
- Support API DescribeDBClusterSpaceSummary.
- Support API DescribeExcessivePrimaryKeys.
- Support API DescribeKernelVersion.
- Support API ModifyDBClusterSSL.
- Support API UpgradeKernelVersion.
- Delete API DescribeSlowLogTrend.
- Update API BatchApplyAdviceByIdList: update response param.
- Update API CreateDBCluster: add param EnableSSL.
- Update API CreateDBCluster: update param DiskEncryption.
- Update API CreateElasticPlan: add param ElasticPlanWeeklyRepeat.
- Update API CreateElasticPlan: add param ElasticPlanMonthlyRepeat.
- Update API CreateElasticPlan: update param ElasticPlanWeeklyRepeat.
- Update API CreateElasticPlan: update param ResourcePoolName.
- Update API DescribeAllAccounts: update response param.
- Update API DescribeAppliedAdvices: add param AdviceType.
- Update API DescribeAppliedAdvices: add param Keyword.
- Update API DescribeAppliedAdvices: add param Order.
- Update API DescribeAppliedAdvices: add param SchemaTableName.
- Update API DescribeAppliedAdvices: update response param.
- Update API DescribeAuditLogConfig: update response param.
- Update API DescribeAuditLogRecords: update param EndTime.
- Update API DescribeAuditLogRecords: update param StartTime.
- Update API DescribeAuditLogRecords: update response param.
- Update API DescribeAvailableAdvices: add param AdviceType.
- Update API DescribeAvailableAdvices: add param Keyword.
- Update API DescribeAvailableAdvices: add param Order.
- Update API DescribeAvailableAdvices: add param SchemaTableName.
- Update API DescribeAvailableAdvices: update response param.
- Update API DescribeBackups: add param CrossRole.
- Update API DescribeBackups: add param CrossUid.
- Update API DescribeBackups: add param RegionId.
- Update API DescribeBackups: update param EndTime.
- Update API DescribeBackups: update param StartTime.
- Update API DescribeBackups: update response param.
- Update API DescribeDBClusterAccessWhiteList: add param RegionId.
- Update API DescribeDBClusterAttribute: add param RegionId.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterNetInfo: add param RegionId.
- Update API DescribeDBClusterNetInfo: update response param.
- Update API DescribeDBClusters: update response param.
- Update API DescribeDBResourceGroup: update response param.
- Update API DescribeDiagnosisDimensions: update response param.
- Update API DescribeDiagnosisMonitorPerformance: update response param.
- Update API DescribeDiagnosisRecords: update response param.
- Update API DescribeEIURange: add param StorageSize.
- Update API DescribeEIURange: add param SubOperation.
- Update API DescribeEIURange: update param ComputeResource.
- Update API DescribeEIURange: update param Operation.
- Update API DescribeEIURange: update response param.
- Update API DescribeElasticPlan: update response param.
- Update API DescribeInclinedTables: add param Lang.
- Update API DescribeInclinedTables: add param RegionId.
- Update API DescribeInclinedTables: update param DBClusterId.
- Update API DescribeInclinedTables: update response param.
- Update API DescribePatternPerformance: update response param.
- Update API DescribeRegions: add param RegionId.
- Update API DescribeSQLPatterns: update response param.
- Update API DescribeTableDetail: add param RegionId.
- Update API DescribeTableDetail: update param DBClusterId.
- Update API DescribeTableDetail: update response param.
- Update API DescribeTablePartitionDiagnose: add param Lang.
- Update API DescribeTablePartitionDiagnose: add param Order.
- Update API DescribeTablePartitionDiagnose: delete param Action.
- Update API DescribeTablePartitionDiagnose: update param AccessKeyId.
- Update API DescribeTablePartitionDiagnose: update param DBClusterId.
- Update API DescribeTablePartitionDiagnose: update param OwnerAccount.
- Update API DescribeTablePartitionDiagnose: update param OwnerId.
- Update API DescribeTablePartitionDiagnose: update param ResourceOwnerAccount.
- Update API DescribeTablePartitionDiagnose: update param ResourceOwnerId.
- Update API DescribeTablePartitionDiagnose: update response param.
- Update API DescribeTableStatistics: add param Keyword.
- Update API DescribeTableStatistics: update param RegionId.
- Update API DescribeTableStatistics: update response param.
- Update API MigrateDBCluster: add param ComputeResource.
- Update API MigrateDBCluster: add param ShardNumber.
- Update API MigrateDBCluster: add param StorageResource.
- Update API MigrateDBCluster: add param StorageResourceSize.
- Update API ModifyBackupPolicy: update param PreferredBackupPeriod.
- Update API ModifyDBClusterPayType: add param RegionId.
- Update API ModifyDBResourceGroup: add param PoolUserList.
- Update API ModifyElasticPlan: add param ElasticPlanMonthlyRepeat.
- Update API ModifyElasticPlan: update param ResourcePoolName.


2024-02-20 Version: 3.1.2
- Update API CreateElasticPlan: add param ElasticPlanWeeklyRepeat.
- Update API CreateElasticPlan: add param ElasticPlanMonthlyRepeat.
- Update API CreateElasticPlan: update param ElasticPlanWeeklyRepeat.
- Update API CreateElasticPlan: update param ResourcePoolName.
- Update API DescribeAuditLogRecords: update param EndTime.
- Update API DescribeAuditLogRecords: update param StartTime.
- Update API DescribeAuditLogRecords: update response param.
- Update API DescribeDiagnosisRecords: update response param.
- Update API DescribeElasticPlan: update response param.
- Update API DescribeTableStatistics: add param Keyword.
- Update API DescribeTableStatistics: update response param.
- Update API ModifyElasticPlan: add param ElasticPlanMonthlyRepeat.
- Update API ModifyElasticPlan: update param ResourcePoolName.


2024-02-06 Version: 3.1.1
- Generated python 2019-03-15 for adb.

2023-12-11 Version: 3.1.0
- Generated python 2019-03-15 for adb.

2023-10-23 Version: 3.0.0
- Generated python 2019-03-15 for adb.

2023-09-19 Version: 2.0.0
- Generated python 2019-03-15 for adb.

2023-08-31 Version: 1.1.2
- Generated python 2019-03-15 for adb.

2023-08-22 Version: 1.1.1
- Generated python 2019-03-15 for adb.

2023-08-17 Version: 1.1.0
- Generated python 2019-03-15 for adb.

2022-05-26 Version: 1.0.11
- Support ModifyDBClusterPayType.

2022-01-05 Version: 1.0.10
- Move to perth for DescribeAuditLogRecords.
- Move to perth for DescribeAuditLogConfig.

2021-10-25 Version: 1.0.9
- CreateDBCluster Support ElasticResourceIO.

2021-05-14 Version: 1.0.8
- Update CreateDBCluster.
- Update ModifyDBCluster.

2021-03-31 Version: 1.0.7
- Generated python 2019-03-15 for adb.

2021-03-12 Version: 1.0.6
- Supportd DescribeTableStatisticsRequest.

