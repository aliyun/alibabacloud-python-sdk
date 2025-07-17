2025-07-17 Version: 7.2.6
- Update API GetProjectMember: add response parameters Body.ProjectMember.UserName.
- Update API ListProjectMembers: add response parameters Body.PagingInfo.ProjectMembers.$.UserName.


2025-07-07 Version: 7.2.5
- Generated python 2024-05-18 for dataworks-public.

2025-07-01 Version: 7.2.3
- Update API GetWorkflowInstance: add response parameters Body.WorkflowInstance.WorkflowParameters.
- Update API ListWorkflowInstances: add response parameters Body.PagingInfo.WorkflowInstances.$.WorkflowParameters.


2025-06-30 Version: 7.2.2
- Generated python 2024-05-18 for dataworks-public.

2025-06-27 Version: 7.2.1
- Update API CreateWorkflowInstances: add request parameters DefaultRunProperties.PriorityWeightStrategy.


2025-06-19 Version: 7.2.0
- Support API GetRerunWorkflowInstancesResult.
- Support API RerunWorkflowInstances.
- Update API GetTaskInstance: add response parameters Body.TaskInstance.WaitingResourceTime.
- Update API GetTaskInstance: add response parameters Body.TaskInstance.WaitingTriggerTime.
- Update API ListTaskInstances: add response parameters Body.PagingInfo.TaskInstances.$.ScriptParameters.
- Update API ListTaskInstances: add response parameters Body.PagingInfo.TaskInstances.$.WaitingResourceTime.
- Update API ListTaskInstances: add response parameters Body.PagingInfo.TaskInstances.$.WaitingTriggerTime.


2025-06-09 Version: 7.1.3
- Update API CreateWorkflowInstances: add request parameters DefaultRunProperties.Priority.


2025-06-05 Version: 7.1.2
- Update API ListFunctions: add request parameters Name.
- Update API ListNodes: add request parameters Name.
- Update API ListResources: add request parameters Name.
- Update API ListWorkflowDefinitions: add request parameters Name.


2025-06-03 Version: 7.1.1
- Generated python 2024-05-18 for dataworks-public.

2025-05-23 Version: 7.1.0
- Support API CreateBusiness.
- Support API CreateFile.
- Support API CreateFolder.
- Support API CreateResourceFile.
- Support API CreateUdfFile.
- Support API DeleteBusiness.
- Support API DeleteFile.
- Support API DeleteFolder.
- Support API DeployFile.
- Support API EstablishRelationTableToBusiness.
- Support API GetBusiness.
- Support API GetDeploymentPackage.
- Support API GetFile.
- Support API GetFileVersion.
- Support API GetFolder.
- Support API GetIDEEventDetail.
- Support API ListBusiness.
- Support API ListDeploymentPackageFiles.
- Support API ListDeploymentPackages.
- Support API ListFileVersions.
- Support API ListFiles.
- Support API ListFolders.
- Support API ListPipelineRunItems.
- Support API SubmitFile.
- Support API UpdateBusiness.
- Support API UpdateFile.
- Support API UpdateFolder.
- Support API UpdateIDEEventResult.
- Support API UpdateUdfFile.
- Update API ListTaskInstances: add request parameters Status.


2025-05-15 Version: 7.0.1
- Update API UpdateWorkflow: add request parameters InstanceMode.


2025-05-15 Version: 7.0.1
- Update API UpdateWorkflow: add request parameters InstanceMode.


2025-05-15 Version: 7.0.1
- Update API UpdateWorkflow: add request parameters InstanceMode.


2025-05-15 Version: 7.0.1
- Update API UpdateWorkflow: add request parameters InstanceMode.


2025-05-09 Version: 7.0.0
- Support API AbolishPipelineRun.
- Support API CreatePipelineRun.
- Support API ExecPipelineRunStage.
- Support API GetPipelineRun.
- Support API ListPipelineRuns.
- Delete API AbolishDeployment.
- Delete API CreateDeployment.
- Delete API ExecDeploymentStage.
- Delete API GetDeployment.
- Delete API ListDeployments.
- Update API CreateResource: add request parameters ResourceFile.
- Update API UpdateResource: add request parameters ResourceFile.


2025-04-14 Version: 6.2.0
- Support API AddEntityIntoMetaCollection.
- Support API CreateLineageRelationship.
- Support API CreateMetaCollection.
- Support API DeleteLineageRelationship.
- Support API DeleteMetaCollection.
- Support API GetCatalog.
- Support API GetColumn.
- Support API GetDatabase.
- Support API GetLineageRelationship.
- Support API GetMetaCollection.
- Support API GetPartition.
- Support API GetSchema.
- Support API GetTable.
- Support API ListCatalogs.
- Support API ListColumns.
- Support API ListCrawlerTypes.
- Support API ListDatabases.
- Support API ListEntitiesInMetaCollection.
- Support API ListLineageRelationships.
- Support API ListLineages.
- Support API ListMetaCollections.
- Support API ListPartitions.
- Support API ListSchemas.
- Support API ListTables.
- Support API RemoveEntityFromMetaCollection.
- Support API UpdateColumnBusinessMetadata.
- Support API UpdateMetaCollection.
- Support API UpdateTableBusinessMetadata.


