2025-05-21 Version: 2.25.0
- Support API DescribeSiteLogs.
- Support API OpenErService.
- Update API CreateRoutineRelatedRecord: add response parameters Body.RecordId.
- Update API GetManagedTransform: add response parameters Body.RealClientIpHeaderName.
- Update API UpdateManagedTransform: add request parameters RealClientIpHeaderName.


2025-05-08 Version: 2.24.0
- Support API ListRoutineCodeVersions.


2025-04-17 Version: 2.23.1
- Update API CreateOriginRule: add request parameters Follow302Enable.
- Update API CreateOriginRule: add request parameters Follow302MaxTries.
- Update API CreateOriginRule: add request parameters Follow302RetainArgs.
- Update API CreateOriginRule: add request parameters Follow302RetainHeader.
- Update API CreateOriginRule: add request parameters Follow302TargetHost.
- Update API GetOriginRule: add response parameters Body.Follow302Enable.
- Update API GetOriginRule: add response parameters Body.Follow302MaxTries.
- Update API GetOriginRule: add response parameters Body.Follow302RetainArgs.
- Update API GetOriginRule: add response parameters Body.Follow302RetainHeader.
- Update API GetOriginRule: add response parameters Body.Follow302TargetHost.
- Update API GetWafRule: add response parameters Body.RulesetId.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302Enable.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302MaxTries.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302RetainArgs.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302RetainHeader.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302TargetHost.
- Update API UpdateOriginRule: add request parameters Follow302Enable.
- Update API UpdateOriginRule: add request parameters Follow302MaxTries.
- Update API UpdateOriginRule: add request parameters Follow302RetainArgs.
- Update API UpdateOriginRule: add request parameters Follow302RetainHeader.
- Update API UpdateOriginRule: add request parameters Follow302TargetHost.


2025-04-17 Version: 2.23.1
- Update API CreateOriginRule: add request parameters Follow302Enable.
- Update API CreateOriginRule: add request parameters Follow302MaxTries.
- Update API CreateOriginRule: add request parameters Follow302RetainArgs.
- Update API CreateOriginRule: add request parameters Follow302RetainHeader.
- Update API CreateOriginRule: add request parameters Follow302TargetHost.
- Update API GetOriginRule: add response parameters Body.Follow302Enable.
- Update API GetOriginRule: add response parameters Body.Follow302MaxTries.
- Update API GetOriginRule: add response parameters Body.Follow302RetainArgs.
- Update API GetOriginRule: add response parameters Body.Follow302RetainHeader.
- Update API GetOriginRule: add response parameters Body.Follow302TargetHost.
- Update API GetWafRule: add response parameters Body.RulesetId.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302Enable.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302MaxTries.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302RetainArgs.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302RetainHeader.
- Update API ListOriginRules: add response parameters Body.Configs.$.Follow302TargetHost.
- Update API UpdateOriginRule: add request parameters Follow302Enable.
- Update API UpdateOriginRule: add request parameters Follow302MaxTries.
- Update API UpdateOriginRule: add request parameters Follow302RetainArgs.
- Update API UpdateOriginRule: add request parameters Follow302RetainHeader.
- Update API UpdateOriginRule: add request parameters Follow302TargetHost.


2025-04-15 Version: 2.23.0
- Support API GetErService.
- Support API ListCertificatesByRecord.
- Support API ListRoutineRelatedRecords.
- Support API ListUserRoutines.
- Update API CreateHttpRequestHeaderModificationRule: add request parameters RequestHeaderModification.$.Type.
- Update API CreateHttpResponseHeaderModificationRule: add request parameters ResponseHeaderModification.$.Type.
- Update API GetHttpRequestHeaderModificationRule: add response parameters Body.RequestHeaderModification.$.Type.
- Update API GetHttpResponseHeaderModificationRule: add response parameters Body.ResponseHeaderModification.$.Type.
- Update API ListHttpRequestHeaderModificationRules: add response parameters Body.Configs.$.RequestHeaderModification.$.Type.
- Update API ListHttpResponseHeaderModificationRules: add response parameters Body.Configs.$.ResponseHeaderModification.$.Type.
- Update API ListWafTemplateRules: add request parameters QueryArgs.Kinds.
- Update API RollbackEdgeContainerAppVersion: add request parameters Percentage.
- Update API RollbackEdgeContainerAppVersion: add request parameters UsedPercent.
- Update API UpdateHttpRequestHeaderModificationRule: add request parameters RequestHeaderModification.$.Type.
- Update API UpdateHttpResponseHeaderModificationRule: add request parameters ResponseHeaderModification.$.Type.


