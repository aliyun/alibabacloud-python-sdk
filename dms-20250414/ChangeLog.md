2026-09-01 Version: 1.26.0
- Support API CreateDataAgentFeedback.


2026-09-01 Version: 1.25.1
- Update API SendChatMessage: add request parameters DataSource.Permission.Tables.$.DisallowedColumns.
- Update API SendChatMessage: add request parameters DataSources.$.Permission.Tables.$.DisallowedColumns.
- Update API SendChatMessage: add request parameters SessionConfig.PermissionConfig.


2026-08-26 Version: 1.24.0
- Support API CreateDataAgentTheme.
- Support API DescribeDataAgentTheme.
- Support API GetDataAgentThemeUploadSignature.
- Support API ListDataAgentTheme.
- Support API ModifyDataAgentTheme.


2026-08-24 Version: 1.23.0
- Support API CreateOneMetaSqlTemplate.
- Support API DeleteOneMetaOssieModel.
- Support API DeleteOneMetaSqlTemplate.
- Support API GetOneMetaOssieModel.
- Support API ImportOneMetaOssieModel.
- Support API ListOneMetaOssieModels.
- Support API ListOneMetaSqlTemplates.
- Support API UpdateOneMetaOssieModel.
- Support API UpdateOneMetaSqlTemplate.


2026-08-24 Version: 1.22.0
- Support API AddDataAgentMemory.
- Update API CreateCustomAgent: add request parameters UserSpecifiedSkillList.
- Update API CreateCustomAgent: add response parameters Body.Data.UserSpecifiedSkillList.
- Update API DescribeCustomAgent: add response parameters Body.Data.UserSpecifiedSkillList.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.UserSpecifiedSkillList.
- Update API ModifyCustomAgent: add request parameters UserSpecifiedSkillList.
- Update API ModifyCustomAgent: add response parameters Body.Data.UserSpecifiedSkillList.
- Update API SendChatMessage: add request parameters SessionConfig.UserSpecifiedSkillList.


2026-08-21 Version: 1.21.3
- Generated python 2025-04-14 for Dms.

2026-08-13 Version: 1.21.2
- Update API CreateCustomAgent: add request parameters ExecutionConfig.ForbiddenAppendDataSource.
- Update API CreateCustomAgent: add response parameters Body.Data.ExecutionConfig.ForbiddenAppendDataSource.
- Update API DescribeCustomAgent: add response parameters Body.Data.ExecutionConfig.ForbiddenAppendDataSource.
- Update API GetDataAgentTaskModelUsage: add request parameters PayLevel.
- Update API GetDataAgentTaskModelUsage: add response parameters Body.Data.AccelerationRatio.
- Update API GetDataAgentTaskModelUsage: add response parameters Body.Data.RateLimitedSessionCount.
- Update API GetDataAgentTaskModelUsage: add response parameters Body.Data.TotalLlmWaitDuration.
- Update API GetDataAgentTaskModelUsage: add response parameters Body.Data.TotalSessionCount.
- Update API GetDataAgentTaskModelUsageMetrics: add request parameters PayLevel.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.ExecutionConfig.ForbiddenAppendDataSource.
- Update API ModifyCustomAgent: add request parameters ExecutionConfig.ForbiddenAppendDataSource.
- Update API ModifyCustomAgent: add response parameters Body.Data.ExecutionConfig.ForbiddenAppendDataSource.


2026-08-11 Version: 1.21.1
- Generated python 2025-04-14 for Dms.

2026-08-04 Version: 1.20.0
- Support API DeleteDataAgentMcp.
- Support API GetDataAgentMcp.
- Support API GetListMcpServerToolsResult.
- Support API InitWorkspaceSystemMcpServer.
- Support API InstallDataAgentMcp.
- Support API ListDataAgentMcp.
- Support API ModifyDataAgentMcp.
- Support API StartListMcpServerTools.
- Update API ListDataAgentSession: add request parameters CreatorId.
- Update API ListDataAgentWorkspace: add request parameters Creator.
- Update API ListDataAgentWorkspace: add response parameters Body.Data.Content.$.CreatorName.
- Update API ListDataAgentWorkspace: add response parameters Body.Data.Content.$.RunningSessionCount.
- Update API ListDataAgentWorkspace: add response parameters Body.Data.Content.$.TotalSessionCount.


