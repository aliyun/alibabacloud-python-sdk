2025-05-29 Version: 4.0.2
- Update API CreateHttpApiRoute: add request parameters body.mcpRouteConfig.


2025-05-21 Version: 4.0.1
- Update API UpdateHttpApi: add request parameters body.onlyChangeConfig.


2025-05-21 Version: 4.0.0
- Support API CreatePluginAttachment.
- Support API DeletePluginAttachment.
- Support API GetPluginAttachment.
- Support API ListPlugins.
- Support API UpdatePluginAttachment.
- Update API CreateDomain: add request parameters body.gatewayType.
- Update API CreateHttpApi: add request parameters body.ingressConfig.clusterId.
- Update API CreateHttpApiRoute: add request parameters body.deployConfigs.
- Update API DeployHttpApi: add request parameters body.httpApiConfig.
- Update API DeployHttpApi: add request parameters body.restApiConfig.gatewayId.
- Update API DeployHttpApi: add request parameters body.restApiConfig.operationIds.
- Update API GetResourceOverview: add request parameters gatewayType.
- Update API GetResourceOverview: add request The number of query or body parameters has changed from zero to many.
- Update API ImportHttpApi: add request parameters body.deployConfigs.
- Update API ImportHttpApi: add request parameters body.mcpRouteId.
- Update API ListDomains: add request parameters gatewayType.
- Update API ListEnvironments: add request parameters gatewayType.
- Update API ListGateways: add request parameters gatewayType.
- Update API ListGateways: add response parameters Body.data.items.$.gatewayType.
- Update API ListGateways: add response parameters Body.data.items.$.legacy.
- Update API ListHttpApiOperations: add request parameters forDeploy.
- Update API ListHttpApiOperations: add request parameters gatewayId.
- Update API ListHttpApiRoutes: add request parameters forDeploy.
- Update API ListHttpApis: add request parameters gatewayType.
- Update API UndeployHttpApi: add request parameters body.gatewayId.
- Update API UndeployHttpApi: add request parameters body.operationId.
- Update API UpdateHttpApiRoute: add request parameters body.deployConfigs.


2025-04-14 Version: 3.2.2
- Update API ListServices: add request parameters sourceTypes.


2025-03-31 Version: 3.2.1
- Update API GetDashboard: add request parameters pluginId.
- Update API GetDashboard: add request parameters upstreamCluster.
- Update API ListHttpApis: add request parameters withAPIsPublishedToEnvironment.
- Update API ListHttpApis: add request parameters withPolicyConfigs.


2025-03-19 Version: 3.2.0
- Support API UndeployHttpApi.
- Update API CreateDomain: update param body.
- Update API CreateService: update param body.
- Update API GetDomain: update response param.
- Update API UpdateDomain: update param body.


2025-02-26 Version: 3.1.0
- Support API CreateService.
- Support API GetService.
- Support API ListHttpApiRoutes.
- Support API ListServices.


2025-02-14 Version: 3.0.0
- Support API ChangeResourceGroup.
- Support API CreateHttpApiRoute.
- Support API CreatePolicy.
- Support API CreatePolicyAttachment.
- Support API DeleteGatewaySecurityGroupRule.
- Support API DeleteHttpApiRoute.
- Support API DeletePolicy.
- Support API DeletePolicyAttachment.
- Support API DeployHttpApi.
- Support API ExportHttpApi.
- Support API GetDashboard.
- Support API GetPolicy.
- Support API GetPolicyAttachment.
- Support API GetResourceOverview.
- Support API GetTraceConfig.
- Support API ImportHttpApi.
- Support API ListPolicyClasses.
- Support API ListSslCerts.
- Support API ListZones.
- Support API RestartGateway.
- Support API UpdateGatewayFeature.
- Support API UpdateGatewayName.
- Support API UpdateHttpApiRoute.
- Support API UpdatePolicy.
- Support API UpgradeGateway.
- Update API CreateHttpApi: update param body.
- Update API GetDomain: update response param.
- Update API ListGateways: add param tag.
- Update API ListGateways: delete param tags.
- Update API ListGateways: update response param.
- Update API ListHttpApis: add param withIngressInfo.
- Update API UpdateDomain: update param body.
- Update API UpdateHttpApi: update param body.


