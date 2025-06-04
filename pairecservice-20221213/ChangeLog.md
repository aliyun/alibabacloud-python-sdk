2025-06-04 Version: 3.1.1
- Update API CreateFeatureConsistencyCheckJobConfig: add request parameters body.ResourceConfig.
- Update API GetFeatureConsistencyCheckJobConfig: add response parameters Body.ResourceConfig.
- Update API ListFeatureConsistencyCheckJobConfigs: add response parameters Body.FeatureConsistencyCheckConfigs.$.ResourceConfig.
- Update API UpdateFeatureConsistencyCheckJobConfig: add request parameters body.ResourceConfig.


2025-05-19 Version: 3.1.0
- Support API CompareSampleConsistencyJob.
- Support API CreateSampleConsistencyJob.
- Support API DeleteSampleConsistencyJob.
- Support API GetSampleConsistencyJob.
- Support API ListSampleConsistencyJobs.
- Support API QuerySampleConsistencyJobDifference.
- Support API ReportSampleConsistencyJob.
- Support API StopSampleConsistencyJob.
- Update API CheckInstanceResources: add request parameters body.ResourceId.
- Update API CreateTrafficControlTask: add request parameters body.FlinkResourceId.
- Update API GetTrafficControlTask: add response parameters Body.FlinkResourceId.
- Update API GetTrafficControlTask: add response parameters Body.FlinkResourceName.
- Update API ListTrafficControlTasks: add response parameters Body.TrafficControlTasks.$.FlinkResourceId.
- Update API ListTrafficControlTasks: add response parameters Body.TrafficControlTasks.$.FlinkResourceName.
- Update API UpdateTrafficControlTask: add request parameters body.FlinkResourceId.


2025-03-03 Version: 3.0.1
- Update API BackflowFeatureConsistencyCheckJobData: update param body.