2025-04-07 Version: 2.22.0
- Support API CreateRoutineRoute.
- Support API DeleteRoutineRoute.
- Support API GetRoutineRoute.
- Support API ListRoutineRoutes.
- Support API ListSiteRoutes.
- Support API UpdateRoutineRoute.


2025-04-02 Version: 2.21.0
- Support API DescribeSiteTimeSeriesData.
- Support API DescribeSiteTopData.


2025-04-01 Version: 2.20.0
- Support API GetEdgeContainerAppResourceStatus.
- Update API CreateOriginRule: add request parameters OriginReadTimeout.
- Update API GetOriginRule: add response parameters Body.OriginReadTimeout.
- Update API ListOriginRules: add response parameters Body.Configs.$.OriginReadTimeout.
- Update API UpdateOriginRule: add request parameters OriginReadTimeout.


2025-03-31 Version: 2.19.0
- Support API GetCrossBorderOptimization.
- Support API UpdateCrossBorderOptimization.


2025-03-31 Version: 2.19.0
- Support API GetCrossBorderOptimization.
- Support API UpdateCrossBorderOptimization.


2025-03-27 Version: 2.18.0
- Support API BatchCreateWafRules.
- Support API BatchUpdateWafRules.
- Support API CreateWafRule.
- Support API CreateWafRuleset.
- Support API DeleteOriginCaCertificate.
- Support API DeleteOriginClientCertificate.
- Support API DeleteSiteOriginClientCertificate.
- Support API DeleteWafRule.
- Support API DeleteWafRuleset.
- Support API GetOriginCaCertificate.
- Support API GetOriginClientCertificate.
- Support API GetOriginClientCertificateHostnames.
- Support API GetSiteOriginClientCertificate.
- Support API GetWafRule.
- Support API GetWafRuleset.
- Support API ListOriginCaCertificates.
- Support API ListOriginClientCertificates.
- Support API ListWafRules.
- Support API ListWafRulesets.
- Support API SetOriginClientCertificateHostnames.
- Support API UpdateWafRule.
- Support API UpdateWafRuleset.
- Support API UploadOriginCaCertificate.
- Support API UploadOriginClientCertificate.
- Support API UploadSiteOriginClientCertificate.
- Update API CreateCacheRule: add request parameters Sequence.
- Update API CreateCompressionRule: add request parameters Sequence.
- Update API CreateHttpRequestHeaderModificationRule: add request parameters Sequence.
- Update API CreateHttpResponseHeaderModificationRule: add request parameters Sequence.
- Update API CreateHttpsApplicationConfiguration: add request parameters Sequence.
- Update API CreateHttpsBasicConfiguration: add request parameters Sequence.
- Update API CreateImageTransform: add request parameters Sequence.
- Update API CreateNetworkOptimization: add request parameters Sequence.
- Update API CreateOriginRule: add request parameters Sequence.
- Update API CreateRedirectRule: add request parameters Sequence.
- Update API CreateRewriteUrlRule: add request parameters Sequence.
- Update API GetIPv6: add response parameters Body.Region.
- Update API UpdateCacheRule: add request parameters Sequence.
- Update API UpdateCompressionRule: add request parameters Sequence.
- Update API UpdateHttpRequestHeaderModificationRule: add request parameters Sequence.
- Update API UpdateHttpResponseHeaderModificationRule: add request parameters Sequence.
- Update API UpdateHttpsApplicationConfiguration: add request parameters Sequence.
- Update API UpdateHttpsBasicConfiguration: add request parameters Sequence.
- Update API UpdateIPv6: add request parameters Region.
- Update API UpdateImageTransform: add request parameters Sequence.
- Update API UpdateNetworkOptimization: add request parameters Sequence.
- Update API UpdateOriginRule: add request parameters Sequence.
- Update API UpdateRedirectRule: add request parameters Sequence.
- Update API UpdateRewriteUrlRule: add request parameters Sequence.


