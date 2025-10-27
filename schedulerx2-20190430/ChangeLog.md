2025-10-27 Version: 2.1.2
- Update API CreateAppGroup: add request parameters NotificationPolicyName.
- Update API GetAppGroup: add response parameters Body.Data.NotificationPolicyName.
- Update API UpdateAppGroup: add request parameters NotificationPolicyName.


2025-06-10 Version: 2.2.0
- Support API ReadSchedulerxDesignateInfo.


2025-05-13 Version: 2.1.0
- Support API DeleteNamespace.
- Support API ListJobScriptHistory.
- Support API ReadSchedulerxDesignateDetail.
- Support API UpdateJobScript.
- Support API UpdateNamespace.
- Update API CreateJob: add request parameters Priority.
- Update API GetAppGroup: add response parameters Body.Data.MonitorContactsJson.
- Update API GetAppGroup: add response parameters Body.Data.Namespace.
- Update API GetWorkFlow: add response parameters Body.Data.WorkFlowInfo.GroupId.
- Update API GetWorkFlow: add response parameters Body.Data.WorkFlowInfo.MaxConcurrency.
- Update API GetWorkFlow: add response parameters Body.Data.WorkFlowInfo.Namespace.
- Update API ListGroups: add response parameters Body.Data.AppGroups.$.Namespace.
- Update API UpdateAppGroup: add request parameters MonitorConfigJson.
- Update API UpdateAppGroup: add request parameters MonitorContactsJson.
- Update API UpdateJob: add request parameters Priority.


2024-10-21 Version: 2.0.3
- Update API BatchDeleteJobs: update response param.
- Update API BatchDeleteRouteStrategy: update response param.
- Update API BatchDisableJobs: update response param.
- Update API BatchEnableJobs: update response param.
- Update API CreateAppGroup: update response param.
- Update API CreateJob: update response param.
- Update API CreateNamespace: update response param.
- Update API CreateRouteStrategy: update response param.
- Update API CreateWorkflow: update response param.
- Update API DeleteAppGroup: update response param.
- Update API DeleteJob: update response param.
- Update API DeleteRouteStrategy: update response param.
- Update API DeleteWorkflow: update response param.
- Update API DesignateWorkers: update response param.
- Update API DisableJob: update response param.
- Update API DisableWorkflow: update response param.
- Update API EnableJob: update response param.
- Update API EnableWorkflow: update response param.
- Update API ExecuteJob: update response param.
- Update API ExecuteWorkflow: update response param.
- Update API GetAppGroup: update response param.
- Update API GetJobInfo: update response param.
- Update API GetJobInstance: update response param.
- Update API GetJobInstanceList: update response param.
- Update API GetLog: update response param.
- Update API GetOverview: update response param.
- Update API GetWorkFlow: update response param.
- Update API GetWorkerList: update response param.
- Update API GetWorkflowInstance: update response param.
- Update API GrantPermission: update response param.
- Update API ListGroups: update response param.
- Update API ListJobs: update response param.
- Update API ListNamespaces: update response param.
- Update API ListWorkflowInstance: update response param.
- Update API RerunJob: update response param.
- Update API RetryJobInstance: update response param.
- Update API RevokePermission: update response param.
- Update API SetJobInstanceSuccess: update response param.
- Update API SetWfInstanceSuccess: update response param.
- Update API StopInstance: update response param.
- Update API UpdateAppGroup: update response param.
- Update API UpdateJob: update response param.
- Update API UpdateWorkflow: update response param.
- Update API UpdateWorkflowDag: update response param.


