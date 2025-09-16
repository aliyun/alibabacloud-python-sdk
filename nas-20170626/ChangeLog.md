2025-09-16 Version: 3.1.1
- Generated python 2017-06-26 for NAS.

2025-09-16 Version: 3.0.3
- Generated python 2017-06-26 for NAS.

2025-09-15 Version: 3.0.2
- Generated python 2017-06-26 for NAS.

2025-07-01 Version: 3.0.0
- Delete API AddTags.
- Delete API RemoveTags.
- Update API CreateDataFlowTask: add request parameters Includes.
- Update API CreateFileSystem: add request parameters Tag.
- Update API CreateLifecyclePolicy: delete request parameters FsetIds.
- Update API CreateLifecyclePolicy: delete request parameters LifecycleRuleType.
- Update API DescribeDataFlowTasks: add response parameters Body.TaskInfo.$.Includes.
- Update API DescribeFileSystems: add response parameters Body.FileSystems.$.VscTarget.
- Update API DescribeFileSystems: delete response parameters Body.FileSystems.$.SecondaryBandwidth.
- Update API DescribeFileSystems: delete response parameters Body.FileSystems.$.SecondaryCapacity.
- Update API DescribeLifecyclePolicies: delete request parameters FileSystemType.
- Update API DescribeLifecyclePolicies: delete request parameters FsetId.
- Update API DescribeLifecyclePolicies: delete response parameters Body.LifecyclePolicies.$.EnableLifecycle.
- Update API DescribeLifecyclePolicies: delete response parameters Body.LifecyclePolicies.$.FsetIds.
- Update API DescribeLifecyclePolicies: delete response parameters Body.LifecyclePolicies.$.LifecycleRuleType.
- Update API DescribeLifecyclePolicies: delete response parameters Body.LifecyclePolicies.$.Status.
- Update API DescribeMountTargets: add response parameters Body.MountTargets.$.Tags.
- Update API ModifyLifecyclePolicy: delete request parameters EnableLifecycle.
- Update API ModifyLifecyclePolicy: delete request parameters FsetIds.


2025-03-19 Version: 2.5.3
- Update API CreateFile: update param OwnerAccessInheritable.
- Update API CreateLifecyclePolicy: add param FsetIds.
- Update API CreateLifecyclePolicy: add param LifecycleRuleType.
- Update API CreateLifecyclePolicy: update param LifecycleRuleName.
- Update API CreateLifecyclePolicy: update param StorageType.
- Update API DescribeFileSystems: update response param.
- Update API DescribeLifecyclePolicies: add param FileSystemType.
- Update API DescribeLifecyclePolicies: add param FsetId.
- Update API DescribeLifecyclePolicies: update param StorageType.
- Update API DescribeLifecyclePolicies: update response param.
- Update API ModifyLifecyclePolicy: add param EnableLifecycle.
- Update API ModifyLifecyclePolicy: add param FsetIds.
- Update API ModifyLifecyclePolicy: update param LifecycleRuleName.
- Update API ModifyLifecyclePolicy: update param StorageType.


2025-01-20 Version: 2.5.2
- Update API DescribeFilesets: add param OrderByField.
- Update API DescribeFilesets: add param SortOrder.


2024-12-19 Version: 2.5.1
- Update API DescribeMountTargets: update response param.
- Update API DescribeSnapshots: update response param.


2024-10-28 Version: 2.5.0
- Support API CancelFilesetQuota.
- Support API SetFilesetQuota.


2024-10-24 Version: 2.4.1
- Update API CreateFileset: add param Quota.
- Update API CreateFileset: update param FileSystemPath.
- Update API DescribeFilesets: update param Filters.
- Update API DescribeFilesets: update response param.


2024-10-17 Version: 2.4.0
- Support API CancelDataFlowSubTask.
- Support API CreateDataFlowSubTask.
- Support API DescribeDataFlowSubTasks.
- Update API CreateMountTarget: update response param.
- Update API DescribeFileSystems: update param FileSystemType.
- Update API DescribeFileSystems: update response param.


2024-09-24 Version: 2.3.0
- Support API CancelDataFlowSubTask.
- Support API CreateDataFlowSubTask.
- Support API DescribeDataFlowSubTasks.


2024-09-09 Version: 2.2.4
- Update API ApplyDataFlowAutoRefresh: update response param.
- Update API CancelAutoSnapshotPolicy: update response param.
- Update API CancelDataFlowAutoRefresh: update response param.
- Update API CancelDataFlowTask: update response param.
- Update API CreateAccessGroup: update response param.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API CreateDataFlowTask: add param CreateDirIfNotExist.
- Update API CreateDataFlowTask: add param DstDirectory.
- Update API CreateDataFlowTask: update param TaskAction.
- Update API DeleteAutoSnapshotPolicy: update response param.
- Update API DeleteDataFlow: update response param.
- Update API DeleteFileSystem: update response param.
- Update API DeleteSnapshot: update response param.
- Update API DescribeDataFlowTasks: update response param.
- Update API DescribeDataFlows: update response param.
- Update API DescribeLogAnalysis: update param FileSystemType.
- Update API GetRecycleBinAttribute: update response param.
- Update API ModifyAutoSnapshotPolicy: update response param.
- Update API ModifyDataFlowAutoRefresh: update response param.
- Update API OpenNASService: update response param.
- Update API SetDirQuota: update response param.
- Update API StartDataFlow: update response param.
- Update API StopDataFlow: update response param.


