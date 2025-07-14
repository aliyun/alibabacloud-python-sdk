2025-07-14 Version: 1.2.2
- Update API CreateTaskExportTask: add request parameters CallingNumber.
- Update API SearchTask: add request parameters CallingNumber.
- Update API SearchTask: add response parameters Body.SearchTaskInfoList.$.CallingNumber.


2025-06-12 Version: 1.2.1
- Update API DescribeScript: add response parameters Body.Script.LabelConfig.
- Update API ModifyScript: add request parameters LabelConfig.


2025-04-25 Version: 1.2.0
- Support API CreateBeebotIntent.
- Support API CreateBeebotIntentLgf.
- Support API CreateBeebotIntentUserSay.
- Support API DeleteBeebotIntent.
- Support API DeleteBeebotIntentLgf.
- Support API DeleteBeebotIntentUserSay.
- Support API DescribeBeebotIntent.
- Support API ListBeebotIntent.
- Support API ListBeebotIntentLgf.
- Support API ListBeebotIntentUserSay.
- Support API ListIntentions.
- Support API ModifyBeebotIntent.
- Support API ModifyBeebotIntentLgf.
- Support API ModifyBeebotIntentUserSay.
- Update API CreateScript: add request parameters ScriptNluProfileJsonString.
- Update API DescribeScript: add response parameters Body.Script.NluEngine.
- Update API DescribeScript: add response parameters Body.Script.NluProfile.
- Update API ListScripts: add response parameters Body.Scripts.List.$.NluProfile.


