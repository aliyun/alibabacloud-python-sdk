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

