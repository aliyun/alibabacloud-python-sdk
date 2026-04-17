# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_alikafka20190916 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('alikafka', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_defined_sg_with_options(
        self,
        tmp_req: main_models.AddUserDefinedSgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserDefinedSgResponse:
        tmp_req.validate()
        request = main_models.AddUserDefinedSgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sg_id_list):
            request.sg_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sg_id_list, 'SgIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sg_id_list_shrink):
            query['SgIdList'] = request.sg_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserDefinedSg',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserDefinedSgResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_defined_sg_with_options_async(
        self,
        tmp_req: main_models.AddUserDefinedSgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserDefinedSgResponse:
        tmp_req.validate()
        request = main_models.AddUserDefinedSgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sg_id_list):
            request.sg_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sg_id_list, 'SgIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sg_id_list_shrink):
            query['SgIdList'] = request.sg_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserDefinedSg',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserDefinedSgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_defined_sg(
        self,
        request: main_models.AddUserDefinedSgRequest,
    ) -> main_models.AddUserDefinedSgResponse:
        runtime = RuntimeOptions()
        return self.add_user_defined_sg_with_options(request, runtime)

    async def add_user_defined_sg_async(
        self,
        request: main_models.AddUserDefinedSgRequest,
    ) -> main_models.AddUserDefinedSgResponse:
        runtime = RuntimeOptions()
        return await self.add_user_defined_sg_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def convert_post_pay_order_with_options(
        self,
        request: main_models.ConvertPostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertPostPayOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertPostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertPostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_post_pay_order_with_options_async(
        self,
        request: main_models.ConvertPostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertPostPayOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertPostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertPostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_post_pay_order(
        self,
        request: main_models.ConvertPostPayOrderRequest,
    ) -> main_models.ConvertPostPayOrderResponse:
        runtime = RuntimeOptions()
        return self.convert_post_pay_order_with_options(request, runtime)

    async def convert_post_pay_order_async(
        self,
        request: main_models.ConvertPostPayOrderRequest,
    ) -> main_models.ConvertPostPayOrderResponse:
        runtime = RuntimeOptions()
        return await self.convert_post_pay_order_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: main_models.CreateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not DaraCore.is_null(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not DaraCore.is_null(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not DaraCore.is_null(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAcl',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: main_models.CreateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not DaraCore.is_null(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not DaraCore.is_null(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not DaraCore.is_null(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAcl',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl(
        self,
        request: main_models.CreateAclRequest,
    ) -> main_models.CreateAclResponse:
        runtime = RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: main_models.CreateAclRequest,
    ) -> main_models.CreateAclResponse:
        runtime = RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: main_models.CreateConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: main_models.CreateConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_post_pay_instance_with_options(
        self,
        tmp_req: main_models.CreatePostPayInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePostPayInstanceResponse:
        tmp_req.validate()
        request = main_models.CreatePostPayInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePostPayInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePostPayInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_post_pay_instance_with_options_async(
        self,
        tmp_req: main_models.CreatePostPayInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePostPayInstanceResponse:
        tmp_req.validate()
        request = main_models.CreatePostPayInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePostPayInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePostPayInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_post_pay_instance(
        self,
        request: main_models.CreatePostPayInstanceRequest,
    ) -> main_models.CreatePostPayInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_post_pay_instance_with_options(request, runtime)

    async def create_post_pay_instance_async(
        self,
        request: main_models.CreatePostPayInstanceRequest,
    ) -> main_models.CreatePostPayInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_post_pay_instance_with_options_async(request, runtime)

    def create_post_pay_order_with_options(
        self,
        tmp_req: main_models.CreatePostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePostPayOrderResponse:
        tmp_req.validate()
        request = main_models.CreatePostPayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_post_pay_order_with_options_async(
        self,
        tmp_req: main_models.CreatePostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePostPayOrderResponse:
        tmp_req.validate()
        request = main_models.CreatePostPayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_post_pay_order(
        self,
        request: main_models.CreatePostPayOrderRequest,
    ) -> main_models.CreatePostPayOrderResponse:
        runtime = RuntimeOptions()
        return self.create_post_pay_order_with_options(request, runtime)

    async def create_post_pay_order_async(
        self,
        request: main_models.CreatePostPayOrderRequest,
    ) -> main_models.CreatePostPayOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_post_pay_order_with_options_async(request, runtime)

    def create_pre_pay_instance_with_options(
        self,
        tmp_req: main_models.CreatePrePayInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrePayInstanceResponse:
        tmp_req.validate()
        request = main_models.CreatePrePayInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrePayInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrePayInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pre_pay_instance_with_options_async(
        self,
        tmp_req: main_models.CreatePrePayInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrePayInstanceResponse:
        tmp_req.validate()
        request = main_models.CreatePrePayInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrePayInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrePayInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pre_pay_instance(
        self,
        request: main_models.CreatePrePayInstanceRequest,
    ) -> main_models.CreatePrePayInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_pre_pay_instance_with_options(request, runtime)

    async def create_pre_pay_instance_async(
        self,
        request: main_models.CreatePrePayInstanceRequest,
    ) -> main_models.CreatePrePayInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_pre_pay_instance_with_options_async(request, runtime)

    def create_pre_pay_order_with_options(
        self,
        tmp_req: main_models.CreatePrePayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrePayOrderResponse:
        tmp_req.validate()
        request = main_models.CreatePrePayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrePayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pre_pay_order_with_options_async(
        self,
        tmp_req: main_models.CreatePrePayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrePayOrderResponse:
        tmp_req.validate()
        request = main_models.CreatePrePayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrePayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrePayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pre_pay_order(
        self,
        request: main_models.CreatePrePayOrderRequest,
    ) -> main_models.CreatePrePayOrderResponse:
        runtime = RuntimeOptions()
        return self.create_pre_pay_order_with_options(request, runtime)

    async def create_pre_pay_order_async(
        self,
        request: main_models.CreatePrePayOrderRequest,
    ) -> main_models.CreatePrePayOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_pre_pay_order_with_options_async(request, runtime)

    def create_sasl_user_with_options(
        self,
        request: main_models.CreateSaslUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSaslUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mechanism):
            query['Mechanism'] = request.mechanism
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSaslUser',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSaslUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sasl_user_with_options_async(
        self,
        request: main_models.CreateSaslUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSaslUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mechanism):
            query['Mechanism'] = request.mechanism
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSaslUser',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSaslUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sasl_user(
        self,
        request: main_models.CreateSaslUserRequest,
    ) -> main_models.CreateSaslUserResponse:
        runtime = RuntimeOptions()
        return self.create_sasl_user_with_options(request, runtime)

    async def create_sasl_user_async(
        self,
        request: main_models.CreateSaslUserRequest,
    ) -> main_models.CreateSaslUserResponse:
        runtime = RuntimeOptions()
        return await self.create_sasl_user_with_options_async(request, runtime)

    def create_scheduled_scaling_rule_with_options(
        self,
        tmp_req: main_models.CreateScheduledScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledScalingRuleResponse:
        tmp_req.validate()
        request = main_models.CreateScheduledScalingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.weekly_types):
            request.weekly_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.weekly_types, 'WeeklyTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.duration_minutes):
            query['DurationMinutes'] = request.duration_minutes
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.first_scheduled_time):
            query['FirstScheduledTime'] = request.first_scheduled_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.reserved_pub_flow):
            query['ReservedPubFlow'] = request.reserved_pub_flow
        if not DaraCore.is_null(request.reserved_sub_flow):
            query['ReservedSubFlow'] = request.reserved_sub_flow
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.weekly_types_shrink):
            query['WeeklyTypes'] = request.weekly_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledScalingRule',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_scaling_rule_with_options_async(
        self,
        tmp_req: main_models.CreateScheduledScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledScalingRuleResponse:
        tmp_req.validate()
        request = main_models.CreateScheduledScalingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.weekly_types):
            request.weekly_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.weekly_types, 'WeeklyTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.duration_minutes):
            query['DurationMinutes'] = request.duration_minutes
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.first_scheduled_time):
            query['FirstScheduledTime'] = request.first_scheduled_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.reserved_pub_flow):
            query['ReservedPubFlow'] = request.reserved_pub_flow
        if not DaraCore.is_null(request.reserved_sub_flow):
            query['ReservedSubFlow'] = request.reserved_sub_flow
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.weekly_types_shrink):
            query['WeeklyTypes'] = request.weekly_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledScalingRule',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_scaling_rule(
        self,
        request: main_models.CreateScheduledScalingRuleRequest,
    ) -> main_models.CreateScheduledScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.create_scheduled_scaling_rule_with_options(request, runtime)

    async def create_scheduled_scaling_rule_async(
        self,
        request: main_models.CreateScheduledScalingRuleRequest,
    ) -> main_models.CreateScheduledScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_scheduled_scaling_rule_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: main_models.CreateTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compact_topic):
            query['CompactTopic'] = request.compact_topic
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.local_topic):
            query['LocalTopic'] = request.local_topic
        if not DaraCore.is_null(request.min_insync_replicas):
            query['MinInsyncReplicas'] = request.min_insync_replicas
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTopic',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        request: main_models.CreateTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compact_topic):
            query['CompactTopic'] = request.compact_topic
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.local_topic):
            query['LocalTopic'] = request.local_topic
        if not DaraCore.is_null(request.min_insync_replicas):
            query['MinInsyncReplicas'] = request.min_insync_replicas
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTopic',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        request: main_models.CreateTopicRequest,
    ) -> main_models.CreateTopicResponse:
        runtime = RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: main_models.CreateTopicRequest,
    ) -> main_models.CreateTopicResponse:
        runtime = RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: main_models.DeleteAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not DaraCore.is_null(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not DaraCore.is_null(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not DaraCore.is_null(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcl',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: main_models.DeleteAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not DaraCore.is_null(request.acl_operation_types):
            query['AclOperationTypes'] = request.acl_operation_types
        if not DaraCore.is_null(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not DaraCore.is_null(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcl',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl(
        self,
        request: main_models.DeleteAclRequest,
    ) -> main_models.DeleteAclResponse:
        runtime = RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: main_models.DeleteAclRequest,
    ) -> main_models.DeleteAclResponse:
        runtime = RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: main_models.DeleteConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: main_models.DeleteConsumerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        request: main_models.DeleteConsumerGroupRequest,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: main_models.DeleteConsumerGroupRequest,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_sasl_user_with_options(
        self,
        request: main_models.DeleteSaslUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSaslUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mechanism):
            query['Mechanism'] = request.mechanism
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSaslUser',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSaslUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sasl_user_with_options_async(
        self,
        request: main_models.DeleteSaslUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSaslUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mechanism):
            query['Mechanism'] = request.mechanism
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSaslUser',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSaslUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sasl_user(
        self,
        request: main_models.DeleteSaslUserRequest,
    ) -> main_models.DeleteSaslUserResponse:
        runtime = RuntimeOptions()
        return self.delete_sasl_user_with_options(request, runtime)

    async def delete_sasl_user_async(
        self,
        request: main_models.DeleteSaslUserRequest,
    ) -> main_models.DeleteSaslUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_sasl_user_with_options_async(request, runtime)

    def delete_scheduled_scaling_rule_with_options(
        self,
        request: main_models.DeleteScheduledScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledScalingRule',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_scaling_rule_with_options_async(
        self,
        request: main_models.DeleteScheduledScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledScalingRule',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_scaling_rule(
        self,
        request: main_models.DeleteScheduledScalingRuleRequest,
    ) -> main_models.DeleteScheduledScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_scheduled_scaling_rule_with_options(request, runtime)

    async def delete_scheduled_scaling_rule_async(
        self,
        request: main_models.DeleteScheduledScalingRuleRequest,
    ) -> main_models.DeleteScheduledScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_scheduled_scaling_rule_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: main_models.DeleteTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTopic',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        request: main_models.DeleteTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTopic',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        request: main_models.DeleteTopicRequest,
    ) -> main_models.DeleteTopicResponse:
        runtime = RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: main_models.DeleteTopicRequest,
    ) -> main_models.DeleteTopicResponse:
        runtime = RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def delete_user_defined_sg_with_options(
        self,
        tmp_req: main_models.DeleteUserDefinedSgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserDefinedSgResponse:
        tmp_req.validate()
        request = main_models.DeleteUserDefinedSgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sg_id_list):
            request.sg_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sg_id_list, 'SgIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sg_id_list_shrink):
            query['SgIdList'] = request.sg_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserDefinedSg',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserDefinedSgResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_defined_sg_with_options_async(
        self,
        tmp_req: main_models.DeleteUserDefinedSgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserDefinedSgResponse:
        tmp_req.validate()
        request = main_models.DeleteUserDefinedSgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sg_id_list):
            request.sg_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sg_id_list, 'SgIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sg_id_list_shrink):
            query['SgIdList'] = request.sg_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserDefinedSg',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserDefinedSgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_defined_sg(
        self,
        request: main_models.DeleteUserDefinedSgRequest,
    ) -> main_models.DeleteUserDefinedSgResponse:
        runtime = RuntimeOptions()
        return self.delete_user_defined_sg_with_options(request, runtime)

    async def delete_user_defined_sg_async(
        self,
        request: main_models.DeleteUserDefinedSgRequest,
    ) -> main_models.DeleteUserDefinedSgResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_defined_sg_with_options_async(request, runtime)

    def describe_acl_resource_name_with_options(
        self,
        request: main_models.DescribeAclResourceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclResourceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclResourceName',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclResourceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_resource_name_with_options_async(
        self,
        request: main_models.DescribeAclResourceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclResourceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclResourceName',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclResourceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_resource_name(
        self,
        request: main_models.DescribeAclResourceNameRequest,
    ) -> main_models.DescribeAclResourceNameResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_resource_name_with_options(request, runtime)

    async def describe_acl_resource_name_async(
        self,
        request: main_models.DescribeAclResourceNameRequest,
    ) -> main_models.DescribeAclResourceNameResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_resource_name_with_options_async(request, runtime)

    def describe_acls_with_options(
        self,
        request: main_models.DescribeAclsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not DaraCore.is_null(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not DaraCore.is_null(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAcls',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acls_with_options_async(
        self,
        request: main_models.DescribeAclsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not DaraCore.is_null(request.acl_permission_type):
            query['AclPermissionType'] = request.acl_permission_type
        if not DaraCore.is_null(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not DaraCore.is_null(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not DaraCore.is_null(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAcls',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acls(
        self,
        request: main_models.DescribeAclsRequest,
    ) -> main_models.DescribeAclsResponse:
        runtime = RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    async def describe_acls_async(
        self,
        request: main_models.DescribeAclsRequest,
    ) -> main_models.DescribeAclsResponse:
        runtime = RuntimeOptions()
        return await self.describe_acls_with_options_async(request, runtime)

    def describe_sasl_users_with_options(
        self,
        request: main_models.DescribeSaslUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSaslUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSaslUsers',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSaslUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sasl_users_with_options_async(
        self,
        request: main_models.DescribeSaslUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSaslUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSaslUsers',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSaslUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sasl_users(
        self,
        request: main_models.DescribeSaslUsersRequest,
    ) -> main_models.DescribeSaslUsersResponse:
        runtime = RuntimeOptions()
        return self.describe_sasl_users_with_options(request, runtime)

    async def describe_sasl_users_async(
        self,
        request: main_models.DescribeSaslUsersRequest,
    ) -> main_models.DescribeSaslUsersResponse:
        runtime = RuntimeOptions()
        return await self.describe_sasl_users_with_options_async(request, runtime)

    def downgrade_post_pay_order_with_options(
        self,
        tmp_req: main_models.DowngradePostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradePostPayOrderResponse:
        tmp_req.validate()
        request = main_models.DowngradePostPayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradePostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_post_pay_order_with_options_async(
        self,
        tmp_req: main_models.DowngradePostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradePostPayOrderResponse:
        tmp_req.validate()
        request = main_models.DowngradePostPayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradePostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradePostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_post_pay_order(
        self,
        request: main_models.DowngradePostPayOrderRequest,
    ) -> main_models.DowngradePostPayOrderResponse:
        runtime = RuntimeOptions()
        return self.downgrade_post_pay_order_with_options(request, runtime)

    async def downgrade_post_pay_order_async(
        self,
        request: main_models.DowngradePostPayOrderRequest,
    ) -> main_models.DowngradePostPayOrderResponse:
        runtime = RuntimeOptions()
        return await self.downgrade_post_pay_order_with_options_async(request, runtime)

    def downgrade_pre_pay_order_with_options(
        self,
        tmp_req: main_models.DowngradePrePayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradePrePayOrderResponse:
        tmp_req.validate()
        request = main_models.DowngradePrePayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradePrePayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_pre_pay_order_with_options_async(
        self,
        tmp_req: main_models.DowngradePrePayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DowngradePrePayOrderResponse:
        tmp_req.validate()
        request = main_models.DowngradePrePayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradePrePayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradePrePayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_pre_pay_order(
        self,
        request: main_models.DowngradePrePayOrderRequest,
    ) -> main_models.DowngradePrePayOrderResponse:
        runtime = RuntimeOptions()
        return self.downgrade_pre_pay_order_with_options(request, runtime)

    async def downgrade_pre_pay_order_async(
        self,
        request: main_models.DowngradePrePayOrderRequest,
    ) -> main_models.DowngradePrePayOrderResponse:
        runtime = RuntimeOptions()
        return await self.downgrade_pre_pay_order_with_options_async(request, runtime)

    def enable_auto_group_creation_with_options(
        self,
        request: main_models.EnableAutoGroupCreationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoGroupCreationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAutoGroupCreation',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoGroupCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_group_creation_with_options_async(
        self,
        request: main_models.EnableAutoGroupCreationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoGroupCreationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAutoGroupCreation',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoGroupCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_group_creation(
        self,
        request: main_models.EnableAutoGroupCreationRequest,
    ) -> main_models.EnableAutoGroupCreationResponse:
        runtime = RuntimeOptions()
        return self.enable_auto_group_creation_with_options(request, runtime)

    async def enable_auto_group_creation_async(
        self,
        request: main_models.EnableAutoGroupCreationRequest,
    ) -> main_models.EnableAutoGroupCreationResponse:
        runtime = RuntimeOptions()
        return await self.enable_auto_group_creation_with_options_async(request, runtime)

    def enable_auto_topic_creation_with_options(
        self,
        request: main_models.EnableAutoTopicCreationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoTopicCreationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.update_partition):
            query['UpdatePartition'] = request.update_partition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAutoTopicCreation',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoTopicCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_topic_creation_with_options_async(
        self,
        request: main_models.EnableAutoTopicCreationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoTopicCreationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.update_partition):
            query['UpdatePartition'] = request.update_partition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAutoTopicCreation',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoTopicCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_topic_creation(
        self,
        request: main_models.EnableAutoTopicCreationRequest,
    ) -> main_models.EnableAutoTopicCreationResponse:
        runtime = RuntimeOptions()
        return self.enable_auto_topic_creation_with_options(request, runtime)

    async def enable_auto_topic_creation_async(
        self,
        request: main_models.EnableAutoTopicCreationRequest,
    ) -> main_models.EnableAutoTopicCreationResponse:
        runtime = RuntimeOptions()
        return await self.enable_auto_topic_creation_with_options_async(request, runtime)

    def failover_test_with_options(
        self,
        request: main_models.FailoverTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailoverTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.configs):
            query['Configs'] = request.configs
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.execute_time):
            query['ExecuteTime'] = request.execute_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailoverTest',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailoverTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_test_with_options_async(
        self,
        request: main_models.FailoverTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailoverTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.configs):
            query['Configs'] = request.configs
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.execute_time):
            query['ExecuteTime'] = request.execute_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailoverTest',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailoverTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_test(
        self,
        request: main_models.FailoverTestRequest,
    ) -> main_models.FailoverTestResponse:
        runtime = RuntimeOptions()
        return self.failover_test_with_options(request, runtime)

    async def failover_test_async(
        self,
        request: main_models.FailoverTestRequest,
    ) -> main_models.FailoverTestResponse:
        runtime = RuntimeOptions()
        return await self.failover_test_with_options_async(request, runtime)

    def get_all_instance_id_list_with_options(
        self,
        request: main_models.GetAllInstanceIdListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAllInstanceIdListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAllInstanceIdList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAllInstanceIdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_instance_id_list_with_options_async(
        self,
        request: main_models.GetAllInstanceIdListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAllInstanceIdListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAllInstanceIdList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAllInstanceIdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_instance_id_list(
        self,
        request: main_models.GetAllInstanceIdListRequest,
    ) -> main_models.GetAllInstanceIdListResponse:
        runtime = RuntimeOptions()
        return self.get_all_instance_id_list_with_options(request, runtime)

    async def get_all_instance_id_list_async(
        self,
        request: main_models.GetAllInstanceIdListRequest,
    ) -> main_models.GetAllInstanceIdListResponse:
        runtime = RuntimeOptions()
        return await self.get_all_instance_id_list_with_options_async(request, runtime)

    def get_allowed_ip_list_with_options(
        self,
        request: main_models.GetAllowedIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAllowedIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAllowedIpList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAllowedIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_allowed_ip_list_with_options_async(
        self,
        request: main_models.GetAllowedIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAllowedIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAllowedIpList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAllowedIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_allowed_ip_list(
        self,
        request: main_models.GetAllowedIpListRequest,
    ) -> main_models.GetAllowedIpListResponse:
        runtime = RuntimeOptions()
        return self.get_allowed_ip_list_with_options(request, runtime)

    async def get_allowed_ip_list_async(
        self,
        request: main_models.GetAllowedIpListRequest,
    ) -> main_models.GetAllowedIpListResponse:
        runtime = RuntimeOptions()
        return await self.get_allowed_ip_list_with_options_async(request, runtime)

    def get_auto_scaling_configuration_with_options(
        self,
        request: main_models.GetAutoScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingConfiguration',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_configuration_with_options_async(
        self,
        request: main_models.GetAutoScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingConfiguration',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_configuration(
        self,
        request: main_models.GetAutoScalingConfigurationRequest,
    ) -> main_models.GetAutoScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_auto_scaling_configuration_with_options(request, runtime)

    async def get_auto_scaling_configuration_async(
        self,
        request: main_models.GetAutoScalingConfigurationRequest,
    ) -> main_models.GetAutoScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_scaling_configuration_with_options_async(request, runtime)

    def get_consumer_list_with_options(
        self,
        request: main_models.GetConsumerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_list_with_options_async(
        self,
        request: main_models.GetConsumerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_list(
        self,
        request: main_models.GetConsumerListRequest,
    ) -> main_models.GetConsumerListResponse:
        runtime = RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    async def get_consumer_list_async(
        self,
        request: main_models.GetConsumerListRequest,
    ) -> main_models.GetConsumerListResponse:
        runtime = RuntimeOptions()
        return await self.get_consumer_list_with_options_async(request, runtime)

    def get_consumer_progress_with_options(
        self,
        request: main_models.GetConsumerProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.hide_last_timestamp):
            query['HideLastTimestamp'] = request.hide_last_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerProgress',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_progress_with_options_async(
        self,
        request: main_models.GetConsumerProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.hide_last_timestamp):
            query['HideLastTimestamp'] = request.hide_last_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerProgress',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_progress(
        self,
        request: main_models.GetConsumerProgressRequest,
    ) -> main_models.GetConsumerProgressResponse:
        runtime = RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    async def get_consumer_progress_async(
        self,
        request: main_models.GetConsumerProgressRequest,
    ) -> main_models.GetConsumerProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_consumer_progress_with_options_async(request, runtime)

    def get_instance_list_with_options(
        self,
        request: main_models.GetInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series):
            query['Series'] = request.series
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_list_with_options_async(
        self,
        request: main_models.GetInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series):
            query['Series'] = request.series
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_list(
        self,
        request: main_models.GetInstanceListRequest,
    ) -> main_models.GetInstanceListResponse:
        runtime = RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    async def get_instance_list_async(
        self,
        request: main_models.GetInstanceListRequest,
    ) -> main_models.GetInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_list_with_options_async(request, runtime)

    def get_kafka_client_ip_with_options(
        self,
        request: main_models.GetKafkaClientIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKafkaClientIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKafkaClientIp',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKafkaClientIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kafka_client_ip_with_options_async(
        self,
        request: main_models.GetKafkaClientIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKafkaClientIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKafkaClientIp',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKafkaClientIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kafka_client_ip(
        self,
        request: main_models.GetKafkaClientIpRequest,
    ) -> main_models.GetKafkaClientIpResponse:
        runtime = RuntimeOptions()
        return self.get_kafka_client_ip_with_options(request, runtime)

    async def get_kafka_client_ip_async(
        self,
        request: main_models.GetKafkaClientIpRequest,
    ) -> main_models.GetKafkaClientIpResponse:
        runtime = RuntimeOptions()
        return await self.get_kafka_client_ip_with_options_async(request, runtime)

    def get_quota_tip_with_options(
        self,
        request: main_models.GetQuotaTipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaTipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaTip',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaTipResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_tip_with_options_async(
        self,
        request: main_models.GetQuotaTipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaTipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaTip',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaTipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_tip(
        self,
        request: main_models.GetQuotaTipRequest,
    ) -> main_models.GetQuotaTipResponse:
        runtime = RuntimeOptions()
        return self.get_quota_tip_with_options(request, runtime)

    async def get_quota_tip_async(
        self,
        request: main_models.GetQuotaTipRequest,
    ) -> main_models.GetQuotaTipResponse:
        runtime = RuntimeOptions()
        return await self.get_quota_tip_with_options_async(request, runtime)

    def get_risk_list_with_options(
        self,
        request: main_models.GetRiskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRiskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_index):
            query['StartIndex'] = request.start_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRiskList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRiskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_list_with_options_async(
        self,
        request: main_models.GetRiskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRiskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_index):
            query['StartIndex'] = request.start_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRiskList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRiskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_list(
        self,
        request: main_models.GetRiskListRequest,
    ) -> main_models.GetRiskListResponse:
        runtime = RuntimeOptions()
        return self.get_risk_list_with_options(request, runtime)

    async def get_risk_list_async(
        self,
        request: main_models.GetRiskListRequest,
    ) -> main_models.GetRiskListResponse:
        runtime = RuntimeOptions()
        return await self.get_risk_list_with_options_async(request, runtime)

    def get_topic_list_with_options(
        self,
        request: main_models.GetTopicListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_list_with_options_async(
        self,
        request: main_models.GetTopicListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicList',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_list(
        self,
        request: main_models.GetTopicListRequest,
    ) -> main_models.GetTopicListResponse:
        runtime = RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    async def get_topic_list_async(
        self,
        request: main_models.GetTopicListRequest,
    ) -> main_models.GetTopicListResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_list_with_options_async(request, runtime)

    def get_topic_status_with_options(
        self,
        request: main_models.GetTopicStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicStatus',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_status_with_options_async(
        self,
        request: main_models.GetTopicStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicStatus',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_status(
        self,
        request: main_models.GetTopicStatusRequest,
    ) -> main_models.GetTopicStatusResponse:
        runtime = RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    async def get_topic_status_async(
        self,
        request: main_models.GetTopicStatusRequest,
    ) -> main_models.GetTopicStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_status_with_options_async(request, runtime)

    def get_topic_subscribe_status_with_options(
        self,
        request: main_models.GetTopicSubscribeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicSubscribeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicSubscribeStatus',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicSubscribeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_subscribe_status_with_options_async(
        self,
        request: main_models.GetTopicSubscribeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicSubscribeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicSubscribeStatus',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicSubscribeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_subscribe_status(
        self,
        request: main_models.GetTopicSubscribeStatusRequest,
    ) -> main_models.GetTopicSubscribeStatusResponse:
        runtime = RuntimeOptions()
        return self.get_topic_subscribe_status_with_options(request, runtime)

    async def get_topic_subscribe_status_async(
        self,
        request: main_models.GetTopicSubscribeStatusRequest,
    ) -> main_models.GetTopicSubscribeStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_subscribe_status_with_options_async(request, runtime)

    def list_rebalance_info_with_options(
        self,
        request: main_models.ListRebalanceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRebalanceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRebalanceInfo',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRebalanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rebalance_info_with_options_async(
        self,
        request: main_models.ListRebalanceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRebalanceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRebalanceInfo',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRebalanceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rebalance_info(
        self,
        request: main_models.ListRebalanceInfoRequest,
    ) -> main_models.ListRebalanceInfoResponse:
        runtime = RuntimeOptions()
        return self.list_rebalance_info_with_options(request, runtime)

    async def list_rebalance_info_async(
        self,
        request: main_models.ListRebalanceInfoRequest,
    ) -> main_models.ListRebalanceInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_rebalance_info_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: main_models.ModifyInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceName',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: main_models.ModifyInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceName',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_name(
        self,
        request: main_models.ModifyInstanceNameRequest,
    ) -> main_models.ModifyInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: main_models.ModifyInstanceNameRequest,
    ) -> main_models.ModifyInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_partition_num_with_options(
        self,
        request: main_models.ModifyPartitionNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPartitionNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_partition_num):
            query['AddPartitionNum'] = request.add_partition_num
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPartitionNum',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPartitionNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_partition_num_with_options_async(
        self,
        request: main_models.ModifyPartitionNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPartitionNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_partition_num):
            query['AddPartitionNum'] = request.add_partition_num
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPartitionNum',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPartitionNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_partition_num(
        self,
        request: main_models.ModifyPartitionNumRequest,
    ) -> main_models.ModifyPartitionNumResponse:
        runtime = RuntimeOptions()
        return self.modify_partition_num_with_options(request, runtime)

    async def modify_partition_num_async(
        self,
        request: main_models.ModifyPartitionNumRequest,
    ) -> main_models.ModifyPartitionNumResponse:
        runtime = RuntimeOptions()
        return await self.modify_partition_num_with_options_async(request, runtime)

    def modify_scheduled_scaling_rule_with_options(
        self,
        request: main_models.ModifyScheduledScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledScalingRule',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScheduledScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_scaling_rule_with_options_async(
        self,
        request: main_models.ModifyScheduledScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledScalingRule',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScheduledScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_scaling_rule(
        self,
        request: main_models.ModifyScheduledScalingRuleRequest,
    ) -> main_models.ModifyScheduledScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_scheduled_scaling_rule_with_options(request, runtime)

    async def modify_scheduled_scaling_rule_async(
        self,
        request: main_models.ModifyScheduledScalingRuleRequest,
    ) -> main_models.ModifyScheduledScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_scheduled_scaling_rule_with_options_async(request, runtime)

    def modify_topic_remark_with_options(
        self,
        request: main_models.ModifyTopicRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTopicRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTopicRemark',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTopicRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_topic_remark_with_options_async(
        self,
        request: main_models.ModifyTopicRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTopicRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTopicRemark',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTopicRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_topic_remark(
        self,
        request: main_models.ModifyTopicRemarkRequest,
    ) -> main_models.ModifyTopicRemarkResponse:
        runtime = RuntimeOptions()
        return self.modify_topic_remark_with_options(request, runtime)

    async def modify_topic_remark_async(
        self,
        request: main_models.ModifyTopicRemarkRequest,
    ) -> main_models.ModifyTopicRemarkResponse:
        runtime = RuntimeOptions()
        return await self.modify_topic_remark_with_options_async(request, runtime)

    def modify_user_defined_sg_with_options(
        self,
        tmp_req: main_models.ModifyUserDefinedSgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserDefinedSgResponse:
        tmp_req.validate()
        request = main_models.ModifyUserDefinedSgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sg_id_list):
            request.sg_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sg_id_list, 'SgIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sg_id_list_shrink):
            query['SgIdList'] = request.sg_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserDefinedSg',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserDefinedSgResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_defined_sg_with_options_async(
        self,
        tmp_req: main_models.ModifyUserDefinedSgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserDefinedSgResponse:
        tmp_req.validate()
        request = main_models.ModifyUserDefinedSgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sg_id_list):
            request.sg_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sg_id_list, 'SgIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sg_id_list_shrink):
            query['SgIdList'] = request.sg_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserDefinedSg',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserDefinedSgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_defined_sg(
        self,
        request: main_models.ModifyUserDefinedSgRequest,
    ) -> main_models.ModifyUserDefinedSgResponse:
        runtime = RuntimeOptions()
        return self.modify_user_defined_sg_with_options(request, runtime)

    async def modify_user_defined_sg_async(
        self,
        request: main_models.ModifyUserDefinedSgRequest,
    ) -> main_models.ModifyUserDefinedSgResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_defined_sg_with_options_async(request, runtime)

    def query_message_with_options(
        self,
        request: main_models.QueryMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMessageResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMessage',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_with_options_async(
        self,
        request: main_models.QueryMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMessageResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMessage',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message(
        self,
        request: main_models.QueryMessageRequest,
    ) -> main_models.QueryMessageResponse:
        runtime = RuntimeOptions()
        return self.query_message_with_options(request, runtime)

    async def query_message_async(
        self,
        request: main_models.QueryMessageRequest,
    ) -> main_models.QueryMessageResponse:
        runtime = RuntimeOptions()
        return await self.query_message_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete_instance):
            query['ForceDeleteInstance'] = request.force_delete_instance
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete_instance):
            query['ForceDeleteInstance'] = request.force_delete_instance
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def reopen_instance_with_options(
        self,
        request: main_models.ReopenInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReopenInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReopenInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReopenInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reopen_instance_with_options_async(
        self,
        request: main_models.ReopenInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReopenInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReopenInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReopenInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reopen_instance(
        self,
        request: main_models.ReopenInstanceRequest,
    ) -> main_models.ReopenInstanceResponse:
        runtime = RuntimeOptions()
        return self.reopen_instance_with_options(request, runtime)

    async def reopen_instance_async(
        self,
        request: main_models.ReopenInstanceRequest,
    ) -> main_models.ReopenInstanceResponse:
        runtime = RuntimeOptions()
        return await self.reopen_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.cross_zone):
            query['CrossZone'] = request.cross_zone
        if not DaraCore.is_null(request.deploy_module):
            query['DeployModule'] = request.deploy_module
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_eip_inner):
            query['IsEipInner'] = request.is_eip_inner
        if not DaraCore.is_null(request.is_force_selected_zones):
            query['IsForceSelectedZones'] = request.is_force_selected_zones
        if not DaraCore.is_null(request.is_set_user_and_password):
            query['IsSetUserAndPassword'] = request.is_set_user_and_password
        if not DaraCore.is_null(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notifier):
            query['Notifier'] = request.notifier
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group):
            query['SecurityGroup'] = request.security_group
        if not DaraCore.is_null(request.selected_zones):
            query['SelectedZones'] = request.selected_zones
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.user_phone_num):
            query['UserPhoneNum'] = request.user_phone_num
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.cross_zone):
            query['CrossZone'] = request.cross_zone
        if not DaraCore.is_null(request.deploy_module):
            query['DeployModule'] = request.deploy_module
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_eip_inner):
            query['IsEipInner'] = request.is_eip_inner
        if not DaraCore.is_null(request.is_force_selected_zones):
            query['IsForceSelectedZones'] = request.is_force_selected_zones
        if not DaraCore.is_null(request.is_set_user_and_password):
            query['IsSetUserAndPassword'] = request.is_set_user_and_password
        if not DaraCore.is_null(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notifier):
            query['Notifier'] = request.notifier
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group):
            query['SecurityGroup'] = request.security_group
        if not DaraCore.is_null(request.selected_zones):
            query['SelectedZones'] = request.selected_zones
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.user_phone_num):
            query['UserPhoneNum'] = request.user_phone_num
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_allowed_ip_with_options(
        self,
        request: main_models.UpdateAllowedIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAllowedIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allowed_list_ip):
            query['AllowedListIp'] = request.allowed_list_ip
        if not DaraCore.is_null(request.allowed_list_type):
            query['AllowedListType'] = request.allowed_list_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port_range):
            query['PortRange'] = request.port_range
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAllowedIp',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAllowedIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_allowed_ip_with_options_async(
        self,
        request: main_models.UpdateAllowedIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAllowedIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allowed_list_ip):
            query['AllowedListIp'] = request.allowed_list_ip
        if not DaraCore.is_null(request.allowed_list_type):
            query['AllowedListType'] = request.allowed_list_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port_range):
            query['PortRange'] = request.port_range
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAllowedIp',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAllowedIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_allowed_ip(
        self,
        request: main_models.UpdateAllowedIpRequest,
    ) -> main_models.UpdateAllowedIpResponse:
        runtime = RuntimeOptions()
        return self.update_allowed_ip_with_options(request, runtime)

    async def update_allowed_ip_async(
        self,
        request: main_models.UpdateAllowedIpRequest,
    ) -> main_models.UpdateAllowedIpResponse:
        runtime = RuntimeOptions()
        return await self.update_allowed_ip_with_options_async(request, runtime)

    def update_consumer_offset_with_options(
        self,
        tmp_req: main_models.UpdateConsumerOffsetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerOffsetResponse:
        tmp_req.validate()
        request = main_models.UpdateConsumerOffsetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.offsets):
            request.offsets_shrink = Utils.array_to_string_with_specified_style(tmp_req.offsets, 'Offsets', 'json')
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.offsets_shrink):
            query['Offsets'] = request.offsets_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reset_type):
            query['ResetType'] = request.reset_type
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerOffset',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_offset_with_options_async(
        self,
        tmp_req: main_models.UpdateConsumerOffsetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerOffsetResponse:
        tmp_req.validate()
        request = main_models.UpdateConsumerOffsetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.offsets):
            request.offsets_shrink = Utils.array_to_string_with_specified_style(tmp_req.offsets, 'Offsets', 'json')
        query = {}
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.offsets_shrink):
            query['Offsets'] = request.offsets_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reset_type):
            query['ResetType'] = request.reset_type
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerOffset',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerOffsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_offset(
        self,
        request: main_models.UpdateConsumerOffsetRequest,
    ) -> main_models.UpdateConsumerOffsetResponse:
        runtime = RuntimeOptions()
        return self.update_consumer_offset_with_options(request, runtime)

    async def update_consumer_offset_async(
        self,
        request: main_models.UpdateConsumerOffsetRequest,
    ) -> main_models.UpdateConsumerOffsetResponse:
        runtime = RuntimeOptions()
        return await self.update_consumer_offset_with_options_async(request, runtime)

    def update_instance_config_with_options(
        self,
        request: main_models.UpdateInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceConfig',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_config_with_options_async(
        self,
        request: main_models.UpdateInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceConfig',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_config(
        self,
        request: main_models.UpdateInstanceConfigRequest,
    ) -> main_models.UpdateInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.update_instance_config_with_options(request, runtime)

    async def update_instance_config_async(
        self,
        request: main_models.UpdateInstanceConfigRequest,
    ) -> main_models.UpdateInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_config_with_options_async(request, runtime)

    def update_topic_config_with_options(
        self,
        request: main_models.UpdateTopicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTopicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTopicConfig',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTopicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_topic_config_with_options_async(
        self,
        request: main_models.UpdateTopicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTopicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTopicConfig',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTopicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_topic_config(
        self,
        request: main_models.UpdateTopicConfigRequest,
    ) -> main_models.UpdateTopicConfigResponse:
        runtime = RuntimeOptions()
        return self.update_topic_config_with_options(request, runtime)

    async def update_topic_config_async(
        self,
        request: main_models.UpdateTopicConfigRequest,
    ) -> main_models.UpdateTopicConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_topic_config_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: main_models.UpgradeInstanceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeInstanceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeInstanceVersion',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_version_with_options_async(
        self,
        request: main_models.UpgradeInstanceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeInstanceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeInstanceVersion',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeInstanceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance_version(
        self,
        request: main_models.UpgradeInstanceVersionRequest,
    ) -> main_models.UpgradeInstanceVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    async def upgrade_instance_version_async(
        self,
        request: main_models.UpgradeInstanceVersionRequest,
    ) -> main_models.UpgradeInstanceVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)

    def upgrade_post_pay_order_with_options(
        self,
        tmp_req: main_models.UpgradePostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradePostPayOrderResponse:
        tmp_req.validate()
        request = main_models.UpgradePostPayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradePostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_post_pay_order_with_options_async(
        self,
        tmp_req: main_models.UpgradePostPayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradePostPayOrderResponse:
        tmp_req.validate()
        request = main_models.UpgradePostPayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.serverless_config):
            request.serverless_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradePostPayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradePostPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_post_pay_order(
        self,
        request: main_models.UpgradePostPayOrderRequest,
    ) -> main_models.UpgradePostPayOrderResponse:
        runtime = RuntimeOptions()
        return self.upgrade_post_pay_order_with_options(request, runtime)

    async def upgrade_post_pay_order_async(
        self,
        request: main_models.UpgradePostPayOrderRequest,
    ) -> main_models.UpgradePostPayOrderResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_post_pay_order_with_options_async(request, runtime)

    def upgrade_pre_pay_order_with_options(
        self,
        tmp_req: main_models.UpgradePrePayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradePrePayOrderResponse:
        tmp_req.validate()
        request = main_models.UpgradePrePayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradePrePayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_pre_pay_order_with_options_async(
        self,
        tmp_req: main_models.UpgradePrePayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradePrePayOrderResponse:
        tmp_req.validate()
        request = main_models.UpgradePrePayOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.confluent_config):
            request.confluent_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.confluent_config, 'ConfluentConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.confluent_config_shrink):
            query['ConfluentConfig'] = request.confluent_config_shrink
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.eip_max):
            query['EipMax'] = request.eip_max
        if not DaraCore.is_null(request.eip_model):
            query['EipModel'] = request.eip_model
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_max):
            query['IoMax'] = request.io_max
        if not DaraCore.is_null(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradePrePayOrder',
            version = '2019-09-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradePrePayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_pre_pay_order(
        self,
        request: main_models.UpgradePrePayOrderRequest,
    ) -> main_models.UpgradePrePayOrderResponse:
        runtime = RuntimeOptions()
        return self.upgrade_pre_pay_order_with_options(request, runtime)

    async def upgrade_pre_pay_order_async(
        self,
        request: main_models.UpgradePrePayOrderRequest,
    ) -> main_models.UpgradePrePayOrderResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_pre_pay_order_with_options_async(request, runtime)
