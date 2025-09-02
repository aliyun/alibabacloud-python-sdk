2025-09-02 Version: 8.0.1
- Generated python 2020-05-18 for dataworks-public.

2025-04-27 Version: 8.0.0
- Update API ListFiles: delete request parameters CommitStatus.


2025-04-22 Version: 7.0.2
- Generated python 2020-05-18 for dataworks-public.

2025-04-07 Version: 7.0.1
- Update API ListFiles: add request parameters CommitStatus.


2025-03-28 Version: 7.0.0
- Delete API MountDirectory.
- Delete API RevokeColumnPermission.
- Delete API UmountDirectory.
- Update API CreatePermissionApplyOrder: add request parameters ApplyType.
- Update API CreatePermissionApplyOrder: add request parameters CatalogName.
- Update API CreatePermissionApplyOrder: add request parameters ApplyObject.$.ColumnMetaList.$.Actions.
- Update API GetPermissionApplyOrderDetail: add response parameters Body.ApplyOrderDetail.ApproveContent.ProjectMeta.ObjectMetaList.$.Actions.
- Update API GetPermissionApplyOrderDetail: add response parameters Body.ApplyOrderDetail.ApproveContent.ProjectMeta.ObjectMetaList.$.ColumnMetaList.$.ColumnActions.
- Update API ListBaselineStatuses: add response parameters Body.Data.BaselineStatuses.$.BaselineType.
- Update API ListFiles: add request parameters LastEditUser.
- Update API ListPermissionApplyOrders: add request parameters ApplyType.
- Update API ListPermissionApplyOrders: add request parameters CatalogName.


2025-02-08 Version: 6.2.4
- Update API CreateFile: add param ImageId.
- Update API GetFile: update response param.
- Update API UpdateFile: add param ImageId.


2025-01-23 Version: 6.2.3
- Update API GetDISyncTask: update response param.
- Update API ListCheckProcesses: add param MessageId.


2025-01-13 Version: 6.2.2
- Update API GetDISyncTask: update response param.


2024-12-13 Version: 6.2.1
- Update API CreateFile: add param Timeout.
- Update API GetFile: update response param.
- Update API GetInstance: update response param.
- Update API UpdateFile: add param Timeout.


2024-11-21 Version: 6.2.0
- Support API ListCheckProcesses.


2024-11-15 Version: 6.1.6
- Update API UpdateQualityRule: update param Checker.


2024-11-04 Version: 6.1.5
- Update API CreateProject: update param ProjectDescription.


2024-10-17 Version: 6.1.4
- Update API ListNodes: update response param.


2024-09-29 Version: 6.1.3
- Update API CreateDISyncTask: update param TaskContent.
- Update API GetNode: update response param.


2024-09-18 Version: 6.1.2
- Update API GetRemind: update response param.


2024-09-03 Version: 6.1.1
- Update API GetFile: update response param.


2024-09-03 Version: 6.1.0
- Support API ListTables.
- Update API CreateFile: add param ApplyScheduleImmediately.
- Update API GetFile: update response param.
- Update API UpdateFile: add param ApplyScheduleImmediately.


2024-08-14 Version: 6.0.1
- Update API DeleteLineageRelation: add param RelationshipType.


2024-07-31 Version: 6.0.0
- Support API ListClusterConfigs.
- Support API ListClusters.
- Support API UpdateClusterConfigs.
- Update API GetQualityRule: update response param.
- Update API QuerySensNodeInfo: add param RegionId.
- Update API QuerySensNodeInfo: delete param regionId.
- Update API UpdateDataSource: update param Content.


2024-06-07 Version: 5.7.0
- Support API ListMeasureData.


2024-06-07 Version: 5.6.2
- Generated python 2020-05-18 for dataworks-public.

2024-06-04 Version: 5.6.1
- Update API CreateDIJob: update param ResourceSettings.
- Update API GetDIJob: update response param.
- Update API GetNode: update response param.
- Update API GetNodeChildren: update response param.
- Update API GetNodeParents: update response param.
- Update API ListNodes: update response param.
- Update API UpdateDIJob: update param ResourceSettings.


2024-05-20 Version: 5.6.0
- Support API DsgDesensPlanAddOrUpdate.
- Support API DsgSceneQuerySceneListByName.
- Support API DsgScenedDeleteScene.
- Support API DsgWhiteListAddOrUpdate.
- Support API DsgWhiteListDeleteList.


2024-05-16 Version: 5.5.0
- Support API DsgDesensPlanDelete.
- Support API DsgDesensPlanQueryList.
- Support API DsgDesensPlanUpdateStatus.
- Support API DsgPlatformQueryProjectsAndSchemaFromMeta.
- Support API DsgQueryDefaultTemplates.
- Support API DsgSceneAddOrUpdateScene.
- Support API DsgUserGroupAddOrUpdate.
- Support API DsgUserGroupDelete.
- Support API DsgUserGroupGetOdpsRoleGroups.
- Support API DsgUserGroupQueryList.
- Support API DsgUserGroupQueryUserList.
- Support API DsgWhiteListQueryList.
- Update API CreateQualityEntity: update response param.
- Update API CreateQualityRelativeNode: update response param.
- Update API DeleteQualityEntity: update response param.
- Update API DeleteQualityRelativeNode: update response param.
- Update API ListQualityResultsByRule: update response param.


