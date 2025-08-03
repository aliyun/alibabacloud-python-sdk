2025-08-03 Version: 1.11.2
- Update API GetAbnormalEventsCount: add request parameters level.
- Update API GetAbnormalEventsCount: add response parameters Body.data.$.eventList.
- Update API ListAbnormalyEvents: add request parameters event.


2025-08-01 Version: 1.11.1
- Update API InitialSysom: add request parameters body.source.


2025-07-08 Version: 1.11.0
- Support API StartAIDiffAnalysis.
- Update API StartAIAnalysis: add request parameters body.analysis_params.
- Update API StartAIAnalysis: add request parameters body.created_by.
- Update API StartAIAnalysis: add request parameters body.instance_type.
- Update API StartAIAnalysis: add request parameters body.iteration_func.
- Update API StartAIAnalysis: add request parameters body.iteration_mod.
- Update API StartAIAnalysis: add request parameters body.iteration_range.
- Update API StartAIAnalysis: add request parameters body.uid.


2025-06-30 Version: 1.10.1
- Update API InstallAgentForCluster: add request parameters body.config_id.
- Update API ListAgentInstallRecords: add request parameters region.
- Update API ListClusterAgentInstallRecords: add request parameters agent_config_id.
- Update API ListClusterAgentInstallRecords: add response parameters Body.data.$.agent_config_id.
- Update API ListClusterAgentInstallRecords: add response parameters Body.data.$.agent_config_name.


2025-05-12 Version: 1.10.0
- Support API CheckInstanceSupport.
- Update API ListAbnormalyEvents: add response parameters Body.total.
- Update API ListAbnormalyEvents: add response parameters Body.data.$.diag_status.
- Update API ListAbnormalyEvents: add response parameters Body.data.$.end_at.
- Update API ListAbnormalyEvents: add response parameters Body.data.$.level.
- Update API ListAbnormalyEvents: add response parameters Body.data.$.namespace.
- Update API ListAbnormalyEvents: add response parameters Body.data.$.pod.
- Update API ListAbnormalyEvents: add response parameters Body.data.$.uuid.
- Update API ListInstancesWithEcsInfo: add response parameters Body.data.$.kernel_version.
- Update API UpdateFuncSwitchRecord: add request parameters params.region.
- Update API UpdateFuncSwitchRecord: add request parameters params.args.duration.
- Update API UpdateFuncSwitchRecord: add request parameters params.args.pid.


2025-02-26 Version: 1.9.1
- Update API StartAIAnalysis: update param body.


2025-02-17 Version: 1.9.0
- Support API GenerateCopilotStreamResponse.
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetCopilotHistory.
- Support API GetHostCount.
- Support API GetHotSpotUniqList.
- Support API GetHotspotAnalysis.
- Support API GetHotspotCompare.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetHotspotTracking.
- Support API GetInstantScore.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API GetServiceFuncStatus.
- Support API InitialSysom.
- Support API InstallAgent.
- Support API InstallAgentForCluster.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListClusterAgentInstallRecords.
- Support API ListClusters.
- Support API ListDiagnosis.
- Support API ListInstanceHealth.
- Support API ListInstanceStatus.
- Support API ListInstances.
- Support API ListInstancesEcsInfoList.
- Support API ListInstancesWithEcsInfo.
- Support API ListPluginsInstances.
- Support API ListPodsOfInstance.
- Support API ListRegions.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UninstallAgentForCluster.
- Support API UpdateEventsAttention.
- Support API UpdateFuncSwitchRecord.
- Support API UpgradeAgent.
- Support API UpgradeAgentForCluster.


2025-02-11 Version: 1.8.0
- Support API GenerateCopilotStreamResponse.
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetCopilotHistory.
- Support API GetHostCount.
- Support API GetHotSpotUniqList.
- Support API GetHotspotAnalysis.
- Support API GetHotspotCompare.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetHotspotTracking.
- Support API GetInstantScore.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API GetServiceFuncStatus.
- Support API InitialSysom.
- Support API InstallAgent.
- Support API InstallAgentForCluster.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListClusterAgentInstallRecords.
- Support API ListClusters.
- Support API ListDiagnosis.
- Support API ListInstanceHealth.
- Support API ListInstanceStatus.
- Support API ListInstances.
- Support API ListPodsOfInstance.
- Support API ListRegions.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UninstallAgentForCluster.
- Support API UpdateEventsAttention.
- Support API UpdateFuncSwitchRecord.
- Support API UpgradeAgent.
- Support API UpgradeAgentForCluster.


