# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._dbversion_detail import DBVersionDetail
from ._instance_detail import InstanceDetail
from ._migration_source import MigrationSource
from ._price_info import PriceInfo
from ._promotion_info import PromotionInfo
from ._change_resource_group_request import ChangeResourceGroupRequest
from ._change_resource_group_response_body import ChangeResourceGroupResponseBody
from ._change_resource_group_response import ChangeResourceGroupResponse
from ._create_default_role_response_body import CreateDefaultRoleResponseBody
from ._create_default_role_response import CreateDefaultRoleResponse
from ._create_instance_request import CreateInstanceRequest
from ._create_instance_response_body import CreateInstanceResponseBody
from ._create_instance_response import CreateInstanceResponse
from ._delete_instance_request import DeleteInstanceRequest
from ._delete_instance_response_body import DeleteInstanceResponseBody
from ._delete_instance_response import DeleteInstanceResponse
from ._describe_access_control_list_request import DescribeAccessControlListRequest
from ._describe_access_control_list_response_body import DescribeAccessControlListResponseBody
from ._describe_access_control_list_response import DescribeAccessControlListResponse
from ._describe_instance_configs_request import DescribeInstanceConfigsRequest
from ._describe_instance_configs_response_body import DescribeInstanceConfigsResponseBody
from ._describe_instance_configs_response import DescribeInstanceConfigsResponse
from ._get_instance_request import GetInstanceRequest
from ._get_instance_response_body import GetInstanceResponseBody
from ._get_instance_response import GetInstanceResponse
from ._get_instance_detail_request import GetInstanceDetailRequest
from ._get_instance_detail_response_body import GetInstanceDetailResponseBody
from ._get_instance_detail_response import GetInstanceDetailResponse
from ._list_instances_request import ListInstancesRequest
from ._list_instances_shrink_request import ListInstancesShrinkRequest
from ._list_instances_response_body import ListInstancesResponseBody
from ._list_instances_response import ListInstancesResponse
from ._list_instances_v2request import ListInstancesV2Request
from ._list_instances_v2shrink_request import ListInstancesV2ShrinkRequest
from ._list_instances_v2response_body import ListInstancesV2ResponseBody
from ._list_instances_v2response import ListInstancesV2Response
from ._modify_instance_config_request import ModifyInstanceConfigRequest
from ._modify_instance_config_response_body import ModifyInstanceConfigResponseBody
from ._modify_instance_config_response import ModifyInstanceConfigResponse
from ._tag_resources_request import TagResourcesRequest
from ._tag_resources_response_body import TagResourcesResponseBody
from ._tag_resources_response import TagResourcesResponse
from ._un_tag_resources_request import UnTagResourcesRequest
from ._un_tag_resources_shrink_request import UnTagResourcesShrinkRequest
from ._un_tag_resources_response_body import UnTagResourcesResponseBody
from ._un_tag_resources_response import UnTagResourcesResponse
from ._update_access_control_list_request import UpdateAccessControlListRequest
from ._update_access_control_list_response_body import UpdateAccessControlListResponseBody
from ._update_access_control_list_response import UpdateAccessControlListResponse
from ._update_instance_request import UpdateInstanceRequest
from ._update_instance_response_body import UpdateInstanceResponseBody
from ._update_instance_response import UpdateInstanceResponse
from ._update_instance_name_request import UpdateInstanceNameRequest
from ._update_instance_name_response_body import UpdateInstanceNameResponseBody
from ._update_instance_name_response import UpdateInstanceNameResponse
from ._update_public_network_status_request import UpdatePublicNetworkStatusRequest
from ._update_public_network_status_response_body import UpdatePublicNetworkStatusResponseBody
from ._update_public_network_status_response import UpdatePublicNetworkStatusResponse
from ._dbversion_detail import DBVersionDetailSpecsComponentSpecs
from ._dbversion_detail import DBVersionDetailSpecs
from ._instance_detail import InstanceDetailComponents
from ._instance_detail import InstanceDetailTags
from ._instance_detail import InstanceDetailVSwitchIds
from ._migration_source import MigrationSourceAuthInfo
from ._migration_source import MigrationSourceEndpoint
from ._price_info import PriceInfoPriceModules
from ._price_info import PriceInfoRules
from ._create_instance_request import CreateInstanceRequestComponents
from ._create_instance_request import CreateInstanceRequestTags
from ._create_instance_request import CreateInstanceRequestVSwitchIds
from ._create_instance_response_body import CreateInstanceResponseBodyData
from ._describe_access_control_list_response_body import DescribeAccessControlListResponseBodyData
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyDataClusterInfo
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyDataHighAvailability
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyDataMeasureConfig
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyDataTags
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyDataVSwitches
from ._get_instance_detail_response_body import GetInstanceDetailResponseBodyData
from ._list_instances_request import ListInstancesRequestTag
from ._list_instances_response_body import ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList
from ._list_instances_response_body import ListInstancesResponseBodyDataClusterInfo
from ._list_instances_response_body import ListInstancesResponseBodyDataTags
from ._list_instances_response_body import ListInstancesResponseBodyData
from ._list_instances_v2request import ListInstancesV2RequestTag
from ._tag_resources_request import TagResourcesRequestTag
from ._update_instance_request import UpdateInstanceRequestComponents

