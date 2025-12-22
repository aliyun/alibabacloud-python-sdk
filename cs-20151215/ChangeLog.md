2025-12-22 Version: 6.2.0
- Support API ListClusterAddonInstanceResources.


2025-12-22 Version: 6.2.0
- Support API ListClusterAddonInstanceResources.


2025-12-01 Version: 6.1.2
- Update API DescribeClusterAttachScripts: add request parameters body.one_time_token.


2025-11-25 Version: 6.1.1
- Update API CreateClusterNodePool: add request parameters body.scaling_group.system_disk_snapshot_policy_id.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.scaling_group.system_disk_snapshot_policy_id.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.status.conditions.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.scaling_group.system_disk_snapshot_policy_id.
- Update API ListOperationPlansForRegion: add response parameters Body.plans.$.state_reason.
- Update API ModifyClusterNodePool: add request parameters body.scaling_group.system_disk_snapshot_policy_id.


2025-11-05 Version: 6.1.0
- Support API ListOperationPlansForRegion.
- Update API CreateClusterNodePool: add request parameters body.node_components.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.node_components.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.node_components.


2025-10-30 Version: 6.0.0
- Update API DescribePolicyGovernanceInCluster: add response parameters Body.Violation.
- Update API DescribePolicyGovernanceInCluster: add response parameters Body.admit_log.log_project.
- Update API DescribePolicyGovernanceInCluster: add response parameters Body.admit_log.log_store.
- Update API DescribePolicyGovernanceInCluster: add response parameters Body.admit_log.logs.
- Update API DescribePolicyGovernanceInCluster: delete response parameters Body.admit_log.log.
- Update API DescribePolicyGovernanceInCluster: delete response parameters Body.totalViolations.
- Update API DescribePolicyGovernanceInCluster: delete response parameters Body.violations.


2025-10-10 Version: 5.0.0
- Delete API CreateEdgeMachine.
- Delete API DeleteEdgeMachine.
- Delete API DescribeEdgeMachineActiveProcess.
- Delete API DescribeEdgeMachineModels.
- Delete API DescribeEdgeMachineTunnelConfigDetail.
- Delete API DescribeEdgeMachines.
- Delete API EdgeClusterAddEdgeMachine.
- Delete API ModifyClusterConfiguration.
- Delete API ScaleCluster.
- Update API CreateClusterNodePool: add request parameters body.scaling_group.resource_pool_options.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.node_config.node_os_config.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.scaling_group.resource_pool_options.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.node_config.node_os_config.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.scaling_group.resource_pool_options.
- Update API ModifyClusterNodePool: add request parameters body.scaling_group.resource_pool_options.
- Update API ModifyNodePoolNodeConfig: add request parameters body.os_config.hugepage.


2025-09-11 Version: 4.9.8
- Generated python 2015-12-15 for CS.

2025-08-19 Version: 4.9.7
- Update API CreateClusterNodePool: add request parameters body.management.auto_vul_fix_policy.exclude_packages.
- Update API DescribeClusterDetail: add response parameters Body.extra_sans.
- Update API DescribeClusterDetail: add response parameters Body.rrsa_config.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.management.auto_vul_fix_policy.exclude_packages.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.management.auto_vul_fix_policy.exclude_packages.
- Update API DescribeNodePoolVuls: add response parameters Body.vul_records.$.vul_list.$.package_list.
- Update API ModifyClusterNodePool: add request parameters body.kubernetes_config.node_name_mode.
- Update API ModifyClusterNodePool: add request parameters body.management.auto_vul_fix_policy.exclude_packages.


2025-07-29 Version: 4.9.6
- Update API CreateCluster: add request parameters body.control_plane_config.instance_metadata_options.
- Update API CreateClusterNodePool: add request parameters body.scaling_group.instance_metadata_options.
- Update API DescribeClusterDetail: add response parameters Body.control_plane_config.instance_metadata_options.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.scaling_group.instance_metadata_options.


2025-07-04 Version: 4.9.5
- Update API CreateCluster: add request parameters body.extra_sans.
- Update API CreateCluster: add request parameters body.rrsa_config.