2026-08-03 Version: 1.19.0
- Support API CheckDataAgentMemoryConfig.
- Support API ConfigDataAgentMemory.
- Support API DeleteDataAgentMemory.
- Support API ListDataAgentMemory.
- Support API UpdateDataAgentMemory.


2026-07-27 Version: 1.18.1
- Update API CreateCustomAgent: add request parameters WebReportTheme.
- Update API CreateCustomAgent: add response parameters Body.Data.WebReportTheme.
- Update API DescribeCustomAgent: add response parameters Body.Data.WebReportTheme.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.WebReportTheme.
- Update API ModifyCustomAgent: add request parameters WebReportTheme.
- Update API ModifyCustomAgent: add response parameters Body.Data.WebReportTheme.
- Update API SendChatMessage: add request parameters DataSource.Permission.
- Update API SendChatMessage: add request parameters DataSources.$.Permission.


2026-07-23 Version: 1.18.0
- Support API DeleteDataAgent.
- Support API DescribeDataAgentMetrics.
- Support API GetAgenticAgentByInstallToken.
- Update API CreateDataAgentAccuracyTest: add request parameters Datasource.
- Update API DescribeFileUploadSignature: add request parameters WorkspaceId.
- Update API FileUploadCallback: add request parameters WorkspaceId.
- Update API ListDataAgentAccuracyTestInstances: add response parameters Body.Data.$.Datasource.
- Update API ListDataAgentAccuracyTestResults: add response parameters Body.Data.FailedCount.
- Update API ListDataAgentAccuracyTestResults: add response parameters Body.Data.PendingCount.
- Update API ListDataAgentAccuracyTestResults: add response parameters Body.Data.Content.$.AgentSql.
- Update API ListDataAgentAccuracyTestResults: add response parameters Body.Data.Content.$.SessionId.
- Update API ListDataCenterDatabase: add request parameters WorkspaceId.
- Update API UpdateDataAgentAccuracyTest: add request parameters Datasource.
- Update API UpdateDataAgentAccuracyTest: add response parameters Body.Data.Datasource.
- Update API UpdateDataAgentAccuracyTest: add response parameters Body.Data.Desc.
- Update API UpdateDataAgentAccuracyTest: add response parameters Body.Data.MaxConcurrent.
- Update API UpdateDataAgentAccuracyTest: add response parameters Body.Data.Name.
- Update API UpdateDataAgentAccuracyTest: add response parameters Body.Data.NeedDelete.


2026-07-03 Version: 1.17.0
- Support API CreateDataAgentAccuracyTest.
- Support API DeleteDataAgentAccuracyTest.
- Support API ListDataAgentAccuracyTestInstances.
- Support API ListDataAgentAccuracyTestResults.
- Support API ListDataAgentAccuracyTestTasks.
- Support API StartDataAgentAccuracyTestTask.
- Support API StopDataAgentAccuracyTestTask.
- Support API UpdateDataAgentAccuracyTest.
- Update API SendChatMessage: add request parameters UserOssBucket.
- Update API SendChatMessage: add request parameters SessionConfig.EnableSearch.
- Update API SendChatMessage: add request parameters SessionConfig.KbUuidList.
- Update API SendChatMessage: add request parameters SessionConfig.McpServerIds.
- Update API SendChatMessage: add request parameters SessionConfig.PlanMode.


2026-07-03 Version: 1.17.0
- Support API CreateDataAgentAccuracyTest.
- Support API DeleteDataAgentAccuracyTest.
- Support API ListDataAgentAccuracyTestInstances.
- Support API ListDataAgentAccuracyTestResults.
- Support API ListDataAgentAccuracyTestTasks.
- Support API StartDataAgentAccuracyTestTask.
- Support API StopDataAgentAccuracyTestTask.
- Support API UpdateDataAgentAccuracyTest.
- Update API SendChatMessage: add request parameters UserOssBucket.
- Update API SendChatMessage: add request parameters SessionConfig.EnableSearch.
- Update API SendChatMessage: add request parameters SessionConfig.KbUuidList.
- Update API SendChatMessage: add request parameters SessionConfig.McpServerIds.
- Update API SendChatMessage: add request parameters SessionConfig.PlanMode.


2026-06-25 Version: 1.16.1
- Update API SendChatMessage: add request parameters WorkspaceId.


2026-06-24 Version: 1.16.0
- Support API GetSqlConsoleOperationLog.
- Update API ListDataAgentSession: add request parameters Mode.


