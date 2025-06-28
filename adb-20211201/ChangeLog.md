2025-06-28 Version: 3.1.2
- Update API DescribeSQLPatterns: add request parameters UserName.


2025-06-25 Version: 3.1.1
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.AINodeNumber.
- Update API DescribeDBClusterAttribute: add response parameters Body.Items.$.AINodeSpec.


2025-05-26 Version: 3.1.0
- Support API DescribeAdbMySqlIndexes.
- Support API DescribeAdbMySqlTableMeta.
- Support API DescribeLLMAnswer.
- Support API DescribeLLMSimilarQuestions.
- Support API DescribeSQLWebSocketDomain.
- Support API DescribeTableStatistics.
- Update API DescribeBackups: add request parameters Remote.
- Update API DescribeBackups: add response parameters Body.Items.$.BackupRegion.
- Update API DescribeBackups: add response parameters Body.Items.$.ParentBackupId.


2025-04-18 Version: 3.0.3
- Update API DescribeDiagnosisSQLInfo: add response parameters Body.StageInfos.$.ExecutionType.


2025-04-17 Version: 3.0.2
- Generated python 2021-12-01 for adb.

2025-04-15 Version: 3.0.1
- Generated python 2021-12-01 for adb.

2025-04-15 Version: 3.0.0
- Support API DescribeInclinedTables.
- Support API DescribeResourceGroupSpec.
- Delete API DeleteProcessInstance.
- Update API GetViewObjects: add request parameters ShowMvBaseTable.
- Update API ModifyDBCluster: delete request parameters OwnerAccount.
- Update API ModifyDBCluster: delete request parameters OwnerId.
- Update API ModifyDBCluster: delete request parameters ResourceOwnerAccount.


2025-03-31 Version: 2.2.1
- Update API CreateDBResourceGroup: add request parameters RayConfig.
- Update API DescribeDBResourceGroup: add response parameters Body.GroupsInfo.$.RayConfig.
- Update API ModifyDBResourceGroup: add request parameters RayConfig.


2025-03-12 Version: 2.2.0
- Support API UpgradeKernelVersion.
- Update API CreateDBCluster: add param ProductVersion.
- Update API CreateDBCluster: add param SecondaryVSwitchId.
- Update API CreateDBCluster: add param SecondaryZoneId.
- Update API DescribeDBClusterAttribute: update response param.


2025-02-18 Version: 2.1.0
- Support API ApplyAdviceById.
- Support API BatchApplyAdviceByIdList.
- Support API CancelSparkReplStatement.
- Support API CancelSparkWarehouseBatchSQL.
- Support API CreateAPSJob.
- Support API CreateApsCopyWorkload.
- Support API CreateApsDatasoure.
- Support API CreateApsHiveJob.
- Support API CreateApsSlsADBJob.
- Support API CreateLakeStorage.
- Support API DeleteApsDatasoure.
- Support API DeleteApsJob.
- Support API DeleteBackups.
- Support API DeleteLakeStorage.
- Support API DescribeAPSADBInstances.
- Support API DescribeAbnormalPatternDetection.
- Support API DescribeAdviceServiceEnabled.
- Support API DescribeAppliedAdvices.
- Support API DescribeApsDatasource.
- Support API DescribeApsDatasources.
- Support API DescribeApsHiveWorkload.
- Support API DescribeApsJobDetail.
- Support API DescribeApsJobs.
- Support API DescribeApsMigrationWorkloads.
- Support API DescribeApsProgress.
- Support API DescribeAvailableAdvices.
- Support API DescribeBadSqlDetection.
- Support API DescribeCompactionServiceSwitch.
- Support API DescribeControllerDetection.
- Support API DescribeEssdCacheConfig.
- Support API DescribeExecutorDetection.
- Support API DescribeInclinedNodes.
- Support API DescribeKernelVersion.
- Support API DescribeLakeCacheSize.
- Support API DescribeOperatorPermission.
- Support API DescribeOversizeNonPartitionTableInfos.
- Support API DescribeSparkAppDiagnosisInfo.
- Support API DescribeSparkAppType.
- Support API DescribeSparkSQLDiagnosisAttribute.
- Support API DescribeSparkSQLDiagnosisList.
- Support API DescribeTableDetail.
- Support API DescribeTablePartitionDiagnose.
- Support API DescribeWorkerDetection.
- Support API DisableAdviceService.
- Support API DownloadInstanceCACertificate.
- Support API EnableAdviceService.
- Support API ExecuteSparkReplStatement.
- Support API ExecuteSparkWarehouseBatchSQL.
- Support API GetApsManagedDatabases.
- Support API GetCreateTableSQL.
- Support API GetLakeStorage.
- Support API GetSparkReplSession.
- Support API GetSparkReplStatement.
- Support API GetSparkWarehouseBatchSQL.
- Support API GrantOperatorPermission.
- Support API KillProcess.
- Support API ListApsLifecycleStrategy.
- Support API ListApsOptimizationStrategy.
- Support API ListApsOptimizationTasks.
- Support API ListLakeStorages.
- Support API ListResultExportJobHistory.
- Support API ListSparkWarehouseBatchSQL.
- Support API ListTagResources.
- Support API ModifyApsDatasoure.
- Support API ModifyApsJob.
- Support API ModifyApsSlsADBJob.
- Support API ModifyApsWorkloadName.
- Support API ModifyClickhouseEngine.
- Support API ModifyCompactionServiceSwitch.
- Support API ModifyDBClusterResourceGroup.
- Support API ModifyDBClusterVip.
- Support API ModifyEssdCacheConfig.
- Support API ModifyLakeCacheSize.
- Support API ModifyUserEniVswitchOptions.
- Support API RevokeOperatorPermission.
- Support API StartApsJob.
- Support API StartSparkReplSession.
- Support API SubmitResultExportJob.
- Support API SuspendApsJob.
- Support API UpdateLakeStorage.
- Delete API GetSparkDefinitions.
- Delete API RenameSparkTemplateFile.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterPerformance: update response param.
- Update API DescribeDiagnosisRecords: update response param.
- Update API DescribePatternPerformance: update response param.
- Update API ListSparkApps: add param Filters.


