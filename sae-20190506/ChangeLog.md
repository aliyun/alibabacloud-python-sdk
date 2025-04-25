2025-04-25 Version: 2.0.4
- Update API CreateApplication: add request parameters InitContainersConfig.
- Update API DeployApplication: add request parameters InitContainersConfig.
- Update API DescribeApplicationConfig: add response parameters Body.Data.InitContainersConfig.


2025-04-23 Version: 2.0.3
- Update API DescribeConfigurationPrice: add request parameters NewSaeVersion.
- Update API QueryResourceStatics: add response parameters Body.Data.RealTimeRes.EphemeralStorage.
- Update API QueryResourceStatics: add response parameters Body.Data.Summary.Cu.
- Update API QueryResourceStatics: add response parameters Body.Data.Summary.EphemeralStorage.


2025-04-15 Version: 2.0.2
- Update API DeployApplication: add request parameters NewSaeVersion.


2025-04-07 Version: 2.0.1
- Update API CreateApplication: add request parameters DiskSize.
- Update API DescribeApplicationConfig: add response parameters Body.Data.DiskSize.
- Update API DescribeApplicationInstances: add request parameters PipelineId.
- Update API DescribeApplicationInstances: add response parameters Body.Data.Instances.$.Timestamp.
- Update API GetChangeOrderMetric: add request parameters AppId.
- Update API GetChangeOrderMetric: add request parameters CoType.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.AvgTimeCostMs.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.MaxTimeCostMs.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.OptimizeSuggestions.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.TaskTimeCostMsAvg.
- Update API ListApplications: add response parameters Body.Data.Applications.$.DiskSize.
- Update API ListChangeOrders: add request parameters OrderBy.
- Update API ListChangeOrders: add request parameters Reverse.
- Update API RescaleApplicationVertically: add request parameters DiskSize.


2025-04-07 Version: 2.0.1
- Update API CreateApplication: add request parameters DiskSize.
- Update API DescribeApplicationConfig: add response parameters Body.Data.DiskSize.
- Update API DescribeApplicationInstances: add request parameters PipelineId.
- Update API DescribeApplicationInstances: add response parameters Body.Data.Instances.$.Timestamp.
- Update API GetChangeOrderMetric: add request parameters AppId.
- Update API GetChangeOrderMetric: add request parameters CoType.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.AvgTimeCostMs.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.MaxTimeCostMs.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.OptimizeSuggestions.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.TaskTimeCostMsAvg.
- Update API ListApplications: add response parameters Body.Data.Applications.$.DiskSize.
- Update API ListChangeOrders: add request parameters OrderBy.
- Update API ListChangeOrders: add request parameters Reverse.
- Update API RescaleApplicationVertically: add request parameters DiskSize.


2025-04-07 Version: 2.0.1
- Update API CreateApplication: add request parameters DiskSize.
- Update API DescribeApplicationConfig: add response parameters Body.Data.DiskSize.
- Update API DescribeApplicationInstances: add request parameters PipelineId.
- Update API DescribeApplicationInstances: add response parameters Body.Data.Instances.$.Timestamp.
- Update API GetChangeOrderMetric: add request parameters AppId.
- Update API GetChangeOrderMetric: add request parameters CoType.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.AvgTimeCostMs.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.MaxTimeCostMs.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.OptimizeSuggestions.
- Update API GetChangeOrderMetric: add response parameters Body.Data.$.TaskTimeCostMsAvg.
- Update API ListApplications: add response parameters Body.Data.Applications.$.DiskSize.
- Update API ListChangeOrders: add request parameters OrderBy.
- Update API ListChangeOrders: add request parameters Reverse.
- Update API RescaleApplicationVertically: add request parameters DiskSize.


