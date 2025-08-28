2025-08-28 Version: 6.1.0
- Support API CreateTairKVCacheVNode.
- Support API TransformToEcs.
- Update API DescribeInstances: add request parameters NodeType.
- Update API DescribePrice: add request parameters SecondaryZoneId.
- Update API DescribeTairKVCacheInferInstances: add response parameters Body.Instances.$.AckId.
- Update API DescribeTairKVCacheInferInstances: add response parameters Body.Instances.$.VNodeCount.


2025-07-30 Version: 6.0.1
- Generated python 2015-01-01 for R-kvstore.

2025-07-09 Version: 6.0.0
- Support API DeleteBackup.
- Support API ModifyBackupExpireTime.
- Delete API DescribeTasks.
- Update API CreateBackup: add request parameters BackupRetentionPeriod.
- Update API CreateGlobalDistributeCache: add response parameters Body.GlobalInstanceId.
- Update API CreateGlobalDistributeCache: add response parameters Body.InstanceId.
- Update API DescribeBackups: add response parameters Body.Backups.$.ExpectExpireTime.
- Update API DescribeClusterBackupList: add response parameters Body.ClusterBackups.$.ExpectExpireTime.
- Update API DescribeHistoryMonitorValues: add request parameters Type.
- Update API DescribeTairKVCacheInferInstanceAttribute: add response parameters Body.Instances.$.ComputeUnitNum.
- Update API DescribeTairKVCacheInferInstanceAttribute: add response parameters Body.Instances.$.Model.
- Update API DescribeTairKVCacheInferInstanceAttribute: add response parameters Body.Instances.$.ModelServiceNum.
- Update API DescribeTairKVCacheInferInstanceAttribute: delete response parameters Body.Instances.$.ReserveGpuNum.
- Update API DescribeTairKVCacheInferInstanceAttribute: delete response parameters Body.Instances.$.SecurityGroupId.
- Update API DescribeTairKVCacheInferInstances: add response parameters Body.Instances.$.ComputeUnitNum.
- Update API DescribeTairKVCacheInferInstances: add response parameters Body.Instances.$.Model.
- Update API DescribeTairKVCacheInferInstances: add response parameters Body.Instances.$.ModelServiceNum.
- Update API DescribeTairKVCacheInferInstances: add response parameters Body.Instances.$.VNodeName.
- Update API DescribeTairKVCacheInferInstances: delete response parameters Body.Instances.$.ModuleName.
- Update API DescribeTairKVCacheInferInstances: delete response parameters Body.Instances.$.ReserveGpuNum.
- Update API DescribeTairKVCacheInferInstances: delete response parameters Body.Instances.$.UsedGpuNum.


2025-04-01 Version: 5.0.0
- Support API DescribeTairKVCacheInferInstanceAttribute.
- Support API DescribeTairKVCacheInferInstances.
- Update API DeleteShardingNode: add request parameters EffectiveTime.
- Update API DescribeAvailableResource: add response parameters Body.AvailableZones.$.IsMainSale.
- Update API DescribeBackupTasks: add response parameters Body.BackupJobs.$.Progress.
- Update API DescribeClusterBackupList: add request parameters NoShardBackup.
- Update API DescribeHistoryTasks: update response parameters Body.Items.$.Status' type has changed.
- Update API DescribeHistoryTasks: update response parameters Body.Items.$.Status' format has changed.
- Update API DescribeInstanceAttribute: add response parameters Body.Instances.$.AutoSecondaryZone.
- Update API DescribePrice: add request parameters EngineVersion.
- Update API DescribeTairKVCacheCustomInstanceAttribute: add response parameters Body.UseEni.
- Update API DescribeTairKVCacheCustomInstances: add request parameters PrivateIp.
- Update API DescribeTairKVCacheCustomInstances: add response parameters Body.Instances.$.PrivateIp.
- Update API DescribeTairKVCacheCustomInstances: add response parameters Body.Instances.$.UseEni.
- Update API MigrateToOtherZone: add request parameters ReadOnlyCount.
- Update API MigrateToOtherZone: add request parameters ReplicaCount.
- Update API MigrateToOtherZone: add request parameters SlaveReadOnlyCount.
- Update API MigrateToOtherZone: add request parameters SlaveReplicaCount.
- Update API ModifyInstanceAutoRenewalAttribute: add request parameters Product.


