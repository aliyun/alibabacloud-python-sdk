2026-04-14 Version: 7.0.1
- Update API CreatePrometheusVirtualInstance: add request parameters body.tenantId.
- Update API ListPrometheusVirtualInstances: add request parameters tenantId.


2026-04-10 Version: 7.0.0
- Update API GetMemories: add request parameters body.filters.
- Update API SearchMemories: add request parameters body.filters.
- Update API SearchMemories: add request parameters body.retrieveLevel.
- Update API SearchMemories: add request parameters body.threshold.
- Update API SearchMemories: delete request parameters body.metadata.
- Update API SearchMemories: update response parameters Body.results.$.metadata' type has changed.


2026-04-02 Version: 6.4.0
- Support API CreateDataset.
- Support API DeleteDataset.
- Support API DeletePrometheusVirtualInstance.
- Support API ExecuteQuery.
- Support API GetDataset.
- Support API ListDatasets.
- Support API UpdateDataset.


2026-03-27 Version: 6.3.0
- Support API CreateDeliveryTask.
- Support API DeleteDeliveryTask.
- Support API GetDeliveryTask.
- Support API ListDeliveryTasks.
- Support API UpdateDeliveryTask.
- Update API CreateMemoryStore: add request parameters body.sourceType.
- Update API CreateMemoryStore: add request parameters body.traceSourceConfig.
- Update API GetMemoryStore: add response parameters Body.sourceType.
- Update API GetMemoryStore: add response parameters Body.traceSourceConfig.


2026-03-24 Version: 6.2.4
- Update API CreateAlertWebhook: add request parameters body.workspace.
- Update API ListAlertWebhooks: add request parameters workspace.
- Update API ListAlertWebhooks: add response parameters Body.webhooks.$.workspace.


2026-03-20 Version: 6.2.3
- Update API AddMemories: add request parameters body.timestamp.
- Update API GetMemories: add response parameters Body.results.$.appId.
- Update API GetMemory: add response parameters Body.agentId.
- Update API GetMemory: add response parameters Body.appId.
- Update API GetMemory: add response parameters Body.runId.
- Update API GetMemory: add response parameters Body.userId.


2026-03-19 Version: 6.2.2
- Update API GetMemoryStore: add response parameters Body.shortTermStorage.
- Update API ListMemoryStores: add response parameters Body.total.


2026-03-17 Version: 6.2.1
- Update API CreateThread: add request parameters body.attributes.
- Update API GetThread: add response parameters Body.attributes.
- Update API ListThreads: add response parameters Body.threads.$.attributes.
- Update API UpdateThread: add request parameters body.attributes.


2026-03-10 Version: 6.2.0
- Support API AddMemories.
- Support API CreateMemoryStore.
- Support API DeleteMemories.
- Support API DeleteMemory.
- Support API DeleteMemoryStore.
- Support API GetMemories.
- Support API GetMemory.
- Support API GetMemoryHistory.
- Support API GetMemoryStore.
- Support API ListMemoryStores.
- Support API SearchMemories.
- Support API UpdateMemory.
- Support API UpdateMemoryStore.


2026-02-24 Version: 6.1.0
- Support API CreateDigitalEmployeeSkill.
- Support API DeleteDigitalEmployeeSkill.
- Support API GetDigitalEmployeeSkill.
- Support API ListDigitalEmployeeSkillVersions.
- Support API ListDigitalEmployeeSkills.
- Support API UpdateDigitalEmployeeSkill.


2026-02-02 Version: 6.0.1
- Update API CreateDigitalEmployee: add request parameters body.resourceGroupId.
- Update API CreateDigitalEmployee: add request parameters body.tags.
- Update API GetDigitalEmployee: add response parameters Body.resourceGroupId.
- Update API GetDigitalEmployee: add response parameters Body.tags.
- Update API ListDigitalEmployees: add request parameters resourceGroupId.
- Update API ListDigitalEmployees: add request parameters tags.
- Update API ListDigitalEmployees: add response parameters Body.digitalEmployees.$.resourceGroupId.
- Update API ListDigitalEmployees: add response parameters Body.digitalEmployees.$.tags.