2025-02-28 Version: 3.0.0
- Support API CheckTrafficControlTaskExpression.
- Support API QueryTrafficControlTargetItemReportDetail.
- Update API CheckInstanceResources: add param RegionId.
- Update API CloneEngineConfig: update param body.
- Update API CloneExperimentGroup: add param RegionId.
- Update API CloneLaboratory: add param RegionId.
- Update API CreateCrowd: add param RegionId.
- Update API CreateEngineConfig: update param body.
- Update API CreateExperiment: add param RegionId.
- Update API CreateFeatureConsistencyCheckJobConfig: update param body.
- Update API CreateLaboratory: add param RegionId.
- Update API CreateLayer: add param RegionId.
- Update API CreateParam: add param RegionId.
- Update API CreateScene: add param RegionId.
- Update API CreateSubCrowd: add param RegionId.
- Update API CreateTableMeta: add param RegionId.
- Update API CreateTrafficControlTask: update param body.
- Update API DeleteABMetric: add param RegionId.
- Update API DeleteABMetricGroup: add param RegionId.
- Update API DeleteCrowd: add param RegionId.
- Update API DeleteExperiment: add param RegionId.
- Update API DeleteExperimentGroup: add param RegionId.
- Update API DeleteLaboratory: add param RegionId.
- Update API DeleteLayer: add param RegionId.
- Update API DeleteParam: add param RegionId.
- Update API DeleteScene: add param RegionId.
- Update API DeleteSubCrowd: add param RegionId.
- Update API DeleteTableMeta: add param RegionId.
- Update API GenerateTrafficControlTaskCode: update param TrafficControlTaskId.
- Update API GenerateTrafficControlTaskCode: update param body.
- Update API GenerateTrafficControlTaskCode: update response param.
- Update API GetABMetric: add param RegionId.
- Update API GetABMetricGroup: add param RegionId.
- Update API GetCalculationJob: add param RegionId.
- Update API GetEngineConfig: update response param.
- Update API GetExperiment: add param RegionId.
- Update API GetFeatureConsistencyCheckJobConfig: update response param.
- Update API GetInstance: add param RegionId.
- Update API GetLaboratory: add param RegionId.
- Update API GetScene: add param RegionId.
- Update API GetSubCrowd: add param RegionId.
- Update API GetTableMeta: add param RegionId.
- Update API GetTrafficControlTask: update response param.
- Update API GetTrafficControlTaskTraffic: update response param.
- Update API ListABMetricGroups: add param RegionId.
- Update API ListABMetrics: add param RegionId.
- Update API ListCalculationJobs: add param RegionId.
- Update API ListCrowdUsers: add param RegionId.
- Update API ListCrowds: add param RegionId.
- Update API ListEngineConfigs: update response param.
- Update API ListExperiments: add param RegionId.
- Update API ListFeatureConsistencyCheckJobConfigs: update response param.
- Update API ListInstances: add param RegionId.
- Update API ListLaboratories: add param RegionId.
- Update API ListParams: add param RegionId.
- Update API ListScenes: add param RegionId.
- Update API ListSubCrowds: add param RegionId.
- Update API ListTableMetas: add param RegionId.
- Update API ListTrafficControlTargetTrafficHistory: update response param.
- Update API ListTrafficControlTasks: update response param.
- Update API OfflineExperiment: add param RegionId.
- Update API OfflineExperimentGroup: add param RegionId.
- Update API OfflineLaboratory: add param RegionId.
- Update API OnlineExperiment: add param RegionId.
- Update API OnlineExperimentGroup: add param RegionId.
- Update API OnlineLaboratory: add param RegionId.
- Update API PushAllExperiment: add param RegionId.
- Update API ReportABMetricGroup: add param RegionId.
- Update API UpdateABMetric: add param RegionId.
- Update API UpdateABMetricGroup: add param RegionId.
- Update API UpdateCrowd: add param RegionId.
- Update API UpdateEngineConfig: update param body.
- Update API UpdateExperiment: add param RegionId.
- Update API UpdateFeatureConsistencyCheckJobConfig: update param body.
- Update API UpdateLaboratory: add param RegionId.
- Update API UpdateLayer: add param RegionId.
- Update API UpdateParam: add param RegionId.
- Update API UpdateScene: add param RegionId.
- Update API UpdateTableMeta: add param RegionId.
- Update API UpdateTrafficControlTarget: add param RegionId.
- Update API UpdateTrafficControlTask: update param body.


2024-08-05 Version: 2.1.1
- Update API GetInstance: update response param.
- Update API ListInstances: update response param.
- Update API UpdateTrafficControlTaskTraffic: add param RegionId.


2024-07-23 Version: 2.1.0
- Support API ApplyEngineConfig.
- Support API CloneEngineConfig.
- Support API CreateEngineConfig.
- Support API DeleteEngineConfig.
- Support API GetEngineConfig.
- Support API ListEngineConfigs.
- Support API UpdateEngineConfig.


2024-07-17 Version: 2.0.1
- Update API GetTrafficControlTarget: update response param.
- Update API GetTrafficControlTask: update response param.
- Update API SplitTrafficControlTarget: update param body.


2024-06-25 Version: 2.0.0
- Update API GetTrafficControlTaskTraffic: update response param.
- Update API ListExperimentGroups: add param TimeRangeEnd.
- Update API ListExperimentGroups: add param TimeRangeStart.


2024-06-07 Version: 1.5.0
- Support API CloneTrafficControlTask.
- Support API CreateTrafficControlTarget.
- Support API CreateTrafficControlTask.
- Support API DeleteTrafficControlTarget.
- Support API DeleteTrafficControlTask.
- Support API GenerateTrafficControlTaskCode.
- Support API GenerateTrafficControlTaskConfig.
- Support API GetTrafficControlTarget.
- Support API GetTrafficControlTask.
- Support API GetTrafficControlTaskTraffic.
- Support API ListTrafficControlTargetTrafficHistory.
- Support API ListTrafficControlTasks.
- Support API ReleaseTrafficControlTask.
- Support API SplitTrafficControlTarget.
- Support API StartTrafficControlTarget.
- Support API StartTrafficControlTask.
- Support API StopTrafficControlTarget.
- Support API StopTrafficControlTask.
- Support API UpdateTrafficControlTarget.
- Support API UpdateTrafficControlTask.
- Support API UpdateTrafficControlTaskTraffic.


