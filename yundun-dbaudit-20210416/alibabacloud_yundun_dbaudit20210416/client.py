# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_dbaudit20210416 import models as yundun_dbaudit_20210416_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def clear_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20210416_models.ClearInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ClearInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ClearInstanceStorageResponse(),
            self.do_rpcrequest('ClearInstanceStorage', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.ClearInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ClearInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ClearInstanceStorageResponse(),
            await self.do_rpcrequest_async('ClearInstanceStorage', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_instance_storage(
        self,
        request: yundun_dbaudit_20210416_models.ClearInstanceStorageRequest,
    ) -> yundun_dbaudit_20210416_models.ClearInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_instance_storage_with_options(request, runtime)

    async def clear_instance_storage_async(
        self,
        request: yundun_dbaudit_20210416_models.ClearInstanceStorageRequest,
    ) -> yundun_dbaudit_20210416_models.ClearInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_instance_storage_with_options_async(request, runtime)

    def create_instance_connection_with_options(
        self,
        request: yundun_dbaudit_20210416_models.CreateInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.CreateInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.CreateInstanceConnectionResponse(),
            self.do_rpcrequest('CreateInstanceConnection', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_connection_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.CreateInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.CreateInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.CreateInstanceConnectionResponse(),
            await self.do_rpcrequest_async('CreateInstanceConnection', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance_connection(
        self,
        request: yundun_dbaudit_20210416_models.CreateInstanceConnectionRequest,
    ) -> yundun_dbaudit_20210416_models.CreateInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_connection_with_options(request, runtime)

    async def create_instance_connection_async(
        self,
        request: yundun_dbaudit_20210416_models.CreateInstanceConnectionRequest,
    ) -> yundun_dbaudit_20210416_models.CreateInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_connection_with_options_async(request, runtime)

    def delete_instance_connection_with_options(
        self,
        request: yundun_dbaudit_20210416_models.DeleteInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DeleteInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DeleteInstanceConnectionResponse(),
            self.do_rpcrequest('DeleteInstanceConnection', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_connection_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.DeleteInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DeleteInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DeleteInstanceConnectionResponse(),
            await self.do_rpcrequest_async('DeleteInstanceConnection', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance_connection(
        self,
        request: yundun_dbaudit_20210416_models.DeleteInstanceConnectionRequest,
    ) -> yundun_dbaudit_20210416_models.DeleteInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_connection_with_options(request, runtime)

    async def delete_instance_connection_async(
        self,
        request: yundun_dbaudit_20210416_models.DeleteInstanceConnectionRequest,
    ) -> yundun_dbaudit_20210416_models.DeleteInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_connection_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceAttributeRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeInstancesResponse(),
            await self.do_rpcrequest_async('DescribeInstances', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstancesRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeInstanceStorageResponse(),
            self.do_rpcrequest('DescribeInstanceStorage', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeInstanceStorageResponse(),
            await self.do_rpcrequest_async('DescribeInstanceStorage', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_storage(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceStorageRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_storage_with_options(request, runtime)

    async def describe_instance_storage_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeInstanceStorageRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_storage_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: yundun_dbaudit_20210416_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: yundun_dbaudit_20210416_models.DescribeRegionsRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: yundun_dbaudit_20210416_models.DescribeRegionsRequest,
    ) -> yundun_dbaudit_20210416_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_dbaudit_20210416_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ListTagKeysResponse(),
            await self.do_rpcrequest_async('ListTagKeys', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: yundun_dbaudit_20210416_models.ListTagKeysRequest,
    ) -> yundun_dbaudit_20210416_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: yundun_dbaudit_20210416_models.ListTagKeysRequest,
    ) -> yundun_dbaudit_20210416_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_dbaudit_20210416_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: yundun_dbaudit_20210416_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20210416_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_dbaudit_20210416_models.ListTagResourcesRequest,
    ) -> yundun_dbaudit_20210416_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ModifyInstanceAttributeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceAttributeRequest,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceAttributeRequest,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_storage_with_options(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ModifyInstanceStorageResponse(),
            self.do_rpcrequest('ModifyInstanceStorage', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_storage_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.ModifyInstanceStorageResponse(),
            await self.do_rpcrequest_async('ModifyInstanceStorage', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_storage(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceStorageRequest,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_storage_with_options(request, runtime)

    async def modify_instance_storage_async(
        self,
        request: yundun_dbaudit_20210416_models.ModifyInstanceStorageRequest,
    ) -> yundun_dbaudit_20210416_models.ModifyInstanceStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_storage_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_dbaudit_20210416_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.MoveResourceGroupResponse(),
            await self.do_rpcrequest_async('MoveResourceGroup', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: yundun_dbaudit_20210416_models.MoveResourceGroupRequest,
    ) -> yundun_dbaudit_20210416_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: yundun_dbaudit_20210416_models.MoveResourceGroupRequest,
    ) -> yundun_dbaudit_20210416_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def refund_instance_with_options(
        self,
        request: yundun_dbaudit_20210416_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.RefundInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.RefundInstanceResponse(),
            self.do_rpcrequest('RefundInstance', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_instance_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.RefundInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.RefundInstanceResponse(),
            await self.do_rpcrequest_async('RefundInstance', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_instance(
        self,
        request: yundun_dbaudit_20210416_models.RefundInstanceRequest,
    ) -> yundun_dbaudit_20210416_models.RefundInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    async def refund_instance_async(
        self,
        request: yundun_dbaudit_20210416_models.RefundInstanceRequest,
    ) -> yundun_dbaudit_20210416_models.RefundInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: yundun_dbaudit_20210416_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: yundun_dbaudit_20210416_models.TagResourcesRequest,
    ) -> yundun_dbaudit_20210416_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: yundun_dbaudit_20210416_models.TagResourcesRequest,
    ) -> yundun_dbaudit_20210416_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: yundun_dbaudit_20210416_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: yundun_dbaudit_20210416_models.UntagResourcesRequest,
    ) -> yundun_dbaudit_20210416_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: yundun_dbaudit_20210416_models.UntagResourcesRequest,
    ) -> yundun_dbaudit_20210416_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_instance_connection_with_options(
        self,
        request: yundun_dbaudit_20210416_models.UpdateInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.UpdateInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.UpdateInstanceConnectionResponse(),
            self.do_rpcrequest('UpdateInstanceConnection', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_connection_with_options_async(
        self,
        request: yundun_dbaudit_20210416_models.UpdateInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_dbaudit_20210416_models.UpdateInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20210416_models.UpdateInstanceConnectionResponse(),
            await self.do_rpcrequest_async('UpdateInstanceConnection', '2021-04-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_connection(
        self,
        request: yundun_dbaudit_20210416_models.UpdateInstanceConnectionRequest,
    ) -> yundun_dbaudit_20210416_models.UpdateInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_connection_with_options(request, runtime)

    async def update_instance_connection_async(
        self,
        request: yundun_dbaudit_20210416_models.UpdateInstanceConnectionRequest,
    ) -> yundun_dbaudit_20210416_models.UpdateInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_connection_with_options_async(request, runtime)
