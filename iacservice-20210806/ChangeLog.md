2026-01-21 Version: 2.2.0
- Support API ManageTerraformState.


2026-01-14 Version: 2.1.3
- Update API ListRegistryModules: add request parameters status.


2025-12-04 Version: 2.1.2
- Update API GetJob: add response parameters Body.job.jobType.
- Update API ListJobs: add request parameters jobType.


2025-12-03 Version: 2.1.1
- Update API GetJob: add response parameters Body.job.statusDetail.errorMessage.


2025-12-03 Version: 2.1.0
- Support API GenerateModule.
- Update API GetJob: add response parameters Body.job.config.hasConfigProactive.


2025-10-29 Version: 2.0.1
- Update API GetJob: add response parameters Body.job.logFile.
- Update API GetJob: add response parameters Body.job.outputJsonPlan.
- Update API ListModules: add request parameters moduleName.


2025-08-22 Version: 2.0.0
- Support API AddSharedAccounts.
- Support API CreateRegistryModule.
- Support API CreateRegistryNamespace.
- Support API DeleteRegistryModule.
- Support API DeleteRegistryModuleVersion.
- Support API DeleteRegistryNamespace.
- Support API ExecuteRegistryModule.
- Support API ExecuteTerraformApply.
- Support API ExecuteTerraformDestroy.
- Support API ExecuteTerraformPlan.
- Support API GetExecuteState.
- Support API GetRegistryModule.
- Support API GetRegistryModuleVersion.
- Support API GetRegistryNamespace.
- Support API GetResourceType.
- Support API ListExplorerRegistryModuleExamples.
- Support API ListExplorerRegistryModuleVersions.
- Support API ListExplorerRegistryModules.
- Support API ListProducts.
- Support API ListRegistryModuleVersions.
- Support API ListRegistryModules.
- Support API ListRegistryNamespaces.
- Support API ListResourceTypes.
- Support API PublishRegistryModuleVersion.
- Support API RemoveSharedAccounts.
- Support API UpdateExplorerModuleAttribute.
- Support API UpdateRegistryModuleAttribute.
- Support API UpdateRegistryNamespaceAttribute.
- Support API ValidateModule.
- Delete API AssociateParameterSet.
- Delete API AttachRabbitmqPublisher.
- Delete API CancelProjectBuild.
- Delete API CancelRamPolicyExportTask.
- Delete API CheckResourceName.
- Delete API CloneGroup.
- Delete API CloneModule.
- Delete API CreateAuthorization.
- Delete API CreateExplorerTask.
- Delete API CreateParameterSet.
- Delete API CreateProjectBuild.
- Delete API CreateRabbitmqPublisher.
- Delete API CreateRamPolicyExportTask.
- Delete API DeleteAuthorization.
- Delete API DeleteParameterSet.
- Delete API DeleteRabbitmqPublisher.
- Delete API DeleteRamPolicyExportTask.
- Delete API DeleteRamPolicyExportTaskVersion.
- Delete API DeleteSceneTestingTask.
- Delete API DetachRabbitmqPublisher.
- Delete API DissociateParameterSet.
- Delete API ExecuteRamPolicyExportTask.
- Delete API GetExplorerTask.
- Delete API GetParameterSet.
- Delete API GetProjectBuildContext.
- Delete API GetRabbitmqPublisher.
- Delete API GetRamPolicyExportTask.
- Delete API GetRamPolicyExportTaskVersion.
- Delete API GetTaskPolicy.
- Delete API ListAuthorizations.
- Delete API ListAvailableTerraformVersions.
- Delete API ListExplorerTasks.
- Delete API ListParameterSetRelation.
- Delete API ListParameterSets.
- Delete API ListProjectBuilds.
- Delete API ListRabbitmqPublishers.
- Delete API ListRamPolicyExportTaskVersions.
- Delete API ListRamPolicyExportTasks.
- Delete API ListResources.
- Delete API RemoveResourceExportTaskVersion.
- Delete API TagResources.
- Delete API UpdateAuthorizationAttribute.
- Delete API UpdateExplorerTaskAttribute.
- Delete API UpdateParameterSetAttribute.
- Delete API UpdateRabbitmqPublisherAttribute.
- Delete API UpdateRamPolicyExportTaskAttribute.
- Delete API UpdateTaskPolicy.
- Update API CancelResourceExportTask: delete request parameters body.ramRole.
- Update API CreateJob: delete request parameters body.executeType.
- Update API CreateModule: add request parameters body.tags.
- Update API CreateResourceExportTask: delete request parameters body.configPath.
- Update API CreateResourceExportTask: delete request parameters body.excludeRules.
- Update API CreateTask: add request parameters body.tags.
- Update API CreateTask: delete request parameters body.parameters.
- Update API CreateTask: delete request parameters body.triggerValue.
- Update API ExecuteResourceExportTask: delete request parameters body.ramRole.
- Update API GetJob: delete response parameters Body.job.runtimeType.
- Update API GetModule: add response parameters Body.module.groupInfo.
- Update API GetModule: add response parameters Body.module.tags.
- Update API GetResourceExportTask: delete response parameters Body.task.configPath.
- Update API GetResourceExportTask: delete response parameters Body.task.excludeRules.
- Update API GetTask: add response parameters Body.task.currentJobStatus.
- Update API GetTask: add response parameters Body.task.deletionProtection.
- Update API GetTask: add response parameters Body.task.latestModuleVersion.
- Update API GetTask: add response parameters Body.task.moduleName.
- Update API GetTask: add response parameters Body.task.tags.
- Update API GetTask: add response parameters Body.task.taskBackend.
- Update API GetTask: delete response parameters Body.task.parameters.
- Update API GetTask: delete response parameters Body.task.triggerValue.
- Update API ListJobs: add response parameters Body.jobs.$.config.moduleDescription.
- Update API ListModules: add request parameters tag.$.tagKey.
- Update API ListModules: add request parameters tag.$.tagValue.
- Update API ListModules: add response parameters Body.modules.$.tags.$.tagKey.
- Update API ListModules: add response parameters Body.modules.$.tags.$.tagValue.
- Update API ListModules: delete request parameters excludeModuleIds.
- Update API ListModules: delete request parameters tag.$.key.
- Update API ListModules: delete request parameters tag.$.value.
- Update API ListModules: delete response parameters Body.modules.$.meta.
- Update API ListModules: delete response parameters Body.modules.$.sourceConfig.
- Update API ListResourceExportTaskVersions: delete response parameters Body.exportTasks.$.excludeRules.
- Update API ListResourceExportTaskVersions: delete response parameters Body.exportTasks.$.hasDestroy.
- Update API ListResourceExportTasks: delete response parameters Body.exportTasks.$.excludeRules.
- Update API ListResourceExportTasks: delete response parameters Body.exportTasks.$.hasDestroy.
- Update API ListTasks: add request parameters tag.$.tagKey.
- Update API ListTasks: add request parameters tag.$.tagValue.
- Update API ListTasks: add response parameters Body.tasks.$.latestModuleVersion.
- Update API ListTasks: add response parameters Body.tasks.$.tags.$.tagKey.
- Update API ListTasks: add response parameters Body.tasks.$.tags.$.tagValue.
- Update API ListTasks: delete request parameters excludeTaskIds.
- Update API ListTasks: delete request parameters tag.$.key.
- Update API ListTasks: delete request parameters tag.$.value.
- Update API ListTerraformProviderVersions: delete response parameters Body.verisonList.
- Update API UpdateModuleAttribute: add request parameters body.clientToken.
- Update API UpdateModuleAttribute: add request parameters body.tags.
- Update API UpdateModuleAttribute: delete request parameters body.source.
- Update API UpdateResourceExportTaskAttribute: delete request parameters body.configPath.
- Update API UpdateResourceExportTaskAttribute: delete request parameters body.excludeRules.
- Update API UpdateTaskAttribute: add request parameters body.clientToken.
- Update API UpdateTaskAttribute: add request parameters body.tags.
- Update API UpdateTaskAttribute: delete request parameters body.moduleId.
- Update API UpdateTaskAttribute: delete request parameters body.parameters.
- Update API UpdateTaskAttribute: delete request parameters body.triggerValue.