2025-03-20 Version: 2.17.1
- Update API CreateOriginRule: add param RangeChunkSize.
- Update API GetOriginRule: update response param.
- Update API ListOriginRules: update response param.
- Update API UpdateOriginRule: add param RangeChunkSize.


2025-03-20 Version: 2.17.0
- Support API GetEdgeContainerAppResourceReserve.
- Support API PurchaseCacheReserve.
- Support API UpdateCacheReserveSpec.
- Support API UpdateEdgeContainerAppResourceReserve.
- Update API CreateRoutine: update param SpecName.
- Update API GetRoutine: update response param.
- Update API ListScheduledPreloadJobs: update response param.
- Update API SetClientCertificateHostnames: update response param.


2025-03-12 Version: 2.16.0
- Support API ActivateVersionManagement.
- Support API CheckAssumeSlrRole.
- Support API CreateHttpsApplicationConfiguration.
- Support API CreateImageTransform.
- Support API CreateLoadBalancer.
- Support API CreateNetworkOptimization.
- Support API CreateSlrRoleForRealtimeLog.
- Support API DeactivateVersionManagement.
- Support API DeleteHttpsApplicationConfiguration.
- Support API DeleteImageTransform.
- Support API DeleteLoadBalancer.
- Support API DeleteNetworkOptimization.
- Support API DescribeEdgeContainerAppStats.
- Support API DescribeRatePlanInstanceStatus.
- Support API GetCacheTag.
- Support API GetCnameFlattening.
- Support API GetDevelopmentMode.
- Support API GetEdgeContainerAppLogRiver.
- Support API GetHttpsApplicationConfiguration.
- Support API GetImageTransform.
- Support API GetLoadBalancer.
- Support API GetNetworkOptimization.
- Support API GetSeoBypass.
- Support API GetSiteNameExclusive.
- Support API GetSitePause.
- Support API ListHttpsApplicationConfigurations.
- Support API ListImageTransforms.
- Support API ListLoadBalancerOriginStatus.
- Support API ListLoadBalancers.
- Support API ListNetworkOptimizations.
- Support API PurchaseRatePlan.
- Support API UpdateCacheTag.
- Support API UpdateCnameFlattening.
- Support API UpdateDevelopmentMode.
- Support API UpdateEdgeContainerAppLogRiver.
- Support API UpdateHttpsApplicationConfiguration.
- Support API UpdateImageTransform.
- Support API UpdateLoadBalancer.
- Support API UpdateNetworkOptimization.
- Support API UpdateRatePlanSpec.
- Support API UpdateSeoBypass.
- Support API UpdateSiteNameExclusive.
- Support API UpdateSitePause.
- Update API CreateCompressionRule: add param Zstd.
- Update API CreateOriginRule: add param OriginMtls.
- Update API CreateOriginRule: add param OriginVerify.
- Update API CreateSiteDeliveryTask: update response param.
- Update API CreateWaitingRoom: update response param.
- Update API CreateWaitingRoomEvent: update response param.
- Update API CreateWaitingRoomRule: update response param.
- Update API DeleteWaitingRoomEvent: update param WaitingRoomEventId.
- Update API DeleteWaitingRoomRule: update param WaitingRoomRuleId.
- Update API DescribeCustomScenePolicies: update param PageNumber.
- Update API DescribePurgeTasks: update param Type.
- Update API GetClientCaCertificate: update response param.
- Update API GetClientCertificate: update response param.
- Update API GetCompressionRule: update response param.
- Update API GetOriginRule: update response param.
- Update API GetPurgeQuota: update param Type.
- Update API GetSite: update response param.
- Update API GetWafFilter: update response param.
- Update API ListCacheReserveInstances: update response param.
- Update API ListClientCaCertificates: update response param.
- Update API ListClientCertificates: update response param.
- Update API ListCompressionRules: update response param.
- Update API ListOriginRules: update response param.
- Update API ListSites: update response param.
- Update API ListUserRatePlanInstances: add param SubscribeType.
- Update API ListUserRatePlanInstances: update response param.
- Update API PurgeCaches: update param Content.
- Update API UpdateCompressionRule: add param Zstd.
- Update API UpdateCustomScenePolicy: update param Objects.
- Update API UpdateOriginRule: add param OriginMtls.
- Update API UpdateOriginRule: add param OriginVerify.
- Update API UpdateScheduledPreloadExecution: update param EndTime.
- Update API UpdateWaitingRoomEvent: update param WaitingRoomEventId.
- Update API UpdateWaitingRoomRule: update param WaitingRoomRuleId.
- Update API UploadClientCaCertificate: update param Name.


