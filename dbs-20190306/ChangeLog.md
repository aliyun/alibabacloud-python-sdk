2026-03-19 Version: 1.0.3
- Update API ConfigureBackupPlan: add request parameters BackupStorageEncryptMethod.
- Update API ConfigureBackupPlan: add request parameters EnableMysqlPhysicalBackupBinlog.
- Update API ConfigureBackupPlan: add request parameters EnableSourceEndpointSsl.
- Update API ConfigureBackupPlan: add request parameters SourceEndpointOracleHome.
- Update API ConfigureBackupPlan: add request parameters SslCaPem.
- Update API CreateRestoreTask: add request parameters AutoOpenDatabase.
- Update API CreateRestoreTask: add request parameters AutoShutdownDatabase.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceClass.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceDatabaseVersion.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceRegion.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceStorageSize.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceType.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceVSwitch.
- Update API CreateRestoreTask: add request parameters DestDatabaseInstanceVpc.
- Update API CreateRestoreTask: add request parameters EnableDestinationEndpointSsl.
- Update API CreateRestoreTask: add request parameters RestoreDestinationMode.
- Update API CreateRestoreTask: add request parameters SslCaPem.
- Update API DescribeBackupPlanList: add request parameters BackupMethod.
- Update API DescribeBackupPlanList: add request parameters ShowBackupStrategyInfo.
- Update API DescribeBackupPlanList: add request parameters ShowRecoverTimeRange.
- Update API DescribeBackupPlanList: add request parameters ShowStorageStrategyInfo.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.BackupGatewayIdentifier.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.BackupPlanRegion.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.EnableMysqlPhysicalBackupBinLog.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.IncrementBackupRetentionPeriod.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.IncrementDuplicationArchivePeriod.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.IncrementDuplicationInfrequentAccessPeriod.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.InstanceChargeType.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.InstanceExpiredTimestamp.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.LogBackupRetentionPeriod.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.LogDuplicationArchivePeriod.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.LogDuplicationInfrequentAccessPeriod.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.SourceEndpointEnableSsl.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.SourceEndpointHost.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.SourceEndpointPort.
- Update API DescribeBackupPlanList: add response parameters Body.Items.$.StorageEncryptMethod.
- Update API DescribeFullBackupList: add request parameters BackupSetStatus.
- Update API DescribeFullBackupList: add request parameters ShowProgress.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.BackupGatewayIdentifier.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.CrossAliyunId.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.CrossRoleName.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.LogicalFullBackupProgress.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.LogicalStructureBackupProgress.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointEnableSsl.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointHost.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointInstanceId.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointInstanceType.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointPort.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointRegion.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.SourceEndpointUserName.
- Update API DescribeFullBackupList: add response parameters Body.Items.$.StorageEncryptMethod.
- Update API DescribeIncrementBackupList: add response parameters Body.Items.$.SourceEndpointHost.
- Update API DescribeIncrementBackupList: add response parameters Body.Items.$.SourceEndpointInstanceId.
- Update API DescribeIncrementBackupList: add response parameters Body.Items.$.SourceEndpointInstanceType.
- Update API DescribeIncrementBackupList: add response parameters Body.Items.$.SourceEndpointPort.
- Update API DescribeIncrementBackupList: add response parameters Body.Items.$.SourceEndpointRegion.
- Update API DescribeRestoreRangeInfo: add response parameters Body.Items.$.BackupSourceHost.
- Update API DescribeRestoreRangeInfo: add response parameters Body.Items.$.BackupSourceInstanceId.
- Update API DescribeRestoreRangeInfo: add response parameters Body.Items.$.BackupSourceInstanceType.
- Update API DescribeRestoreRangeInfo: add response parameters Body.Items.$.BackupSourcePort.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.BackupGatewayIdentifier.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.BackupSourceOssRegion.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.DestinationEndpointEnableSsl.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.DestinationEndpointHost.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.DestinationEndpointPort.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.PhysicalBackupRecoverProgress.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.PhysicalDatabaseOnlineProgress.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.PhysicalFullAndIncrementBackupRecoverProgress.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.PhysicalFullBackupRecoverProgress.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.PhysicalIncrementBackupRecoverProgress.
- Update API DescribeRestoreTaskList: add response parameters Body.Items.$.RestoreDestinationMode.
- Update API DisableBackupLog: add request parameters DisableMysqlPhysicalBackupBinlogOnly.
- Update API EnableBackupLog: add request parameters EnableMysqlPhysicalBackupBinlog.
- Update API ModifyBackupSourceEndpoint: add request parameters EnableSourceEndpointSsl.
- Update API ModifyBackupSourceEndpoint: add request parameters SourceEndpointOracleHome.
- Update API ModifyBackupSourceEndpoint: add request parameters SslCaPem.
- Update API ModifyStorageStrategy: add request parameters BackupStorageEncryptMethod.
- Update API ModifyStorageStrategy: add request parameters IncrementBackupRetentionPeriod.
- Update API ModifyStorageStrategy: add request parameters IncrementDuplicationArchivePeriod.
- Update API ModifyStorageStrategy: add request parameters IncrementDuplicationInfrequentAccessPeriod.
- Update API ModifyStorageStrategy: add request parameters LogBackupRetentionPeriod.
- Update API ModifyStorageStrategy: add request parameters LogDuplicationArchivePeriod.
- Update API ModifyStorageStrategy: add request parameters LogDuplicationInfrequentAccessPeriod.


2025-12-01 Version: 1.0.2
- Update API InitializeDbsServiceLinkedRole: add request parameters RegionId.


2022-07-28 Version: 1.0.1
- Automatically generate sdk tasks.

2020-12-30 Version: 1.0.0
- AMP Version Change.

