2025-12-24 Version: 1.12.0
- Support API DescribeInstanceCreateAndDeleteStatistics.
- Support API DescribeScalingActivityStatistics.
- Support API QueryHistoricalMetric.
- Support API QueryPredictiveMetric.
- Support API QueryPredictiveTaskInfo.
- Support API QueryPredictiveValue.


2025-12-17 Version: 1.11.0
- Support API DeleteDiagnoseReport.


2025-12-17 Version: 1.11.0
- Support API DeleteDiagnoseReport.


2025-12-17 Version: 1.11.0
- Support API DeleteDiagnoseReport.


2025-12-05 Version: 1.10.22
- Update API RemoveInstances: add request parameters LifecycleHookContext.LifecycleHookResult.
- Update API RemoveInstances: add response parameters Body.IgnoredInstances.
- Update API ScaleWithAdjustment: add request parameters LifecycleHookContext.LifecycleHookResult.


2025-12-03 Version: 1.10.21
- Update API ModifyEciScalingConfiguration: add request parameters Override.


2025-12-03 Version: 1.10.21
- Update API ModifyEciScalingConfiguration: add request parameters Override.


2025-11-04 Version: 1.10.20
- Update API CreateScalingGroup: add request parameters AutoRebalance.
- Update API CreateScalingGroup: add request parameters BalanceMode.
- Update API DescribeScalingGroups: add response parameters Body.ScalingGroups.$.AutoRebalance.
- Update API DescribeScalingGroups: add response parameters Body.ScalingGroups.$.BalanceMode.
- Update API ModifyScalingGroup: add request parameters AutoRebalance.
- Update API ModifyScalingGroup: add request parameters BalanceMode.


2025-09-12 Version: 1.10.19
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.CheckpointPauseTime.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.Checkpoints.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.Containers.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.LaunchTemplateId.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.LaunchTemplateOverrides.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.LaunchTemplateVersion.
- Update API StartInstanceRefresh: add request parameters CheckpointPauseTime.
- Update API StartInstanceRefresh: add request parameters Checkpoints.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.Containers.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.LaunchTemplateId.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.LaunchTemplateOverrides.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.LaunchTemplateVersion.


2025-09-12 Version: 1.10.19
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.CheckpointPauseTime.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.Checkpoints.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.Containers.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.LaunchTemplateId.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.LaunchTemplateOverrides.
- Update API DescribeInstanceRefreshes: add response parameters Body.InstanceRefreshTasks.$.DesiredConfiguration.LaunchTemplateVersion.
- Update API StartInstanceRefresh: add request parameters CheckpointPauseTime.
- Update API StartInstanceRefresh: add request parameters Checkpoints.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.Containers.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.LaunchTemplateId.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.LaunchTemplateOverrides.
- Update API StartInstanceRefresh: add request parameters DesiredConfiguration.LaunchTemplateVersion.


2025-08-11 Version: 1.10.18
- Update API CreateNotificationConfiguration: add request parameters MessageEncoding.
- Update API DescribeNotificationConfigurations: add response parameters Body.NotificationConfigurationModels.$.MessageEncoding.
- Update API ModifyNotificationConfiguration: add request parameters MessageEncoding.


2025-07-25 Version: 1.10.17
- Update API ScaleWithAdjustment: add request parameters Overrides.UserData.


2025-07-17 Version: 1.10.16
- Update API ScaleWithAdjustment: add request parameters ExecutionMode.
- Update API ScaleWithAdjustment: add response parameters Body.PlanResult.


2025-05-08 Version: 1.10.15
- Update API ScaleWithAdjustment: add request parameters ParallelTask.


2025-04-29 Version: 1.10.14
- Update API CreateScalingRule: add request parameters AlarmOptions.
- Update API DescribeScalingRules: add response parameters Body.ScalingRules.$.Alarms.$.Period.
- Update API ModifyScalingRule: add request parameters AlarmOptions.


2025-04-16 Version: 1.10.13
- Update API RemoveInstances: add request parameters LifecycleHookContext.


2025-04-08 Version: 1.10.12
- Update API ModifyInstanceAttribute: add request parameters InstanceIds.


