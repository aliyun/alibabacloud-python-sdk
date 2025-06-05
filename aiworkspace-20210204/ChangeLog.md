2025-06-05 Version: 6.4.3
- Update API GetConfig: add response parameters Body.GmtCreateTime.
- Update API GetConfig: add response parameters Body.GmtModifiedTime.
- Update API ListConfigs: add response parameters Body.Configs.$.GmtCreateTime.
- Update API ListConfigs: add response parameters Body.Configs.$.GmtModifiedTime.


2025-06-04 Version: 6.4.2
- Update API CreateDataset: add request parameters body.Edition.
- Update API GetDataset: add response parameters Body.Edition.
- Update API UpdateDataset: add request parameters body.Edition.


2025-05-29 Version: 6.4.1
- Update API GetMember: add response parameters Body.AccountType.
- Update API ListMembers: add response parameters Body.Members.$.AccountType.


2025-05-16 Version: 6.4.0
- Support API CreateConnection.
- Support API DeleteConnection.
- Support API GetConnection.
- Support API ListConnections.
- Support API UpdateConnection.


2025-05-15 Version: 6.3.2
- Update API DeleteUserConfig: add request parameters Scope.


2025-05-12 Version: 6.3.1
- Generated python 2021-02-04 for AIWorkSpace.

2025-04-28 Version: 6.3.0
- Support API DeleteConfig.
- Support API GetConfig.
- Support API ListConfigs.
- Support API UpdateConfig.
- Support API UpdateConfigs.


2025-04-23 Version: 6.2.0
- Support API GetDatasetFileMetasStatistics.
- Update API CreateModel: add request parameters body.Tag.
- Update API ListModels: add request parameters Tag.


2025-04-17 Version: 6.1.0
- Support API DeleteUserConfig.
- Support API ListUserConfigs.
- Support API SetUserConfigs.
- Update API ListDatasetFileMetas: add request parameters EndTagUpdateTime.
- Update API ListDatasetFileMetas: add request parameters MaxResults.
- Update API ListDatasetFileMetas: add request parameters QueryFileDir.
- Update API ListDatasetFileMetas: add request parameters QueryFileName.
- Update API ListDatasetFileMetas: add request parameters QueryFileTypeIncludeAny.
- Update API ListDatasetFileMetas: add request parameters QueryImage.
- Update API ListDatasetFileMetas: add request parameters QueryTagsExclude.
- Update API ListDatasetFileMetas: add request parameters QueryTagsIncludeAll.
- Update API ListDatasetFileMetas: add request parameters QueryTagsIncludeAny.
- Update API ListDatasetFileMetas: add request parameters StartTagUpdateTime.
- Update API ListDatasetFileMetas: add request parameters ThumbnailMode.
- Update API ListDatasetFileMetas: add response parameters Body.MaxResults.


2025-04-01 Version: 6.0.1
- Update API AddImage: add request parameters body.SourceId.
- Update API AddImage: add request parameters body.SourceType.
- Update API GetImage: add response parameters Body.SourceId.
- Update API GetImage: add response parameters Body.SourceType.
- Update API ListImages: add response parameters Body.Images.$.SourceId.
- Update API ListImages: add response parameters Body.Images.$.SourceType.


2025-03-03 Version: 6.0.0
- Support API AcceptDataworksEvent.
- Support API ChangeResourceGroup.
- Support API CreateDatasetFileMetas.
- Support API CreateDatasetJob.
- Support API CreateDatasetJobConfig.
- Support API DeleteDatasetFileMetas.
- Support API DeleteDatasetJob.
- Support API DeleteDatasetJobConfig.
- Support API GetDatasetFileMeta.
- Support API GetDatasetJob.
- Support API GetDatasetJobConfig.
- Support API ListDatasetFileMetas.
- Support API ListDatasetJobConfigs.
- Support API ListDatasetJobs.
- Support API StopDatasetJob.
- Support API UpdateDatasetFileMetas.
- Support API UpdateDatasetJob.
- Support API UpdateDatasetJobConfig.
- Update API CreateDataset: update param body.
- Update API CreateDatasetVersion: update param body.
- Update API CreateWorkspace: update param body.
- Update API CreateWorkspace: update response param.
- Update API GetDataset: update response param.
- Update API GetDatasetVersion: update response param.
- Update API GetWorkspace: update response param.
- Update API ListDatasetVersions: add param LabelValues.
- Update API ListDatasetVersions: delete param DataSourcesTypes.
- Update API ListDatasetVersions: delete param LableValues.
- Update API ListDatasets: add param SortBy.
- Update API ListImages: delete param ParentUserId.
- Update API ListImages: delete param UserId.
- Update API ListWorkspaces: add param ResourceGroupId.
- Update API ListWorkspaces: update response param.
- Update API UpdateDataset: update param body.


