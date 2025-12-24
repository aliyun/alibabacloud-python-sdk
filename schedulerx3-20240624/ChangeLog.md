2025-12-24 Version: 1.4.0
- Support API CreateExecutors.
- Support API GetExecutorConfig.
- Support API ListK8sResource.
- Support API SyncJobs.
- Support API UpdateExecutors.
- Update API CreateJob: add request parameters Coordinate.
- Update API CreateJob: add request parameters DependentStrategy.
- Update API CreateJob: add request parameters StartTimeType.
- Update API CreateJob: add request parameters NoticeConfig.EndEarly.
- Update API CreateJob: add request parameters NoticeConfig.EndEarlyEnable.
- Update API GetCluster: add response parameters Body.Data.MaxWorkflowNum.
- Update API GetCluster: add response parameters Body.Data.WorkflowNum.
- Update API GetLogEvent: add request parameters EventType.
- Update API GetLogEvent: add request parameters WorkflowExecutionId.
- Update API GetLogEvent: add request parameters WorkflowName.
- Update API GetLogEvent: add response parameters Body.Data.Records.$.EventType.
- Update API GetLogEvent: add response parameters Body.Data.Records.$.WorkflowExecutionId.
- Update API GetLogEvent: add response parameters Body.Data.Records.$.WorkflowName.
- Update API ListJobExecutions: add request parameters WorkflowExecutionId.
- Update API ListJobExecutions: add response parameters Body.Data.Records.$.WorkflowExecutionId.
- Update API ListJobExecutions: add response parameters Body.Data.Records.$.WorkflowId.
- Update API ListJobExecutions: add response parameters Body.Data.Records.$.WorkflowName.
- Update API ListJobs: add request parameters WorkflowId.
- Update API ListJobs: add response parameters Body.Data.Records.$.DependentStrategy.
- Update API ListJobs: add response parameters Body.Data.Records.$.NodeType.
- Update API ListJobs: add response parameters Body.Data.Records.$.StartTimeType.
- Update API ListJobs: add response parameters Body.Data.Records.$.WorkflowId.
- Update API ListScheduleEvent: add request parameters WorkflowExecutionId.
- Update API ListScheduleEvent: add request parameters WorkflowName.
- Update API ListScheduleEvent: add response parameters Body.Data.Records.$.EventType.
- Update API ListScheduleEvent: add response parameters Body.Data.Records.$.WorkflowExecutionId.
- Update API ListScheduleEvent: add response parameters Body.Data.Records.$.WorkflowName.
- Update API OperateRetryJobExecution: add request parameters TriggerChild.
- Update API UpdateJob: add request parameters DependentStrategy.
- Update API UpdateJob: add request parameters StartTimeType.
- Update API UpdateJob: add request parameters NoticeConfig.EndEarly.
- Update API UpdateJob: add request parameters NoticeConfig.EndEarlyEnable.


2025-10-17 Version: 1.3.3
- Update API GetLog: add request parameters ScheduleTime.
- Update API GetLog: add request parameters WorkerAddr.


2025-09-24 Version: 1.3.2
- Update API CreateCluster: add request parameters ChargeType.
- Update API CreateCluster: add request parameters Duration.
- Update API CreateCluster: add request parameters PricingCycle.
- Update API GetJobExecutionProgress: add response parameters Body.Data.EndTime.
- Update API GetJobExecutionProgress: add response parameters Body.Data.StartTime.
- Update API ListAppNames: add response parameters Body.Data.$.AppType.
- Update API ListAppNames: add response parameters Body.Data.$.WorkerRegistry.
- Update API ListApps: add response parameters Body.Data.Records.$.WorkerRegistry.


2025-08-22 Version: 1.3.1
- Update API CreateApp: add request parameters AppType.
- Update API CreateJob: add request parameters Weight.
- Update API GetApp: add response parameters Body.Data.AppType.
- Update API ListApps: add response parameters Body.Data.Records.$.AppType.
- Update API ListExecutors: add response parameters Body.Data.$.Weight.
- Update API ListJobs: add response parameters Body.Data.Records.$.Weight.
- Update API UpdateJob: add request parameters Weight.


2025-07-11 Version: 1.3.0
- Support API GetApp.
- Support API ListJobScriptHistory.
- Support API UpdateJobScript.
- Update API CreateApp: add request parameters LabelRouteStrategy.
- Update API ListApps: add response parameters Body.Data.Records.$.LabelRouteStrategy.
- Update API UpdateApp: add request parameters LabelRouteStrategy.


2025-07-04 Version: 1.2.0
- Support API GetJobExecutionThreadDump.
- Support API GetLogEvent.
- Update API CreateCluster: add request parameters Tag.
- Update API GetCluster: add response parameters Body.Data.Tags.
- Update API ListClusters: add request parameters Tag.
- Update API ListClusters: add response parameters Body.Data.Records.$.Tags.


2025-06-04 Version: 1.1.0
- Support API GetJobExecution.
- Update API CreateJob: add request parameters Script.
- Update API ListJobs: add response parameters Body.Data.Records.$.Script.
- Update API UpdateJob: add request parameters Script.


2025-05-20 Version: 1.0.4
- Update API ListJobExecutions: add response parameters Body.Data.Records.$.TotalTokens.
- Update API ListScheduleEvent: add request parameters EventType.


2025-05-20 Version: 1.0.4
- Update API ListJobExecutions: add response parameters Body.Data.Records.$.TotalTokens.
- Update API ListScheduleEvent: add request parameters EventType.


2025-04-29 Version: 1.0.3
- Update API GetCluster: add response parameters Body.Data.VersionLifecycle.
- Update API ListClusters: add response parameters Body.Data.Records.$.VersionLifecycle.


2025-03-25 Version: 1.0.2
- Update API CreateJob: add param ChildJobId.
- Update API CreateJob: update param NoticeContacts.
- Update API ListJobs: update response param.
- Update API UpdateJob: add param ChildJobId.
- Update API UpdateJob: update param NoticeContacts.


2024-12-27 Version: 1.0.1
- Update API CreateJob: add param ExecutorBlockStrategy.
- Update API CreateJob: update param TimeType.
- Update API ListJobs: update response param.
- Update API OperateRetryJobExecution: add param TaskList.
- Update API OperateRetryJobExecution: delete param JobId.
- Update API OperateRetryJobExecution: update param JobExecutionId.
- Update API OperateStopJobExecution: add param TaskList.
- Update API OperateStopJobExecution: delete param JobId.
- Update API OperateStopJobExecution: update param JobExecutionId.
- Update API UpdateJob: add param ExecutorBlockStrategy.
- Update API UpdateJob: update param AttemptInterval.
- Update API UpdateJob: update param MaxAttempt.
- Update API UpdateJob: update param MaxConcurrency.
- Update API UpdateJob: update param NoticeConfig.
- Update API UpdateJob: update param TimeType.


2024-11-27 Version: 1.0.0
- Generated python 2024-06-24 for SchedulerX3.