2025-04-02 Version: 6.1.3
- Update API ListNodes: add response parameters Body.PagingInfo.Nodes.$.RuntimeResource.ResourceGroup.


2025-03-31 Version: 6.1.2
- Update API GetDataQualityEvaluationTaskInstance: add response parameters Body.DataQualityEvaluationTaskInstance.Results.
- Update API ListDataQualityEvaluationTasks: add response parameters Body.PagingInfo.DataQualityEvaluationTasks.$.DataSourceId.


2025-03-27 Version: 6.1.1
- Update API CreateDIJob: add request parameters JobType.
- Update API GetDIJob: add response parameters Body.PagingInfo.JobType.


2025-03-27 Version: 6.1.1
- Update API CreateDIJob: add request parameters JobType.
- Update API GetDIJob: add response parameters Body.PagingInfo.JobType.


2025-03-20 Version: 6.1.0
- Support API DeleteCertificate.
- Support API GetCertificate.
- Support API ImportCertificate.
- Support API ListCertificates.
- Support API TestDataSourceConnectivity.
- Update API CreateRoute: add param ResourceGroupId.
- Update API CreateWorkflowInstances: update param DefaultRunProperties.
- Update API CreateWorkflowInstances: update param Type.
- Update API ExecuteAdhocWorkflowInstance: update param BizDate.
- Update API ListResourceGroups: update response param.


2025-02-18 Version: 6.0.2
- Update API ExecuteAdhocWorkflowInstance: update param EnvType.
- Update API GetDIJobLog: add param NodeType.
- Update API GetDIJobLog: add param PageNumber.
- Update API GetNode: update response param.
- Update API GetWorkflowDefinition: add param IncludeScriptContent.
- Update API GetWorkflowDefinition: update response param.
- Update API ImportWorkflowDefinition: update param RegionId.
- Update API ListResourceGroups: update param Statuses.
- Update API ListResourceGroups: update response param.


2025-01-23 Version: 6.0.1
- Update API ListRoutes: add param ResourceGroupId.
- Update API ListRoutes: update param NetworkId.


