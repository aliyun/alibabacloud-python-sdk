2025-09-10 Version: 5.8.0
- Support API DeleteConsumeProcessor.
- Support API GetConsumeProcessor.
- Support API ListConsumeProcessors.
- Support API PutConsumeProcessor.
- Update API CreateLogtailPipelineConfig: add request parameters body.task.
- Update API ListLogtailPipelineConfig: add request parameters configType.
- Update API UpdateLogtailPipelineConfig: add request parameters body.task.


2025-06-10 Version: 5.7.4
- Generated python 2020-12-30 for Sls.

2025-06-09 Version: 5.7.3
- Generated python 2020-12-30 for Sls.

2025-06-09 Version: 5.7.2
- Update API CreateAgentInstanceConfig: add request parameters body.attributes.
- Update API CreateAgentInstanceConfig: add request parameters body.configType.
- Update API CreateAgentInstanceConfig: add request parameters body.grayConfigs.
- Update API DeleteAgentInstanceConfig: add request parameters configType.
- Update API DeleteAgentInstanceConfig: add request parameters attributes.
- Update API GetAgentInstanceConfig: add request parameters configType.
- Update API GetAgentInstanceConfig: add request parameters attributes.
- Update API GetAgentInstanceConfig: add response parameters Body.attributes.
- Update API GetAgentInstanceConfig: add response parameters Body.configType.
- Update API GetAgentInstanceConfig: add response parameters Body.grayConfigs.
- Update API ListAgentInstanceConfigs: add request parameters attributes.
- Update API ListAgentInstanceConfigs: add request parameters configType.
- Update API ListDashboard: add request parameters dashboardName.
- Update API ListDashboard: add request parameters displayName.
- Update API ListDashboard: add request parameters tags.
- Update API ListDashboard: add response parameters Body.dashboardItems.$.description.
- Update API UpdateAgentInstanceConfig: add request parameters configType.
- Update API UpdateAgentInstanceConfig: add request parameters attributes.
- Update API UpdateAgentInstanceConfig: add request parameters body.grayConfigs.


2025-04-14 Version: 5.7.1
- Generated python 2020-12-30 for Sls.

2025-03-31 Version: 5.7.0
- Support API CallAiTools.
- Support API CreateMaxComputeExport.
- Support API DeleteIngestProcessor.
- Support API DeleteMaxComputeExport.
- Support API GetIngestProcessor.
- Support API GetMaxComputeExport.
- Support API ListAiTools.
- Support API ListIngestProcessors.
- Support API ListMaxComputeExports.
- Support API PutIngestProcessor.
- Support API StartMaxComputeExport.
- Support API StopMaxComputeExport.
- Support API UpdateLogStoreProcessor.
- Support API UpdateMaxComputeExport.
- Support API UpdateMetricStoreProcessor.
- Update API CreateMetricStore: add request parameters body.hot_ttl.
- Update API CreateMetricStore: add request parameters body.infrequentAccessTTL.
- Update API CreateProject: add request parameters body.recycleBinEnabled.
- Update API DeleteProject: add request parameters forceDelete.
- Update API GetMetricStore: add response parameters Body.hot_ttl.
- Update API GetMetricStore: add response parameters Body.infrequentAccessTTL.
- Update API UpdateMetricStore: add request parameters body.hot_ttl.
- Update API UpdateMetricStore: add request parameters body.infrequentAccessTTL.
- Update API UpdateProject: add request parameters body.recycleBinEnabled.


2024-12-09 Version: 5.6.0
- Support API CreateAgentInstanceConfig.
- Support API DeleteAgentInstanceConfig.
- Support API GetAgentInstanceConfig.
- Support API ListAgentInstanceConfigs.
- Support API UpdateAgentInstanceConfig.


2024-12-04 Version: 5.5.1
- Update API GetDownloadJob: update response param.
- Update API ListDownloadJobs: update response param.


