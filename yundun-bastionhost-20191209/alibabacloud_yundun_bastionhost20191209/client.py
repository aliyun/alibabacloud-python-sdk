# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_bastionhost20191209 import models as yundun_bastionhost_20191209_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-bastionhost', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def config_instance_security_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse().from_map(
            self.do_rpcrequest('ConfigInstanceSecurityGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_instance_security_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('ConfigInstanceSecurityGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_security_groups(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_instance_security_groups_with_options(request, runtime)

    async def config_instance_security_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_security_groups_with_options_async(request, runtime)

    def config_instance_white_list_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse().from_map(
            self.do_rpcrequest('ConfigInstanceWhiteList', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_instance_white_list_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse().from_map(
            await self.do_rpcrequest_async('ConfigInstanceWhiteList', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_white_list(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    async def config_instance_white_list_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_white_list_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def disable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse().from_map(
            self.do_rpcrequest('DisableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_instance_public_access_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse().from_map(
            await self.do_rpcrequest_async('DisableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_instance_public_access(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    async def disable_instance_public_access_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_public_access_with_options_async(request, runtime)

    def enable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse().from_map(
            self.do_rpcrequest('EnableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_instance_public_access_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse().from_map(
            await self.do_rpcrequest_async('EnableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_instance_public_access(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    async def enable_instance_public_access_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_public_access_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.StartInstanceResponse().from_map(
            self.do_rpcrequest('StartInstance', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.StartInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartInstance', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