2024-10-16 Version: 1.3.15
- Update API CreateDBResourceGroup: add param AutoStopInterval.
- Update API DescribeDBResourceGroup: update response param.
- Update API DescribePerformanceViewAttribute: update response param.
- Update API ModifyDBResourceGroup: add param AutoStopInterval.
- Update API ModifyDBResourceGroup: add param Status.


2024-10-12 Version: 1.3.14
- Update API DescribeBackups: update response param.
- Update API ModifyBackupPolicy: update param PreferredBackupPeriod.


2024-10-11 Version: 1.3.13
- Update API CreateDBResourceGroup: add param MaxGpuQuantity.
- Update API CreateDBResourceGroup: add param MinGpuQuantity.
- Update API CreateDBResourceGroup: add param SpecName.
- Update API CreateDBResourceGroup: add param TargetResourceGroupName.
- Update API DescribeClusterAccessWhiteList: add param RegionId.
- Update API DescribeDBResourceGroup: update response param.
- Update API ModifyDBResourceGroup: add param MaxGpuQuantity.
- Update API ModifyDBResourceGroup: add param MinGpuQuantity.
- Update API ModifyDBResourceGroup: add param SpecName.
- Update API ModifyDBResourceGroup: add param TargetResourceGroupName.


2024-09-24 Version: 1.3.12
- Update API CreateDBCluster: add param CloneSourceRegionId.
- Update API CreateDBCluster: update param ProductForm.
- Update API DescribeDiagnosisRecords: update response param.
- Update API ModifyDBCluster: add param ProductForm.


2024-08-20 Version: 1.3.11
- Update API GetTableObjects: update param PageNumber.
- Update API GetTableObjects: update param PageSize.
- Update API ModifyAuditLogConfig: add param EngineType.


2024-08-14 Version: 1.3.10
- Update API CreateDBResourceGroup: add param Engine.
- Update API CreateDBResourceGroup: add param EngineParams.
- Update API DescribeDBResourceGroup: update response param.
- Update API ModifyDBResourceGroup: add param EngineParams.


2024-08-09 Version: 1.3.9
- Generated python 2021-12-01 for adb.

2024-08-06 Version: 1.3.8
- Update API DescribeSQLPatterns: update response param.


2024-07-24 Version: 1.3.7
- Update API DescribeRegions: add param RegionId.
- Update API GetTable: update param DbName.
- Update API GetTable: update param TableName.