2024-05-07 Version: 1.4.0
- Support API CreateResourceRule.
- Support API CreateResourceRuleItem.
- Support API DebugResourceRule.
- Support API DeleteResourceRule.
- Support API DeleteResourceRuleItem.
- Support API GetResourceRule.
- Support API ListResourceRules.
- Support API PushResourceRule.
- Support API UpdateResourceRule.
- Support API UpdateResourceRuleItem.


2024-04-28 Version: 1.3.3
- Generated python 2022-12-13 for PaiRecService.

2024-03-22 Version: 1.3.2
- Generated python 2022-12-13 for PaiRecService.

2024-03-20 Version: 1.3.1
- Update API CreateExperimentGroup: add param RegionId.
- Update API CreateExperimentGroup: update param body.
- Update API GetExperimentGroup: add param RegionId.
- Update API GetExperimentGroup: update response param.
- Update API GetLayer: add param RegionId.
- Update API GetLayer: update response param.
- Update API ListExperimentGroups: add param RegionId.
- Update API ListExperimentGroups: update response param.
- Update API ListLayers: add param RegionId.
- Update API ListLayers: update response param.
- Update API UpdateExperimentGroup: add param RegionId.
- Update API UpdateExperimentGroup: update param body.


2024-03-19 Version: 1.3.0
- Support API UploadRecommendationData.


2024-03-19 Version: 1.2.2
- Update API CheckInstanceResources: update param InstanceId.
- Update API CheckInstanceResources: update param body.
- Update API CreateABMetric: update param body.
- Update API CreateABMetricGroup: update param body.
- Update API CreateCalculationJobs: update param body.
- Update API CreateFeatureConsistencyCheckJob: update param body.
- Update API CreateFeatureConsistencyCheckJobConfig: update param body.
- Update API CreateInstanceResource: add param RegionId.
- Update API CreateInstanceResource: update param InstanceId.
- Update API CreateInstanceResource: update param body.
- Update API CreateTableMeta: update param body.
- Update API DeleteABMetric: update param ABMetricId.
- Update API DeleteABMetricGroup: update param ABMetricGroupId.
- Update API DeleteABMetricGroup: update param InstanceId.
- Update API DeleteInstanceResource: add param RegionId.
- Update API DeleteInstanceResource: update param InstanceId.
- Update API DeleteInstanceResource: update param ResourceId.
- Update API DeleteTableMeta: update param TableMetaId.
- Update API GetABMetric: update param ABMetricId.
- Update API GetABMetricGroup: update param ABMetricGroupId.
- Update API GetABMetricGroup: update param InstanceId.
- Update API GetCalculationJob: update param CalculationJobId.
- Update API GetCalculationJob: update param InstanceId.
- Update API GetFeatureConsistencyCheckJobConfig: update response param.
- Update API GetInstanceResource: add param RegionId.
- Update API GetInstanceResource: update param InstanceId.
- Update API GetInstanceResource: update param ResourceId.
- Update API GetInstanceResourceTable: add param RegionId.
- Update API GetInstanceResourceTable: update param InstanceId.
- Update API GetInstanceResourceTable: update param ResourceId.
- Update API GetInstanceResourceTable: update param TableName.
- Update API GetInstanceResourceTable: update response param.
- Update API GetTableMeta: update param TableMetaId.
- Update API GetTableMeta: update param InstanceId.
- Update API GetTableMeta: update response param.
- Update API ListABMetricGroups: add param Order.
- Update API ListABMetricGroups: add param SortBy.
- Update API ListABMetricGroups: update param InstanceId.
- Update API ListCalculationJobs: update param SceneId.
- Update API ListFeatureConsistencyCheckJobConfigs: update response param.
- Update API ListInstanceResources: add param RegionId.
- Update API ListInstanceResources: update param InstanceId.
- Update API ListTableMetas: update param Module.
- Update API ListTableMetas: update response param.
- Update API UpdateABMetric: update param ABMetricId.
- Update API UpdateABMetric: update param body.
- Update API UpdateABMetricGroup: update param ABMetricGroupId.
- Update API UpdateABMetricGroup: update param body.
- Update API UpdateFeatureConsistencyCheckJobConfig: update param body.
- Update API UpdateInstanceResource: add param RegionId.
- Update API UpdateInstanceResource: update param InstanceId.
- Update API UpdateInstanceResource: update param ResourceId.
- Update API UpdateTableMeta: update param TableMetaId.
- Update API UpdateTableMeta: update param body.


