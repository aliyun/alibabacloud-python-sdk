# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._endpoint_status import EndpointStatus
from ._endpoint_status_detail import EndpointStatusDetail
from ._instance_life_cycle import InstanceLifeCycle
from ._instance_status import InstanceStatus
from ._ip_port import IpPort
from ._metric import Metric
from ._slot_life_cycle import SlotLifeCycle
from ._slot_status import SlotStatus
from ._slot_status_detail import SlotStatusDetail
from ._bind_endpoint_response_body import BindEndpointResponseBody
from ._bind_endpoint_response import BindEndpointResponse
from ._create_endpoint_request import CreateEndpointRequest
from ._create_endpoint_response_body import CreateEndpointResponseBody
from ._create_endpoint_response import CreateEndpointResponse
from ._create_instance_request import CreateInstanceRequest
from ._create_instance_response_body import CreateInstanceResponseBody
from ._create_instance_response import CreateInstanceResponse
from ._create_slot_request import CreateSlotRequest
from ._create_slot_response_body import CreateSlotResponseBody
from ._create_slot_response import CreateSlotResponse
from ._create_slots_request import CreateSlotsRequest
from ._create_slots_response_body import CreateSlotsResponseBody
from ._create_slots_response import CreateSlotsResponse
from ._create_tag_request import CreateTagRequest
from ._create_tag_response_body import CreateTagResponseBody
from ._create_tag_response import CreateTagResponse
from ._delete_endpoint_response_body import DeleteEndpointResponseBody
from ._delete_endpoint_response import DeleteEndpointResponse
from ._delete_instance_response_body import DeleteInstanceResponseBody
from ._delete_instance_response import DeleteInstanceResponse
from ._delete_slot_request import DeleteSlotRequest
from ._delete_slot_response_body import DeleteSlotResponseBody
from ._delete_slot_response import DeleteSlotResponse
from ._delete_tag_request import DeleteTagRequest
from ._delete_tag_response_body import DeleteTagResponseBody
from ._delete_tag_response import DeleteTagResponse
from ._describe_component_request import DescribeComponentRequest
from ._describe_component_shrink_request import DescribeComponentShrinkRequest
from ._describe_component_response_body import DescribeComponentResponseBody
from ._describe_component_response import DescribeComponentResponse
from ._describe_endpoint_response_body import DescribeEndpointResponseBody
from ._describe_endpoint_response import DescribeEndpointResponse
from ._describe_instance_response_body import DescribeInstanceResponseBody
from ._describe_instance_response import DescribeInstanceResponse
from ._describe_slot_response_body import DescribeSlotResponseBody
from ._describe_slot_response import DescribeSlotResponse
from ._list_components_request import ListComponentsRequest
from ._list_components_response_body import ListComponentsResponseBody
from ._list_components_response import ListComponentsResponse
from ._list_endpoints_request import ListEndpointsRequest
from ._list_endpoints_response_body import ListEndpointsResponseBody
from ._list_endpoints_response import ListEndpointsResponse
from ._list_instances_request import ListInstancesRequest
from ._list_instances_response_body import ListInstancesResponseBody
from ._list_instances_response import ListInstancesResponse
from ._list_slots_request import ListSlotsRequest
from ._list_slots_response_body import ListSlotsResponseBody
from ._list_slots_response import ListSlotsResponse
from ._list_tags_request import ListTagsRequest
from ._list_tags_response_body import ListTagsResponseBody
from ._list_tags_response import ListTagsResponse
from ._query_instance_metrics_request import QueryInstanceMetricsRequest
from ._query_instance_metrics_shrink_request import QueryInstanceMetricsShrinkRequest
from ._query_instance_metrics_response_body import QueryInstanceMetricsResponseBody
from ._query_instance_metrics_response import QueryInstanceMetricsResponse
from ._query_slot_metrics_request import QuerySlotMetricsRequest
from ._query_slot_metrics_shrink_request import QuerySlotMetricsShrinkRequest
from ._query_slot_metrics_response_body import QuerySlotMetricsResponseBody
from ._query_slot_metrics_response import QuerySlotMetricsResponse
from ._query_statistic_request import QueryStatisticRequest
from ._query_statistic_response_body import QueryStatisticResponseBody
from ._query_statistic_response import QueryStatisticResponse
from ._reload_slot_response_body import ReloadSlotResponseBody
from ._reload_slot_response import ReloadSlotResponse
from ._stop_slot_response_body import StopSlotResponseBody
from ._stop_slot_response import StopSlotResponse
from ._unbind_endpoint_response_body import UnbindEndpointResponseBody
from ._unbind_endpoint_response import UnbindEndpointResponse
from ._update_instance_request import UpdateInstanceRequest
from ._update_instance_response_body import UpdateInstanceResponseBody
from ._update_instance_response import UpdateInstanceResponse
from ._update_slot_request import UpdateSlotRequest
from ._update_slot_response_body import UpdateSlotResponseBody
from ._update_slot_response import UpdateSlotResponse
from ._create_instance_request import CreateInstanceRequestTags
from ._create_slot_request import CreateSlotRequestEndpoints
from ._create_slot_request import CreateSlotRequestTags
from ._create_slots_request import CreateSlotsRequestSlotsTags
from ._create_slots_request import CreateSlotsRequestSlots
from ._describe_component_response_body import DescribeComponentResponseBodyTemplate
from ._describe_instance_response_body import DescribeInstanceResponseBodyTags
from ._describe_slot_response_body import DescribeSlotResponseBodyTags
from ._list_components_response_body import ListComponentsResponseBodyComponentsTemplate
from ._list_components_response_body import ListComponentsResponseBodyComponents
from ._list_endpoints_response_body import ListEndpointsResponseBodyEndpoints
from ._list_instances_response_body import ListInstancesResponseBodyInstancesTags
from ._list_instances_response_body import ListInstancesResponseBodyInstances
from ._list_slots_response_body import ListSlotsResponseBodySlotsEndpoints
from ._list_slots_response_body import ListSlotsResponseBodySlotsTags
from ._list_slots_response_body import ListSlotsResponseBodySlots
from ._list_tags_response_body import ListTagsResponseBodyTags
from ._update_slot_request import UpdateSlotRequestTags

