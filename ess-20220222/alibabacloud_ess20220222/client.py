# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ess20220222 import models as main_models
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
        self._endpoint_map = {
            'cn-qingdao': 'ess.aliyuncs.com',
            'cn-beijing': 'ess.aliyuncs.com',
            'cn-hangzhou': 'ess.aliyuncs.com',
            'cn-shanghai': 'ess.aliyuncs.com',
            'cn-shenzhen': 'ess.aliyuncs.com',
            'cn-hongkong': 'ess.aliyuncs.com',
            'ap-southeast-1': 'ess.aliyuncs.com',
            'us-east-1': 'ess.aliyuncs.com',
            'us-west-1': 'ess.aliyuncs.com',
            'cn-shanghai-finance-1': 'ess.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ess.aliyuncs.com',
            'cn-north-2-gov-1': 'ess.aliyuncs.com',
            'ap-northeast-2-pop': 'ess.aliyuncs.com',
            'cn-beijing-finance-pop': 'ess.aliyuncs.com',
            'cn-beijing-gov-1': 'ess.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ess.aliyuncs.com',
            'cn-edge-1': 'ess.aliyuncs.com',
            'cn-fujian': 'ess.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ess.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ess.aliyuncs.com',
            'cn-hangzhou-finance': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ess.aliyuncs.com',
            'cn-hangzhou-test-306': 'ess.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ess.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ess.aliyuncs.com',
            'cn-qingdao-nebula': 'ess.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ess.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ess.aliyuncs.com',
            'cn-shanghai-inner': 'ess.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ess.aliyuncs.com',
            'cn-shenzhen-inner': 'ess.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ess.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ess.aliyuncs.com',
            'cn-wuhan': 'ess.aliyuncs.com',
            'cn-yushanfang': 'ess.aliyuncs.com',
            'cn-zhangbei': 'ess.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ess.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ess.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ess.aliyuncs.com',
            'eu-west-1-oxs': 'ess.aliyuncs.com',
            'rus-west-1-pop': 'ess.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_eci_scaling_configuration_with_options(
        self,
        request: main_models.ApplyEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_eci_scaling_configuration_with_options_async(
        self,
        request: main_models.ApplyEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_eci_scaling_configuration(
        self,
        request: main_models.ApplyEciScalingConfigurationRequest,
    ) -> main_models.ApplyEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.apply_eci_scaling_configuration_with_options(request, runtime)

    async def apply_eci_scaling_configuration_async(
        self,
        request: main_models.ApplyEciScalingConfigurationRequest,
    ) -> main_models.ApplyEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.apply_eci_scaling_configuration_with_options_async(request, runtime)

    def apply_scaling_group_with_options(
        self,
        request: main_models.ApplyScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scaling_group_with_options_async(
        self,
        request: main_models.ApplyScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.format):
            query['Format'] = request.format
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scaling_group(
        self,
        request: main_models.ApplyScalingGroupRequest,
    ) -> main_models.ApplyScalingGroupResponse:
        runtime = RuntimeOptions()
        return self.apply_scaling_group_with_options(request, runtime)

    async def apply_scaling_group_async(
        self,
        request: main_models.ApplyScalingGroupRequest,
    ) -> main_models.ApplyScalingGroupResponse:
        runtime = RuntimeOptions()
        return await self.apply_scaling_group_with_options_async(request, runtime)

    def attach_alb_server_groups_with_options(
        self,
        request: main_models.AttachAlbServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAlbServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAlbServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_alb_server_groups_with_options_async(
        self,
        request: main_models.AttachAlbServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAlbServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAlbServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAlbServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_alb_server_groups(
        self,
        request: main_models.AttachAlbServerGroupsRequest,
    ) -> main_models.AttachAlbServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.attach_alb_server_groups_with_options(request, runtime)

    async def attach_alb_server_groups_async(
        self,
        request: main_models.AttachAlbServerGroupsRequest,
    ) -> main_models.AttachAlbServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.attach_alb_server_groups_with_options_async(request, runtime)

    def attach_dbinstances_with_options(
        self,
        request: main_models.AttachDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDBInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dbinstances_with_options_async(
        self,
        request: main_models.AttachDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDBInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_dbinstances(
        self,
        request: main_models.AttachDBInstancesRequest,
    ) -> main_models.AttachDBInstancesResponse:
        runtime = RuntimeOptions()
        return self.attach_dbinstances_with_options(request, runtime)

    async def attach_dbinstances_async(
        self,
        request: main_models.AttachDBInstancesRequest,
    ) -> main_models.AttachDBInstancesResponse:
        runtime = RuntimeOptions()
        return await self.attach_dbinstances_with_options_async(request, runtime)

    def attach_instances_with_options(
        self,
        request: main_models.AttachInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not DaraCore.is_null(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not DaraCore.is_null(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        request: main_models.AttachInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not DaraCore.is_null(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not DaraCore.is_null(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances(
        self,
        request: main_models.AttachInstancesRequest,
    ) -> main_models.AttachInstancesResponse:
        runtime = RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    async def attach_instances_async(
        self,
        request: main_models.AttachInstancesRequest,
    ) -> main_models.AttachInstancesResponse:
        runtime = RuntimeOptions()
        return await self.attach_instances_with_options_async(request, runtime)

    def attach_load_balancers_with_options(
        self,
        request: main_models.AttachLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not DaraCore.is_null(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachLoadBalancers',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_load_balancers_with_options_async(
        self,
        request: main_models.AttachLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not DaraCore.is_null(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachLoadBalancers',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_load_balancers(
        self,
        request: main_models.AttachLoadBalancersRequest,
    ) -> main_models.AttachLoadBalancersResponse:
        runtime = RuntimeOptions()
        return self.attach_load_balancers_with_options(request, runtime)

    async def attach_load_balancers_async(
        self,
        request: main_models.AttachLoadBalancersRequest,
    ) -> main_models.AttachLoadBalancersResponse:
        runtime = RuntimeOptions()
        return await self.attach_load_balancers_with_options_async(request, runtime)

    def attach_server_groups_with_options(
        self,
        request: main_models.AttachServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_server_groups_with_options_async(
        self,
        request: main_models.AttachServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_server_groups(
        self,
        request: main_models.AttachServerGroupsRequest,
    ) -> main_models.AttachServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.attach_server_groups_with_options(request, runtime)

    async def attach_server_groups_async(
        self,
        request: main_models.AttachServerGroupsRequest,
    ) -> main_models.AttachServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.attach_server_groups_with_options_async(request, runtime)

    def attach_vserver_groups_with_options(
        self,
        request: main_models.AttachVServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vserver_groups_with_options_async(
        self,
        request: main_models.AttachVServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vserver_groups(
        self,
        request: main_models.AttachVServerGroupsRequest,
    ) -> main_models.AttachVServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.attach_vserver_groups_with_options(request, runtime)

    async def attach_vserver_groups_async(
        self,
        request: main_models.AttachVServerGroupsRequest,
    ) -> main_models.AttachVServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.attach_vserver_groups_with_options_async(request, runtime)

    def cancel_instance_refresh_with_options(
        self,
        request: main_models.CancelInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelInstanceRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_instance_refresh_with_options_async(
        self,
        request: main_models.CancelInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelInstanceRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_instance_refresh(
        self,
        request: main_models.CancelInstanceRefreshRequest,
    ) -> main_models.CancelInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return self.cancel_instance_refresh_with_options(request, runtime)

    async def cancel_instance_refresh_async(
        self,
        request: main_models.CancelInstanceRefreshRequest,
    ) -> main_models.CancelInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return await self.cancel_instance_refresh_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-02-22',
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
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-02-22',
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

    def complete_lifecycle_action_with_options(
        self,
        request: main_models.CompleteLifecycleActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteLifecycleActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not DaraCore.is_null(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompleteLifecycleAction',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteLifecycleActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_lifecycle_action_with_options_async(
        self,
        request: main_models.CompleteLifecycleActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompleteLifecycleActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not DaraCore.is_null(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompleteLifecycleAction',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteLifecycleActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_lifecycle_action(
        self,
        request: main_models.CompleteLifecycleActionRequest,
    ) -> main_models.CompleteLifecycleActionResponse:
        runtime = RuntimeOptions()
        return self.complete_lifecycle_action_with_options(request, runtime)

    async def complete_lifecycle_action_async(
        self,
        request: main_models.CompleteLifecycleActionRequest,
    ) -> main_models.CompleteLifecycleActionResponse:
        runtime = RuntimeOptions()
        return await self.complete_lifecycle_action_with_options_async(request, runtime)

    def create_alarm_with_options(
        self,
        request: main_models.CreateAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not DaraCore.is_null(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective):
            query['Effective'] = request.effective
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.expressions):
            query['Expressions'] = request.expressions
        if not DaraCore.is_null(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.statistics):
            query['Statistics'] = request.statistics
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        request: main_models.CreateAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not DaraCore.is_null(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective):
            query['Effective'] = request.effective
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.expressions):
            query['Expressions'] = request.expressions
        if not DaraCore.is_null(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.statistics):
            query['Statistics'] = request.statistics
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm(
        self,
        request: main_models.CreateAlarmRequest,
    ) -> main_models.CreateAlarmResponse:
        runtime = RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    async def create_alarm_async(
        self,
        request: main_models.CreateAlarmRequest,
    ) -> main_models.CreateAlarmResponse:
        runtime = RuntimeOptions()
        return await self.create_alarm_with_options_async(request, runtime)

    def create_diagnose_report_with_options(
        self,
        request: main_models.CreateDiagnoseReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnoseReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnoseReport',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnoseReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnose_report_with_options_async(
        self,
        request: main_models.CreateDiagnoseReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnoseReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnoseReport',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnoseReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnose_report(
        self,
        request: main_models.CreateDiagnoseReportRequest,
    ) -> main_models.CreateDiagnoseReportResponse:
        runtime = RuntimeOptions()
        return self.create_diagnose_report_with_options(request, runtime)

    async def create_diagnose_report_async(
        self,
        request: main_models.CreateDiagnoseReportRequest,
    ) -> main_models.CreateDiagnoseReportResponse:
        runtime = RuntimeOptions()
        return await self.create_diagnose_report_with_options_async(request, runtime)

    def create_eci_scaling_configuration_with_options(
        self,
        request: main_models.CreateEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not DaraCore.is_null(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not DaraCore.is_null(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not DaraCore.is_null(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not DaraCore.is_null(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not DaraCore.is_null(request.containers):
            query['Containers'] = request.containers
        if not DaraCore.is_null(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not DaraCore.is_null(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not DaraCore.is_null(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not DaraCore.is_null(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not DaraCore.is_null(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not DaraCore.is_null(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not DaraCore.is_null(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not DaraCore.is_null(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not DaraCore.is_null(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not DaraCore.is_null(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not DaraCore.is_null(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not DaraCore.is_null(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not DaraCore.is_null(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not DaraCore.is_null(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not DaraCore.is_null(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not DaraCore.is_null(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not DaraCore.is_null(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eci_scaling_configuration_with_options_async(
        self,
        request: main_models.CreateEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not DaraCore.is_null(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not DaraCore.is_null(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not DaraCore.is_null(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not DaraCore.is_null(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not DaraCore.is_null(request.containers):
            query['Containers'] = request.containers
        if not DaraCore.is_null(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not DaraCore.is_null(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not DaraCore.is_null(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not DaraCore.is_null(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not DaraCore.is_null(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not DaraCore.is_null(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not DaraCore.is_null(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not DaraCore.is_null(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not DaraCore.is_null(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not DaraCore.is_null(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not DaraCore.is_null(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not DaraCore.is_null(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not DaraCore.is_null(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not DaraCore.is_null(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not DaraCore.is_null(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not DaraCore.is_null(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not DaraCore.is_null(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eci_scaling_configuration(
        self,
        request: main_models.CreateEciScalingConfigurationRequest,
    ) -> main_models.CreateEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.create_eci_scaling_configuration_with_options(request, runtime)

    async def create_eci_scaling_configuration_async(
        self,
        request: main_models.CreateEciScalingConfigurationRequest,
    ) -> main_models.CreateEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.create_eci_scaling_configuration_with_options_async(request, runtime)

    def create_lifecycle_hook_with_options(
        self,
        request: main_models.CreateLifecycleHookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLifecycleHookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_result):
            query['DefaultResult'] = request.default_result
        if not DaraCore.is_null(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLifecycleHook',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_hook_with_options_async(
        self,
        request: main_models.CreateLifecycleHookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLifecycleHookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_result):
            query['DefaultResult'] = request.default_result
        if not DaraCore.is_null(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLifecycleHook',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_hook(
        self,
        request: main_models.CreateLifecycleHookRequest,
    ) -> main_models.CreateLifecycleHookResponse:
        runtime = RuntimeOptions()
        return self.create_lifecycle_hook_with_options(request, runtime)

    async def create_lifecycle_hook_async(
        self,
        request: main_models.CreateLifecycleHookRequest,
    ) -> main_models.CreateLifecycleHookResponse:
        runtime = RuntimeOptions()
        return await self.create_lifecycle_hook_with_options_async(request, runtime)

    def create_notification_configuration_with_options(
        self,
        request: main_models.CreateNotificationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNotificationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message_encoding):
            query['MessageEncoding'] = request.message_encoding
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNotificationConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_notification_configuration_with_options_async(
        self,
        request: main_models.CreateNotificationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNotificationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message_encoding):
            query['MessageEncoding'] = request.message_encoding
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNotificationConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_notification_configuration(
        self,
        request: main_models.CreateNotificationConfigurationRequest,
    ) -> main_models.CreateNotificationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.create_notification_configuration_with_options(request, runtime)

    async def create_notification_configuration_async(
        self,
        request: main_models.CreateNotificationConfigurationRequest,
    ) -> main_models.CreateNotificationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.create_notification_configuration_with_options_async(request, runtime)

    def create_scaling_configuration_with_options(
        self,
        tmp_req: main_models.CreateScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingConfigurationResponse:
        tmp_req.validate()
        request = main_models.CreateScalingConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scheduler_options):
            request.scheduler_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.affinity):
            query['Affinity'] = request.affinity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not DaraCore.is_null(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not DaraCore.is_null(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not DaraCore.is_null(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not DaraCore.is_null(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not DaraCore.is_null(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not DaraCore.is_null(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not DaraCore.is_null(request.image_family):
            query['ImageFamily'] = request.image_family
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not DaraCore.is_null(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not DaraCore.is_null(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_pool_options):
            query['ResourcePoolOptions'] = request.resource_pool_options
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not DaraCore.is_null(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not DaraCore.is_null(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not DaraCore.is_null(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not DaraCore.is_null(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not DaraCore.is_null(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not DaraCore.is_null(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not DaraCore.is_null(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.image_options):
            query['ImageOptions'] = request.image_options
        if not DaraCore.is_null(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not DaraCore.is_null(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_configuration_with_options_async(
        self,
        tmp_req: main_models.CreateScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingConfigurationResponse:
        tmp_req.validate()
        request = main_models.CreateScalingConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scheduler_options):
            request.scheduler_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.affinity):
            query['Affinity'] = request.affinity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not DaraCore.is_null(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not DaraCore.is_null(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not DaraCore.is_null(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not DaraCore.is_null(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not DaraCore.is_null(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not DaraCore.is_null(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not DaraCore.is_null(request.image_family):
            query['ImageFamily'] = request.image_family
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not DaraCore.is_null(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not DaraCore.is_null(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_pool_options):
            query['ResourcePoolOptions'] = request.resource_pool_options
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not DaraCore.is_null(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not DaraCore.is_null(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not DaraCore.is_null(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not DaraCore.is_null(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not DaraCore.is_null(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not DaraCore.is_null(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not DaraCore.is_null(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.image_options):
            query['ImageOptions'] = request.image_options
        if not DaraCore.is_null(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not DaraCore.is_null(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_configuration(
        self,
        request: main_models.CreateScalingConfigurationRequest,
    ) -> main_models.CreateScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    async def create_scaling_configuration_async(
        self,
        request: main_models.CreateScalingConfigurationRequest,
    ) -> main_models.CreateScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.create_scaling_configuration_with_options_async(request, runtime)

    def create_scaling_group_with_options(
        self,
        request: main_models.CreateScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not DaraCore.is_null(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not DaraCore.is_null(request.auto_rebalance):
            query['AutoRebalance'] = request.auto_rebalance
        if not DaraCore.is_null(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not DaraCore.is_null(request.balance_mode):
            query['BalanceMode'] = request.balance_mode
        if not DaraCore.is_null(request.capacity_options):
            query['CapacityOptions'] = request.capacity_options
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not DaraCore.is_null(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not DaraCore.is_null(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not DaraCore.is_null(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not DaraCore.is_null(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not DaraCore.is_null(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not DaraCore.is_null(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not DaraCore.is_null(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not DaraCore.is_null(request.max_size):
            query['MaxSize'] = request.max_size
        if not DaraCore.is_null(request.min_size):
            query['MinSize'] = request.min_size
        if not DaraCore.is_null(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not DaraCore.is_null(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not DaraCore.is_null(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not DaraCore.is_null(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not DaraCore.is_null(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not DaraCore.is_null(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not DaraCore.is_null(request.stop_instance_timeout):
            query['StopInstanceTimeout'] = request.stop_instance_timeout
        if not DaraCore.is_null(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_group_with_options_async(
        self,
        request: main_models.CreateScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not DaraCore.is_null(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not DaraCore.is_null(request.auto_rebalance):
            query['AutoRebalance'] = request.auto_rebalance
        if not DaraCore.is_null(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not DaraCore.is_null(request.balance_mode):
            query['BalanceMode'] = request.balance_mode
        if not DaraCore.is_null(request.capacity_options):
            query['CapacityOptions'] = request.capacity_options
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not DaraCore.is_null(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not DaraCore.is_null(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not DaraCore.is_null(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not DaraCore.is_null(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not DaraCore.is_null(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not DaraCore.is_null(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not DaraCore.is_null(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not DaraCore.is_null(request.max_size):
            query['MaxSize'] = request.max_size
        if not DaraCore.is_null(request.min_size):
            query['MinSize'] = request.min_size
        if not DaraCore.is_null(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not DaraCore.is_null(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not DaraCore.is_null(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not DaraCore.is_null(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not DaraCore.is_null(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not DaraCore.is_null(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not DaraCore.is_null(request.stop_instance_timeout):
            query['StopInstanceTimeout'] = request.stop_instance_timeout
        if not DaraCore.is_null(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_group(
        self,
        request: main_models.CreateScalingGroupRequest,
    ) -> main_models.CreateScalingGroupResponse:
        runtime = RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    async def create_scaling_group_async(
        self,
        request: main_models.CreateScalingGroupRequest,
    ) -> main_models.CreateScalingGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_scaling_group_with_options_async(request, runtime)

    def create_scaling_rule_with_options(
        self,
        request: main_models.CreateScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not DaraCore.is_null(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not DaraCore.is_null(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not DaraCore.is_null(request.alarm_options):
            query['AlarmOptions'] = request.alarm_options
        if not DaraCore.is_null(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not DaraCore.is_null(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not DaraCore.is_null(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not DaraCore.is_null(request.hybrid_metrics):
            query['HybridMetrics'] = request.hybrid_metrics
        if not DaraCore.is_null(request.hybrid_monitor_namespace):
            query['HybridMonitorNamespace'] = request.hybrid_monitor_namespace
        if not DaraCore.is_null(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not DaraCore.is_null(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not DaraCore.is_null(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not DaraCore.is_null(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not DaraCore.is_null(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not DaraCore.is_null(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: main_models.CreateScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not DaraCore.is_null(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not DaraCore.is_null(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not DaraCore.is_null(request.alarm_options):
            query['AlarmOptions'] = request.alarm_options
        if not DaraCore.is_null(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not DaraCore.is_null(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not DaraCore.is_null(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not DaraCore.is_null(request.hybrid_metrics):
            query['HybridMetrics'] = request.hybrid_metrics
        if not DaraCore.is_null(request.hybrid_monitor_namespace):
            query['HybridMonitorNamespace'] = request.hybrid_monitor_namespace
        if not DaraCore.is_null(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not DaraCore.is_null(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not DaraCore.is_null(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not DaraCore.is_null(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not DaraCore.is_null(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not DaraCore.is_null(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_rule(
        self,
        request: main_models.CreateScalingRuleRequest,
    ) -> main_models.CreateScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    async def create_scaling_rule_async(
        self,
        request: main_models.CreateScalingRuleRequest,
    ) -> main_models.CreateScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_scaling_rule_with_options_async(request, runtime)

    def create_scheduled_task_with_options(
        self,
        request: main_models.CreateScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not DaraCore.is_null(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not DaraCore.is_null(request.max_value):
            query['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            query['MinValue'] = request.min_value
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not DaraCore.is_null(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not DaraCore.is_null(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not DaraCore.is_null(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        request: main_models.CreateScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not DaraCore.is_null(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not DaraCore.is_null(request.max_value):
            query['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            query['MinValue'] = request.min_value
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not DaraCore.is_null(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not DaraCore.is_null(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not DaraCore.is_null(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    async def create_scheduled_task_async(
        self,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_scheduled_task_with_options_async(request, runtime)

    def deactivate_scaling_configuration_with_options(
        self,
        request: main_models.DeactivateScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactivateScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_scaling_configuration_with_options_async(
        self,
        request: main_models.DeactivateScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactivateScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_scaling_configuration(
        self,
        request: main_models.DeactivateScalingConfigurationRequest,
    ) -> main_models.DeactivateScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.deactivate_scaling_configuration_with_options(request, runtime)

    async def deactivate_scaling_configuration_async(
        self,
        request: main_models.DeactivateScalingConfigurationRequest,
    ) -> main_models.DeactivateScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.deactivate_scaling_configuration_with_options_async(request, runtime)

    def delete_alarm_with_options(
        self,
        request: main_models.DeleteAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarm_with_options_async(
        self,
        request: main_models.DeleteAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarm(
        self,
        request: main_models.DeleteAlarmRequest,
    ) -> main_models.DeleteAlarmResponse:
        runtime = RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    async def delete_alarm_async(
        self,
        request: main_models.DeleteAlarmRequest,
    ) -> main_models.DeleteAlarmResponse:
        runtime = RuntimeOptions()
        return await self.delete_alarm_with_options_async(request, runtime)

    def delete_diagnose_report_with_options(
        self,
        request: main_models.DeleteDiagnoseReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiagnoseReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiagnoseReport',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiagnoseReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_diagnose_report_with_options_async(
        self,
        request: main_models.DeleteDiagnoseReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiagnoseReportResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiagnoseReport',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiagnoseReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_diagnose_report(
        self,
        request: main_models.DeleteDiagnoseReportRequest,
    ) -> main_models.DeleteDiagnoseReportResponse:
        runtime = RuntimeOptions()
        return self.delete_diagnose_report_with_options(request, runtime)

    async def delete_diagnose_report_async(
        self,
        request: main_models.DeleteDiagnoseReportRequest,
    ) -> main_models.DeleteDiagnoseReportResponse:
        runtime = RuntimeOptions()
        return await self.delete_diagnose_report_with_options_async(request, runtime)

    def delete_eci_scaling_configuration_with_options(
        self,
        request: main_models.DeleteEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_eci_scaling_configuration_with_options_async(
        self,
        request: main_models.DeleteEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_eci_scaling_configuration(
        self,
        request: main_models.DeleteEciScalingConfigurationRequest,
    ) -> main_models.DeleteEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.delete_eci_scaling_configuration_with_options(request, runtime)

    async def delete_eci_scaling_configuration_async(
        self,
        request: main_models.DeleteEciScalingConfigurationRequest,
    ) -> main_models.DeleteEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.delete_eci_scaling_configuration_with_options_async(request, runtime)

    def delete_lifecycle_hook_with_options(
        self,
        request: main_models.DeleteLifecycleHookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLifecycleHookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLifecycleHook',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lifecycle_hook_with_options_async(
        self,
        request: main_models.DeleteLifecycleHookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLifecycleHookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLifecycleHook',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lifecycle_hook(
        self,
        request: main_models.DeleteLifecycleHookRequest,
    ) -> main_models.DeleteLifecycleHookResponse:
        runtime = RuntimeOptions()
        return self.delete_lifecycle_hook_with_options(request, runtime)

    async def delete_lifecycle_hook_async(
        self,
        request: main_models.DeleteLifecycleHookRequest,
    ) -> main_models.DeleteLifecycleHookResponse:
        runtime = RuntimeOptions()
        return await self.delete_lifecycle_hook_with_options_async(request, runtime)

    def delete_notification_configuration_with_options(
        self,
        request: main_models.DeleteNotificationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNotificationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNotificationConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_notification_configuration_with_options_async(
        self,
        request: main_models.DeleteNotificationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNotificationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNotificationConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_notification_configuration(
        self,
        request: main_models.DeleteNotificationConfigurationRequest,
    ) -> main_models.DeleteNotificationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.delete_notification_configuration_with_options(request, runtime)

    async def delete_notification_configuration_async(
        self,
        request: main_models.DeleteNotificationConfigurationRequest,
    ) -> main_models.DeleteNotificationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.delete_notification_configuration_with_options_async(request, runtime)

    def delete_scaling_configuration_with_options(
        self,
        request: main_models.DeleteScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_configuration_with_options_async(
        self,
        request: main_models.DeleteScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_configuration(
        self,
        request: main_models.DeleteScalingConfigurationRequest,
    ) -> main_models.DeleteScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    async def delete_scaling_configuration_async(
        self,
        request: main_models.DeleteScalingConfigurationRequest,
    ) -> main_models.DeleteScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.delete_scaling_configuration_with_options_async(request, runtime)

    def delete_scaling_group_with_options(
        self,
        request: main_models.DeleteScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_group_with_options_async(
        self,
        request: main_models.DeleteScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_group(
        self,
        request: main_models.DeleteScalingGroupRequest,
    ) -> main_models.DeleteScalingGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    async def delete_scaling_group_async(
        self,
        request: main_models.DeleteScalingGroupRequest,
    ) -> main_models.DeleteScalingGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_scaling_group_with_options_async(request, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: main_models.DeleteScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: main_models.DeleteScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: main_models.DeleteScalingRuleRequest,
    ) -> main_models.DeleteScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    async def delete_scaling_rule_async(
        self,
        request: main_models.DeleteScalingRuleRequest,
    ) -> main_models.DeleteScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_scaling_rule_with_options_async(request, runtime)

    def delete_scheduled_task_with_options(
        self,
        request: main_models.DeleteScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledTask',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_task_with_options_async(
        self,
        request: main_models.DeleteScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledTask',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_task(
        self,
        request: main_models.DeleteScheduledTaskRequest,
    ) -> main_models.DeleteScheduledTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    async def delete_scheduled_task_async(
        self,
        request: main_models.DeleteScheduledTaskRequest,
    ) -> main_models.DeleteScheduledTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_scheduled_task_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: main_models.DescribeAlarmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlarmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlarms',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: main_models.DescribeAlarmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlarmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlarms',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms(
        self,
        request: main_models.DescribeAlarmsRequest,
    ) -> main_models.DescribeAlarmsResponse:
        runtime = RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: main_models.DescribeAlarmsRequest,
    ) -> main_models.DescribeAlarmsResponse:
        runtime = RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_alert_configuration_with_options(
        self,
        request: main_models.DescribeAlertConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_configuration_with_options_async(
        self,
        request: main_models.DescribeAlertConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_configuration(
        self,
        request: main_models.DescribeAlertConfigurationRequest,
    ) -> main_models.DescribeAlertConfigurationResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_configuration_with_options(request, runtime)

    async def describe_alert_configuration_async(
        self,
        request: main_models.DescribeAlertConfigurationRequest,
    ) -> main_models.DescribeAlertConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_configuration_with_options_async(request, runtime)

    def describe_diagnose_reports_with_options(
        self,
        request: main_models.DescribeDiagnoseReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnoseReportsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnoseReports',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnoseReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnose_reports_with_options_async(
        self,
        request: main_models.DescribeDiagnoseReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnoseReportsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnoseReports',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnoseReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnose_reports(
        self,
        request: main_models.DescribeDiagnoseReportsRequest,
    ) -> main_models.DescribeDiagnoseReportsResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnose_reports_with_options(request, runtime)

    async def describe_diagnose_reports_async(
        self,
        request: main_models.DescribeDiagnoseReportsRequest,
    ) -> main_models.DescribeDiagnoseReportsResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnose_reports_with_options_async(request, runtime)

    def describe_eci_scaling_configuration_detail_with_options(
        self,
        request: main_models.DescribeEciScalingConfigurationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEciScalingConfigurationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_format):
            query['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEciScalingConfigurationDetail',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEciScalingConfigurationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eci_scaling_configuration_detail_with_options_async(
        self,
        request: main_models.DescribeEciScalingConfigurationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEciScalingConfigurationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_format):
            query['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEciScalingConfigurationDetail',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEciScalingConfigurationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eci_scaling_configuration_detail(
        self,
        request: main_models.DescribeEciScalingConfigurationDetailRequest,
    ) -> main_models.DescribeEciScalingConfigurationDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_eci_scaling_configuration_detail_with_options(request, runtime)

    async def describe_eci_scaling_configuration_detail_async(
        self,
        request: main_models.DescribeEciScalingConfigurationDetailRequest,
    ) -> main_models.DescribeEciScalingConfigurationDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_eci_scaling_configuration_detail_with_options_async(request, runtime)

    def describe_eci_scaling_configurations_with_options(
        self,
        request: main_models.DescribeEciScalingConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEciScalingConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not DaraCore.is_null(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEciScalingConfigurations',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEciScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eci_scaling_configurations_with_options_async(
        self,
        request: main_models.DescribeEciScalingConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEciScalingConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not DaraCore.is_null(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEciScalingConfigurations',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEciScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eci_scaling_configurations(
        self,
        request: main_models.DescribeEciScalingConfigurationsRequest,
    ) -> main_models.DescribeEciScalingConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.describe_eci_scaling_configurations_with_options(request, runtime)

    async def describe_eci_scaling_configurations_async(
        self,
        request: main_models.DescribeEciScalingConfigurationsRequest,
    ) -> main_models.DescribeEciScalingConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_eci_scaling_configurations_with_options_async(request, runtime)

    def describe_elastic_strength_with_options(
        self,
        request: main_models.DescribeElasticStrengthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticStrengthResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticStrength',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticStrengthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_strength_with_options_async(
        self,
        request: main_models.DescribeElasticStrengthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticStrengthResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticStrength',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticStrengthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_strength(
        self,
        request: main_models.DescribeElasticStrengthRequest,
    ) -> main_models.DescribeElasticStrengthResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_strength_with_options(request, runtime)

    async def describe_elastic_strength_async(
        self,
        request: main_models.DescribeElasticStrengthRequest,
    ) -> main_models.DescribeElasticStrengthResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_strength_with_options_async(request, runtime)

    def describe_instance_create_and_delete_statistics_with_options(
        self,
        request: main_models.DescribeInstanceCreateAndDeleteStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceCreateAndDeleteStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceCreateAndDeleteStatistics',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceCreateAndDeleteStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_create_and_delete_statistics_with_options_async(
        self,
        request: main_models.DescribeInstanceCreateAndDeleteStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceCreateAndDeleteStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceCreateAndDeleteStatistics',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceCreateAndDeleteStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_create_and_delete_statistics(
        self,
        request: main_models.DescribeInstanceCreateAndDeleteStatisticsRequest,
    ) -> main_models.DescribeInstanceCreateAndDeleteStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_create_and_delete_statistics_with_options(request, runtime)

    async def describe_instance_create_and_delete_statistics_async(
        self,
        request: main_models.DescribeInstanceCreateAndDeleteStatisticsRequest,
    ) -> main_models.DescribeInstanceCreateAndDeleteStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_create_and_delete_statistics_with_options_async(request, runtime)

    def describe_instance_refreshes_with_options(
        self,
        request: main_models.DescribeInstanceRefreshesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRefreshesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_ids):
            query['InstanceRefreshTaskIds'] = request.instance_refresh_task_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRefreshes',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRefreshesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_refreshes_with_options_async(
        self,
        request: main_models.DescribeInstanceRefreshesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRefreshesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_ids):
            query['InstanceRefreshTaskIds'] = request.instance_refresh_task_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRefreshes',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRefreshesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_refreshes(
        self,
        request: main_models.DescribeInstanceRefreshesRequest,
    ) -> main_models.DescribeInstanceRefreshesResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_refreshes_with_options(request, runtime)

    async def describe_instance_refreshes_async(
        self,
        request: main_models.DescribeInstanceRefreshesRequest,
    ) -> main_models.DescribeInstanceRefreshesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_refreshes_with_options_async(request, runtime)

    def describe_lifecycle_actions_with_options(
        self,
        request: main_models.DescribeLifecycleActionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLifecycleActionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLifecycleActions',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLifecycleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_actions_with_options_async(
        self,
        request: main_models.DescribeLifecycleActionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLifecycleActionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLifecycleActions',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLifecycleActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_actions(
        self,
        request: main_models.DescribeLifecycleActionsRequest,
    ) -> main_models.DescribeLifecycleActionsResponse:
        runtime = RuntimeOptions()
        return self.describe_lifecycle_actions_with_options(request, runtime)

    async def describe_lifecycle_actions_async(
        self,
        request: main_models.DescribeLifecycleActionsRequest,
    ) -> main_models.DescribeLifecycleActionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_lifecycle_actions_with_options_async(request, runtime)

    def describe_lifecycle_hooks_with_options(
        self,
        request: main_models.DescribeLifecycleHooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLifecycleHooksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLifecycleHooks',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLifecycleHooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_hooks_with_options_async(
        self,
        request: main_models.DescribeLifecycleHooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLifecycleHooksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLifecycleHooks',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLifecycleHooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_hooks(
        self,
        request: main_models.DescribeLifecycleHooksRequest,
    ) -> main_models.DescribeLifecycleHooksResponse:
        runtime = RuntimeOptions()
        return self.describe_lifecycle_hooks_with_options(request, runtime)

    async def describe_lifecycle_hooks_async(
        self,
        request: main_models.DescribeLifecycleHooksRequest,
    ) -> main_models.DescribeLifecycleHooksResponse:
        runtime = RuntimeOptions()
        return await self.describe_lifecycle_hooks_with_options_async(request, runtime)

    def describe_limitation_with_options(
        self,
        request: main_models.DescribeLimitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLimitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLimitation',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_limitation_with_options_async(
        self,
        request: main_models.DescribeLimitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLimitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLimitation',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLimitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_limitation(
        self,
        request: main_models.DescribeLimitationRequest,
    ) -> main_models.DescribeLimitationResponse:
        runtime = RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    async def describe_limitation_async(
        self,
        request: main_models.DescribeLimitationRequest,
    ) -> main_models.DescribeLimitationResponse:
        runtime = RuntimeOptions()
        return await self.describe_limitation_with_options_async(request, runtime)

    def describe_notification_configurations_with_options(
        self,
        request: main_models.DescribeNotificationConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNotificationConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNotificationConfigurations',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNotificationConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_configurations_with_options_async(
        self,
        request: main_models.DescribeNotificationConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNotificationConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNotificationConfigurations',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNotificationConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_configurations(
        self,
        request: main_models.DescribeNotificationConfigurationsRequest,
    ) -> main_models.DescribeNotificationConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.describe_notification_configurations_with_options(request, runtime)

    async def describe_notification_configurations_async(
        self,
        request: main_models.DescribeNotificationConfigurationsRequest,
    ) -> main_models.DescribeNotificationConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_notification_configurations_with_options_async(request, runtime)

    def describe_notification_types_with_options(
        self,
        request: main_models.DescribeNotificationTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNotificationTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNotificationTypes',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNotificationTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_types_with_options_async(
        self,
        request: main_models.DescribeNotificationTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNotificationTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNotificationTypes',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNotificationTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_types(
        self,
        request: main_models.DescribeNotificationTypesRequest,
    ) -> main_models.DescribeNotificationTypesResponse:
        runtime = RuntimeOptions()
        return self.describe_notification_types_with_options(request, runtime)

    async def describe_notification_types_async(
        self,
        request: main_models.DescribeNotificationTypesRequest,
    ) -> main_models.DescribeNotificationTypesResponse:
        runtime = RuntimeOptions()
        return await self.describe_notification_types_with_options_async(request, runtime)

    def describe_pattern_types_with_options(
        self,
        request: main_models.DescribePatternTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePatternTypesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePatternTypes',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePatternTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pattern_types_with_options_async(
        self,
        request: main_models.DescribePatternTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePatternTypesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePatternTypes',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePatternTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pattern_types(
        self,
        request: main_models.DescribePatternTypesRequest,
    ) -> main_models.DescribePatternTypesResponse:
        runtime = RuntimeOptions()
        return self.describe_pattern_types_with_options(request, runtime)

    async def describe_pattern_types_async(
        self,
        request: main_models.DescribePatternTypesRequest,
    ) -> main_models.DescribePatternTypesResponse:
        runtime = RuntimeOptions()
        return await self.describe_pattern_types_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scaling_activities_with_options(
        self,
        request: main_models.DescribeScalingActivitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingActivitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingActivities',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activities_with_options_async(
        self,
        request: main_models.DescribeScalingActivitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingActivitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingActivities',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activities(
        self,
        request: main_models.DescribeScalingActivitiesRequest,
    ) -> main_models.DescribeScalingActivitiesResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    async def describe_scaling_activities_async(
        self,
        request: main_models.DescribeScalingActivitiesRequest,
    ) -> main_models.DescribeScalingActivitiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_activities_with_options_async(request, runtime)

    def describe_scaling_activity_detail_with_options(
        self,
        request: main_models.DescribeScalingActivityDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingActivityDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingActivityDetail',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingActivityDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activity_detail_with_options_async(
        self,
        request: main_models.DescribeScalingActivityDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingActivityDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingActivityDetail',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingActivityDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activity_detail(
        self,
        request: main_models.DescribeScalingActivityDetailRequest,
    ) -> main_models.DescribeScalingActivityDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    async def describe_scaling_activity_detail_async(
        self,
        request: main_models.DescribeScalingActivityDetailRequest,
    ) -> main_models.DescribeScalingActivityDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_activity_detail_with_options_async(request, runtime)

    def describe_scaling_activity_statistics_with_options(
        self,
        request: main_models.DescribeScalingActivityStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingActivityStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingActivityStatistics',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingActivityStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activity_statistics_with_options_async(
        self,
        request: main_models.DescribeScalingActivityStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingActivityStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingActivityStatistics',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingActivityStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activity_statistics(
        self,
        request: main_models.DescribeScalingActivityStatisticsRequest,
    ) -> main_models.DescribeScalingActivityStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_activity_statistics_with_options(request, runtime)

    async def describe_scaling_activity_statistics_async(
        self,
        request: main_models.DescribeScalingActivityStatisticsRequest,
    ) -> main_models.DescribeScalingActivityStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_activity_statistics_with_options_async(request, runtime)

    def describe_scaling_configurations_with_options(
        self,
        request: main_models.DescribeScalingConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not DaraCore.is_null(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingConfigurations',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_configurations_with_options_async(
        self,
        request: main_models.DescribeScalingConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not DaraCore.is_null(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingConfigurations',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_configurations(
        self,
        request: main_models.DescribeScalingConfigurationsRequest,
    ) -> main_models.DescribeScalingConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    async def describe_scaling_configurations_async(
        self,
        request: main_models.DescribeScalingConfigurationsRequest,
    ) -> main_models.DescribeScalingConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_configurations_with_options_async(request, runtime)

    def describe_scaling_group_detail_with_options(
        self,
        request: main_models.DescribeScalingGroupDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingGroupDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_format):
            query['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingGroupDetail',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_group_detail_with_options_async(
        self,
        request: main_models.DescribeScalingGroupDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingGroupDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_format):
            query['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingGroupDetail',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_group_detail(
        self,
        request: main_models.DescribeScalingGroupDetailRequest,
    ) -> main_models.DescribeScalingGroupDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_group_detail_with_options(request, runtime)

    async def describe_scaling_group_detail_async(
        self,
        request: main_models.DescribeScalingGroupDetailRequest,
    ) -> main_models.DescribeScalingGroupDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_group_detail_with_options_async(request, runtime)

    def describe_scaling_group_diagnose_details_with_options(
        self,
        request: main_models.DescribeScalingGroupDiagnoseDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingGroupDiagnoseDetailsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingGroupDiagnoseDetails',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingGroupDiagnoseDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_group_diagnose_details_with_options_async(
        self,
        request: main_models.DescribeScalingGroupDiagnoseDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingGroupDiagnoseDetailsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingGroupDiagnoseDetails',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingGroupDiagnoseDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_group_diagnose_details(
        self,
        request: main_models.DescribeScalingGroupDiagnoseDetailsRequest,
    ) -> main_models.DescribeScalingGroupDiagnoseDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_group_diagnose_details_with_options(request, runtime)

    async def describe_scaling_group_diagnose_details_async(
        self,
        request: main_models.DescribeScalingGroupDiagnoseDetailsRequest,
    ) -> main_models.DescribeScalingGroupDiagnoseDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_group_diagnose_details_with_options_async(request, runtime)

    def describe_scaling_groups_with_options(
        self,
        request: main_models.DescribeScalingGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not DaraCore.is_null(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not DaraCore.is_null(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_groups_with_options_async(
        self,
        request: main_models.DescribeScalingGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not DaraCore.is_null(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not DaraCore.is_null(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_groups(
        self,
        request: main_models.DescribeScalingGroupsRequest,
    ) -> main_models.DescribeScalingGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_groups_with_options(request, runtime)

    async def describe_scaling_groups_async(
        self,
        request: main_models.DescribeScalingGroupsRequest,
    ) -> main_models.DescribeScalingGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_groups_with_options_async(request, runtime)

    def describe_scaling_instances_with_options(
        self,
        request: main_models.DescribeScalingInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creation_type):
            query['CreationType'] = request.creation_type
        if not DaraCore.is_null(request.creation_types):
            query['CreationTypes'] = request.creation_types
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not DaraCore.is_null(request.lifecycle_states):
            query['LifecycleStates'] = request.lifecycle_states
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_instances_with_options_async(
        self,
        request: main_models.DescribeScalingInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creation_type):
            query['CreationType'] = request.creation_type
        if not DaraCore.is_null(request.creation_types):
            query['CreationTypes'] = request.creation_types
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not DaraCore.is_null(request.lifecycle_states):
            query['LifecycleStates'] = request.lifecycle_states
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_instances(
        self,
        request: main_models.DescribeScalingInstancesRequest,
    ) -> main_models.DescribeScalingInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    async def describe_scaling_instances_async(
        self,
        request: main_models.DescribeScalingInstancesRequest,
    ) -> main_models.DescribeScalingInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_instances_with_options_async(request, runtime)

    def describe_scaling_rules_with_options(
        self,
        request: main_models.DescribeScalingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not DaraCore.is_null(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not DaraCore.is_null(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not DaraCore.is_null(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingRules',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_rules_with_options_async(
        self,
        request: main_models.DescribeScalingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not DaraCore.is_null(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not DaraCore.is_null(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not DaraCore.is_null(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScalingRules',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_rules(
        self,
        request: main_models.DescribeScalingRulesRequest,
    ) -> main_models.DescribeScalingRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    async def describe_scaling_rules_async(
        self,
        request: main_models.DescribeScalingRulesRequest,
    ) -> main_models.DescribeScalingRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_scaling_rules_with_options_async(request, runtime)

    def describe_scheduled_tasks_with_options(
        self,
        request: main_models.DescribeScheduledTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not DaraCore.is_null(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not DaraCore.is_null(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        if not DaraCore.is_null(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScheduledTasks',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduled_tasks_with_options_async(
        self,
        request: main_models.DescribeScheduledTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not DaraCore.is_null(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not DaraCore.is_null(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        if not DaraCore.is_null(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScheduledTasks',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduled_tasks(
        self,
        request: main_models.DescribeScheduledTasksRequest,
    ) -> main_models.DescribeScheduledTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    async def describe_scheduled_tasks_async(
        self,
        request: main_models.DescribeScheduledTasksRequest,
    ) -> main_models.DescribeScheduledTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_scheduled_tasks_with_options_async(request, runtime)

    def detach_alb_server_groups_with_options(
        self,
        request: main_models.DetachAlbServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachAlbServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAlbServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_alb_server_groups_with_options_async(
        self,
        request: main_models.DetachAlbServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachAlbServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAlbServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAlbServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_alb_server_groups(
        self,
        request: main_models.DetachAlbServerGroupsRequest,
    ) -> main_models.DetachAlbServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.detach_alb_server_groups_with_options(request, runtime)

    async def detach_alb_server_groups_async(
        self,
        request: main_models.DetachAlbServerGroupsRequest,
    ) -> main_models.DetachAlbServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.detach_alb_server_groups_with_options_async(request, runtime)

    def detach_dbinstances_with_options(
        self,
        request: main_models.DetachDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_security_group):
            query['RemoveSecurityGroup'] = request.remove_security_group
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDBInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_dbinstances_with_options_async(
        self,
        request: main_models.DetachDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_security_group):
            query['RemoveSecurityGroup'] = request.remove_security_group
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDBInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_dbinstances(
        self,
        request: main_models.DetachDBInstancesRequest,
    ) -> main_models.DetachDBInstancesResponse:
        runtime = RuntimeOptions()
        return self.detach_dbinstances_with_options(request, runtime)

    async def detach_dbinstances_async(
        self,
        request: main_models.DetachDBInstancesRequest,
    ) -> main_models.DetachDBInstancesResponse:
        runtime = RuntimeOptions()
        return await self.detach_dbinstances_with_options_async(request, runtime)

    def detach_instances_with_options(
        self,
        request: main_models.DetachInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not DaraCore.is_null(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not DaraCore.is_null(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_instances_with_options_async(
        self,
        request: main_models.DetachInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not DaraCore.is_null(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not DaraCore.is_null(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_instances(
        self,
        request: main_models.DetachInstancesRequest,
    ) -> main_models.DetachInstancesResponse:
        runtime = RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    async def detach_instances_async(
        self,
        request: main_models.DetachInstancesRequest,
    ) -> main_models.DetachInstancesResponse:
        runtime = RuntimeOptions()
        return await self.detach_instances_with_options_async(request, runtime)

    def detach_load_balancers_with_options(
        self,
        request: main_models.DetachLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachLoadBalancers',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_load_balancers_with_options_async(
        self,
        request: main_models.DetachLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachLoadBalancers',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_load_balancers(
        self,
        request: main_models.DetachLoadBalancersRequest,
    ) -> main_models.DetachLoadBalancersResponse:
        runtime = RuntimeOptions()
        return self.detach_load_balancers_with_options(request, runtime)

    async def detach_load_balancers_async(
        self,
        request: main_models.DetachLoadBalancersRequest,
    ) -> main_models.DetachLoadBalancersResponse:
        runtime = RuntimeOptions()
        return await self.detach_load_balancers_with_options_async(request, runtime)

    def detach_server_groups_with_options(
        self,
        request: main_models.DetachServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_server_groups_with_options_async(
        self,
        request: main_models.DetachServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_server_groups(
        self,
        request: main_models.DetachServerGroupsRequest,
    ) -> main_models.DetachServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.detach_server_groups_with_options(request, runtime)

    async def detach_server_groups_async(
        self,
        request: main_models.DetachServerGroupsRequest,
    ) -> main_models.DetachServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.detach_server_groups_with_options_async(request, runtime)

    def detach_vserver_groups_with_options(
        self,
        request: main_models.DetachVServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vserver_groups_with_options_async(
        self,
        request: main_models.DetachVServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVServerGroups',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vserver_groups(
        self,
        request: main_models.DetachVServerGroupsRequest,
    ) -> main_models.DetachVServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.detach_vserver_groups_with_options(request, runtime)

    async def detach_vserver_groups_async(
        self,
        request: main_models.DetachVServerGroupsRequest,
    ) -> main_models.DetachVServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.detach_vserver_groups_with_options_async(request, runtime)

    def disable_alarm_with_options(
        self,
        request: main_models.DisableAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_alarm_with_options_async(
        self,
        request: main_models.DisableAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_alarm(
        self,
        request: main_models.DisableAlarmRequest,
    ) -> main_models.DisableAlarmResponse:
        runtime = RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    async def disable_alarm_async(
        self,
        request: main_models.DisableAlarmRequest,
    ) -> main_models.DisableAlarmResponse:
        runtime = RuntimeOptions()
        return await self.disable_alarm_with_options_async(request, runtime)

    def disable_scaling_group_with_options(
        self,
        request: main_models.DisableScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_scaling_group_with_options_async(
        self,
        request: main_models.DisableScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_scaling_group(
        self,
        request: main_models.DisableScalingGroupRequest,
    ) -> main_models.DisableScalingGroupResponse:
        runtime = RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    async def disable_scaling_group_async(
        self,
        request: main_models.DisableScalingGroupRequest,
    ) -> main_models.DisableScalingGroupResponse:
        runtime = RuntimeOptions()
        return await self.disable_scaling_group_with_options_async(request, runtime)

    def enable_alarm_with_options(
        self,
        request: main_models.EnableAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_alarm_with_options_async(
        self,
        request: main_models.EnableAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_alarm(
        self,
        request: main_models.EnableAlarmRequest,
    ) -> main_models.EnableAlarmResponse:
        runtime = RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    async def enable_alarm_async(
        self,
        request: main_models.EnableAlarmRequest,
    ) -> main_models.EnableAlarmResponse:
        runtime = RuntimeOptions()
        return await self.enable_alarm_with_options_async(request, runtime)

    def enable_scaling_group_with_options(
        self,
        request: main_models.EnableScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not DaraCore.is_null(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not DaraCore.is_null(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not DaraCore.is_null(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_scaling_group_with_options_async(
        self,
        request: main_models.EnableScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not DaraCore.is_null(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not DaraCore.is_null(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not DaraCore.is_null(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_scaling_group(
        self,
        request: main_models.EnableScalingGroupRequest,
    ) -> main_models.EnableScalingGroupResponse:
        runtime = RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    async def enable_scaling_group_async(
        self,
        request: main_models.EnableScalingGroupRequest,
    ) -> main_models.EnableScalingGroupResponse:
        runtime = RuntimeOptions()
        return await self.enable_scaling_group_with_options_async(request, runtime)

    def enter_standby_with_options(
        self,
        request: main_models.EnterStandbyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterStandbyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnterStandby',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enter_standby_with_options_async(
        self,
        request: main_models.EnterStandbyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnterStandbyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnterStandby',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnterStandbyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enter_standby(
        self,
        request: main_models.EnterStandbyRequest,
    ) -> main_models.EnterStandbyResponse:
        runtime = RuntimeOptions()
        return self.enter_standby_with_options(request, runtime)

    async def enter_standby_async(
        self,
        request: main_models.EnterStandbyRequest,
    ) -> main_models.EnterStandbyResponse:
        runtime = RuntimeOptions()
        return await self.enter_standby_with_options_async(request, runtime)

    def execute_scaling_rule_with_options(
        self,
        request: main_models.ExecuteScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.metric_value):
            query['MetricValue'] = request.metric_value
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_scaling_rule_with_options_async(
        self,
        request: main_models.ExecuteScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.metric_value):
            query['MetricValue'] = request.metric_value
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_scaling_rule(
        self,
        request: main_models.ExecuteScalingRuleRequest,
    ) -> main_models.ExecuteScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    async def execute_scaling_rule_async(
        self,
        request: main_models.ExecuteScalingRuleRequest,
    ) -> main_models.ExecuteScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.execute_scaling_rule_with_options_async(request, runtime)

    def exit_standby_with_options(
        self,
        request: main_models.ExitStandbyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExitStandbyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExitStandby',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExitStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    async def exit_standby_with_options_async(
        self,
        request: main_models.ExitStandbyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExitStandbyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExitStandby',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExitStandbyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exit_standby(
        self,
        request: main_models.ExitStandbyRequest,
    ) -> main_models.ExitStandbyResponse:
        runtime = RuntimeOptions()
        return self.exit_standby_with_options(request, runtime)

    async def exit_standby_async(
        self,
        request: main_models.ExitStandbyRequest,
    ) -> main_models.ExitStandbyResponse:
        runtime = RuntimeOptions()
        return await self.exit_standby_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-02-22',
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
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-02-22',
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

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_alarm_with_options(
        self,
        request: main_models.ModifyAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective):
            query['Effective'] = request.effective
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.expressions):
            query['Expressions'] = request.expressions
        if not DaraCore.is_null(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.statistics):
            query['Statistics'] = request.statistics
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_alarm_with_options_async(
        self,
        request: main_models.ModifyAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not DaraCore.is_null(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not DaraCore.is_null(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective):
            query['Effective'] = request.effective
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.expressions):
            query['Expressions'] = request.expressions
        if not DaraCore.is_null(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.statistics):
            query['Statistics'] = request.statistics
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAlarm',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_alarm(
        self,
        request: main_models.ModifyAlarmRequest,
    ) -> main_models.ModifyAlarmResponse:
        runtime = RuntimeOptions()
        return self.modify_alarm_with_options(request, runtime)

    async def modify_alarm_async(
        self,
        request: main_models.ModifyAlarmRequest,
    ) -> main_models.ModifyAlarmResponse:
        runtime = RuntimeOptions()
        return await self.modify_alarm_with_options_async(request, runtime)

    def modify_alert_configuration_with_options(
        self,
        request: main_models.ModifyAlertConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAlertConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scale_statuses):
            query['ScaleStatuses'] = request.scale_statuses
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAlertConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAlertConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_alert_configuration_with_options_async(
        self,
        request: main_models.ModifyAlertConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAlertConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scale_statuses):
            query['ScaleStatuses'] = request.scale_statuses
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAlertConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAlertConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_alert_configuration(
        self,
        request: main_models.ModifyAlertConfigurationRequest,
    ) -> main_models.ModifyAlertConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_alert_configuration_with_options(request, runtime)

    async def modify_alert_configuration_async(
        self,
        request: main_models.ModifyAlertConfigurationRequest,
    ) -> main_models.ModifyAlertConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_alert_configuration_with_options_async(request, runtime)

    def modify_eci_scaling_configuration_with_options(
        self,
        request: main_models.ModifyEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not DaraCore.is_null(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not DaraCore.is_null(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not DaraCore.is_null(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not DaraCore.is_null(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not DaraCore.is_null(request.containers):
            query['Containers'] = request.containers
        if not DaraCore.is_null(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not DaraCore.is_null(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not DaraCore.is_null(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not DaraCore.is_null(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not DaraCore.is_null(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not DaraCore.is_null(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not DaraCore.is_null(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not DaraCore.is_null(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not DaraCore.is_null(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not DaraCore.is_null(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not DaraCore.is_null(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not DaraCore.is_null(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not DaraCore.is_null(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not DaraCore.is_null(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not DaraCore.is_null(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not DaraCore.is_null(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not DaraCore.is_null(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not DaraCore.is_null(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_eci_scaling_configuration_with_options_async(
        self,
        request: main_models.ModifyEciScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEciScalingConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not DaraCore.is_null(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not DaraCore.is_null(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not DaraCore.is_null(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not DaraCore.is_null(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not DaraCore.is_null(request.containers):
            query['Containers'] = request.containers
        if not DaraCore.is_null(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not DaraCore.is_null(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not DaraCore.is_null(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not DaraCore.is_null(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not DaraCore.is_null(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not DaraCore.is_null(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not DaraCore.is_null(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not DaraCore.is_null(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not DaraCore.is_null(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not DaraCore.is_null(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not DaraCore.is_null(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not DaraCore.is_null(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not DaraCore.is_null(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not DaraCore.is_null(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not DaraCore.is_null(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not DaraCore.is_null(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not DaraCore.is_null(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not DaraCore.is_null(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEciScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_eci_scaling_configuration(
        self,
        request: main_models.ModifyEciScalingConfigurationRequest,
    ) -> main_models.ModifyEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_eci_scaling_configuration_with_options(request, runtime)

    async def modify_eci_scaling_configuration_async(
        self,
        request: main_models.ModifyEciScalingConfigurationRequest,
    ) -> main_models.ModifyEciScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_eci_scaling_configuration_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
    ) -> main_models.ModifyInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
    ) -> main_models.ModifyInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_lifecycle_hook_with_options(
        self,
        request: main_models.ModifyLifecycleHookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLifecycleHookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_result):
            query['DefaultResult'] = request.default_result
        if not DaraCore.is_null(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not DaraCore.is_null(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLifecycleHook',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lifecycle_hook_with_options_async(
        self,
        request: main_models.ModifyLifecycleHookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLifecycleHookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_result):
            query['DefaultResult'] = request.default_result
        if not DaraCore.is_null(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not DaraCore.is_null(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not DaraCore.is_null(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not DaraCore.is_null(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLifecycleHook',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lifecycle_hook(
        self,
        request: main_models.ModifyLifecycleHookRequest,
    ) -> main_models.ModifyLifecycleHookResponse:
        runtime = RuntimeOptions()
        return self.modify_lifecycle_hook_with_options(request, runtime)

    async def modify_lifecycle_hook_async(
        self,
        request: main_models.ModifyLifecycleHookRequest,
    ) -> main_models.ModifyLifecycleHookResponse:
        runtime = RuntimeOptions()
        return await self.modify_lifecycle_hook_with_options_async(request, runtime)

    def modify_notification_configuration_with_options(
        self,
        request: main_models.ModifyNotificationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNotificationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message_encoding):
            query['MessageEncoding'] = request.message_encoding
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNotificationConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_notification_configuration_with_options_async(
        self,
        request: main_models.ModifyNotificationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNotificationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message_encoding):
            query['MessageEncoding'] = request.message_encoding
        if not DaraCore.is_null(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not DaraCore.is_null(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNotificationConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_notification_configuration(
        self,
        request: main_models.ModifyNotificationConfigurationRequest,
    ) -> main_models.ModifyNotificationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_notification_configuration_with_options(request, runtime)

    async def modify_notification_configuration_async(
        self,
        request: main_models.ModifyNotificationConfigurationRequest,
    ) -> main_models.ModifyNotificationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_notification_configuration_with_options_async(request, runtime)

    def modify_scaling_configuration_with_options(
        self,
        tmp_req: main_models.ModifyScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingConfigurationResponse:
        tmp_req.validate()
        request = main_models.ModifyScalingConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scheduler_options):
            request.scheduler_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.affinity):
            query['Affinity'] = request.affinity
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not DaraCore.is_null(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not DaraCore.is_null(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not DaraCore.is_null(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not DaraCore.is_null(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not DaraCore.is_null(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not DaraCore.is_null(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not DaraCore.is_null(request.image_family):
            query['ImageFamily'] = request.image_family
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not DaraCore.is_null(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not DaraCore.is_null(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not DaraCore.is_null(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_pool_options):
            query['ResourcePoolOptions'] = request.resource_pool_options
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not DaraCore.is_null(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not DaraCore.is_null(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not DaraCore.is_null(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not DaraCore.is_null(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not DaraCore.is_null(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not DaraCore.is_null(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.image_options):
            query['ImageOptions'] = request.image_options
        if not DaraCore.is_null(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not DaraCore.is_null(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_configuration_with_options_async(
        self,
        tmp_req: main_models.ModifyScalingConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingConfigurationResponse:
        tmp_req.validate()
        request = main_models.ModifyScalingConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scheduler_options):
            request.scheduler_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.affinity):
            query['Affinity'] = request.affinity
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not DaraCore.is_null(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not DaraCore.is_null(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not DaraCore.is_null(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not DaraCore.is_null(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not DaraCore.is_null(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not DaraCore.is_null(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not DaraCore.is_null(request.image_family):
            query['ImageFamily'] = request.image_family
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not DaraCore.is_null(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not DaraCore.is_null(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not DaraCore.is_null(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not DaraCore.is_null(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_pool_options):
            query['ResourcePoolOptions'] = request.resource_pool_options
        if not DaraCore.is_null(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not DaraCore.is_null(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not DaraCore.is_null(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not DaraCore.is_null(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not DaraCore.is_null(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not DaraCore.is_null(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not DaraCore.is_null(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not DaraCore.is_null(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not DaraCore.is_null(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not DaraCore.is_null(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not DaraCore.is_null(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.image_options):
            query['ImageOptions'] = request.image_options
        if not DaraCore.is_null(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not DaraCore.is_null(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingConfiguration',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_configuration(
        self,
        request: main_models.ModifyScalingConfigurationRequest,
    ) -> main_models.ModifyScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_scaling_configuration_with_options(request, runtime)

    async def modify_scaling_configuration_async(
        self,
        request: main_models.ModifyScalingConfigurationRequest,
    ) -> main_models.ModifyScalingConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_scaling_configuration_with_options_async(request, runtime)

    def modify_scaling_group_with_options(
        self,
        request: main_models.ModifyScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not DaraCore.is_null(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not DaraCore.is_null(request.auto_rebalance):
            query['AutoRebalance'] = request.auto_rebalance
        if not DaraCore.is_null(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not DaraCore.is_null(request.balance_mode):
            query['BalanceMode'] = request.balance_mode
        if not DaraCore.is_null(request.capacity_options):
            query['CapacityOptions'] = request.capacity_options
        if not DaraCore.is_null(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not DaraCore.is_null(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not DaraCore.is_null(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.disable_desired_capacity):
            query['DisableDesiredCapacity'] = request.disable_desired_capacity
        if not DaraCore.is_null(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not DaraCore.is_null(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not DaraCore.is_null(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not DaraCore.is_null(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not DaraCore.is_null(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not DaraCore.is_null(request.max_size):
            query['MaxSize'] = request.max_size
        if not DaraCore.is_null(request.min_size):
            query['MinSize'] = request.min_size
        if not DaraCore.is_null(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not DaraCore.is_null(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not DaraCore.is_null(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not DaraCore.is_null(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not DaraCore.is_null(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not DaraCore.is_null(request.stop_instance_timeout):
            query['StopInstanceTimeout'] = request.stop_instance_timeout
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_group_with_options_async(
        self,
        request: main_models.ModifyScalingGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not DaraCore.is_null(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not DaraCore.is_null(request.auto_rebalance):
            query['AutoRebalance'] = request.auto_rebalance
        if not DaraCore.is_null(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not DaraCore.is_null(request.balance_mode):
            query['BalanceMode'] = request.balance_mode
        if not DaraCore.is_null(request.capacity_options):
            query['CapacityOptions'] = request.capacity_options
        if not DaraCore.is_null(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not DaraCore.is_null(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not DaraCore.is_null(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.disable_desired_capacity):
            query['DisableDesiredCapacity'] = request.disable_desired_capacity
        if not DaraCore.is_null(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not DaraCore.is_null(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not DaraCore.is_null(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not DaraCore.is_null(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not DaraCore.is_null(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not DaraCore.is_null(request.max_size):
            query['MaxSize'] = request.max_size
        if not DaraCore.is_null(request.min_size):
            query['MinSize'] = request.min_size
        if not DaraCore.is_null(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not DaraCore.is_null(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not DaraCore.is_null(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not DaraCore.is_null(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not DaraCore.is_null(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not DaraCore.is_null(request.stop_instance_timeout):
            query['StopInstanceTimeout'] = request.stop_instance_timeout
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingGroup',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_group(
        self,
        request: main_models.ModifyScalingGroupRequest,
    ) -> main_models.ModifyScalingGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    async def modify_scaling_group_async(
        self,
        request: main_models.ModifyScalingGroupRequest,
    ) -> main_models.ModifyScalingGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_scaling_group_with_options_async(request, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: main_models.ModifyScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not DaraCore.is_null(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not DaraCore.is_null(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not DaraCore.is_null(request.alarm_options):
            query['AlarmOptions'] = request.alarm_options
        if not DaraCore.is_null(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not DaraCore.is_null(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not DaraCore.is_null(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not DaraCore.is_null(request.hybrid_metrics):
            query['HybridMetrics'] = request.hybrid_metrics
        if not DaraCore.is_null(request.hybrid_monitor_namespace):
            query['HybridMonitorNamespace'] = request.hybrid_monitor_namespace
        if not DaraCore.is_null(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not DaraCore.is_null(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not DaraCore.is_null(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not DaraCore.is_null(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not DaraCore.is_null(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: main_models.ModifyScalingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not DaraCore.is_null(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not DaraCore.is_null(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not DaraCore.is_null(request.alarm_options):
            query['AlarmOptions'] = request.alarm_options
        if not DaraCore.is_null(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not DaraCore.is_null(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not DaraCore.is_null(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not DaraCore.is_null(request.hybrid_metrics):
            query['HybridMetrics'] = request.hybrid_metrics
        if not DaraCore.is_null(request.hybrid_monitor_namespace):
            query['HybridMonitorNamespace'] = request.hybrid_monitor_namespace
        if not DaraCore.is_null(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not DaraCore.is_null(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not DaraCore.is_null(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not DaraCore.is_null(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not DaraCore.is_null(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingRule',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: main_models.ModifyScalingRuleRequest,
    ) -> main_models.ModifyScalingRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    async def modify_scaling_rule_async(
        self,
        request: main_models.ModifyScalingRuleRequest,
    ) -> main_models.ModifyScalingRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_scaling_rule_with_options_async(request, runtime)

    def modify_scheduled_task_with_options(
        self,
        request: main_models.ModifyScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not DaraCore.is_null(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not DaraCore.is_null(request.max_value):
            query['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            query['MinValue'] = request.min_value
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not DaraCore.is_null(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not DaraCore.is_null(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not DaraCore.is_null(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not DaraCore.is_null(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledTask',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        request: main_models.ModifyScheduledTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not DaraCore.is_null(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not DaraCore.is_null(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not DaraCore.is_null(request.max_value):
            query['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            query['MinValue'] = request.min_value
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not DaraCore.is_null(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not DaraCore.is_null(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not DaraCore.is_null(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not DaraCore.is_null(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledTask',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        request: main_models.ModifyScheduledTaskRequest,
    ) -> main_models.ModifyScheduledTaskResponse:
        runtime = RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    async def modify_scheduled_task_async(
        self,
        request: main_models.ModifyScheduledTaskRequest,
    ) -> main_models.ModifyScheduledTaskResponse:
        runtime = RuntimeOptions()
        return await self.modify_scheduled_task_with_options_async(request, runtime)

    def query_historical_metric_with_options(
        self,
        request: main_models.QueryHistoricalMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHistoricalMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHistoricalMetric',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHistoricalMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_historical_metric_with_options_async(
        self,
        request: main_models.QueryHistoricalMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHistoricalMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHistoricalMetric',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHistoricalMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_historical_metric(
        self,
        request: main_models.QueryHistoricalMetricRequest,
    ) -> main_models.QueryHistoricalMetricResponse:
        runtime = RuntimeOptions()
        return self.query_historical_metric_with_options(request, runtime)

    async def query_historical_metric_async(
        self,
        request: main_models.QueryHistoricalMetricRequest,
    ) -> main_models.QueryHistoricalMetricResponse:
        runtime = RuntimeOptions()
        return await self.query_historical_metric_with_options_async(request, runtime)

    def query_predictive_metric_with_options(
        self,
        request: main_models.QueryPredictiveMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPredictiveMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPredictiveMetric',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPredictiveMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_predictive_metric_with_options_async(
        self,
        request: main_models.QueryPredictiveMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPredictiveMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPredictiveMetric',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPredictiveMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_predictive_metric(
        self,
        request: main_models.QueryPredictiveMetricRequest,
    ) -> main_models.QueryPredictiveMetricResponse:
        runtime = RuntimeOptions()
        return self.query_predictive_metric_with_options(request, runtime)

    async def query_predictive_metric_async(
        self,
        request: main_models.QueryPredictiveMetricRequest,
    ) -> main_models.QueryPredictiveMetricResponse:
        runtime = RuntimeOptions()
        return await self.query_predictive_metric_with_options_async(request, runtime)

    def query_predictive_task_info_with_options(
        self,
        request: main_models.QueryPredictiveTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPredictiveTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPredictiveTaskInfo',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPredictiveTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_predictive_task_info_with_options_async(
        self,
        request: main_models.QueryPredictiveTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPredictiveTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPredictiveTaskInfo',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPredictiveTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_predictive_task_info(
        self,
        request: main_models.QueryPredictiveTaskInfoRequest,
    ) -> main_models.QueryPredictiveTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.query_predictive_task_info_with_options(request, runtime)

    async def query_predictive_task_info_async(
        self,
        request: main_models.QueryPredictiveTaskInfoRequest,
    ) -> main_models.QueryPredictiveTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_predictive_task_info_with_options_async(request, runtime)

    def query_predictive_value_with_options(
        self,
        request: main_models.QueryPredictiveValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPredictiveValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPredictiveValue',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPredictiveValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_predictive_value_with_options_async(
        self,
        request: main_models.QueryPredictiveValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPredictiveValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPredictiveValue',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPredictiveValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_predictive_value(
        self,
        request: main_models.QueryPredictiveValueRequest,
    ) -> main_models.QueryPredictiveValueResponse:
        runtime = RuntimeOptions()
        return self.query_predictive_value_with_options(request, runtime)

    async def query_predictive_value_async(
        self,
        request: main_models.QueryPredictiveValueRequest,
    ) -> main_models.QueryPredictiveValueResponse:
        runtime = RuntimeOptions()
        return await self.query_predictive_value_with_options_async(request, runtime)

    def rebalance_instances_with_options(
        self,
        request: main_models.RebalanceInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebalanceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebalanceInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebalanceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_instances_with_options_async(
        self,
        request: main_models.RebalanceInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebalanceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebalanceInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebalanceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_instances(
        self,
        request: main_models.RebalanceInstancesRequest,
    ) -> main_models.RebalanceInstancesResponse:
        runtime = RuntimeOptions()
        return self.rebalance_instances_with_options(request, runtime)

    async def rebalance_instances_async(
        self,
        request: main_models.RebalanceInstancesRequest,
    ) -> main_models.RebalanceInstancesResponse:
        runtime = RuntimeOptions()
        return await self.rebalance_instances_with_options_async(request, runtime)

    def record_lifecycle_action_heartbeat_with_options(
        self,
        request: main_models.RecordLifecycleActionHeartbeatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordLifecycleActionHeartbeatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not DaraCore.is_null(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordLifecycleActionHeartbeat',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordLifecycleActionHeartbeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_lifecycle_action_heartbeat_with_options_async(
        self,
        request: main_models.RecordLifecycleActionHeartbeatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecordLifecycleActionHeartbeatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not DaraCore.is_null(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not DaraCore.is_null(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecordLifecycleActionHeartbeat',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecordLifecycleActionHeartbeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_lifecycle_action_heartbeat(
        self,
        request: main_models.RecordLifecycleActionHeartbeatRequest,
    ) -> main_models.RecordLifecycleActionHeartbeatResponse:
        runtime = RuntimeOptions()
        return self.record_lifecycle_action_heartbeat_with_options(request, runtime)

    async def record_lifecycle_action_heartbeat_async(
        self,
        request: main_models.RecordLifecycleActionHeartbeatRequest,
    ) -> main_models.RecordLifecycleActionHeartbeatResponse:
        runtime = RuntimeOptions()
        return await self.record_lifecycle_action_heartbeat_with_options_async(request, runtime)

    def remove_instances_with_options(
        self,
        tmp_req: main_models.RemoveInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveInstancesResponse:
        tmp_req.validate()
        request = main_models.RemoveInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not DaraCore.is_null(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.stop_instance_timeout):
            query['StopInstanceTimeout'] = request.stop_instance_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_instances_with_options_async(
        self,
        tmp_req: main_models.RemoveInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveInstancesResponse:
        tmp_req.validate()
        request = main_models.RemoveInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not DaraCore.is_null(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.stop_instance_timeout):
            query['StopInstanceTimeout'] = request.stop_instance_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveInstances',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_instances(
        self,
        request: main_models.RemoveInstancesRequest,
    ) -> main_models.RemoveInstancesResponse:
        runtime = RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    async def remove_instances_async(
        self,
        request: main_models.RemoveInstancesRequest,
    ) -> main_models.RemoveInstancesResponse:
        runtime = RuntimeOptions()
        return await self.remove_instances_with_options_async(request, runtime)

    def resume_instance_refresh_with_options(
        self,
        request: main_models.ResumeInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_refresh_with_options_async(
        self,
        request: main_models.ResumeInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance_refresh(
        self,
        request: main_models.ResumeInstanceRefreshRequest,
    ) -> main_models.ResumeInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return self.resume_instance_refresh_with_options(request, runtime)

    async def resume_instance_refresh_async(
        self,
        request: main_models.ResumeInstanceRefreshRequest,
    ) -> main_models.ResumeInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return await self.resume_instance_refresh_with_options_async(request, runtime)

    def resume_processes_with_options(
        self,
        request: main_models.ResumeProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeProcessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.processes):
            query['Processes'] = request.processes
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeProcesses',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_processes_with_options_async(
        self,
        request: main_models.ResumeProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeProcessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.processes):
            query['Processes'] = request.processes
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeProcesses',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_processes(
        self,
        request: main_models.ResumeProcessesRequest,
    ) -> main_models.ResumeProcessesResponse:
        runtime = RuntimeOptions()
        return self.resume_processes_with_options(request, runtime)

    async def resume_processes_async(
        self,
        request: main_models.ResumeProcessesRequest,
    ) -> main_models.ResumeProcessesResponse:
        runtime = RuntimeOptions()
        return await self.resume_processes_with_options_async(request, runtime)

    def rollback_instance_refresh_with_options(
        self,
        request: main_models.RollbackInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackInstanceRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_instance_refresh_with_options_async(
        self,
        request: main_models.RollbackInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackInstanceRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_instance_refresh(
        self,
        request: main_models.RollbackInstanceRefreshRequest,
    ) -> main_models.RollbackInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return self.rollback_instance_refresh_with_options(request, runtime)

    async def rollback_instance_refresh_async(
        self,
        request: main_models.RollbackInstanceRefreshRequest,
    ) -> main_models.RollbackInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return await self.rollback_instance_refresh_with_options_async(request, runtime)

    def scale_with_adjustment_with_options(
        self,
        tmp_req: main_models.ScaleWithAdjustmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScaleWithAdjustmentResponse:
        tmp_req.validate()
        request = main_models.ScaleWithAdjustmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        if not DaraCore.is_null(tmp_req.overrides):
            request.overrides_shrink = Utils.array_to_string_with_specified_style(tmp_req.overrides, 'Overrides', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_metadata):
            query['ActivityMetadata'] = request.activity_metadata
        if not DaraCore.is_null(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not DaraCore.is_null(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not DaraCore.is_null(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not DaraCore.is_null(request.overrides_shrink):
            query['Overrides'] = request.overrides_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parallel_task):
            query['ParallelTask'] = request.parallel_task
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleWithAdjustment',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleWithAdjustmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_with_adjustment_with_options_async(
        self,
        tmp_req: main_models.ScaleWithAdjustmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScaleWithAdjustmentResponse:
        tmp_req.validate()
        request = main_models.ScaleWithAdjustmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        if not DaraCore.is_null(tmp_req.overrides):
            request.overrides_shrink = Utils.array_to_string_with_specified_style(tmp_req.overrides, 'Overrides', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_metadata):
            query['ActivityMetadata'] = request.activity_metadata
        if not DaraCore.is_null(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not DaraCore.is_null(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not DaraCore.is_null(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not DaraCore.is_null(request.overrides_shrink):
            query['Overrides'] = request.overrides_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parallel_task):
            query['ParallelTask'] = request.parallel_task
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleWithAdjustment',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleWithAdjustmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_with_adjustment(
        self,
        request: main_models.ScaleWithAdjustmentRequest,
    ) -> main_models.ScaleWithAdjustmentResponse:
        runtime = RuntimeOptions()
        return self.scale_with_adjustment_with_options(request, runtime)

    async def scale_with_adjustment_async(
        self,
        request: main_models.ScaleWithAdjustmentRequest,
    ) -> main_models.ScaleWithAdjustmentResponse:
        runtime = RuntimeOptions()
        return await self.scale_with_adjustment_with_options_async(request, runtime)

    def set_group_deletion_protection_with_options(
        self,
        request: main_models.SetGroupDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGroupDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGroupDeletionProtection',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGroupDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_group_deletion_protection_with_options_async(
        self,
        request: main_models.SetGroupDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGroupDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGroupDeletionProtection',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGroupDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_group_deletion_protection(
        self,
        request: main_models.SetGroupDeletionProtectionRequest,
    ) -> main_models.SetGroupDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return self.set_group_deletion_protection_with_options(request, runtime)

    async def set_group_deletion_protection_async(
        self,
        request: main_models.SetGroupDeletionProtectionRequest,
    ) -> main_models.SetGroupDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return await self.set_group_deletion_protection_with_options_async(request, runtime)

    def set_instance_health_with_options(
        self,
        request: main_models.SetInstanceHealthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetInstanceHealthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetInstanceHealth',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetInstanceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instance_health_with_options_async(
        self,
        request: main_models.SetInstanceHealthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetInstanceHealthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.health_status):
            query['HealthStatus'] = request.health_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetInstanceHealth',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetInstanceHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instance_health(
        self,
        request: main_models.SetInstanceHealthRequest,
    ) -> main_models.SetInstanceHealthResponse:
        runtime = RuntimeOptions()
        return self.set_instance_health_with_options(request, runtime)

    async def set_instance_health_async(
        self,
        request: main_models.SetInstanceHealthRequest,
    ) -> main_models.SetInstanceHealthResponse:
        runtime = RuntimeOptions()
        return await self.set_instance_health_with_options_async(request, runtime)

    def set_instances_protection_with_options(
        self,
        request: main_models.SetInstancesProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetInstancesProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetInstancesProtection',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetInstancesProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instances_protection_with_options_async(
        self,
        request: main_models.SetInstancesProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetInstancesProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetInstancesProtection',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetInstancesProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instances_protection(
        self,
        request: main_models.SetInstancesProtectionRequest,
    ) -> main_models.SetInstancesProtectionResponse:
        runtime = RuntimeOptions()
        return self.set_instances_protection_with_options(request, runtime)

    async def set_instances_protection_async(
        self,
        request: main_models.SetInstancesProtectionRequest,
    ) -> main_models.SetInstancesProtectionResponse:
        runtime = RuntimeOptions()
        return await self.set_instances_protection_with_options_async(request, runtime)

    def start_instance_refresh_with_options(
        self,
        request: main_models.StartInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.checkpoint_pause_time):
            query['CheckpointPauseTime'] = request.checkpoint_pause_time
        if not DaraCore.is_null(request.checkpoints):
            query['Checkpoints'] = request.checkpoints
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.desired_configuration):
            query['DesiredConfiguration'] = request.desired_configuration
        if not DaraCore.is_null(request.max_healthy_percentage):
            query['MaxHealthyPercentage'] = request.max_healthy_percentage
        if not DaraCore.is_null(request.min_healthy_percentage):
            query['MinHealthyPercentage'] = request.min_healthy_percentage
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.skip_matching):
            query['SkipMatching'] = request.skip_matching
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_refresh_with_options_async(
        self,
        request: main_models.StartInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.checkpoint_pause_time):
            query['CheckpointPauseTime'] = request.checkpoint_pause_time
        if not DaraCore.is_null(request.checkpoints):
            query['Checkpoints'] = request.checkpoints
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.desired_configuration):
            query['DesiredConfiguration'] = request.desired_configuration
        if not DaraCore.is_null(request.max_healthy_percentage):
            query['MaxHealthyPercentage'] = request.max_healthy_percentage
        if not DaraCore.is_null(request.min_healthy_percentage):
            query['MinHealthyPercentage'] = request.min_healthy_percentage
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not DaraCore.is_null(request.skip_matching):
            query['SkipMatching'] = request.skip_matching
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance_refresh(
        self,
        request: main_models.StartInstanceRefreshRequest,
    ) -> main_models.StartInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return self.start_instance_refresh_with_options(request, runtime)

    async def start_instance_refresh_async(
        self,
        request: main_models.StartInstanceRefreshRequest,
    ) -> main_models.StartInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return await self.start_instance_refresh_with_options_async(request, runtime)

    def suspend_instance_refresh_with_options(
        self,
        request: main_models.SuspendInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendInstanceRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_instance_refresh_with_options_async(
        self,
        request: main_models.SuspendInstanceRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendInstanceRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_refresh_task_id):
            query['InstanceRefreshTaskId'] = request.instance_refresh_task_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendInstanceRefresh',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendInstanceRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_instance_refresh(
        self,
        request: main_models.SuspendInstanceRefreshRequest,
    ) -> main_models.SuspendInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return self.suspend_instance_refresh_with_options(request, runtime)

    async def suspend_instance_refresh_async(
        self,
        request: main_models.SuspendInstanceRefreshRequest,
    ) -> main_models.SuspendInstanceRefreshResponse:
        runtime = RuntimeOptions()
        return await self.suspend_instance_refresh_with_options_async(request, runtime)

    def suspend_processes_with_options(
        self,
        request: main_models.SuspendProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendProcessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.processes):
            query['Processes'] = request.processes
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendProcesses',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_processes_with_options_async(
        self,
        request: main_models.SuspendProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendProcessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.processes):
            query['Processes'] = request.processes
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendProcesses',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_processes(
        self,
        request: main_models.SuspendProcessesRequest,
    ) -> main_models.SuspendProcessesResponse:
        runtime = RuntimeOptions()
        return self.suspend_processes_with_options(request, runtime)

    async def suspend_processes_async(
        self,
        request: main_models.SuspendProcessesRequest,
    ) -> main_models.SuspendProcessesResponse:
        runtime = RuntimeOptions()
        return await self.suspend_processes_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-02-22',
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
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-02-22',
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
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-02-22',
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
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-02-22',
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

    def verify_authentication_with_options(
        self,
        request: main_models.VerifyAuthenticationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyAuthenticationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.only_check):
            query['OnlyCheck'] = request.only_check
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyAuthentication',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_authentication_with_options_async(
        self,
        request: main_models.VerifyAuthenticationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyAuthenticationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.only_check):
            query['OnlyCheck'] = request.only_check
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyAuthentication',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_authentication(
        self,
        request: main_models.VerifyAuthenticationRequest,
    ) -> main_models.VerifyAuthenticationResponse:
        runtime = RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    async def verify_authentication_async(
        self,
        request: main_models.VerifyAuthenticationRequest,
    ) -> main_models.VerifyAuthenticationResponse:
        runtime = RuntimeOptions()
        return await self.verify_authentication_with_options_async(request, runtime)

    def verify_user_with_options(
        self,
        request: main_models.VerifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyUser',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_user_with_options_async(
        self,
        request: main_models.VerifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyUser',
            version = '2022-02-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_user(
        self,
        request: main_models.VerifyUserRequest,
    ) -> main_models.VerifyUserResponse:
        runtime = RuntimeOptions()
        return self.verify_user_with_options(request, runtime)

    async def verify_user_async(
        self,
        request: main_models.VerifyUserRequest,
    ) -> main_models.VerifyUserResponse:
        runtime = RuntimeOptions()
        return await self.verify_user_with_options_async(request, runtime)