2024-10-18 Version: 2.0.2
- Update API ExecuteWorkflow: update response param.
- Update API GetAppGroup: update response param.
- Update API GetJobInfo: update response param.
- Update API GetJobInstance: update response param.
- Update API GetJobInstanceList: update response param.
- Update API GetLog: update response param.
- Update API GetOverview: update response param.
- Update API GetWorkFlow: update response param.
- Update API GetWorkerList: update response param.
- Update API GetWorkflowInstance: update response param.
- Update API GrantPermission: update response param.
- Update API ListGroups: update response param.
- Update API ListJobs: update response param.
- Update API ListNamespaces: update response param.
- Update API ListWorkflowInstance: update response param.
- Update API RetryJobInstance: update response param.
- Update API RevokePermission: update response param.
- Update API SetJobInstanceSuccess: update response param.
- Update API SetWfInstanceSuccess: update response param.
- Update API UpdateAppGroup: update response param.
- Update API UpdateJob: update response param.
- Update API UpdateWorkflow: update response param.
- Update API UpdateWorkflowDag: update response param.


2024-10-16 Version: 2.0.1
- Update API GrantPermission: update response param.


2024-06-26 Version: 2.0.0
- Update API CreateAppGroup: add param AppVersion.
- Update API CreateAppGroup: delete param Version.
- Update API CreateWorkflow: update param TimeType.
- Update API DescribeRegions: update param RegionId.
- Update API GetAppGroup: update response param.
- Update API ListGroups: update response param.
- Update API UpdateAppGroup: add param AppVersion.
- Update API UpdateAppGroup: delete param Version.


2024-05-30 Version: 1.1.15
- Generated python 2019-04-30 for schedulerx2.

2024-05-29 Version: 1.1.14
- Update API CreateAppGroup: add param Version.
- Update API ListGroups: update response param.
- Update API UpdateAppGroup: add param Version.


2024-05-29 Version: 1.1.14
- Update API CreateAppGroup: add param Version.
- Update API ListGroups: update response param.
- Update API UpdateAppGroup: add param Version.


2024-05-17 Version: 1.1.13
- Update API CreateWorkflow: update response param.
- Update API GetJobInstanceList: add param PageNum.
- Update API GetJobInstanceList: add param PageSize.
- Update API GetJobInstanceList: update param EndTimestamp.
- Update API GetJobInstanceList: update param JobId.
- Update API GetJobInstanceList: update param StartTimestamp.
- Update API GetJobInstanceList: update param Status.


2023-07-17 Version: 1.1.12
- Get Workflow Instance Add Node Field.

2023-07-17 Version: 1.1.11
- Get Job Instance API add Field.
- Get Workflow Instance Add Node Field.

2023-06-07 Version: 1.1.10
- Add Overview Query API.
- Support Update Job With XAttrs.

2023-02-27 Version: 1.1.9
- Create Job Support Timezone.
- Update Job Support Timezone.

2023-02-23 Version: 1.1.8
- Get Job Instance Add RegionId.

2023-02-21 Version: 1.1.7
- Update AppGroup Hide xattrs.
- Get AppGroup Hide xattrs.
- Create AppGroup HIde xattrs.
- Get AppGroup Hide appGroupId.

2023-02-16 Version: 1.1.6
- Support Create Workflow.
- Support Update Workflow DAG.
- Support Get Workflow Instance and DAG.
- Support Retry Job Instance.
- Support Get Log.
- Create Job Add FailTimes and SuccessNoticeEnable.

2022-11-02 Version: 1.1.5
- ListJobs return JobType and XAttrs.
- GetJobInfo return JobType and XAttrs.

2022-10-26 Version: 1.1.4
- Update Job Support Incremental Updating.

2022-09-27 Version: 1.1.3
- Create Job Support XAttrs.

2022-06-13 Version: 1.1.2
- Create Job Support Setting Status.

2022-04-06 Version: 1.1.1
- Create App Group Support Schedule Busy Workers.

2022-03-21 Version: 1.0.9
- Get Job Support Query By Job Name.
- Add Api Create Namespace.
- Create App Support Set User Defined App Key.

2022-01-25 Version: 1.0.8
- Supported Get Worker List.
- Execute Job Support Designate Machine.
- Job Interface Add Config.