2025-01-22 Version: 6.0.0
- Support API BatchUpdateTasks.
- Support API CreateDataAssetTag.
- Support API CreateWorkflowInstances.
- Support API DeleteDataAssetTag.
- Support API DeleteWorkflow.
- Support API ExecuteAdhocWorkflowInstance.
- Support API GetCreateWorkflowInstancesResult.
- Support API GetWorkflow.
- Support API GetWorkflowInstance.
- Support API ListDataAssetTags.
- Support API ListDataAssets.
- Support API ListDataQualityRuleTemplates.
- Support API ListWorkflowInstances.
- Support API ListWorkflows.
- Support API StartWorkflowInstances.
- Support API StopWorkflowInstances.
- Support API TagDataAssets.
- Support API UnTagDataAssets.
- Support API UpdateDataAssetTag.
- Support API UpdateTask.
- Support API UpdateWorkflow.
- Delete API ListDataQualityRuleTemplate.
- Update API AbolishDeployment: update param ProjectId.
- Update API AttachDataQualityRulesToEvaluationTask: update param DataQualityRuleIds.
- Update API CloneDataSource: update param CloneDataSourceName.
- Update API CloneDataSource: update param Id.
- Update API CreateAlertRule: update param TriggerCondition.
- Update API CreateDIAlarmRule: update param NotificationSettings.
- Update API CreateDIAlarmRule: update param TriggerConditions.
- Update API CreateDIAlarmRule: update response param.
- Update API CreateDIJob: add param Name.
- Update API CreateDIJob: update param JobName.
- Update API CreateDIJob: update response param.
- Update API CreateDataQualityEvaluationTask: update param DataQualityRules.
- Update API CreateDataQualityEvaluationTask: update param Description.
- Update API CreateDataQualityEvaluationTask: update param Name.
- Update API CreateDataQualityEvaluationTask: update param Notifications.
- Update API CreateDataQualityEvaluationTask: update param ProjectId.
- Update API CreateDataQualityEvaluationTask: update param Target.
- Update API CreateDataQualityRule: update param Description.
- Update API CreateDataQualityRule: update param Enabled.
- Update API CreateDataQualityRule: update param Name.
- Update API CreateDataQualityRule: update param ProjectId.
- Update API CreateDataQualityRule: update param SamplingConfig.
- Update API CreateDataQualityRule: update param Severity.
- Update API CreateDataQualityRule: update param TemplateCode.
- Update API CreateDataQualityRuleTemplate: update param Name.
- Update API CreateDataQualityRuleTemplate: update param ProjectId.
- Update API CreateDataQualityRuleTemplate: update param SamplingConfig.
- Update API CreateDataQualityRuleTemplate: update param VisibleScope.
- Update API CreateDeployment: update param ProjectId.
- Update API CreateFunction: update param ProjectId.
- Update API CreateFunction: update response param.
- Update API CreateNetwork: update response param.
- Update API CreateNode: update param ContainerId.
- Update API CreateNode: update param ProjectId.
- Update API CreateNode: update response param.
- Update API CreateProject: update response param.
- Update API CreateResource: update param ProjectId.
- Update API CreateResource: update response param.
- Update API CreateResourceGroup: add param AliyunResourceGroupId.
- Update API CreateResourceGroup: add param AliyunResourceTags.
- Update API CreateResourceGroup: add param AutoRenewEnabled.
- Update API CreateResourceGroup: delete param AutoRenew.
- Update API CreateRoute: update response param.
- Update API CreateWorkflowDefinition: update param ProjectId.
- Update API CreateWorkflowDefinition: update response param.
- Update API DeleteDIAlarmRule: add param Id.
- Update API DeleteDIAlarmRule: update param DIAlarmRuleId.
- Update API DeleteDIAlarmRule: update param DIJobId.
- Update API DeleteDIJob: add param Id.
- Update API DeleteDIJob: update param DIJobId.
- Update API DeleteDataQualityEvaluationTask: update param Id.
- Update API DeleteDataQualityEvaluationTask: update param ProjectId.
- Update API DeleteDataQualityRule: update param Id.
- Update API DeleteDataQualityRule: update param ProjectId.
- Update API DeleteDataQualityRuleTemplate: update param Code.
- Update API DeleteDataQualityRuleTemplate: update param ProjectId.
- Update API DeleteDataSource: update param Id.
- Update API DeleteFunction: update param Id.
- Update API DeleteFunction: update param ProjectId.
- Update API DeleteNode: update param Id.
- Update API DeleteNode: update param ProjectId.
- Update API DeleteResource: update param Id.
- Update API DeleteResource: update param ProjectId.
- Update API DeleteWorkflowDefinition: update param Id.
- Update API DeleteWorkflowDefinition: update param ProjectId.
- Update API DetachDataQualityRulesFromEvaluationTask: update param DataQualityRuleIds.
- Update API ExecDeploymentStage: update param ProjectId.
- Update API GetAlertRule: update response param.
- Update API GetDIJob: add param Id.
- Update API GetDIJob: update param DIJobId.
- Update API GetDIJob: update response param.
- Update API GetDIJobLog: add param Id.
- Update API GetDIJobLog: update param DIJobId.
- Update API GetDataQualityEvaluationTask: update param Id.
- Update API GetDataQualityEvaluationTask: update response param.
- Update API GetDataQualityEvaluationTaskInstance: update param Id.
- Update API GetDataQualityRule: update param Id.
- Update API GetDataQualityRule: update response param.
- Update API GetDataQualityRuleTemplate: update param Code.
- Update API GetDataQualityRuleTemplate: update response param.
- Update API GetDeployment: update param ProjectId.
- Update API GetDeployment: update response param.
- Update API GetFunction: update param Id.
- Update API GetFunction: update param ProjectId.
- Update API GetFunction: update response param.
- Update API GetNode: update param Id.
- Update API GetNode: update param ProjectId.
- Update API GetNode: update response param.
- Update API GetResource: update param Id.
- Update API GetResource: update param ProjectId.
- Update API GetResource: update response param.
- Update API GetResourceGroup: update response param.
- Update API GetTask: update response param.
- Update API GetTaskInstance: update response param.
- Update API GetWorkflowDefinition: update param Id.
- Update API GetWorkflowDefinition: update param ProjectId.
- Update API GetWorkflowDefinition: update response param.
- Update API ImportWorkflowDefinition: update param RegionId.
- Update API ImportWorkflowDefinition: update param ProjectId.
- Update API ImportWorkflowDefinition: update param Spec.
- Update API ListAlertRules: update response param.
- Update API ListDIAlarmRules: update response param.
- Update API ListDIJobs: update response param.
- Update API ListDataQualityEvaluationTaskInstances: update param ProjectId.
- Update API ListDataQualityEvaluationTaskInstances: update response param.
- Update API ListDataQualityEvaluationTasks: update param ProjectId.
- Update API ListDataQualityEvaluationTasks: update response param.
- Update API ListDataQualityResults: update param ProjectId.
- Update API ListDataQualityResults: update response param.
- Update API ListDataQualityRules: update param ProjectId.
- Update API ListDataQualityRules: update response param.
- Update API ListDataSourceSharedRules: update response param.
- Update API ListDataSources: update response param.
- Update API ListDeployments: update param ProjectId.
- Update API ListDeployments: update response param.
- Update API ListDownstreamTaskInstances: update response param.
- Update API ListDownstreamTasks: update response param.
- Update API ListFunctions: update param ProjectId.
- Update API ListFunctions: update response param.
- Update API ListNetworks: add param PageNumber.
- Update API ListNetworks: add param PageSize.
- Update API ListNetworks: add param SortBy.
- Update API ListNetworks: update response param.
- Update API ListNodeDependencies: update param Id.
- Update API ListNodeDependencies: update param ProjectId.
- Update API ListNodeDependencies: update response param.
- Update API ListNodes: update param ContainerId.
- Update API ListNodes: update param ProjectId.
- Update API ListNodes: update response param.
- Update API ListResourceGroups: add param AliyunResourceGroupId.
- Update API ListResourceGroups: add param AliyunResourceTags.
- Update API ListResourceGroups: add param PageNumber.
- Update API ListResourceGroups: add param PageSize.
- Update API ListResourceGroups: add param SortBy.
- Update API ListResourceGroups: update param Statuses.
- Update API ListResourceGroups: update response param.
- Update API ListResources: update param ProjectId.
- Update API ListResources: update response param.
- Update API ListRoutes: add param PageNumber.
- Update API ListRoutes: add param PageSize.
- Update API ListRoutes: add param SortBy.
- Update API ListRoutes: update response param.
- Update API ListTaskInstances: update response param.
- Update API ListTasks: add param Ids.
- Update API ListTasks: update response param.
- Update API ListUpstreamTaskInstances: update response param.
- Update API ListUpstreamTasks: update param ProjectEnv.
- Update API ListUpstreamTasks: update response param.
- Update API ListWorkflowDefinitions: update param ProjectId.
- Update API ListWorkflowDefinitions: update response param.
- Update API MoveFunction: update param Id.
- Update API MoveFunction: update param ProjectId.
- Update API MoveNode: update param Id.
- Update API MoveNode: update param ProjectId.
- Update API MoveResource: update param Id.
- Update API MoveResource: update param ProjectId.
- Update API MoveWorkflowDefinition: update param Id.
- Update API MoveWorkflowDefinition: update param ProjectId.
- Update API RenameFunction: update param Id.
- Update API RenameFunction: update param ProjectId.
- Update API RenameNode: update param Id.
- Update API RenameNode: update param ProjectId.
- Update API RenameResource: update param Id.
- Update API RenameResource: update param ProjectId.
- Update API RenameWorkflowDefinition: update param Id.
- Update API RenameWorkflowDefinition: update param ProjectId.
- Update API StartDIJob: add param Id.
- Update API StartDIJob: update param DIJobId.
- Update API StartDIJob: update param RealtimeStartSettings.
- Update API StopDIJob: add param Id.
- Update API StopDIJob: update param DIJobId.
- Update API TriggerSchedulerTaskInstance: add param EnvType.
- Update API UpdateAlertRule: update param TriggerCondition.
- Update API UpdateDIAlarmRule: add param Id.
- Update API UpdateDIAlarmRule: update param DIAlarmRuleId.
- Update API UpdateDIAlarmRule: update param DIJobId.
- Update API UpdateDIAlarmRule: update param NotificationSettings.
- Update API UpdateDIAlarmRule: update param TriggerConditions.
- Update API UpdateDIJob: add param Id.
- Update API UpdateDIJob: update param DIJobId.
- Update API UpdateDIJob: update param ResourceSettings.
- Update API UpdateDataQualityEvaluationTask: update param DataQualityRules.
- Update API UpdateDataQualityEvaluationTask: update param Description.
- Update API UpdateDataQualityEvaluationTask: update param Name.
- Update API UpdateDataQualityEvaluationTask: update param Notifications.
- Update API UpdateDataQualityEvaluationTask: update param Target.
- Update API UpdateDataQualityRule: delete param Target.
- Update API UpdateDataQualityRule: update param CheckingConfig.
- Update API UpdateDataQualityRule: update param Description.
- Update API UpdateDataQualityRule: update param Enabled.
- Update API UpdateDataQualityRule: update param Id.
- Update API UpdateDataQualityRule: update param Name.
- Update API UpdateDataQualityRule: update param ProjectId.
- Update API UpdateDataQualityRule: update param SamplingConfig.
- Update API UpdateDataQualityRule: update param Severity.
- Update API UpdateDataQualityRuleTemplate: update param Code.
- Update API UpdateDataQualityRuleTemplate: update param Name.
- Update API UpdateDataQualityRuleTemplate: update param SamplingConfig.
- Update API UpdateFunction: update param Id.
- Update API UpdateFunction: update param ProjectId.
- Update API UpdateNode: update param Id.
- Update API UpdateNode: update param ProjectId.
- Update API UpdateResource: update param Id.
- Update API UpdateResource: update param ProjectId.
- Update API UpdateResourceGroup: add param AliyunResourceGroupId.
- Update API UpdateTaskInstances: update param RegionId.
- Update API UpdateWorkflowDefinition: update param Id.
- Update API UpdateWorkflowDefinition: update param ProjectId.