2025-04-01 Version: 2.0.0
- Support API UnbindNlb.
- Update API CreateApplication: add request parameters MicroserviceEngineConfig.
- Update API CreateApplication: add request parameters NewSaeVersion.
- Update API CreateIngress: add request parameters CorsConfig.
- Update API DeployApplication: add request parameters MicroserviceEngineConfig.
- Update API DescribeApplicationScalingRule: delete response parameters Body.Data.EnableIdle.
- Update API DescribeApplicationScalingRules: delete response parameters Body.Data.ApplicationScalingRules.$.EnableIdle.
- Update API DescribeIngress: add response parameters Body.Data.CorsConfig.
- Update API ListApplications: add response parameters Body.Data.Applications.$.EnableIdle.
- Update API ListIngresses: add response parameters Body.Data.IngressList.$.CorsConfig.
- Update API UpdateIngress: add request parameters CorsConfig.


2025-03-12 Version: 1.26.0
- Support API ListAppServices.
- Update API DeployApplication: add param SwimlanePvtzDiscoverySvc.
- Update API DescribeApplicationConfig: update response param.
- Update API DescribeApplicationSlbs: update response param.
- Update API DescribeConfigurationPrice: add param ResourceType.
- Update API ListApplications: update response param.
- Update API ListIngresses: update response param.


2025-01-13 Version: 1.25.2
- Update API CreateApplication: add param CustomImageNetworkType.
- Update API CreateApplication: add param ResourceType.
- Update API CreateIngress: add param AddressType.
- Update API CreateIngress: add param LoadBalancerEdition.
- Update API CreateIngress: add param ZoneMappings.
- Update API CreateIngress: update param SlbId.
- Update API DeployApplication: add param CustomImageNetworkType.
- Update API DescribeApplicationConfig: update response param.
- Update API DescribeApplicationInstances: add param InstanceId.
- Update API DescribeApplicationInstances: update response param.
- Update API DescribeIngress: update response param.
- Update API GetWebshellToken: add param ContainerName.


2025-01-10 Version: 1.25.1
- Update API CreateApplication: add param CustomImageNetworkType.
- Update API CreateIngress: add param AddressType.
- Update API CreateIngress: add param LoadBalancerEdition.
- Update API CreateIngress: add param ZoneMappings.
- Update API CreateIngress: update param SlbId.
- Update API DeployApplication: add param CustomImageNetworkType.
- Update API DescribeApplicationConfig: update response param.
- Update API DescribeApplicationInstances: add param InstanceId.
- Update API DescribeApplicationInstances: update response param.
- Update API DescribeIngress: update response param.
- Update API GetWebshellToken: add param ContainerName.


2024-12-20 Version: 1.25.0
- Support API GetWebshellToken.
- Update API CreateApplication: add param EnableSidecarResourceIsolated.
- Update API CreateApplication: add param SecretMountDesc.
- Update API CreateApplication: add param SidecarContainersConfig.
- Update API DeployApplication: add param EnableSidecarResourceIsolated.
- Update API DeployApplication: add param SecretMountDesc.
- Update API DeployApplication: add param SidecarContainersConfig.
- Update API DescribeApplicationConfig: update response param.
- Update API DescribeApplicationInstances: update response param.
- Update API DescribeInstanceLog: add param ContainerId.


2024-11-08 Version: 1.24.6
- Update API CreateApplication: add param OidcRoleName.
- Update API DeployApplication: add param OidcRoleName.
- Update API DescribeApplicationConfig: update response param.


2024-11-06 Version: 1.24.5
- Update API DescribeIngress: update response param.


2024-10-29 Version: 1.24.4
- Update API CreateIngress: add param EnableXForwardedFor.
- Update API CreateIngress: add param EnableXForwardedForClientSrcPort.
- Update API CreateIngress: add param EnableXForwardedForProto.
- Update API CreateIngress: add param EnableXForwardedForSlbId.
- Update API CreateIngress: add param EnableXForwardedForSlbPort.
- Update API CreateIngress: update param IdleTimeout.
- Update API CreateIngress: update param RequestTimeout.
- Update API CreateIngress: update param SecurityPolicyId.
- Update API DescribeIngress: update response param.
- Update API UpdateIngress: add param EnableXForwardedFor.
- Update API UpdateIngress: add param EnableXForwardedForClientSrcPort.
- Update API UpdateIngress: add param EnableXForwardedForProto.
- Update API UpdateIngress: add param EnableXForwardedForSlbId.
- Update API UpdateIngress: add param EnableXForwardedForSlbPort.
- Update API UpdateIngress: update param IdleTimeout.
- Update API UpdateIngress: update param RequestTimeout.
- Update API UpdateIngress: update param SecurityPolicyId.


