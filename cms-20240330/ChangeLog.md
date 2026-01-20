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