2026-06-16 Version: 1.15.3
- Update API CreateDataAgentWorkspace: add response parameters Body.Data.Type.
- Update API DescribeDataAgentSession: add response parameters Body.Data.Artifacts.
- Update API DescribeDataAgentSession: add response parameters Body.Data.DataSources.
- Update API DescribeDataAgentSession: add response parameters Body.Data.RecallResults.
- Update API GetDataAgentWorkspaceInfo: add response parameters Body.Data.Type.
- Update API ListDataAgentWorkspace: add response parameters Body.Data.Content.$.Type.
- Update API SendChatMessage: add request parameters TaskConfig.
- Update API SendChatMessage: add request parameters SessionConfig.SkipAskHuman.
- Update API SendChatMessage: add request parameters SessionConfig.SkipPlan.
- Update API SendChatMessage: add request parameters SessionConfig.SkipSqlConfirm.
- Update API SendChatMessage: add request parameters SessionConfig.SkipWebReportConfirm.
- Update API SendChatMessage: add response parameters Body.Data.MessageId.


2026-06-11 Version: 1.15.2
- Generated python 2025-04-14 for Dms.

2026-06-11 Version: 1.15.1
- Generated python 2025-04-14 for Dms.

2026-06-09 Version: 1.15.0
- Support API RetrieveKnowledgeBase.


2026-06-02 Version: 1.14.0
- Support API DeleteWorkspaceCode.
- Support API GetWorkspaceCode.
- Support API ListWorkspaceCode.
- Support API SaveWorkspaceCode.
- Update API CreateCustomAgent: add request parameters RelatedSessionId.
- Update API CreateCustomAgent: add response parameters Body.Data.RelatedSessionId.
- Update API DescribeCustomAgent: add response parameters Body.Data.RelatedSessionId.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.RelatedSessionId.
- Update API ModifyCustomAgent: add request parameters RelatedSessionId.
- Update API ModifyCustomAgent: add response parameters Body.Data.RelatedSessionId.


2026-05-20 Version: 1.13.1
- Update API FileUploadCallback: add request parameters OssBucket.


2026-05-20 Version: 1.13.1
- Update API FileUploadCallback: add request parameters OssBucket.


2026-05-18 Version: 1.13.0
- Support API DeleteDocument.
- Support API DeleteDocumentChunks.
- Support API DescribeDocument.
- Support API DescribeKnowledgeBaseUploadSignature.
- Support API ListDocumentChunks.
- Support API ListDocuments.
- Support API ListKnowledgeBases.
- Support API UpdateDocument.
- Support API UpdateKnowledgeBase.
- Support API UploadDocument.
- Support API UpsertDocumentChunks.


2026-05-15 Version: 1.12.0
- Support API ConfigAirflow.
- Support API CreateDataAgentKnowledgeBase.
- Support API DeleteDataAgentKnowledgeBase.
- Support API DescribeKnowledgeBaseStats.
- Support API GetWorkspaceQuota.
- Support API ListAirflowVersions.
- Support API RedeployAirflow.
- Support API SetWorkspaceQuota.


2026-05-13 Version: 1.11.0
- Support API GetWorkspaceCodePublishSetting.
- Support API SetWorkspaceCodePublishSetting.
- Support API WorkspaceActionLog.
- Support API WorkspaceActionStatus.
- Support API WorkspaceCodePublish.


2026-05-13 Version: 1.10.8
- Update API ListFileUpload: add request parameters DownloadLinkExpire.


2026-05-07 Version: 1.10.7
- Update API CreateDataAgentWorkspace: add request parameters IsSessionShareEnabled.
- Update API CreateDataAgentWorkspace: add response parameters Body.Data.IsSessionShareEnabled.
- Update API GetDataAgentWorkspaceInfo: add response parameters Body.Data.IsSessionShareEnabled.
- Update API ListDataAgentWorkspace: add response parameters Body.Data.Content.$.IsSessionShareEnabled.
- Update API UpdateDataAgentSpaceInfo: add request parameters IsSessionShareEnabled.
- Update API UpdateDataAgentSpaceInfo: add response parameters Body.Data.IsSessionShareEnabled.


2026-04-28 Version: 1.10.6
- Update API ListDataCenterDatabase: add response parameters Body.Data.$.DownloadLink.
- Update API ListDataCenterDatabase: add response parameters Body.Data.$.IntranetDownloadLink.
- Update API ListDataCenterDatabase: add response parameters Body.Data.$.OssBucket.
- Update API ListDataCenterDatabase: add response parameters Body.Data.$.UseUserOssBucket.