2025-06-10 Version: 4.9.4
- Update API CreateCluster: add request parameters body.auto_mode.
- Update API CreateClusterNodePool: add request parameters body.auto_mode.
- Update API DescribeClusterDetail: add response parameters Body.auto_mode.


2025-06-09 Version: 4.9.3
- Update API CreateClusterNodePool: add request parameters body.eflo_node_group.


2025-05-30 Version: 4.9.2
- Update API CreateClusterNodePool: add request parameters body.management.auto_repair_policy.approval_required.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.management.auto_repair_policy.approval_required.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.management.auto_repair_policy.approval_required.
- Update API ModifyClusterNodePool: add request parameters body.management.auto_repair_policy.approval_required.


2025-05-23 Version: 4.9.1
- Update API CreateCluster: add request parameters body.audit_log_config.


2025-05-14 Version: 4.9.0
- Support API CreateClusterInspectConfig.
- Support API DeleteClusterInspectConfig.
- Support API GetClusterInspectConfig.
- Support API GetClusterInspectReportDetail.
- Support API ListClusterInspectReports.
- Support API RunClusterInspect.
- Support API UpdateClusterInspectConfig.
- Update API DescribeClusterNodePoolDetail: add response parameters Body.auto_mode.
- Update API DescribeClusterNodePools: add response parameters Body.nodepools.$.auto_mode.
- Update API ModifyClusterNodePool: add request parameters body.scaling_group.deploymentset_id.
- Update API ModifyClusterNodePool: add request parameters body.scaling_group.security_group_ids.


2025-03-18 Version: 4.8.14
- Update API DescribeSubaccountK8sClusterUserConfig: update response param.


2025-02-28 Version: 4.8.13
- Update API DescribeClusterAttachScripts: update param body.
- Update API DescribeClusterUserKubeconfig: update response param.
- Update API DescribeClusterV2UserKubeconfig: update response param.
- Update API ModifyCluster: update param body.


2025-01-10 Version: 4.8.8
- Update API CreateAutoscalingConfig: update param body.


2024-12-30 Version: 4.8.7
- Update API ListOperationPlans: update response param.


2024-12-18 Version: 4.8.6
- Update API ModifyClusterTags: add param body.
- Update API ModifyClusterTags: update param body.


2024-12-13 Version: 4.8.5
- Update API GetClusterDiagnosisCheckItems: add param language.
- Update API GetClusterDiagnosisResult: add param language.


2024-12-12 Version: 4.8.4
- Update API InstallClusterAddons: update response param.
- Update API UnInstallClusterAddons: update response param.


2024-12-11 Version: 4.8.3
- Update API DescribeClusterV2UserKubeconfig: add param TemporaryDurationMinutes.


2024-12-05 Version: 4.8.2
- Update API CreateAutoscalingConfig: update param body.
- Update API CreateAutoscalingConfig: update response param.
- Update API CreateCluster: update param body.
- Update API CreateClusterNodePool: update param body.
- Update API ModifyClusterNodePool: update param body.


2024-11-25 Version: 4.8.1
- Update API CreateCluster: update param body.
- Update API DescribeClusterAttachScripts: add param body.
- Update API DescribeClusterAttachScripts: update param body.
- Update API DescribeClusterDetail: update response param.
- Update API DescribeClustersForRegion: update response param.
- Update API ModifyCluster: update param body.
- Update API ModifyClusterConfiguration: add param body.
- Update API ModifyClusterConfiguration: update param body.


2024-11-07 Version: 4.8.0
- Support API DescribeClustersForRegion.
- Support API DescribeEventsForRegion.


2024-11-05 Version: 4.7.10
- Update API CreateClusterNodePool: update param body.
- Update API DescribeClusterNodePoolDetail: update response param.


2024-10-24 Version: 4.7.9
- Update API DescribePolicyInstances: update response param.


2024-10-18 Version: 4.7.8
- Update API DescribeClusterDetail: update response param.
- Update API DescribeClustersV1: update response param.
- Update API ModifyCluster: update param body.


