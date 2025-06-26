2025-06-26 Version: 1.11.0
- Support API ListKyuubiServices.
- Support API ListKyuubiToken.
- Update API GetSessionCluster: add response parameters Body.sessionCluster.connectionToken.
- Update API ListJobRuns: add request parameters isWorkflow.
- Update API ListKyuubiSparkApplications: add request parameters minDuration.
- Update API ListKyuubiSparkApplications: add request parameters orderBy.
- Update API ListKyuubiSparkApplications: add request parameters resourceQueueId.
- Update API ListKyuubiSparkApplications: add request parameters sort.


2025-05-30 Version: 1.10.3
- Generated python 2023-08-08 for emr-serverless-spark.

2025-05-19 Version: 1.10.2
- Update API CreateSessionCluster: add request parameters body.publicEndpointEnabled.
- Update API GetSessionCluster: add response parameters Body.sessionCluster.publicEndpointEnabled.
- Update API GetTemplate: add request parameters templateBizId.
- Update API ListSessionClusters: add response parameters Body.sessionClusters.$.publicEndpointEnabled.
- Update API ListWorkspaces: add response parameters Body.workspaces.$.prePaidQuota.orderId.


2025-05-16 Version: 1.10.1
- Generated python 2023-08-08 for emr-serverless-spark.

2025-05-06 Version: 1.10.0
- Support API CreateSessionCluster.
- Support API CreateWorkspace.
- Support API EditWorkspaceQueue.
- Support API GetCuHours.
- Support API GetDoctorApplication.
- Support API ListKyuubiSparkApplications.
- Update API CreateProcessDefinitionWithSchedule: add request parameters globalParams.
- Update API CreateProcessDefinitionWithSchedule: add request parameters taskDefinitionJson.$.taskParams.localParams.
- Update API GetSessionCluster: add response parameters Body.sessionCluster.extra.
- Update API GetSqlStatement: add response parameters Body.data.sqlOutputs.$.rowsFilePath.
- Update API ListJobRuns: add request parameters minDuration.
- Update API ListReleaseVersions: add request parameters serviceFilter.
- Update API ListSessionClusters: add response parameters Body.sessionClusters.$.extra.
- Update API ListWorkspaceQueues: add response parameters Body.queues.$.createTime.
- Update API ListWorkspaceQueues: add response parameters Body.queues.$.paymentType.
- Update API ListWorkspaces: add request parameters tag.
- Update API ListWorkspaces: add response parameters Body.workspaces.$.prePaidQuota.
- Update API ListWorkspaces: add response parameters Body.workspaces.$.tags.
- Update API StartProcessInstance: add request parameters action.
- Update API StartProcessInstance: add request parameters comments.
- Update API StartProcessInstance: add request parameters email.
- Update API StartProcessInstance: add request parameters interval.
- Update API UpdateProcessDefinitionWithSchedule: add request parameters globalParams.
- Update API UpdateProcessDefinitionWithSchedule: add request parameters taskDefinitionJson.$.taskParams.localParams.


2024-12-24 Version: 1.9.0
- Support API CreateProcessDefinitionWithSchedule.
- Support API StartProcessInstance.
- Support API UpdateProcessDefinitionWithSchedule.


2024-12-10 Version: 1.8.1
- Update API ListJobRuns: update response param.


2024-11-27 Version: 1.8.0
- Support API GetTemplate.


2024-11-25 Version: 1.7.0
- Support API GetSessionCluster.
- Update API GetJobRun: update response param.
- Update API ListSessionClusters: update response param.


2024-11-06 Version: 1.6.0
- Support API ListLogContents.


2024-10-17 Version: 1.5.0
- Support API StartSessionCluster.
- Support API StopSessionCluster.
- Update API ListJobRuns: update param workspaceId.
- Update API ListJobRuns: update param creator.
- Update API ListJobRuns: update param endTime.
- Update API ListJobRuns: update param jobRunDeploymentId.
- Update API ListJobRuns: update param jobRunId.
- Update API ListJobRuns: update param maxResults.
- Update API ListJobRuns: update param name.
- Update API ListJobRuns: update param nextToken.
- Update API ListJobRuns: update param resourceQueueId.
- Update API ListJobRuns: update param startTime.
- Update API ListJobRuns: update param states.
- Update API ListJobRuns: update param tags.
- Update API ListReleaseVersions: add param workspaceId.


2024-08-22 Version: 1.4.3
- Update API GetJobRun: update response param.


2024-08-20 Version: 1.4.2
- Update API ListJobRuns: update response param.
- Update API ListReleaseVersions: update response param.
- Update API ListSessionClusters: update response param.
- Update API ListWorkspaces: update response param.
- Update API StartJobRun: update param body.


2024-07-09 Version: 1.4.1
- Update API ListSessionClusters: add param kind.
- Update API ListSessionClusters: update response param.


2024-05-31 Version: 1.4.0
- Support API CreateSqlStatement.
- Support API GetSqlStatement.
- Support API TerminateSqlStatement.
- Update API ListJobRuns: add param jobRunDeploymentId.


2024-05-22 Version: 1.3.0
- Support API AddMembers.
- Support API GrantRoleToUsers.


2024-05-21 Version: 1.2.0
- Support API ListSessionClusters.


2024-05-21 Version: 1.2.0
- Support API ListSessionClusters.


2024-05-20 Version: 1.1.0
- Support API ListReleaseVersions.
- Support API ListWorkspaceQueues.
- Support API ListWorkspaces.


2024-05-17 Version: 1.0.1
- Update API CancelJobRun: update param workspaceId.
- Update API CancelJobRun: update param jobRunId.
- Update API GetJobRun: update param workspaceId.
- Update API GetJobRun: update param jobRunId.
- Update API ListJobRuns: update param workspaceId.
- Update API StartJobRun: update param workspaceId.


2024-04-16 Version: 1.0.0
- Generated python 2023-08-08 for emr-serverless-spark.