2024-10-28 Version: 1.24.3
- Update API QueryResourceStatics: update response param.


2024-10-17 Version: 1.24.2
- Update API DescribeConfigurationPrice: update response param.


2024-10-11 Version: 1.24.1
- Update API CreateApplication: add param EnableCpuBurst.
- Update API DeployApplication: add param EnableCpuBurst.
- Update API DescribeApplicationConfig: update response param.


2024-10-10 Version: 1.24.0
- Support API DowngradeApplicationApmService.
- Support API GetApplication.
- Support API UpgradeApplicationApmService.


2024-09-24 Version: 1.23.6
- Update API CreateApplication: add param Dotnet.
- Update API DeployApplication: add param Dotnet.
- Update API DescribeApplicationConfig: update response param.
- Update API ListApplications: update response param.
- Update API RescaleApplicationVertically: add param autoEnableApplicationScalingRule.
- Update API RescaleApplicationVertically: add param minReadyInstanceRatio.
- Update API RescaleApplicationVertically: add param minReadyInstances.


2024-09-11 Version: 1.23.5
- Update API CreateApplicationScalingRule: add param EnableIdle.
- Update API CreateApplicationScalingRule: update response param.
- Update API CreateIngress: add param IdleTimeout.
- Update API DescribeApplicationScalingRule: update response param.
- Update API DescribeApplicationScalingRules: update response param.
- Update API DescribeIngress: update response param.
- Update API UpdateApplicationScalingRule: add param EnableIdle.
- Update API UpdateApplicationScalingRule: update response param.
- Update API UpdateIngress: add param IdleTimeout.


2024-08-28 Version: 1.23.4
- Update API CreateApplication: add param EnableNewArms.
- Update API DeployApplication: add param EnableNewArms.
- Update API DescribeApplicationConfig: update response param.
- Update API DescribeWebCustomDomain: update response param.
- Update API ListWebCustomDomains: update param NamespaceId.


2024-08-21 Version: 1.23.3
- Update API CreateIngress: add param RequestTimeout.
- Update API CreateIngress: add param SecurityPolicyId.
- Update API DescribeIngress: update response param.
- Update API UpdateIngress: add param RequestTimeout.
- Update API UpdateIngress: add param SecurityPolicyId.


2024-08-12 Version: 1.23.2
- Update API DescribeApplicationConfig: update response param.


2024-08-07 Version: 1.23.1
- Update API BindSlb: add param InternetSlbChargeType.
- Update API BindSlb: add param IntranetSlbChargeType.
- Update API DescribeApplicationSlbs: update response param.