2024-12-03 Version: 2.0.1
- Update API CreateDomain: update param body.
- Update API GetDomain: update response param.
- Update API ListHttpApiOperations: add param withPluginAttachmentByPluginId.
- Update API ListHttpApis: add param withAuthPolicyList.
- Update API ListHttpApis: add param withEnvironmentInfoById.
- Update API ListHttpApis: add param withPluginAttachmentByPluginId.
- Update API UpdateDomain: update param body.


2024-11-26 Version: 2.0.0
- Support API GetHttpApiRoute.
- Delete API CreateGatewayRoute.
- Delete API CreateGatewayService.
- Delete API CreateGatewayServiceVersion.
- Delete API CreateServiceSource.
- Delete API DeleteGatewayRoute.
- Delete API DeleteGatewayService.
- Delete API DeleteGatewayServiceVersion.
- Delete API DeleteServiceSource.
- Delete API GetGatewayRoute.
- Delete API GetGatewayService.
- Delete API ListGatewayRoutes.
- Delete API ListGatewayServices.
- Delete API OfflineGatewayRoute.
- Delete API OfflineHttpApi.
- Delete API PublishGatewayRoute.
- Delete API PublishHttpApi.
- Delete API UpdateGatewayRoute.
- Delete API UpdateGatewayService.
- Delete API UpdateGatewayServiceVersion.
- Delete API UpdateServiceSource.
- Update API CreateDomain: update param body.
- Update API CreateEnvironment: update param body.
- Update API CreateHttpApi: add param RegionId.
- Update API CreateHttpApi: update param body.
- Update API GetDomain: add param withStatistics.
- Update API GetDomain: update response param.
- Update API GetEnvironment: add param withStatistics.
- Update API GetEnvironment: add param withVpcInfo.
- Update API GetEnvironment: update response param.
- Update API GetGateway: update response param.
- Update API ListDomains: add param resourceGroupId.
- Update API ListEnvironments: add param resourceGroupId.
- Update API ListEnvironments: update response param.
- Update API ListGateways: add param resourceGroupId.
- Update API ListGateways: add param tags.
- Update API ListGateways: update response param.
- Update API ListHttpApiOperations: add param consumerAuthorizationRuleId.
- Update API ListHttpApiOperations: add param withConsumerInEnvironmentId.
- Update API ListHttpApiOperations: add param withConsumerInfoById.
- Update API ListHttpApis: add param gatewayId.
- Update API ListHttpApis: add param resourceGroupId.
- Update API ListHttpApis: add param types.
- Update API ListHttpApis: add param withAuthPolicyInEnvironmentId.
- Update API ListHttpApis: add param withConsumerInfoById.
- Update API ListHttpApis: add param withEnvironmentInfo.
- Update API ListHttpApis: delete param publishedOnly.
- Update API ListHttpApis: update param keyword.
- Update API ListHttpApis: update param name.
- Update API ListHttpApis: update param pageNumber.
- Update API ListHttpApis: update param pageSize.
- Update API UpdateDomain: update response param.
- Update API UpdateHttpApi: update param body.


2024-08-08 Version: 1.0.5
- Generated python 2024-03-27 for APIG.

2024-08-06 Version: 1.0.4
- Update API ListGateways: update response param.


2024-08-05 Version: 1.0.3
- Update API ListHttpApiOperations: add param name.
- Update API ListHttpApis: add param name.


2024-08-05 Version: 1.0.3
- Update API ListHttpApiOperations: add param name.
- Update API ListHttpApis: add param name.


2024-07-29 Version: 1.0.2
- Update API ListDomains: add param gatewayId.


2024-07-26 Version: 1.0.1
- Update API ListHttpApis: add param publishedOnly.


2024-07-25 Version: 1.0.0
- Generated python 2024-03-27 for APIG.

