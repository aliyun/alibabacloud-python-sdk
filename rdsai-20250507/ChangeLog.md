2026-04-24 Version: 3.0.0
- Support API CreateApiKey.
- Support API DeleteApiKey.
- Support API DescribeMOTokenUsageDetail.
- Support API DescribeModelOperator.
- Support API DescribeMonitorData.
- Support API DescribeWhitelistIps.
- Support API EnableAgentRuntime.
- Support API GetModelOperatorOrder.
- Support API ListApiKeys.
- Support API ModifyWhitelistIps.
- Support API RenameApiKey.
- Support API ResetApiKey.
- Support API UpdateApiKeyQuota.
- Delete API CreateEdgeFunction.
- Delete API DeleteEdgeFunction.
- Delete API DescribeEdgeFunctions.
- Delete API UpdateEdgeFunction.
- Update API CreateScheduledTask: add request parameters InspectionItems.
- Update API GetScheduledReports: add response parameters Body.Reports.$.InspectionItems.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.InspectionItems.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.InspectionItems.
- Update API ModifyScheduledTask: add request parameters InspectionItems.


2026-04-10 Version: 2.5.0
- Support API DescribeSandboxTemplates.


2026-03-23 Version: 2.4.0
- Support API CreateEdgeFunction.
- Support API DeleteEdgeFunction.
- Support API DescribeEdgeFunctions.
- Support API UpdateEdgeFunction.
- Update API CreateInspectionTask: add request parameters RegionId.
- Update API CreateInspectionTask: add request parameters ReportType.
- Update API CreateScheduledTask: add request parameters RegionId.
- Update API CreateScheduledTask: add request parameters ReportType.
- Update API GetInspectionReport: add request parameters ReportType.
- Update API GetScheduledReports: add response parameters Body.Reports.$.RegionId.
- Update API GetScheduledReports: add response parameters Body.Reports.$.ReportType.
- Update API GetStandAloneReports: add request parameters ReportType.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.RegionId.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.ReportType.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.RegionId.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.ReportType.


2026-03-23 Version: 2.4.0
- Support API CreateEdgeFunction.
- Support API DeleteEdgeFunction.
- Support API DescribeEdgeFunctions.
- Support API UpdateEdgeFunction.
- Update API CreateInspectionTask: add request parameters RegionId.
- Update API CreateInspectionTask: add request parameters ReportType.
- Update API CreateScheduledTask: add request parameters RegionId.
- Update API CreateScheduledTask: add request parameters ReportType.
- Update API GetInspectionReport: add request parameters ReportType.
- Update API GetScheduledReports: add response parameters Body.Reports.$.RegionId.
- Update API GetScheduledReports: add response parameters Body.Reports.$.ReportType.
- Update API GetStandAloneReports: add request parameters ReportType.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.RegionId.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.ReportType.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.RegionId.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.ReportType.


2026-03-12 Version: 2.3.1
- Update API CreateInspectionTask: add request parameters ReportLanguage.
- Update API CreateScheduledTask: add request parameters ReportLanguage.
- Update API GetScheduledReports: add response parameters Body.Reports.$.ReportLanguage.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.ReportLanguage.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.ReportLanguage.
- Update API ModifyScheduledTask: add request parameters ReportLanguage.


2026-03-12 Version: 2.3.1
- Update API CreateInspectionTask: add request parameters ReportLanguage.
- Update API CreateScheduledTask: add request parameters ReportLanguage.
- Update API GetScheduledReports: add response parameters Body.Reports.$.ReportLanguage.
- Update API GetStandAloneReports: add response parameters Body.Reports.$.ReportLanguage.
- Update API ListScheduledTasks: add response parameters Body.Schedules.$.ReportLanguage.
- Update API ModifyScheduledTask: add request parameters ReportLanguage.


2026-02-27 Version: 2.3.0
- Support API CreateSkill.
- Support API DeleteSkill.
- Support API GetSkill.
- Support API ListSkill.
- Support API UpdateSkill.


2026-02-05 Version: 2.2.0
- Support API CreateInspectionTask.
- Support API CreateScheduledTask.
- Support API DeleteScheduledTask.
- Support API GetInspectionReport.
- Support API GetScheduledInstances.
- Support API GetScheduledReports.
- Support API GetStandAloneReports.
- Support API ListScheduledTasks.
- Support API ModifyScheduledTask.
- Update API DescribeAppInstanceAttribute: add response parameters Body.EipId.
- Update API DescribeAppInstanceAttribute: add response parameters Body.NatCreatedBy.
- Update API DescribeAppInstanceAttribute: add response parameters Body.NatGatewayId.