2026-04-23 Version: 1.10.5
- Update API SendChatMessage: add request parameters SessionConfig.Mode.


2026-04-22 Version: 1.10.4
- Update API GetChatContent: add response parameters Body.timestamp.


2026-04-14 Version: 1.10.3
- Update API CreateCustomAgent: add request parameters KnowledgeConfigList.$.KbUuid.
- Update API CreateCustomAgent: add response parameters Body.Data.KnowledgeConfigList.$.KbUuid.
- Update API CreateDataAgentSession: add request parameters SessionConfig.KbUuidList.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.KbUuidList.
- Update API DescribeCustomAgent: add response parameters Body.Data.KnowledgeConfigList.$.KbUuid.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.KbUuidList.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.KnowledgeConfigList.$.KbUuid.
- Update API ModifyCustomAgent: add request parameters KnowledgeConfigList.$.KbUuid.
- Update API ModifyCustomAgent: add response parameters Body.Data.KnowledgeConfigList.$.KbUuid.


2026-04-14 Version: 1.10.3
- Update API CreateCustomAgent: add request parameters KnowledgeConfigList.$.KbUuid.
- Update API CreateCustomAgent: add response parameters Body.Data.KnowledgeConfigList.$.KbUuid.
- Update API CreateDataAgentSession: add request parameters SessionConfig.KbUuidList.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.KbUuidList.
- Update API DescribeCustomAgent: add response parameters Body.Data.KnowledgeConfigList.$.KbUuid.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.KbUuidList.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.KnowledgeConfigList.$.KbUuid.
- Update API ModifyCustomAgent: add request parameters KnowledgeConfigList.$.KbUuid.
- Update API ModifyCustomAgent: add response parameters Body.Data.KnowledgeConfigList.$.KbUuid.


2026-03-17 Version: 1.10.1
- Update API CreateCustomAgent: add request parameters CallbackConfig.
- Update API CreateCustomAgent: add response parameters Body.Data.CallbackConfig.
- Update API DescribeCustomAgent: add response parameters Body.Data.CallbackConfig.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.CallbackConfig.
- Update API ModifyCustomAgent: add request parameters CallbackConfig.
- Update API ModifyCustomAgent: add response parameters Body.Data.CallbackConfig.


2026-02-14 Version: 1.10.0
- Support API CreateCustomAgent.
- Support API DeleteCustomAgent.
- Support API ListDataCenterDatabase.
- Support API ListDataCenterTable.
- Support API ModifyCustomAgent.
- Support API OperateCustomAgent.


2026-02-13 Version: 1.9.0
- Support API ListDataAgentSession.


2026-02-10 Version: 1.8.7
- Update API CreateDataAgentSession: add request parameters SessionConfig.EncryptKey.
- Update API CreateDataAgentSession: add request parameters SessionConfig.EncryptType.
- Update API CreateDataAgentSession: add request parameters SessionConfig.ReportPageWidth.
- Update API CreateDataAgentSession: add request parameters SessionConfig.ReportWaterMark.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.EncryptKey.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.EncryptType.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.ReportPageWidth.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.ReportWaterMark.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.EncryptKey.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.EncryptType.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.ReportPageWidth.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.ReportWaterMark.


2026-02-03 Version: 1.8.6
- Update API SendChatMessage: add request parameters ParentSessionId.


2026-02-03 Version: 1.8.6
- Update API SendChatMessage: add request parameters ParentSessionId.


2026-02-03 Version: 1.8.6
- Update API SendChatMessage: add request parameters ParentSessionId.


2026-01-28 Version: 1.8.5
- Update API CreateDataAgentSession: add request parameters SessionConfig.UserOssBucket.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.UserOssBucket.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.UserOssBucket.


2026-01-20 Version: 1.8.4
- Update API DescribeCustomAgent: add response parameters Body.Data.DMSUnit.
- Update API DescribeCustomAgent: add response parameters Body.Data.IsScheduleTask.
- Update API DescribeCustomAgent: add response parameters Body.Data.NextRuntime.
- Update API DescribeCustomAgent: add response parameters Body.Data.ScheduleTaskConfig.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.DMSUnit.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.IsScheduleTask.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.NextRuntime.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.ScheduleTaskConfig.