2025-01-14 Version: 5.0.0
- Support API CreateDataAssetTag.
- Support API DeleteDataAssetTag.
- Support API ListDataAssetTags.
- Support API ListDataAssets.
- Support API ListDataQualityRuleTemplates.
- Support API TagDataAssets.
- Support API UnTagDataAssets.
- Support API UpdateDataAssetTag.
- Delete API ListDataQualityRuleTemplate.
- Update API AbolishDeployment: update param ProjectId.
- Update API AttachDataQualityRulesToEvaluationTask: update param DataQualityRuleIds.
- Update API CloneDataSource: update param CloneDataSourceName.
- Update API CloneDataSource: update param Id.
- Update API CreateAlertRule: update param TriggerCondition.
- Update API CreateDIAlarmRule: update param NotificationSettings.
- Update API CreateDIAlarmRule: update param TriggerConditions.
- Update API CreateDIAlarmRule: update response param.
- Update API CreateDIJob: add param Name.
- Update API CreateDIJob: update param JobName.
- Update API CreateDIJob: update response param.
- Update API CreateDataQualityEvaluationTask: update param DataQualityRules.
- Update API CreateDataQualityEvaluationTask: update param Description.
- Update API CreateDataQualityEvaluationTask: update param Name.
- Update API CreateDataQualityEvaluationTask: update param Notifications.
- Update API CreateDataQualityEvaluationTask: update param ProjectId.
- Update API CreateDataQualityEvaluationTask: update param Target.
- Update API CreateDataQualityRule: update param Description.
- Update API CreateDataQualityRule: update param Enabled.
- Update API CreateDataQualityRule: update param Name.
- Update API CreateDataQualityRule: update param ProjectId.
- Update API CreateDataQualityRule: update param SamplingConfig.
- Update API CreateDataQualityRule: update param Severity.
- Update API CreateDataQualityRule: update param TemplateCode.
- Update API CreateDataQualityRuleTemplate: update param Name.
- Update API CreateDataQualityRuleTemplate: update param ProjectId.
- Update API CreateDataQualityRuleTemplate: update param SamplingConfig.
- Update API CreateDataQualityRuleTemplate: update param VisibleScope.
- Update API CreateDeployment: update param ProjectId.
- Update API CreateFunction: update param ProjectId.
- Update API CreateFunction: update response param.
- Update API CreateNetwork: update response param.
- Update API CreateNode: update param ContainerId.
- Update API CreateNode: update param ProjectId.
- Update API CreateNode: update response param.
- Update API CreateProject: update response param.
- Update API CreateResource: update param ProjectId.
- Update API CreateResource: update response param.
- Update API CreateResourceGroup: add param AliyunResourceGroupId.
- Update API CreateResourceGroup: add param AliyunResourceTags.
- Update API CreateResourceGroup: add param AutoRenewEnabled.
- Update API CreateResourceGroup: delete param AutoRenew.
- Update API CreateRoute: update response param.
- Update API CreateWorkflowDefinition: update param ProjectId.
- Update API CreateWorkflowDefinition: update response param.
- Update API DeleteDIAlarmRule: add param Id.
- Update API DeleteDIAlarmRule: update param DIAlarmRuleId.
- Update API DeleteDIAlarmRule: update param DIJobId.
- Update API DeleteDIJob: add param Id.
- Update API DeleteDIJob: update param DIJobId.
- Update API DeleteDataQualityEvaluationTask: update param Id.
- Update API DeleteDataQualityEvaluationTask: update param ProjectId.
- Update API DeleteDataQualityRule: update param Id.
- Update API DeleteDataQualityRule: update param ProjectId.
- Update API DeleteDataQualityRuleTemplate: update param Code.
- Update API DeleteDataQualityRuleTemplate: update param ProjectId.
- Update API DeleteDataSource: update param Id.
- Update API DeleteFunction: update param Id.
- Update API DeleteFunction: update param ProjectId.
- Update API DeleteNode: update param Id.
- Update API DeleteNode: update param ProjectId.
- Update API DeleteResource: update param Id.
- Update API DeleteResource: update param ProjectId.
- Update API DeleteWorkflowDefinition: update param Id.
- Update API DeleteWorkflowDefinition: update param ProjectId.
- Update API DetachDataQualityRulesFromEvaluationTask: update param DataQualityRuleIds.
- Update API ExecDeploymentStage: update param ProjectId.
- Update API GetAlertRule: update response param.
- Update API GetDIJob: add param Id.
- Update API GetDIJob: update param DIJobId.
- Update API GetDIJob: update response param.
- Update API GetDIJobLog: add param Id.
- Update API GetDIJobLog: update param DIJobId.
- Update API GetDataQualityEvaluationTask: update param Id.
- Update API GetDataQualityEvaluationTaskInstance: update param Id.
- Update API GetDataQualityRule: update param Id.
- Update API GetDataQualityRule: update response param.
- Update API GetDataQualityRuleTemplate: update param Code.
- Update API GetDataQualityRuleTemplate: update response param.
- Update API GetDeployment: update param ProjectId.
- Update API GetDeployment: update response param.
- Update API GetFunction: update param Id.
- Update API GetFunction: update param ProjectId.
- Update API GetFunction: update response param.
- Update API GetNode: update param Id.
- Update API GetNode: update param ProjectId.
- Update API GetNode: update response param.
- Update API GetResource: update param Id.
- Update API GetResource: update param ProjectId.
- Update API GetResource: update response param.
- Update API GetResourceGroup: update response param.
- Update API GetTask: update response param.
- Update API GetWorkflowDefinition: update param Id.
- Update API GetWorkflowDefinition: update param ProjectId.
- Update API GetWorkflowDefinition: update response param.
- Update API ImportWorkflowDefinition: update param RegionId.
- Update API ImportWorkflowDefinition: update param ProjectId.
- Update API ImportWorkflowDefinition: update param Spec.
- Update API ListAlertRules: update response param.
- Update API ListDIAlarmRules: update response param.
- Update API ListDIJobs: update response param.
- Update API ListDataQualityEvaluationTaskInstances: update param ProjectId.
- Update API ListDataQualityEvaluationTaskInstances: update response param.
- Update API ListDataQualityEvaluationTasks: update param ProjectId.
- Update API ListDataQualityEvaluationTasks: update response param.
- Update API ListDataQualityResults: update param ProjectId.
- Update API ListDataQualityResults: update response param.
- Update API ListDataQualityRules: update param ProjectId.
- Update API ListDataQualityRules: update response param.
- Update API ListDataSourceSharedRules: update response param.
- Update API ListDataSources: update response param.
- Update API ListDeployments: update param ProjectId.
- Update API ListDeployments: update response param.
- Update API ListDownstreamTaskInstances: update response param.
- Update API ListDownstreamTasks: update response param.
- Update API ListFunctions: update param ProjectId.
- Update API ListFunctions: update response param.
- Update API ListNetworks: add param PageNumber.
- Update API ListNetworks: add param PageSize.
- Update API ListNetworks: add param SortBy.
- Update API ListNetworks: update response param.
- Update API ListNodeDependencies: update param Id.
- Update API ListNodeDependencies: update param ProjectId.
- Update API ListNodeDependencies: update response param.
- Update API ListNodes: update param ContainerId.
- Update API ListNodes: update param ProjectId.
- Update API ListNodes: update response param.
- Update API ListResourceGroups: add param AliyunResourceGroupId.
- Update API ListResourceGroups: add param AliyunResourceTags.
- Update API ListResourceGroups: add param PageNumber.
- Update API ListResourceGroups: add param PageSize.
- Update API ListResourceGroups: add param SortBy.
- Update API ListResourceGroups: update param Statuses.
- Update API ListResourceGroups: update response param.
- Update API ListResources: update param ProjectId.
- Update API ListResources: update response param.
- Update API ListRoutes: add param PageNumber.
- Update API ListRoutes: add param PageSize.
- Update API ListRoutes: add param SortBy.
- Update API ListRoutes: update response param.
- Update API ListTasks: update response param.
- Update API ListUpstreamTaskInstances: update response param.
- Update API ListUpstreamTasks: update param ProjectEnv.
- Update API ListUpstreamTasks: update response param.
- Update API ListWorkflowDefinitions: update param ProjectId.
- Update API ListWorkflowDefinitions: update response param.
- Update API MoveFunction: update param Id.
- Update API MoveFunction: update param ProjectId.
- Update API MoveNode: update param Id.
- Update API MoveNode: update param ProjectId.
- Update API MoveResource: update param Id.
- Update API MoveResource: update param ProjectId.
- Update API MoveWorkflowDefinition: update param Id.
- Update API MoveWorkflowDefinition: update param ProjectId.
- Update API RenameFunction: update param Id.
- Update API RenameFunction: update param ProjectId.
- Update API RenameNode: update param Id.
- Update API RenameNode: update param ProjectId.
- Update API RenameResource: update param Id.
- Update API RenameResource: update param ProjectId.
- Update API RenameWorkflowDefinition: update param Id.
- Update API RenameWorkflowDefinition: update param ProjectId.
- Update API StartDIJob: add param Id.
- Update API StartDIJob: update param DIJobId.
- Update API StartDIJob: update param RealtimeStartSettings.
- Update API StopDIJob: add param Id.
- Update API StopDIJob: update param DIJobId.
- Update API TriggerSchedulerTaskInstance: add param EnvType.
- Update API UpdateAlertRule: update param TriggerCondition.
- Update API UpdateDIAlarmRule: add param Id.
- Update API UpdateDIAlarmRule: update param DIAlarmRuleId.
- Update API UpdateDIAlarmRule: update param DIJobId.
- Update API UpdateDIAlarmRule: update param NotificationSettings.
- Update API UpdateDIAlarmRule: update param TriggerConditions.
- Update API UpdateDIJob: add param Id.
- Update API UpdateDIJob: update param DIJobId.
- Update API UpdateDIJob: update param ResourceSettings.
- Update API UpdateDataQualityEvaluationTask: update param DataQualityRules.
- Update API UpdateDataQualityEvaluationTask: update param Description.
- Update API UpdateDataQualityEvaluationTask: update param Name.
- Update API UpdateDataQualityEvaluationTask: update param Notifications.
- Update API UpdateDataQualityEvaluationTask: update param Target.
- Update API UpdateDataQualityRule: update param CheckingConfig.
- Update API UpdateDataQualityRule: update param Description.
- Update API UpdateDataQualityRule: update param Enabled.
- Update API UpdateDataQualityRule: update param Id.
- Update API UpdateDataQualityRule: update param Name.
- Update API UpdateDataQualityRule: update param ProjectId.
- Update API UpdateDataQualityRule: update param SamplingConfig.
- Update API UpdateDataQualityRule: update param Severity.
- Update API UpdateDataQualityRule: update param Target.
- Update API UpdateDataQualityRuleTemplate: update param Code.
- Update API UpdateDataQualityRuleTemplate: update param Name.
- Update API UpdateDataQualityRuleTemplate: update param SamplingConfig.
- Update API UpdateFunction: update param Id.
- Update API UpdateFunction: update param ProjectId.
- Update API UpdateNode: update param Id.
- Update API UpdateNode: update param ProjectId.
- Update API UpdateResource: update param Id.
- Update API UpdateResource: update param ProjectId.
- Update API UpdateResourceGroup: add param AliyunResourceGroupId.
- Update API UpdateWorkflowDefinition: update param Id.
- Update API UpdateWorkflowDefinition: update param ProjectId.