2024-10-15 Version: 4.7.7
- Update API CreateCluster: update param body.
- Update API DescribeClusterDetail: update response param.
- Update API DescribeClustersV1: update response param.


2024-09-27 Version: 4.7.6
- Update API CreateClusterNodePool: update param body.
- Update API DescribeClusterNodePoolDetail: update response param.
- Update API DescribeClusterNodePools: update response param.
- Update API ModifyClusterNodePool: update param body.


2024-09-24 Version: 4.7.5
- Update API CancelOperationPlan: update response param.
- Update API CreateCluster: update param body.
- Update API DescribeClusterAddonInstance: update param ClusterID.
- Update API DescribeClusterAddonInstance: update param AddonName.


2024-09-04 Version: 4.7.4
- Update API CreateCluster: update param body.
- Update API DeleteAlertContact: update response param.
- Update API DeleteAlertContactGroup: update response param.
- Update API DescribeSubaccountK8sClusterUserConfig: update response param.


2024-08-14 Version: 4.7.3
- Update API UpgradeCluster: update param body.


2024-08-06 Version: 4.7.2
- Update API GetClusterAuditProject: update response param.


2024-08-02 Version: 4.7.1
- Update API DeleteAlertContact: update param contact_ids.
- Update API DeleteAlertContact: update response param.
- Update API DeleteAlertContactGroup: update param contact_group_ids.
- Update API DeleteAlertContactGroup: update response param.
- Update API StartAlert: update param body.
- Update API StartAlert: update param body.
- Update API StopAlert: update param body.
- Update API UpdateContactGroupForAlert: add param body.
- Update API UpdateContactGroupForAlert: update response param.


2024-07-25 Version: 4.7.0
- Support API RevokeK8sClusterKubeConfig.


2024-07-24 Version: 4.6.0
- Support API GetClusterAuditProject.


2024-07-24 Version: 4.5.2
- Update API UpgradeClusterAddons: update response param.


2024-07-19 Version: 4.5.1
- Generated python 2015-12-15 for CS.

2024-07-15 Version: 4.5.0
- Support API CleanClusterUserPermissions.
- Support API CleanUserPermissions.
- Support API ListClusterKubeconfigStates.
- Support API ListUserKubeConfigStates.


2024-07-11 Version: 4.4.0
- Support API UpdateClusterAuditLogConfig.


2024-07-09 Version: 4.3.3
- Update API CreateClusterNodePool: update param body.
- Update API DescribeClusterNodePoolDetail: update response param.
- Update API DescribeClusterNodePools: update response param.


2024-06-25 Version: 4.3.2
- Update API DescribeClusters: add param resource_group_id.


2024-06-25 Version: 4.3.1
- Update API DescribeNodePoolVuls: update response param.


2024-06-13 Version: 4.3.0
- Support API DescribeResourcesDeleteProtection.
- Support API UpdateResourcesDeleteProtection.
- Update API CreateClusterNodePool: update param body.
- Update API DescribeClusterNodePoolDetail: update response param.
- Update API DescribeClusterNodePools: update response param.
- Update API ModifyClusterNodePool: update param body.


2024-06-13 Version: 4.2.1
- Update API CreateClusterNodePool: update param body.
- Update API DescribeClusterNodePoolDetail: update response param.
- Update API DescribeClusterNodePools: update response param.
- Update API ModifyClusterNodePool: update param body.


2024-06-06 Version: 4.2.0
- Support API CreateClusterDiagnosis.
- Support API GetClusterDiagnosisCheckItems.
- Support API GetClusterDiagnosisResult.


2024-05-27 Version: 4.1.1
- Update API RepairClusterNodePool: update param body.


2024-05-24 Version: 4.1.0
- Support API CheckServiceRole.


2024-05-15 Version: 4.0.10
- Generated python 2015-12-15 for CS.

2024-05-15 Version: 4.0.9
- Update API DescribeKubernetesVersionMetadata: add param QueryUpgradableVersion.
- Update API DescribeKubernetesVersionMetadata: update response param.