2026-01-23 Version: 6.0.0
- Update API ListAggTaskGroups: delete response parameters Body.aggTaskGroups.$.tags.
- Update API ListIntegrationPolicies: delete response parameters Body.policies.$.tags.
- Update API ListPrometheusInstances: add request parameters workspace.
- Update API ListPrometheusInstances: delete response parameters Body.prometheusInstances.$.resourceGroupId.
- Update API ListPrometheusInstances: delete response parameters Body.prometheusInstances.$.tags.
- Update API ListPrometheusViews: delete response parameters Body.prometheusViews.$.resourceGroupId.
- Update API ListPrometheusViews: delete response parameters Body.prometheusViews.$.tags.


2026-01-20 Version: 5.0.0
- Update API CreateChat: add response parameters Body.messages.$.artifacts.
- Update API CreateChat: add response parameters Body.messages.$.events.
- Update API CreateChat: add response parameters Body.messages.$.version.
- Update API CreateChat: update response parameters Body.messages.$.timestamp' type has changed.
- Update API CreateChat: update response parameters Body.messages.$.timestamp' format has changed.
- Update API CreateDigitalEmployee: add request parameters body.knowledges.sop.
- Update API GetDigitalEmployee: add response parameters Body.knowledges.sop.
- Update API GetThreadData: add response parameters Body.data.
- Update API GetThreadData: delete response parameters Body.messages.
- Update API ListDigitalEmployees: add request parameters displayName.
- Update API ListDigitalEmployees: add response parameters Body.digitalEmployees.$.knowledges.sop.
- Update API UpdateDigitalEmployee: add request parameters body.knowledges.sop.


2026-01-06 Version: 4.2.0
- Support API CreateServiceObservability.
- Update API CreateIntegrationPolicy: add request parameters body.entityGroup.clusterNamespace.
- Update API GetDigitalEmployee: add response parameters Body.employeeType.
- Update API ListDigitalEmployees: add request parameters employeeType.
- Update API ListDigitalEmployees: add response parameters Body.digitalEmployees.$.employeeType.


2025-12-30 Version: 4.1.0
- Support API ChangeResourceGroup.
- Support API ListTagResources.
- Support API TagResources.
- Support API UntagResources.


2025-12-29 Version: 4.0.0
- Update API DeleteThread: delete response parameters Body.deleted.


2025-12-26 Version: 3.6.1
- Update API CreateService: add request parameters body.resourceGroupId.
- Update API CreateService: add request parameters body.tags.
- Update API GetService: add response parameters Body.service.resourceGroupId.
- Update API GetService: add response parameters Body.service.tags.
- Update API ListServices: add request parameters resourceGroupId.
- Update API ListServices: add request parameters serviceName.
- Update API ListServices: add request parameters tags.
- Update API ListServices: add response parameters Body.services.$.resourceGroupId.


2025-12-25 Version: 3.6.0
- Support API CreateChat.
- Support API CreateDigitalEmployee.
- Support API CreateThread.
- Support API DeleteDigitalEmployee.
- Support API DeleteThread.
- Support API GetDigitalEmployee.
- Support API GetThread.
- Support API GetThreadData.
- Support API ListDigitalEmployees.
- Support API ListThreads.
- Support API UpdateDigitalEmployee.
- Support API UpdateThread.


2025-11-27 Version: 3.5.0
- Support API CreateBizTrace.
- Support API DeleteBizTrace.
- Support API GetAddon.
- Support API GetAddonCodeTemplate.
- Support API GetAddonSchema.
- Support API GetBizTrace.
- Support API GetIntegrationVersionForCS.
- Support API ListAddons.
- Support API ListBizTraces.
- Support API ListIntegrationPolicyAddons.
- Support API ListIntegrationPolicyCollectors.
- Support API UpdateBizTrace.


2025-11-26 Version: 3.4.0
- Support API CreateCloudResource.
- Support API DeleteCloudResource.
- Support API DescribeRegions.
- Support API GetCloudResource.
- Support API GetCloudResourceData.
- Support API GetCmsService.
- Support API GetPrometheusUserSetting.
- Support API ListIntegrationPolicyServiceMonitors.
- Support API UpdatePrometheusUserSetting.


2025-11-10 Version: 3.3.0
- Support API DeleteUmodelCommonSchemaRef.
- Support API GetUmodelCommonSchemaRef.
- Support API UpdateNotifyStrategy.
- Support API UpdateSubscription.
- Support API UpsertUmodelCommonSchemaRef.