2024-07-19 Version: 1.23.0
- Support API CreateWebApplication.
- Support API CreateWebCustomDomain.
- Support API DeleteWebApplication.
- Support API DeleteWebApplicationRevision.
- Support API DeleteWebCustomDomain.
- Support API DescribeWebApplication.
- Support API DescribeWebApplicationResourceStatics.
- Support API DescribeWebApplicationRevision.
- Support API DescribeWebApplicationScalingConfig.
- Support API DescribeWebApplicationTrafficConfig.
- Support API DescribeWebCustomDomain.
- Support API DescribeWebInstanceLogs.
- Support API ListWebApplicationInstances.
- Support API ListWebApplicationRevisions.
- Support API ListWebApplications.
- Support API ListWebCustomDomains.
- Support API PublishWebApplicationRevision.
- Support API StartWebApplication.
- Support API StopWebApplication.
- Support API UpdateWebApplication.
- Support API UpdateWebApplicationScalingConfig.
- Support API UpdateWebApplicationTrafficConfig.
- Support API UpdateWebCustomDomain.
- Update API BatchStartApplications: add param Version.
- Update API BatchStopApplications: add param Version.
- Update API CreateApplication: add param AppSource.
- Update API CreateApplication: add param BaseAppId.
- Update API CreateApplication: add param EnableEbpf.
- Update API CreateApplication: add param MicroRegistrationConfig.
- Update API CreateApplication: add param Php.
- Update API CreateApplication: add param SaeVersion.
- Update API CreateApplication: add param ServiceTags.
- Update API CreateApplicationScalingRule: update response param.
- Update API CreateSecret: update param SecretData.
- Update API DeployApplication: add param Cpu.
- Update API DeployApplication: add param Memory.
- Update API DeployApplication: add param MicroRegistrationConfig.
- Update API DeployApplication: add param Php.
- Update API DeployApplication: add param Replicas.
- Update API DeployApplication: add param SecurityGroupId.
- Update API DeployApplication: add param ServiceTags.
- Update API DeployApplication: add param VSwitchId.
- Update API DescribeAppServiceDetail: add param NacosInstanceId.
- Update API DescribeAppServiceDetail: add param NacosNamespaceId.
- Update API DescribeAppServiceDetail: update response param.
- Update API DescribeApplicationConfig: update response param.
- Update API DescribeApplicationScalingRule: update response param.
- Update API DescribeApplicationScalingRules: update response param.
- Update API DescribeApplicationSlbs: update response param.
- Update API DescribeConfigurationPrice: update response param.
- Update API DescribeIngress: update response param.
- Update API GetArmsTopNMetric: add param AppSource.
- Update API GetArmsTopNMetric: add param CpuStrategy.
- Update API GetAvailabilityMetric: add param AppSource.
- Update API GetAvailabilityMetric: add param CpuStrategy.
- Update API GetChangeOrderMetric: add param AppSource.
- Update API GetChangeOrderMetric: add param CpuStrategy.
- Update API GetScaleAppMetric: add param AppSource.
- Update API GetScaleAppMetric: add param CpuStrategy.
- Update API GetWarningEventMetric: add param AppSource.
- Update API GetWarningEventMetric: add param CpuStrategy.
- Update API ListApplications: add param AppSource.
- Update API ListApplications: update response param.
- Update API ListIngresses: update response param.
- Update API ListJobs: update response param.
- Update API RestartApplication: add param AutoEnableApplicationScalingRule.
- Update API UpdateApplicationScalingRule: update response param.
- Update API UpdateSecret: update param SecretData.


2023-03-23 Version: 1.22.11
- Support Create Namespace Without Micro Service Registration.

2023-02-15 Version: 1.22.10
- Add execjob api.

2023-02-08 Version: 1.22.9
- Add metric api.

2023-01-04 Version: 1.22.8
- Update deployApplication request parameters.

2022-12-19 Version: 1.22.7
- Fixed ApplicationScalingRule related api response struct.

2022-12-19 Version: 1.22.6
- Fixed ApplicationScalingRule related api response struct.

2022-12-01 Version: 1.22.2
- Add updateJob.

2022-12-01 Version: 1.22.1
- Add updateJob.

2022-08-02 Version: 1.21.3
- Delete kafka params.

2022-07-07 Version: 1.21.2
- Support execJob.

2022-07-07 Version: 1.21.1
- Support execJob.

2022-07-07 Version: 1.21.0
- Support execJob.

2022-05-16 Version: 1.20.1
- Support UpdateApplicationVswitches and DescribeComponents.

2022-05-12 Version: 1.20.0
- Support alb.

2022-03-15 Version: 1.19.0
- Support collect logs to kafka.

2022-01-18 Version: 1.18.16
- Support tag route rules crud.

2021-11-26 Version: 1.0.0
- Support tag route rules crud.