__all__ = [
    DBVersionDetail,
    InstanceDetail,
    MigrationSource,
    PriceInfo,
    PromotionInfo,
    ChangeResourceGroupRequest,
    ChangeResourceGroupResponseBody,
    ChangeResourceGroupResponse,
    CreateDefaultRoleResponseBody,
    CreateDefaultRoleResponse,
    CreateInstanceRequest,
    CreateInstanceResponseBody,
    CreateInstanceResponse,
    DeleteInstanceRequest,
    DeleteInstanceResponseBody,
    DeleteInstanceResponse,
    DescribeAccessControlListRequest,
    DescribeAccessControlListResponseBody,
    DescribeAccessControlListResponse,
    DescribeInstanceConfigsRequest,
    DescribeInstanceConfigsResponseBody,
    DescribeInstanceConfigsResponse,
    GetInstanceRequest,
    GetInstanceResponseBody,
    GetInstanceResponse,
    GetInstanceDetailRequest,
    GetInstanceDetailResponseBody,
    GetInstanceDetailResponse,
    ListInstancesRequest,
    ListInstancesShrinkRequest,
    ListInstancesResponseBody,
    ListInstancesResponse,
    ListInstancesV2Request,
    ListInstancesV2ShrinkRequest,
    ListInstancesV2ResponseBody,
    ListInstancesV2Response,
    ModifyInstanceConfigRequest,
    ModifyInstanceConfigResponseBody,
    ModifyInstanceConfigResponse,
    TagResourcesRequest,
    TagResourcesResponseBody,
    TagResourcesResponse,
    UnTagResourcesRequest,
    UnTagResourcesShrinkRequest,
    UnTagResourcesResponseBody,
    UnTagResourcesResponse,
    UpdateAccessControlListRequest,
    UpdateAccessControlListResponseBody,
    UpdateAccessControlListResponse,
    UpdateInstanceRequest,
    UpdateInstanceResponseBody,
    UpdateInstanceResponse,
    UpdateInstanceNameRequest,
    UpdateInstanceNameResponseBody,
    UpdateInstanceNameResponse,
    UpdatePublicNetworkStatusRequest,
    UpdatePublicNetworkStatusResponseBody,
    UpdatePublicNetworkStatusResponse,
    DBVersionDetailSpecsComponentSpecs,
    DBVersionDetailSpecs,
    InstanceDetailComponents,
    InstanceDetailTags,
    InstanceDetailVSwitchIds,
    MigrationSourceAuthInfo,
    MigrationSourceEndpoint,
    PriceInfoPriceModules,
    PriceInfoRules,
    CreateInstanceRequestComponents,
    CreateInstanceRequestTags,
    CreateInstanceRequestVSwitchIds,
    CreateInstanceResponseBodyData,
    DescribeAccessControlListResponseBodyData,
    GetInstanceDetailResponseBodyDataClusterInfoMilvusResourceInfoList,
    GetInstanceDetailResponseBodyDataClusterInfo,
    GetInstanceDetailResponseBodyDataHighAvailability,
    GetInstanceDetailResponseBodyDataMeasureConfig,
    GetInstanceDetailResponseBodyDataTags,
    GetInstanceDetailResponseBodyDataVSwitches,
    GetInstanceDetailResponseBodyData,
    ListInstancesRequestTag,
    ListInstancesResponseBodyDataClusterInfoMilvusResourceInfoList,
    ListInstancesResponseBodyDataClusterInfo,
    ListInstancesResponseBodyDataTags,
    ListInstancesResponseBodyData,
    ListInstancesV2RequestTag,
    TagResourcesRequestTag,
    UpdateInstanceRequestComponents
]