2025-02-12 Version: 2.15.0
- Support API ActivateVersionManagement.
- Support API CheckAssumeSlrRole.
- Support API CreateHttpsApplicationConfiguration.
- Support API CreateImageTransform.
- Support API CreateLoadBalancer.
- Support API CreateNetworkOptimization.
- Support API CreateSlrRoleForRealtimeLog.
- Support API DeactivateVersionManagement.
- Support API DeleteHttpsApplicationConfiguration.
- Support API DeleteImageTransform.
- Support API DeleteLoadBalancer.
- Support API DeleteNetworkOptimization.
- Support API GetCacheTag.
- Support API GetCnameFlattening.
- Support API GetDevelopmentMode.
- Support API GetHttpsApplicationConfiguration.
- Support API GetImageTransform.
- Support API GetLoadBalancer.
- Support API GetNetworkOptimization.
- Support API GetSeoBypass.
- Support API GetSiteNameExclusive.
- Support API GetSitePause.
- Support API ListHttpsApplicationConfigurations.
- Support API ListImageTransforms.
- Support API ListLoadBalancerOriginStatus.
- Support API ListLoadBalancers.
- Support API ListNetworkOptimizations.
- Support API UpdateCacheTag.
- Support API UpdateCnameFlattening.
- Support API UpdateDevelopmentMode.
- Support API UpdateHttpsApplicationConfiguration.
- Support API UpdateImageTransform.
- Support API UpdateLoadBalancer.
- Support API UpdateNetworkOptimization.
- Support API UpdateSeoBypass.
- Support API UpdateSiteNameExclusive.
- Support API UpdateSitePause.
- Update API CreateCompressionRule: add param Zstd.
- Update API CreateWaitingRoom: update response param.
- Update API CreateWaitingRoomEvent: update response param.
- Update API CreateWaitingRoomRule: update response param.
- Update API DescribePurgeTasks: update param Type.
- Update API GetCompressionRule: update response param.
- Update API GetPurgeQuota: update param Type.
- Update API ListCompressionRules: update response param.
- Update API ListUserRatePlanInstances: add param SubscribeType.
- Update API ListUserRatePlanInstances: update response param.
- Update API PurgeCaches: update param Content.
- Update API UpdateCompressionRule: add param Zstd.