2024-11-21 Version: 5.5.0
- Support API DescribeRegions.
- Support API PullLogs.
- Support API PutLogs.
- Support API UpdateLogStoreEncryption.
- Update API CreateMetricStore: update param project.
- Update API CreateMetricStore: update param body.
- Update API CreateSavedSearch: update param body.
- Update API GetLogsV2: update response param.
- Update API GetMetricStore: update param project.
- Update API GetMetricStoreMeteringMode: update param project.
- Update API GetMetricStoreMeteringMode: update response param.
- Update API ListMetricStores: update param project.
- Update API ListMetricStores: update response param.
- Update API UpdateLogStore: update param body.
- Update API UpdateMetricStore: update param project.
- Update API UpdateMetricStore: update param body.
- Update API UpdateMetricStoreMeteringMode: update param project.


2024-09-02 Version: 5.4.1
- Update API CreateIndex: update param body.
- Update API GetIndex: update response param.
- Update API UpdateIndex: update param body.


2024-08-29 Version: 5.4.0
- Support API CreateMetricStore.
- Support API DeleteMetricStore.
- Support API GetMetricStore.
- Support API ListMetricStores.
- Support API UpdateMetricStore.
- Update API CreateLogStore: update param body.
- Update API UpdateLogStore: update param body.


2024-08-02 Version: 5.3.0
- Support API CreateDownloadJob.
- Support API DeleteDownloadJob.
- Support API GetDownloadJob.
- Support API ListDownloadJobs.


2024-07-25 Version: 5.2.3
- Generated python 2020-12-30 for Sls.

2024-07-05 Version: 5.2.2
- Update API ConsumerGroupUpdateCheckPoint: update param body.
- Update API CreateIndex: update param body.
- Update API DeleteCollectionPolicy: update response param.
- Update API GetCollectionPolicy: update response param.
- Update API GetIndex: update response param.
- Update API ListCollectionPolicies: add param centralProject.
- Update API ListCollectionPolicies: add param offset.
- Update API ListCollectionPolicies: add param size.
- Update API ListCollectionPolicies: update response param.
- Update API PutProjectTransferAcceleration: update param project.
- Update API PutProjectTransferAcceleration: update param body.
- Update API UpdateIndex: update param body.
- Update API UpsertCollectionPolicy: update param body.
- Update API UpsertCollectionPolicy: update response param.


2024-05-17 Version: 5.2.1
- Update API ListProject: add param fetchQuota.


2024-05-10 Version: 5.2.0
- Support API ConsumerGroupUpdateCheckPoint.
- Support API CreateStoreView.
- Support API DeleteStoreView.
- Support API DisableScheduledSQL.
- Support API EnableScheduledSQL.
- Support API GetMetricStoreMeteringMode.
- Support API GetStoreView.
- Support API GetStoreViewIndex.
- Support API ListStoreViews.
- Support API UpdateMetricStoreMeteringMode.
- Support API UpdateStoreView.
- Update API GetLogStoreMeteringMode: update response param.
- Update API GetMLServiceResults: add param version.


2024-04-09 Version: 5.1.0
- Support API CreateSqlInstance.
- Support API GetSlsService.
- Support API GetSqlInstance.
- Support API OpenSlsService.
- Support API RefreshToken.
- Support API UpdateSqlInstance.
- Update API CreateTicket: add param accessTokenExpirationTime.
- Update API CreateTicket: add param expirationTime.
- Update API DeleteAlert: update param project.
- Update API DeleteAlert: update param alertName.
- Update API DisableAlert: update param project.
- Update API DisableAlert: update param alertName.
- Update API EnableAlert: update param project.
- Update API EnableAlert: update param alertName.
- Update API GetAlert: update param project.
- Update API GetAlert: update param alertName.
- Update API GetLogsV2: update param project.
- Update API GetLogsV2: update param logstore.
- Update API GetLogsV2: update param Accept-Encoding.
- Update API GetLogsV2: update param body.
- Update API ListETLs: add param logstore.
- Update API ListETLs: update param project.
- Update API ListExternalStore: update response param.
- Update API ListOSSExports: add param logstore.
- Update API ListOSSHDFSExports: add param logstore.
- Update API ListOSSIngestions: add param logstore.
- Update API ListScheduledSQLs: add param logstore.
- Update API UpdateAlert: update param project.
- Update API UpdateAlert: update param alertName.