2024-11-18 Version: 5.1.2
- Update API CreateCodeSource: update param body.
- Update API ListMembers: update response param.


2024-11-13 Version: 5.1.1
- Update API CreateCodeSource: update param body.


2024-11-07 Version: 5.1.0
- Support API UpdateCodeSource.


2024-11-06 Version: 5.0.1
- Update API GetPermission: add param Labels.


2024-10-30 Version: 5.0.0
- Support API CreateDatasetVersion.
- Support API CreateDatasetVersionLabels.
- Support API DeleteDatasetVersion.
- Support API DeleteDatasetVersionLabels.
- Support API GetDatasetVersion.
- Support API ListDatasetVersions.
- Support API UpdateDatasetVersion.
- Update API CreateDataset: update param body.
- Update API GetDataset: update response param.
- Update API ListDatasets: add param SourceDatasetId.


2024-10-24 Version: 4.1.0
- Support API CreateDatasetVersion.
- Support API CreateDatasetVersionLabels.
- Support API DeleteDatasetVersion.
- Support API DeleteDatasetVersionLabels.
- Support API GetDatasetVersion.
- Support API ListDatasetVersions.
- Support API UpdateDatasetVersion.
- Update API CreateDataset: update param body.
- Update API GetDataset: update response param.
- Update API ListDatasets: add param SourceDatasetId.


2024-10-18 Version: 4.0.1
- Update API CreateDataset: update param body.
- Update API GetDataset: update response param.
- Update API ListDatasets: add param SourceDatasetId.


2024-10-12 Version: 4.0.0
- Support API CreateExperiment.
- Support API CreateRun.
- Support API DeleteExperiment.
- Support API DeleteExperimentLabel.
- Support API DeleteRun.
- Support API DeleteRunLabel.
- Support API GetExperiment.
- Support API GetRun.
- Support API ListExperiment.
- Support API ListRunMetrics.
- Support API ListRuns.
- Support API LogRunMetrics.
- Support API SetExperimentLabels.
- Support API UpdateExperiment.
- Support API UpdateRun.
- Delete API GetServiceTemplate.
- Delete API ListServiceTemplates.
- Update API ListImages: add param ImageUri.


2024-07-25 Version: 3.0.7
- Update API GetDataset: update response param.


2024-07-03 Version: 3.0.6
- Update API CreateModelVersion: update param body.
- Update API GetModelVersion: update response param.
- Update API UpdateModelVersion: update param body.


2024-06-20 Version: 3.0.5
- Update API CreateDataset: update param body.
- Update API GetPermission: add param Option.


2024-04-12 Version: 3.0.4
- Update API GetPermission: add param Option.


2024-03-23 Version: 3.0.2
- Update API CreateDataset: update param body.
- Update API GetPermission: add param Resource.
- Update API ListDatasets: add param Provider.


2023-12-26 Version: 3.0.1
- Generated python 2021-02-04 for AIWorkSpace.

2023-12-21 Version: 3.0.0
- Generated python 2021-02-04 for AIWorkSpace.

2023-10-21 Version: 2.0.4
- Generated python 2021-02-04 for AIWorkSpace.

2023-10-07 Version: 2.0.3
- Generated python 2021-02-04 for AIWorkSpace.

2023-09-26 Version: 2.0.2
- Generated python 2021-02-04 for AIWorkSpace.

2023-09-01 Version: 2.0.1
- Generated python 2021-02-04 for AIWorkSpace.

2023-08-08 Version: 2.0.0
- Generated python 2021-02-04 for AIWorkSpace.

2023-03-13 Version: 1.2.9
- Release master.

2022-10-28 Version: 1.2.8
- Add models related API.

2022-06-27 Version: 1.2.5
- Fix CodeSourceItem spec.

2022-01-10 Version: 1.2.4
- Support workspace config.

