# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._acs import ACS
from ._action import Action
from ._algorithm_spec import AlgorithmSpec
from ._allocate_strategy_spec import AllocateStrategySpec
from ._assign_node_spec import AssignNodeSpec
from ._binding_policy import BindingPolicy
from ._cache_info import CacheInfo
from ._cache_service import CacheService
from ._capacity_lock import CapacityLock
from ._channel import Channel
from ._channel_property import ChannelProperty
from ._cluster_spec import ClusterSpec
from ._component_spec import ComponentSpec
from ._condition_expression import ConditionExpression
from ._data_source import DataSource
from ._ecs_spec import EcsSpec
from ._eni_cache_config import EniCacheConfig
from ._features import Features
from ._forward_info import ForwardInfo
from ._gpuinfo import GPUInfo
from ._gpumetric import GPUMetric
from ._hyper_parameter_definition import HyperParameterDefinition
from ._hyper_parameter_range import HyperParameterRange
from ._job_settings import JobSettings
from ._job_view_metric import JobViewMetric
from ._label import Label
from ._location import Location
from ._machine_group import MachineGroup
from ._metric import Metric
from ._metric_definition import MetricDefinition
from ._node import Node
from ._node_cordon_parameters import NodeCordonParameters
from ._node_drain_parameters import NodeDrainParameters
from ._node_gpumetric import NodeGPUMetric
from ._node_metric import NodeMetric
from ._node_operation_parameters import NodeOperationParameters
from ._node_operation_result import NodeOperationResult
from ._node_pod_info import NodePodInfo
from ._node_snapshot import NodeSnapshot
from ._node_spec import NodeSpec
from ._node_statistics import NodeStatistics
from ._node_type import NodeType
from ._node_type_statistic import NodeTypeStatistic
from ._node_uncordon_parameters import NodeUncordonParameters
from ._node_view_metric import NodeViewMetric
from ._oversold_usage_config import OversoldUsageConfig
from ._permission import Permission
from ._queue_info import QueueInfo
from ._quota import Quota
from ._quota_cluster import QuotaCluster
from ._quota_config import QuotaConfig
from ._quota_details import QuotaDetails
from ._quota_id_name import QuotaIdName
from ._quota_job import QuotaJob
from ._quota_job_view_metric import QuotaJobViewMetric
from ._quota_metric import QuotaMetric
from ._quota_node_view_metric import QuotaNodeViewMetric
from ._quota_topo import QuotaTopo
from ._quota_user import QuotaUser
from ._quota_user_view_metric import QuotaUserViewMetric
from ._resource_amount import ResourceAmount
from ._resource_diagnosis_detail import ResourceDiagnosisDetail
from ._resource_group import ResourceGroup
from ._resource_group_metric import ResourceGroupMetric
from ._resource_info import ResourceInfo
from ._resource_infos import ResourceInfos
from ._resource_limit_details import ResourceLimitDetails
from ._resource_operation import ResourceOperation
from ._resource_spec import ResourceSpec
from ._rules import Rules
from ._sandbox_cache_config import SandboxCacheConfig
from ._scheduling_rule import SchedulingRule
from ._self_quota_preemption_config import SelfQuotaPreemptionConfig
from ._spot_price_item import SpotPriceItem
from ._spot_stock_preview import SpotStockPreview
from ._statistics_details import StatisticsDetails
from ._statistics_resources import StatisticsResources
from ._sub_quota_preemption_config import SubQuotaPreemptionConfig
from ._task import Task
from ._task_instance import TaskInstance
from ._task_instance_event import TaskInstanceEvent
from ._time_range_filter import TimeRangeFilter
from ._unschedulable_node_detail import UnschedulableNodeDetail
from ._user_info import UserInfo
from ._user_quota_permission import UserQuotaPermission
from ._user_view_metric import UserViewMetric
from ._user_vpc import UserVpc
from ._workload_details import WorkloadDetails
from ._workspace_id_name import WorkspaceIdName
from ._workspace_spec import WorkspaceSpec
from ._workspace_specs import WorkspaceSpecs
from ._check_instance_web_terminal_request import CheckInstanceWebTerminalRequest
from ._check_instance_web_terminal_response_body import CheckInstanceWebTerminalResponseBody
from ._check_instance_web_terminal_response import CheckInstanceWebTerminalResponse
from ._create_algorithm_request import CreateAlgorithmRequest
from ._create_algorithm_response_body import CreateAlgorithmResponseBody
from ._create_algorithm_response import CreateAlgorithmResponse
from ._create_algorithm_version_request import CreateAlgorithmVersionRequest
from ._create_algorithm_version_shrink_request import CreateAlgorithmVersionShrinkRequest
from ._create_algorithm_version_response_body import CreateAlgorithmVersionResponseBody
from ._create_algorithm_version_response import CreateAlgorithmVersionResponse
from ._create_instance_web_terminal_response_body import CreateInstanceWebTerminalResponseBody
from ._create_instance_web_terminal_response import CreateInstanceWebTerminalResponse
from ._create_quota_request import CreateQuotaRequest
from ._create_quota_response_body import CreateQuotaResponseBody
from ._create_quota_response import CreateQuotaResponse
from ._create_resource_group_request import CreateResourceGroupRequest
from ._create_resource_group_response_body import CreateResourceGroupResponseBody
from ._create_resource_group_response import CreateResourceGroupResponse
from ._create_training_job_request import CreateTrainingJobRequest
from ._create_training_job_response_body import CreateTrainingJobResponseBody
from ._create_training_job_response import CreateTrainingJobResponse
from ._delete_algorithm_response_body import DeleteAlgorithmResponseBody
from ._delete_algorithm_response import DeleteAlgorithmResponse
from ._delete_algorithm_version_response_body import DeleteAlgorithmVersionResponseBody
from ._delete_algorithm_version_response import DeleteAlgorithmVersionResponse
from ._delete_machine_group_response_body import DeleteMachineGroupResponseBody
from ._delete_machine_group_response import DeleteMachineGroupResponse
from ._delete_quota_response_body import DeleteQuotaResponseBody
from ._delete_quota_response import DeleteQuotaResponse
from ._delete_resource_group_response_body import DeleteResourceGroupResponseBody
from ._delete_resource_group_response import DeleteResourceGroupResponse
from ._delete_resource_group_machine_group_response_body import DeleteResourceGroupMachineGroupResponseBody
from ._delete_resource_group_machine_group_response import DeleteResourceGroupMachineGroupResponse
from ._delete_training_job_response_body import DeleteTrainingJobResponseBody
from ._delete_training_job_response import DeleteTrainingJobResponse
from ._delete_training_job_labels_request import DeleteTrainingJobLabelsRequest
from ._delete_training_job_labels_response_body import DeleteTrainingJobLabelsResponseBody
from ._delete_training_job_labels_response import DeleteTrainingJobLabelsResponse
from ._get_algorithm_response_body import GetAlgorithmResponseBody
from ._get_algorithm_response import GetAlgorithmResponse
from ._get_algorithm_version_response_body import GetAlgorithmVersionResponseBody
from ._get_algorithm_version_response import GetAlgorithmVersionResponse
from ._get_machine_group_response_body import GetMachineGroupResponseBody
from ._get_machine_group_response import GetMachineGroupResponse
from ._get_node_metrics_request import GetNodeMetricsRequest
from ._get_node_metrics_response_body import GetNodeMetricsResponseBody
from ._get_node_metrics_response import GetNodeMetricsResponse
from ._get_quota_request import GetQuotaRequest
from ._get_quota_response_body import GetQuotaResponseBody
from ._get_quota_response import GetQuotaResponse
from ._get_resource_group_request import GetResourceGroupRequest
from ._get_resource_group_shrink_request import GetResourceGroupShrinkRequest
from ._get_resource_group_response_body import GetResourceGroupResponseBody
from ._get_resource_group_response import GetResourceGroupResponse
from ._get_resource_group_machine_group_request import GetResourceGroupMachineGroupRequest
from ._get_resource_group_machine_group_shrink_request import GetResourceGroupMachineGroupShrinkRequest
from ._get_resource_group_machine_group_response_body import GetResourceGroupMachineGroupResponseBody
from ._get_resource_group_machine_group_response import GetResourceGroupMachineGroupResponse
from ._get_resource_group_request_request import GetResourceGroupRequestRequest
from ._get_resource_group_request_response_body import GetResourceGroupRequestResponseBody
from ._get_resource_group_request_response import GetResourceGroupRequestResponse
from ._get_resource_group_total_request import GetResourceGroupTotalRequest
from ._get_resource_group_total_response_body import GetResourceGroupTotalResponseBody
from ._get_resource_group_total_response import GetResourceGroupTotalResponse
from ._get_spot_price_history_request import GetSpotPriceHistoryRequest
from ._get_spot_price_history_response_body import GetSpotPriceHistoryResponseBody
from ._get_spot_price_history_response import GetSpotPriceHistoryResponse
from ._get_token_request import GetTokenRequest
from ._get_token_response_body import GetTokenResponseBody
from ._get_token_response import GetTokenResponse
from ._get_training_job_response_body import GetTrainingJobResponseBody
from ._get_training_job_response import GetTrainingJobResponse
from ._get_training_job_error_info_response_body import GetTrainingJobErrorInfoResponseBody
from ._get_training_job_error_info_response import GetTrainingJobErrorInfoResponse
from ._get_training_job_latest_metrics_request import GetTrainingJobLatestMetricsRequest
from ._get_training_job_latest_metrics_response_body import GetTrainingJobLatestMetricsResponseBody
from ._get_training_job_latest_metrics_response import GetTrainingJobLatestMetricsResponse
from ._get_user_view_metrics_request import GetUserViewMetricsRequest
from ._get_user_view_metrics_response_body import GetUserViewMetricsResponseBody
from ._get_user_view_metrics_response import GetUserViewMetricsResponse
from ._list_algorithm_versions_request import ListAlgorithmVersionsRequest
from ._list_algorithm_versions_response_body import ListAlgorithmVersionsResponseBody
from ._list_algorithm_versions_response import ListAlgorithmVersionsResponse
from ._list_algorithms_request import ListAlgorithmsRequest
from ._list_algorithms_response_body import ListAlgorithmsResponseBody
from ._list_algorithms_response import ListAlgorithmsResponse
from ._list_nodes_request import ListNodesRequest
from ._list_nodes_shrink_request import ListNodesShrinkRequest
from ._list_nodes_response_body import ListNodesResponseBody
from ._list_nodes_response import ListNodesResponse
from ._list_quota_workloads_request import ListQuotaWorkloadsRequest
from ._list_quota_workloads_response_body import ListQuotaWorkloadsResponseBody
from ._list_quota_workloads_response import ListQuotaWorkloadsResponse
from ._list_quotas_request import ListQuotasRequest
from ._list_quotas_response_body import ListQuotasResponseBody
from ._list_quotas_response import ListQuotasResponse
from ._list_resource_group_machine_groups_request import ListResourceGroupMachineGroupsRequest
from ._list_resource_group_machine_groups_response_body import ListResourceGroupMachineGroupsResponseBody
from ._list_resource_group_machine_groups_response import ListResourceGroupMachineGroupsResponse
from ._list_resource_groups_request import ListResourceGroupsRequest
from ._list_resource_groups_response_body import ListResourceGroupsResponseBody
from ._list_resource_groups_response import ListResourceGroupsResponse
from ._list_tag_resources_request import ListTagResourcesRequest
from ._list_tag_resources_shrink_request import ListTagResourcesShrinkRequest
from ._list_tag_resources_response_body import ListTagResourcesResponseBody
from ._list_tag_resources_response import ListTagResourcesResponse
from ._list_training_job_events_request import ListTrainingJobEventsRequest
from ._list_training_job_events_response_body import ListTrainingJobEventsResponseBody
from ._list_training_job_events_response import ListTrainingJobEventsResponse
from ._list_training_job_instance_events_request import ListTrainingJobInstanceEventsRequest
from ._list_training_job_instance_events_response_body import ListTrainingJobInstanceEventsResponseBody
from ._list_training_job_instance_events_response import ListTrainingJobInstanceEventsResponse
from ._list_training_job_instance_metrics_request import ListTrainingJobInstanceMetricsRequest
from ._list_training_job_instance_metrics_response_body import ListTrainingJobInstanceMetricsResponseBody
from ._list_training_job_instance_metrics_response import ListTrainingJobInstanceMetricsResponse
from ._list_training_job_logs_request import ListTrainingJobLogsRequest
from ._list_training_job_logs_response_body import ListTrainingJobLogsResponseBody
from ._list_training_job_logs_response import ListTrainingJobLogsResponse
from ._list_training_job_metrics_request import ListTrainingJobMetricsRequest
from ._list_training_job_metrics_response_body import ListTrainingJobMetricsResponseBody
from ._list_training_job_metrics_response import ListTrainingJobMetricsResponse
from ._list_training_job_output_models_response_body import ListTrainingJobOutputModelsResponseBody
from ._list_training_job_output_models_response import ListTrainingJobOutputModelsResponse
from ._list_training_jobs_request import ListTrainingJobsRequest
from ._list_training_jobs_shrink_request import ListTrainingJobsShrinkRequest
from ._list_training_jobs_response_body import ListTrainingJobsResponseBody
from ._list_training_jobs_response import ListTrainingJobsResponse
from ._operate_node_request import OperateNodeRequest
from ._operate_node_response_body import OperateNodeResponseBody
from ._operate_node_response import OperateNodeResponse
from ._scale_quota_request import ScaleQuotaRequest
from ._scale_quota_response_body import ScaleQuotaResponseBody
from ._scale_quota_response import ScaleQuotaResponse
from ._stop_training_job_response_body import StopTrainingJobResponseBody
from ._stop_training_job_response import StopTrainingJobResponse
from ._tag_resources_request import TagResourcesRequest
from ._tag_resources_response_body import TagResourcesResponseBody
from ._tag_resources_response import TagResourcesResponse
from ._untag_resources_request import UntagResourcesRequest
from ._untag_resources_shrink_request import UntagResourcesShrinkRequest
from ._untag_resources_response_body import UntagResourcesResponseBody
from ._untag_resources_response import UntagResourcesResponse
from ._update_algorithm_request import UpdateAlgorithmRequest
from ._update_algorithm_response_body import UpdateAlgorithmResponseBody
from ._update_algorithm_response import UpdateAlgorithmResponse
from ._update_algorithm_version_request import UpdateAlgorithmVersionRequest
from ._update_algorithm_version_shrink_request import UpdateAlgorithmVersionShrinkRequest
from ._update_algorithm_version_response_body import UpdateAlgorithmVersionResponseBody
from ._update_algorithm_version_response import UpdateAlgorithmVersionResponse
from ._update_quota_request import UpdateQuotaRequest
from ._update_quota_response_body import UpdateQuotaResponseBody
from ._update_quota_response import UpdateQuotaResponse
from ._update_resource_group_request import UpdateResourceGroupRequest
from ._update_resource_group_response_body import UpdateResourceGroupResponseBody
from ._update_resource_group_response import UpdateResourceGroupResponse
from ._update_training_job_labels_request import UpdateTrainingJobLabelsRequest
from ._update_training_job_labels_response_body import UpdateTrainingJobLabelsResponseBody
from ._update_training_job_labels_response import UpdateTrainingJobLabelsResponse
from ._algorithm_spec import AlgorithmSpecComputeResourcePolicy
from ._algorithm_spec import AlgorithmSpecComputeResource
from ._algorithm_spec import AlgorithmSpecCustomization
from ._algorithm_spec import AlgorithmSpecProgressDefinitionsOverallProgress
from ._algorithm_spec import AlgorithmSpecProgressDefinitionsRemainingTime
from ._algorithm_spec import AlgorithmSpecProgressDefinitions
from ._features import FeaturesQuota
from ._node_snapshot import NodeSnapshotWorkloads
from ._node_statistics import NodeStatisticsGPUDetails
from ._node_statistics import NodeStatisticsHyperNodeDetails
from ._quota_user import QuotaUserResources
from ._create_resource_group_request import CreateResourceGroupRequestTag
from ._create_training_job_request import CreateTrainingJobRequestComputeResourceInstanceSpec
from ._create_training_job_request import CreateTrainingJobRequestComputeResourceSpotSpec
from ._create_training_job_request import CreateTrainingJobRequestComputeResource
from ._create_training_job_request import CreateTrainingJobRequestExperimentConfig
from ._create_training_job_request import CreateTrainingJobRequestHyperParameters
from ._create_training_job_request import CreateTrainingJobRequestInputChannels
from ._create_training_job_request import CreateTrainingJobRequestLabels
from ._create_training_job_request import CreateTrainingJobRequestOutputChannels
from ._create_training_job_request import CreateTrainingJobRequestScheduler
from ._create_training_job_request import CreateTrainingJobRequestUserVpc
from ._get_resource_group_request import GetResourceGroupRequestTag
from ._get_resource_group_response_body import GetResourceGroupResponseBodyTags
from ._get_resource_group_machine_group_request import GetResourceGroupMachineGroupRequestTag
from ._get_resource_group_machine_group_response_body import GetResourceGroupMachineGroupResponseBodyTags
from ._get_training_job_response_body import GetTrainingJobResponseBodyComputeResourceInstanceSpec
from ._get_training_job_response_body import GetTrainingJobResponseBodyComputeResourceSpotSpec
from ._get_training_job_response_body import GetTrainingJobResponseBodyComputeResource
from ._get_training_job_response_body import GetTrainingJobResponseBodyExperimentConfig
from ._get_training_job_response_body import GetTrainingJobResponseBodyHyperParameters
from ._get_training_job_response_body import GetTrainingJobResponseBodyInputChannels
from ._get_training_job_response_body import GetTrainingJobResponseBodyInstances
from ._get_training_job_response_body import GetTrainingJobResponseBodyLabels
from ._get_training_job_response_body import GetTrainingJobResponseBodyLatestMetrics
from ._get_training_job_response_body import GetTrainingJobResponseBodyLatestProgressOverallProgress
from ._get_training_job_response_body import GetTrainingJobResponseBodyLatestProgressRemainingTime
from ._get_training_job_response_body import GetTrainingJobResponseBodyLatestProgress
from ._get_training_job_response_body import GetTrainingJobResponseBodyOutputChannels
from ._get_training_job_response_body import GetTrainingJobResponseBodyOutputModel
from ._get_training_job_response_body import GetTrainingJobResponseBodyScheduler
from ._get_training_job_response_body import GetTrainingJobResponseBodyStatusTransitions
from ._get_training_job_response_body import GetTrainingJobResponseBodyUserVpc
from ._get_training_job_error_info_response_body import GetTrainingJobErrorInfoResponseBodyErrorInfo
from ._get_training_job_latest_metrics_response_body import GetTrainingJobLatestMetricsResponseBodyMetrics
from ._list_algorithm_versions_response_body import ListAlgorithmVersionsResponseBodyAlgorithmVersions
from ._list_algorithms_response_body import ListAlgorithmsResponseBodyAlgorithms
from ._list_nodes_request import ListNodesRequestHealthCount
from ._list_nodes_request import ListNodesRequestHealthRate
from ._list_tag_resources_request import ListTagResourcesRequestTag
from ._list_tag_resources_response_body import ListTagResourcesResponseBodyTagResources
from ._list_training_job_instance_metrics_response_body import ListTrainingJobInstanceMetricsResponseBodyInstanceMetricsMetrics
from ._list_training_job_instance_metrics_response_body import ListTrainingJobInstanceMetricsResponseBodyInstanceMetrics
from ._list_training_job_metrics_response_body import ListTrainingJobMetricsResponseBodyMetrics
from ._list_training_job_output_models_response_body import ListTrainingJobOutputModelsResponseBodyOutputModelsLabels
from ._list_training_job_output_models_response_body import ListTrainingJobOutputModelsResponseBodyOutputModels
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsComputeResourceInstanceSpec
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsComputeResource
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsExperimentConfig
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsHyperParameters
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsInputChannels
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsLabels
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsOutputChannels
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsScheduler
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsStatusTransitions
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobsUserVpc
from ._list_training_jobs_response_body import ListTrainingJobsResponseBodyTrainingJobs
from ._tag_resources_request import TagResourcesRequestTag
from ._update_training_job_labels_request import UpdateTrainingJobLabelsRequestLabels

