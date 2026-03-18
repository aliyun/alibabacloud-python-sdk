# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ddosbgp20180720 import models as main_models
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
            'cn-qingdao': 'ddosbgp.aliyuncs.com',
            'cn-beijing': 'ddosbgp.aliyuncs.com',
            'cn-zhangjiakou': 'ddosbgp.aliyuncs.com',
            'cn-huhehaote': 'ddosbgp.aliyuncs.com',
            'cn-hangzhou': 'ddosbgp.aliyuncs.com',
            'cn-shanghai': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen': 'ddosbgp.aliyuncs.com',
            'ap-northeast-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'ddosbgp.aliyuncs.com',
            'eu-central-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-shanghai-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-north-2-gov-1': 'ddosbgp.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddosbgp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ip_with_options(
        self,
        request: main_models.AddIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIp',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ip_with_options_async(
        self,
        request: main_models.AddIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIp',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ip(
        self,
        request: main_models.AddIpRequest,
    ) -> main_models.AddIpResponse:
        runtime = RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    async def add_ip_async(
        self,
        request: main_models.AddIpRequest,
    ) -> main_models.AddIpResponse:
        runtime = RuntimeOptions()
        return await self.add_ip_with_options_async(request, runtime)

    def add_rd_member_list_with_options(
        self,
        tmp_req: main_models.AddRdMemberListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRdMemberListResponse:
        tmp_req.validate()
        request = main_models.AddRdMemberListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.member_list):
            request.member_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not DaraCore.is_null(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRdMemberList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRdMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rd_member_list_with_options_async(
        self,
        tmp_req: main_models.AddRdMemberListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRdMemberListResponse:
        tmp_req.validate()
        request = main_models.AddRdMemberListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.member_list):
            request.member_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not DaraCore.is_null(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRdMemberList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRdMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rd_member_list(
        self,
        request: main_models.AddRdMemberListRequest,
    ) -> main_models.AddRdMemberListResponse:
        runtime = RuntimeOptions()
        return self.add_rd_member_list_with_options(request, runtime)

    async def add_rd_member_list_async(
        self,
        request: main_models.AddRdMemberListRequest,
    ) -> main_models.AddRdMemberListResponse:
        runtime = RuntimeOptions()
        return await self.add_rd_member_list_with_options_async(request, runtime)

    def attach_asset_group_to_instance_with_options(
        self,
        tmp_req: main_models.AttachAssetGroupToInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAssetGroupToInstanceResponse:
        tmp_req.validate()
        request = main_models.AttachAssetGroupToInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_group_list):
            request.asset_group_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not DaraCore.is_null(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAssetGroupToInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAssetGroupToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_asset_group_to_instance_with_options_async(
        self,
        tmp_req: main_models.AttachAssetGroupToInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAssetGroupToInstanceResponse:
        tmp_req.validate()
        request = main_models.AttachAssetGroupToInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_group_list):
            request.asset_group_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not DaraCore.is_null(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAssetGroupToInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAssetGroupToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_asset_group_to_instance(
        self,
        request: main_models.AttachAssetGroupToInstanceRequest,
    ) -> main_models.AttachAssetGroupToInstanceResponse:
        runtime = RuntimeOptions()
        return self.attach_asset_group_to_instance_with_options(request, runtime)

    async def attach_asset_group_to_instance_async(
        self,
        request: main_models.AttachAssetGroupToInstanceRequest,
    ) -> main_models.AttachAssetGroupToInstanceResponse:
        runtime = RuntimeOptions()
        return await self.attach_asset_group_to_instance_with_options_async(request, runtime)

    def attach_to_policy_with_options(
        self,
        tmp_req: main_models.AttachToPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachToPolicyResponse:
        tmp_req.validate()
        request = main_models.AttachToPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not DaraCore.is_null(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachToPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachToPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_to_policy_with_options_async(
        self,
        tmp_req: main_models.AttachToPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachToPolicyResponse:
        tmp_req.validate()
        request = main_models.AttachToPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not DaraCore.is_null(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachToPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachToPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_to_policy(
        self,
        request: main_models.AttachToPolicyRequest,
    ) -> main_models.AttachToPolicyResponse:
        runtime = RuntimeOptions()
        return self.attach_to_policy_with_options(request, runtime)

    async def attach_to_policy_async(
        self,
        request: main_models.AttachToPolicyRequest,
    ) -> main_models.AttachToPolicyResponse:
        runtime = RuntimeOptions()
        return await self.attach_to_policy_with_options_async(request, runtime)

    def check_access_log_auth_with_options(
        self,
        request: main_models.CheckAccessLogAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccessLogAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAccessLogAuth',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccessLogAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_access_log_auth_with_options_async(
        self,
        request: main_models.CheckAccessLogAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccessLogAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAccessLogAuth',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccessLogAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_access_log_auth(
        self,
        request: main_models.CheckAccessLogAuthRequest,
    ) -> main_models.CheckAccessLogAuthResponse:
        runtime = RuntimeOptions()
        return self.check_access_log_auth_with_options(request, runtime)

    async def check_access_log_auth_async(
        self,
        request: main_models.CheckAccessLogAuthRequest,
    ) -> main_models.CheckAccessLogAuthResponse:
        runtime = RuntimeOptions()
        return await self.check_access_log_auth_with_options_async(request, runtime)

    def check_grant_with_options(
        self,
        request: main_models.CheckGrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckGrantResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckGrant',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckGrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_grant_with_options_async(
        self,
        request: main_models.CheckGrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckGrantResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckGrant',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckGrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_grant(
        self,
        request: main_models.CheckGrantRequest,
    ) -> main_models.CheckGrantResponse:
        runtime = RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    async def check_grant_async(
        self,
        request: main_models.CheckGrantRequest,
    ) -> main_models.CheckGrantResponse:
        runtime = RuntimeOptions()
        return await self.check_grant_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def delete_blackhole_with_options(
        self,
        request: main_models.DeleteBlackholeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBlackholeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBlackhole',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBlackholeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_blackhole_with_options_async(
        self,
        request: main_models.DeleteBlackholeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBlackholeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBlackhole',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBlackholeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_blackhole(
        self,
        request: main_models.DeleteBlackholeRequest,
    ) -> main_models.DeleteBlackholeResponse:
        runtime = RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    async def delete_blackhole_async(
        self,
        request: main_models.DeleteBlackholeRequest,
    ) -> main_models.DeleteBlackholeResponse:
        runtime = RuntimeOptions()
        return await self.delete_blackhole_with_options_async(request, runtime)

    def delete_ip_with_options(
        self,
        request: main_models.DeleteIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIp',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_with_options_async(
        self,
        request: main_models.DeleteIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIp',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip(
        self,
        request: main_models.DeleteIpRequest,
    ) -> main_models.DeleteIpResponse:
        runtime = RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    async def delete_ip_async(
        self,
        request: main_models.DeleteIpRequest,
    ) -> main_models.DeleteIpResponse:
        runtime = RuntimeOptions()
        return await self.delete_ip_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_rd_member_list_with_options(
        self,
        tmp_req: main_models.DeleteRdMemberListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRdMemberListResponse:
        tmp_req.validate()
        request = main_models.DeleteRdMemberListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.member_list):
            request.member_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not DaraCore.is_null(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRdMemberList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRdMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rd_member_list_with_options_async(
        self,
        tmp_req: main_models.DeleteRdMemberListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRdMemberListResponse:
        tmp_req.validate()
        request = main_models.DeleteRdMemberListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.member_list):
            request.member_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not DaraCore.is_null(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRdMemberList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRdMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rd_member_list(
        self,
        request: main_models.DeleteRdMemberListRequest,
    ) -> main_models.DeleteRdMemberListResponse:
        runtime = RuntimeOptions()
        return self.delete_rd_member_list_with_options(request, runtime)

    async def delete_rd_member_list_async(
        self,
        request: main_models.DeleteRdMemberListRequest,
    ) -> main_models.DeleteRdMemberListResponse:
        runtime = RuntimeOptions()
        return await self.delete_rd_member_list_with_options_async(request, runtime)

    def describe_asset_group_with_options(
        self,
        request: main_models.DescribeAssetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetGroup',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_group_with_options_async(
        self,
        request: main_models.DescribeAssetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetGroup',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_group(
        self,
        request: main_models.DescribeAssetGroupRequest,
    ) -> main_models.DescribeAssetGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_asset_group_with_options(request, runtime)

    async def describe_asset_group_async(
        self,
        request: main_models.DescribeAssetGroupRequest,
    ) -> main_models.DescribeAssetGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_asset_group_with_options_async(request, runtime)

    def describe_asset_group_to_instance_with_options(
        self,
        request: main_models.DescribeAssetGroupToInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetGroupToInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetGroupToInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetGroupToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_group_to_instance_with_options_async(
        self,
        request: main_models.DescribeAssetGroupToInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetGroupToInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetGroupToInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetGroupToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_group_to_instance(
        self,
        request: main_models.DescribeAssetGroupToInstanceRequest,
    ) -> main_models.DescribeAssetGroupToInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_asset_group_to_instance_with_options(request, runtime)

    async def describe_asset_group_to_instance_async(
        self,
        request: main_models.DescribeAssetGroupToInstanceRequest,
    ) -> main_models.DescribeAssetGroupToInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_asset_group_to_instance_with_options_async(request, runtime)

    def describe_ddos_event_with_options(
        self,
        request: main_models.DescribeDdosEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosEvent',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_with_options_async(
        self,
        request: main_models.DescribeDdosEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosEvent',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event(
        self,
        request: main_models.DescribeDdosEventRequest,
    ) -> main_models.DescribeDdosEventResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    async def describe_ddos_event_async(
        self,
        request: main_models.DescribeDdosEventRequest,
    ) -> main_models.DescribeDdosEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_with_options_async(request, runtime)

    def describe_ddos_origin_instance_bill_with_options(
        self,
        request: main_models.DescribeDdosOriginInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosOriginInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_show_list):
            query['IsShowList'] = request.is_show_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosOriginInstanceBill',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosOriginInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_origin_instance_bill_with_options_async(
        self,
        request: main_models.DescribeDdosOriginInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosOriginInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_show_list):
            query['IsShowList'] = request.is_show_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosOriginInstanceBill',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosOriginInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_origin_instance_bill(
        self,
        request: main_models.DescribeDdosOriginInstanceBillRequest,
    ) -> main_models.DescribeDdosOriginInstanceBillResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_origin_instance_bill_with_options(request, runtime)

    async def describe_ddos_origin_instance_bill_async(
        self,
        request: main_models.DescribeDdosOriginInstanceBillRequest,
    ) -> main_models.DescribeDdosOriginInstanceBillResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_origin_instance_bill_with_options_async(request, runtime)

    def describe_excpetion_count_with_options(
        self,
        request: main_models.DescribeExcpetionCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExcpetionCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExcpetionCount',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExcpetionCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_excpetion_count_with_options_async(
        self,
        request: main_models.DescribeExcpetionCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExcpetionCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExcpetionCount',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExcpetionCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_excpetion_count(
        self,
        request: main_models.DescribeExcpetionCountRequest,
    ) -> main_models.DescribeExcpetionCountResponse:
        runtime = RuntimeOptions()
        return self.describe_excpetion_count_with_options(request, runtime)

    async def describe_excpetion_count_async(
        self,
        request: main_models.DescribeExcpetionCountRequest,
    ) -> main_models.DescribeExcpetionCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_excpetion_count_with_options_async(request, runtime)

    def describe_instance_list_with_options(
        self,
        request: main_models.DescribeInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.orderby):
            query['Orderby'] = request.orderby
        if not DaraCore.is_null(request.orderdire):
            query['Orderdire'] = request.orderdire
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_list_with_options_async(
        self,
        request: main_models.DescribeInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.orderby):
            query['Orderby'] = request.orderby
        if not DaraCore.is_null(request.orderdire):
            query['Orderdire'] = request.orderdire
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_list(
        self,
        request: main_models.DescribeInstanceListRequest,
    ) -> main_models.DescribeInstanceListResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    async def describe_instance_list_async(
        self,
        request: main_models.DescribeInstanceListRequest,
    ) -> main_models.DescribeInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_list_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecs',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecs',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_specs(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
    ) -> main_models.DescribeInstanceSpecsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
    ) -> main_models.DescribeInstanceSpecsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: main_models.DescribeOpEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.op_action):
            query['OpAction'] = request.op_action
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_dir):
            query['OrderDir'] = request.order_dir
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpEntities',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: main_models.DescribeOpEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.op_action):
            query['OpAction'] = request.op_action
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_dir):
            query['OrderDir'] = request.order_dir
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpEntities',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_op_entities(
        self,
        request: main_models.DescribeOpEntitiesRequest,
    ) -> main_models.DescribeOpEntitiesResponse:
        runtime = RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: main_models.DescribeOpEntitiesRequest,
    ) -> main_models.DescribeOpEntitiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_pack_ip_list_with_options(
        self,
        request: main_models.DescribePackIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackIpList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pack_ip_list_with_options_async(
        self,
        request: main_models.DescribePackIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackIpListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackIpList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pack_ip_list(
        self,
        request: main_models.DescribePackIpListRequest,
    ) -> main_models.DescribePackIpListResponse:
        runtime = RuntimeOptions()
        return self.describe_pack_ip_list_with_options(request, runtime)

    async def describe_pack_ip_list_async(
        self,
        request: main_models.DescribePackIpListRequest,
    ) -> main_models.DescribePackIpListResponse:
        runtime = RuntimeOptions()
        return await self.describe_pack_ip_list_with_options_async(request, runtime)

    def describe_rd_member_list_with_options(
        self,
        request: main_models.DescribeRdMemberListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdMemberListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_directory_id):
            query['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdMemberList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rd_member_list_with_options_async(
        self,
        request: main_models.DescribeRdMemberListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdMemberListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_directory_id):
            query['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdMemberList',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rd_member_list(
        self,
        request: main_models.DescribeRdMemberListRequest,
    ) -> main_models.DescribeRdMemberListResponse:
        runtime = RuntimeOptions()
        return self.describe_rd_member_list_with_options(request, runtime)

    async def describe_rd_member_list_async(
        self,
        request: main_models.DescribeRdMemberListRequest,
    ) -> main_models.DescribeRdMemberListResponse:
        runtime = RuntimeOptions()
        return await self.describe_rd_member_list_with_options_async(request, runtime)

    def describe_rd_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRdStatus',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rd_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRdStatus',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rd_status(self) -> main_models.DescribeRdStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_rd_status_with_options(runtime)

    async def describe_rd_status_async(self) -> main_models.DescribeRdStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_rd_status_with_options_async(runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-07-20',
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

    def describe_traffic_with_options(
        self,
        request: main_models.DescribeTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.flow_type):
            query['FlowType'] = request.flow_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ipnet):
            query['Ipnet'] = request.ipnet
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTraffic',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_with_options_async(
        self,
        request: main_models.DescribeTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.flow_type):
            query['FlowType'] = request.flow_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.ipnet):
            query['Ipnet'] = request.ipnet
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTraffic',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic(
        self,
        request: main_models.DescribeTrafficRequest,
    ) -> main_models.DescribeTrafficResponse:
        runtime = RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    async def describe_traffic_async(
        self,
        request: main_models.DescribeTrafficRequest,
    ) -> main_models.DescribeTrafficResponse:
        runtime = RuntimeOptions()
        return await self.describe_traffic_with_options_async(request, runtime)

    def detach_from_policy_with_options(
        self,
        tmp_req: main_models.DetachFromPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachFromPolicyResponse:
        tmp_req.validate()
        request = main_models.DetachFromPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not DaraCore.is_null(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachFromPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachFromPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_from_policy_with_options_async(
        self,
        tmp_req: main_models.DetachFromPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachFromPolicyResponse:
        tmp_req.validate()
        request = main_models.DetachFromPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not DaraCore.is_null(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachFromPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachFromPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_from_policy(
        self,
        request: main_models.DetachFromPolicyRequest,
    ) -> main_models.DetachFromPolicyResponse:
        runtime = RuntimeOptions()
        return self.detach_from_policy_with_options(request, runtime)

    async def detach_from_policy_async(
        self,
        request: main_models.DetachFromPolicyRequest,
    ) -> main_models.DetachFromPolicyResponse:
        runtime = RuntimeOptions()
        return await self.detach_from_policy_with_options_async(request, runtime)

    def dettach_asset_group_to_instance_with_options(
        self,
        tmp_req: main_models.DettachAssetGroupToInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DettachAssetGroupToInstanceResponse:
        tmp_req.validate()
        request = main_models.DettachAssetGroupToInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_group_list):
            request.asset_group_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not DaraCore.is_null(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DettachAssetGroupToInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DettachAssetGroupToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def dettach_asset_group_to_instance_with_options_async(
        self,
        tmp_req: main_models.DettachAssetGroupToInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DettachAssetGroupToInstanceResponse:
        tmp_req.validate()
        request = main_models.DettachAssetGroupToInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_group_list):
            request.asset_group_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not DaraCore.is_null(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DettachAssetGroupToInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DettachAssetGroupToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dettach_asset_group_to_instance(
        self,
        request: main_models.DettachAssetGroupToInstanceRequest,
    ) -> main_models.DettachAssetGroupToInstanceResponse:
        runtime = RuntimeOptions()
        return self.dettach_asset_group_to_instance_with_options(request, runtime)

    async def dettach_asset_group_to_instance_async(
        self,
        request: main_models.DettachAssetGroupToInstanceRequest,
    ) -> main_models.DettachAssetGroupToInstanceResponse:
        runtime = RuntimeOptions()
        return await self.dettach_asset_group_to_instance_with_options_async(request, runtime)

    def get_sls_open_status_with_options(
        self,
        request: main_models.GetSlsOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSlsOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSlsOpenStatus',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sls_open_status_with_options_async(
        self,
        request: main_models.GetSlsOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSlsOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSlsOpenStatus',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSlsOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sls_open_status(
        self,
        request: main_models.GetSlsOpenStatusRequest,
    ) -> main_models.GetSlsOpenStatusResponse:
        runtime = RuntimeOptions()
        return self.get_sls_open_status_with_options(request, runtime)

    async def get_sls_open_status_async(
        self,
        request: main_models.GetSlsOpenStatusRequest,
    ) -> main_models.GetSlsOpenStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_sls_open_status_with_options_async(request, runtime)

    def list_opened_access_log_instances_with_options(
        self,
        request: main_models.ListOpenedAccessLogInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOpenedAccessLogInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOpenedAccessLogInstances',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOpenedAccessLogInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_opened_access_log_instances_with_options_async(
        self,
        request: main_models.ListOpenedAccessLogInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOpenedAccessLogInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOpenedAccessLogInstances',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOpenedAccessLogInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_opened_access_log_instances(
        self,
        request: main_models.ListOpenedAccessLogInstancesRequest,
    ) -> main_models.ListOpenedAccessLogInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_opened_access_log_instances_with_options(request, runtime)

    async def list_opened_access_log_instances_async(
        self,
        request: main_models.ListOpenedAccessLogInstancesRequest,
    ) -> main_models.ListOpenedAccessLogInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_opened_access_log_instances_with_options_async(request, runtime)

    def list_policy_with_options(
        self,
        request: main_models.ListPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_with_options_async(
        self,
        request: main_models.ListPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy(
        self,
        request: main_models.ListPolicyRequest,
    ) -> main_models.ListPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_policy_with_options(request, runtime)

    async def list_policy_async(
        self,
        request: main_models.ListPolicyRequest,
    ) -> main_models.ListPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_with_options_async(request, runtime)

    def list_policy_attachment_with_options(
        self,
        tmp_req: main_models.ListPolicyAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyAttachmentResponse:
        tmp_req.validate()
        request = main_models.ListPolicyAttachmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not DaraCore.is_null(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyAttachment',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_attachment_with_options_async(
        self,
        tmp_req: main_models.ListPolicyAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyAttachmentResponse:
        tmp_req.validate()
        request = main_models.ListPolicyAttachmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not DaraCore.is_null(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyAttachment',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_attachment(
        self,
        request: main_models.ListPolicyAttachmentRequest,
    ) -> main_models.ListPolicyAttachmentResponse:
        runtime = RuntimeOptions()
        return self.list_policy_attachment_with_options(request, runtime)

    async def list_policy_attachment_async(
        self,
        request: main_models.ListPolicyAttachmentRequest,
    ) -> main_models.ListPolicyAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_attachment_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2018-07-20',
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

    def modify_policy_with_options(
        self,
        tmp_req: main_models.ModifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyResponse:
        tmp_req.validate()
        request = main_models.ModifyPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_with_options_async(
        self,
        tmp_req: main_models.ModifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyResponse:
        tmp_req.validate()
        request = main_models.ModifyPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicy',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy(
        self,
        request: main_models.ModifyPolicyRequest,
    ) -> main_models.ModifyPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: main_models.ModifyPolicyRequest,
    ) -> main_models.ModifyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def modify_policy_content_with_options(
        self,
        tmp_req: main_models.ModifyPolicyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyContentResponse:
        tmp_req.validate()
        request = main_models.ModifyPolicyContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyContent',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_content_with_options_async(
        self,
        tmp_req: main_models.ModifyPolicyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyContentResponse:
        tmp_req.validate()
        request = main_models.ModifyPolicyContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content):
            request.content_shrink = Utils.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not DaraCore.is_null(request.content_shrink):
            query['Content'] = request.content_shrink
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_version):
            query['PortVersion'] = request.port_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyContent',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_content(
        self,
        request: main_models.ModifyPolicyContentRequest,
    ) -> main_models.ModifyPolicyContentResponse:
        runtime = RuntimeOptions()
        return self.modify_policy_content_with_options(request, runtime)

    async def modify_policy_content_async(
        self,
        request: main_models.ModifyPolicyContentRequest,
    ) -> main_models.ModifyPolicyContentResponse:
        runtime = RuntimeOptions()
        return await self.modify_policy_content_with_options_async(request, runtime)

    def modify_remark_with_options(
        self,
        request: main_models.ModifyRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRemark',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_remark_with_options_async(
        self,
        request: main_models.ModifyRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRemark',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_remark(
        self,
        request: main_models.ModifyRemarkRequest,
    ) -> main_models.ModifyRemarkResponse:
        runtime = RuntimeOptions()
        return self.modify_remark_with_options(request, runtime)

    async def modify_remark_async(
        self,
        request: main_models.ModifyRemarkRequest,
    ) -> main_models.ModifyRemarkResponse:
        runtime = RuntimeOptions()
        return await self.modify_remark_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def release_ddos_origin_instance_with_options(
        self,
        request: main_models.ReleaseDdosOriginInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseDdosOriginInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseDdosOriginInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseDdosOriginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_ddos_origin_instance_with_options_async(
        self,
        request: main_models.ReleaseDdosOriginInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseDdosOriginInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseDdosOriginInstance',
            version = '2018-07-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseDdosOriginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_ddos_origin_instance(
        self,
        request: main_models.ReleaseDdosOriginInstanceRequest,
    ) -> main_models.ReleaseDdosOriginInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_ddos_origin_instance_with_options(request, runtime)

    async def release_ddos_origin_instance_async(
        self,
        request: main_models.ReleaseDdosOriginInstanceRequest,
    ) -> main_models.ReleaseDdosOriginInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_ddos_origin_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2018-07-20',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2018-07-20',
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