2024-12-12 Version: 4.0.0
- Update API UpdateDIJob: update param ResourceSettings.


2024-12-04 Version: 3.1.0
- Support API AttachDataQualityRulesToEvaluationTask.
- Support API CreateDataQualityEvaluationTask.
- Support API CreateDataQualityEvaluationTaskInstance.
- Support API CreateDataQualityRule.
- Support API CreateDataQualityRuleTemplate.
- Support API DeleteDataQualityEvaluationTask.
- Support API DeleteDataQualityRule.
- Support API DeleteDataQualityRuleTemplate.
- Support API DetachDataQualityRulesFromEvaluationTask.
- Support API GetDataQualityEvaluationTask.
- Support API GetDataQualityEvaluationTaskInstance.
- Support API GetDataQualityRule.
- Support API GetDataQualityRuleTemplate.
- Support API ListDataQualityRuleTemplate.
- Support API UpdateDataQualityEvaluationTask.
- Support API UpdateDataQualityRule.
- Support API UpdateDataQualityRuleTemplate.
- Update API ListDataQualityRules: update response param.


2024-11-21 Version: 3.0.0
- Support API CreateAlertRule.
- Support API DeleteAlertRule.
- Support API GetAlertRule.
- Support API ListAlertRules.
- Support API UpdateAlertRule.
- Update API GetTask: update response param.
- Update API GetTaskInstance: update response param.
- Update API ListDataQualityEvaluationTaskInstances: update response param.
- Update API ListDataQualityEvaluationTasks: update response param.
- Update API ListDataQualityResults: update response param.
- Update API ListDataQualityRules: update response param.
- Update API ListDownstreamTaskInstances: update response param.
- Update API ListDownstreamTasks: update response param.
- Update API ListTaskInstances: add param TriggerRecurrence.
- Update API ListTaskInstances: add param TriggerType.
- Update API ListTaskInstances: update param TaskType.
- Update API ListTaskInstances: update response param.
- Update API ListTasks: update response param.
- Update API ListUpstreamTaskInstances: update response param.
- Update API ListUpstreamTasks: update response param.