2024-05-07 Version: 5.4.1
- Generated python 2020-05-18 for dataworks-public.

2024-04-24 Version: 5.4.0
- Support API AddRecognizeRule.
- Support API DeleteRecognizeRule.
- Support API DsgRunSensIdentify.
- Support API DsgStopSensIdentify.
- Support API EditRecognizeRule.
- Support API QueryDefaultTemplate.
- Support API QueryRecognizeDataByRuleType.
- Support API QueryRecognizeRuleDetail.
- Support API QueryRecognizeRulesType.
- Support API QuerySensClassification.
- Support API QuerySensLevel.
- Support API QuerySensNodeInfo.
- Update API SubmitDataServiceApi: update response param.


2024-04-17 Version: 5.3.0
- Support API DsgQuerySensResult.
- Update API CreateFile: update param DependentType.
- Update API ListInstances: update param NodeId.
- Update API UpdateFile: update param DependentType.


2024-03-29 Version: 5.2.0
- Support API CreateProject.
- Support API GetAlertMessage.
- Update API CreateDIJob: update param JobSettings.
- Update API CreateDIJob: update response param.
- Update API CreateQualityEntity: update param ProjectId.
- Update API DeleteQualityEntity: update param ProjectId.
- Update API DeleteQualityRule: update param ProjectId.
- Update API GetDIJob: update response param.
- Update API GetQualityEntity: update param ProjectId.
- Update API GetQualityFollower: update param ProjectId.
- Update API ListNodes: add param SchedulerType.
- Update API ListQualityResultsByEntity: update param EntityId.
- Update API ListQualityResultsByEntity: update param ProjectId.
- Update API ListQualityResultsByEntity: update response param.
- Update API ListQualityResultsByRule: update param ProjectId.
- Update API ListQualityRules: update param ProjectId.
- Update API ListQualityRules: update response param.
- Update API RunCycleDagNodes: add param AlertNoticeType.
- Update API RunCycleDagNodes: add param AlertType.
- Update API RunCycleDagNodes: add param ConcurrentRuns.
- Update API UpdateDIJob: update param JobSettings.
- Update API UpdateDIJob: update response param.
- Update API UpdateQualityRule: update param ProjectId.


2024-02-29 Version: 5.1.0
- Support API GetAlertMessage.
- Update API CreateDIJob: update param JobSettings.
- Update API CreateDIJob: update response param.
- Update API CreateQualityEntity: update param ProjectId.
- Update API DeleteQualityEntity: update param ProjectId.
- Update API DeleteQualityRule: update param ProjectId.
- Update API GetDIJob: update response param.
- Update API GetQualityEntity: update param ProjectId.
- Update API GetQualityFollower: update param ProjectId.
- Update API ListNodes: add param SchedulerType.
- Update API ListQualityResultsByEntity: update param EntityId.
- Update API ListQualityResultsByEntity: update param ProjectId.
- Update API ListQualityResultsByEntity: update response param.
- Update API ListQualityResultsByRule: update param ProjectId.
- Update API ListQualityRules: update param ProjectId.
- Update API ListQualityRules: update response param.
- Update API RunCycleDagNodes: add param AlertNoticeType.
- Update API RunCycleDagNodes: add param AlertType.
- Update API RunCycleDagNodes: add param ConcurrentRuns.
- Update API UpdateDIJob: update param JobSettings.
- Update API UpdateDIJob: update response param.
- Update API UpdateQualityRule: update param ProjectId.


2023-12-11 Version: 5.0.0
- Generated python 2020-05-18 for dataworks-public.

2023-11-23 Version: 4.7.4
- Generated python 2020-05-18 for dataworks-public.

2023-11-15 Version: 4.7.3
- Generated python 2020-05-18 for dataworks-public.

2023-10-10 Version: 4.7.2
- Generated python 2020-05-18 for dataworks-public.

2023-10-09 Version: 4.7.1
- Generated python 2020-05-18 for dataworks-public.

2023-09-25 Version: 4.7.0
- Support DIJob and DIAlarmRule related APIs.

2023-09-19 Version: 4.6.0
- Generated python 2020-05-18 for dataworks-public.

2023-08-10 Version: 4.5.0
- Generated python 2020-05-18 for dataworks-public.

2023-07-25 Version: 4.4.12
- Generated python 2020-05-18 for dataworks-public.

2023-07-17 Version: 4.4.11
- Generated python 2020-05-18 for dataworks-public.

2023-06-12 Version: 4.4.10
- Generated python 2020-05-18 for dataworks-public.

2023-06-05 Version: 4.4.9
- Generated python 2020-05-18 for dataworks-public.

2023-03-31 Version: 4.4.8
- Generated python 2020-05-18 for dataworks-public.

2023-03-16 Version: 4.4.7
- Generated python 2020-05-18 for dataworks-public.

