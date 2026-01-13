# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tablestore20201209 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('tablestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_instance_2vpc_with_options(
        self,
        request: main_models.BindInstance2VpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindInstance2VpcResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_vpc_name):
            body['InstanceVpcName'] = request.instance_vpc_name
        if not DaraCore.is_null(request.virtual_switch_id):
            body['VirtualSwitchId'] = request.virtual_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindInstance2Vpc',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/bindinstance2vpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInstance2VpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_instance_2vpc_with_options_async(
        self,
        request: main_models.BindInstance2VpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindInstance2VpcResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_vpc_name):
            body['InstanceVpcName'] = request.instance_vpc_name
        if not DaraCore.is_null(request.virtual_switch_id):
            body['VirtualSwitchId'] = request.virtual_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindInstance2Vpc',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/bindinstance2vpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInstance2VpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_instance_2vpc(
        self,
        request: main_models.BindInstance2VpcRequest,
    ) -> main_models.BindInstance2VpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_instance_2vpc_with_options(request, headers, runtime)

    async def bind_instance_2vpc_async(
        self,
        request: main_models.BindInstance2VpcRequest,
    ) -> main_models.BindInstance2VpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_instance_2vpc_with_options_async(request, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/changeresourcegroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/changeresourcegroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def check_instance_policy_with_options(
        self,
        request: main_models.CheckInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstancePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstancePolicy',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/checkinstancepolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstancePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_policy_with_options_async(
        self,
        request: main_models.CheckInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstancePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstancePolicy',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/checkinstancepolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstancePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_policy(
        self,
        request: main_models.CheckInstancePolicyRequest,
    ) -> main_models.CheckInstancePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_instance_policy_with_options(request, headers, runtime)

    async def check_instance_policy_async(
        self,
        request: main_models.CheckInstancePolicyRequest,
    ) -> main_models.CheckInstancePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_instance_policy_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.disable_replication):
            body['DisableReplication'] = request.disable_replication
        if not DaraCore.is_null(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.network):
            body['Network'] = request.network
        if not DaraCore.is_null(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not DaraCore.is_null(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/createinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.disable_replication):
            body['DisableReplication'] = request.disable_replication
        if not DaraCore.is_null(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.network):
            body['Network'] = request.network
        if not DaraCore.is_null(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not DaraCore.is_null(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/createinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_vcuinstance_with_options(
        self,
        request: main_models.CreateVCUInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVCUInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias_name):
            body['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.auto_renew_period_in_month):
            body['AutoRenewPeriodInMonth'] = request.auto_renew_period_in_month
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_auto_renew):
            body['EnableAutoRenew'] = request.enable_auto_renew
        if not DaraCore.is_null(request.enable_elastic_vcu):
            body['EnableElasticVCU'] = request.enable_elastic_vcu
        if not DaraCore.is_null(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.period_in_month):
            body['PeriodInMonth'] = request.period_in_month
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.vcu):
            body['VCU'] = request.vcu
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVCUInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/createvcuinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVCUInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcuinstance_with_options_async(
        self,
        request: main_models.CreateVCUInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVCUInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias_name):
            body['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.auto_renew_period_in_month):
            body['AutoRenewPeriodInMonth'] = request.auto_renew_period_in_month
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_auto_renew):
            body['EnableAutoRenew'] = request.enable_auto_renew
        if not DaraCore.is_null(request.enable_elastic_vcu):
            body['EnableElasticVCU'] = request.enable_elastic_vcu
        if not DaraCore.is_null(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.period_in_month):
            body['PeriodInMonth'] = request.period_in_month
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.vcu):
            body['VCU'] = request.vcu
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVCUInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/createvcuinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVCUInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcuinstance(
        self,
        request: main_models.CreateVCUInstanceRequest,
    ) -> main_models.CreateVCUInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_vcuinstance_with_options(request, headers, runtime)

    async def create_vcuinstance_async(
        self,
        request: main_models.CreateVCUInstanceRequest,
    ) -> main_models.CreateVCUInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_vcuinstance_with_options_async(request, headers, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/deleteinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/deleteinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.delete_instance_with_options(request, headers, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(request, headers, runtime)

    def delete_instance_policy_with_options(
        self,
        request: main_models.DeleteInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstancePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstancePolicy',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/deleteinstancepolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstancePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_policy_with_options_async(
        self,
        request: main_models.DeleteInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstancePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstancePolicy',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/deleteinstancepolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstancePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_policy(
        self,
        request: main_models.DeleteInstancePolicyRequest,
    ) -> main_models.DeleteInstancePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_policy_with_options(request, headers, runtime)

    async def delete_instance_policy_async(
        self,
        request: main_models.DeleteInstancePolicyRequest,
    ) -> main_models.DeleteInstancePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_policy_with_options_async(request, headers, runtime)

    def delete_vcuinstance_with_options(
        self,
        request: main_models.DeleteVCUInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVCUInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVCUInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/deletevcuinstance',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVCUInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcuinstance_with_options_async(
        self,
        request: main_models.DeleteVCUInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVCUInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVCUInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/deletevcuinstance',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVCUInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcuinstance(
        self,
        request: main_models.DeleteVCUInstanceRequest,
    ) -> main_models.DeleteVCUInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_vcuinstance_with_options(request, headers, runtime)

    async def delete_vcuinstance_async(
        self,
        request: main_models.DeleteVCUInstanceRequest,
    ) -> main_models.DeleteVCUInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_vcuinstance_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/region/DescribeRegions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/region/DescribeRegions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/getinstance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/getinstance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(request, headers, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(request, headers, runtime)

    def list_cluster_type_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterTypeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListClusterType',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listclustertype',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_type_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterTypeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListClusterType',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listclustertype',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_type(self) -> main_models.ListClusterTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_type_with_options(headers, runtime)

    async def list_cluster_type_async(self) -> main_models.ListClusterTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_type_with_options_async(headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_name_list):
            request.instance_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_name_list, 'InstanceNameList', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_name_list_shrink):
            query['InstanceNameList'] = request.instance_name_list_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listinstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_name_list):
            request.instance_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_name_list, 'InstanceNameList', 'simple')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_name_list_shrink):
            query['InstanceNameList'] = request.instance_name_list_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listinstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'simple')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listtagresources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'simple')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listtagresources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_vpc_info_by_instance_with_options(
        self,
        request: main_models.ListVpcInfoByInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcInfoByInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcInfoByInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listvpcinfobyinstance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcInfoByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_info_by_instance_with_options_async(
        self,
        request: main_models.ListVpcInfoByInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcInfoByInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcInfoByInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listvpcinfobyinstance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcInfoByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_info_by_instance(
        self,
        request: main_models.ListVpcInfoByInstanceRequest,
    ) -> main_models.ListVpcInfoByInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vpc_info_by_instance_with_options(request, headers, runtime)

    async def list_vpc_info_by_instance_async(
        self,
        request: main_models.ListVpcInfoByInstanceRequest,
    ) -> main_models.ListVpcInfoByInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vpc_info_by_instance_with_options_async(request, headers, runtime)

    def list_vpc_info_by_vpc_with_options(
        self,
        request: main_models.ListVpcInfoByVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcInfoByVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcInfoByVpc',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listvpcinfobyvpc',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcInfoByVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_info_by_vpc_with_options_async(
        self,
        request: main_models.ListVpcInfoByVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcInfoByVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcInfoByVpc',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/listvpcinfobyvpc',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcInfoByVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_info_by_vpc(
        self,
        request: main_models.ListVpcInfoByVpcRequest,
    ) -> main_models.ListVpcInfoByVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vpc_info_by_vpc_with_options(request, headers, runtime)

    async def list_vpc_info_by_vpc_async(
        self,
        request: main_models.ListVpcInfoByVpcRequest,
    ) -> main_models.ListVpcInfoByVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vpc_info_by_vpc_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/tagresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/tagresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def unbind_instance_2vpc_with_options(
        self,
        request: main_models.UnbindInstance2VpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindInstance2VpcResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_vpc_name):
            body['InstanceVpcName'] = request.instance_vpc_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindInstance2Vpc',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/unbindinstance2vpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindInstance2VpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_instance_2vpc_with_options_async(
        self,
        request: main_models.UnbindInstance2VpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindInstance2VpcResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_vpc_name):
            body['InstanceVpcName'] = request.instance_vpc_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindInstance2Vpc',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/unbindinstance2vpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindInstance2VpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_instance_2vpc(
        self,
        request: main_models.UnbindInstance2VpcRequest,
    ) -> main_models.UnbindInstance2VpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_instance_2vpc_with_options(request, headers, runtime)

    async def unbind_instance_2vpc_async(
        self,
        request: main_models.UnbindInstance2VpcRequest,
    ) -> main_models.UnbindInstance2VpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_instance_2vpc_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/untagresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/untagresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias_name):
            body['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.network):
            body['Network'] = request.network
        if not DaraCore.is_null(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not DaraCore.is_null(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/updateinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias_name):
            body['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.network):
            body['Network'] = request.network
        if not DaraCore.is_null(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not DaraCore.is_null(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/updateinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(request, headers, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(request, headers, runtime)

    def update_instance_elastic_vcuupper_limit_with_options(
        self,
        request: main_models.UpdateInstanceElasticVCUUpperLimitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceElasticVCUUpperLimitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_vcuupper_limit):
            body['ElasticVCUUpperLimit'] = request.elastic_vcuupper_limit
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceElasticVCUUpperLimit',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/updateinstanceelasticvcuupperlimit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceElasticVCUUpperLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_elastic_vcuupper_limit_with_options_async(
        self,
        request: main_models.UpdateInstanceElasticVCUUpperLimitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceElasticVCUUpperLimitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_vcuupper_limit):
            body['ElasticVCUUpperLimit'] = request.elastic_vcuupper_limit
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceElasticVCUUpperLimit',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/updateinstanceelasticvcuupperlimit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceElasticVCUUpperLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_elastic_vcuupper_limit(
        self,
        request: main_models.UpdateInstanceElasticVCUUpperLimitRequest,
    ) -> main_models.UpdateInstanceElasticVCUUpperLimitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_elastic_vcuupper_limit_with_options(request, headers, runtime)

    async def update_instance_elastic_vcuupper_limit_async(
        self,
        request: main_models.UpdateInstanceElasticVCUUpperLimitRequest,
    ) -> main_models.UpdateInstanceElasticVCUUpperLimitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_elastic_vcuupper_limit_with_options_async(request, headers, runtime)

    def update_instance_policy_with_options(
        self,
        request: main_models.UpdateInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstancePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        if not DaraCore.is_null(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstancePolicy',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/updateinstancepolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstancePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_policy_with_options_async(
        self,
        request: main_models.UpdateInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstancePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        if not DaraCore.is_null(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstancePolicy',
            version = '2020-12-09',
            protocol = 'HTTPS',
            pathname = f'/v2/openapi/updateinstancepolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstancePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_policy(
        self,
        request: main_models.UpdateInstancePolicyRequest,
    ) -> main_models.UpdateInstancePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_policy_with_options(request, headers, runtime)

    async def update_instance_policy_async(
        self,
        request: main_models.UpdateInstancePolicyRequest,
    ) -> main_models.UpdateInstancePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_policy_with_options_async(request, headers, runtime)