__all__ = [
    ACS,
    Action,
    AlgorithmSpec,
    AllocateStrategySpec,
    AssignNodeSpec,
    BindingPolicy,
    CacheInfo,
    CacheService,
    CapacityLock,
    Channel,
    ChannelProperty,
    ClusterSpec,
    ComponentSpec,
    ConditionExpression,
    DataSource,
    EcsSpec,
    EniCacheConfig,
    Features,
    ForwardInfo,
    GPUInfo,
    GPUMetric,
    HyperParameterDefinition,
    HyperParameterRange,
    JobSettings,
    JobViewMetric,
    Label,
    Location,
    MachineGroup,
    Metric,
    MetricDefinition,
    Node,
    NodeCordonParameters,
    NodeDrainParameters,
    NodeGPUMetric,
    NodeMetric,
    NodeOperationParameters,
    NodeOperationResult,
    NodePodInfo,
    NodeSnapshot,
    NodeSpec,
    NodeStatistics,
    NodeType,
    NodeTypeStatistic,
    NodeUncordonParameters,
    NodeViewMetric,
    OversoldUsageConfig,
    Permission,
    QueueInfo,
    Quota,
    QuotaCluster,
    QuotaConfig,
    QuotaDetails,
    QuotaIdName,
    QuotaJob,
    QuotaJobViewMetric,
    QuotaMetric,
    QuotaNodeViewMetric,
    QuotaTopo,
    QuotaUser,
    QuotaUserViewMetric,
    ResourceAmount,
    ResourceDiagnosisDetail,
    ResourceGroup,
    ResourceGroupMetric,
    ResourceInfo,
    ResourceInfos,
    ResourceLimitDetails,
    ResourceOperation,
    ResourceSpec,
    Rules,
    SandboxCacheConfig,
    SchedulingRule,
    SelfQuotaPreemptionConfig,
    SpotPriceItem,
    SpotStockPreview,
    StatisticsDetails,
    StatisticsResources,
    SubQuotaPreemptionConfig,
    Task,
    TaskInstance,
    TaskInstanceEvent,
    TimeRangeFilter,
    UnschedulableNodeDetail,
    UserInfo,
    UserQuotaPermission,
    UserViewMetric,
    UserVpc,
    WorkloadDetails,
    WorkspaceIdName,
    WorkspaceSpec,
    WorkspaceSpecs,
    CheckInstanceWebTerminalRequest,
    CheckInstanceWebTerminalResponseBody,
    CheckInstanceWebTerminalResponse,
    CreateAlgorithmRequest,
    CreateAlgorithmResponseBody,
    CreateAlgorithmResponse,
    CreateAlgorithmVersionRequest,
    CreateAlgorithmVersionShrinkRequest,
    CreateAlgorithmVersionResponseBody,
    CreateAlgorithmVersionResponse,
    CreateInstanceWebTerminalResponseBody,
    CreateInstanceWebTerminalResponse,
    CreateQuotaRequest,
    CreateQuotaResponseBody,
    CreateQuotaResponse,
    CreateResourceGroupRequest,
    CreateResourceGroupResponseBody,
    CreateResourceGroupResponse,
    CreateTrainingJobRequest,
    CreateTrainingJobResponseBody,
    CreateTrainingJobResponse,
    DeleteAlgorithmResponseBody,
    DeleteAlgorithmResponse,
    DeleteAlgorithmVersionResponseBody,
    DeleteAlgorithmVersionResponse,
    DeleteMachineGroupResponseBody,
    DeleteMachineGroupResponse,
    DeleteQuotaResponseBody,
    DeleteQuotaResponse,
    DeleteResourceGroupResponseBody,
    DeleteResourceGroupResponse,
    DeleteResourceGroupMachineGroupResponseBody,
    DeleteResourceGroupMachineGroupResponse,
    DeleteTrainingJobResponseBody,
    DeleteTrainingJobResponse,
    DeleteTrainingJobLabelsRequest,
    DeleteTrainingJobLabelsResponseBody,
    DeleteTrainingJobLabelsResponse,
    GetAlgorithmResponseBody,
    GetAlgorithmResponse,
    GetAlgorithmVersionResponseBody,
    GetAlgorithmVersionResponse,
    GetMachineGroupResponseBody,
    GetMachineGroupResponse,
    GetNodeMetricsRequest,
    GetNodeMetricsResponseBody,
    GetNodeMetricsResponse,
    GetQuotaRequest,
    GetQuotaResponseBody,
    GetQuotaResponse,
    GetResourceGroupRequest,
    GetResourceGroupShrinkRequest,
    GetResourceGroupResponseBody,
    GetResourceGroupResponse,
    GetResourceGroupMachineGroupRequest,
    GetResourceGroupMachineGroupShrinkRequest,
    GetResourceGroupMachineGroupResponseBody,
    GetResourceGroupMachineGroupResponse,
    GetResourceGroupRequestRequest,
    GetResourceGroupRequestResponseBody,
    GetResourceGroupRequestResponse,
    GetResourceGroupTotalRequest,
    GetResourceGroupTotalResponseBody,
    GetResourceGroupTotalResponse,
    GetSpotPriceHistoryRequest,
    GetSpotPriceHistoryResponseBody,
    GetSpotPriceHistoryResponse,
    GetTokenRequest,
    GetTokenResponseBody,
    GetTokenResponse,
    GetTrainingJobResponseBody,
    GetTrainingJobResponse,
    GetTrainingJobErrorInfoResponseBody,
    GetTrainingJobErrorInfoResponse,
    GetTrainingJobLatestMetricsRequest,
    GetTrainingJobLatestMetricsResponseBody,
    GetTrainingJobLatestMetricsResponse,
    GetUserViewMetricsRequest,
    GetUserViewMetricsResponseBody,
    GetUserViewMetricsResponse,
    ListAlgorithmVersionsRequest,
    ListAlgorithmVersionsResponseBody,
    ListAlgorithmVersionsResponse,
    ListAlgorithmsRequest,
    ListAlgorithmsResponseBody,
    ListAlgorithmsResponse,
    ListNodesRequest,
    ListNodesShrinkRequest,
    ListNodesResponseBody,
    ListNodesResponse,
    ListQuotaWorkloadsRequest,
    ListQuotaWorkloadsResponseBody,
    ListQuotaWorkloadsResponse,
    ListQuotasRequest,
    ListQuotasResponseBody,
    ListQuotasResponse,
    ListResourceGroupMachineGroupsRequest,
    ListResourceGroupMachineGroupsResponseBody,
    ListResourceGroupMachineGroupsResponse,
    ListResourceGroupsRequest,
    ListResourceGroupsResponseBody,
    ListResourceGroupsResponse,
    ListTagResourcesRequest,
    ListTagResourcesShrinkRequest,
    ListTagResourcesResponseBody,
    ListTagResourcesResponse,
    ListTrainingJobEventsRequest,
    ListTrainingJobEventsResponseBody,
    ListTrainingJobEventsResponse,
    ListTrainingJobInstanceEventsRequest,
    ListTrainingJobInstanceEventsResponseBody,
    ListTrainingJobInstanceEventsResponse,
    ListTrainingJobInstanceMetricsRequest,
    ListTrainingJobInstanceMetricsResponseBody,
    ListTrainingJobInstanceMetricsResponse,
    ListTrainingJobLogsRequest,
    ListTrainingJobLogsResponseBody,
    ListTrainingJobLogsResponse,
    ListTrainingJobMetricsRequest,
    ListTrainingJobMetricsResponseBody,
    ListTrainingJobMetricsResponse,
    ListTrainingJobOutputModelsResponseBody,
    ListTrainingJobOutputModelsResponse,
    ListTrainingJobsRequest,
    ListTrainingJobsShrinkRequest,
    ListTrainingJobsResponseBody,
    ListTrainingJobsResponse,
    OperateNodeRequest,
    OperateNodeResponseBody,
    OperateNodeResponse,
    ScaleQuotaRequest,
    ScaleQuotaResponseBody,
    ScaleQuotaResponse,
    StopTrainingJobResponseBody,
    StopTrainingJobResponse,
    TagResourcesRequest,
    TagResourcesResponseBody,
    TagResourcesResponse,
    UntagResourcesRequest,
    UntagResourcesShrinkRequest,
    UntagResourcesResponseBody,
    UntagResourcesResponse,
    UpdateAlgorithmRequest,
    UpdateAlgorithmResponseBody,
    UpdateAlgorithmResponse,
    UpdateAlgorithmVersionRequest,
    UpdateAlgorithmVersionShrinkRequest,
    UpdateAlgorithmVersionResponseBody,
    UpdateAlgorithmVersionResponse,
    UpdateQuotaRequest,
    UpdateQuotaResponseBody,
    UpdateQuotaResponse,
    UpdateResourceGroupRequest,
    UpdateResourceGroupResponseBody,
    UpdateResourceGroupResponse,
    UpdateTrainingJobLabelsRequest,
    UpdateTrainingJobLabelsResponseBody,
    UpdateTrainingJobLabelsResponse,
    AlgorithmSpecComputeResourcePolicy,
    AlgorithmSpecComputeResource,
    AlgorithmSpecCustomization,
    AlgorithmSpecProgressDefinitionsOverallProgress,
    AlgorithmSpecProgressDefinitionsRemainingTime,
    AlgorithmSpecProgressDefinitions,
    FeaturesQuota,
    NodeSnapshotWorkloads,
    NodeStatisticsGPUDetails,
    NodeStatisticsHyperNodeDetails,
    QuotaUserResources,
    CreateResourceGroupRequestTag,
    CreateTrainingJobRequestComputeResourceInstanceSpec,
    CreateTrainingJobRequestComputeResourceSpotSpec,
    CreateTrainingJobRequestComputeResource,
    CreateTrainingJobRequestExperimentConfig,
    CreateTrainingJobRequestHyperParameters,
    CreateTrainingJobRequestInputChannels,
    CreateTrainingJobRequestLabels,
    CreateTrainingJobRequestOutputChannels,
    CreateTrainingJobRequestScheduler,
    CreateTrainingJobRequestUserVpc,
    GetResourceGroupRequestTag,
    GetResourceGroupResponseBodyTags,
    GetResourceGroupMachineGroupRequestTag,
    GetResourceGroupMachineGroupResponseBodyTags,
    GetTrainingJobResponseBodyComputeResourceInstanceSpec,
    GetTrainingJobResponseBodyComputeResourceSpotSpec,
    GetTrainingJobResponseBodyComputeResource,
    GetTrainingJobResponseBodyExperimentConfig,
    GetTrainingJobResponseBodyHyperParameters,
    GetTrainingJobResponseBodyInputChannels,
    GetTrainingJobResponseBodyInstances,
    GetTrainingJobResponseBodyLabels,
    GetTrainingJobResponseBodyLatestMetrics,
    GetTrainingJobResponseBodyLatestProgressOverallProgress,
    GetTrainingJobResponseBodyLatestProgressRemainingTime,
    GetTrainingJobResponseBodyLatestProgress,
    GetTrainingJobResponseBodyOutputChannels,
    GetTrainingJobResponseBodyOutputModel,
    GetTrainingJobResponseBodyScheduler,
    GetTrainingJobResponseBodyStatusTransitions,
    GetTrainingJobResponseBodyUserVpc,
    GetTrainingJobErrorInfoResponseBodyErrorInfo,
    GetTrainingJobLatestMetricsResponseBodyMetrics,
    ListAlgorithmVersionsResponseBodyAlgorithmVersions,
    ListAlgorithmsResponseBodyAlgorithms,
    ListNodesRequestHealthCount,
    ListNodesRequestHealthRate,
    ListTagResourcesRequestTag,
    ListTagResourcesResponseBodyTagResources,
    ListTrainingJobInstanceMetricsResponseBodyInstanceMetricsMetrics,
    ListTrainingJobInstanceMetricsResponseBodyInstanceMetrics,
    ListTrainingJobMetricsResponseBodyMetrics,
    ListTrainingJobOutputModelsResponseBodyOutputModelsLabels,
    ListTrainingJobOutputModelsResponseBodyOutputModels,
    ListTrainingJobsResponseBodyTrainingJobsComputeResourceInstanceSpec,
    ListTrainingJobsResponseBodyTrainingJobsComputeResource,
    ListTrainingJobsResponseBodyTrainingJobsExperimentConfig,
    ListTrainingJobsResponseBodyTrainingJobsHyperParameters,
    ListTrainingJobsResponseBodyTrainingJobsInputChannels,
    ListTrainingJobsResponseBodyTrainingJobsLabels,
    ListTrainingJobsResponseBodyTrainingJobsOutputChannels,
    ListTrainingJobsResponseBodyTrainingJobsScheduler,
    ListTrainingJobsResponseBodyTrainingJobsStatusTransitions,
    ListTrainingJobsResponseBodyTrainingJobsUserVpc,
    ListTrainingJobsResponseBodyTrainingJobs,
    TagResourcesRequestTag,
    UpdateTrainingJobLabelsRequestLabels
]