2024-05-13 Version: 4.0.8
- Generated python 2015-12-15 for CS.

2024-05-09 Version: 4.0.7
- Update API DeleteCluster: add param delete_options.


2024-05-07 Version: 4.0.6
- Update API DescribeClusterDetail: update response param.
- Update API DescribeClusterNodePools: add param NodepoolName.


2024-04-24 Version: 4.0.5
- Update API ModifyCluster: update param body.


2024-04-23 Version: 4.0.4
- Update API DescribeClusterAddonMetadata: update param version.


2024-04-22 Version: 4.0.3
- Update API CreateCluster: update param body.
- Update API CreateClusterNodePool: update param body.
- Update API DescribeClusterNodePoolDetail: update response param.
- Update API DescribeClusterNodePools: update response param.


2024-04-19 Version: 4.0.2
- Update API CreateCluster: update param body.
- Update API CreateClusterNodePool: update param body.
- Update API ModifyClusterNodePool: update param body.
- Update API ModifyNodePoolNodeConfig: update param body.


2024-04-17 Version: 4.0.1
- Update API ModifyNodePoolNodeConfig: update param body.


2024-03-19 Version: 4.0.0
- Support API UpdateUserPermissions.
- Update API DeleteAlertContact: add param contact_ids.
- Update API DeleteAlertContact: update response param.
- Update API DeleteAlertContactGroup: add param contact_group_ids.
- Update API DeleteAlertContactGroup: update response param.
- Update API DescribeClusterResources: add param with_addon_resources.
- Update API DescribeClusterResources: update response param.
- Update API DescribeUserQuota: update response param.
- Update API ListClusterChecks: add param target.
- Update API RunClusterCheck: update param body.
- Update API StartAlert: add param body.
- Update API StopAlert: add param body.
- Update API UpgradeClusterAddons: update response param.
- Update API UpgradeClusterNodepool: update param body.


2024-02-06 Version: 3.3.5
- Generated python 2015-12-15 for CS.

2024-01-31 Version: 3.3.4
- Generated python 2015-12-15 for CS.

2024-01-19 Version: 3.3.3
- Generated python 2015-12-15 for CS.

2024-01-11 Version: 3.3.2
- Generated python 2015-12-15 for CS.

2024-01-09 Version: 3.3.1
- Generated python 2015-12-15 for CS.

2023-12-25 Version: 3.3.0
- Generated python 2015-12-15 for CS.

2023-12-13 Version: 3.2.1
- Generated python 2015-12-15 for CS.

2023-12-12 Version: 3.2.0
- Generated python 2015-12-15 for CS.

2023-11-25 Version: 3.1.2
- Generated python 2015-12-15 for CS.

2023-11-21 Version: 3.1.1
- Generated python 2015-12-15 for CS.

2023-11-20 Version: 3.1.0
- Generated python 2015-12-15 for CS.

2023-10-18 Version: 3.0.27
- Generated python 2015-12-15 for CS.

2023-10-12 Version: 3.0.26
- Generated python 2015-12-15 for CS.

2023-10-10 Version: 3.0.25
- Generated python 2015-12-15 for CS.

2023-08-15 Version: 3.0.24
- Generated python 2015-12-15 for CS.

2023-08-09 Version: 3.0.23
- Generated python 2015-12-15 for CS.

2023-08-08 Version: 3.0.22
- Generated python 2015-12-15 for CS.

2023-08-01 Version: 3.0.21
- Add new API DescribeUserClusterNamespaces.

2022-11-24 Version: 3.0.20
- Update DescribeUserQuota.

2022-09-26 Version: 3.0.19
- Update CreateCluster.

2022-09-23 Version: 3.0.18
- Update CreateCluster.

2022-09-21 Version: 3.0.17
- Update endpoint.

2022-09-02 Version: 3.0.16
- Update endpoint.

2022-08-30 Version: 3.0.15
- Update.

2022-08-11 Version: 3.0.14
- Update.

2022-05-24 Version: 3.0.13
- Update DescribeClusterResources.