2026-01-15 Version: 1.8.3
- Update API DescribeCustomAgent: add response parameters Body.Data.DefaultAgent.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.DefaultAgent.


2026-01-14 Version: 1.8.2
- Update API DescribeCustomAgent: add response parameters Body.Data.KnowledgeConfigList.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.KnowledgeConfigList.


2026-01-07 Version: 1.8.1
- Update API DescribeCustomAgent: add response parameters Body.Data.ExecutionConfig.SkipAskHuman.
- Update API DescribeCustomAgent: add response parameters Body.Data.ExecutionConfig.SkipSqlConfirm.
- Update API DescribeCustomAgent: add response parameters Body.Data.ExecutionConfig.SkipWebReportConfirm.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.ExecutionConfig.SkipAskHuman.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.ExecutionConfig.SkipSqlConfirm.
- Update API ListCustomAgent: add response parameters Body.Data.Content.$.ExecutionConfig.SkipWebReportConfirm.


2026-01-07 Version: 1.8.0
- Support API AddUserToDataAgentWorkspace.
- Support API CreateDataAgentWorkspace.
- Support API DeleteDataAgentWorkspace.
- Support API GetDataAgentSubAccountInfo.
- Support API GetDataAgentWorkspaceInfo.
- Support API ListDataAgentWorkspace.
- Support API ListDataAgentWorkspaceMember.
- Support API RemoveUserToDataAgentWorkspace.
- Support API UpdateDataAgentSpaceInfo.
- Support API UpdateDataAgentWorkspaceMemberRole.


2026-01-05 Version: 1.7.0
- Support API DeleteFileUpload.
- Support API DescribeFileUploadSignature.
- Support API FileUploadCallback.


2025-12-29 Version: 1.6.1
- Update API SendChatMessage: add request parameters SessionConfig.ReportWaterMark.


2025-12-29 Version: 1.6.1
- Update API SendChatMessage: add request parameters SessionConfig.ReportWaterMark.


2025-12-29 Version: 1.6.0
- Support API DescribeCustomAgent.
- Support API ListCustomAgent.


2025-12-17 Version: 1.5.0
- Support API ListFileUpload.


2025-12-16 Version: 1.4.1
- Update API CreateDataAgentSession: add request parameters SessionConfig.McpServerIds.
- Update API CreateDataAgentSession: add response parameters Body.Data.SessionConfig.McpServerIds.
- Update API DescribeDataAgentSession: add response parameters Body.Data.SessionConfig.McpServerIds.


2025-12-09 Version: 1.4.0
- Support API CreateDataAgentSession.
- Support API DescribeDataAgentSession.


2025-12-09 Version: 1.3.0
- Support API GetChatContent.
- Support API GetNotebookTaskStatus.
- Support API SendChatMessage.


2025-10-22 Version: 1.2.0
- Support API GetNotebookAndSubmitTask.


2025-08-26 Version: 1.1.0
- Support API BatchCreateDataLakePartitions.
- Support API BatchDeleteDataLakePartitions.
- Support API BatchUpdateDataLakePartitions.
- Support API CreateAirflow.
- Support API CreateDataLakeDatabase.
- Support API CreateDataLakeFunction.
- Support API CreateDataLakePartition.
- Support API CreateDataLakeTable.
- Support API DeleteAirflow.
- Support API DeleteDataLakeDatabase.
- Support API DeleteDataLakeFunction.
- Support API DeleteDataLakePartition.
- Support API DeleteDataLakeTable.
- Support API GetAirflow.
- Support API GetDataLakeCatalog.
- Support API GetDataLakeDatabase.
- Support API GetDataLakeFunction.
- Support API GetDataLakePartition.
- Support API GetDataLakeTable.
- Support API ListAirflows.
- Support API ListDataLakeCatalog.
- Support API ListDataLakeDatabase.
- Support API ListDataLakeFunction.
- Support API ListDataLakeFunctionName.
- Support API ListDataLakePartition.
- Support API ListDataLakePartitionByFilter.
- Support API ListDataLakePartitionName.
- Support API ListDataLakeTable.
- Support API ListDataLakeTableName.
- Support API ListDataLakeTablebaseInfo.
- Support API UpdateAirflow.
- Support API UpdateDataLakeDatabase.
- Support API UpdateDataLakeFunction.
- Support API UpdateDataLakePartition.
- Support API UpdateDataLakeTable.


2025-06-05 Version: 1.0.0
- Generated python 2025-04-14 for Dms.

