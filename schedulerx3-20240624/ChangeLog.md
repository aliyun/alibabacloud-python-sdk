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