2024-10-30 Version: 2.1.1
- Generated python 2024-05-18 for dataworks-public.

2024-10-28 Version: 2.1.0
- Support API CreateProjectMember.
- Support API DeleteProjectMember.
- Support API DeleteTask.
- Support API GetProjectMember.
- Support API GetTask.
- Support API GetTaskInstance.
- Support API GetTaskInstanceLog.
- Support API GrantMemberProjectRoles.
- Support API ListDataQualityEvaluationTaskInstances.
- Support API ListDataQualityEvaluationTasks.
- Support API ListDataQualityResults.
- Support API ListDataQualityRules.
- Support API ListDownstreamTaskInstances.
- Support API ListDownstreamTasks.
- Support API ListProjectMembers.
- Support API ListTaskInstanceOperationLogs.
- Support API ListTaskInstances.
- Support API ListTaskOperationLogs.
- Support API ListTasks.
- Support API ListUpstreamTaskInstances.
- Support API ListUpstreamTasks.
- Support API RemoveTaskInstanceDependencies.
- Support API RerunTaskInstances.
- Support API ResumeTaskInstances.
- Support API RevokeMemberProjectRoles.
- Support API SetSuccessTaskInstances.
- Support API StopTaskInstances.
- Support API SuspendTaskInstances.
- Support API TriggerSchedulerTaskInstance.
- Support API UpdateTaskInstances.
- Update API ListDIJobs: update response param.