2025-10-30 Version: 3.2.5
- Update API CreateIntegrationPolicy: add request parameters body.entityGroup.entityUserId.
- Update API GetIntegrationPolicy: add response parameters Body.policy.csUmodelStatus.
- Update API ListIntegrationPolicies: add response parameters Body.policies.$.csUmodelStatus.
- Update API ListIntegrationPolicies: add response parameters Body.policies.$.feePackage.


2025-10-20 Version: 3.2.4
- Update API ListIntegrationPolicyDashboards: add request parameters language.
- Update API ListIntegrationPolicyDashboards: add response parameters Body.dashboards.$.engine.


2025-10-15 Version: 3.2.3
- Update API ListIntegrationPolicies: add request parameters bindResourceId.
- Update API ListIntegrationPolicyDashboards: add response parameters Body.dashboards.$.name.


2025-10-14 Version: 3.2.2
- Update API ListIntegrationPolicies: add response parameters Body.policies.$.managedInfo.eniId.


2025-10-13 Version: 3.2.1
- Update API CreateIntegrationPolicy: add request parameters body.entityGroup.disablePolicyShare.


2025-09-28 Version: 3.2.0
- Support API ListIntegrationPolicies.
- Support API ListIntegrationPolicyDashboards.


2025-09-24 Version: 3.1.1
- Generated python 2024-03-30 for Cms.

2025-09-10 Version: 3.1.0
- Support API CreateAddonRelease.
- Support API CreateAggTaskGroup.
- Support API CreateIntegrationPolicy.
- Support API CreatePrometheusView.
- Support API CreatePrometheusVirtualInstance.
- Support API DeleteAddonRelease.
- Support API DeleteAggTaskGroup.
- Support API DeleteIntegrationPolicy.
- Support API DeletePrometheusInstance.
- Support API DeletePrometheusView.
- Support API GetAddonRelease.
- Support API GetAggTaskGroup.
- Support API GetIntegrationPolicy.
- Support API GetPrometheusInstance.
- Support API GetPrometheusView.
- Support API ListAddonReleases.
- Support API ListAggTaskGroups.
- Support API ListIntegrationPolicyCustomScrapeJobRules.
- Support API ListIntegrationPolicyPodMonitors.
- Support API ListIntegrationPolicyStorageRequirements.
- Support API ListPrometheusDashboards.
- Support API ListPrometheusInstances.
- Support API ListPrometheusViews.
- Support API ListPrometheusVirtualInstances.
- Support API UpdateAddonRelease.
- Support API UpdateAggTaskGroup.
- Support API UpdateAggTaskGroupStatus.
- Support API UpdateIntegrationPolicy.
- Support API UpdatePrometheusInstance.
- Support API UpdatePrometheusView.
- Update API GetEntityStoreData: add response parameters Body.responseStatus.


2025-08-12 Version: 3.0.0
- Update API CreateUmodel: delete request parameters body.commonSchemaRef.
- Update API GetUmodel: delete response parameters Body.commonSchemaRef.$.items.
- Update API UpdateUmodel: delete request parameters body.commonSchemaRef.


2025-07-25 Version: 2.3.0
- Support API CreateTicket.


2025-07-24 Version: 2.2.0
- Support API CreateService.
- Support API DeleteService.
- Support API GetService.
- Support API ListServices.
- Support API UpdateService.


2025-07-23 Version: 2.1.0
- Support API GetServiceObservability.
- Update API ListAlertActions: add response parameters Body.alertActions.$.ebParam.
- Update API ListAlertActions: add response parameters Body.alertActions.$.fc3Param.


2025-05-13 Version: 2.0.0
- Support API CreateEntityStore.
- Support API CreatePrometheusInstance.
- Support API CreateUmodel.
- Support API DeleteEntityStore.
- Support API DeleteUmodel.
- Support API DeleteUmodelData.
- Support API DeleteWorkspace.
- Support API GetEntityStore.
- Support API GetEntityStoreData.
- Support API GetUmodel.
- Support API GetUmodelData.
- Support API GetWorkspace.
- Support API ListWorkspaces.
- Support API PutWorkspace.
- Support API UpdateUmodel.
- Support API UpsertUmodelData.
- Update API ListAlertActions: add request parameters RegionId.
- Update API ListAlertActions: delete request parameters regionId.


2024-11-04 Version: 1.0.0
- Generated python 2024-03-30 for Cms.

