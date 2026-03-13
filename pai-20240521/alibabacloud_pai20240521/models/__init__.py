# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._acs import ACS
from ._action import Action
from ._algorithm_spec import AlgorithmSpec
from ._allocate_strategy_spec import AllocateStrategySpec
from ._cache_service import CacheService
from ._channel import Channel
from ._channel_property import ChannelProperty
from ._component_spec import ComponentSpec
from ._condition_expression import ConditionExpression
from ._features import Features
from ._filter import Filter
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
from ._model_version import ModelVersion
from ._node import Node
from ._node_gpumetric import NodeGPUMetric
from ._node_metric import NodeMetric
from ._node_pod_info import NodePodInfo
from ._node_snapshot import NodeSnapshot
from ._node_spec import NodeSpec
from ._node_type import NodeType
from ._node_type_statistic import NodeTypeStatistic
from ._node_view_metric import NodeViewMetric
from ._permission import Permission
from ._queue_info import QueueInfo
from ._quick_start_model import QuickStartModel
from ._quota import Quota
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
from ._resource_limit_details import ResourceLimitDetails
from ._resource_operation import ResourceOperation
from ._resource_spec import ResourceSpec
from ._rules import Rules
from ._scheduling_rule import SchedulingRule
from ._spot_price_item import SpotPriceItem
from ._spot_stock_preview import SpotStockPreview
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
from ._get_user_ali_uid_by_instance_id_request import GetUserAliUidByInstanceIdRequest
from ._get_user_ali_uid_by_instance_id_response_body import GetUserAliUidByInstanceIdResponseBody
from ._get_user_ali_uid_by_instance_id_response import GetUserAliUidByInstanceIdResponse
from ._get_user_view_metrics_request import GetUserViewMetricsRequest
from ._get_user_view_metrics_response_body import GetUserViewMetricsResponseBody
from ._get_user_view_metrics_response import GetUserViewMetricsResponse
from ._list_data_cache_services_request import ListDataCacheServicesRequest
from ._list_data_cache_services_response_body import ListDataCacheServicesResponseBody
from ._list_data_cache_services_response import ListDataCacheServicesResponse
from ._list_nodes_request import ListNodesRequest
from ._list_nodes_shrink_request import ListNodesShrinkRequest
from ._list_nodes_response_body import ListNodesResponseBody
from ._list_nodes_response import ListNodesResponse
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
from ._tag_resources_system_tags_request import TagResourcesSystemTagsRequest
from ._tag_resources_system_tags_response_body import TagResourcesSystemTagsResponseBody
from ._tag_resources_system_tags_response import TagResourcesSystemTagsResponse
from ._untag_resources_system_tags_request import UntagResourcesSystemTagsRequest
from ._untag_resources_system_tags_shrink_request import UntagResourcesSystemTagsShrinkRequest
from ._untag_resources_system_tags_response_body import UntagResourcesSystemTagsResponseBody
from ._untag_resources_system_tags_response import UntagResourcesSystemTagsResponse
from ._algorithm_spec import AlgorithmSpecComputeResourcePolicy
from ._algorithm_spec import AlgorithmSpecComputeResource
from ._algorithm_spec import AlgorithmSpecCustomization
from ._algorithm_spec import AlgorithmSpecProgressDefinitionsOverallProgress
from ._algorithm_spec import AlgorithmSpecProgressDefinitionsRemainingTime
from ._algorithm_spec import AlgorithmSpecProgressDefinitions
from ._features import FeaturesQuota
from ._node_snapshot import NodeSnapshotWorkloads
from ._quota_user import QuotaUserResources
from ._get_resource_group_request import GetResourceGroupRequestTag
from ._get_resource_group_response_body import GetResourceGroupResponseBodyTags
from ._get_resource_group_machine_group_request import GetResourceGroupMachineGroupRequestTag
from ._get_resource_group_machine_group_response_body import GetResourceGroupMachineGroupResponseBodyTags
from ._list_nodes_request import ListNodesRequestHealthCount
from ._list_nodes_request import ListNodesRequestHealthRate
from ._list_tag_resources_request import ListTagResourcesRequestTag
from ._list_tag_resources_response_body import ListTagResourcesResponseBodyTagResources
from ._tag_resources_system_tags_request import TagResourcesSystemTagsRequestTag

__all__ = [
    ACS,
    Action,
    AlgorithmSpec,
    AllocateStrategySpec,
    CacheService,
    Channel,
    ChannelProperty,
    ComponentSpec,
    ConditionExpression,
    Features,
    Filter,
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
    ModelVersion,
    Node,
    NodeGPUMetric,
    NodeMetric,
    NodePodInfo,
    NodeSnapshot,
    NodeSpec,
    NodeType,
    NodeTypeStatistic,
    NodeViewMetric,
    Permission,
    QueueInfo,
    QuickStartModel,
    Quota,
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
    ResourceLimitDetails,
    ResourceOperation,
    ResourceSpec,
    Rules,
    SchedulingRule,
    SpotPriceItem,
    SpotStockPreview,
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
    GetUserAliUidByInstanceIdRequest,
    GetUserAliUidByInstanceIdResponseBody,
    GetUserAliUidByInstanceIdResponse,
    GetUserViewMetricsRequest,
    GetUserViewMetricsResponseBody,
    GetUserViewMetricsResponse,
    ListDataCacheServicesRequest,
    ListDataCacheServicesResponseBody,
    ListDataCacheServicesResponse,
    ListNodesRequest,
    ListNodesShrinkRequest,
    ListNodesResponseBody,
    ListNodesResponse,
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
    TagResourcesSystemTagsRequest,
    TagResourcesSystemTagsResponseBody,
    TagResourcesSystemTagsResponse,
    UntagResourcesSystemTagsRequest,
    UntagResourcesSystemTagsShrinkRequest,
    UntagResourcesSystemTagsResponseBody,
    UntagResourcesSystemTagsResponse,
    AlgorithmSpecComputeResourcePolicy,
    AlgorithmSpecComputeResource,
    AlgorithmSpecCustomization,
    AlgorithmSpecProgressDefinitionsOverallProgress,
    AlgorithmSpecProgressDefinitionsRemainingTime,
    AlgorithmSpecProgressDefinitions,
    FeaturesQuota,
    NodeSnapshotWorkloads,
    QuotaUserResources,
    GetResourceGroupRequestTag,
    GetResourceGroupResponseBodyTags,
    GetResourceGroupMachineGroupRequestTag,
    GetResourceGroupMachineGroupResponseBodyTags,
    ListNodesRequestHealthCount,
    ListNodesRequestHealthRate,
    ListTagResourcesRequestTag,
    ListTagResourcesResponseBodyTagResources,
    TagResourcesSystemTagsRequestTag
]