2024-02-06 Version: 5.0.0
- Generated python 2020-12-30 for Sls.

2024-01-19 Version: 4.4.1
- Generated python 2020-12-30 for Sls.

2024-01-15 Version: 4.4.0
- Generated python 2020-12-30 for Sls.

2024-01-10 Version: 4.3.0
- Generated python 2020-12-30 for Sls.

2023-12-27 Version: 4.2.1
- Generated python 2020-12-30 for Sls.

2023-12-27 Version: 4.2.0
- Generated python 2020-12-30 for Sls.

2023-12-07 Version: 4.1.2
- Generated python 2020-12-30 for Sls.

2023-12-07 Version: 4.1.1
- Generated python 2020-12-30 for Sls.

2023-11-29 Version: 4.1.0
- Generated python 2020-12-30 for Sls.

2023-11-02 Version: 4.0.0
- Generated python 2020-12-30 for Sls.

2023-10-23 Version: 3.1.0
- Generated python 2020-12-30 for Sls.

2023-09-18 Version: 3.0.0
- Generated python 2020-12-30 for Sls.

2023-09-17 Version: 2.2.1
- Generated python 2020-12-30 for Sls.

2023-09-17 Version: 2.2.0
- Generated python 2020-12-30 for Sls.

2023-09-15 Version: 2.1.0
- Generated python 2020-12-30 for Sls.

2023-08-22 Version: 2.0.2
- Generated python 2020-12-30 for Sls.

2023-08-01 Version: 2.0.1
- Support config api.

2023-04-21 Version: 2.0.0
- Update project structure.

2023-04-21 Version: 1.5.16
- Incompatible changes update. 

2023-03-27 Version: 1.5.15
- Fix project api head.

2023-03-23 Version: 1.5.14
- Fix project api head.

2023-02-22 Version: 1.5.13
- Fix api pathname.

2023-02-20 Version: 1.5.12
- Fix api pathname.

2023-02-08 Version: 1.5.11
- Add productType to logstore API.

2023-02-08 Version: 1.5.10
- Add productType to logstore API.

2023-02-08 Version: 1.5.9
- Add productType to logstore API.

2023-02-08 Version: 1.5.8
- Add productType to logstore API.

2023-02-07 Version: 1.5.7
- Add productType to logstore API.

2023-02-06 Version: 1.5.6
- Add productType to logstore API.

2023-02-03 Version: 1.5.5
- Add productType to logstore API.

2023-02-02 Version: 1.5.4
- Add productType to logstore API.

2023-02-02 Version: 1.5.3
- Add productType to logstore API.

2022-10-20 Version: 1.5.2
- Fix signature bug.

2022-09-15 Version: 1.5.1
- Fix signature bug.

2022-08-01 Version: 1.5.0
- Add resource Shipper.
- Add resource ExternalStore.

2022-07-12 Version: 1.4.0
- Add DeleteSavedsearch.
- Add EtlMeta.

2022-07-07 Version: 1.3.0
- Add Get Create Delete Update Logging.
- Add Update Get CheckPoint.
- Add ListMachines.
- Add Delete Create List Domain.
- Add ApplyConfigToMachineGroup.
- Add RemoveConfigFromMachineGroup.
- Add GetAppliedConfigs.

2022-07-06 Version: 1.2.0
- Rename config to LogtailConfig, fix conflict.
- Add Get Delete Create List Update MachineGroup.
- Add TagResources UnTagResources ListTagResources.

2022-07-06 Version: 1.1.1
- Rename config to LogtailConfig, fix conflict.

2022-07-05 Version: 1.1.0
- Add SplitShard, MergeShard, ListShards.
- Add getLogs, getContextLogs.
- Add getCursorTime, getCursor.

2022-07-05 Version: 1.0.4
- Add resource index and domain.
- Add api GetProjectLogs.

2022-06-01 Version: 1.0.3
- Generated python 2020-12-30 for Sls.

2022-02-22 Version: 1.0.2
- Generated python 2020-12-30 for Sls.

2021-12-31 Version: 1.0.1
- Generated python 2020-12-30 for Sls.

2021-12-16 Version: 1.0.0
- Generated python 2020-12-30 for Sls.