2025-03-26 Version: 1.10.11
- Update API CreateScalingConfiguration: add request parameters ResourcePoolOptions.
- Update API DescribeScalingConfigurations: add response parameters Body.ScalingConfigurations.$.ResourcePoolOptions.
- Update API ModifyScalingConfiguration: add request parameters ResourcePoolOptions.


2025-03-14 Version: 1.10.10
- Update API DescribeElasticStrength: update response param.


2025-02-18 Version: 1.10.9
- Update API CreateScalingGroup: update param CapacityOptions.
- Update API DescribeScalingActivities: update response param.
- Update API DescribeScalingGroups: update response param.
- Update API ModifyScalingGroup: update param CapacityOptions.


2025-01-14 Version: 1.10.8
- Update API DescribeScalingActivities: update response param.


2025-01-08 Version: 1.10.7
- Update API AttachInstances: add param IgnoreInvalidInstance.


2024-12-18 Version: 1.10.6
- Update API DescribeElasticStrength: update response param.


2024-12-17 Version: 1.10.5
- Update API ModifyScheduledTask: add param RegionId.


2024-12-12 Version: 1.10.4
- Generated python 2022-02-22 for Ess.

2024-12-10 Version: 1.10.3
- Update API CreateEciScalingConfiguration: add param GpuDriverVersion.
- Update API CreateScalingGroup: add param CapacityOptions.
- Update API DescribeEciScalingConfigurations: update response param.
- Update API DescribeInstanceRefreshes: update response param.
- Update API DescribeScalingGroups: update response param.
- Update API ModifyEciScalingConfiguration: add param GpuDriverVersion.
- Update API ModifyScalingGroup: add param CapacityOptions.
- Update API StartInstanceRefresh: add param SkipMatching.


2024-12-10 Version: 1.10.3
- Update API CreateEciScalingConfiguration: add param GpuDriverVersion.
- Update API CreateScalingGroup: add param CapacityOptions.
- Update API DescribeEciScalingConfigurations: update response param.
- Update API DescribeInstanceRefreshes: update response param.
- Update API DescribeScalingGroups: update response param.
- Update API ModifyEciScalingConfiguration: add param GpuDriverVersion.
- Update API ModifyScalingGroup: add param CapacityOptions.
- Update API StartInstanceRefresh: add param SkipMatching.


2024-12-02 Version: 1.10.2
- Update API DescribeElasticStrength: add param DataDiskCategories.
- Update API DescribeElasticStrength: add param ImageFamily.
- Update API DescribeElasticStrength: add param ImageId.
- Update API DescribeElasticStrength: add param ImageName.
- Update API DescribeElasticStrength: add param Ipv6AddressCount.
- Update API DescribeElasticStrength: add param SpotStrategy.
- Update API DescribeElasticStrength: add param VSwitchIds.


2024-11-12 Version: 1.10.1
- Update API DescribePatternTypes: add param ZoneId.


2024-11-11 Version: 1.10.0
- Support API CreateDiagnoseReport.
- Support API DescribeDiagnoseReports.
- Support API DescribeScalingGroupDiagnoseDetails.


2024-11-08 Version: 1.9.1
- Update API CreateScalingConfiguration: add param HttpEndpoint.
- Update API CreateScalingConfiguration: add param HttpTokens.
- Update API DescribeScalingConfigurations: update response param.
- Update API ModifyScalingConfiguration: add param HttpEndpoint.
- Update API ModifyScalingConfiguration: add param HttpTokens.
- Update API ModifyScalingConfiguration: add param InternetMaxBandwidthIn.


2024-10-21 Version: 1.9.0
- Support API DescribeElasticStrength.


2024-10-16 Version: 1.8.2
- Update API CreateScalingGroup: add param StopInstanceTimeout.
- Update API DescribeScalingGroups: update response param.
- Update API ModifyScalingGroup: add param StopInstanceTimeout.
- Update API RemoveInstances: add param StopInstanceTimeout.


2024-10-10 Version: 1.8.1
- Update API CreateScalingConfiguration: add param SecurityOptions.
- Update API DescribeScalingConfigurations: update response param.
- Update API ModifyScalingConfiguration: add param SecurityOptions.


