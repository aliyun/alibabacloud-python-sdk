# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._bind_instance_2vpc_request import BindInstance2VpcRequest
from ._bind_instance_2vpc_response_body import BindInstance2VpcResponseBody
from ._bind_instance_2vpc_response import BindInstance2VpcResponse
from ._change_resource_group_request import ChangeResourceGroupRequest
from ._change_resource_group_response_body import ChangeResourceGroupResponseBody
from ._change_resource_group_response import ChangeResourceGroupResponse
from ._check_instance_policy_request import CheckInstancePolicyRequest
from ._check_instance_policy_response_body import CheckInstancePolicyResponseBody
from ._check_instance_policy_response import CheckInstancePolicyResponse
from ._create_instance_request import CreateInstanceRequest
from ._create_instance_response_body import CreateInstanceResponseBody
from ._create_instance_response import CreateInstanceResponse
from ._create_vcuinstance_request import CreateVCUInstanceRequest
from ._create_vcuinstance_response_body import CreateVCUInstanceResponseBody
from ._create_vcuinstance_response import CreateVCUInstanceResponse
from ._delete_instance_request import DeleteInstanceRequest
from ._delete_instance_response_body import DeleteInstanceResponseBody
from ._delete_instance_response import DeleteInstanceResponse
from ._delete_instance_policy_request import DeleteInstancePolicyRequest
from ._delete_instance_policy_response_body import DeleteInstancePolicyResponseBody
from ._delete_instance_policy_response import DeleteInstancePolicyResponse
from ._delete_vcuinstance_request import DeleteVCUInstanceRequest
from ._delete_vcuinstance_response_body import DeleteVCUInstanceResponseBody
from ._delete_vcuinstance_response import DeleteVCUInstanceResponse
from ._describe_regions_request import DescribeRegionsRequest
from ._describe_regions_response_body import DescribeRegionsResponseBody
from ._describe_regions_response import DescribeRegionsResponse
from ._get_instance_request import GetInstanceRequest
from ._get_instance_response_body import GetInstanceResponseBody
from ._get_instance_response import GetInstanceResponse
from ._list_cluster_type_response_body import ListClusterTypeResponseBody
from ._list_cluster_type_response import ListClusterTypeResponse
from ._list_instances_request import ListInstancesRequest
from ._list_instances_shrink_request import ListInstancesShrinkRequest
from ._list_instances_response_body import ListInstancesResponseBody
from ._list_instances_response import ListInstancesResponse
from ._list_tag_resources_request import ListTagResourcesRequest
from ._list_tag_resources_shrink_request import ListTagResourcesShrinkRequest
from ._list_tag_resources_response_body import ListTagResourcesResponseBody
from ._list_tag_resources_response import ListTagResourcesResponse
from ._list_vpc_info_by_instance_request import ListVpcInfoByInstanceRequest
from ._list_vpc_info_by_instance_response_body import ListVpcInfoByInstanceResponseBody
from ._list_vpc_info_by_instance_response import ListVpcInfoByInstanceResponse
from ._list_vpc_info_by_vpc_request import ListVpcInfoByVpcRequest
from ._list_vpc_info_by_vpc_response_body import ListVpcInfoByVpcResponseBody
from ._list_vpc_info_by_vpc_response import ListVpcInfoByVpcResponse
from ._tag_resources_request import TagResourcesRequest
from ._tag_resources_response_body import TagResourcesResponseBody
from ._tag_resources_response import TagResourcesResponse
from ._unbind_instance_2vpc_request import UnbindInstance2VpcRequest
from ._unbind_instance_2vpc_response_body import UnbindInstance2VpcResponseBody
from ._unbind_instance_2vpc_response import UnbindInstance2VpcResponse
from ._untag_resources_request import UntagResourcesRequest
from ._untag_resources_response_body import UntagResourcesResponseBody
from ._untag_resources_response import UntagResourcesResponse
from ._update_instance_request import UpdateInstanceRequest
from ._update_instance_response_body import UpdateInstanceResponseBody
from ._update_instance_response import UpdateInstanceResponse
from ._update_instance_elastic_vcuupper_limit_request import UpdateInstanceElasticVCUUpperLimitRequest
from ._update_instance_elastic_vcuupper_limit_response_body import UpdateInstanceElasticVCUUpperLimitResponseBody
from ._update_instance_elastic_vcuupper_limit_response import UpdateInstanceElasticVCUUpperLimitResponse
from ._update_instance_policy_request import UpdateInstancePolicyRequest
from ._update_instance_policy_response_body import UpdateInstancePolicyResponseBody
from ._update_instance_policy_response import UpdateInstancePolicyResponse
from ._create_instance_request import CreateInstanceRequestTags
from ._create_vcuinstance_request import CreateVCUInstanceRequestTags
from ._describe_regions_response_body import DescribeRegionsResponseBodyRegions
from ._get_instance_response_body import GetInstanceResponseBodyTags
from ._list_cluster_type_response_body import ListClusterTypeResponseBodyClusterTypeDetailList
from ._list_instances_request import ListInstancesRequestTag
from ._list_instances_response_body import ListInstancesResponseBodyInstances
from ._list_tag_resources_request import ListTagResourcesRequestTags
from ._list_tag_resources_response_body import ListTagResourcesResponseBodyTagResources
from ._list_vpc_info_by_instance_response_body import ListVpcInfoByInstanceResponseBodyVpcInfos
from ._list_vpc_info_by_vpc_response_body import ListVpcInfoByVpcResponseBodyVpcInfos
from ._tag_resources_request import TagResourcesRequestTags