2025-04-23 Version: 1.1.0
- Support API CancelProjectBuild.
- Support API CreateExplorerTask.
- Support API GetExplorerTask.
- Support API ListExplorerTasks.
- Support API TagResources.
- Support API UpdateExplorerTaskAttribute.
- Update API CreateJob: add request parameters body.executeType.
- Update API CreateJob: add request parameters body.taskType.
- Update API CreateResourceExportTask: add request parameters body.configPath.
- Update API CreateTask: add request parameters body.initModuleState.
- Update API CreateTask: add request parameters body.skipPropertyValidation.
- Update API CreateTask: add request parameters body.taskBackend.
- Update API GetJob: add request parameters taskType.
- Update API GetJob: add response parameters Body.job.downloadUrl.
- Update API GetJob: add response parameters Body.job.executeType.
- Update API GetJob: add response parameters Body.job.taskType.
- Update API GetJob: add response parameters Body.job.terraformProviderVersion.
- Update API GetJob: add response parameters Body.job.config.subCommand.
- Update API GetProjectBuildContext: add request parameters isPassAssertCheck.
- Update API GetProjectBuildContext: add request parameters status.
- Update API GetResourceExportTask: add response parameters Body.task.configPath.
- Update API GetTask: add response parameters Body.task.initModuleState.
- Update API GetTask: add response parameters Body.task.skipPropertyValidation.
- Update API ListGroup: add request parameters keyword.
- Update API ListGroup: add request parameters tag.
- Update API ListGroup: add response parameters Body.groups.$.tags.
- Update API ListJobs: add request parameters taskType.
- Update API ListJobs: add response parameters Body.jobs.$.executeType.
- Update API ListJobs: add response parameters Body.jobs.$.config.isDestroy.
- Update API ListJobs: add response parameters Body.jobs.$.config.subCommand.
- Update API ListModules: add request parameters excludeModuleIds.
- Update API ListModules: add request parameters tag.
- Update API ListModules: add response parameters Body.modules.$.tags.
- Update API ListParameterSets: add response parameters Body.parameterSets.$.deletionProtection.
- Update API ListProject: add request parameters keyword.
- Update API ListProject: add request parameters tag.
- Update API ListProject: add response parameters Body.projects.$.tags.
- Update API ListTasks: add request parameters excludeTaskIds.
- Update API ListTasks: add request parameters status.
- Update API ListTasks: add request parameters tag.
- Update API ListTasks: add response parameters Body.tasks.$.deletionProtection.
- Update API ListTasks: add response parameters Body.tasks.$.tags.
- Update API ListTerraformProviderVersions: add request parameters keyword.
- Update API ListTerraformProviderVersions: add request parameters maxResults.
- Update API ListTerraformProviderVersions: add request parameters nextToken.
- Update API ListTerraformProviderVersions: add request parameters usage.
- Update API ListTerraformProviderVersions: add response parameters Body.maxResults.
- Update API ListTerraformProviderVersions: add response parameters Body.nextToken.
- Update API ListTerraformProviderVersions: add response parameters Body.versions.
- Update API OperateJob: add request parameters taskType.
- Update API UpdateResourceExportTaskAttribute: add request parameters body.configPath.
- Update API UpdateTaskAttribute: add request parameters body.initModuleState.
- Update API UpdateTaskAttribute: add request parameters body.skipPropertyValidation.


2023-02-16 Version: 1.0.1
- Sdk.
- Ram Policy  Export.

2022-09-09 Version: 1.0.0
- Generated python 2021-08-06 for IaCService.