2024-07-01 Version: 2.0.0
- Support API CreatePerformanceView.
- Support API DeletePerformanceView.
- Support API DescribeExcessivePrimaryKeys.
- Support API DescribePerformanceViewAttribute.
- Support API DescribePerformanceViews.
- Support API ModifyPerformanceView.
- Update API AllocateClusterPublicConnection: add param Engine.
- Update API CreateAccount: add param Engine.
- Update API CreateDBCluster: add param DiskEncryption.
- Update API CreateDBCluster: add param KmsId.
- Update API DeleteAccount: add param Engine.
- Update API DescribeAccounts: add param Engine.
- Update API DescribeAccounts: update response param.
- Update API DescribeApsActionLogs: delete param Action.
- Update API DescribeApsActionLogs: update response param.
- Update API DescribeClusterNetInfo: add param Engine.
- Update API DescribeClusterNetInfo: update response param.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusterHealthStatus: update response param.
- Update API DescribeDBClusters: update response param.
- Update API DescribeDownloadRecords: update response param.
- Update API DescribeJobResourceUsage: update response param.
- Update API DescribeSQLPatterns: update response param.
- Update API ModifyAccountDescription: add param Engine.
- Update API ReleaseClusterPublicConnection: add param Engine.
- Update API ResetAccountPassword: add param Engine.
- Update API SubmitSparkApp: update param AppName.


2024-05-10 Version: 1.3.5
- Update API CreateOssSubDirectory: update param DBClusterId.


2024-05-10 Version: 1.3.5
- Update API CreateOssSubDirectory: update param DBClusterId.


2024-05-09 Version: 1.3.4
- Update API CreateDBCluster: add param ProductForm.
- Update API CreateDBCluster: add param ReservedNodeCount.
- Update API CreateDBCluster: add param ReservedNodeSize.
- Update API CreateDBCluster: update param ComputeResource.
- Update API CreateDBCluster: update param StorageResource.
- Update API DescribeDBClusterAttribute: update response param.
- Update API DescribeDBClusters: add param DBClusterVersion.
- Update API DescribeDBClusters: add param ProductVersion.
- Update API DescribeDBClusters: update response param.
- Update API ExistRunningSQLEngine: update response param.
- Update API ModifyDBCluster: add param ReservedNodeCount.
- Update API ModifyDBCluster: add param ReservedNodeSize.
- Update API ModifyDBCluster: update param ComputeResource.
- Update API ModifyDBCluster: update param StorageResource.


2024-04-10 Version: 1.3.3
- Update API DescribeApsResourceGroups: add param RegionId.
- Update API DescribeApsResourceGroups: add param WorkloadId.


2024-04-09 Version: 1.3.2
- Generated python 2021-12-01 for adb.

2024-03-25 Version: 1.3.1
- Update API CreateDBResourceGroup: add param Rules.
- Update API DescribeDBResourceGroup: update response param.
- Update API ModifyDBResourceGroup: add param Rules.


2024-03-23 Version: 1.3.0
- Support API DescribeDBClusterSpaceSummary.
- Update API CreateDBResourceGroup: add param EnableSpot.
- Update API DescribeApsActionLogs: update response param.
- Update API DescribeClusterResourceDetail: update response param.
- Update API DescribeDBResourceGroup: add param RegionId.
- Update API DescribeDBResourceGroup: update response param.
- Update API ModifyDBResourceGroup: add param EnableSpot.


2024-03-01 Version: 1.2.9
- Update API CreateDBResourceGroup: add param EnableSpot.
- Update API DescribeApsActionLogs: update response param.
- Update API DescribeClusterResourceDetail: update response param.
- Update API DescribeDBResourceGroup: add param RegionId.
- Update API DescribeDBResourceGroup: update response param.
- Update API ModifyDBResourceGroup: add param EnableSpot.


2024-01-26 Version: 1.2.8
- Update API CreateDBResourceGroupadd EnableSpot param.
- Update API DescribeApsActionLogsupdate response param.
- Update API DescribeClusterResourceDetailupdate response param.
- Update API DescribeDBResourceGroupupdate response param.
- Update API ModifyDBResourceGroupadd EnableSpot param.


2024-01-18 Version: 1.2.7
- Generated python 2021-12-01 for adb.

2024-01-05 Version: 1.2.6
- Generated python 2021-12-01 for adb.

2023-12-21 Version: 1.2.5
- Generated python 2021-12-01 for adb.

2023-12-20 Version: 1.2.4
- Generated python 2021-12-01 for adb.

2023-12-19 Version: 1.2.3
- Generated python 2021-12-01 for adb.

2023-12-13 Version: 1.2.2
- Generated python 2021-12-01 for adb.

2023-12-12 Version: 1.2.1
- Generated python 2021-12-01 for adb.

2023-12-06 Version: 1.2.0
- Generated python 2021-12-01 for adb.

2023-11-25 Version: 1.1.1
- Generated python 2021-12-01 for adb.

2023-11-21 Version: 1.1.0
- Generated python 2021-12-01 for adb.

2023-02-22 Version: 1.0.0
- Release API for spark log analyze task.