2025-04-09 Version: 1.1.0
- Support API CreateAgentProfile.
- Support API CreateAnnotationMission.
- Support API DeleteAgentProfiles.
- Support API GetAgentProfile.
- Support API GetAgentProfileTemplate.
- Support API GetAnnotationMissionSummary.
- Support API GetAnnotationMissionTagInfoList.
- Support API GetJobDataUploadParams.
- Support API GetRealtimeConcurrencyReport.
- Support API ListAgentProfiles.
- Support API ListAnnotationMission.
- Support API ListAnnotationMissionSession.
- Support API ListApiPlugins.
- Support API ListFlashSmsTemplates.
- Support API ModifyAgentProfile.
- Support API ModifyAnnotationMission.
- Support API SaveAnnotationMissionSessionList.
- Support API SaveAnnotationMissionTagInfoList.
- Update API CreateBatchRepeatJob: add request parameters FlashSmsExtras.
- Update API CreateBatchRepeatJob: add request parameters RecallCallingNumber.
- Update API CreateJobGroup: add request parameters FlashSmsExtras.
- Update API CreateJobGroup: add request parameters RecallCallingNumber.
- Update API CreateJobGroup: add response parameters Body.JobGroup.RecallCallingNumbers.
- Update API CreateScript: add request parameters AgentId.
- Update API CreateScript: add request parameters AgentKey.
- Update API CreateScript: add request parameters AgentLlm.
- Update API CreateScript: add request parameters NluAccessType.
- Update API CreateScript: add request parameters NluEngine.
- Update API CreateScript: add response parameters Body.Script.NluAccessType.
- Update API CreateScript: add response parameters Body.Script.NluEngine.
- Update API DescribeDialogueNodeStatistics: add response parameters Body.HangUpDialogueNodes.
- Update API DescribeGroupExecutingInfo: add response parameters Body.ExecutingInfo.NoInteractionNum.
- Update API DescribeIntentStatistics: add response parameters Body.IntentsAfterNoAnswer.$.GroupId.
- Update API DescribeIntentStatistics: add response parameters Body.IntentsAfterNoAnswer.$.HitAfterNoAnswer.
- Update API DescribeIntentStatistics: add response parameters Body.IntentsAfterNoAnswer.$.IntentId.
- Update API DescribeIntentStatistics: add response parameters Body.IntentsAfterNoAnswer.$.IntentName.
- Update API DescribeIntentStatistics: add response parameters Body.ProcessIntents.$.RateDisplay.
- Update API DescribeJob: add response parameters Body.Job.Tasks.$.RealRingingDuration.
- Update API DescribeJob: add response parameters Body.Job.Tasks.$.SipCode.
- Update API DescribeJob: add response parameters Body.Job.Tasks.$.SipDuration.
- Update API DescribeJobGroup: add response parameters Body.JobGroup.FlashSmsExtras.
- Update API DescribeJobGroup: add response parameters Body.JobGroup.RecallCallingNumbers.
- Update API DescribeJobGroup: add response parameters Body.JobGroup.Strategy.Repeatable.
- Update API DescribeScript: add response parameters Body.Script.AgentId.
- Update API DescribeScript: add response parameters Body.Script.AgentKey.
- Update API DescribeScript: add response parameters Body.Script.AgentLlm.
- Update API DescribeScript: add response parameters Body.Script.ChatConfig.
- Update API DescribeTTSDemo: add request parameters AccessKey.
- Update API DescribeTTSDemo: add request parameters AliCustomizedVoice.
- Update API DescribeTTSDemo: add request parameters AppKey.
- Update API DescribeTTSDemo: add request parameters Engine.
- Update API DescribeTTSDemo: add request parameters NlsServiceType.
- Update API DescribeTTSDemo: add request parameters SecretKey.
- Update API GetBaseStrategyPeriod: add response parameters Body.OnlyWorkdays.
- Update API GetTaskByUuid: add response parameters Body.Code.
- Update API GetTaskByUuid: add response parameters Body.HttpStatusCode.
- Update API GetTaskByUuid: add response parameters Body.Message.
- Update API GetTaskByUuid: add response parameters Body.Success.
- Update API GetTaskByUuid: add response parameters Body.Task.Conversations.
- Update API ImportScript: add request parameters NluEngine.
- Update API ListChatbotInstances: add request parameters AgentKey.
- Update API ListDownloadTasks: add request parameters InstanceId.
- Update API ListInstances: add request parameters Name.
- Update API ListInstances: add request parameters PageNumber.
- Update API ListInstances: add request parameters PageSize.
- Update API ListInstances: add response parameters Body.PageNumber.
- Update API ListInstances: add response parameters Body.PageSize.
- Update API ListInstances: add response parameters Body.TotalCount.
- Update API ListJobGroups: add request parameters OnlyMinConcurrencyEnabled.
- Update API ListJobGroups: add response parameters Body.JobGroups.List.$.MinConcurrency.
- Update API ListJobGroupsAsync: add response parameters Body.JobGroups.$.MinConcurrency.
- Update API ListScriptRecording: add request parameters RefIdsJson.
- Update API ListScriptRecording: add response parameters Body.ScriptRecordings.$.RefId.
- Update API ListScripts: add request parameters NluEngine.
- Update API ListScripts: add request parameters ScriptName.
- Update API ListScripts: add response parameters Body.Scripts.List.$.AgentKey.
- Update API ListScripts: add response parameters Body.Scripts.List.$.AgentLlm.
- Update API ListScripts: add response parameters Body.Scripts.List.$.CreateTime.
- Update API ListScripts: add response parameters Body.Scripts.List.$.NluAccessType.
- Update API ListScripts: add response parameters Body.Scripts.List.$.NluEngine.
- Update API ListScripts: add response parameters Body.Scripts.List.$.agentId.
- Update API ModifyJobGroup: add request parameters FlashSmsExtras.
- Update API ModifyJobGroup: add request parameters RecallCallingNumber.
- Update API ModifyJobGroup: add response parameters Body.JobGroup.FlashSmsExtras.
- Update API ModifyScript: add request parameters AgentId.
- Update API ModifyScript: add request parameters AgentKey.
- Update API ModifyScript: add request parameters AgentLlm.
- Update API ModifyScript: add request parameters ChatConfig.
- Update API ModifyScript: add request parameters NluAccessType.
- Update API ModifyScript: add request parameters NluEngine.
- Update API ModifyTTSConfig: add request parameters PitchRate.
- Update API ModifyTTSConfig: add response parameters Body.TTSConfig.PitchRate.
- Update API QueryJobs: add response parameters Body.Jobs.List.$.TagHits.
- Update API QueryJobsWithResult: add request parameters EndActualTimeFilter.
- Update API QueryJobsWithResult: add request parameters JobFailureReasonsFilter.
- Update API QueryJobsWithResult: add request parameters StartActualTimeFilter.
- Update API SaveBaseStrategyPeriod: add request parameters OnlyWorkdays.
- Update API SubmitScriptReview: add request parameters From.


2023-01-31 Version: 1.0.1
- Supported new features for outbound.

2021-03-30 Version: 1.0.0
- Generated python 2019-12-26 for OutboundBot.