__all__ = [
    EndpointStatus,
    EndpointStatusDetail,
    InstanceLifeCycle,
    InstanceStatus,
    IpPort,
    Metric,
    SlotLifeCycle,
    SlotStatus,
    SlotStatusDetail,
    BindEndpointResponseBody,
    BindEndpointResponse,
    CreateEndpointRequest,
    CreateEndpointResponseBody,
    CreateEndpointResponse,
    CreateInstanceRequest,
    CreateInstanceResponseBody,
    CreateInstanceResponse,
    CreateSlotRequest,
    CreateSlotResponseBody,
    CreateSlotResponse,
    CreateSlotsRequest,
    CreateSlotsResponseBody,
    CreateSlotsResponse,
    CreateTagRequest,
    CreateTagResponseBody,
    CreateTagResponse,
    DeleteEndpointResponseBody,
    DeleteEndpointResponse,
    DeleteInstanceResponseBody,
    DeleteInstanceResponse,
    DeleteSlotRequest,
    DeleteSlotResponseBody,
    DeleteSlotResponse,
    DeleteTagRequest,
    DeleteTagResponseBody,
    DeleteTagResponse,
    DescribeComponentRequest,
    DescribeComponentShrinkRequest,
    DescribeComponentResponseBody,
    DescribeComponentResponse,
    DescribeEndpointResponseBody,
    DescribeEndpointResponse,
    DescribeInstanceResponseBody,
    DescribeInstanceResponse,
    DescribeSlotResponseBody,
    DescribeSlotResponse,
    ListComponentsRequest,
    ListComponentsResponseBody,
    ListComponentsResponse,
    ListEndpointsRequest,
    ListEndpointsResponseBody,
    ListEndpointsResponse,
    ListInstancesRequest,
    ListInstancesResponseBody,
    ListInstancesResponse,
    ListSlotsRequest,
    ListSlotsResponseBody,
    ListSlotsResponse,
    ListTagsRequest,
    ListTagsResponseBody,
    ListTagsResponse,
    QueryInstanceMetricsRequest,
    QueryInstanceMetricsShrinkRequest,
    QueryInstanceMetricsResponseBody,
    QueryInstanceMetricsResponse,
    QuerySlotMetricsRequest,
    QuerySlotMetricsShrinkRequest,
    QuerySlotMetricsResponseBody,
    QuerySlotMetricsResponse,
    QueryStatisticRequest,
    QueryStatisticResponseBody,
    QueryStatisticResponse,
    ReloadSlotResponseBody,
    ReloadSlotResponse,
    StopSlotResponseBody,
    StopSlotResponse,
    UnbindEndpointResponseBody,
    UnbindEndpointResponse,
    UpdateInstanceRequest,
    UpdateInstanceResponseBody,
    UpdateInstanceResponse,
    UpdateSlotRequest,
    UpdateSlotResponseBody,
    UpdateSlotResponse,
    CreateInstanceRequestTags,
    CreateSlotRequestEndpoints,
    CreateSlotRequestTags,
    CreateSlotsRequestSlotsTags,
    CreateSlotsRequestSlots,
    DescribeComponentResponseBodyTemplate,
    DescribeInstanceResponseBodyTags,
    DescribeSlotResponseBodyTags,
    ListComponentsResponseBodyComponentsTemplate,
    ListComponentsResponseBodyComponents,
    ListEndpointsResponseBodyEndpoints,
    ListInstancesResponseBodyInstancesTags,
    ListInstancesResponseBodyInstances,
    ListSlotsResponseBodySlotsEndpoints,
    ListSlotsResponseBodySlotsTags,
    ListSlotsResponseBodySlots,
    ListTagsResponseBodyTags,
    UpdateSlotRequestTags
]