2024-10-18 Version: 2.0.0
- Support API AssociateProjectToResourceGroup.
- Support API CloneDataSource.
- Support API CreateDIAlarmRule.
- Support API CreateDIJob.
- Support API CreateDataSource.
- Support API CreateDataSourceSharedRule.
- Support API CreateNetwork.
- Support API CreateProject.
- Support API CreateResourceGroup.
- Support API CreateRoute.
- Support API DeleteDIAlarmRule.
- Support API DeleteDIJob.
- Support API DeleteDataSource.
- Support API DeleteDataSourceSharedRule.
- Support API DeleteNetwork.
- Support API DeleteProject.
- Support API DeleteResourceGroup.
- Support API DeleteRoute.
- Support API DissociateProjectFromResourceGroup.
- Support API GetDIJob.
- Support API GetDIJobLog.
- Support API GetDataSource.
- Support API GetJobStatus.
- Support API GetNetwork.
- Support API GetProject.
- Support API GetProjectRole.
- Support API GetResourceGroup.
- Support API GetRoute.
- Support API ImportWorkflowDefinition.
- Support API ListDIAlarmRules.
- Support API ListDIJobEvents.
- Support API ListDIJobMetrics.
- Support API ListDIJobRunDetails.
- Support API ListDIJobs.
- Support API ListDataSourceSharedRules.
- Support API ListDataSources.
- Support API ListNetworks.
- Support API ListProjectRoles.
- Support API ListProjects.
- Support API ListResourceGroups.
- Support API ListRoutes.
- Support API StartDIJob.
- Support API StopDIJob.
- Support API UpdateDIAlarmRule.
- Support API UpdateDIJob.
- Support API UpdateDataSource.
- Support API UpdateProject.
- Support API UpdateResourceGroup.
- Support API UpdateRoute.
- Update API ListNodes: add param Recurrence.
- Update API ListNodes: delete param Rerurrence.


2024-10-10 Version: 1.1.0
- Support API CloneDataSource.
- Support API CreateDIJob.
- Support API CreateDataSource.
- Support API CreateDataSourceSharedRule.
- Support API CreateProject.
- Support API DeleteDIJob.
- Support API DeleteDataSource.
- Support API DeleteDataSourceSharedRule.
- Support API DeleteProject.
- Support API GetDIJob.
- Support API GetDIJobLog.
- Support API GetDataSource.
- Support API GetProject.
- Support API ListDIJobEvents.
- Support API ListDIJobMetrics.
- Support API ListDIJobs.
- Support API ListDataSourceSharedRules.
- Support API ListDataSources.
- Support API ListProjects.
- Support API StartDIJob.
- Support API UpdateDIJob.
- Support API UpdateDataSource.
- Support API UpdateProject.


2024-09-19 Version: 1.0.0
- Generated python 2024-05-18 for dataworks-public.

