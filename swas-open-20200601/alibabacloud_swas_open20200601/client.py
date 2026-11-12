# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_swas_open20200601 import models as main_models
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
        self._product_id = 'SWAS-OPEN'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'swas.ap-northeast-1.aliyuncs.com',
            'ap-northeast-2': 'swas.ap-northeast-2.aliyuncs.com',
            'ap-southeast-1': 'swas.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'swas.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'swas.ap-southeast-5.aliyuncs.com',
            'ap-southeast-6': 'swas.ap-southeast-6.aliyuncs.com',
            'ap-southeast-7': 'swas.ap-southeast-7.aliyuncs.com',
            'cn-beijing': 'swas.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'swas.cn-chengdu.aliyuncs.com',
            'cn-fuzhou': 'swas.cn-fuzhou.aliyuncs.com',
            'cn-guangzhou': 'swas.cn-guangzhou.aliyuncs.com',
            'cn-hangzhou': 'swas.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'swas.cn-heyuan.aliyuncs.com',
            'cn-hongkong': 'swas.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'swas.cn-huhehaote.aliyuncs.com',
            'cn-nanjing': 'swas.cn-nanjing.aliyuncs.com',
            'cn-qingdao': 'swas.cn-qingdao.aliyuncs.com',
            'cn-shanghai': 'swas.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'swas.cn-shenzhen.aliyuncs.com',
            'cn-wuhan-lr': 'swas.cn-wuhan-lr.aliyuncs.com',
            'cn-wulanchabu': 'swas.cn-wulanchabu.aliyuncs.com',
            'cn-zhangjiakou': 'swas.cn-zhangjiakou.aliyuncs.com',
            'us-west-1': 'swas.us-west-1.aliyuncs.com',
            'us-east-1': 'swas.us-east-1.aliyuncs.com',
            'eu-west-1': 'swas.eu-west-1.aliyuncs.com',
            'eu-central-1': 'swas.eu-central-1.aliyuncs.com',
            'me-central-1': 'swas.me-central-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('swas-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_custom_image_share_account_with_options(
        self,
        request: main_models.AddCustomImageShareAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomImageShareAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomImageShareAccount',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomImageShareAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_image_share_account_with_options_async(
        self,
        request: main_models.AddCustomImageShareAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomImageShareAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomImageShareAccount',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomImageShareAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_image_share_account(
        self,
        request: main_models.AddCustomImageShareAccountRequest,
    ) -> main_models.AddCustomImageShareAccountResponse:
        runtime = RuntimeOptions()
        return self.add_custom_image_share_account_with_options(request, runtime)

    async def add_custom_image_share_account_async(
        self,
        request: main_models.AddCustomImageShareAccountRequest,
    ) -> main_models.AddCustomImageShareAccountResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_image_share_account_with_options_async(request, runtime)

    def allocate_public_connection_with_options(
        self,
        request: main_models.AllocatePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocatePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocatePublicConnection',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocatePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_connection_with_options_async(
        self,
        request: main_models.AllocatePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocatePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocatePublicConnection',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocatePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_connection(
        self,
        request: main_models.AllocatePublicConnectionRequest,
    ) -> main_models.AllocatePublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.allocate_public_connection_with_options(request, runtime)

    async def allocate_public_connection_async(
        self,
        request: main_models.AllocatePublicConnectionRequest,
    ) -> main_models.AllocatePublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.allocate_public_connection_with_options_async(request, runtime)

    def apply_firewall_template_with_options(
        self,
        request: main_models.ApplyFirewallTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyFirewallTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyFirewallTemplate',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyFirewallTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_firewall_template_with_options_async(
        self,
        request: main_models.ApplyFirewallTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyFirewallTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyFirewallTemplate',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyFirewallTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_firewall_template(
        self,
        request: main_models.ApplyFirewallTemplateRequest,
    ) -> main_models.ApplyFirewallTemplateResponse:
        runtime = RuntimeOptions()
        return self.apply_firewall_template_with_options(request, runtime)

    async def apply_firewall_template_async(
        self,
        request: main_models.ApplyFirewallTemplateRequest,
    ) -> main_models.ApplyFirewallTemplateResponse:
        runtime = RuntimeOptions()
        return await self.apply_firewall_template_with_options_async(request, runtime)

    def attach_key_pair_with_options(
        self,
        request: main_models.AttachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_key_pair_with_options_async(
        self,
        request: main_models.AttachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_key_pair(
        self,
        request: main_models.AttachKeyPairRequest,
    ) -> main_models.AttachKeyPairResponse:
        runtime = RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    async def attach_key_pair_async(
        self,
        request: main_models.AttachKeyPairRequest,
    ) -> main_models.AttachKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.attach_key_pair_with_options_async(request, runtime)

    def create_command_with_options(
        self,
        request: main_models.CreateCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_command_with_options_async(
        self,
        request: main_models.CreateCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_command(
        self,
        request: main_models.CreateCommandRequest,
    ) -> main_models.CreateCommandResponse:
        runtime = RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    async def create_command_async(
        self,
        request: main_models.CreateCommandRequest,
    ) -> main_models.CreateCommandResponse:
        runtime = RuntimeOptions()
        return await self.create_command_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: main_models.CreateCustomImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomImage',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_image_with_options_async(
        self,
        request: main_models.CreateCustomImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomImage',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_image(
        self,
        request: main_models.CreateCustomImageRequest,
    ) -> main_models.CreateCustomImageResponse:
        runtime = RuntimeOptions()
        return self.create_custom_image_with_options(request, runtime)

    async def create_custom_image_async(
        self,
        request: main_models.CreateCustomImageRequest,
    ) -> main_models.CreateCustomImageResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_image_with_options_async(request, runtime)

    def create_firewall_rule_with_options(
        self,
        request: main_models.CreateFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_rule_with_options_async(
        self,
        request: main_models.CreateFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_rule(
        self,
        request: main_models.CreateFirewallRuleRequest,
    ) -> main_models.CreateFirewallRuleResponse:
        runtime = RuntimeOptions()
        return self.create_firewall_rule_with_options(request, runtime)

    async def create_firewall_rule_async(
        self,
        request: main_models.CreateFirewallRuleRequest,
    ) -> main_models.CreateFirewallRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_firewall_rule_with_options_async(request, runtime)

    def create_firewall_rules_with_options(
        self,
        tmp_req: main_models.CreateFirewallRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallRulesResponse:
        tmp_req.validate()
        request = main_models.CreateFirewallRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.firewall_rules):
            request.firewall_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.firewall_rules, 'FirewallRules', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_rules_shrink):
            query['FirewallRules'] = request.firewall_rules_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_rules_with_options_async(
        self,
        tmp_req: main_models.CreateFirewallRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallRulesResponse:
        tmp_req.validate()
        request = main_models.CreateFirewallRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.firewall_rules):
            request.firewall_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.firewall_rules, 'FirewallRules', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_rules_shrink):
            query['FirewallRules'] = request.firewall_rules_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_rules(
        self,
        request: main_models.CreateFirewallRulesRequest,
    ) -> main_models.CreateFirewallRulesResponse:
        runtime = RuntimeOptions()
        return self.create_firewall_rules_with_options(request, runtime)

    async def create_firewall_rules_async(
        self,
        request: main_models.CreateFirewallRulesRequest,
    ) -> main_models.CreateFirewallRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_firewall_rules_with_options_async(request, runtime)

    def create_firewall_template_with_options(
        self,
        request: main_models.CreateFirewallTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallTemplate',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_template_with_options_async(
        self,
        request: main_models.CreateFirewallTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallTemplate',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_template(
        self,
        request: main_models.CreateFirewallTemplateRequest,
    ) -> main_models.CreateFirewallTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_firewall_template_with_options(request, runtime)

    async def create_firewall_template_async(
        self,
        request: main_models.CreateFirewallTemplateRequest,
    ) -> main_models.CreateFirewallTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_firewall_template_with_options_async(request, runtime)

    def create_firewall_template_rules_with_options(
        self,
        request: main_models.CreateFirewallTemplateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallTemplateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallTemplateRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallTemplateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_template_rules_with_options_async(
        self,
        request: main_models.CreateFirewallTemplateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirewallTemplateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirewallTemplateRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirewallTemplateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_template_rules(
        self,
        request: main_models.CreateFirewallTemplateRulesRequest,
    ) -> main_models.CreateFirewallTemplateRulesResponse:
        runtime = RuntimeOptions()
        return self.create_firewall_template_rules_with_options(request, runtime)

    async def create_firewall_template_rules_async(
        self,
        request: main_models.CreateFirewallTemplateRulesRequest,
    ) -> main_models.CreateFirewallTemplateRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_firewall_template_rules_with_options_async(request, runtime)

    def create_instance_key_pair_with_options(
        self,
        request: main_models.CreateInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_key_pair_with_options_async(
        self,
        request: main_models.CreateInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_key_pair(
        self,
        request: main_models.CreateInstanceKeyPairRequest,
    ) -> main_models.CreateInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return self.create_instance_key_pair_with_options(request, runtime)

    async def create_instance_key_pair_async(
        self,
        request: main_models.CreateInstanceKeyPairRequest,
    ) -> main_models.CreateInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_key_pair_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: main_models.CreateInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: main_models.CreateInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instances(
        self,
        request: main_models.CreateInstancesRequest,
    ) -> main_models.CreateInstancesResponse:
        runtime = RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    async def create_instances_async(
        self,
        request: main_models.CreateInstancesRequest,
    ) -> main_models.CreateInstancesResponse:
        runtime = RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_key_pair_with_options(
        self,
        request: main_models.CreateKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: main_models.CreateKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_pair(
        self,
        request: main_models.CreateKeyPairRequest,
    ) -> main_models.CreateKeyPairResponse:
        runtime = RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: main_models.CreateKeyPairRequest,
    ) -> main_models.CreateKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: main_models.CreateOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrder',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: main_models.CreateOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrder',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: main_models.CreateSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSnapshot',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: main_models.CreateSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSnapshot',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: main_models.CreateSnapshotRequest,
    ) -> main_models.CreateSnapshotResponse:
        runtime = RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: main_models.CreateSnapshotRequest,
    ) -> main_models.CreateSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_command_with_options(
        self,
        request: main_models.DeleteCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_command_with_options_async(
        self,
        request: main_models.DeleteCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_command(
        self,
        request: main_models.DeleteCommandRequest,
    ) -> main_models.DeleteCommandResponse:
        runtime = RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    async def delete_command_async(
        self,
        request: main_models.DeleteCommandRequest,
    ) -> main_models.DeleteCommandResponse:
        runtime = RuntimeOptions()
        return await self.delete_command_with_options_async(request, runtime)

    def delete_custom_image_with_options(
        self,
        request: main_models.DeleteCustomImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomImage',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_image_with_options_async(
        self,
        request: main_models.DeleteCustomImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomImage',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_image(
        self,
        request: main_models.DeleteCustomImageRequest,
    ) -> main_models.DeleteCustomImageResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_image_with_options(request, runtime)

    async def delete_custom_image_async(
        self,
        request: main_models.DeleteCustomImageRequest,
    ) -> main_models.DeleteCustomImageResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_image_with_options_async(request, runtime)

    def delete_custom_images_with_options(
        self,
        request: main_models.DeleteCustomImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomImages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_images_with_options_async(
        self,
        request: main_models.DeleteCustomImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomImages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_images(
        self,
        request: main_models.DeleteCustomImagesRequest,
    ) -> main_models.DeleteCustomImagesResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_images_with_options(request, runtime)

    async def delete_custom_images_async(
        self,
        request: main_models.DeleteCustomImagesRequest,
    ) -> main_models.DeleteCustomImagesResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_images_with_options_async(request, runtime)

    def delete_firewall_rule_with_options(
        self,
        request: main_models.DeleteFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_rule_with_options_async(
        self,
        request: main_models.DeleteFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_rule(
        self,
        request: main_models.DeleteFirewallRuleRequest,
    ) -> main_models.DeleteFirewallRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_firewall_rule_with_options(request, runtime)

    async def delete_firewall_rule_async(
        self,
        request: main_models.DeleteFirewallRuleRequest,
    ) -> main_models.DeleteFirewallRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_firewall_rule_with_options_async(request, runtime)

    def delete_firewall_rules_with_options(
        self,
        tmp_req: main_models.DeleteFirewallRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteFirewallRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rule_ids):
            request.rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rule_ids, 'RuleIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_ids_shrink):
            query['RuleIds'] = request.rule_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_rules_with_options_async(
        self,
        tmp_req: main_models.DeleteFirewallRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteFirewallRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rule_ids):
            request.rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rule_ids, 'RuleIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_ids_shrink):
            query['RuleIds'] = request.rule_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_rules(
        self,
        request: main_models.DeleteFirewallRulesRequest,
    ) -> main_models.DeleteFirewallRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_firewall_rules_with_options(request, runtime)

    async def delete_firewall_rules_async(
        self,
        request: main_models.DeleteFirewallRulesRequest,
    ) -> main_models.DeleteFirewallRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_firewall_rules_with_options_async(request, runtime)

    def delete_firewall_template_rules_with_options(
        self,
        request: main_models.DeleteFirewallTemplateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallTemplateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.firewall_template_rule_id):
            query['FirewallTemplateRuleId'] = request.firewall_template_rule_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallTemplateRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallTemplateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_template_rules_with_options_async(
        self,
        request: main_models.DeleteFirewallTemplateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallTemplateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.firewall_template_rule_id):
            query['FirewallTemplateRuleId'] = request.firewall_template_rule_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallTemplateRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallTemplateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_template_rules(
        self,
        request: main_models.DeleteFirewallTemplateRulesRequest,
    ) -> main_models.DeleteFirewallTemplateRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_firewall_template_rules_with_options(request, runtime)

    async def delete_firewall_template_rules_async(
        self,
        request: main_models.DeleteFirewallTemplateRulesRequest,
    ) -> main_models.DeleteFirewallTemplateRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_firewall_template_rules_with_options_async(request, runtime)

    def delete_firewall_templates_with_options(
        self,
        request: main_models.DeleteFirewallTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallTemplates',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_templates_with_options_async(
        self,
        request: main_models.DeleteFirewallTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallTemplates',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_templates(
        self,
        request: main_models.DeleteFirewallTemplatesRequest,
    ) -> main_models.DeleteFirewallTemplatesResponse:
        runtime = RuntimeOptions()
        return self.delete_firewall_templates_with_options(request, runtime)

    async def delete_firewall_templates_async(
        self,
        request: main_models.DeleteFirewallTemplatesRequest,
    ) -> main_models.DeleteFirewallTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.delete_firewall_templates_with_options_async(request, runtime)

    def delete_instance_key_pair_with_options(
        self,
        request: main_models.DeleteInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_key_pair_with_options_async(
        self,
        request: main_models.DeleteInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_key_pair(
        self,
        request: main_models.DeleteInstanceKeyPairRequest,
    ) -> main_models.DeleteInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_key_pair_with_options(request, runtime)

    async def delete_instance_key_pair_async(
        self,
        request: main_models.DeleteInstanceKeyPairRequest,
    ) -> main_models.DeleteInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_key_pair_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: main_models.DeleteKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeyPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.key_pair_names):
            query['KeyPairNames'] = request.key_pair_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyPairs',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: main_models.DeleteKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeyPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.key_pair_names):
            query['KeyPairNames'] = request.key_pair_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyPairs',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_pairs(
        self,
        request: main_models.DeleteKeyPairsRequest,
    ) -> main_models.DeleteKeyPairsResponse:
        runtime = RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: main_models.DeleteKeyPairsRequest,
    ) -> main_models.DeleteKeyPairsResponse:
        runtime = RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: main_models.DeleteSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshot',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: main_models.DeleteSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshot',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: main_models.DeleteSnapshotRequest,
    ) -> main_models.DeleteSnapshotResponse:
        runtime = RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: main_models.DeleteSnapshotRequest,
    ) -> main_models.DeleteSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_snapshots_with_options(
        self,
        request: main_models.DeleteSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshots',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshots_with_options_async(
        self,
        request: main_models.DeleteSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshots',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshots(
        self,
        request: main_models.DeleteSnapshotsRequest,
    ) -> main_models.DeleteSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.delete_snapshots_with_options(request, runtime)

    async def delete_snapshots_async(
        self,
        request: main_models.DeleteSnapshotsRequest,
    ) -> main_models.DeleteSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.delete_snapshots_with_options_async(request, runtime)

    def describe_cloud_assistant_attributes_with_options(
        self,
        tmp_req: main_models.DescribeCloudAssistantAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudAssistantAttributesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudAssistantAttributesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudAssistantAttributes',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudAssistantAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_assistant_attributes_with_options_async(
        self,
        tmp_req: main_models.DescribeCloudAssistantAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudAssistantAttributesResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudAssistantAttributesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudAssistantAttributes',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudAssistantAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_assistant_attributes(
        self,
        request: main_models.DescribeCloudAssistantAttributesRequest,
    ) -> main_models.DescribeCloudAssistantAttributesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_assistant_attributes_with_options(request, runtime)

    async def describe_cloud_assistant_attributes_async(
        self,
        request: main_models.DescribeCloudAssistantAttributesRequest,
    ) -> main_models.DescribeCloudAssistantAttributesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_assistant_attributes_with_options_async(request, runtime)

    def describe_cloud_assistant_status_with_options(
        self,
        tmp_req: main_models.DescribeCloudAssistantStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudAssistantStatusResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudAssistantStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudAssistantStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudAssistantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_assistant_status_with_options_async(
        self,
        tmp_req: main_models.DescribeCloudAssistantStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudAssistantStatusResponse:
        tmp_req.validate()
        request = main_models.DescribeCloudAssistantStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudAssistantStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudAssistantStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_assistant_status(
        self,
        request: main_models.DescribeCloudAssistantStatusRequest,
    ) -> main_models.DescribeCloudAssistantStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    async def describe_cloud_assistant_status_async(
        self,
        request: main_models.DescribeCloudAssistantStatusRequest,
    ) -> main_models.DescribeCloudAssistantStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_assistant_status_with_options_async(request, runtime)

    def describe_cloud_monitor_agent_statuses_with_options(
        self,
        request: main_models.DescribeCloudMonitorAgentStatusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudMonitorAgentStatusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudMonitorAgentStatuses',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudMonitorAgentStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_monitor_agent_statuses_with_options_async(
        self,
        request: main_models.DescribeCloudMonitorAgentStatusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudMonitorAgentStatusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudMonitorAgentStatuses',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudMonitorAgentStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_monitor_agent_statuses(
        self,
        request: main_models.DescribeCloudMonitorAgentStatusesRequest,
    ) -> main_models.DescribeCloudMonitorAgentStatusesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_monitor_agent_statuses_with_options(request, runtime)

    async def describe_cloud_monitor_agent_statuses_async(
        self,
        request: main_models.DescribeCloudMonitorAgentStatusesRequest,
    ) -> main_models.DescribeCloudMonitorAgentStatusesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_monitor_agent_statuses_with_options_async(request, runtime)

    def describe_command_invocations_with_options(
        self,
        request: main_models.DescribeCommandInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommandInvocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.command_name):
            query['CommandName'] = request.command_name
        if not DaraCore.is_null(request.command_type):
            query['CommandType'] = request.command_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invocation_status):
            query['InvocationStatus'] = request.invocation_status
        if not DaraCore.is_null(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommandInvocations',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommandInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_command_invocations_with_options_async(
        self,
        request: main_models.DescribeCommandInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommandInvocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.command_name):
            query['CommandName'] = request.command_name
        if not DaraCore.is_null(request.command_type):
            query['CommandType'] = request.command_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invocation_status):
            query['InvocationStatus'] = request.invocation_status
        if not DaraCore.is_null(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommandInvocations',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommandInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_command_invocations(
        self,
        request: main_models.DescribeCommandInvocationsRequest,
    ) -> main_models.DescribeCommandInvocationsResponse:
        runtime = RuntimeOptions()
        return self.describe_command_invocations_with_options(request, runtime)

    async def describe_command_invocations_async(
        self,
        request: main_models.DescribeCommandInvocationsRequest,
    ) -> main_models.DescribeCommandInvocationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_command_invocations_with_options_async(request, runtime)

    def describe_commands_with_options(
        self,
        request: main_models.DescribeCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommands',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_commands_with_options_async(
        self,
        request: main_models.DescribeCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommands',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_commands(
        self,
        request: main_models.DescribeCommandsRequest,
    ) -> main_models.DescribeCommandsResponse:
        runtime = RuntimeOptions()
        return self.describe_commands_with_options(request, runtime)

    async def describe_commands_async(
        self,
        request: main_models.DescribeCommandsRequest,
    ) -> main_models.DescribeCommandsResponse:
        runtime = RuntimeOptions()
        return await self.describe_commands_with_options_async(request, runtime)

    def describe_database_error_logs_with_options(
        self,
        request: main_models.DescribeDatabaseErrorLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseErrorLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseErrorLogs',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_error_logs_with_options_async(
        self,
        request: main_models.DescribeDatabaseErrorLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseErrorLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseErrorLogs',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseErrorLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_error_logs(
        self,
        request: main_models.DescribeDatabaseErrorLogsRequest,
    ) -> main_models.DescribeDatabaseErrorLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_database_error_logs_with_options(request, runtime)

    async def describe_database_error_logs_async(
        self,
        request: main_models.DescribeDatabaseErrorLogsRequest,
    ) -> main_models.DescribeDatabaseErrorLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_database_error_logs_with_options_async(request, runtime)

    def describe_database_instance_metric_data_with_options(
        self,
        request: main_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseInstanceMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseInstanceMetricData',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseInstanceMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instance_metric_data_with_options_async(
        self,
        request: main_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseInstanceMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseInstanceMetricData',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseInstanceMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instance_metric_data(
        self,
        request: main_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> main_models.DescribeDatabaseInstanceMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_database_instance_metric_data_with_options(request, runtime)

    async def describe_database_instance_metric_data_async(
        self,
        request: main_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> main_models.DescribeDatabaseInstanceMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_database_instance_metric_data_with_options_async(request, runtime)

    def describe_database_instance_parameters_with_options(
        self,
        request: main_models.DescribeDatabaseInstanceParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseInstanceParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseInstanceParameters',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseInstanceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instance_parameters_with_options_async(
        self,
        request: main_models.DescribeDatabaseInstanceParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseInstanceParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseInstanceParameters',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseInstanceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instance_parameters(
        self,
        request: main_models.DescribeDatabaseInstanceParametersRequest,
    ) -> main_models.DescribeDatabaseInstanceParametersResponse:
        runtime = RuntimeOptions()
        return self.describe_database_instance_parameters_with_options(request, runtime)

    async def describe_database_instance_parameters_async(
        self,
        request: main_models.DescribeDatabaseInstanceParametersRequest,
    ) -> main_models.DescribeDatabaseInstanceParametersResponse:
        runtime = RuntimeOptions()
        return await self.describe_database_instance_parameters_with_options_async(request, runtime)

    def describe_database_instances_with_options(
        self,
        request: main_models.DescribeDatabaseInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_ids):
            query['DatabaseInstanceIds'] = request.database_instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instances_with_options_async(
        self,
        request: main_models.DescribeDatabaseInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_ids):
            query['DatabaseInstanceIds'] = request.database_instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instances(
        self,
        request: main_models.DescribeDatabaseInstancesRequest,
    ) -> main_models.DescribeDatabaseInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_database_instances_with_options(request, runtime)

    async def describe_database_instances_async(
        self,
        request: main_models.DescribeDatabaseInstancesRequest,
    ) -> main_models.DescribeDatabaseInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_database_instances_with_options_async(request, runtime)

    def describe_database_slow_log_records_with_options(
        self,
        request: main_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseSlowLogRecords',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_slow_log_records_with_options_async(
        self,
        request: main_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatabaseSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatabaseSlowLogRecords',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatabaseSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_slow_log_records(
        self,
        request: main_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> main_models.DescribeDatabaseSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_database_slow_log_records_with_options(request, runtime)

    async def describe_database_slow_log_records_async(
        self,
        request: main_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> main_models.DescribeDatabaseSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_database_slow_log_records_with_options_async(request, runtime)

    def describe_firewall_template_apply_results_with_options(
        self,
        request: main_models.DescribeFirewallTemplateApplyResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTemplateApplyResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTemplateApplyResults',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTemplateApplyResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_template_apply_results_with_options_async(
        self,
        request: main_models.DescribeFirewallTemplateApplyResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTemplateApplyResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTemplateApplyResults',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTemplateApplyResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_template_apply_results(
        self,
        request: main_models.DescribeFirewallTemplateApplyResultsRequest,
    ) -> main_models.DescribeFirewallTemplateApplyResultsResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_template_apply_results_with_options(request, runtime)

    async def describe_firewall_template_apply_results_async(
        self,
        request: main_models.DescribeFirewallTemplateApplyResultsRequest,
    ) -> main_models.DescribeFirewallTemplateApplyResultsResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_template_apply_results_with_options_async(request, runtime)

    def describe_firewall_template_rules_apply_result_with_options(
        self,
        request: main_models.DescribeFirewallTemplateRulesApplyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTemplateRulesApplyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTemplateRulesApplyResult',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTemplateRulesApplyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_template_rules_apply_result_with_options_async(
        self,
        request: main_models.DescribeFirewallTemplateRulesApplyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTemplateRulesApplyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTemplateRulesApplyResult',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTemplateRulesApplyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_template_rules_apply_result(
        self,
        request: main_models.DescribeFirewallTemplateRulesApplyResultRequest,
    ) -> main_models.DescribeFirewallTemplateRulesApplyResultResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_template_rules_apply_result_with_options(request, runtime)

    async def describe_firewall_template_rules_apply_result_async(
        self,
        request: main_models.DescribeFirewallTemplateRulesApplyResultRequest,
    ) -> main_models.DescribeFirewallTemplateRulesApplyResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_template_rules_apply_result_with_options_async(request, runtime)

    def describe_firewall_templates_with_options(
        self,
        request: main_models.DescribeFirewallTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTemplates',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_templates_with_options_async(
        self,
        request: main_models.DescribeFirewallTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTemplates',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_templates(
        self,
        request: main_models.DescribeFirewallTemplatesRequest,
    ) -> main_models.DescribeFirewallTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_templates_with_options(request, runtime)

    async def describe_firewall_templates_async(
        self,
        request: main_models.DescribeFirewallTemplatesRequest,
    ) -> main_models.DescribeFirewallTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_templates_with_options_async(request, runtime)

    def describe_instance_key_pair_with_options(
        self,
        request: main_models.DescribeInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_key_pair_with_options_async(
        self,
        request: main_models.DescribeInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_key_pair(
        self,
        request: main_models.DescribeInstanceKeyPairRequest,
    ) -> main_models.DescribeInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_key_pair_with_options(request, runtime)

    async def describe_instance_key_pair_async(
        self,
        request: main_models.DescribeInstanceKeyPairRequest,
    ) -> main_models.DescribeInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_key_pair_with_options_async(request, runtime)

    def describe_instance_passwords_setting_with_options(
        self,
        request: main_models.DescribeInstancePasswordsSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancePasswordsSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstancePasswordsSetting',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancePasswordsSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_passwords_setting_with_options_async(
        self,
        request: main_models.DescribeInstancePasswordsSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancePasswordsSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstancePasswordsSetting',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancePasswordsSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_passwords_setting(
        self,
        request: main_models.DescribeInstancePasswordsSettingRequest,
    ) -> main_models.DescribeInstancePasswordsSettingResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_passwords_setting_with_options(request, runtime)

    async def describe_instance_passwords_setting_async(
        self,
        request: main_models.DescribeInstancePasswordsSettingRequest,
    ) -> main_models.DescribeInstancePasswordsSettingResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_passwords_setting_with_options_async(request, runtime)

    def describe_instance_vnc_url_with_options(
        self,
        request: main_models.DescribeInstanceVncUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceVncUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceVncUrl',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceVncUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_vnc_url_with_options_async(
        self,
        request: main_models.DescribeInstanceVncUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceVncUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceVncUrl',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceVncUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_vnc_url(
        self,
        request: main_models.DescribeInstanceVncUrlRequest,
    ) -> main_models.DescribeInstanceVncUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    async def describe_instance_vnc_url_async(
        self,
        request: main_models.DescribeInstanceVncUrlRequest,
    ) -> main_models.DescribeInstanceVncUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_vnc_url_with_options_async(request, runtime)

    def describe_invocation_result_with_options(
        self,
        request: main_models.DescribeInvocationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocationResult',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocation_result_with_options_async(
        self,
        request: main_models.DescribeInvocationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocationResult',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocation_result(
        self,
        request: main_models.DescribeInvocationResultRequest,
    ) -> main_models.DescribeInvocationResultResponse:
        runtime = RuntimeOptions()
        return self.describe_invocation_result_with_options(request, runtime)

    async def describe_invocation_result_async(
        self,
        request: main_models.DescribeInvocationResultRequest,
    ) -> main_models.DescribeInvocationResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_invocation_result_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: main_models.DescribeInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocations',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: main_models.DescribeInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocations',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: main_models.DescribeInvocationsRequest,
    ) -> main_models.DescribeInvocationsResponse:
        runtime = RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: main_models.DescribeInvocationsRequest,
    ) -> main_models.DescribeInvocationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_monitor_data_with_options(
        self,
        request: main_models.DescribeMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorData',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_data_with_options_async(
        self,
        request: main_models.DescribeMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorData',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_data(
        self,
        request: main_models.DescribeMonitorDataRequest,
    ) -> main_models.DescribeMonitorDataResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_data_with_options(request, runtime)

    async def describe_monitor_data_async(
        self,
        request: main_models.DescribeMonitorDataRequest,
    ) -> main_models.DescribeMonitorDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_data_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: main_models.DescribePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.commodity_type):
            query['CommodityType'] = request.commodity_type
        if not DaraCore.is_null(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.price_unit):
            query['PriceUnit'] = request.price_unit
        if not DaraCore.is_null(request.promotion_options):
            query['PromotionOptions'] = request.promotion_options
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrice',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: main_models.DescribePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.commodity_type):
            query['CommodityType'] = request.commodity_type
        if not DaraCore.is_null(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.price_unit):
            query['PriceUnit'] = request.price_unit
        if not DaraCore.is_null(request.promotion_options):
            query['PromotionOptions'] = request.promotion_options
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrice',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: main_models.DescribePriceRequest,
    ) -> main_models.DescribePriceResponse:
        runtime = RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: main_models.DescribePriceRequest,
    ) -> main_models.DescribePriceResponse:
        runtime = RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_security_agent_status_with_options(
        self,
        request: main_models.DescribeSecurityAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityAgentStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityAgentStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_agent_status_with_options_async(
        self,
        request: main_models.DescribeSecurityAgentStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityAgentStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityAgentStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_agent_status(
        self,
        request: main_models.DescribeSecurityAgentStatusRequest,
    ) -> main_models.DescribeSecurityAgentStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_security_agent_status_with_options(request, runtime)

    async def describe_security_agent_status_async(
        self,
        request: main_models.DescribeSecurityAgentStatusRequest,
    ) -> main_models.DescribeSecurityAgentStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_agent_status_with_options_async(request, runtime)

    def detach_key_pair_with_options(
        self,
        request: main_models.DetachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_key_pair_with_options_async(
        self,
        request: main_models.DetachKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_key_pair(
        self,
        request: main_models.DetachKeyPairRequest,
    ) -> main_models.DetachKeyPairResponse:
        runtime = RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    async def detach_key_pair_async(
        self,
        request: main_models.DetachKeyPairRequest,
    ) -> main_models.DetachKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def disable_firewall_rule_with_options(
        self,
        request: main_models.DisableFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_firewall_rule_with_options_async(
        self,
        request: main_models.DisableFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_firewall_rule(
        self,
        request: main_models.DisableFirewallRuleRequest,
    ) -> main_models.DisableFirewallRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_firewall_rule_with_options(request, runtime)

    async def disable_firewall_rule_async(
        self,
        request: main_models.DisableFirewallRuleRequest,
    ) -> main_models.DisableFirewallRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_firewall_rule_with_options_async(request, runtime)

    def enable_firewall_rule_with_options(
        self,
        request: main_models.EnableFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_firewall_rule_with_options_async(
        self,
        request: main_models.EnableFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_firewall_rule(
        self,
        request: main_models.EnableFirewallRuleRequest,
    ) -> main_models.EnableFirewallRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_firewall_rule_with_options(request, runtime)

    async def enable_firewall_rule_async(
        self,
        request: main_models.EnableFirewallRuleRequest,
    ) -> main_models.EnableFirewallRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_firewall_rule_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: main_models.ImportKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: main_models.ImportKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_pair(
        self,
        request: main_models.ImportKeyPairRequest,
    ) -> main_models.ImportKeyPairResponse:
        runtime = RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: main_models.ImportKeyPairRequest,
    ) -> main_models.ImportKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def install_cloud_assistant_with_options(
        self,
        tmp_req: main_models.InstallCloudAssistantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCloudAssistantResponse:
        tmp_req.validate()
        request = main_models.InstallCloudAssistantShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCloudAssistant',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCloudAssistantResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_assistant_with_options_async(
        self,
        tmp_req: main_models.InstallCloudAssistantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCloudAssistantResponse:
        tmp_req.validate()
        request = main_models.InstallCloudAssistantShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCloudAssistant',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCloudAssistantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_assistant(
        self,
        request: main_models.InstallCloudAssistantRequest,
    ) -> main_models.InstallCloudAssistantResponse:
        runtime = RuntimeOptions()
        return self.install_cloud_assistant_with_options(request, runtime)

    async def install_cloud_assistant_async(
        self,
        request: main_models.InstallCloudAssistantRequest,
    ) -> main_models.InstallCloudAssistantResponse:
        runtime = RuntimeOptions()
        return await self.install_cloud_assistant_with_options_async(request, runtime)

    def install_cloud_monitor_agent_with_options(
        self,
        request: main_models.InstallCloudMonitorAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCloudMonitorAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCloudMonitorAgent',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCloudMonitorAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_monitor_agent_with_options_async(
        self,
        request: main_models.InstallCloudMonitorAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCloudMonitorAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCloudMonitorAgent',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCloudMonitorAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_monitor_agent(
        self,
        request: main_models.InstallCloudMonitorAgentRequest,
    ) -> main_models.InstallCloudMonitorAgentResponse:
        runtime = RuntimeOptions()
        return self.install_cloud_monitor_agent_with_options(request, runtime)

    async def install_cloud_monitor_agent_async(
        self,
        request: main_models.InstallCloudMonitorAgentRequest,
    ) -> main_models.InstallCloudMonitorAgentResponse:
        runtime = RuntimeOptions()
        return await self.install_cloud_monitor_agent_with_options_async(request, runtime)

    def invoke_command_with_options(
        self,
        tmp_req: main_models.InvokeCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeCommandResponse:
        tmp_req.validate()
        request = main_models.InvokeCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_command_with_options_async(
        self,
        tmp_req: main_models.InvokeCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeCommandResponse:
        tmp_req.validate()
        request = main_models.InvokeCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_command(
        self,
        request: main_models.InvokeCommandRequest,
    ) -> main_models.InvokeCommandResponse:
        runtime = RuntimeOptions()
        return self.invoke_command_with_options(request, runtime)

    async def invoke_command_async(
        self,
        request: main_models.InvokeCommandRequest,
    ) -> main_models.InvokeCommandResponse:
        runtime = RuntimeOptions()
        return await self.invoke_command_with_options_async(request, runtime)

    def list_custom_image_share_accounts_with_options(
        self,
        request: main_models.ListCustomImageShareAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomImageShareAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomImageShareAccounts',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomImageShareAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_image_share_accounts_with_options_async(
        self,
        request: main_models.ListCustomImageShareAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomImageShareAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomImageShareAccounts',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomImageShareAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_image_share_accounts(
        self,
        request: main_models.ListCustomImageShareAccountsRequest,
    ) -> main_models.ListCustomImageShareAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_image_share_accounts_with_options(request, runtime)

    async def list_custom_image_share_accounts_async(
        self,
        request: main_models.ListCustomImageShareAccountsRequest,
    ) -> main_models.ListCustomImageShareAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_image_share_accounts_with_options_async(request, runtime)

    def list_custom_images_with_options(
        self,
        request: main_models.ListCustomImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.image_names):
            query['ImageNames'] = request.image_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share):
            query['Share'] = request.share
        if not DaraCore.is_null(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomImages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_images_with_options_async(
        self,
        request: main_models.ListCustomImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.image_names):
            query['ImageNames'] = request.image_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share):
            query['Share'] = request.share
        if not DaraCore.is_null(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomImages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_images(
        self,
        request: main_models.ListCustomImagesRequest,
    ) -> main_models.ListCustomImagesResponse:
        runtime = RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: main_models.ListCustomImagesRequest,
    ) -> main_models.ListCustomImagesResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def list_disks_with_options(
        self,
        request: main_models.ListDisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisks',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disks_with_options_async(
        self,
        request: main_models.ListDisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisks',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_disks(
        self,
        request: main_models.ListDisksRequest,
    ) -> main_models.ListDisksResponse:
        runtime = RuntimeOptions()
        return self.list_disks_with_options(request, runtime)

    async def list_disks_async(
        self,
        request: main_models.ListDisksRequest,
    ) -> main_models.ListDisksResponse:
        runtime = RuntimeOptions()
        return await self.list_disks_with_options_async(request, runtime)

    def list_firewall_rules_with_options(
        self,
        request: main_models.ListFirewallRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFirewallRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_rule_id):
            query['FirewallRuleId'] = request.firewall_rule_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFirewallRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_firewall_rules_with_options_async(
        self,
        request: main_models.ListFirewallRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFirewallRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_rule_id):
            query['FirewallRuleId'] = request.firewall_rule_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFirewallRules',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_firewall_rules(
        self,
        request: main_models.ListFirewallRulesRequest,
    ) -> main_models.ListFirewallRulesResponse:
        runtime = RuntimeOptions()
        return self.list_firewall_rules_with_options(request, runtime)

    async def list_firewall_rules_async(
        self,
        request: main_models.ListFirewallRulesRequest,
    ) -> main_models.ListFirewallRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_firewall_rules_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: main_models.ListImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: main_models.ListImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_instance_plans_modification_with_options(
        self,
        request: main_models.ListInstancePlansModificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePlansModificationResponse:
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
            action = 'ListInstancePlansModification',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePlansModificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_plans_modification_with_options_async(
        self,
        request: main_models.ListInstancePlansModificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePlansModificationResponse:
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
            action = 'ListInstancePlansModification',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePlansModificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_plans_modification(
        self,
        request: main_models.ListInstancePlansModificationRequest,
    ) -> main_models.ListInstancePlansModificationResponse:
        runtime = RuntimeOptions()
        return self.list_instance_plans_modification_with_options(request, runtime)

    async def list_instance_plans_modification_async(
        self,
        request: main_models.ListInstancePlansModificationRequest,
    ) -> main_models.ListInstancePlansModificationResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_plans_modification_with_options_async(request, runtime)

    def list_instance_status_with_options(
        self,
        request: main_models.ListInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_status_with_options_async(
        self,
        request: main_models.ListInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_status(
        self,
        request: main_models.ListInstanceStatusRequest,
    ) -> main_models.ListInstanceStatusResponse:
        runtime = RuntimeOptions()
        return self.list_instance_status_with_options(request, runtime)

    async def list_instance_status_async(
        self,
        request: main_models.ListInstanceStatusRequest,
    ) -> main_models.ListInstanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_status_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_type):
            query['PlanType'] = request.plan_type
        if not DaraCore.is_null(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_type):
            query['PlanType'] = request.plan_type
        if not DaraCore.is_null(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_instances_traffic_packages_with_options(
        self,
        request: main_models.ListInstancesTrafficPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesTrafficPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesTrafficPackages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesTrafficPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_traffic_packages_with_options_async(
        self,
        request: main_models.ListInstancesTrafficPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesTrafficPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesTrafficPackages',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesTrafficPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_traffic_packages(
        self,
        request: main_models.ListInstancesTrafficPackagesRequest,
    ) -> main_models.ListInstancesTrafficPackagesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_traffic_packages_with_options(request, runtime)

    async def list_instances_traffic_packages_async(
        self,
        request: main_models.ListInstancesTrafficPackagesRequest,
    ) -> main_models.ListInstancesTrafficPackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_traffic_packages_with_options_async(request, runtime)

    def list_key_pairs_with_options(
        self,
        request: main_models.ListKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeyPairsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeyPairs',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_key_pairs_with_options_async(
        self,
        request: main_models.ListKeyPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeyPairsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeyPairs',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_key_pairs(
        self,
        request: main_models.ListKeyPairsRequest,
    ) -> main_models.ListKeyPairsResponse:
        runtime = RuntimeOptions()
        return self.list_key_pairs_with_options(request, runtime)

    async def list_key_pairs_async(
        self,
        request: main_models.ListKeyPairsRequest,
    ) -> main_models.ListKeyPairsResponse:
        runtime = RuntimeOptions()
        return await self.list_key_pairs_with_options_async(request, runtime)

    def list_plans_with_options(
        self,
        request: main_models.ListPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlans',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plans_with_options_async(
        self,
        request: main_models.ListPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlans',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plans(
        self,
        request: main_models.ListPlansRequest,
    ) -> main_models.ListPlansResponse:
        runtime = RuntimeOptions()
        return self.list_plans_with_options(request, runtime)

    async def list_plans_async(
        self,
        request: main_models.ListPlansRequest,
    ) -> main_models.ListPlansResponse:
        runtime = RuntimeOptions()
        return await self.list_plans_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_snapshots_with_options(
        self,
        request: main_models.ListSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not DaraCore.is_null(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshots',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: main_models.ListSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not DaraCore.is_null(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshots',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshots(
        self,
        request: main_models.ListSnapshotsRequest,
    ) -> main_models.ListSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    async def list_snapshots_async(
        self,
        request: main_models.ListSnapshotsRequest,
    ) -> main_models.ListSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
            version = '2020-06-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
            version = '2020-06-01',
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

    def login_instance_with_options(
        self,
        request: main_models.LoginInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoginInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoginInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_instance_with_options_async(
        self,
        request: main_models.LoginInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoginInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoginInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login_instance(
        self,
        request: main_models.LoginInstanceRequest,
    ) -> main_models.LoginInstanceResponse:
        runtime = RuntimeOptions()
        return self.login_instance_with_options(request, runtime)

    async def login_instance_async(
        self,
        request: main_models.LoginInstanceRequest,
    ) -> main_models.LoginInstanceResponse:
        runtime = RuntimeOptions()
        return await self.login_instance_with_options_async(request, runtime)

    def modify_database_instance_description_with_options(
        self,
        request: main_models.ModifyDatabaseInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_description):
            query['DatabaseInstanceDescription'] = request.database_instance_description
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseInstanceDescription',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_instance_description_with_options_async(
        self,
        request: main_models.ModifyDatabaseInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_description):
            query['DatabaseInstanceDescription'] = request.database_instance_description
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseInstanceDescription',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_instance_description(
        self,
        request: main_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> main_models.ModifyDatabaseInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_database_instance_description_with_options(request, runtime)

    async def modify_database_instance_description_async(
        self,
        request: main_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> main_models.ModifyDatabaseInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_database_instance_description_with_options_async(request, runtime)

    def modify_database_instance_parameter_with_options(
        self,
        request: main_models.ModifyDatabaseInstanceParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseInstanceParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.force_restart):
            query['ForceRestart'] = request.force_restart
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseInstanceParameter',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseInstanceParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_instance_parameter_with_options_async(
        self,
        request: main_models.ModifyDatabaseInstanceParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseInstanceParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.force_restart):
            query['ForceRestart'] = request.force_restart
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseInstanceParameter',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseInstanceParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_instance_parameter(
        self,
        request: main_models.ModifyDatabaseInstanceParameterRequest,
    ) -> main_models.ModifyDatabaseInstanceParameterResponse:
        runtime = RuntimeOptions()
        return self.modify_database_instance_parameter_with_options(request, runtime)

    async def modify_database_instance_parameter_async(
        self,
        request: main_models.ModifyDatabaseInstanceParameterRequest,
    ) -> main_models.ModifyDatabaseInstanceParameterResponse:
        runtime = RuntimeOptions()
        return await self.modify_database_instance_parameter_with_options_async(request, runtime)

    def modify_firewall_rule_with_options(
        self,
        request: main_models.ModifyFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_firewall_rule_with_options_async(
        self,
        request: main_models.ModifyFirewallRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirewallRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirewallRule',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_firewall_rule(
        self,
        request: main_models.ModifyFirewallRuleRequest,
    ) -> main_models.ModifyFirewallRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_firewall_rule_with_options(request, runtime)

    async def modify_firewall_rule_async(
        self,
        request: main_models.ModifyFirewallRuleRequest,
    ) -> main_models.ModifyFirewallRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_firewall_rule_with_options_async(request, runtime)

    def modify_firewall_template_with_options(
        self,
        request: main_models.ModifyFirewallTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirewallTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.firewall_template_rule):
            query['FirewallTemplateRule'] = request.firewall_template_rule
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirewallTemplate',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirewallTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_firewall_template_with_options_async(
        self,
        request: main_models.ModifyFirewallTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirewallTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not DaraCore.is_null(request.firewall_template_rule):
            query['FirewallTemplateRule'] = request.firewall_template_rule
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirewallTemplate',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirewallTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_firewall_template(
        self,
        request: main_models.ModifyFirewallTemplateRequest,
    ) -> main_models.ModifyFirewallTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_firewall_template_with_options(request, runtime)

    async def modify_firewall_template_async(
        self,
        request: main_models.ModifyFirewallTemplateRequest,
    ) -> main_models.ModifyFirewallTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_firewall_template_with_options_async(request, runtime)

    def modify_image_share_status_with_options(
        self,
        request: main_models.ModifyImageShareStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyImageShareStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyImageShareStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyImageShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_share_status_with_options_async(
        self,
        request: main_models.ModifyImageShareStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyImageShareStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyImageShareStatus',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyImageShareStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_share_status(
        self,
        request: main_models.ModifyImageShareStatusRequest,
    ) -> main_models.ModifyImageShareStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_image_share_status_with_options(request, runtime)

    async def modify_image_share_status_async(
        self,
        request: main_models.ModifyImageShareStatusRequest,
    ) -> main_models.ModifyImageShareStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_image_share_status_with_options_async(request, runtime)

    def modify_instance_vnc_password_with_options(
        self,
        request: main_models.ModifyInstanceVncPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceVncPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceVncPassword',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceVncPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vnc_password_with_options_async(
        self,
        request: main_models.ModifyInstanceVncPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceVncPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceVncPassword',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceVncPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vnc_password(
        self,
        request: main_models.ModifyInstanceVncPasswordRequest,
    ) -> main_models.ModifyInstanceVncPasswordResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_vnc_password_with_options(request, runtime)

    async def modify_instance_vnc_password_async(
        self,
        request: main_models.ModifyInstanceVncPasswordRequest,
    ) -> main_models.ModifyInstanceVncPasswordResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_vnc_password_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: main_models.RebootInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: main_models.RebootInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instance(
        self,
        request: main_models.RebootInstanceRequest,
    ) -> main_models.RebootInstanceResponse:
        runtime = RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: main_models.RebootInstanceRequest,
    ) -> main_models.RebootInstanceResponse:
        runtime = RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def reboot_instances_with_options(
        self,
        request: main_models.RebootInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_reboot):
            query['ForceReboot'] = request.force_reboot
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instances_with_options_async(
        self,
        request: main_models.RebootInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_reboot):
            query['ForceReboot'] = request.force_reboot
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instances(
        self,
        request: main_models.RebootInstancesRequest,
    ) -> main_models.RebootInstancesResponse:
        runtime = RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: main_models.RebootInstancesRequest,
    ) -> main_models.RebootInstancesResponse:
        runtime = RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def release_public_connection_with_options(
        self,
        request: main_models.ReleasePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleasePublicConnection',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleasePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_connection_with_options_async(
        self,
        request: main_models.ReleasePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleasePublicConnection',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleasePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_connection(
        self,
        request: main_models.ReleasePublicConnectionRequest,
    ) -> main_models.ReleasePublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.release_public_connection_with_options(request, runtime)

    async def release_public_connection_async(
        self,
        request: main_models.ReleasePublicConnectionRequest,
    ) -> main_models.ReleasePublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.release_public_connection_with_options_async(request, runtime)

    def remove_custom_image_share_account_with_options(
        self,
        request: main_models.RemoveCustomImageShareAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveCustomImageShareAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveCustomImageShareAccount',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveCustomImageShareAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_custom_image_share_account_with_options_async(
        self,
        request: main_models.RemoveCustomImageShareAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveCustomImageShareAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveCustomImageShareAccount',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveCustomImageShareAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_custom_image_share_account(
        self,
        request: main_models.RemoveCustomImageShareAccountRequest,
    ) -> main_models.RemoveCustomImageShareAccountResponse:
        runtime = RuntimeOptions()
        return self.remove_custom_image_share_account_with_options(request, runtime)

    async def remove_custom_image_share_account_async(
        self,
        request: main_models.RemoveCustomImageShareAccountRequest,
    ) -> main_models.RemoveCustomImageShareAccountResponse:
        runtime = RuntimeOptions()
        return await self.remove_custom_image_share_account_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_database_account_password_with_options(
        self,
        request: main_models.ResetDatabaseAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDatabaseAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetDatabaseAccountPassword',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDatabaseAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_database_account_password_with_options_async(
        self,
        request: main_models.ResetDatabaseAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDatabaseAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetDatabaseAccountPassword',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDatabaseAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_database_account_password(
        self,
        request: main_models.ResetDatabaseAccountPasswordRequest,
    ) -> main_models.ResetDatabaseAccountPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_database_account_password_with_options(request, runtime)

    async def reset_database_account_password_async(
        self,
        request: main_models.ResetDatabaseAccountPasswordRequest,
    ) -> main_models.ResetDatabaseAccountPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_database_account_password_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: main_models.ResetDiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetDisk',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: main_models.ResetDiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetDisk',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_disk(
        self,
        request: main_models.ResetDiskRequest,
    ) -> main_models.ResetDiskResponse:
        runtime = RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    async def reset_disk_async(
        self,
        request: main_models.ResetDiskRequest,
    ) -> main_models.ResetDiskResponse:
        runtime = RuntimeOptions()
        return await self.reset_disk_with_options_async(request, runtime)

    def reset_system_with_options(
        self,
        request: main_models.ResetSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_credentials):
            query['LoginCredentials'] = request.login_credentials
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSystem',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_system_with_options_async(
        self,
        request: main_models.ResetSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_credentials):
            query['LoginCredentials'] = request.login_credentials
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetSystem',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_system(
        self,
        request: main_models.ResetSystemRequest,
    ) -> main_models.ResetSystemResponse:
        runtime = RuntimeOptions()
        return self.reset_system_with_options(request, runtime)

    async def reset_system_async(
        self,
        request: main_models.ResetSystemRequest,
    ) -> main_models.ResetSystemResponse:
        runtime = RuntimeOptions()
        return await self.reset_system_with_options_async(request, runtime)

    def restart_database_instance_with_options(
        self,
        request: main_models.RestartDatabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDatabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDatabaseInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_database_instance_with_options_async(
        self,
        request: main_models.RestartDatabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDatabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDatabaseInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_database_instance(
        self,
        request: main_models.RestartDatabaseInstanceRequest,
    ) -> main_models.RestartDatabaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.restart_database_instance_with_options(request, runtime)

    async def restart_database_instance_async(
        self,
        request: main_models.RestartDatabaseInstanceRequest,
    ) -> main_models.RestartDatabaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.restart_database_instance_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: main_models.RunCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommandResponse:
        tmp_req.validate()
        request = main_models.RunCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not DaraCore.is_null(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not DaraCore.is_null(request.working_user):
            query['WorkingUser'] = request.working_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: main_models.RunCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommandResponse:
        tmp_req.validate()
        request = main_models.RunCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.command_content):
            query['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not DaraCore.is_null(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not DaraCore.is_null(request.working_user):
            query['WorkingUser'] = request.working_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunCommand',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: main_models.RunCommandRequest,
    ) -> main_models.RunCommandResponse:
        runtime = RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: main_models.RunCommandRequest,
    ) -> main_models.RunCommandResponse:
        runtime = RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def start_database_instance_with_options(
        self,
        request: main_models.StartDatabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDatabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDatabaseInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_database_instance_with_options_async(
        self,
        request: main_models.StartDatabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDatabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDatabaseInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_database_instance(
        self,
        request: main_models.StartDatabaseInstanceRequest,
    ) -> main_models.StartDatabaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_database_instance_with_options(request, runtime)

    async def start_database_instance_async(
        self,
        request: main_models.StartDatabaseInstanceRequest,
    ) -> main_models.StartDatabaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_database_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2020-06-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2020-06-01',
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

    def start_instances_with_options(
        self,
        request: main_models.StartInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instances_with_options_async(
        self,
        request: main_models.StartInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instances(
        self,
        request: main_models.StartInstancesRequest,
    ) -> main_models.StartInstancesResponse:
        runtime = RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: main_models.StartInstancesRequest,
    ) -> main_models.StartInstancesResponse:
        runtime = RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def start_terminal_session_with_options(
        self,
        request: main_models.StartTerminalSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTerminalSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_line):
            query['CommandLine'] = request.command_line
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTerminalSession',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTerminalSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_terminal_session_with_options_async(
        self,
        request: main_models.StartTerminalSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTerminalSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_line):
            query['CommandLine'] = request.command_line
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTerminalSession',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTerminalSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_terminal_session(
        self,
        request: main_models.StartTerminalSessionRequest,
    ) -> main_models.StartTerminalSessionResponse:
        runtime = RuntimeOptions()
        return self.start_terminal_session_with_options(request, runtime)

    async def start_terminal_session_async(
        self,
        request: main_models.StartTerminalSessionRequest,
    ) -> main_models.StartTerminalSessionResponse:
        runtime = RuntimeOptions()
        return await self.start_terminal_session_with_options_async(request, runtime)

    def stop_database_instance_with_options(
        self,
        request: main_models.StopDatabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDatabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDatabaseInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_database_instance_with_options_async(
        self,
        request: main_models.StopDatabaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDatabaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDatabaseInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_database_instance(
        self,
        request: main_models.StopDatabaseInstanceRequest,
    ) -> main_models.StopDatabaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_database_instance_with_options(request, runtime)

    async def stop_database_instance_async(
        self,
        request: main_models.StopDatabaseInstanceRequest,
    ) -> main_models.StopDatabaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_database_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2020-06-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2020-06-01',
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

    def stop_instances_with_options(
        self,
        request: main_models.StopInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        request: main_models.StopInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstances',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instances(
        self,
        request: main_models.StopInstancesRequest,
    ) -> main_models.StopInstancesResponse:
        runtime = RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: main_models.StopInstancesRequest,
    ) -> main_models.StopInstancesResponse:
        runtime = RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
            version = '2020-06-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
            version = '2020-06-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
            version = '2020-06-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
            version = '2020-06-01',
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

    def update_command_attribute_with_options(
        self,
        request: main_models.UpdateCommandAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCommandAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCommandAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCommandAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_command_attribute_with_options_async(
        self,
        request: main_models.UpdateCommandAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCommandAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCommandAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCommandAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_command_attribute(
        self,
        request: main_models.UpdateCommandAttributeRequest,
    ) -> main_models.UpdateCommandAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_command_attribute_with_options(request, runtime)

    async def update_command_attribute_async(
        self,
        request: main_models.UpdateCommandAttributeRequest,
    ) -> main_models.UpdateCommandAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_command_attribute_with_options_async(request, runtime)

    def update_disk_attribute_with_options(
        self,
        request: main_models.UpdateDiskAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDiskAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDiskAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDiskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_disk_attribute_with_options_async(
        self,
        request: main_models.UpdateDiskAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDiskAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDiskAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDiskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_disk_attribute(
        self,
        request: main_models.UpdateDiskAttributeRequest,
    ) -> main_models.UpdateDiskAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_disk_attribute_with_options(request, runtime)

    async def update_disk_attribute_async(
        self,
        request: main_models.UpdateDiskAttributeRequest,
    ) -> main_models.UpdateDiskAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_disk_attribute_with_options_async(request, runtime)

    def update_instance_attribute_with_options(
        self,
        request: main_models.UpdateInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_attribute_with_options_async(
        self,
        request: main_models.UpdateInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_attribute(
        self,
        request: main_models.UpdateInstanceAttributeRequest,
    ) -> main_models.UpdateInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_instance_attribute_with_options(request, runtime)

    async def update_instance_attribute_async(
        self,
        request: main_models.UpdateInstanceAttributeRequest,
    ) -> main_models.UpdateInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_attribute_with_options_async(request, runtime)

    def update_snapshot_attribute_with_options(
        self,
        request: main_models.UpdateSnapshotAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSnapshotAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSnapshotAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSnapshotAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_snapshot_attribute_with_options_async(
        self,
        request: main_models.UpdateSnapshotAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSnapshotAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSnapshotAttribute',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSnapshotAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_snapshot_attribute(
        self,
        request: main_models.UpdateSnapshotAttributeRequest,
    ) -> main_models.UpdateSnapshotAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_snapshot_attribute_with_options(request, runtime)

    async def update_snapshot_attribute_async(
        self,
        request: main_models.UpdateSnapshotAttributeRequest,
    ) -> main_models.UpdateSnapshotAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_snapshot_attribute_with_options_async(request, runtime)

    def upgrade_instance_with_options(
        self,
        request: main_models.UpgradeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        request: main_models.UpgradeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeInstance',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance(
        self,
        request: main_models.UpgradeInstanceRequest,
    ) -> main_models.UpgradeInstanceResponse:
        runtime = RuntimeOptions()
        return self.upgrade_instance_with_options(request, runtime)

    async def upgrade_instance_async(
        self,
        request: main_models.UpgradeInstanceRequest,
    ) -> main_models.UpgradeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_instance_with_options_async(request, runtime)

    def upload_instance_key_pair_with_options(
        self,
        request: main_models.UploadInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_instance_key_pair_with_options_async(
        self,
        request: main_models.UploadInstanceKeyPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadInstanceKeyPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadInstanceKeyPair',
            version = '2020-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_instance_key_pair(
        self,
        request: main_models.UploadInstanceKeyPairRequest,
    ) -> main_models.UploadInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return self.upload_instance_key_pair_with_options(request, runtime)

    async def upload_instance_key_pair_async(
        self,
        request: main_models.UploadInstanceKeyPairRequest,
    ) -> main_models.UploadInstanceKeyPairResponse:
        runtime = RuntimeOptions()
        return await self.upload_instance_key_pair_with_options_async(request, runtime)