2024-12-17 Version: 4.3.0
- Support API CancelActiveOperationTasks.
- Support API CreateTCInstance.
- Support API DescribeTairKVCacheCustomInstanceAttribute.
- Support API DescribeTairKVCacheCustomInstanceHistoryMonitorValues.
- Support API DescribeTairKVCacheCustomInstances.
- Support API MasterNodeShutDownFailOver.
- Support API ModifyInstanceBandwidth.
- Support API ModifyTairKVCacheCustomInstanceAttribute.
- Support API ModifyTaskInfo.
- Support API ResetTairKVCacheCustomInstancePassword.
- Support API ResizeTairKVCacheCustomInstanceDisk.
- Support API RestartTairKVCacheCustomInstance.
- Support API StartTairKVCacheCustomInstance.
- Support API StopTairKVCacheCustomInstance.
- Support API SwitchInstanceZoneFailOver.
- Update API CreateInstance: add param ReplicaCount.
- Update API CreateInstance: add param SlaveReplicaCount.
- Update API CreateInstance: update param SlaveReadOnlyCount.
- Update API CreateTairInstance: add param ConnectionStringPrefix.
- Update API CreateTairInstance: add param ReplicaCount.
- Update API CreateTairInstance: add param SlaveReplicaCount.
- Update API DescribeAvailableResource: update response param.
- Update API DescribeBackups: update param PageSize.
- Update API DescribeInstanceAttribute: update response param.
- Update API DescribeInstanceConfig: update response param.
- Update API DescribeInstances: update response param.
- Update API DescribeRoleZoneInfo: update param PageSize.
- Update API ModifyInstanceConfig: add param ParamNoLooseSentinelEnabled.
- Update API ModifyInstanceConfig: add param ParamNoLooseSentinelPasswordFreeAccess.
- Update API ModifyInstanceConfig: add param ParamNoLooseSentinelPasswordFreeCommands.
- Update API ModifyInstanceConfig: add param ParamReplMode.
- Update API ModifyInstanceConfig: add param ParamSemisyncReplTimeout.
- Update API ModifyInstanceConfig: add param ParamSentinelCompatEnable.
- Update API ModifyInstanceConfig: update param Config.
- Update API ModifyInstanceSpec: add param ReplicaCount.
- Update API ModifyInstanceSpec: add param SlaveReplicaCount.
- Update API ModifyInstanceSpec: add param Storage.
- Update API ModifyInstanceSpec: add param StorageType.
- Update API TransformToPrePaid: add param AutoRenew.
- Update API TransformToPrePaid: add param AutoRenewPeriod.


2024-08-28 Version: 4.2.1
- Update API CreateTairInstance: update param EngineVersion.
- Update API DescribePrice: add param ShardCount.
- Update API ModifyInstanceParameter: update param RegionId.
- Update API ModifyParameterGroup: update param ParameterGroupName.


2024-07-19 Version: 4.2.0
- Support API DescribeActiveOperationTasks.
- Support API ModifyActiveOperationTasks.
- Update API CreateAccount: add param SourceBiz.
- Update API DeleteAccount: add param SourceBiz.
- Update API DeleteAccount: update response param.
- Update API DescribeInstances: update response param.
- Update API GrantAccountPrivilege: add param SourceBiz.
- Update API ModifyAccountDescription: add param SourceBiz.
- Update API ModifyAccountPassword: add param SourceBiz.
- Update API ResetAccountPassword: add param SourceBiz.


2024-06-19 Version: 4.1.0
- Support API CreateParameterGroup.
- Support API DeleteParameterGroup.
- Support API DescribeParameterGroup.
- Support API DescribeParameterGroupSupportParam.
- Support API DescribeParameterGroupTemplateList.
- Support API DescribeParameterGroups.
- Support API ModifyDBInstanceAutoUpgrade.
- Support API ModifyParameterGroup.
- Update API CreateInstance: add param RecoverConfigMode.
- Update API CreateInstance: add param SlaveReadOnlyCount.
- Update API CreateTairInstance: add param RecoverConfigMode.
- Update API DescribeBackups: update response param.
- Update API DescribeClusterBackupList: update response param.
- Update API ModifyBackupPolicy: update param BackupRetentionPeriod.