2025-02-10 Version: 2.14.0
- Support API ActivateVersionManagement.
- Support API CreateHttpsApplicationConfiguration.
- Support API CreateImageTransform.
- Support API CreateLoadBalancer.
- Support API CreateNetworkOptimization.
- Support API DeactivateVersionManagement.
- Support API DeleteHttpsApplicationConfiguration.
- Support API DeleteImageTransform.
- Support API DeleteLoadBalancer.
- Support API DeleteNetworkOptimization.
- Support API GetCacheTag.
- Support API GetCnameFlattening.
- Support API GetDevelopmentMode.
- Support API GetHttpsApplicationConfiguration.
- Support API GetImageTransform.
- Support API GetLoadBalancer.
- Support API GetNetworkOptimization.
- Support API GetSeoBypass.
- Support API GetSiteNameExclusive.
- Support API GetSitePause.
- Support API ListHttpsApplicationConfigurations.
- Support API ListImageTransforms.
- Support API ListLoadBalancerOriginStatus.
- Support API ListLoadBalancers.
- Support API ListNetworkOptimizations.
- Support API UpdateCacheTag.
- Support API UpdateCnameFlattening.
- Support API UpdateDevelopmentMode.
- Support API UpdateHttpsApplicationConfiguration.
- Support API UpdateImageTransform.
- Support API UpdateLoadBalancer.
- Support API UpdateNetworkOptimization.
- Support API UpdateSeoBypass.
- Support API UpdateSiteNameExclusive.
- Support API UpdateSitePause.
- Update API DescribePurgeTasks: update param Type.
- Update API GetPurgeQuota: update param Type.
- Update API PurgeCaches: update param Content.


2025-02-08 Version: 2.13.0
- Support API ActivateVersionManagement.
- Support API CreateHttpsApplicationConfiguration.
- Support API CreateImageTransform.
- Support API CreateLoadBalancer.
- Support API CreateNetworkOptimization.
- Support API DeactivateVersionManagement.
- Support API DeleteHttpsApplicationConfiguration.
- Support API DeleteImageTransform.
- Support API DeleteLoadBalancer.
- Support API DeleteNetworkOptimization.
- Support API GetCacheTag.
- Support API GetCnameFlattening.
- Support API GetDevelopmentMode.
- Support API GetHttpsApplicationConfiguration.
- Support API GetImageTransform.
- Support API GetLoadBalancer.
- Support API GetNetworkOptimization.
- Support API GetSeoBypass.
- Support API GetSiteNameExclusive.
- Support API GetSitePause.
- Support API ListHttpsApplicationConfigurations.
- Support API ListImageTransforms.
- Support API ListLoadBalancerOriginStatus.
- Support API ListLoadBalancers.
- Support API ListNetworkOptimizations.
- Support API UpdateCacheTag.
- Support API UpdateCnameFlattening.
- Support API UpdateDevelopmentMode.
- Support API UpdateHttpsApplicationConfiguration.
- Support API UpdateImageTransform.
- Support API UpdateLoadBalancer.
- Support API UpdateNetworkOptimization.
- Support API UpdateSeoBypass.
- Support API UpdateSiteNameExclusive.
- Support API UpdateSitePause.


2025-02-08 Version: 2.13.0
- Support API ActivateVersionManagement.
- Support API CreateHttpsApplicationConfiguration.
- Support API CreateImageTransform.
- Support API CreateLoadBalancer.
- Support API CreateNetworkOptimization.
- Support API DeactivateVersionManagement.
- Support API DeleteHttpsApplicationConfiguration.
- Support API DeleteImageTransform.
- Support API DeleteLoadBalancer.
- Support API DeleteNetworkOptimization.
- Support API GetCacheTag.
- Support API GetCnameFlattening.
- Support API GetDevelopmentMode.
- Support API GetHttpsApplicationConfiguration.
- Support API GetImageTransform.
- Support API GetLoadBalancer.
- Support API GetNetworkOptimization.
- Support API GetSeoBypass.
- Support API GetSiteNameExclusive.
- Support API GetSitePause.
- Support API ListHttpsApplicationConfigurations.
- Support API ListImageTransforms.
- Support API ListLoadBalancerOriginStatus.
- Support API ListLoadBalancers.
- Support API ListNetworkOptimizations.
- Support API UpdateCacheTag.
- Support API UpdateCnameFlattening.
- Support API UpdateDevelopmentMode.
- Support API UpdateHttpsApplicationConfiguration.
- Support API UpdateImageTransform.
- Support API UpdateLoadBalancer.
- Support API UpdateNetworkOptimization.
- Support API UpdateSeoBypass.
- Support API UpdateSiteNameExclusive.
- Support API UpdateSitePause.