2024-09-14 Version: 1.8.0
- Support API CancelInstanceRefresh.
- Support API DescribeInstanceRefreshes.
- Support API ResumeInstanceRefresh.
- Support API RollbackInstanceRefresh.
- Support API StartInstanceRefresh.
- Support API SuspendInstanceRefresh.
- Update API CreateScalingRule: add param HybridMetrics.
- Update API CreateScalingRule: add param HybridMonitorNamespace.
- Update API CreateScalingRule: add param MetricType.
- Update API DescribeAlarms: update response param.
- Update API DescribeScalingActivities: add param InstanceRefreshTaskId.
- Update API DescribeScalingActivities: update response param.
- Update API DescribeScalingGroups: update response param.
- Update API DescribeScalingRules: update response param.
- Update API ModifyScalingRule: add param HybridMetrics.
- Update API ModifyScalingRule: add param HybridMonitorNamespace.
- Update API ModifyScalingRule: add param MetricType.


2024-08-06 Version: 1.7.4
- Generated python 2022-02-22 for Ess.

2024-08-05 Version: 1.7.3
- Update API CreateNotificationConfiguration: add param TimeZone.
- Update API DescribeNotificationConfigurations: update response param.
- Update API ModifyNotificationConfiguration: add param TimeZone.


2024-07-04 Version: 1.7.2
- Update API DescribeScheduledTasks: add param RecurrenceType.
- Update API DescribeScheduledTasks: add param RecurrenceValue.
- Update API DescribeScheduledTasks: add param TaskEnabled.
- Update API DescribeScheduledTasks: add param TaskName.


2024-07-03 Version: 1.7.1
- Update API DescribeScalingConfigurations: update response param.
- Update API ModifyScalingConfiguration: add param Password.


2024-07-03 Version: 1.7.1
- Update API DescribeScalingConfigurations: update response param.
- Update API ModifyScalingConfiguration: add param Password.


2024-06-14 Version: 1.7.0
- Support API DescribeAlertConfiguration.
- Support API ModifyAlertConfiguration.


2024-06-12 Version: 1.6.2
- Update API CreateScalingConfiguration: update param InstancePatternInfos.
- Update API DescribePatternTypes: add param CpuArchitectures.
- Update API DescribePatternTypes: add param GpuSpecs.
- Update API DescribePatternTypes: add param InstanceCategories.
- Update API DescribePatternTypes: add param InstanceTypeFamilies.
- Update API DescribePatternTypes: add param MaximumCpuCoreCount.
- Update API DescribePatternTypes: add param MaximumGpuAmount.
- Update API DescribePatternTypes: add param MaximumMemorySize.
- Update API DescribePatternTypes: add param MinimumBaselineCredit.
- Update API DescribePatternTypes: add param MinimumCpuCoreCount.
- Update API DescribePatternTypes: add param MinimumEniIpv6AddressQuantity.
- Update API DescribePatternTypes: add param MinimumEniPrivateIpAddressQuantity.
- Update API DescribePatternTypes: add param MinimumEniQuantity.
- Update API DescribePatternTypes: add param MinimumGpuAmount.
- Update API DescribePatternTypes: add param MinimumInitialCredit.
- Update API DescribePatternTypes: add param MinimumMemorySize.
- Update API DescribePatternTypes: add param PhysicalProcessorModels.
- Update API DescribeScalingConfigurations: update response param.
- Update API ModifyScalingConfiguration: update param InstancePatternInfos.


2024-05-21 Version: 1.6.1
- Update API DetachInstances: add param IgnoreInvalidInstance.
- Update API RemoveInstances: add param IgnoreInvalidInstance.


2024-05-16 Version: 1.6.0
- Support API DescribePatternTypes.


2024-04-23 Version: 1.5.2
- Update API AttachDBInstances: add param AttachMode.
- Update API AttachDBInstances: add param Type.
- Update API CreateScalingConfiguration: add param DedicatedHostClusterId.
- Update API CreateScalingGroup: add param DBInstances.
- Update API DescribeScalingConfigurations: update response param.
- Update API DescribeScalingGroups: update response param.
- Update API DetachDBInstances: add param RemoveSecurityGroup.
- Update API ModifyScalingConfiguration: add param DedicatedHostClusterId.


2024-04-17 Version: 1.5.1
- Generated python 2022-02-22 for Ess.