2024-07-08 Version: 2.2.3
- Update API DescribeFileSystems: update response param.
- Update API ModifyFileSystem: add param Options.


2024-07-08 Version: 2.2.3
- Update API DescribeFileSystems: update response param.
- Update API ModifyFileSystem: add param Options.


2024-06-05 Version: 2.2.2
- Update API CreateFileset: add param DeletionProtection.
- Update API CreateFileset: update response param.
- Update API DescribeAutoSnapshotPolicies: update param FileSystemType.
- Update API DescribeAutoSnapshotPolicies: update response param.
- Update API DescribeDirQuotas: update response param.
- Update API DescribeFilesets: update response param.
- Update API DescribeLogAnalysis: add param FileSystemType.
- Update API DescribeSnapshots: update param FileSystemType.
- Update API DescribeSnapshots: update response param.
- Update API ModifyDataFlow: update param Throughput.
- Update API ModifyDataFlow: update response param.
- Update API ModifyFileset: add param DeletionProtection.
- Update API ModifyFileset: update response param.


2024-03-25 Version: 2.2.1
- Update API CreateLifecyclePolicy: update param LifecycleRuleName.
- Update API CreateLifecyclePolicy: update param StorageType.
- Update API CreateLifecycleRetrieveJob: add param StorageType.
- Update API DescribeFileSystems: update response param.
- Update API DescribeLifecyclePolicies: add param StorageType.
- Update API DescribeLifecyclePolicies: update response param.
- Update API GetDirectoryOrFileProperties: update response param.
- Update API ListDirectoriesAndFiles: update param StorageType.
- Update API ListDirectoriesAndFiles: update response param.
- Update API ListLifecycleRetrieveJobs: add param StorageType.
- Update API ListLifecycleRetrieveJobs: update response param.
- Update API ModifyLifecyclePolicy: update param LifecycleRuleName.
- Update API ModifyLifecyclePolicy: update param StorageType.


2024-03-21 Version: 2.2.0
- Support API CreateAccessPoint.
- Support API CreateDir.
- Support API DeleteAccessPoint.
- Support API DescribeAccessPoint.
- Support API DescribeAccessPoints.
- Support API ModifyAccessPoint.
- Update API CreateDataFlow: add param FileSystemPath.
- Update API CreateDataFlow: add param SourceStoragePath.
- Update API CreateDataFlow: update param FsetId.
- Update API CreateDataFlow: update param SourceStorage.
- Update API CreateDataFlow: update param Throughput.
- Update API CreateDataFlow: update response param.
- Update API CreateDataFlowTask: add param ConflictPolicy.
- Update API CreateDataFlowTask: update param Directory.
- Update API CreateDataFlowTask: update response param.
- Update API CreateFileSystem: update param StorageType.
- Update API DescribeAccessGroups: update response param.
- Update API DescribeAccessRules: update response param.
- Update API DescribeDataFlowTasks: update response param.
- Update API DescribeDataFlows: update param Filters.
- Update API DescribeDataFlows: update response param.
- Update API DescribeFileSystemStatistics: update response param.
- Update API DescribeFileSystems: update response param.
- Update API ModifyAccessRule: update param SourceCidrIp.


2024-02-29 Version: 2.1.2
- Update API CreateDataFlow: add param FileSystemPath.
- Update API CreateDataFlow: add param SourceStoragePath.
- Update API CreateDataFlow: update param FsetId.
- Update API CreateDataFlow: update param SourceStorage.
- Update API CreateDataFlow: update param Throughput.
- Update API CreateDataFlow: update response param.
- Update API CreateDataFlowTask: add param ConflictPolicy.
- Update API CreateDataFlowTask: update param Directory.
- Update API CreateDataFlowTask: update response param.
- Update API CreateFileSystem: update param StorageType.
- Update API DescribeAccessGroups: update response param.
- Update API DescribeAccessRules: update response param.
- Update API DescribeDataFlowTasks: update response param.
- Update API DescribeDataFlows: update param Filters.
- Update API DescribeDataFlows: update response param.
- Update API DescribeFileSystemStatistics: update response param.
- Update API DescribeFileSystems: update response param.
- Update API ModifyAccessRule: update param SourceCidrIp.


2024-02-27 Version: 2.1.1
- Update API CreateFileSystem: update param StorageType.
- Update API DescribeAccessGroups: update response param.
- Update API DescribeAccessRules: update response param.
- Update API DescribeFileSystemStatistics: update response param.
- Update API DescribeFileSystems: update response param.
- Update API ModifyAccessRule: update param SourceCidrIp.


2024-01-24 Version: 2.1.0
- Generated python 2017-06-26 for NAS.

2023-12-26 Version: 2.0.4
- Generated python 2017-06-26 for NAS.

2021-09-23 Version: 2.0.3
- Generated python 2017-06-26 for NAS.

2021-03-30 Version: 2.0.2
- Generated python 2017-06-26 for NAS.

2021-02-16 Version: 2.0.1
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