2023-03-08 Version: 4.4.6
- Generated python 2020-05-18 for dataworks-public.

2023-03-07 Version: 4.4.5
- Generated python 2020-05-18 for dataworks-public.

2023-03-07 Version: 4.4.4
- Generated python 2020-05-18 for dataworks-public.

2023-03-02 Version: 4.4.3
- Generated python 2020-05-18 for dataworks-public.

2023-03-02 Version: 4.4.2
- Generated python 2020-05-18 for dataworks-public.

2023-02-09 Version: 4.4.1
- Generated python 2020-05-18 for dataworks-public.

2023-01-13 Version: 4.4.0
- Generated python 2020-05-18 for dataworks-public.

2023-01-05 Version: 4.3.22
- Generated python 2020-05-18 for dataworks-public.

2022-12-23 Version: 4.3.21
- Generated python 2020-05-18 for dataworks-public.

2022-12-22 Version: 4.3.20
- Generated python 2020-05-18 for dataworks-public.

2022-12-16 Version: 4.3.19
- Generated python 2020-05-18 for dataworks-public.

2022-12-02 Version: 4.3.18
- Generated python 2020-05-18 for dataworks-public.

2022-12-02 Version: 4.3.17
- Generated python 2020-05-18 for dataworks-public.

2022-11-16 Version: 4.3.16
- Generated python 2020-05-18 for dataworks-public.

2022-10-13 Version: 4.3.15
- Generated python 2020-05-18 for dataworks-public.

2022-08-31 Version: 4.3.14
- Generated python 2020-05-18 for dataworks-public.

2022-08-16 Version: 4.3.13
- Generated python 2020-05-18 for dataworks-public.

2022-08-11 Version: 4.3.12
- Generated python 2020-05-18 for dataworks-public.

2022-07-20 Version: 4.3.11
- Generated python 2020-05-18 for dataworks-public.

2022-07-19 Version: 4.3.10
- Generated python 2020-05-18 for dataworks-public.

2022-05-30 Version: 4.3.9
- Generated python 2020-05-18 for dataworks-public.

2022-05-10 Version: 4.3.8
- Generated python 2020-05-18 for dataworks-public.

2022-05-07 Version: 4.3.7
- Generated python 2020-05-18 for dataworks-public.

2022-04-25 Version: 4.3.6
- Generated python 2020-05-18 for dataworks-public.

2022-04-19 Version: 4.3.5
- Generated python 2020-05-18 for dataworks-public.

2022-04-07 Version: 4.3.4
- Generated python 2020-05-18 for dataworks-public.

2022-03-21 Version: 4.3.3
- Generated python 2020-05-18 for dataworks-public.

2022-02-28 Version: 4.3.2
- Generated python 2020-05-18 for dataworks-public.

2021-12-06 Version: 4.3.1
- Generated python 2020-05-18 for dataworks-public.

2021-11-30 Version: 4.3.0
- Generated python 2020-05-18 for dataworks-public.

2021-11-16 Version: 4.2.5
- Generated python 2020-05-18 for dataworks-public.

2021-10-21 Version: 4.2.4
- Generated python 2020-05-18 for dataworks-public.

2021-10-21 Version: 4.2.3
- Generated python 2020-05-18 for dataworks-public.

2021-09-28 Version: 4.2.2
- Generated python 2020-05-18 for dataworks-public.

2021-09-26 Version: 4.2.1
- Generated python 2020-05-18 for dataworks-public.

2021-09-24 Version: 3.4.3
- Generated python 2020-05-18 for dataworks-public.

2021-09-24 Version: 4.2.0
- Generated python 2020-05-18 for dataworks-public.

2021-09-10 Version: 4.1.0
- Generated python 2020-05-18 for dataworks-public.

2021-09-01 Version: 3.4.2
- Generated python 2020-05-18 for dataworks-public.

2021-08-20 Version: 4.0.1
- Generated python 2020-05-18 for dataworks-public.

2021-08-20 Version: 3.4.1
- Generated python 2020-05-18 for dataworks-public.

2021-05-20 Version: 4.0.0
- Generated python 2020-05-18 for dataworks-public.

2021-04-15 Version: 2.3.2
- Generated python 2020-05-18 for dataworks-public.

2021-04-12 Version: 2.3.1
- Generated python 2020-05-18 for dataworks-public.

2021-04-09 Version: 2.3.0
- Generated python 2020-05-18 for dataworks-public.

2021-03-31 Version: 2.2.0
- Generated python 2020-05-18 for dataworks-public.

2020-11-25 Version: 2.1.1
- Generated python 2020-05-18 for dataworks-public.

2020-11-17 Version: 2.1.0
- Generated python 2020-05-18 for dataworks-public.

2020-10-27 Version: 2.0.2
- Generated python 2020-05-18 for dataworks-public.

2020-10-14 Version: 2.0.2
- Generated python 2020-05-18 for dataworks-public.

2020-09-25 Version: 2.0.1
- Generated python 2020-05-18 for dataworks-public.

2020-09-23 Version: 2.0.0
- Generated python 2020-05-18 for dataworks-public.