2025-02-07 Version: 2.12.0
- Support API ActivateVersionManagement.
- Support API CreateHttpsApplicationConfiguration.
- Support API CreateLoadBalancer.
- Support API DeactivateVersionManagement.
- Support API DeleteHttpsApplicationConfiguration.
- Support API DeleteLoadBalancer.
- Support API GetCacheTag.
- Support API GetCnameFlattening.
- Support API GetDevelopmentMode.
- Support API GetHttpsApplicationConfiguration.
- Support API GetLoadBalancer.
- Support API GetSeoBypass.
- Support API GetSiteNameExclusive.
- Support API ListHttpsApplicationConfigurations.
- Support API ListLoadBalancerOriginStatus.
- Support API ListLoadBalancers.
- Support API UpdateCacheTag.
- Support API UpdateCnameFlattening.
- Support API UpdateDevelopmentMode.
- Support API UpdateHttpsApplicationConfiguration.
- Support API UpdateLoadBalancer.
- Support API UpdateSeoBypass.
- Support API UpdateSiteNameExclusive.


2025-01-14 Version: 2.11.0
- Support API CreateCacheRule.
- Support API CreateCompressionRule.
- Support API CreateHttpRequestHeaderModificationRule.
- Support API CreateHttpResponseHeaderModificationRule.
- Support API CreateHttpsBasicConfiguration.
- Support API CreateOriginRule.
- Support API CreateRedirectRule.
- Support API CreateRewriteUrlRule.
- Support API DeleteCacheRule.
- Support API DeleteCompressionRule.
- Support API DeleteHttpRequestHeaderModificationRule.
- Support API DeleteHttpResponseHeaderModificationRule.
- Support API DeleteHttpsBasicConfiguration.
- Support API DeleteOriginRule.
- Support API DeleteRedirectRule.
- Support API DeleteRewriteUrlRule.
- Support API GetCacheRule.
- Support API GetCompressionRule.
- Support API GetHttpRequestHeaderModificationRule.
- Support API GetHttpResponseHeaderModificationRule.
- Support API GetHttpsBasicConfiguration.
- Support API GetIPv6.
- Support API GetManagedTransform.
- Support API GetOriginRule.
- Support API GetRedirectRule.
- Support API GetRewriteUrlRule.
- Support API GetTieredCache.
- Support API ListCacheRules.
- Support API ListCompressionRules.
- Support API ListHttpRequestHeaderModificationRules.
- Support API ListHttpResponseHeaderModificationRules.
- Support API ListHttpsBasicConfigurations.
- Support API ListOriginRules.
- Support API ListRedirectRules.
- Support API ListRewriteUrlRules.
- Support API UpdateCacheRule.
- Support API UpdateCompressionRule.
- Support API UpdateHttpRequestHeaderModificationRule.
- Support API UpdateHttpResponseHeaderModificationRule.
- Support API UpdateHttpsBasicConfiguration.
- Support API UpdateIPv6.
- Support API UpdateList.
- Support API UpdateManagedTransform.
- Support API UpdateOriginRule.
- Support API UpdateRedirectRule.
- Support API UpdateRewriteUrlRule.
- Support API UpdateTieredCache.


2025-01-10 Version: 2.10.2
- Update API ListPages: add param QueryArgs.
- Update API ListUserRatePlanInstances: update response param.
- Update API SetCertificate: update response param.


2025-01-09 Version: 2.10.1
- Generated python 2024-09-10 for ESA.

2025-01-06 Version: 2.9.0
- Support API DescribeDDoSBpsList.
- Support API DescribeDDoSL7QpsList.


