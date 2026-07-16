# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._bandwidth_limit import BandwidthLimit
from ._credential_config import CredentialConfig
from ._demo_category import DemoCategory
from ._dynamic_mount import DynamicMount
from ._dynamic_mount_point import DynamicMountPoint
from ._forward_info import ForwardInfo
from ._forward_info_response import ForwardInfoResponse
from ._pod_ip import PodIp
from ._service_config import ServiceConfig
from ._create_diagnosis_request import CreateDiagnosisRequest
from ._create_diagnosis_response_body import CreateDiagnosisResponseBody
from ._create_diagnosis_response import CreateDiagnosisResponse
from ._create_idle_instance_culler_request import CreateIdleInstanceCullerRequest
from ._create_idle_instance_culler_response_body import CreateIdleInstanceCullerResponseBody
from ._create_idle_instance_culler_response import CreateIdleInstanceCullerResponse
from ._create_instance_request import CreateInstanceRequest
from ._create_instance_response_body import CreateInstanceResponseBody
from ._create_instance_response import CreateInstanceResponse
from ._create_instance_shutdown_timer_request import CreateInstanceShutdownTimerRequest
from ._create_instance_shutdown_timer_response_body import CreateInstanceShutdownTimerResponseBody
from ._create_instance_shutdown_timer_response import CreateInstanceShutdownTimerResponse
from ._create_instance_snapshot_request import CreateInstanceSnapshotRequest
from ._create_instance_snapshot_response_body import CreateInstanceSnapshotResponseBody
from ._create_instance_snapshot_response import CreateInstanceSnapshotResponse
from ._create_sanity_check_task_request import CreateSanityCheckTaskRequest
from ._create_sanity_check_task_response_body import CreateSanityCheckTaskResponseBody
from ._create_sanity_check_task_response import CreateSanityCheckTaskResponse
from ._create_temp_file_request import CreateTempFileRequest
from ._create_temp_file_response_body import CreateTempFileResponseBody
from ._create_temp_file_response import CreateTempFileResponse
from ._create_temp_file_task_request import CreateTempFileTaskRequest
from ._create_temp_file_task_response_body import CreateTempFileTaskResponseBody
from ._create_temp_file_task_response import CreateTempFileTaskResponse
from ._delete_idle_instance_culler_response_body import DeleteIdleInstanceCullerResponseBody
from ._delete_idle_instance_culler_response import DeleteIdleInstanceCullerResponse
from ._delete_instance_response_body import DeleteInstanceResponseBody
from ._delete_instance_response import DeleteInstanceResponse
from ._delete_instance_labels_request import DeleteInstanceLabelsRequest
from ._delete_instance_labels_response_body import DeleteInstanceLabelsResponseBody
from ._delete_instance_labels_response import DeleteInstanceLabelsResponse
from ._delete_instance_shutdown_timer_response_body import DeleteInstanceShutdownTimerResponseBody
from ._delete_instance_shutdown_timer_response import DeleteInstanceShutdownTimerResponse
from ._delete_instance_snapshot_response_body import DeleteInstanceSnapshotResponseBody
from ._delete_instance_snapshot_response import DeleteInstanceSnapshotResponse
from ._delete_instances_request import DeleteInstancesRequest
from ._delete_instances_response_body import DeleteInstancesResponseBody
from ._delete_instances_response import DeleteInstancesResponse
from ._delete_temp_file_response_body import DeleteTempFileResponseBody
from ._delete_temp_file_response import DeleteTempFileResponse
from ._delete_temp_file_task_response_body import DeleteTempFileTaskResponseBody
from ._delete_temp_file_task_response import DeleteTempFileTaskResponse
from ._delete_temp_file_tasks_request import DeleteTempFileTasksRequest
from ._delete_temp_file_tasks_response_body import DeleteTempFileTasksResponseBody
from ._delete_temp_file_tasks_response import DeleteTempFileTasksResponse
from ._get_idle_instance_culler_response_body import GetIdleInstanceCullerResponseBody
from ._get_idle_instance_culler_response import GetIdleInstanceCullerResponse
from ._get_instance_request import GetInstanceRequest
from ._get_instance_response_body import GetInstanceResponseBody
from ._get_instance_response import GetInstanceResponse
from ._get_instance_events_request import GetInstanceEventsRequest
from ._get_instance_events_response_body import GetInstanceEventsResponseBody
from ._get_instance_events_response import GetInstanceEventsResponse
from ._get_instance_metrics_request import GetInstanceMetricsRequest
from ._get_instance_metrics_response_body import GetInstanceMetricsResponseBody
from ._get_instance_metrics_response import GetInstanceMetricsResponse
from ._get_instance_shutdown_timer_response_body import GetInstanceShutdownTimerResponseBody
from ._get_instance_shutdown_timer_response import GetInstanceShutdownTimerResponse
from ._get_instance_snapshot_response_body import GetInstanceSnapshotResponseBody
from ._get_instance_snapshot_response import GetInstanceSnapshotResponse
from ._get_lifecycle_request import GetLifecycleRequest
from ._get_lifecycle_response_body import GetLifecycleResponseBody
from ._get_lifecycle_response import GetLifecycleResponse
from ._get_metrics_request import GetMetricsRequest
from ._get_metrics_response_body import GetMetricsResponseBody
from ._get_metrics_response import GetMetricsResponse
from ._get_resource_group_statistics_request import GetResourceGroupStatisticsRequest
from ._get_resource_group_statistics_response_body import GetResourceGroupStatisticsResponseBody
from ._get_resource_group_statistics_response import GetResourceGroupStatisticsResponse
from ._get_sanity_check_task_request import GetSanityCheckTaskRequest
from ._get_sanity_check_task_response_body import GetSanityCheckTaskResponseBody
from ._get_sanity_check_task_response import GetSanityCheckTaskResponse
from ._get_temp_file_response_body import GetTempFileResponseBody
from ._get_temp_file_response import GetTempFileResponse
from ._get_temp_file_task_response_body import GetTempFileTaskResponseBody
from ._get_temp_file_task_response import GetTempFileTaskResponse
from ._get_token_request import GetTokenRequest
from ._get_token_response_body import GetTokenResponseBody
from ._get_token_response import GetTokenResponse
from ._get_user_command_request import GetUserCommandRequest
from ._get_user_command_response_body import GetUserCommandResponseBody
from ._get_user_command_response import GetUserCommandResponse
from ._get_user_config_response_body import GetUserConfigResponseBody
from ._get_user_config_response import GetUserConfigResponse
from ._list_ecs_specs_request import ListEcsSpecsRequest
from ._list_ecs_specs_response_body import ListEcsSpecsResponseBody
from ._list_ecs_specs_response import ListEcsSpecsResponse
from ._list_instance_snapshot_request import ListInstanceSnapshotRequest
from ._list_instance_snapshot_response_body import ListInstanceSnapshotResponseBody
from ._list_instance_snapshot_response import ListInstanceSnapshotResponse
from ._list_instance_statistics_request import ListInstanceStatisticsRequest
from ._list_instance_statistics_response_body import ListInstanceStatisticsResponseBody
from ._list_instance_statistics_response import ListInstanceStatisticsResponse
from ._list_instances_request import ListInstancesRequest
from ._list_instances_shrink_request import ListInstancesShrinkRequest
from ._list_instances_response_body import ListInstancesResponseBody
from ._list_instances_response import ListInstancesResponse
from ._list_system_logs_request import ListSystemLogsRequest
from ._list_system_logs_response_body import ListSystemLogsResponseBody
from ._list_system_logs_response import ListSystemLogsResponse
from ._list_temp_files_request import ListTempFilesRequest
from ._list_temp_files_response_body import ListTempFilesResponseBody
from ._list_temp_files_response import ListTempFilesResponse
from ._query_auto_shutdown_policies_request import QueryAutoShutdownPoliciesRequest
from ._query_auto_shutdown_policies_response_body import QueryAutoShutdownPoliciesResponseBody
from ._query_auto_shutdown_policies_response import QueryAutoShutdownPoliciesResponse
from ._start_instance_response_body import StartInstanceResponseBody
from ._start_instance_response import StartInstanceResponse
from ._stop_instance_request import StopInstanceRequest
from ._stop_instance_response_body import StopInstanceResponseBody
from ._stop_instance_response import StopInstanceResponse
from ._stop_instances_request import StopInstancesRequest
from ._stop_instances_response_body import StopInstancesResponseBody
from ._stop_instances_response import StopInstancesResponse
from ._update_instance_request import UpdateInstanceRequest
from ._update_instance_response_body import UpdateInstanceResponseBody
from ._update_instance_response import UpdateInstanceResponse
from ._update_instance_labels_request import UpdateInstanceLabelsRequest
from ._update_instance_labels_response_body import UpdateInstanceLabelsResponseBody
from ._update_instance_labels_response import UpdateInstanceLabelsResponse
from ._update_temp_file_request import UpdateTempFileRequest
from ._update_temp_file_response_body import UpdateTempFileResponseBody
from ._update_temp_file_response import UpdateTempFileResponse
from ._update_temp_file_task_request import UpdateTempFileTaskRequest
from ._update_temp_file_task_response_body import UpdateTempFileTaskResponseBody
from ._update_temp_file_task_response import UpdateTempFileTaskResponse
from ._credential_config import CredentialConfigConfigsRolesUserInfo
from ._credential_config import CredentialConfigConfigsRoles
from ._credential_config import CredentialConfigConfigs
from ._forward_info_response import ForwardInfoResponseConnectInfoInternet
from ._forward_info_response import ForwardInfoResponseConnectInfoIntranet
from ._forward_info_response import ForwardInfoResponseConnectInfo
from ._create_instance_request import CreateInstanceRequestAffinityCPU
from ._create_instance_request import CreateInstanceRequestAffinity
from ._create_instance_request import CreateInstanceRequestAssignNodeSpec
from ._create_instance_request import CreateInstanceRequestCloudDisksStatus
from ._create_instance_request import CreateInstanceRequestCloudDisks
from ._create_instance_request import CreateInstanceRequestDatasets
from ._create_instance_request import CreateInstanceRequestDockerConfig
from ._create_instance_request import CreateInstanceRequestLabels
from ._create_instance_request import CreateInstanceRequestRequestedResource
from ._create_instance_request import CreateInstanceRequestSpotSpec
from ._create_instance_request import CreateInstanceRequestTag
from ._create_instance_request import CreateInstanceRequestUserCommandOnStart
from ._create_instance_request import CreateInstanceRequestUserCommand
from ._create_instance_request import CreateInstanceRequestUserVpc
from ._create_instance_snapshot_request import CreateInstanceSnapshotRequestLabels
from ._get_instance_response_body import GetInstanceResponseBodyAffinityCPU
from ._get_instance_response_body import GetInstanceResponseBodyAffinity
from ._get_instance_response_body import GetInstanceResponseBodyCloudDisksStatus
from ._get_instance_response_body import GetInstanceResponseBodyCloudDisks
from ._get_instance_response_body import GetInstanceResponseBodyDatasets
from ._get_instance_response_body import GetInstanceResponseBodyDockerConfig
from ._get_instance_response_body import GetInstanceResponseBodyIdleInstanceCuller
from ._get_instance_response_body import GetInstanceResponseBodyInstanceShutdownTimer
from ._get_instance_response_body import GetInstanceResponseBodyInstanceSnapshotList
from ._get_instance_response_body import GetInstanceResponseBodyLabels
from ._get_instance_response_body import GetInstanceResponseBodyLatestSnapshot
from ._get_instance_response_body import GetInstanceResponseBodyNodeErrorRecovery
from ._get_instance_response_body import GetInstanceResponseBodyRequestedResource
from ._get_instance_response_body import GetInstanceResponseBodyTags
from ._get_instance_response_body import GetInstanceResponseBodyUserVpc
from ._get_instance_metrics_response_body import GetInstanceMetricsResponseBodyPodMetricsMetrics
from ._get_instance_metrics_response_body import GetInstanceMetricsResponseBodyPodMetrics
from ._get_instance_snapshot_response_body import GetInstanceSnapshotResponseBodyLabels
from ._get_lifecycle_response_body import GetLifecycleResponseBodyLifecycle
from ._get_sanity_check_task_response_body import GetSanityCheckTaskResponseBodyCheckDetails
from ._get_user_command_response_body import GetUserCommandResponseBodyOnStart
from ._get_user_config_response_body import GetUserConfigResponseBodyFreeTier
from ._list_ecs_specs_response_body import ListEcsSpecsResponseBodyEcsSpecsLabels
from ._list_ecs_specs_response_body import ListEcsSpecsResponseBodyEcsSpecs
from ._list_instance_snapshot_response_body import ListInstanceSnapshotResponseBodySnapshotsLabels
from ._list_instance_snapshot_response_body import ListInstanceSnapshotResponseBodySnapshots
from ._list_instances_request import ListInstancesRequestTag
from ._list_instances_response_body import ListInstancesResponseBodyInstancesAffinityCPU
from ._list_instances_response_body import ListInstancesResponseBodyInstancesAffinity
from ._list_instances_response_body import ListInstancesResponseBodyInstancesCloudDisks
from ._list_instances_response_body import ListInstancesResponseBodyInstancesDatasets
from ._list_instances_response_body import ListInstancesResponseBodyInstancesIdleInstanceCuller
from ._list_instances_response_body import ListInstancesResponseBodyInstancesInstanceShutdownTimer
from ._list_instances_response_body import ListInstancesResponseBodyInstancesInstanceSnapshotList
from ._list_instances_response_body import ListInstancesResponseBodyInstancesLabels
from ._list_instances_response_body import ListInstancesResponseBodyInstancesLatestSnapshot
from ._list_instances_response_body import ListInstancesResponseBodyInstancesRequestedResource
from ._list_instances_response_body import ListInstancesResponseBodyInstancesTags
from ._list_instances_response_body import ListInstancesResponseBodyInstancesUserVpc
from ._list_instances_response_body import ListInstancesResponseBodyInstances
from ._list_system_logs_response_body import ListSystemLogsResponseBodySystemLogs
from ._list_temp_files_response_body import ListTempFilesResponseBodyQuota
from ._list_temp_files_response_body import ListTempFilesResponseBodyTempFiles
from ._query_auto_shutdown_policies_response_body import QueryAutoShutdownPoliciesResponseBodyAutoShutdownPoliciesConditions
from ._query_auto_shutdown_policies_response_body import QueryAutoShutdownPoliciesResponseBodyAutoShutdownPolicies
from ._update_instance_request import UpdateInstanceRequestAffinityCPU
from ._update_instance_request import UpdateInstanceRequestAffinity
from ._update_instance_request import UpdateInstanceRequestAssignNodeSpec
from ._update_instance_request import UpdateInstanceRequestCloudDisks
from ._update_instance_request import UpdateInstanceRequestDatasets
from ._update_instance_request import UpdateInstanceRequestRequestedResource
from ._update_instance_request import UpdateInstanceRequestSpotSpec
from ._update_instance_request import UpdateInstanceRequestUserCommandOnStart
from ._update_instance_request import UpdateInstanceRequestUserCommand
from ._update_instance_request import UpdateInstanceRequestUserVpc
from ._update_instance_labels_request import UpdateInstanceLabelsRequestLabels

