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