2022-04-11 Version: 3.0.12
- Update CreateAutoscalingConfig.

2022-04-08 Version: 3.0.11
- Update DeleteClusterNodepool.

2022-04-08 Version: 3.0.10
- Update DeleteClusterNodepool.
- Update UpgradeClusterAddons.

2022-03-18 Version: 3.0.9
- Update DescribeClustersV1.

2022-03-15 Version: 3.0.8
- Update ModifyPolicyInstance.

2022-03-09 Version: 3.0.7
- Update UpdateK8sClusterUserConfig.

2022-02-21 Version: 3.0.6
- Update DeployPolicyInstance.

2022-01-07 Version: 3.0.5
- The node pool supports the desired number of nodes.

2021-12-17 Version: 3.0.4
- CreateClusterNodePool support user-defined node names .

2021-11-30 Version: 3.0.3
- Generated python 2015-12-15 for CS.

2021-11-24 Version: 3.0.2
- Update CreateCluster and ModifyCluster.

2021-11-19 Version: 3.0.1
- Support edge node pool.

2021-11-16 Version: 3.0.0
- Updated the data structure for worker_data_disks in CreateCluster.

2021-07-28 Version: 2.4.5
- Publish API CreateTrigger DeleteTrigger, DescribeTrigger, These three apis will replace CreateKubernetesTrigger, DeleteKubernetesTrigger, and GetKubernetesTrigger for trigger operations, The new API has authentication capabilities and operations are more controlled.
- CreateCluster Added the parameters for security hardening and enabling the log function of the control plane.
- DeleteClusterNodes returns cluster_id, request_id, and task_id.
- DeleteClusterNodepool returns request_id.

2021-07-13 Version: 2.4.4
- Publish CreateAutosaclingConfig API.

2021-07-06 Version: 2.4.3
- Fixed an issue with inconsistent size types in the WorkdataDisks in ScaleOutCluster.
- CreateClusterNodePool support public network IP.

2021-06-09 Version: 2.4.2
- AMP Version.

2021-03-16 Version: 2.4.1
- DescribeClusterNamespaces add response body.

2021-03-12 Version: 2.4.0
- ListTagResources has added the required parameters resource_type and region_id.
- DescribeClusterNodes changes the type of parameter instanceIds to string.
- DescribeClusterAddonsUpgradeStatus set parameters componentIds required .

2021-02-22 Version: 2.3.0
- AMP Version Upgrade.

2021-02-22 Version: 2.3.0
- AMP Version Upgrade.

2021-02-22 Version: 2.3.0
- AMP Version Upgrade.

2021-02-22 Version: 2.3.0
- AMP Version Upgrade.

2021-02-09 Version: 2.2.7
- AMP Version Upgrade.

2021-02-08 Version: 2.2.6
- AMP Version Upgrade.

2021-02-06 Version: 2.2.5
- AMP Version Upgrade.

2021-02-02 Version: 2.2.4
- AMP Version Upgrade.

2021-02-02 Version: 2.2.4
- AMP Version Upgrade.

2021-01-26 Version: 2.2.3
- AMP Version Upgrade.

2020-12-31 Version: 2.2.1
- AMP Version Upgrade.

2020-12-29 Version: 2.2.0
- AMP Version Upgrade.

2020-12-28 Version: 2.1.3
- AMP Version Upgrade.

2020-12-25 Version: 2.1.2
- AMP Version Upgrade.

2020-12-22 Version: 2.1.1
- AMP Version Upgrade.

2020-12-17 Version: 2.1.0
- AMP Version.

2020-12-08 Version: 2.0.6
- AMP Version.

2020-11-20 Version: 2.1.0
- AMP Version.

2020-09-28 Version: 2.0.6
- AMP Version.

2020-09-27 Version: 2.0.4
- AMP Version.

2020-09-27 Version: 2.0.3
- AMP Version.

2020-09-23 Version: 2.0.2
- AMP Version.

2020-09-23 Version: 2.0.1
- AMP Version.

2020-09-23 Version: 2.0.0
- AMP Version.