2024-02-22 Version: 1.2.1
- Update API CheckInstanceResources: update param InstanceId.
- Update API CheckInstanceResources: update param body.
- Update API CreateABMetric: update param body.
- Update API CreateABMetricGroup: update param body.
- Update API CreateCalculationJobs: update param body.
- Update API CreateFeatureConsistencyCheckJob: update param body.
- Update API CreateFeatureConsistencyCheckJobConfig: update param body.
- Update API CreateInstanceResource: add param RegionId.
- Update API CreateInstanceResource: update param InstanceId.
- Update API CreateInstanceResource: update param body.
- Update API CreateTableMeta: update param body.
- Update API DeleteABMetric: update param ABMetricId.
- Update API DeleteABMetricGroup: update param ABMetricGroupId.
- Update API DeleteABMetricGroup: update param InstanceId.
- Update API DeleteInstanceResource: add param RegionId.
- Update API DeleteInstanceResource: update param InstanceId.
- Update API DeleteInstanceResource: update param ResourceId.
- Update API DeleteTableMeta: update param TableMetaId.
- Update API GetABMetric: update param ABMetricId.
- Update API GetABMetricGroup: update param ABMetricGroupId.
- Update API GetABMetricGroup: update param InstanceId.
- Update API GetCalculationJob: update param CalculationJobId.
- Update API GetCalculationJob: update param InstanceId.
- Update API GetFeatureConsistencyCheckJobConfig: update response param.
- Update API GetInstanceResource: add param RegionId.
- Update API GetInstanceResource: update param InstanceId.
- Update API GetInstanceResource: update param ResourceId.
- Update API GetInstanceResourceTable: add param RegionId.
- Update API GetInstanceResourceTable: update param InstanceId.
- Update API GetInstanceResourceTable: update param ResourceId.
- Update API GetInstanceResourceTable: update param TableName.
- Update API GetInstanceResourceTable: update response param.
- Update API GetTableMeta: update param TableMetaId.
- Update API GetTableMeta: update param InstanceId.
- Update API GetTableMeta: update response param.
- Update API ListABMetricGroups: add param Order.
- Update API ListABMetricGroups: add param SortBy.
- Update API ListABMetricGroups: update param InstanceId.
- Update API ListCalculationJobs: update param SceneId.
- Update API ListFeatureConsistencyCheckJobConfigs: update response param.
- Update API ListInstanceResources: add param RegionId.
- Update API ListInstanceResources: update param InstanceId.
- Update API ListTableMetas: update param Module.
- Update API ListTableMetas: update response param.
- Update API UpdateABMetric: update param ABMetricId.
- Update API UpdateABMetric: update param body.
- Update API UpdateABMetricGroup: update param ABMetricGroupId.
- Update API UpdateABMetricGroup: update param body.
- Update API UpdateFeatureConsistencyCheckJobConfig: update param body.
- Update API UpdateInstanceResource: add param RegionId.
- Update API UpdateInstanceResource: update param InstanceId.
- Update API UpdateInstanceResource: update param ResourceId.
- Update API UpdateTableMeta: update param TableMetaId.
- Update API UpdateTableMeta: update param body.


2023-12-22 Version: 1.2.0
- Generated python 2022-12-13 for PaiRecService.

2023-12-21 Version: 1.1.0
- Generated python 2022-12-13 for PaiRecService.

2023-09-14 Version: 1.0.0
- Generated python 2022-12-13 for PaiRecService.