__all__ = [
    BindInstance2VpcRequest,
    BindInstance2VpcResponseBody,
    BindInstance2VpcResponse,
    ChangeResourceGroupRequest,
    ChangeResourceGroupResponseBody,
    ChangeResourceGroupResponse,
    CheckInstancePolicyRequest,
    CheckInstancePolicyResponseBody,
    CheckInstancePolicyResponse,
    CreateInstanceRequest,
    CreateInstanceResponseBody,
    CreateInstanceResponse,
    CreateVCUInstanceRequest,
    CreateVCUInstanceResponseBody,
    CreateVCUInstanceResponse,
    DeleteInstanceRequest,
    DeleteInstanceResponseBody,
    DeleteInstanceResponse,
    DeleteInstancePolicyRequest,
    DeleteInstancePolicyResponseBody,
    DeleteInstancePolicyResponse,
    DeleteVCUInstanceRequest,
    DeleteVCUInstanceResponseBody,
    DeleteVCUInstanceResponse,
    DescribeRegionsRequest,
    DescribeRegionsResponseBody,
    DescribeRegionsResponse,
    GetInstanceRequest,
    GetInstanceResponseBody,
    GetInstanceResponse,
    ListClusterTypeResponseBody,
    ListClusterTypeResponse,
    ListInstancesRequest,
    ListInstancesShrinkRequest,
    ListInstancesResponseBody,
    ListInstancesResponse,
    ListTagResourcesRequest,
    ListTagResourcesShrinkRequest,
    ListTagResourcesResponseBody,
    ListTagResourcesResponse,
    ListVpcInfoByInstanceRequest,
    ListVpcInfoByInstanceResponseBody,
    ListVpcInfoByInstanceResponse,
    ListVpcInfoByVpcRequest,
    ListVpcInfoByVpcResponseBody,
    ListVpcInfoByVpcResponse,
    TagResourcesRequest,
    TagResourcesResponseBody,
    TagResourcesResponse,
    UnbindInstance2VpcRequest,
    UnbindInstance2VpcResponseBody,
    UnbindInstance2VpcResponse,
    UntagResourcesRequest,
    UntagResourcesResponseBody,
    UntagResourcesResponse,
    UpdateInstanceRequest,
    UpdateInstanceResponseBody,
    UpdateInstanceResponse,
    UpdateInstanceElasticVCUUpperLimitRequest,
    UpdateInstanceElasticVCUUpperLimitResponseBody,
    UpdateInstanceElasticVCUUpperLimitResponse,
    UpdateInstancePolicyRequest,
    UpdateInstancePolicyResponseBody,
    UpdateInstancePolicyResponse,
    CreateInstanceRequestTags,
    CreateVCUInstanceRequestTags,
    DescribeRegionsResponseBodyRegions,
    GetInstanceResponseBodyTags,
    ListClusterTypeResponseBodyClusterTypeDetailList,
    ListInstancesRequestTag,
    ListInstancesResponseBodyInstances,
    ListTagResourcesRequestTags,
    ListTagResourcesResponseBodyTagResources,
    ListVpcInfoByInstanceResponseBodyVpcInfos,
    ListVpcInfoByVpcResponseBodyVpcInfos,
    TagResourcesRequestTags
]