2024-05-08 Version: 4.0.1
- Update API DescribeHistoryMonitorValues: add param NodeRole.


2024-05-06 Version: 4.0.0
- Update API CreateGlobalDistributeCache: add param EffectiveTime.
- Update API CreateTairInstance: add param RestoreTime.
- Update API DescribeBackups: update response param.
- Update API DescribeEngineVersion: update response param.
- Update API DescribePrice: update response param.


2024-04-07 Version: 3.0.1
- Update API DescribePrice: update response param.
- Update API LockDBInstanceWrite: update param AccessKeyId.
- Update API UnlockDBInstanceWrite: update param AccessKeyId.


2024-03-30 Version: 3.0.0
- Update API DescribeBackupTasks: update response param.
- Update API DescribeBackups: update param BackupId.
- Update API DescribeBackups: update param BackupJobId.
- Update API DescribeClusterBackupList: update param ClusterBackupId.
- Update API DescribePrice: update response param.
- Update API ModifyInstanceSpec: add param NodeType.


2024-02-28 Version: 2.25.6
- Update API DescribeClusterBackupList: update param ClusterBackupId.
- Update API DescribePrice: update response param.


2024-01-30 Version: 2.25.5
- Update API ModifyBackupPolicyadd BackupRetentionPeriod param.
- Update API RenewInstanceadd AutoRenew param.


2024-01-29 Version: 2.25.4
- Update API CreateTairInstanceadd SlaveReadOnlyCount param.
- Update API DescribeBackupsupdate response param.
- Update API DescribeClusterBackupListupdate response param.
- Update API ModifyInstanceSpecadd SlaveReadOnlyCount param.


2024-01-22 Version: 2.25.3
- Generated python 2015-01-01 for R-kvstore.

2024-01-18 Version: 2.25.2
- Generated python 2015-01-01 for R-kvstore.

2024-01-18 Version: 2.25.1
- Generated python 2015-01-01 for R-kvstore.

2024-01-12 Version: 2.25.0
- Generated python 2015-01-01 for R-kvstore.

2023-12-27 Version: 2.24.1
- Generated python 2015-01-01 for R-kvstore.

2023-12-13 Version: 2.24.0
- Generated python 2015-01-01 for R-kvstore.

2023-11-21 Version: 2.23.0
- Generated python 2015-01-01 for R-kvstore.

2023-10-18 Version: 2.22.1
- Generated python 2015-01-01 for R-kvstore.

2023-09-20 Version: 2.22.0
- Generated python 2015-01-01 for R-kvstore.

2023-08-31 Version: 2.21.2
- Generated python 2015-01-01 for R-kvstore.

2023-08-30 Version: 2.21.1
- Generated python 2015-01-01 for R-kvstore.

2023-08-30 Version: 2.21.1
- Generated python 2015-01-01 for R-kvstore.

2023-08-24 Version: 2.21.0
- Generated python 2015-01-01 for R-kvstore.

2022-11-18 Version: 2.20.7
- Update python sdk.

2022-11-09 Version: 2.20.6
- Update python sdk.

2022-06-15 Version: 2.20.5
- Update by sdk platform.

2022-03-23 Version: 2.20.4
- Update by sdk platform.

2022-03-15 Version: 2.20.3
- Update by sdk platform.

2022-01-12 Version: 1.0.6
- Update sdk by platform.

2022-01-11 Version: 1.0.5
- Update mongodb sdk.

2021-05-24 Version: 1.0.4
- Generated python 2015-01-01 for R-kvstore.

2021-03-23 Version: 1.0.3
- Generated python 2015-01-01 for R-kvstore.

2021-03-11 Version: 1.0.2
- AMP Version Change.

2021-01-28 Version: 1.0.1
- AMP Version Change.

2020-12-30 Version: 1.0.0
- AMP Version Change.

2020-12-30 Version: 1.0.0
- AMP Version Change.