__all__ = [
    BandwidthLimit,
    CredentialConfig,
    DemoCategory,
    DynamicMount,
    DynamicMountPoint,
    ForwardInfo,
    ForwardInfoResponse,
    PodIp,
    ServiceConfig,
    CreateDiagnosisRequest,
    CreateDiagnosisResponseBody,
    CreateDiagnosisResponse,
    CreateIdleInstanceCullerRequest,
    CreateIdleInstanceCullerResponseBody,
    CreateIdleInstanceCullerResponse,
    CreateInstanceRequest,
    CreateInstanceResponseBody,
    CreateInstanceResponse,
    CreateInstanceShutdownTimerRequest,
    CreateInstanceShutdownTimerResponseBody,
    CreateInstanceShutdownTimerResponse,
    CreateInstanceSnapshotRequest,
    CreateInstanceSnapshotResponseBody,
    CreateInstanceSnapshotResponse,
    CreateSanityCheckTaskRequest,
    CreateSanityCheckTaskResponseBody,
    CreateSanityCheckTaskResponse,
    CreateTempFileRequest,
    CreateTempFileResponseBody,
    CreateTempFileResponse,
    CreateTempFileTaskRequest,
    CreateTempFileTaskResponseBody,
    CreateTempFileTaskResponse,
    DeleteIdleInstanceCullerResponseBody,
    DeleteIdleInstanceCullerResponse,
    DeleteInstanceResponseBody,
    DeleteInstanceResponse,
    DeleteInstanceLabelsRequest,
    DeleteInstanceLabelsResponseBody,
    DeleteInstanceLabelsResponse,
    DeleteInstanceShutdownTimerResponseBody,
    DeleteInstanceShutdownTimerResponse,
    DeleteInstanceSnapshotResponseBody,
    DeleteInstanceSnapshotResponse,
    DeleteInstancesRequest,
    DeleteInstancesResponseBody,
    DeleteInstancesResponse,
    DeleteTempFileResponseBody,
    DeleteTempFileResponse,
    DeleteTempFileTaskResponseBody,
    DeleteTempFileTaskResponse,
    DeleteTempFileTasksRequest,
    DeleteTempFileTasksResponseBody,
    DeleteTempFileTasksResponse,
    GetIdleInstanceCullerResponseBody,
    GetIdleInstanceCullerResponse,
    GetInstanceRequest,
    GetInstanceResponseBody,
    GetInstanceResponse,
    GetInstanceEventsRequest,
    GetInstanceEventsResponseBody,
    GetInstanceEventsResponse,
    GetInstanceMetricsRequest,
    GetInstanceMetricsResponseBody,
    GetInstanceMetricsResponse,
    GetInstanceShutdownTimerResponseBody,
    GetInstanceShutdownTimerResponse,
    GetInstanceSnapshotResponseBody,
    GetInstanceSnapshotResponse,
    GetLifecycleRequest,
    GetLifecycleResponseBody,
    GetLifecycleResponse,
    GetMetricsRequest,
    GetMetricsResponseBody,
    GetMetricsResponse,
    GetResourceGroupStatisticsRequest,
    GetResourceGroupStatisticsResponseBody,
    GetResourceGroupStatisticsResponse,
    GetSanityCheckTaskRequest,
    GetSanityCheckTaskResponseBody,
    GetSanityCheckTaskResponse,
    GetTempFileResponseBody,
    GetTempFileResponse,
    GetTempFileTaskResponseBody,
    GetTempFileTaskResponse,
    GetTokenRequest,
    GetTokenResponseBody,
    GetTokenResponse,
    GetUserCommandRequest,
    GetUserCommandResponseBody,
    GetUserCommandResponse,
    GetUserConfigResponseBody,
    GetUserConfigResponse,
    ListEcsSpecsRequest,
    ListEcsSpecsResponseBody,
    ListEcsSpecsResponse,
    ListInstanceSnapshotRequest,
    ListInstanceSnapshotResponseBody,
    ListInstanceSnapshotResponse,
    ListInstanceStatisticsRequest,
    ListInstanceStatisticsResponseBody,
    ListInstanceStatisticsResponse,
    ListInstancesRequest,
    ListInstancesShrinkRequest,
    ListInstancesResponseBody,
    ListInstancesResponse,
    ListSystemLogsRequest,
    ListSystemLogsResponseBody,
    ListSystemLogsResponse,
    ListTempFilesRequest,
    ListTempFilesResponseBody,
    ListTempFilesResponse,
    QueryAutoShutdownPoliciesRequest,
    QueryAutoShutdownPoliciesResponseBody,
    QueryAutoShutdownPoliciesResponse,
    StartInstanceResponseBody,
    StartInstanceResponse,
    StopInstanceRequest,
    StopInstanceResponseBody,
    StopInstanceResponse,
    StopInstancesRequest,
    StopInstancesResponseBody,
    StopInstancesResponse,
    UpdateInstanceRequest,
    UpdateInstanceResponseBody,
    UpdateInstanceResponse,
    UpdateInstanceLabelsRequest,
    UpdateInstanceLabelsResponseBody,
    UpdateInstanceLabelsResponse,
    UpdateTempFileRequest,
    UpdateTempFileResponseBody,
    UpdateTempFileResponse,
    UpdateTempFileTaskRequest,
    UpdateTempFileTaskResponseBody,
    UpdateTempFileTaskResponse,
    CredentialConfigConfigsRolesUserInfo,
    CredentialConfigConfigsRoles,
    CredentialConfigConfigs,
    ForwardInfoResponseConnectInfoInternet,
    ForwardInfoResponseConnectInfoIntranet,
    ForwardInfoResponseConnectInfo,
    CreateInstanceRequestAffinityCPU,
    CreateInstanceRequestAffinity,
    CreateInstanceRequestAssignNodeSpec,
    CreateInstanceRequestCloudDisksStatus,
    CreateInstanceRequestCloudDisks,
    CreateInstanceRequestDatasets,
    CreateInstanceRequestDockerConfig,
    CreateInstanceRequestLabels,
    CreateInstanceRequestRequestedResource,
    CreateInstanceRequestSpotSpec,
    CreateInstanceRequestTag,
    CreateInstanceRequestUserCommandOnStart,
    CreateInstanceRequestUserCommand,
    CreateInstanceRequestUserVpc,
    CreateInstanceSnapshotRequestLabels,
    GetInstanceResponseBodyAffinityCPU,
    GetInstanceResponseBodyAffinity,
    GetInstanceResponseBodyCloudDisksStatus,
    GetInstanceResponseBodyCloudDisks,
    GetInstanceResponseBodyDatasets,
    GetInstanceResponseBodyDockerConfig,
    GetInstanceResponseBodyIdleInstanceCuller,
    GetInstanceResponseBodyInstanceShutdownTimer,
    GetInstanceResponseBodyInstanceSnapshotList,
    GetInstanceResponseBodyLabels,
    GetInstanceResponseBodyLatestSnapshot,
    GetInstanceResponseBodyNodeErrorRecovery,
    GetInstanceResponseBodyRequestedResource,
    GetInstanceResponseBodyTags,
    GetInstanceResponseBodyUserVpc,
    GetInstanceMetricsResponseBodyPodMetricsMetrics,
    GetInstanceMetricsResponseBodyPodMetrics,
    GetInstanceSnapshotResponseBodyLabels,
    GetLifecycleResponseBodyLifecycle,
    GetSanityCheckTaskResponseBodyCheckDetails,
    GetUserCommandResponseBodyOnStart,
    GetUserConfigResponseBodyFreeTier,
    ListEcsSpecsResponseBodyEcsSpecsLabels,
    ListEcsSpecsResponseBodyEcsSpecs,
    ListInstanceSnapshotResponseBodySnapshotsLabels,
    ListInstanceSnapshotResponseBodySnapshots,
    ListInstancesRequestTag,
    ListInstancesResponseBodyInstancesAffinityCPU,
    ListInstancesResponseBodyInstancesAffinity,
    ListInstancesResponseBodyInstancesCloudDisks,
    ListInstancesResponseBodyInstancesDatasets,
    ListInstancesResponseBodyInstancesIdleInstanceCuller,
    ListInstancesResponseBodyInstancesInstanceShutdownTimer,
    ListInstancesResponseBodyInstancesInstanceSnapshotList,
    ListInstancesResponseBodyInstancesLabels,
    ListInstancesResponseBodyInstancesLatestSnapshot,
    ListInstancesResponseBodyInstancesRequestedResource,
    ListInstancesResponseBodyInstancesTags,
    ListInstancesResponseBodyInstancesUserVpc,
    ListInstancesResponseBodyInstances,
    ListSystemLogsResponseBodySystemLogs,
    ListTempFilesResponseBodyQuota,
    ListTempFilesResponseBodyTempFiles,
    QueryAutoShutdownPoliciesResponseBodyAutoShutdownPoliciesConditions,
    QueryAutoShutdownPoliciesResponseBodyAutoShutdownPolicies,
    UpdateInstanceRequestAffinityCPU,
    UpdateInstanceRequestAffinity,
    UpdateInstanceRequestAssignNodeSpec,
    UpdateInstanceRequestCloudDisks,
    UpdateInstanceRequestDatasets,
    UpdateInstanceRequestRequestedResource,
    UpdateInstanceRequestSpotSpec,
    UpdateInstanceRequestUserCommandOnStart,
    UpdateInstanceRequestUserCommand,
    UpdateInstanceRequestUserVpc,
    UpdateInstanceLabelsRequestLabels
]