2024-12-27 Version: 2.8.0
- Support API ApplyCertificate.
- Support API CreateOriginPool.
- Support API DeleteOriginPool.
- Support API GetCertificate.
- Support API GetOriginPool.
- Support API ListCertificates.
- Support API ListOriginPools.
- Support API UpdateOriginPool.
- Update API CreateUserDeliveryTask: add param Details.
- Update API GetOriginProtection: update param SiteId.
- Update API GetUserDeliveryTask: update response param.
- Update API UpdatePage: update param Description.
- Update API UpdateUserDeliveryTask: add param Details.


2024-12-24 Version: 2.7.6
- Update API GetOriginProtection: update param SiteId.


2024-12-20 Version: 2.7.5
- Generated python 2024-09-10 for ESA.

2024-12-19 Version: 2.7.4
- Update API GetSiteWafSettings: add param Path.


2024-12-12 Version: 2.7.3
- Update API GetSiteWafSettings: add param Path.
- Update API ListWafRules: update param QueryArgs.


2024-12-07 Version: 2.7.2
- Update API PurgeCaches: update param SiteId.
- Update API PurgeCaches: update param Type.


2024-12-05 Version: 2.7.1
- Update API CommitRoutineStagingCode: update param Name.
- Update API CreateRoutine: update param Description.
- Update API CreateRoutine: update param Name.
- Update API CreateRoutine: update param SpecName.
- Update API CreateRoutineRelatedRecord: update param Name.
- Update API CreateRoutineRelatedRecord: update param RecordName.
- Update API CreateRoutineRelatedRecord: update param SiteId.
- Update API CreateRoutineRelatedRoute: add param ByPass.
- Update API CreateRoutineRelatedRoute: update param Name.
- Update API CreateRoutineRelatedRoute: update param Route.
- Update API CreateRoutineRelatedRoute: update param SiteId.
- Update API DeleteRoutine: update param Name.
- Update API DeleteRoutineCodeVersion: update param CodeVersion.
- Update API DeleteRoutineCodeVersion: update param Name.
- Update API DeleteRoutineRelatedRecord: update param Name.
- Update API DeleteRoutineRelatedRecord: update param RecordId.
- Update API DeleteRoutineRelatedRecord: update param RecordName.
- Update API DeleteRoutineRelatedRecord: update param SiteId.
- Update API DeleteRoutineRelatedRoute: update param Name.
- Update API DeleteRoutineRelatedRoute: update param Route.
- Update API DeleteRoutineRelatedRoute: update param RouteId.
- Update API DeleteRoutineRelatedRoute: update param SiteId.
- Update API GetRoutine: update param Name.
- Update API GetRoutine: update response param.
- Update API GetRoutineStagingCodeUploadInfo: update param Name.
- Update API PublishRoutineCodeVersion: update param Env.
- Update API PublishRoutineCodeVersion: update param Name.


2024-12-02 Version: 2.7.0
- Support API GetClientCertificateHostnames.
- Support API SetClientCertificateHostnames.


2024-11-29 Version: 2.6.0
- Support API CreateClientCertificate.
- Support API DeleteCertificate.
- Support API DeleteClientCaCertificate.
- Support API DeleteClientCertificate.
- Support API GetCertificateQuota.
- Support API GetClientCaCertificate.
- Support API GetClientCertificate.
- Support API ListCiphers.
- Support API ListClientCaCertificates.
- Support API RevokeClientCertificate.
- Support API UploadClientCaCertificate.
- Update API ListSites: add param OrderBy.
- Update API ListSites: update response param.
- Update API ListUserRatePlanInstances: add param RemainingExpireDays.


2024-11-22 Version: 2.5.0
- Support API CreateOriginProtection.
- Support API CreateSiteFunction.
- Support API DeleteOriginProtection.
- Support API DeleteSiteFunction.
- Support API GetOriginProtection.
- Support API ListSiteFunctions.
- Support API UpdateOriginProtection.
- Support API UpdateOriginProtectionIpWhiteList.
- Support API UpdateSiteFunction.


