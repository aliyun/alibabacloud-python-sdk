2026-01-27 Version: 3.0.0
- Support API ConfigureBackupSetInfo.
- Support API DescribeBakDataSourceStorageAccessInfo.
- Support API DescribeCostInfoByDbsInstance.
- Support API RetryDownloadTask.
- Update API CreateDownload: add request parameters AdminDatabase.
- Update API CreateDownload: add request parameters ClusterName.
- Update API CreateDownload: add request parameters IsCluster.
- Update API CreateDownload: add request parameters IsPhysical.
- Update API CreateDownload: add request parameters PrimaryKeyTypeOnly.
- Update API CreateDownload: add request parameters UseZstd.
- Update API DescribeBackupPolicy: add response parameters Body.Data.AdvanceIncPolicies.
- Update API DescribeBackupPolicy: add response parameters Body.Data.AdvanceDataPolicies.$.StorageClass.
- Update API DescribeBackupPolicy: add response parameters Body.Data.AdvanceLogPolicies.$.FilterKey.
- Update API DescribeBackupPolicy: add response parameters Body.Data.AdvanceLogPolicies.$.FilterType.
- Update API DescribeBackupPolicy: add response parameters Body.Data.AdvanceLogPolicies.$.FilterValue.
- Update API DescribeBackupPolicy: add response parameters Body.Data.AdvanceLogPolicies.$.PolicyId.
- Update API DescribeBackupPolicy: delete response parameters Body.Data.AdvanceDataPolicies.$.StrategyId.
- Update API DescribeBackupPolicy: update response parameters Body.Data.AdvanceLogPolicies.$.EnableLogBackup' type has changed.
- Update API DescribeBackupPolicy: update response parameters Body.Data.AdvanceLogPolicies.$.EnableLogBackup' format has changed.
- Update API DescribeBackupPolicy: delete response parameters Body.Data.AdvanceLogPolicies.$.StrategyId.
- Update API DescribeDBTablesRecoveryBackupSet: add request parameters ClusterName.
- Update API DescribeDBTablesRecoveryState: add request parameters ClusterName.
- Update API DescribeDBTablesRecoveryTimeRange: add request parameters ClusterName.
- Update API DescribeDownloadBackupSetStorageInfo: add request parameters ClusterName.
- Update API DescribeDownloadSupport: add request parameters ClusterName.
- Update API DescribeDownloadTask: add request parameters ClusterName.
- Update API ModifyBackupPolicy: add request parameters AdvanceIncPolicies.
- Update API ModifyBackupPolicy: add request parameters AdvanceLogPolicies.
- Update API ModifyBackupPolicy: add request parameters BackupMethod.
- Update API ModifyBackupPolicy: add request parameters BackupPriority.
- Update API ModifyBackupPolicy: add request parameters BackupRetentionPolicyOnClusterDeletion.
- Update API ModifyBackupPolicy: add request parameters Category.
- Update API ModifyBackupPolicy: add request parameters EnableIncBackup.
- Update API ModifyBackupPolicy: add request parameters AdvanceDataPolicies.$.OnlyPreserveOneEachDay.
- Update API ModifyBackupPolicy: add request parameters AdvanceDataPolicies.$.StorageClass.
- Update API ModifyBackupPolicy: add response parameters Body.Data.AdvanceIncPolicies.
- Update API ModifyBackupPolicy: add response parameters Body.Data.AdvanceLogPolicies.
- Update API ModifyBackupPolicy: add response parameters Body.Data.BackupMethod.
- Update API ModifyBackupPolicy: add response parameters Body.Data.BackupPriority.
- Update API ModifyBackupPolicy: add response parameters Body.Data.BackupRetentionPolicyOnClusterDeletion.
- Update API ModifyBackupPolicy: add response parameters Body.Data.Category.
- Update API ModifyBackupPolicy: add response parameters Body.Data.EnableIncBackup.
- Update API ModifyBackupPolicy: add response parameters Body.Data.AdvanceDataPolicies.$.OnlyPreserveOneEachDay.
- Update API ModifyBackupPolicy: add response parameters Body.Data.AdvanceDataPolicies.$.StorageClass.
- Update API ModifyBackupPolicy: delete request parameters AdvanceDataPolicies.$.FilterType-copy.
- Update API ModifyDBTablesRecoveryState: add request parameters ClusterName.
- Update API SupportDBTableRecovery: add request parameters ClusterName.


2024-05-20 Version: 2.1.0
- Support API CreateAdvancedPolicy.
- Support API ModifyBackupPolicy.


2024-05-17 Version: 2.0.1
- Update API DescribeBackupPolicy: update response param.


2024-04-29 Version: 2.0.0
- Support API DescribeBackupDataList.
- Support API DescribeBackupPolicy.
- Delete API CreateSandboxInstance.
- Update API ChangeResourceGroup: add param RegionCode.


2023-08-21 Version: 1.0.4
- Generated python 2021-01-01 for Dbs.

2023-07-26 Version: 1.0.3
- Update Sdk.

2023-01-31 Version: 1.0.2
- Update Sdk.

2022-12-14 Version: 1.0.1
- Update Sdk.

2022-07-25 Version: 1.0.0
- Generated python 2021-01-01 for Dbs.