2025-02-10 Version: 1.7.0
- Support API GenerateCopilotStreamResponse.
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetCopilotHistory.
- Support API GetHostCount.
- Support API GetHotSpotUniqList.
- Support API GetHotspotAnalysis.
- Support API GetHotspotCompare.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetHotspotTracking.
- Support API GetInstantScore.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API InitialSysom.
- Support API InstallAgent.
- Support API InstallAgentForCluster.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListClusterAgentInstallRecords.
- Support API ListClusters.
- Support API ListDiagnosis.
- Support API ListInstanceHealth.
- Support API ListInstanceStatus.
- Support API ListInstances.
- Support API ListPodsOfInstance.
- Support API ListRegions.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UninstallAgentForCluster.
- Support API UpdateEventsAttention.
- Support API UpgradeAgent.
- Support API UpgradeAgentForCluster.


2025-02-07 Version: 1.6.0
- Support API GenerateCopilotStreamResponse.
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetCopilotHistory.
- Support API GetHostCount.
- Support API GetHotSpotUniqList.
- Support API GetHotspotAnalysis.
- Support API GetHotspotCompare.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetHotspotTracking.
- Support API GetInstantScore.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API InitialSysom.
- Support API InstallAgent.
- Support API InstallAgentForCluster.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListClusterAgentInstallRecords.
- Support API ListClusters.
- Support API ListDiagnosis.
- Support API ListInstanceHealth.
- Support API ListInstanceStatus.
- Support API ListInstances.
- Support API ListPodsOfInstance.
- Support API ListRegions.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UninstallAgentForCluster.
- Support API UpdateEventsAttention.
- Support API UpgradeAgent.
- Support API UpgradeAgentForCluster.


2025-02-07 Version: 1.5.0
- Support API GenerateCopilotStreamResponse.
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetCopilotHistory.
- Support API GetHostCount.
- Support API GetHotSpotUniqList.
- Support API GetHotspotAnalysis.
- Support API GetHotspotCompare.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetHotspotTracking.
- Support API GetInstantScore.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API InitialSysom.
- Support API InstallAgent.
- Support API InstallAgentForCluster.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListClusterAgentInstallRecords.
- Support API ListClusters.
- Support API ListDiagnosis.
- Support API ListInstanceHealth.
- Support API ListInstanceStatus.
- Support API ListInstances.
- Support API ListPodsOfInstance.
- Support API ListRegions.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UninstallAgentForCluster.
- Support API UpdateEventsAttention.
- Support API UpgradeAgent.
- Support API UpgradeAgentForCluster.


2025-02-07 Version: 1.4.0
- Support API GenerateCopilotStreamResponse.
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetCopilotHistory.
- Support API GetHostCount.
- Support API GetHotSpotUniqList.
- Support API GetHotspotAnalysis.
- Support API GetHotspotCompare.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetHotspotTracking.
- Support API GetInstantScore.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API InitialSysom.
- Support API InstallAgent.
- Support API InstallAgentForCluster.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListClusterAgentInstallRecords.
- Support API ListClusters.
- Support API ListDiagnosis.
- Support API ListInstanceHealth.
- Support API ListInstanceStatus.
- Support API ListInstances.
- Support API ListPodsOfInstance.
- Support API ListRegions.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UninstallAgentForCluster.
- Support API UpdateEventsAttention.
- Support API UpgradeAgent.
- Support API UpgradeAgentForCluster.


2024-12-26 Version: 1.3.0
- Support API GetAIQueryResult.
- Support API GetAgent.
- Support API GetAgentTask.
- Support API GetHostCount.
- Support API GetHotspotAnalysis.
- Support API GetHotspotInstanceList.
- Support API GetHotspotPidList.
- Support API GetListRecord.
- Support API GetProblemPercentage.
- Support API GetRangeScore.
- Support API GetResources.
- Support API InstallAgent.
- Support API InvokeAnomalyDiagnosis.
- Support API ListAbnormalyEvents.
- Support API ListAgentInstallRecords.
- Support API ListAgents.
- Support API ListInstanceHealth.
- Support API StartAIAnalysis.
- Support API UninstallAgent.
- Support API UpgradeAgent.


2024-12-24 Version: 1.2.1
- Update API GetAbnormalEventsCount: add param showPod.


2024-10-16 Version: 1.2.0
- Support API GetAbnormalEventsCount.
- Support API GetHealthPercentage.
- Update API AuthDiagnosis: update param body.
- Update API GenerateCopilotResponse: update response param.
- Update API GetDiagnosisResult: update response param.
- Update API InvokeDiagnosis: update response param.


2024-04-09 Version: 1.1.0
- Support API GenerateCopilotResponse.


2024-04-09 Version: 1.0.1
- Generated python 2023-12-30 for SysOM.

2024-01-29 Version: 1.0.0
- Generated python 2023-12-30 for SysOM.