2024-03-20 Version: 1.5.0
- Support API ApplyEciScalingConfiguration.
- Support API DescribeEciScalingConfigurationDetail.
- Support API DescribeScalingGroupDetail.
- Support API ModifyInstanceAttribute.
- Update API CreateScalingConfiguration: add param NetworkInterfaces.
- Update API DescribeScalingActivities: update response param.
- Update API DescribeScalingConfigurations: update response param.
- Update API ModifyScalingConfiguration: add param NetworkInterfaces.
- Update API ModifyScalingGroup: add param ScalingPolicy.
- Update API ScaleWithAdjustment: add param ActivityMetadata.
- Update API ScaleWithAdjustment: add param LifecycleHookContext.


2024-03-13 Version: 1.4.0
- Support API ApplyEciScalingConfiguration.
- Support API DescribeEciScalingConfigurationDetail.
- Support API DescribeScalingGroupDetail.
- Support API ModifyInstanceAttribute.
- Update API DescribeScalingActivities: update response param.
- Update API ModifyScalingGroup: add param ScalingPolicy.
- Update API ScaleWithAdjustment: add param ActivityMetadata.
- Update API ScaleWithAdjustment: add param LifecycleHookContext.


2024-02-28 Version: 1.3.0
- Support API ApplyEciScalingConfiguration.
- Support API DescribeEciScalingConfigurationDetail.
- Support API DescribeScalingGroupDetail.
- Support API ModifyInstanceAttribute.
- Update API ModifyScalingGroup: add param ScalingPolicy.


2024-02-22 Version: 1.2.0
- Support API ModifyInstanceAttribute.
- Update API ModifyScalingGroup: add param ScalingPolicy.


2024-02-22 Version: 1.2.0
- Support API ModifyInstanceAttribute.
- Update API ModifyScalingGroup: add param ScalingPolicy.


2024-02-01 Version: 1.1.2
- Update API CreateScalingConfigurationadd CustomPriorities param.
- Update API CreateScalingGroupadd HealthCheckTypes param.
- Update API DescribeScalingConfigurationsupdate response param.
- Update API DescribeScalingGroupsupdate response param.
- Update API ModifyScalingConfigurationadd CustomPriorities param.
- Update API ModifyScalingGroupadd HealthCheckTypes param.


2024-01-29 Version: 1.1.1
- Update API CreateScalingConfigurationadd CustomPriorities param.
- Update API DescribeScalingConfigurationsupdate response param.
- Update API ModifyScalingConfigurationadd CustomPriorities param.


2024-01-23 Version: 1.1.0
- Generated python 2022-02-22 for Ess.

2023-12-25 Version: 1.0.15
- Generated python 2022-02-22 for Ess.

2023-12-06 Version: 1.0.14
- Generated python 2022-02-22 for Ess.

2023-12-04 Version: 1.0.13
- Generated python 2022-02-22 for Ess.

2023-11-17 Version: 1.0.12
- Generated python 2022-02-22 for Ess.

2023-10-18 Version: 1.0.11
- Generated python 2022-02-22 for Ess.

2023-10-18 Version: 1.0.10
- Generated python 2022-02-22 for Ess.

2023-09-19 Version: 1.0.9
- Generated python 2022-02-22 for Ess.

2023-08-23 Version: 1.0.8
- Generated python 2022-02-22 for Ess.

2023-07-20 Version: 1.0.7
- DescribeScalingInstances support creationTypes.

2023-04-19 Version: 1.0.6
- Configuration support LoginAsNonRoot .

2023-03-09 Version: 1.0.5
- Fix the incompatibility of some parameters in the SDK .

2023-02-12 Version: 1.0.4
- CreateScalingGroup and DescribeScalingGroup support NLB server group and new open api AttachServerGroups and DetachServerGroups .

2023-01-13 Version: 1.0.3
- CreateScalingGroup and DescribeScalingGroup support resourcegroup.

2022-10-14 Version: 1.0.2
- Support user custom removal  function policy.

2022-10-14 Version: 1.0.1
- LifecycleHook support disable and enable, ScaleWithAdjustment support scale by instance type.

2022-09-09 Version: 1.0.0
- Ess Tea 2022 SDK release.