2024-11-20 Version: 2.4.5
- Update API DescribeDDoSAllEventList: update response param.


2024-11-19 Version: 2.4.4
- Update API ListRecords: update param Proxied.


2024-11-13 Version: 2.4.3
- Update API BatchCreateRecords: update param RecordList.
- Update API CreateScheduledPreloadExecutions: update param Executions.
- Update API GetEdgeContainerAppVersion: update response param.
- Update API ListEdgeContainerAppVersions: update response param.
- Update API ListUserRatePlanInstances: update response param.
- Update API ListWafManagedRules: add param ProtectionLevel.
- Update API ListWafManagedRules: update param QueryArgs.
- Update API ListWafTemplateRules: add param SiteId.


2024-11-08 Version: 2.4.2
- Generated python 2024-09-10 for ESA.

2024-11-06 Version: 2.4.1
- Generated python 2024-09-10 for ESA.

2024-10-28 Version: 2.4.0
- Support API CreateEdgeContainerApp.
- Support API CreateEdgeContainerAppRecord.
- Support API CreateEdgeContainerAppVersion.
- Support API DeleteEdgeContainerApp.
- Support API DeleteEdgeContainerAppRecord.
- Support API DeleteEdgeContainerAppVersion.
- Support API GetEdgeContainerApp.
- Support API GetEdgeContainerAppStatus.
- Support API GetEdgeContainerAppVersion.
- Support API GetEdgeContainerDeployRegions.
- Support API GetEdgeContainerLogs.
- Support API GetEdgeContainerStagingDeployStatus.
- Support API GetEdgeContainerTerminal.
- Support API ListEdgeContainerAppVersions.
- Support API PublishEdgeContainerAppVersion.
- Support API RebuildEdgeContainerAppStagingEnv.
- Support API RollbackEdgeContainerAppVersion.


2024-10-18 Version: 2.3.1
- Update API CreateSiteDeliveryTask: update param DiscardRate.
- Update API CreateSiteDeliveryTask: update param SiteId.


2024-10-16 Version: 2.3.0
- Support API CommitRoutineStagingCode.
- Support API CreateRoutine.
- Support API CreateRoutineRelatedRecord.
- Support API CreateRoutineRelatedRoute.
- Support API DeleteRoutine.
- Support API DeleteRoutineCodeVersion.
- Support API DeleteRoutineRelatedRecord.
- Support API DeleteRoutineRelatedRoute.
- Support API GetErService.
- Support API GetRoutine.
- Support API GetRoutineStagingCodeUploadInfo.
- Support API GetRoutineStagingEnvIp.
- Support API GetRoutineUserInfo.
- Support API ListRoutineCanaryAreas.
- Support API ListRoutineOptionalSpecs.
- Support API PublishRoutineCodeVersion.


2024-10-12 Version: 2.2.0
- Support API ListClientCertificates.


2024-10-11 Version: 2.1.0
- Support API DeleteKv.
- Support API DeleteKvNamespace.
- Support API DescribeKvAccountStatus.
- Support API GetKv.
- Support API GetKvAccount.


2024-10-11 Version: 2.0.1
- Update API CreateRecord: update param HostPolicy.
- Update API UpdateRecord: update param HostPolicy.


2024-10-10 Version: 2.0.0
- Support API GetCacheReserveSpecification.
- Support API ListCacheReserveInstances.
- Support API ListEdgeContainerApps.
- Support API ListEdgeRoutinePlans.
- Support API ListInstanceQuotas.
- Support API ListInstanceQuotasWithUsage.
- Support API ListUserRatePlanInstances.
- Support API ListWafManagedRules.
- Delete API AddUserBusinessForm.
- Delete API AdvancePurgeObjectCache.
- Delete API PutKvAccount.
- Update API SetCertificate: update param SiteId.


2024-10-08 Version: 1.0.0
- Generated python 2024-09-10 for ESA.