2026-02-02 Version: 2.1.1
- Update API CreateCustomAgent: add request parameters SkillIds.
- Update API CreateCustomAgent: add response parameters Body.Skills.
- Update API GetCustomAgent: add response parameters Body.Skills.
- Update API ListCustomAgent: add response parameters Body.Skills.
- Update API UpdateCustomAgent: add request parameters SkillIds.
- Update API UpdateCustomAgent: add response parameters Body.Skills.


2026-02-02 Version: 2.1.1
- Update API CreateCustomAgent: add request parameters SkillIds.
- Update API CreateCustomAgent: add response parameters Body.Skills.
- Update API GetCustomAgent: add response parameters Body.Skills.
- Update API ListCustomAgent: add response parameters Body.Skills.
- Update API UpdateCustomAgent: add request parameters SkillIds.
- Update API UpdateCustomAgent: add response parameters Body.Skills.


2026-01-25 Version: 2.1.0
- Support API ModifyInstancesSSL.
- Update API ChatMessages: add request parameters EventMode.
- Update API GetMessages: add request parameters EventMode.
- Update API GetMessages: add response parameters Body.Data.$.Events.


2026-01-12 Version: 2.0.4
- Update API DescribeInstanceIpWhitelist: add request parameters GroupName.


2025-12-23 Version: 2.0.3
- Update API DescribeEventsList: add response parameters Body.Events.$.RegionId.
- Update API DescribeInstanceEndpoints: add response parameters Body.DBInstanceEndpoints.


2025-12-23 Version: 2.0.3
- Update API DescribeEventsList: add response parameters Body.Events.$.RegionId.
- Update API DescribeInstanceEndpoints: add response parameters Body.DBInstanceEndpoints.


2025-12-19 Version: 2.0.2
- Update API CreateAppInstance: add request parameters InitializeWithExistingData.


2025-12-08 Version: 2.0.1
- Generated python 2025-05-07 for RdsAi.

2025-12-05 Version: 2.0.0
- Update API ChatMessages: delete request parameters ApiId.
- Update API ChatMessagesTaskStop: delete request parameters ApiId.
- Update API CreateCustomAgent: delete request parameters ApiId.
- Update API DeleteCustomAgent: delete request parameters ApiId.
- Update API GetConversations: delete request parameters ApiId.
- Update API GetCustomAgent: delete request parameters ApiId.
- Update API GetMessages: delete request parameters ApiId.
- Update API ListCustomAgent: delete request parameters ApiId.
- Update API ListCustomAgentTools: delete request parameters ApiId.
- Update API ModifyMessagesFeedbacks: delete request parameters ApiId.
- Update API UpdateCustomAgent: delete request parameters ApiId.


2025-12-03 Version: 1.5.0
- Support API ChatMessages.
- Support API ChatMessagesTaskStop.
- Support API CreateCustomAgent.
- Support API DeleteCustomAgent.
- Support API DescribeEventsList.
- Support API GetConversations.
- Support API GetCustomAgent.
- Support API GetMessages.
- Support API ListCustomAgent.
- Support API ListCustomAgentTools.
- Support API ModifyMessagesFeedbacks.
- Support API UpdateCustomAgent.


2025-11-25 Version: 1.4.1
- Update API CreateAppInstance: add request parameters PublicEndpointEnabled.
- Update API ResetInstancePassword: add request parameters DatabasePassword.


2025-11-18 Version: 1.4.0
- Support API ModifyInstanceConfig.
- Update API DescribeAppInstanceAttribute: add response parameters Body.EipStatus.
- Update API DescribeAppInstanceAttribute: add response parameters Body.NatStatus.


2025-09-25 Version: 1.3.0
- Support API DescribeInstanceRAGConfig.
- Support API DescribeInstanceSSL.
- Support API ModifyInstanceRAGConfig.
- Support API ModifyInstanceSSL.


2025-09-22 Version: 1.2.0
- Support API DescribeInstanceStorageConfig.
- Support API ModifyInstanceAuthConfig.
- Support API ModifyInstanceStorageConfig.
- Support API ResetInstancePassword.
- Support API RestartInstance.
- Support API StartInstance.
- Support API StopInstance.


2025-09-11 Version: 1.1.2
- Update API DescribeInstanceAuthInfo: add response parameters Body.ConfigList.
- Update API DescribeInstanceAuthInfo: add response parameters Body.InstanceName.


2025-09-10 Version: 1.1.1
- Update API CreateAppInstance: add request parameters DBInstanceConfig.
- Update API CreateAppInstance: add request parameters RAGEnabled.


2025-09-10 Version: 1.1.1
- Update API CreateAppInstance: add request parameters DBInstanceConfig.
- Update API CreateAppInstance: add request parameters RAGEnabled.


2025-08-28 Version: 1.1.0
- Support API DescribeInstanceAuthInfo.


2025-08-18 Version: 1.0.0
- Generated python 2025-05-07 for RdsAi.

