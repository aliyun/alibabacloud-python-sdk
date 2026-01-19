# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudapi20160714 import models as main_models
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
            'cn-qingdao': 'apigateway.cn-qingdao.aliyuncs.com',
            'cn-beijing': 'apigateway.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'apigateway.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'apigateway.cn-huhehaote.aliyuncs.com',
            'cn-wulanchabu': 'apigateway.cn-wulanchabu.aliyuncs.com',
            'cn-hangzhou': 'apigateway.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'apigateway.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'apigateway.cn-shenzhen.aliyuncs.com',
            'cn-heyuan': 'apigateway.cn-heyuan.aliyuncs.com',
            'cn-guangzhou': 'apigateway.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'apigateway.cn-chengdu.aliyuncs.com',
            'cn-hongkong': 'apigateway.cn-hongkong.aliyuncs.com',
            'ap-northeast-1': 'apigateway.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'apigateway.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'apigateway.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'apigateway.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'apigateway.ap-southeast-5.aliyuncs.com',
            'ap-southeast-6': 'apigateway.ap-southeast-6.aliyuncs.com',
            'ap-southeast-7': 'apigateway.ap-southeast-7.aliyuncs.com',
            'us-east-1': 'apigateway.us-east-1.aliyuncs.com',
            'us-west-1': 'apigateway.us-west-1.aliyuncs.com',
            'eu-west-1': 'apigateway.eu-west-1.aliyuncs.com',
            'eu-central-1': 'apigateway.eu-central-1.aliyuncs.com',
            'ap-south-1': 'apigateway.ap-south-1.aliyuncs.com',
            'me-east-1': 'apigateway.me-east-1.aliyuncs.com',
            'me-central-1': 'apigateway.me-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'apigateway.cn-hangzhou-finance.aliyuncs.com',
            'cn-shanghai-finance-1': 'apigateway.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shenzhen-finance-1': 'apigateway.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-north-2-gov-1': 'apigateway.cn-north-2-gov-1.aliyuncs.com',
            'ap-northeast-2-pop': 'apigateway.aliyuncs.com',
            'cn-beijing-finance-1': 'apigateway.cn-beijing-finance-1.aliyuncs.com',
            'cn-beijing-finance-pop': 'apigateway.aliyuncs.com',
            'cn-beijing-gov-1': 'apigateway.aliyuncs.com',
            'cn-beijing-nu16-b01': 'apigateway.aliyuncs.com',
            'cn-edge-1': 'apigateway.aliyuncs.com',
            'cn-fujian': 'apigateway.aliyuncs.com',
            'cn-haidian-cm12-c01': 'apigateway.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'apigateway.aliyuncs.com',
            'cn-hangzhou-test-306': 'apigateway.aliyuncs.com',
            'cn-hongkong-finance-pop': 'apigateway.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'apigateway.aliyuncs.com',
            'cn-qingdao-nebula': 'apigateway.aliyuncs.com',
            'cn-shanghai-et15-b01': 'apigateway.aliyuncs.com',
            'cn-shanghai-et2-b01': 'apigateway.aliyuncs.com',
            'cn-shanghai-inner': 'apigateway.cn-shanghai-inner.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'apigateway.aliyuncs.com',
            'cn-shenzhen-inner': 'apigateway.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'apigateway.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'apigateway.aliyuncs.com',
            'cn-wuhan': 'apigateway.aliyuncs.com',
            'cn-yushanfang': 'apigateway.aliyuncs.com',
            'cn-zhangbei': 'apigateway.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'apigateway.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'apigateway.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'apigateway.aliyuncs.com',
            'eu-west-1-oxs': 'apigateway.aliyuncs.com',
            'rus-west-1-pop': 'apigateway.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_api_with_options(
        self,
        request: main_models.AbolishApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbolishApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbolishApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbolishApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_api_with_options_async(
        self,
        request: main_models.AbolishApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AbolishApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbolishApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbolishApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_api(
        self,
        request: main_models.AbolishApiRequest,
    ) -> main_models.AbolishApiResponse:
        runtime = RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    async def abolish_api_async(
        self,
        request: main_models.AbolishApiRequest,
    ) -> main_models.AbolishApiResponse:
        runtime = RuntimeOptions()
        return await self.abolish_api_with_options_async(request, runtime)

    def add_access_control_list_entry_with_options(
        self,
        request: main_models.AddAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAccessControlListEntry',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_access_control_list_entry_with_options_async(
        self,
        request: main_models.AddAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAccessControlListEntry',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAccessControlListEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_access_control_list_entry(
        self,
        request: main_models.AddAccessControlListEntryRequest,
    ) -> main_models.AddAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return self.add_access_control_list_entry_with_options(request, runtime)

    async def add_access_control_list_entry_async(
        self,
        request: main_models.AddAccessControlListEntryRequest,
    ) -> main_models.AddAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return await self.add_access_control_list_entry_with_options_async(request, runtime)

    def add_ip_control_policy_item_with_options(
        self,
        request: main_models.AddIpControlPolicyItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpControlPolicyItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpControlPolicyItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ip_control_policy_item_with_options_async(
        self,
        request: main_models.AddIpControlPolicyItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpControlPolicyItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpControlPolicyItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ip_control_policy_item(
        self,
        request: main_models.AddIpControlPolicyItemRequest,
    ) -> main_models.AddIpControlPolicyItemResponse:
        runtime = RuntimeOptions()
        return self.add_ip_control_policy_item_with_options(request, runtime)

    async def add_ip_control_policy_item_async(
        self,
        request: main_models.AddIpControlPolicyItemRequest,
    ) -> main_models.AddIpControlPolicyItemResponse:
        runtime = RuntimeOptions()
        return await self.add_ip_control_policy_item_with_options_async(request, runtime)

    def add_traffic_special_control_with_options(
        self,
        request: main_models.AddTrafficSpecialControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTrafficSpecialControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.special_key):
            query['SpecialKey'] = request.special_key
        if not DaraCore.is_null(request.special_type):
            query['SpecialType'] = request.special_type
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not DaraCore.is_null(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTrafficSpecialControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_traffic_special_control_with_options_async(
        self,
        request: main_models.AddTrafficSpecialControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTrafficSpecialControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.special_key):
            query['SpecialKey'] = request.special_key
        if not DaraCore.is_null(request.special_type):
            query['SpecialType'] = request.special_type
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not DaraCore.is_null(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTrafficSpecialControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_traffic_special_control(
        self,
        request: main_models.AddTrafficSpecialControlRequest,
    ) -> main_models.AddTrafficSpecialControlResponse:
        runtime = RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    async def add_traffic_special_control_async(
        self,
        request: main_models.AddTrafficSpecialControlRequest,
    ) -> main_models.AddTrafficSpecialControlResponse:
        runtime = RuntimeOptions()
        return await self.add_traffic_special_control_with_options_async(request, runtime)

    def associate_instance_with_private_dnswith_options(
        self,
        tmp_req: main_models.AssociateInstanceWithPrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateInstanceWithPrivateDNSResponse:
        tmp_req.validate()
        request = main_models.AssociateInstanceWithPrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intranet_domains):
            request.intranet_domains_shrink = Utils.array_to_string_with_specified_style(tmp_req.intranet_domains, 'IntranetDomains', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.intranet_domains_shrink):
            body['IntranetDomains'] = request.intranet_domains_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateInstanceWithPrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateInstanceWithPrivateDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_instance_with_private_dnswith_options_async(
        self,
        tmp_req: main_models.AssociateInstanceWithPrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateInstanceWithPrivateDNSResponse:
        tmp_req.validate()
        request = main_models.AssociateInstanceWithPrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intranet_domains):
            request.intranet_domains_shrink = Utils.array_to_string_with_specified_style(tmp_req.intranet_domains, 'IntranetDomains', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.intranet_domains_shrink):
            body['IntranetDomains'] = request.intranet_domains_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateInstanceWithPrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateInstanceWithPrivateDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_instance_with_private_dns(
        self,
        request: main_models.AssociateInstanceWithPrivateDNSRequest,
    ) -> main_models.AssociateInstanceWithPrivateDNSResponse:
        runtime = RuntimeOptions()
        return self.associate_instance_with_private_dnswith_options(request, runtime)

    async def associate_instance_with_private_dns_async(
        self,
        request: main_models.AssociateInstanceWithPrivateDNSRequest,
    ) -> main_models.AssociateInstanceWithPrivateDNSResponse:
        runtime = RuntimeOptions()
        return await self.associate_instance_with_private_dnswith_options_async(request, runtime)

    def attach_api_product_with_options(
        self,
        request: main_models.AttachApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.apis):
            query['Apis'] = request.apis
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_api_product_with_options_async(
        self,
        request: main_models.AttachApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.apis):
            query['Apis'] = request.apis
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachApiProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_api_product(
        self,
        request: main_models.AttachApiProductRequest,
    ) -> main_models.AttachApiProductResponse:
        runtime = RuntimeOptions()
        return self.attach_api_product_with_options(request, runtime)

    async def attach_api_product_async(
        self,
        request: main_models.AttachApiProductRequest,
    ) -> main_models.AttachApiProductResponse:
        runtime = RuntimeOptions()
        return await self.attach_api_product_with_options_async(request, runtime)

    def attach_group_plugin_with_options(
        self,
        request: main_models.AttachGroupPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachGroupPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachGroupPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachGroupPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_group_plugin_with_options_async(
        self,
        request: main_models.AttachGroupPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachGroupPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachGroupPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachGroupPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_group_plugin(
        self,
        request: main_models.AttachGroupPluginRequest,
    ) -> main_models.AttachGroupPluginResponse:
        runtime = RuntimeOptions()
        return self.attach_group_plugin_with_options(request, runtime)

    async def attach_group_plugin_async(
        self,
        request: main_models.AttachGroupPluginRequest,
    ) -> main_models.AttachGroupPluginResponse:
        runtime = RuntimeOptions()
        return await self.attach_group_plugin_with_options_async(request, runtime)

    def attach_plugin_with_options(
        self,
        request: main_models.AttachPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_plugin_with_options_async(
        self,
        request: main_models.AttachPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_plugin(
        self,
        request: main_models.AttachPluginRequest,
    ) -> main_models.AttachPluginResponse:
        runtime = RuntimeOptions()
        return self.attach_plugin_with_options(request, runtime)

    async def attach_plugin_async(
        self,
        request: main_models.AttachPluginRequest,
    ) -> main_models.AttachPluginResponse:
        runtime = RuntimeOptions()
        return await self.attach_plugin_with_options_async(request, runtime)

    def batch_abolish_apis_with_options(
        self,
        request: main_models.BatchAbolishApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAbolishApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAbolishApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAbolishApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_abolish_apis_with_options_async(
        self,
        request: main_models.BatchAbolishApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAbolishApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAbolishApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAbolishApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_abolish_apis(
        self,
        request: main_models.BatchAbolishApisRequest,
    ) -> main_models.BatchAbolishApisResponse:
        runtime = RuntimeOptions()
        return self.batch_abolish_apis_with_options(request, runtime)

    async def batch_abolish_apis_async(
        self,
        request: main_models.BatchAbolishApisRequest,
    ) -> main_models.BatchAbolishApisResponse:
        runtime = RuntimeOptions()
        return await self.batch_abolish_apis_with_options_async(request, runtime)

    def batch_deploy_apis_with_options(
        self,
        request: main_models.BatchDeployApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeployApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeployApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeployApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_deploy_apis_with_options_async(
        self,
        request: main_models.BatchDeployApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeployApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api):
            query['Api'] = request.api
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeployApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeployApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_deploy_apis(
        self,
        request: main_models.BatchDeployApisRequest,
    ) -> main_models.BatchDeployApisResponse:
        runtime = RuntimeOptions()
        return self.batch_deploy_apis_with_options(request, runtime)

    async def batch_deploy_apis_async(
        self,
        request: main_models.BatchDeployApisRequest,
    ) -> main_models.BatchDeployApisResponse:
        runtime = RuntimeOptions()
        return await self.batch_deploy_apis_with_options_async(request, runtime)

    def create_access_control_list_with_options(
        self,
        request: main_models.CreateAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessControlList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_control_list_with_options_async(
        self,
        request: main_models.CreateAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessControlList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_control_list(
        self,
        request: main_models.CreateAccessControlListRequest,
    ) -> main_models.CreateAccessControlListResponse:
        runtime = RuntimeOptions()
        return self.create_access_control_list_with_options(request, runtime)

    async def create_access_control_list_async(
        self,
        request: main_models.CreateAccessControlListRequest,
    ) -> main_models.CreateAccessControlListResponse:
        runtime = RuntimeOptions()
        return await self.create_access_control_list_with_options_async(request, runtime)

    def create_api_with_options(
        self,
        request: main_models.CreateApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_enable):
            query['BackendEnable'] = request.backend_enable
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not DaraCore.is_null(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not DaraCore.is_null(request.request_config):
            query['RequestConfig'] = request.request_config
        if not DaraCore.is_null(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        if not DaraCore.is_null(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        body = {}
        if not DaraCore.is_null(request.constant_parameters):
            body['ConstantParameters'] = request.constant_parameters
        if not DaraCore.is_null(request.error_code_samples):
            body['ErrorCodeSamples'] = request.error_code_samples
        if not DaraCore.is_null(request.fail_result_sample):
            body['FailResultSample'] = request.fail_result_sample
        if not DaraCore.is_null(request.request_parameters):
            body['RequestParameters'] = request.request_parameters
        if not DaraCore.is_null(request.result_descriptions):
            body['ResultDescriptions'] = request.result_descriptions
        if not DaraCore.is_null(request.result_sample):
            body['ResultSample'] = request.result_sample
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        if not DaraCore.is_null(request.service_parameters_map):
            body['ServiceParametersMap'] = request.service_parameters_map
        if not DaraCore.is_null(request.system_parameters):
            body['SystemParameters'] = request.system_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_with_options_async(
        self,
        request: main_models.CreateApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_enable):
            query['BackendEnable'] = request.backend_enable
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not DaraCore.is_null(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not DaraCore.is_null(request.request_config):
            query['RequestConfig'] = request.request_config
        if not DaraCore.is_null(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        if not DaraCore.is_null(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        body = {}
        if not DaraCore.is_null(request.constant_parameters):
            body['ConstantParameters'] = request.constant_parameters
        if not DaraCore.is_null(request.error_code_samples):
            body['ErrorCodeSamples'] = request.error_code_samples
        if not DaraCore.is_null(request.fail_result_sample):
            body['FailResultSample'] = request.fail_result_sample
        if not DaraCore.is_null(request.request_parameters):
            body['RequestParameters'] = request.request_parameters
        if not DaraCore.is_null(request.result_descriptions):
            body['ResultDescriptions'] = request.result_descriptions
        if not DaraCore.is_null(request.result_sample):
            body['ResultSample'] = request.result_sample
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        if not DaraCore.is_null(request.service_parameters_map):
            body['ServiceParametersMap'] = request.service_parameters_map
        if not DaraCore.is_null(request.system_parameters):
            body['SystemParameters'] = request.system_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api(
        self,
        request: main_models.CreateApiRequest,
    ) -> main_models.CreateApiResponse:
        runtime = RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    async def create_api_async(
        self,
        request: main_models.CreateApiRequest,
    ) -> main_models.CreateApiResponse:
        runtime = RuntimeOptions()
        return await self.create_api_with_options_async(request, runtime)

    def create_api_group_with_options(
        self,
        request: main_models.CreateApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_path):
            query['BasePath'] = request.base_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_group_with_options_async(
        self,
        request: main_models.CreateApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_path):
            query['BasePath'] = request.base_path
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_group(
        self,
        request: main_models.CreateApiGroupRequest,
    ) -> main_models.CreateApiGroupResponse:
        runtime = RuntimeOptions()
        return self.create_api_group_with_options(request, runtime)

    async def create_api_group_async(
        self,
        request: main_models.CreateApiGroupRequest,
    ) -> main_models.CreateApiGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_api_group_with_options_async(request, runtime)

    def create_api_stage_variable_with_options(
        self,
        request: main_models.CreateApiStageVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiStageVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_id):
            query['StageId'] = request.stage_id
        if not DaraCore.is_null(request.stage_route_model):
            query['StageRouteModel'] = request.stage_route_model
        if not DaraCore.is_null(request.support_route):
            query['SupportRoute'] = request.support_route
        if not DaraCore.is_null(request.variable_name):
            query['VariableName'] = request.variable_name
        if not DaraCore.is_null(request.variable_value):
            query['VariableValue'] = request.variable_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiStageVariable',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_stage_variable_with_options_async(
        self,
        request: main_models.CreateApiStageVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiStageVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_id):
            query['StageId'] = request.stage_id
        if not DaraCore.is_null(request.stage_route_model):
            query['StageRouteModel'] = request.stage_route_model
        if not DaraCore.is_null(request.support_route):
            query['SupportRoute'] = request.support_route
        if not DaraCore.is_null(request.variable_name):
            query['VariableName'] = request.variable_name
        if not DaraCore.is_null(request.variable_value):
            query['VariableValue'] = request.variable_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiStageVariable',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiStageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_stage_variable(
        self,
        request: main_models.CreateApiStageVariableRequest,
    ) -> main_models.CreateApiStageVariableResponse:
        runtime = RuntimeOptions()
        return self.create_api_stage_variable_with_options(request, runtime)

    async def create_api_stage_variable_async(
        self,
        request: main_models.CreateApiStageVariableRequest,
    ) -> main_models.CreateApiStageVariableResponse:
        runtime = RuntimeOptions()
        return await self.create_api_stage_variable_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_code_with_options(
        self,
        request: main_models.CreateAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_code_with_options_async(
        self,
        request: main_models.CreateAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_code(
        self,
        request: main_models.CreateAppCodeRequest,
    ) -> main_models.CreateAppCodeResponse:
        runtime = RuntimeOptions()
        return self.create_app_code_with_options(request, runtime)

    async def create_app_code_async(
        self,
        request: main_models.CreateAppCodeRequest,
    ) -> main_models.CreateAppCodeResponse:
        runtime = RuntimeOptions()
        return await self.create_app_code_with_options_async(request, runtime)

    def create_app_key_with_options(
        self,
        request: main_models.CreateAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_secret):
            query['AppSecret'] = request.app_secret
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppKey',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_key_with_options_async(
        self,
        request: main_models.CreateAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_secret):
            query['AppSecret'] = request.app_secret
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppKey',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_key(
        self,
        request: main_models.CreateAppKeyRequest,
    ) -> main_models.CreateAppKeyResponse:
        runtime = RuntimeOptions()
        return self.create_app_key_with_options(request, runtime)

    async def create_app_key_async(
        self,
        request: main_models.CreateAppKeyRequest,
    ) -> main_models.CreateAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_app_key_with_options_async(request, runtime)

    def create_backend_with_options(
        self,
        request: main_models.CreateBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.create_event_bridge_service_linked_role):
            query['CreateEventBridgeServiceLinkedRole'] = request.create_event_bridge_service_linked_role
        if not DaraCore.is_null(request.create_slr):
            query['CreateSlr'] = request.create_slr
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backend_with_options_async(
        self,
        request: main_models.CreateBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.create_event_bridge_service_linked_role):
            query['CreateEventBridgeServiceLinkedRole'] = request.create_event_bridge_service_linked_role
        if not DaraCore.is_null(request.create_slr):
            query['CreateSlr'] = request.create_slr
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backend(
        self,
        request: main_models.CreateBackendRequest,
    ) -> main_models.CreateBackendResponse:
        runtime = RuntimeOptions()
        return self.create_backend_with_options(request, runtime)

    async def create_backend_async(
        self,
        request: main_models.CreateBackendRequest,
    ) -> main_models.CreateBackendResponse:
        runtime = RuntimeOptions()
        return await self.create_backend_with_options_async(request, runtime)

    def create_backend_model_with_options(
        self,
        request: main_models.CreateBackendModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackendModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_model_data):
            query['BackendModelData'] = request.backend_model_data
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackendModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackendModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backend_model_with_options_async(
        self,
        request: main_models.CreateBackendModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackendModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_model_data):
            query['BackendModelData'] = request.backend_model_data
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackendModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackendModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backend_model(
        self,
        request: main_models.CreateBackendModelRequest,
    ) -> main_models.CreateBackendModelResponse:
        runtime = RuntimeOptions()
        return self.create_backend_model_with_options(request, runtime)

    async def create_backend_model_async(
        self,
        request: main_models.CreateBackendModelRequest,
    ) -> main_models.CreateBackendModelResponse:
        runtime = RuntimeOptions()
        return await self.create_backend_model_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        request: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            query['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            query['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_dataset_item_with_options(
        self,
        request: main_models.CreateDatasetItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_item_with_options_async(
        self,
        request: main_models.CreateDatasetItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasetItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset_item(
        self,
        request: main_models.CreateDatasetItemRequest,
    ) -> main_models.CreateDatasetItemResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_item_with_options(request, runtime)

    async def create_dataset_item_async(
        self,
        request: main_models.CreateDatasetItemRequest,
    ) -> main_models.CreateDatasetItemResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_item_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not DaraCore.is_null(request.instance_cidr):
            query['InstanceCidr'] = request.instance_cidr
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_vpc_id):
            query['UserVpcId'] = request.user_vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.zone_vswitch_security_group):
            query['ZoneVSwitchSecurityGroup'] = request.zone_vswitch_security_group
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not DaraCore.is_null(request.instance_cidr):
            query['InstanceCidr'] = request.instance_cidr
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_vpc_id):
            query['UserVpcId'] = request.user_vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.zone_vswitch_security_group):
            query['ZoneVSwitchSecurityGroup'] = request.zone_vswitch_security_group
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_intranet_domain_with_options(
        self,
        request: main_models.CreateIntranetDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntranetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntranetDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntranetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intranet_domain_with_options_async(
        self,
        request: main_models.CreateIntranetDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntranetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntranetDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntranetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intranet_domain(
        self,
        request: main_models.CreateIntranetDomainRequest,
    ) -> main_models.CreateIntranetDomainResponse:
        runtime = RuntimeOptions()
        return self.create_intranet_domain_with_options(request, runtime)

    async def create_intranet_domain_async(
        self,
        request: main_models.CreateIntranetDomainRequest,
    ) -> main_models.CreateIntranetDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_intranet_domain_with_options_async(request, runtime)

    def create_ip_control_with_options(
        self,
        request: main_models.CreateIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not DaraCore.is_null(request.ip_control_policys):
            query['IpControlPolicys'] = request.ip_control_policys
        if not DaraCore.is_null(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ip_control_with_options_async(
        self,
        request: main_models.CreateIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not DaraCore.is_null(request.ip_control_policys):
            query['IpControlPolicys'] = request.ip_control_policys
        if not DaraCore.is_null(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ip_control(
        self,
        request: main_models.CreateIpControlRequest,
    ) -> main_models.CreateIpControlResponse:
        runtime = RuntimeOptions()
        return self.create_ip_control_with_options(request, runtime)

    async def create_ip_control_async(
        self,
        request: main_models.CreateIpControlRequest,
    ) -> main_models.CreateIpControlResponse:
        runtime = RuntimeOptions()
        return await self.create_ip_control_with_options_async(request, runtime)

    def create_log_config_with_options(
        self,
        request: main_models.CreateLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_slr):
            query['CreateSlr'] = request.create_slr
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not DaraCore.is_null(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_config_with_options_async(
        self,
        request: main_models.CreateLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_slr):
            query['CreateSlr'] = request.create_slr
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not DaraCore.is_null(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_config(
        self,
        request: main_models.CreateLogConfigRequest,
    ) -> main_models.CreateLogConfigResponse:
        runtime = RuntimeOptions()
        return self.create_log_config_with_options(request, runtime)

    async def create_log_config_async(
        self,
        request: main_models.CreateLogConfigRequest,
    ) -> main_models.CreateLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_log_config_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        request: main_models.CreateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: main_models.CreateModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_monitor_group_with_options(
        self,
        request: main_models.CreateMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth):
            query['Auth'] = request.auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.raw_monitor_group_id):
            query['RawMonitorGroupId'] = request.raw_monitor_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_with_options_async(
        self,
        request: main_models.CreateMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth):
            query['Auth'] = request.auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.raw_monitor_group_id):
            query['RawMonitorGroupId'] = request.raw_monitor_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group(
        self,
        request: main_models.CreateMonitorGroupRequest,
    ) -> main_models.CreateMonitorGroupResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    async def create_monitor_group_async(
        self,
        request: main_models.CreateMonitorGroupRequest,
    ) -> main_models.CreateMonitorGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_group_with_options_async(request, runtime)

    def create_plugin_with_options(
        self,
        request: main_models.CreatePluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.plugin_data):
            query['PluginData'] = request.plugin_data
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_with_options_async(
        self,
        request: main_models.CreatePluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.plugin_data):
            query['PluginData'] = request.plugin_data
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin(
        self,
        request: main_models.CreatePluginRequest,
    ) -> main_models.CreatePluginResponse:
        runtime = RuntimeOptions()
        return self.create_plugin_with_options(request, runtime)

    async def create_plugin_async(
        self,
        request: main_models.CreatePluginRequest,
    ) -> main_models.CreatePluginResponse:
        runtime = RuntimeOptions()
        return await self.create_plugin_with_options_async(request, runtime)

    def create_private_dnswith_options(
        self,
        tmp_req: main_models.CreatePrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateDNSResponse:
        tmp_req.validate()
        request = main_models.CreatePrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.records):
            request.records_shrink = Utils.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.records_shrink):
            body['Records'] = request.records_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_dnswith_options_async(
        self,
        tmp_req: main_models.CreatePrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateDNSResponse:
        tmp_req.validate()
        request = main_models.CreatePrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.records):
            request.records_shrink = Utils.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.records_shrink):
            body['Records'] = request.records_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_dns(
        self,
        request: main_models.CreatePrivateDNSRequest,
    ) -> main_models.CreatePrivateDNSResponse:
        runtime = RuntimeOptions()
        return self.create_private_dnswith_options(request, runtime)

    async def create_private_dns_async(
        self,
        request: main_models.CreatePrivateDNSRequest,
    ) -> main_models.CreatePrivateDNSResponse:
        runtime = RuntimeOptions()
        return await self.create_private_dnswith_options_async(request, runtime)

    def create_signature_with_options(
        self,
        request: main_models.CreateSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_key):
            query['SignatureKey'] = request.signature_key
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        if not DaraCore.is_null(request.signature_secret):
            query['SignatureSecret'] = request.signature_secret
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_signature_with_options_async(
        self,
        request: main_models.CreateSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_key):
            query['SignatureKey'] = request.signature_key
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        if not DaraCore.is_null(request.signature_secret):
            query['SignatureSecret'] = request.signature_secret
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_signature(
        self,
        request: main_models.CreateSignatureRequest,
    ) -> main_models.CreateSignatureResponse:
        runtime = RuntimeOptions()
        return self.create_signature_with_options(request, runtime)

    async def create_signature_async(
        self,
        request: main_models.CreateSignatureRequest,
    ) -> main_models.CreateSignatureResponse:
        runtime = RuntimeOptions()
        return await self.create_signature_with_options_async(request, runtime)

    def create_traffic_control_with_options(
        self,
        request: main_models.CreateTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_default):
            query['ApiDefault'] = request.api_default
        if not DaraCore.is_null(request.app_default):
            query['AppDefault'] = request.app_default
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not DaraCore.is_null(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not DaraCore.is_null(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_with_options_async(
        self,
        request: main_models.CreateTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_default):
            query['ApiDefault'] = request.api_default
        if not DaraCore.is_null(request.app_default):
            query['AppDefault'] = request.app_default
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not DaraCore.is_null(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not DaraCore.is_null(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control(
        self,
        request: main_models.CreateTrafficControlRequest,
    ) -> main_models.CreateTrafficControlResponse:
        runtime = RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    async def create_traffic_control_async(
        self,
        request: main_models.CreateTrafficControlRequest,
    ) -> main_models.CreateTrafficControlResponse:
        runtime = RuntimeOptions()
        return await self.create_traffic_control_with_options_async(request, runtime)

    def delete_access_control_list_with_options(
        self,
        request: main_models.DeleteAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessControlList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_control_list_with_options_async(
        self,
        request: main_models.DeleteAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessControlList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_control_list(
        self,
        request: main_models.DeleteAccessControlListRequest,
    ) -> main_models.DeleteAccessControlListResponse:
        runtime = RuntimeOptions()
        return self.delete_access_control_list_with_options(request, runtime)

    async def delete_access_control_list_async(
        self,
        request: main_models.DeleteAccessControlListRequest,
    ) -> main_models.DeleteAccessControlListResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_control_list_with_options_async(request, runtime)

    def delete_all_traffic_special_control_with_options(
        self,
        request: main_models.DeleteAllTrafficSpecialControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllTrafficSpecialControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAllTrafficSpecialControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_traffic_special_control_with_options_async(
        self,
        request: main_models.DeleteAllTrafficSpecialControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAllTrafficSpecialControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAllTrafficSpecialControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAllTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_traffic_special_control(
        self,
        request: main_models.DeleteAllTrafficSpecialControlRequest,
    ) -> main_models.DeleteAllTrafficSpecialControlResponse:
        runtime = RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    async def delete_all_traffic_special_control_async(
        self,
        request: main_models.DeleteAllTrafficSpecialControlRequest,
    ) -> main_models.DeleteAllTrafficSpecialControlResponse:
        runtime = RuntimeOptions()
        return await self.delete_all_traffic_special_control_with_options_async(request, runtime)

    def delete_api_with_options(
        self,
        request: main_models.DeleteApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_with_options_async(
        self,
        request: main_models.DeleteApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api(
        self,
        request: main_models.DeleteApiRequest,
    ) -> main_models.DeleteApiResponse:
        runtime = RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    async def delete_api_async(
        self,
        request: main_models.DeleteApiRequest,
    ) -> main_models.DeleteApiResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_with_options_async(request, runtime)

    def delete_api_group_with_options(
        self,
        request: main_models.DeleteApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_group_with_options_async(
        self,
        request: main_models.DeleteApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_group(
        self,
        request: main_models.DeleteApiGroupRequest,
    ) -> main_models.DeleteApiGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    async def delete_api_group_async(
        self,
        request: main_models.DeleteApiGroupRequest,
    ) -> main_models.DeleteApiGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_group_with_options_async(request, runtime)

    def delete_api_product_with_options(
        self,
        request: main_models.DeleteApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_product_with_options_async(
        self,
        request: main_models.DeleteApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_product(
        self,
        request: main_models.DeleteApiProductRequest,
    ) -> main_models.DeleteApiProductResponse:
        runtime = RuntimeOptions()
        return self.delete_api_product_with_options(request, runtime)

    async def delete_api_product_async(
        self,
        request: main_models.DeleteApiProductRequest,
    ) -> main_models.DeleteApiProductResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_product_with_options_async(request, runtime)

    def delete_api_stage_variable_with_options(
        self,
        request: main_models.DeleteApiStageVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiStageVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_id):
            query['StageId'] = request.stage_id
        if not DaraCore.is_null(request.variable_name):
            query['VariableName'] = request.variable_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiStageVariable',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_stage_variable_with_options_async(
        self,
        request: main_models.DeleteApiStageVariableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiStageVariableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_id):
            query['StageId'] = request.stage_id
        if not DaraCore.is_null(request.variable_name):
            query['VariableName'] = request.variable_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiStageVariable',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiStageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_stage_variable(
        self,
        request: main_models.DeleteApiStageVariableRequest,
    ) -> main_models.DeleteApiStageVariableResponse:
        runtime = RuntimeOptions()
        return self.delete_api_stage_variable_with_options(request, runtime)

    async def delete_api_stage_variable_async(
        self,
        request: main_models.DeleteApiStageVariableRequest,
    ) -> main_models.DeleteApiStageVariableResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_stage_variable_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: main_models.DeleteAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: main_models.DeleteAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: main_models.DeleteAppRequest,
    ) -> main_models.DeleteAppResponse:
        runtime = RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: main_models.DeleteAppRequest,
    ) -> main_models.DeleteAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_app_code_with_options(
        self,
        request: main_models.DeleteAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_code_with_options_async(
        self,
        request: main_models.DeleteAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_code(
        self,
        request: main_models.DeleteAppCodeRequest,
    ) -> main_models.DeleteAppCodeResponse:
        runtime = RuntimeOptions()
        return self.delete_app_code_with_options(request, runtime)

    async def delete_app_code_async(
        self,
        request: main_models.DeleteAppCodeRequest,
    ) -> main_models.DeleteAppCodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_code_with_options_async(request, runtime)

    def delete_app_key_with_options(
        self,
        request: main_models.DeleteAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppKey',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_key_with_options_async(
        self,
        request: main_models.DeleteAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppKey',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_key(
        self,
        request: main_models.DeleteAppKeyRequest,
    ) -> main_models.DeleteAppKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_app_key_with_options(request, runtime)

    async def delete_app_key_async(
        self,
        request: main_models.DeleteAppKeyRequest,
    ) -> main_models.DeleteAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_key_with_options_async(request, runtime)

    def delete_backend_with_options(
        self,
        request: main_models.DeleteBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backend_with_options_async(
        self,
        request: main_models.DeleteBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backend(
        self,
        request: main_models.DeleteBackendRequest,
    ) -> main_models.DeleteBackendResponse:
        runtime = RuntimeOptions()
        return self.delete_backend_with_options(request, runtime)

    async def delete_backend_async(
        self,
        request: main_models.DeleteBackendRequest,
    ) -> main_models.DeleteBackendResponse:
        runtime = RuntimeOptions()
        return await self.delete_backend_with_options_async(request, runtime)

    def delete_backend_model_with_options(
        self,
        request: main_models.DeleteBackendModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackendModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_model_id):
            query['BackendModelId'] = request.backend_model_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackendModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackendModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backend_model_with_options_async(
        self,
        request: main_models.DeleteBackendModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackendModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_model_id):
            query['BackendModelId'] = request.backend_model_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackendModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackendModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backend_model(
        self,
        request: main_models.DeleteBackendModelRequest,
    ) -> main_models.DeleteBackendModelResponse:
        runtime = RuntimeOptions()
        return self.delete_backend_model_with_options(request, runtime)

    async def delete_backend_model_async(
        self,
        request: main_models.DeleteBackendModelRequest,
    ) -> main_models.DeleteBackendModelResponse:
        runtime = RuntimeOptions()
        return await self.delete_backend_model_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_dataset_item_with_options(
        self,
        request: main_models.DeleteDatasetItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_item_with_options_async(
        self,
        request: main_models.DeleteDatasetItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_item(
        self,
        request: main_models.DeleteDatasetItemRequest,
    ) -> main_models.DeleteDatasetItemResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_item_with_options(request, runtime)

    async def delete_dataset_item_async(
        self,
        request: main_models.DeleteDatasetItemRequest,
    ) -> main_models.DeleteDatasetItemResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_item_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_certificate_with_options(
        self,
        request: main_models.DeleteDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainCertificate',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_certificate_with_options_async(
        self,
        request: main_models.DeleteDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainCertificate',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_certificate(
        self,
        request: main_models.DeleteDomainCertificateRequest,
    ) -> main_models.DeleteDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_certificate_with_options(request, runtime)

    async def delete_domain_certificate_async(
        self,
        request: main_models.DeleteDomainCertificateRequest,
    ) -> main_models.DeleteDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_certificate_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2016-07-14',
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2016-07-14',
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

    def delete_ip_control_with_options(
        self,
        request: main_models.DeleteIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_control_with_options_async(
        self,
        request: main_models.DeleteIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip_control(
        self,
        request: main_models.DeleteIpControlRequest,
    ) -> main_models.DeleteIpControlResponse:
        runtime = RuntimeOptions()
        return self.delete_ip_control_with_options(request, runtime)

    async def delete_ip_control_async(
        self,
        request: main_models.DeleteIpControlRequest,
    ) -> main_models.DeleteIpControlResponse:
        runtime = RuntimeOptions()
        return await self.delete_ip_control_with_options_async(request, runtime)

    def delete_log_config_with_options(
        self,
        request: main_models.DeleteLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_config_with_options_async(
        self,
        request: main_models.DeleteLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_config(
        self,
        request: main_models.DeleteLogConfigRequest,
    ) -> main_models.DeleteLogConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_log_config_with_options(request, runtime)

    async def delete_log_config_async(
        self,
        request: main_models.DeleteLogConfigRequest,
    ) -> main_models.DeleteLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_log_config_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: main_models.DeleteModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: main_models.DeleteModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def delete_monitor_group_with_options(
        self,
        request: main_models.DeleteMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.raw_monitor_group_id):
            query['RawMonitorGroupId'] = request.raw_monitor_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_with_options_async(
        self,
        request: main_models.DeleteMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.raw_monitor_group_id):
            query['RawMonitorGroupId'] = request.raw_monitor_group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group(
        self,
        request: main_models.DeleteMonitorGroupRequest,
    ) -> main_models.DeleteMonitorGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_monitor_group_with_options(request, runtime)

    async def delete_monitor_group_async(
        self,
        request: main_models.DeleteMonitorGroupRequest,
    ) -> main_models.DeleteMonitorGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_monitor_group_with_options_async(request, runtime)

    def delete_plugin_with_options(
        self,
        request: main_models.DeletePluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_with_options_async(
        self,
        request: main_models.DeletePluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin(
        self,
        request: main_models.DeletePluginRequest,
    ) -> main_models.DeletePluginResponse:
        runtime = RuntimeOptions()
        return self.delete_plugin_with_options(request, runtime)

    async def delete_plugin_async(
        self,
        request: main_models.DeletePluginRequest,
    ) -> main_models.DeletePluginResponse:
        runtime = RuntimeOptions()
        return await self.delete_plugin_with_options_async(request, runtime)

    def delete_private_dnswith_options(
        self,
        request: main_models.DeletePrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_dnswith_options_async(
        self,
        request: main_models.DeletePrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_dns(
        self,
        request: main_models.DeletePrivateDNSRequest,
    ) -> main_models.DeletePrivateDNSResponse:
        runtime = RuntimeOptions()
        return self.delete_private_dnswith_options(request, runtime)

    async def delete_private_dns_async(
        self,
        request: main_models.DeletePrivateDNSRequest,
    ) -> main_models.DeletePrivateDNSResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_dnswith_options_async(request, runtime)

    def delete_signature_with_options(
        self,
        request: main_models.DeleteSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_signature_with_options_async(
        self,
        request: main_models.DeleteSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_signature(
        self,
        request: main_models.DeleteSignatureRequest,
    ) -> main_models.DeleteSignatureResponse:
        runtime = RuntimeOptions()
        return self.delete_signature_with_options(request, runtime)

    async def delete_signature_async(
        self,
        request: main_models.DeleteSignatureRequest,
    ) -> main_models.DeleteSignatureResponse:
        runtime = RuntimeOptions()
        return await self.delete_signature_with_options_async(request, runtime)

    def delete_traffic_control_with_options(
        self,
        request: main_models.DeleteTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_with_options_async(
        self,
        request: main_models.DeleteTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control(
        self,
        request: main_models.DeleteTrafficControlRequest,
    ) -> main_models.DeleteTrafficControlResponse:
        runtime = RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    async def delete_traffic_control_async(
        self,
        request: main_models.DeleteTrafficControlRequest,
    ) -> main_models.DeleteTrafficControlResponse:
        runtime = RuntimeOptions()
        return await self.delete_traffic_control_with_options_async(request, runtime)

    def delete_traffic_special_control_with_options(
        self,
        request: main_models.DeleteTrafficSpecialControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficSpecialControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.special_key):
            query['SpecialKey'] = request.special_key
        if not DaraCore.is_null(request.special_type):
            query['SpecialType'] = request.special_type
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficSpecialControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_special_control_with_options_async(
        self,
        request: main_models.DeleteTrafficSpecialControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficSpecialControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.special_key):
            query['SpecialKey'] = request.special_key
        if not DaraCore.is_null(request.special_type):
            query['SpecialType'] = request.special_type
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficSpecialControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_special_control(
        self,
        request: main_models.DeleteTrafficSpecialControlRequest,
    ) -> main_models.DeleteTrafficSpecialControlResponse:
        runtime = RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    async def delete_traffic_special_control_async(
        self,
        request: main_models.DeleteTrafficSpecialControlRequest,
    ) -> main_models.DeleteTrafficSpecialControlResponse:
        runtime = RuntimeOptions()
        return await self.delete_traffic_special_control_with_options_async(request, runtime)

    def deploy_api_with_options(
        self,
        request: main_models.DeployApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_api_with_options_async(
        self,
        request: main_models.DeployApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_api(
        self,
        request: main_models.DeployApiRequest,
    ) -> main_models.DeployApiResponse:
        runtime = RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    async def deploy_api_async(
        self,
        request: main_models.DeployApiRequest,
    ) -> main_models.DeployApiResponse:
        runtime = RuntimeOptions()
        return await self.deploy_api_with_options_async(request, runtime)

    def describe_abolish_api_task_with_options(
        self,
        request: main_models.DescribeAbolishApiTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAbolishApiTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAbolishApiTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAbolishApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abolish_api_task_with_options_async(
        self,
        request: main_models.DescribeAbolishApiTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAbolishApiTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAbolishApiTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAbolishApiTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abolish_api_task(
        self,
        request: main_models.DescribeAbolishApiTaskRequest,
    ) -> main_models.DescribeAbolishApiTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_abolish_api_task_with_options(request, runtime)

    async def describe_abolish_api_task_async(
        self,
        request: main_models.DescribeAbolishApiTaskRequest,
    ) -> main_models.DescribeAbolishApiTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_abolish_api_task_with_options_async(request, runtime)

    def describe_access_control_list_attribute_with_options(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlListAttribute',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_list_attribute_with_options_async(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlListAttribute',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_list_attribute(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_access_control_list_attribute_with_options(request, runtime)

    async def describe_access_control_list_attribute_async(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_control_list_attribute_with_options_async(request, runtime)

    def describe_access_control_lists_with_options(
        self,
        request: main_models.DescribeAccessControlListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlLists',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_lists_with_options_async(
        self,
        request: main_models.DescribeAccessControlListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlLists',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_lists(
        self,
        request: main_models.DescribeAccessControlListsRequest,
    ) -> main_models.DescribeAccessControlListsResponse:
        runtime = RuntimeOptions()
        return self.describe_access_control_lists_with_options(request, runtime)

    async def describe_access_control_lists_async(
        self,
        request: main_models.DescribeAccessControlListsRequest,
    ) -> main_models.DescribeAccessControlListsResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_control_lists_with_options_async(request, runtime)

    def describe_api_with_options(
        self,
        request: main_models.DescribeApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_with_options_async(
        self,
        request: main_models.DescribeApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api(
        self,
        request: main_models.DescribeApiRequest,
    ) -> main_models.DescribeApiResponse:
        runtime = RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    async def describe_api_async(
        self,
        request: main_models.DescribeApiRequest,
    ) -> main_models.DescribeApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_with_options_async(request, runtime)

    def describe_api_doc_with_options(
        self,
        request: main_models.DescribeApiDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiDoc',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_doc_with_options_async(
        self,
        request: main_models.DescribeApiDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiDoc',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_doc(
        self,
        request: main_models.DescribeApiDocRequest,
    ) -> main_models.DescribeApiDocResponse:
        runtime = RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    async def describe_api_doc_async(
        self,
        request: main_models.DescribeApiDocRequest,
    ) -> main_models.DescribeApiDocResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_doc_with_options_async(request, runtime)

    def describe_api_group_with_options(
        self,
        request: main_models.DescribeApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_with_options_async(
        self,
        request: main_models.DescribeApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group(
        self,
        request: main_models.DescribeApiGroupRequest,
    ) -> main_models.DescribeApiGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_api_group_with_options(request, runtime)

    async def describe_api_group_async(
        self,
        request: main_models.DescribeApiGroupRequest,
    ) -> main_models.DescribeApiGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_group_with_options_async(request, runtime)

    def describe_api_group_vpc_whitelist_with_options(
        self,
        request: main_models.DescribeApiGroupVpcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupVpcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroupVpcWhitelist',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupVpcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_vpc_whitelist_with_options_async(
        self,
        request: main_models.DescribeApiGroupVpcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupVpcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroupVpcWhitelist',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupVpcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group_vpc_whitelist(
        self,
        request: main_models.DescribeApiGroupVpcWhitelistRequest,
    ) -> main_models.DescribeApiGroupVpcWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_api_group_vpc_whitelist_with_options(request, runtime)

    async def describe_api_group_vpc_whitelist_async(
        self,
        request: main_models.DescribeApiGroupVpcWhitelistRequest,
    ) -> main_models.DescribeApiGroupVpcWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_group_vpc_whitelist_with_options_async(request, runtime)

    def describe_api_groups_with_options(
        self,
        request: main_models.DescribeApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_path):
            query['BasePath'] = request.base_path
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroups',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_groups_with_options_async(
        self,
        request: main_models.DescribeApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_path):
            query['BasePath'] = request.base_path
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiGroups',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_groups(
        self,
        request: main_models.DescribeApiGroupsRequest,
    ) -> main_models.DescribeApiGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    async def describe_api_groups_async(
        self,
        request: main_models.DescribeApiGroupsRequest,
    ) -> main_models.DescribeApiGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_groups_with_options_async(request, runtime)

    def describe_api_histories_with_options(
        self,
        request: main_models.DescribeApiHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiHistories',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_histories_with_options_async(
        self,
        request: main_models.DescribeApiHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiHistories',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_histories(
        self,
        request: main_models.DescribeApiHistoriesRequest,
    ) -> main_models.DescribeApiHistoriesResponse:
        runtime = RuntimeOptions()
        return self.describe_api_histories_with_options(request, runtime)

    async def describe_api_histories_async(
        self,
        request: main_models.DescribeApiHistoriesRequest,
    ) -> main_models.DescribeApiHistoriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_histories_with_options_async(request, runtime)

    def describe_api_history_with_options(
        self,
        request: main_models.DescribeApiHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiHistory',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_history_with_options_async(
        self,
        request: main_models.DescribeApiHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiHistory',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_history(
        self,
        request: main_models.DescribeApiHistoryRequest,
    ) -> main_models.DescribeApiHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_api_history_with_options(request, runtime)

    async def describe_api_history_async(
        self,
        request: main_models.DescribeApiHistoryRequest,
    ) -> main_models.DescribeApiHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_history_with_options_async(request, runtime)

    def describe_api_ip_controls_with_options(
        self,
        request: main_models.DescribeApiIpControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiIpControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiIpControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_ip_controls_with_options_async(
        self,
        request: main_models.DescribeApiIpControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiIpControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiIpControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiIpControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_ip_controls(
        self,
        request: main_models.DescribeApiIpControlsRequest,
    ) -> main_models.DescribeApiIpControlsResponse:
        runtime = RuntimeOptions()
        return self.describe_api_ip_controls_with_options(request, runtime)

    async def describe_api_ip_controls_async(
        self,
        request: main_models.DescribeApiIpControlsRequest,
    ) -> main_models.DescribeApiIpControlsResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_ip_controls_with_options_async(request, runtime)

    def describe_api_latency_data_with_options(
        self,
        request: main_models.DescribeApiLatencyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiLatencyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiLatencyData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiLatencyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_latency_data_with_options_async(
        self,
        request: main_models.DescribeApiLatencyDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiLatencyDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiLatencyData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiLatencyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_latency_data(
        self,
        request: main_models.DescribeApiLatencyDataRequest,
    ) -> main_models.DescribeApiLatencyDataResponse:
        runtime = RuntimeOptions()
        return self.describe_api_latency_data_with_options(request, runtime)

    async def describe_api_latency_data_async(
        self,
        request: main_models.DescribeApiLatencyDataRequest,
    ) -> main_models.DescribeApiLatencyDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_latency_data_with_options_async(request, runtime)

    def describe_api_market_attributes_with_options(
        self,
        request: main_models.DescribeApiMarketAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiMarketAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiMarketAttributes',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiMarketAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_market_attributes_with_options_async(
        self,
        request: main_models.DescribeApiMarketAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiMarketAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiMarketAttributes',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiMarketAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_market_attributes(
        self,
        request: main_models.DescribeApiMarketAttributesRequest,
    ) -> main_models.DescribeApiMarketAttributesResponse:
        runtime = RuntimeOptions()
        return self.describe_api_market_attributes_with_options(request, runtime)

    async def describe_api_market_attributes_async(
        self,
        request: main_models.DescribeApiMarketAttributesRequest,
    ) -> main_models.DescribeApiMarketAttributesResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_market_attributes_with_options_async(request, runtime)

    def describe_api_product_apis_with_options(
        self,
        request: main_models.DescribeApiProductApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiProductApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiProductApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiProductApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_product_apis_with_options_async(
        self,
        request: main_models.DescribeApiProductApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiProductApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiProductApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiProductApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_product_apis(
        self,
        request: main_models.DescribeApiProductApisRequest,
    ) -> main_models.DescribeApiProductApisResponse:
        runtime = RuntimeOptions()
        return self.describe_api_product_apis_with_options(request, runtime)

    async def describe_api_product_apis_async(
        self,
        request: main_models.DescribeApiProductApisRequest,
    ) -> main_models.DescribeApiProductApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_product_apis_with_options_async(request, runtime)

    def describe_api_products_by_app_with_options(
        self,
        request: main_models.DescribeApiProductsByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiProductsByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiProductsByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiProductsByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_products_by_app_with_options_async(
        self,
        request: main_models.DescribeApiProductsByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiProductsByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiProductsByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiProductsByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_products_by_app(
        self,
        request: main_models.DescribeApiProductsByAppRequest,
    ) -> main_models.DescribeApiProductsByAppResponse:
        runtime = RuntimeOptions()
        return self.describe_api_products_by_app_with_options(request, runtime)

    async def describe_api_products_by_app_async(
        self,
        request: main_models.DescribeApiProductsByAppRequest,
    ) -> main_models.DescribeApiProductsByAppResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_products_by_app_with_options_async(request, runtime)

    def describe_api_qps_data_with_options(
        self,
        request: main_models.DescribeApiQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiQpsData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_qps_data_with_options_async(
        self,
        request: main_models.DescribeApiQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiQpsData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_qps_data(
        self,
        request: main_models.DescribeApiQpsDataRequest,
    ) -> main_models.DescribeApiQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_api_qps_data_with_options(request, runtime)

    async def describe_api_qps_data_async(
        self,
        request: main_models.DescribeApiQpsDataRequest,
    ) -> main_models.DescribeApiQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_qps_data_with_options_async(request, runtime)

    def describe_api_signatures_with_options(
        self,
        request: main_models.DescribeApiSignaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiSignaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiSignatures',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_signatures_with_options_async(
        self,
        request: main_models.DescribeApiSignaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiSignaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiSignatures',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_signatures(
        self,
        request: main_models.DescribeApiSignaturesRequest,
    ) -> main_models.DescribeApiSignaturesResponse:
        runtime = RuntimeOptions()
        return self.describe_api_signatures_with_options(request, runtime)

    async def describe_api_signatures_async(
        self,
        request: main_models.DescribeApiSignaturesRequest,
    ) -> main_models.DescribeApiSignaturesResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_signatures_with_options_async(request, runtime)

    def describe_api_traffic_controls_with_options(
        self,
        request: main_models.DescribeApiTrafficControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiTrafficControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiTrafficControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_traffic_controls_with_options_async(
        self,
        request: main_models.DescribeApiTrafficControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiTrafficControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiTrafficControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiTrafficControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_traffic_controls(
        self,
        request: main_models.DescribeApiTrafficControlsRequest,
    ) -> main_models.DescribeApiTrafficControlsResponse:
        runtime = RuntimeOptions()
        return self.describe_api_traffic_controls_with_options(request, runtime)

    async def describe_api_traffic_controls_async(
        self,
        request: main_models.DescribeApiTrafficControlsRequest,
    ) -> main_models.DescribeApiTrafficControlsResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_traffic_controls_with_options_async(request, runtime)

    def describe_api_traffic_data_with_options(
        self,
        request: main_models.DescribeApiTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiTrafficData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_traffic_data_with_options_async(
        self,
        request: main_models.DescribeApiTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiTrafficData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_traffic_data(
        self,
        request: main_models.DescribeApiTrafficDataRequest,
    ) -> main_models.DescribeApiTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_api_traffic_data_with_options(request, runtime)

    async def describe_api_traffic_data_async(
        self,
        request: main_models.DescribeApiTrafficDataRequest,
    ) -> main_models.DescribeApiTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_traffic_data_with_options_async(request, runtime)

    def describe_apis_with_options(
        self,
        request: main_models.DescribeApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_method):
            query['ApiMethod'] = request.api_method
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_path):
            query['ApiPath'] = request.api_path
        if not DaraCore.is_null(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.un_deployed):
            query['UnDeployed'] = request.un_deployed
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_with_options_async(
        self,
        request: main_models.DescribeApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_method):
            query['ApiMethod'] = request.api_method
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_path):
            query['ApiPath'] = request.api_path
        if not DaraCore.is_null(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.un_deployed):
            query['UnDeployed'] = request.un_deployed
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis(
        self,
        request: main_models.DescribeApisRequest,
    ) -> main_models.DescribeApisResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    async def describe_apis_async(
        self,
        request: main_models.DescribeApisRequest,
    ) -> main_models.DescribeApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_with_options_async(request, runtime)

    def describe_apis_by_app_with_options(
        self,
        request: main_models.DescribeApisByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_app_with_options_async(
        self,
        request: main_models.DescribeApisByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_app(
        self,
        request: main_models.DescribeApisByAppRequest,
    ) -> main_models.DescribeApisByAppResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    async def describe_apis_by_app_async(
        self,
        request: main_models.DescribeApisByAppRequest,
    ) -> main_models.DescribeApisByAppResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_by_app_with_options_async(request, runtime)

    def describe_apis_by_backend_with_options(
        self,
        request: main_models.DescribeApisByBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_backend_with_options_async(
        self,
        request: main_models.DescribeApisByBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_backend(
        self,
        request: main_models.DescribeApisByBackendRequest,
    ) -> main_models.DescribeApisByBackendResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_by_backend_with_options(request, runtime)

    async def describe_apis_by_backend_async(
        self,
        request: main_models.DescribeApisByBackendRequest,
    ) -> main_models.DescribeApisByBackendResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_by_backend_with_options_async(request, runtime)

    def describe_apis_by_ip_control_with_options(
        self,
        request: main_models.DescribeApisByIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_ip_control_with_options_async(
        self,
        request: main_models.DescribeApisByIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_ip_control(
        self,
        request: main_models.DescribeApisByIpControlRequest,
    ) -> main_models.DescribeApisByIpControlResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_by_ip_control_with_options(request, runtime)

    async def describe_apis_by_ip_control_async(
        self,
        request: main_models.DescribeApisByIpControlRequest,
    ) -> main_models.DescribeApisByIpControlResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_by_ip_control_with_options_async(request, runtime)

    def describe_apis_by_signature_with_options(
        self,
        request: main_models.DescribeApisBySignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisBySignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisBySignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisBySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_signature_with_options_async(
        self,
        request: main_models.DescribeApisBySignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisBySignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisBySignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisBySignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_signature(
        self,
        request: main_models.DescribeApisBySignatureRequest,
    ) -> main_models.DescribeApisBySignatureResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_by_signature_with_options(request, runtime)

    async def describe_apis_by_signature_async(
        self,
        request: main_models.DescribeApisBySignatureRequest,
    ) -> main_models.DescribeApisBySignatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_by_signature_with_options_async(request, runtime)

    def describe_apis_by_traffic_control_with_options(
        self,
        request: main_models.DescribeApisByTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_traffic_control_with_options_async(
        self,
        request: main_models.DescribeApisByTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_traffic_control(
        self,
        request: main_models.DescribeApisByTrafficControlRequest,
    ) -> main_models.DescribeApisByTrafficControlResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_by_traffic_control_with_options(request, runtime)

    async def describe_apis_by_traffic_control_async(
        self,
        request: main_models.DescribeApisByTrafficControlRequest,
    ) -> main_models.DescribeApisByTrafficControlResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_by_traffic_control_with_options_async(request, runtime)

    def describe_apis_by_vpc_access_with_options(
        self,
        request: main_models.DescribeApisByVpcAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByVpcAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByVpcAccess',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_vpc_access_with_options_async(
        self,
        request: main_models.DescribeApisByVpcAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisByVpcAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisByVpcAccess',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisByVpcAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_vpc_access(
        self,
        request: main_models.DescribeApisByVpcAccessRequest,
    ) -> main_models.DescribeApisByVpcAccessResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_by_vpc_access_with_options(request, runtime)

    async def describe_apis_by_vpc_access_async(
        self,
        request: main_models.DescribeApisByVpcAccessRequest,
    ) -> main_models.DescribeApisByVpcAccessResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_by_vpc_access_with_options_async(request, runtime)

    def describe_apis_with_stage_name_integrated_by_app_with_options(
        self,
        request: main_models.DescribeApisWithStageNameIntegratedByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisWithStageNameIntegratedByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisWithStageNameIntegratedByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisWithStageNameIntegratedByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_with_stage_name_integrated_by_app_with_options_async(
        self,
        request: main_models.DescribeApisWithStageNameIntegratedByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisWithStageNameIntegratedByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisWithStageNameIntegratedByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisWithStageNameIntegratedByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_with_stage_name_integrated_by_app(
        self,
        request: main_models.DescribeApisWithStageNameIntegratedByAppRequest,
    ) -> main_models.DescribeApisWithStageNameIntegratedByAppResponse:
        runtime = RuntimeOptions()
        return self.describe_apis_with_stage_name_integrated_by_app_with_options(request, runtime)

    async def describe_apis_with_stage_name_integrated_by_app_async(
        self,
        request: main_models.DescribeApisWithStageNameIntegratedByAppRequest,
    ) -> main_models.DescribeApisWithStageNameIntegratedByAppResponse:
        runtime = RuntimeOptions()
        return await self.describe_apis_with_stage_name_integrated_by_app_with_options_async(request, runtime)

    def describe_app_with_options(
        self,
        request: main_models.DescribeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_with_options_async(
        self,
        request: main_models.DescribeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app(
        self,
        request: main_models.DescribeAppRequest,
    ) -> main_models.DescribeAppResponse:
        runtime = RuntimeOptions()
        return self.describe_app_with_options(request, runtime)

    async def describe_app_async(
        self,
        request: main_models.DescribeAppRequest,
    ) -> main_models.DescribeAppResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_with_options_async(request, runtime)

    def describe_app_attributes_with_options(
        self,
        request: main_models.DescribeAppAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppAttributes',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_attributes_with_options_async(
        self,
        request: main_models.DescribeAppAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppAttributes',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_attributes(
        self,
        request: main_models.DescribeAppAttributesRequest,
    ) -> main_models.DescribeAppAttributesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_attributes_with_options(request, runtime)

    async def describe_app_attributes_async(
        self,
        request: main_models.DescribeAppAttributesRequest,
    ) -> main_models.DescribeAppAttributesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_attributes_with_options_async(request, runtime)

    def describe_app_securities_with_options(
        self,
        request: main_models.DescribeAppSecuritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppSecuritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppSecurities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppSecuritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_securities_with_options_async(
        self,
        request: main_models.DescribeAppSecuritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppSecuritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppSecurities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppSecuritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_securities(
        self,
        request: main_models.DescribeAppSecuritiesRequest,
    ) -> main_models.DescribeAppSecuritiesResponse:
        runtime = RuntimeOptions()
        return self.describe_app_securities_with_options(request, runtime)

    async def describe_app_securities_async(
        self,
        request: main_models.DescribeAppSecuritiesRequest,
    ) -> main_models.DescribeAppSecuritiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_securities_with_options_async(request, runtime)

    def describe_app_security_with_options(
        self,
        request: main_models.DescribeAppSecurityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppSecurityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppSecurity',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppSecurityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_security_with_options_async(
        self,
        request: main_models.DescribeAppSecurityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppSecurityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppSecurity',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppSecurityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_security(
        self,
        request: main_models.DescribeAppSecurityRequest,
    ) -> main_models.DescribeAppSecurityResponse:
        runtime = RuntimeOptions()
        return self.describe_app_security_with_options(request, runtime)

    async def describe_app_security_async(
        self,
        request: main_models.DescribeAppSecurityRequest,
    ) -> main_models.DescribeAppSecurityResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_security_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: main_models.DescribeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_owner):
            query['AppOwner'] = request.app_owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: main_models.DescribeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_owner):
            query['AppOwner'] = request.app_owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: main_models.DescribeAppsRequest,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: main_models.DescribeAppsRequest,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_apps_by_api_product_with_options(
        self,
        request: main_models.DescribeAppsByApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsByApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppsByApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsByApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_by_api_product_with_options_async(
        self,
        request: main_models.DescribeAppsByApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsByApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppsByApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsByApiProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps_by_api_product(
        self,
        request: main_models.DescribeAppsByApiProductRequest,
    ) -> main_models.DescribeAppsByApiProductResponse:
        runtime = RuntimeOptions()
        return self.describe_apps_by_api_product_with_options(request, runtime)

    async def describe_apps_by_api_product_async(
        self,
        request: main_models.DescribeAppsByApiProductRequest,
    ) -> main_models.DescribeAppsByApiProductResponse:
        runtime = RuntimeOptions()
        return await self.describe_apps_by_api_product_with_options_async(request, runtime)

    def describe_authorized_apis_with_options(
        self,
        request: main_models.DescribeAuthorizedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthorizedApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthorizedApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthorizedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_authorized_apis_with_options_async(
        self,
        request: main_models.DescribeAuthorizedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthorizedApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthorizedApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthorizedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_authorized_apis(
        self,
        request: main_models.DescribeAuthorizedApisRequest,
    ) -> main_models.DescribeAuthorizedApisResponse:
        runtime = RuntimeOptions()
        return self.describe_authorized_apis_with_options(request, runtime)

    async def describe_authorized_apis_async(
        self,
        request: main_models.DescribeAuthorizedApisRequest,
    ) -> main_models.DescribeAuthorizedApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_authorized_apis_with_options_async(request, runtime)

    def describe_authorized_apps_with_options(
        self,
        request: main_models.DescribeAuthorizedAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthorizedAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthorizedApps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthorizedAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_authorized_apps_with_options_async(
        self,
        request: main_models.DescribeAuthorizedAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuthorizedAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuthorizedApps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuthorizedAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_authorized_apps(
        self,
        request: main_models.DescribeAuthorizedAppsRequest,
    ) -> main_models.DescribeAuthorizedAppsResponse:
        runtime = RuntimeOptions()
        return self.describe_authorized_apps_with_options(request, runtime)

    async def describe_authorized_apps_async(
        self,
        request: main_models.DescribeAuthorizedAppsRequest,
    ) -> main_models.DescribeAuthorizedAppsResponse:
        runtime = RuntimeOptions()
        return await self.describe_authorized_apps_with_options_async(request, runtime)

    def describe_backend_info_with_options(
        self,
        request: main_models.DescribeBackendInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackendInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackendInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackendInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backend_info_with_options_async(
        self,
        request: main_models.DescribeBackendInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackendInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackendInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackendInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backend_info(
        self,
        request: main_models.DescribeBackendInfoRequest,
    ) -> main_models.DescribeBackendInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_backend_info_with_options(request, runtime)

    async def describe_backend_info_async(
        self,
        request: main_models.DescribeBackendInfoRequest,
    ) -> main_models.DescribeBackendInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_backend_info_with_options_async(request, runtime)

    def describe_backend_list_with_options(
        self,
        request: main_models.DescribeBackendListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackendListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackendList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackendListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backend_list_with_options_async(
        self,
        request: main_models.DescribeBackendListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackendListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackendList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackendListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backend_list(
        self,
        request: main_models.DescribeBackendListRequest,
    ) -> main_models.DescribeBackendListResponse:
        runtime = RuntimeOptions()
        return self.describe_backend_list_with_options(request, runtime)

    async def describe_backend_list_async(
        self,
        request: main_models.DescribeBackendListRequest,
    ) -> main_models.DescribeBackendListResponse:
        runtime = RuntimeOptions()
        return await self.describe_backend_list_with_options_async(request, runtime)

    def describe_dataset_info_with_options(
        self,
        request: main_models.DescribeDatasetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dataset_info_with_options_async(
        self,
        request: main_models.DescribeDatasetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dataset_info(
        self,
        request: main_models.DescribeDatasetInfoRequest,
    ) -> main_models.DescribeDatasetInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dataset_info_with_options(request, runtime)

    async def describe_dataset_info_async(
        self,
        request: main_models.DescribeDatasetInfoRequest,
    ) -> main_models.DescribeDatasetInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dataset_info_with_options_async(request, runtime)

    def describe_dataset_item_info_with_options(
        self,
        request: main_models.DescribeDatasetItemInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetItemInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetItemInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetItemInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dataset_item_info_with_options_async(
        self,
        request: main_models.DescribeDatasetItemInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetItemInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetItemInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetItemInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dataset_item_info(
        self,
        request: main_models.DescribeDatasetItemInfoRequest,
    ) -> main_models.DescribeDatasetItemInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dataset_item_info_with_options(request, runtime)

    async def describe_dataset_item_info_async(
        self,
        request: main_models.DescribeDatasetItemInfoRequest,
    ) -> main_models.DescribeDatasetItemInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dataset_item_info_with_options_async(request, runtime)

    def describe_dataset_item_list_with_options(
        self,
        request: main_models.DescribeDatasetItemListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetItemListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_ids):
            query['DatasetItemIds'] = request.dataset_item_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetItemList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dataset_item_list_with_options_async(
        self,
        request: main_models.DescribeDatasetItemListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetItemListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_ids):
            query['DatasetItemIds'] = request.dataset_item_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetItemList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dataset_item_list(
        self,
        request: main_models.DescribeDatasetItemListRequest,
    ) -> main_models.DescribeDatasetItemListResponse:
        runtime = RuntimeOptions()
        return self.describe_dataset_item_list_with_options(request, runtime)

    async def describe_dataset_item_list_async(
        self,
        request: main_models.DescribeDatasetItemListRequest,
    ) -> main_models.DescribeDatasetItemListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dataset_item_list_with_options_async(request, runtime)

    def describe_dataset_list_with_options(
        self,
        request: main_models.DescribeDatasetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_ids):
            query['DatasetIds'] = request.dataset_ids
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dataset_list_with_options_async(
        self,
        request: main_models.DescribeDatasetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDatasetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_ids):
            query['DatasetIds'] = request.dataset_ids
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDatasetList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDatasetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dataset_list(
        self,
        request: main_models.DescribeDatasetListRequest,
    ) -> main_models.DescribeDatasetListResponse:
        runtime = RuntimeOptions()
        return self.describe_dataset_list_with_options(request, runtime)

    async def describe_dataset_list_async(
        self,
        request: main_models.DescribeDatasetListRequest,
    ) -> main_models.DescribeDatasetListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dataset_list_with_options_async(request, runtime)

    def describe_deploy_api_task_with_options(
        self,
        request: main_models.DescribeDeployApiTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeployApiTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeployApiTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeployApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deploy_api_task_with_options_async(
        self,
        request: main_models.DescribeDeployApiTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeployApiTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeployApiTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeployApiTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deploy_api_task(
        self,
        request: main_models.DescribeDeployApiTaskRequest,
    ) -> main_models.DescribeDeployApiTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_deploy_api_task_with_options(request, runtime)

    async def describe_deploy_api_task_async(
        self,
        request: main_models.DescribeDeployApiTaskRequest,
    ) -> main_models.DescribeDeployApiTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_deploy_api_task_with_options_async(request, runtime)

    def describe_deployed_api_with_options(
        self,
        request: main_models.DescribeDeployedApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeployedApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeployedApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeployedApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_api_with_options_async(
        self,
        request: main_models.DescribeDeployedApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeployedApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeployedApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeployedApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_api(
        self,
        request: main_models.DescribeDeployedApiRequest,
    ) -> main_models.DescribeDeployedApiResponse:
        runtime = RuntimeOptions()
        return self.describe_deployed_api_with_options(request, runtime)

    async def describe_deployed_api_async(
        self,
        request: main_models.DescribeDeployedApiRequest,
    ) -> main_models.DescribeDeployedApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_deployed_api_with_options_async(request, runtime)

    def describe_deployed_apis_with_options(
        self,
        request: main_models.DescribeDeployedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeployedApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_method):
            query['ApiMethod'] = request.api_method
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_path):
            query['ApiPath'] = request.api_path
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeployedApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeployedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_apis_with_options_async(
        self,
        request: main_models.DescribeDeployedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeployedApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_method):
            query['ApiMethod'] = request.api_method
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_path):
            query['ApiPath'] = request.api_path
        if not DaraCore.is_null(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeployedApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeployedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_apis(
        self,
        request: main_models.DescribeDeployedApisRequest,
    ) -> main_models.DescribeDeployedApisResponse:
        runtime = RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    async def describe_deployed_apis_async(
        self,
        request: main_models.DescribeDeployedApisRequest,
    ) -> main_models.DescribeDeployedApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_deployed_apis_with_options_async(request, runtime)

    def describe_domain_with_options(
        self,
        request: main_models.DescribeDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_with_options_async(
        self,
        request: main_models.DescribeDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain(
        self,
        request: main_models.DescribeDomainRequest,
    ) -> main_models.DescribeDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    async def describe_domain_async(
        self,
        request: main_models.DescribeDomainRequest,
    ) -> main_models.DescribeDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_with_options_async(request, runtime)

    def describe_group_latency_with_options(
        self,
        request: main_models.DescribeGroupLatencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupLatencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupLatency',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupLatencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_latency_with_options_async(
        self,
        request: main_models.DescribeGroupLatencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupLatencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupLatency',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupLatencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_latency(
        self,
        request: main_models.DescribeGroupLatencyRequest,
    ) -> main_models.DescribeGroupLatencyResponse:
        runtime = RuntimeOptions()
        return self.describe_group_latency_with_options(request, runtime)

    async def describe_group_latency_async(
        self,
        request: main_models.DescribeGroupLatencyRequest,
    ) -> main_models.DescribeGroupLatencyResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_latency_with_options_async(request, runtime)

    def describe_group_qps_with_options(
        self,
        request: main_models.DescribeGroupQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupQps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_qps_with_options_async(
        self,
        request: main_models.DescribeGroupQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupQps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_qps(
        self,
        request: main_models.DescribeGroupQpsRequest,
    ) -> main_models.DescribeGroupQpsResponse:
        runtime = RuntimeOptions()
        return self.describe_group_qps_with_options(request, runtime)

    async def describe_group_qps_async(
        self,
        request: main_models.DescribeGroupQpsRequest,
    ) -> main_models.DescribeGroupQpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_qps_with_options_async(request, runtime)

    def describe_group_traffic_with_options(
        self,
        request: main_models.DescribeGroupTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupTraffic',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_traffic_with_options_async(
        self,
        request: main_models.DescribeGroupTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupTraffic',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_traffic(
        self,
        request: main_models.DescribeGroupTrafficRequest,
    ) -> main_models.DescribeGroupTrafficResponse:
        runtime = RuntimeOptions()
        return self.describe_group_traffic_with_options(request, runtime)

    async def describe_group_traffic_async(
        self,
        request: main_models.DescribeGroupTrafficRequest,
    ) -> main_models.DescribeGroupTrafficResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_traffic_with_options_async(request, runtime)

    def describe_history_apis_with_options(
        self,
        request: main_models.DescribeHistoryApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_apis_with_options_async(
        self,
        request: main_models.DescribeHistoryApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_apis(
        self,
        request: main_models.DescribeHistoryApisRequest,
    ) -> main_models.DescribeHistoryApisResponse:
        runtime = RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    async def describe_history_apis_async(
        self,
        request: main_models.DescribeHistoryApisRequest,
    ) -> main_models.DescribeHistoryApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_history_apis_with_options_async(request, runtime)

    def describe_import_oastask_with_options(
        self,
        request: main_models.DescribeImportOASTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImportOASTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImportOASTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImportOASTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_import_oastask_with_options_async(
        self,
        request: main_models.DescribeImportOASTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImportOASTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImportOASTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImportOASTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_import_oastask(
        self,
        request: main_models.DescribeImportOASTaskRequest,
    ) -> main_models.DescribeImportOASTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_import_oastask_with_options(request, runtime)

    async def describe_import_oastask_async(
        self,
        request: main_models.DescribeImportOASTaskRequest,
    ) -> main_models.DescribeImportOASTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_import_oastask_with_options_async(request, runtime)

    def describe_instance_cluster_info_with_options(
        self,
        request: main_models.DescribeInstanceClusterInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceClusterInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_cluster_name):
            query['InstanceClusterName'] = request.instance_cluster_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceClusterInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceClusterInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_cluster_info_with_options_async(
        self,
        request: main_models.DescribeInstanceClusterInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceClusterInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_cluster_name):
            query['InstanceClusterName'] = request.instance_cluster_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceClusterInfo',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceClusterInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_cluster_info(
        self,
        request: main_models.DescribeInstanceClusterInfoRequest,
    ) -> main_models.DescribeInstanceClusterInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_cluster_info_with_options(request, runtime)

    async def describe_instance_cluster_info_async(
        self,
        request: main_models.DescribeInstanceClusterInfoRequest,
    ) -> main_models.DescribeInstanceClusterInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_cluster_info_with_options_async(request, runtime)

    def describe_instance_cluster_list_with_options(
        self,
        request: main_models.DescribeInstanceClusterListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceClusterListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_cluster_id):
            query['InstanceClusterId'] = request.instance_cluster_id
        if not DaraCore.is_null(request.instance_cluster_name):
            query['InstanceClusterName'] = request.instance_cluster_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceClusterList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceClusterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_cluster_list_with_options_async(
        self,
        request: main_models.DescribeInstanceClusterListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceClusterListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_cluster_id):
            query['InstanceClusterId'] = request.instance_cluster_id
        if not DaraCore.is_null(request.instance_cluster_name):
            query['InstanceClusterName'] = request.instance_cluster_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceClusterList',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceClusterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_cluster_list(
        self,
        request: main_models.DescribeInstanceClusterListRequest,
    ) -> main_models.DescribeInstanceClusterListResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_cluster_list_with_options(request, runtime)

    async def describe_instance_cluster_list_async(
        self,
        request: main_models.DescribeInstanceClusterListRequest,
    ) -> main_models.DescribeInstanceClusterListResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_cluster_list_with_options_async(request, runtime)

    def describe_instance_drop_connections_with_options(
        self,
        request: main_models.DescribeInstanceDropConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDropConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDropConnections',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDropConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_drop_connections_with_options_async(
        self,
        request: main_models.DescribeInstanceDropConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDropConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDropConnections',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDropConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_drop_connections(
        self,
        request: main_models.DescribeInstanceDropConnectionsRequest,
    ) -> main_models.DescribeInstanceDropConnectionsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_drop_connections_with_options(request, runtime)

    async def describe_instance_drop_connections_async(
        self,
        request: main_models.DescribeInstanceDropConnectionsRequest,
    ) -> main_models.DescribeInstanceDropConnectionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_drop_connections_with_options_async(request, runtime)

    def describe_instance_drop_packet_with_options(
        self,
        request: main_models.DescribeInstanceDropPacketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDropPacketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDropPacket',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDropPacketResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_drop_packet_with_options_async(
        self,
        request: main_models.DescribeInstanceDropPacketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDropPacketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDropPacket',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDropPacketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_drop_packet(
        self,
        request: main_models.DescribeInstanceDropPacketRequest,
    ) -> main_models.DescribeInstanceDropPacketResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_drop_packet_with_options(request, runtime)

    async def describe_instance_drop_packet_async(
        self,
        request: main_models.DescribeInstanceDropPacketRequest,
    ) -> main_models.DescribeInstanceDropPacketResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_drop_packet_with_options_async(request, runtime)

    def describe_instance_http_code_with_options(
        self,
        request: main_models.DescribeInstanceHttpCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceHttpCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceHttpCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceHttpCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_http_code_with_options_async(
        self,
        request: main_models.DescribeInstanceHttpCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceHttpCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceHttpCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceHttpCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_http_code(
        self,
        request: main_models.DescribeInstanceHttpCodeRequest,
    ) -> main_models.DescribeInstanceHttpCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_http_code_with_options(request, runtime)

    async def describe_instance_http_code_async(
        self,
        request: main_models.DescribeInstanceHttpCodeRequest,
    ) -> main_models.DescribeInstanceHttpCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_http_code_with_options_async(request, runtime)

    def describe_instance_latency_with_options(
        self,
        request: main_models.DescribeInstanceLatencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceLatencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceLatency',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceLatencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_latency_with_options_async(
        self,
        request: main_models.DescribeInstanceLatencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceLatencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceLatency',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceLatencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_latency(
        self,
        request: main_models.DescribeInstanceLatencyRequest,
    ) -> main_models.DescribeInstanceLatencyResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_latency_with_options(request, runtime)

    async def describe_instance_latency_async(
        self,
        request: main_models.DescribeInstanceLatencyRequest,
    ) -> main_models.DescribeInstanceLatencyResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_latency_with_options_async(request, runtime)

    def describe_instance_new_connections_with_options(
        self,
        request: main_models.DescribeInstanceNewConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceNewConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceNewConnections',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceNewConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_new_connections_with_options_async(
        self,
        request: main_models.DescribeInstanceNewConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceNewConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceNewConnections',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceNewConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_new_connections(
        self,
        request: main_models.DescribeInstanceNewConnectionsRequest,
    ) -> main_models.DescribeInstanceNewConnectionsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_new_connections_with_options(request, runtime)

    async def describe_instance_new_connections_async(
        self,
        request: main_models.DescribeInstanceNewConnectionsRequest,
    ) -> main_models.DescribeInstanceNewConnectionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_new_connections_with_options_async(request, runtime)

    def describe_instance_packets_with_options(
        self,
        request: main_models.DescribeInstancePacketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancePacketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstancePackets',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancePacketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_packets_with_options_async(
        self,
        request: main_models.DescribeInstancePacketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancePacketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstancePackets',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancePacketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_packets(
        self,
        request: main_models.DescribeInstancePacketsRequest,
    ) -> main_models.DescribeInstancePacketsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_packets_with_options(request, runtime)

    async def describe_instance_packets_async(
        self,
        request: main_models.DescribeInstancePacketsRequest,
    ) -> main_models.DescribeInstancePacketsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_packets_with_options_async(request, runtime)

    def describe_instance_qps_with_options(
        self,
        request: main_models.DescribeInstanceQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceQps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_qps_with_options_async(
        self,
        request: main_models.DescribeInstanceQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceQps',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_qps(
        self,
        request: main_models.DescribeInstanceQpsRequest,
    ) -> main_models.DescribeInstanceQpsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_qps_with_options(request, runtime)

    async def describe_instance_qps_async(
        self,
        request: main_models.DescribeInstanceQpsRequest,
    ) -> main_models.DescribeInstanceQpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_qps_with_options_async(request, runtime)

    def describe_instance_slb_connect_with_options(
        self,
        request: main_models.DescribeInstanceSlbConnectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSlbConnectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSlbConnect',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSlbConnectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_slb_connect_with_options_async(
        self,
        request: main_models.DescribeInstanceSlbConnectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSlbConnectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSlbConnect',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSlbConnectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_slb_connect(
        self,
        request: main_models.DescribeInstanceSlbConnectRequest,
    ) -> main_models.DescribeInstanceSlbConnectResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_slb_connect_with_options(request, runtime)

    async def describe_instance_slb_connect_async(
        self,
        request: main_models.DescribeInstanceSlbConnectRequest,
    ) -> main_models.DescribeInstanceSlbConnectResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_slb_connect_with_options_async(request, runtime)

    def describe_instance_traffic_with_options(
        self,
        request: main_models.DescribeInstanceTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceTraffic',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_traffic_with_options_async(
        self,
        request: main_models.DescribeInstanceTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceTraffic',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_traffic(
        self,
        request: main_models.DescribeInstanceTrafficRequest,
    ) -> main_models.DescribeInstanceTrafficResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_traffic_with_options(request, runtime)

    async def describe_instance_traffic_async(
        self,
        request: main_models.DescribeInstanceTrafficRequest,
    ) -> main_models.DescribeInstanceTrafficResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_traffic_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_tag_authorization):
            query['EnableTagAuthorization'] = request.enable_tag_authorization
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_tag_authorization):
            query['EnableTagAuthorization'] = request.enable_tag_authorization
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_ip_control_policy_items_with_options(
        self,
        request: main_models.DescribeIpControlPolicyItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpControlPolicyItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpControlPolicyItems',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpControlPolicyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_control_policy_items_with_options_async(
        self,
        request: main_models.DescribeIpControlPolicyItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpControlPolicyItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpControlPolicyItems',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpControlPolicyItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_control_policy_items(
        self,
        request: main_models.DescribeIpControlPolicyItemsRequest,
    ) -> main_models.DescribeIpControlPolicyItemsResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_control_policy_items_with_options(request, runtime)

    async def describe_ip_control_policy_items_async(
        self,
        request: main_models.DescribeIpControlPolicyItemsRequest,
    ) -> main_models.DescribeIpControlPolicyItemsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_control_policy_items_with_options_async(request, runtime)

    def describe_ip_controls_with_options(
        self,
        request: main_models.DescribeIpControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not DaraCore.is_null(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_controls_with_options_async(
        self,
        request: main_models.DescribeIpControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not DaraCore.is_null(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_controls(
        self,
        request: main_models.DescribeIpControlsRequest,
    ) -> main_models.DescribeIpControlsResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_controls_with_options(request, runtime)

    async def describe_ip_controls_async(
        self,
        request: main_models.DescribeIpControlsRequest,
    ) -> main_models.DescribeIpControlsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_controls_with_options_async(request, runtime)

    def describe_log_config_with_options(
        self,
        request: main_models.DescribeLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_config_with_options_async(
        self,
        request: main_models.DescribeLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_config(
        self,
        request: main_models.DescribeLogConfigRequest,
    ) -> main_models.DescribeLogConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_log_config_with_options(request, runtime)

    async def describe_log_config_async(
        self,
        request: main_models.DescribeLogConfigRequest,
    ) -> main_models.DescribeLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_config_with_options_async(request, runtime)

    def describe_market_remains_quota_with_options(
        self,
        request: main_models.DescribeMarketRemainsQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMarketRemainsQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMarketRemainsQuota',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMarketRemainsQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_market_remains_quota_with_options_async(
        self,
        request: main_models.DescribeMarketRemainsQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMarketRemainsQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMarketRemainsQuota',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMarketRemainsQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_market_remains_quota(
        self,
        request: main_models.DescribeMarketRemainsQuotaRequest,
    ) -> main_models.DescribeMarketRemainsQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_market_remains_quota_with_options(request, runtime)

    async def describe_market_remains_quota_async(
        self,
        request: main_models.DescribeMarketRemainsQuotaRequest,
    ) -> main_models.DescribeMarketRemainsQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_market_remains_quota_with_options_async(request, runtime)

    def describe_models_with_options(
        self,
        request: main_models.DescribeModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModels',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_models_with_options_async(
        self,
        request: main_models.DescribeModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeModels',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_models(
        self,
        request: main_models.DescribeModelsRequest,
    ) -> main_models.DescribeModelsResponse:
        runtime = RuntimeOptions()
        return self.describe_models_with_options(request, runtime)

    async def describe_models_async(
        self,
        request: main_models.DescribeModelsRequest,
    ) -> main_models.DescribeModelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_models_with_options_async(request, runtime)

    def describe_plugin_apis_with_options(
        self,
        request: main_models.DescribePluginApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugin_apis_with_options_async(
        self,
        request: main_models.DescribePluginApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugin_apis(
        self,
        request: main_models.DescribePluginApisRequest,
    ) -> main_models.DescribePluginApisResponse:
        runtime = RuntimeOptions()
        return self.describe_plugin_apis_with_options(request, runtime)

    async def describe_plugin_apis_async(
        self,
        request: main_models.DescribePluginApisRequest,
    ) -> main_models.DescribePluginApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugin_apis_with_options_async(request, runtime)

    def describe_plugin_groups_with_options(
        self,
        request: main_models.DescribePluginGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginGroups',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugin_groups_with_options_async(
        self,
        request: main_models.DescribePluginGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginGroups',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugin_groups(
        self,
        request: main_models.DescribePluginGroupsRequest,
    ) -> main_models.DescribePluginGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_plugin_groups_with_options(request, runtime)

    async def describe_plugin_groups_async(
        self,
        request: main_models.DescribePluginGroupsRequest,
    ) -> main_models.DescribePluginGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugin_groups_with_options_async(request, runtime)

    def describe_plugin_schemas_with_options(
        self,
        request: main_models.DescribePluginSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginSchemas',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugin_schemas_with_options_async(
        self,
        request: main_models.DescribePluginSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginSchemas',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugin_schemas(
        self,
        request: main_models.DescribePluginSchemasRequest,
    ) -> main_models.DescribePluginSchemasResponse:
        runtime = RuntimeOptions()
        return self.describe_plugin_schemas_with_options(request, runtime)

    async def describe_plugin_schemas_async(
        self,
        request: main_models.DescribePluginSchemasRequest,
    ) -> main_models.DescribePluginSchemasResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugin_schemas_with_options_async(request, runtime)

    def describe_plugin_templates_with_options(
        self,
        request: main_models.DescribePluginTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginTemplates',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugin_templates_with_options_async(
        self,
        request: main_models.DescribePluginTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginTemplates',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugin_templates(
        self,
        request: main_models.DescribePluginTemplatesRequest,
    ) -> main_models.DescribePluginTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_plugin_templates_with_options(request, runtime)

    async def describe_plugin_templates_async(
        self,
        request: main_models.DescribePluginTemplatesRequest,
    ) -> main_models.DescribePluginTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugin_templates_with_options_async(request, runtime)

    def describe_plugins_with_options(
        self,
        request: main_models.DescribePluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlugins',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugins_with_options_async(
        self,
        request: main_models.DescribePluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlugins',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugins(
        self,
        request: main_models.DescribePluginsRequest,
    ) -> main_models.DescribePluginsResponse:
        runtime = RuntimeOptions()
        return self.describe_plugins_with_options(request, runtime)

    async def describe_plugins_async(
        self,
        request: main_models.DescribePluginsRequest,
    ) -> main_models.DescribePluginsResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugins_with_options_async(request, runtime)

    def describe_plugins_by_api_with_options(
        self,
        request: main_models.DescribePluginsByApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginsByApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginsByApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugins_by_api_with_options_async(
        self,
        request: main_models.DescribePluginsByApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginsByApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginsByApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginsByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugins_by_api(
        self,
        request: main_models.DescribePluginsByApiRequest,
    ) -> main_models.DescribePluginsByApiResponse:
        runtime = RuntimeOptions()
        return self.describe_plugins_by_api_with_options(request, runtime)

    async def describe_plugins_by_api_async(
        self,
        request: main_models.DescribePluginsByApiRequest,
    ) -> main_models.DescribePluginsByApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugins_by_api_with_options_async(request, runtime)

    def describe_plugins_by_group_with_options(
        self,
        request: main_models.DescribePluginsByGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginsByGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginsByGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginsByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugins_by_group_with_options_async(
        self,
        request: main_models.DescribePluginsByGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePluginsByGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePluginsByGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePluginsByGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugins_by_group(
        self,
        request: main_models.DescribePluginsByGroupRequest,
    ) -> main_models.DescribePluginsByGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_plugins_by_group_with_options(request, runtime)

    async def describe_plugins_by_group_async(
        self,
        request: main_models.DescribePluginsByGroupRequest,
    ) -> main_models.DescribePluginsByGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_plugins_by_group_with_options_async(request, runtime)

    def describe_purchased_api_group_with_options(
        self,
        request: main_models.DescribePurchasedApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_group_with_options_async(
        self,
        request: main_models.DescribePurchasedApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_group(
        self,
        request: main_models.DescribePurchasedApiGroupRequest,
    ) -> main_models.DescribePurchasedApiGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_purchased_api_group_with_options(request, runtime)

    async def describe_purchased_api_group_async(
        self,
        request: main_models.DescribePurchasedApiGroupRequest,
    ) -> main_models.DescribePurchasedApiGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_purchased_api_group_with_options_async(request, runtime)

    def describe_purchased_api_groups_with_options(
        self,
        request: main_models.DescribePurchasedApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedApiGroups',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_groups_with_options_async(
        self,
        request: main_models.DescribePurchasedApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedApiGroups',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_groups(
        self,
        request: main_models.DescribePurchasedApiGroupsRequest,
    ) -> main_models.DescribePurchasedApiGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_purchased_api_groups_with_options(request, runtime)

    async def describe_purchased_api_groups_async(
        self,
        request: main_models.DescribePurchasedApiGroupsRequest,
    ) -> main_models.DescribePurchasedApiGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_purchased_api_groups_with_options_async(request, runtime)

    def describe_purchased_apis_with_options(
        self,
        request: main_models.DescribePurchasedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_apis_with_options_async(
        self,
        request: main_models.DescribePurchasedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_apis(
        self,
        request: main_models.DescribePurchasedApisRequest,
    ) -> main_models.DescribePurchasedApisResponse:
        runtime = RuntimeOptions()
        return self.describe_purchased_apis_with_options(request, runtime)

    async def describe_purchased_apis_async(
        self,
        request: main_models.DescribePurchasedApisRequest,
    ) -> main_models.DescribePurchasedApisResponse:
        runtime = RuntimeOptions()
        return await self.describe_purchased_apis_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2016-07-14',
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
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2016-07-14',
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

    def describe_signatures_with_options(
        self,
        request: main_models.DescribeSignaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSignaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSignatures',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_signatures_with_options_async(
        self,
        request: main_models.DescribeSignaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSignaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSignatures',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_signatures(
        self,
        request: main_models.DescribeSignaturesRequest,
    ) -> main_models.DescribeSignaturesResponse:
        runtime = RuntimeOptions()
        return self.describe_signatures_with_options(request, runtime)

    async def describe_signatures_async(
        self,
        request: main_models.DescribeSignaturesRequest,
    ) -> main_models.DescribeSignaturesResponse:
        runtime = RuntimeOptions()
        return await self.describe_signatures_with_options_async(request, runtime)

    def describe_signatures_by_api_with_options(
        self,
        request: main_models.DescribeSignaturesByApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSignaturesByApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSignaturesByApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSignaturesByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_signatures_by_api_with_options_async(
        self,
        request: main_models.DescribeSignaturesByApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSignaturesByApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSignaturesByApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSignaturesByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_signatures_by_api(
        self,
        request: main_models.DescribeSignaturesByApiRequest,
    ) -> main_models.DescribeSignaturesByApiResponse:
        runtime = RuntimeOptions()
        return self.describe_signatures_by_api_with_options(request, runtime)

    async def describe_signatures_by_api_async(
        self,
        request: main_models.DescribeSignaturesByApiRequest,
    ) -> main_models.DescribeSignaturesByApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_signatures_by_api_with_options_async(request, runtime)

    def describe_summary_data_with_options(
        self,
        request: main_models.DescribeSummaryDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSummaryDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSummaryData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSummaryDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_summary_data_with_options_async(
        self,
        request: main_models.DescribeSummaryDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSummaryDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSummaryData',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSummaryDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_summary_data(
        self,
        request: main_models.DescribeSummaryDataRequest,
    ) -> main_models.DescribeSummaryDataResponse:
        runtime = RuntimeOptions()
        return self.describe_summary_data_with_options(request, runtime)

    async def describe_summary_data_async(
        self,
        request: main_models.DescribeSummaryDataRequest,
    ) -> main_models.DescribeSummaryDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_summary_data_with_options_async(request, runtime)

    def describe_system_parameters_with_options(
        self,
        request: main_models.DescribeSystemParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemParameters',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_parameters_with_options_async(
        self,
        request: main_models.DescribeSystemParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemParameters',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_parameters(
        self,
        request: main_models.DescribeSystemParametersRequest,
    ) -> main_models.DescribeSystemParametersResponse:
        runtime = RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    async def describe_system_parameters_async(
        self,
        request: main_models.DescribeSystemParametersRequest,
    ) -> main_models.DescribeSystemParametersResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_parameters_with_options_async(request, runtime)

    def describe_traffic_controls_with_options(
        self,
        request: main_models.DescribeTrafficControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not DaraCore.is_null(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrafficControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_controls_with_options_async(
        self,
        request: main_models.DescribeTrafficControlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficControlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not DaraCore.is_null(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrafficControls',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_controls(
        self,
        request: main_models.DescribeTrafficControlsRequest,
    ) -> main_models.DescribeTrafficControlsResponse:
        runtime = RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    async def describe_traffic_controls_async(
        self,
        request: main_models.DescribeTrafficControlsRequest,
    ) -> main_models.DescribeTrafficControlsResponse:
        runtime = RuntimeOptions()
        return await self.describe_traffic_controls_with_options_async(request, runtime)

    def describe_traffic_controls_by_api_with_options(
        self,
        request: main_models.DescribeTrafficControlsByApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficControlsByApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrafficControlsByApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficControlsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_controls_by_api_with_options_async(
        self,
        request: main_models.DescribeTrafficControlsByApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficControlsByApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrafficControlsByApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficControlsByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_controls_by_api(
        self,
        request: main_models.DescribeTrafficControlsByApiRequest,
    ) -> main_models.DescribeTrafficControlsByApiResponse:
        runtime = RuntimeOptions()
        return self.describe_traffic_controls_by_api_with_options(request, runtime)

    async def describe_traffic_controls_by_api_async(
        self,
        request: main_models.DescribeTrafficControlsByApiRequest,
    ) -> main_models.DescribeTrafficControlsByApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_traffic_controls_by_api_with_options_async(request, runtime)

    def describe_update_backend_task_with_options(
        self,
        request: main_models.DescribeUpdateBackendTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUpdateBackendTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUpdateBackendTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUpdateBackendTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_update_backend_task_with_options_async(
        self,
        request: main_models.DescribeUpdateBackendTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUpdateBackendTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUpdateBackendTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUpdateBackendTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_update_backend_task(
        self,
        request: main_models.DescribeUpdateBackendTaskRequest,
    ) -> main_models.DescribeUpdateBackendTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_update_backend_task_with_options(request, runtime)

    async def describe_update_backend_task_async(
        self,
        request: main_models.DescribeUpdateBackendTaskRequest,
    ) -> main_models.DescribeUpdateBackendTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_update_backend_task_with_options_async(request, runtime)

    def describe_update_vpc_info_task_with_options(
        self,
        request: main_models.DescribeUpdateVpcInfoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUpdateVpcInfoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUpdateVpcInfoTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUpdateVpcInfoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_update_vpc_info_task_with_options_async(
        self,
        request: main_models.DescribeUpdateVpcInfoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUpdateVpcInfoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUpdateVpcInfoTask',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUpdateVpcInfoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_update_vpc_info_task(
        self,
        request: main_models.DescribeUpdateVpcInfoTaskRequest,
    ) -> main_models.DescribeUpdateVpcInfoTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_update_vpc_info_task_with_options(request, runtime)

    async def describe_update_vpc_info_task_async(
        self,
        request: main_models.DescribeUpdateVpcInfoTaskRequest,
    ) -> main_models.DescribeUpdateVpcInfoTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_update_vpc_info_task_with_options_async(request, runtime)

    def describe_vpc_accesses_with_options(
        self,
        request: main_models.DescribeVpcAccessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcAccessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accurate_query):
            query['AccurateQuery'] = request.accurate_query
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_access_id):
            query['VpcAccessId'] = request.vpc_access_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcAccesses',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcAccessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_accesses_with_options_async(
        self,
        request: main_models.DescribeVpcAccessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcAccessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accurate_query):
            query['AccurateQuery'] = request.accurate_query
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_access_id):
            query['VpcAccessId'] = request.vpc_access_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcAccesses',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcAccessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_accesses(
        self,
        request: main_models.DescribeVpcAccessesRequest,
    ) -> main_models.DescribeVpcAccessesResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_accesses_with_options(request, runtime)

    async def describe_vpc_accesses_async(
        self,
        request: main_models.DescribeVpcAccessesRequest,
    ) -> main_models.DescribeVpcAccessesResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_accesses_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_api_product_with_options(
        self,
        request: main_models.DetachApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.apis):
            query['Apis'] = request.apis
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_api_product_with_options_async(
        self,
        request: main_models.DetachApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.apis):
            query['Apis'] = request.apis
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachApiProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_api_product(
        self,
        request: main_models.DetachApiProductRequest,
    ) -> main_models.DetachApiProductResponse:
        runtime = RuntimeOptions()
        return self.detach_api_product_with_options(request, runtime)

    async def detach_api_product_async(
        self,
        request: main_models.DetachApiProductRequest,
    ) -> main_models.DetachApiProductResponse:
        runtime = RuntimeOptions()
        return await self.detach_api_product_with_options_async(request, runtime)

    def detach_group_plugin_with_options(
        self,
        request: main_models.DetachGroupPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachGroupPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachGroupPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachGroupPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_group_plugin_with_options_async(
        self,
        request: main_models.DetachGroupPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachGroupPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachGroupPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachGroupPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_group_plugin(
        self,
        request: main_models.DetachGroupPluginRequest,
    ) -> main_models.DetachGroupPluginResponse:
        runtime = RuntimeOptions()
        return self.detach_group_plugin_with_options(request, runtime)

    async def detach_group_plugin_async(
        self,
        request: main_models.DetachGroupPluginRequest,
    ) -> main_models.DetachGroupPluginResponse:
        runtime = RuntimeOptions()
        return await self.detach_group_plugin_with_options_async(request, runtime)

    def detach_plugin_with_options(
        self,
        request: main_models.DetachPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_plugin_with_options_async(
        self,
        request: main_models.DetachPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_plugin(
        self,
        request: main_models.DetachPluginRequest,
    ) -> main_models.DetachPluginResponse:
        runtime = RuntimeOptions()
        return self.detach_plugin_with_options(request, runtime)

    async def detach_plugin_async(
        self,
        request: main_models.DetachPluginRequest,
    ) -> main_models.DetachPluginResponse:
        runtime = RuntimeOptions()
        return await self.detach_plugin_with_options_async(request, runtime)

    def disable_instance_access_control_with_options(
        self,
        request: main_models.DisableInstanceAccessControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstanceAccessControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstanceAccessControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstanceAccessControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_access_control_with_options_async(
        self,
        request: main_models.DisableInstanceAccessControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstanceAccessControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstanceAccessControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstanceAccessControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_instance_access_control(
        self,
        request: main_models.DisableInstanceAccessControlRequest,
    ) -> main_models.DisableInstanceAccessControlResponse:
        runtime = RuntimeOptions()
        return self.disable_instance_access_control_with_options(request, runtime)

    async def disable_instance_access_control_async(
        self,
        request: main_models.DisableInstanceAccessControlRequest,
    ) -> main_models.DisableInstanceAccessControlResponse:
        runtime = RuntimeOptions()
        return await self.disable_instance_access_control_with_options_async(request, runtime)

    def dissociate_instance_with_private_dnswith_options(
        self,
        tmp_req: main_models.DissociateInstanceWithPrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateInstanceWithPrivateDNSResponse:
        tmp_req.validate()
        request = main_models.DissociateInstanceWithPrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intranet_domains):
            request.intranet_domains_shrink = Utils.array_to_string_with_specified_style(tmp_req.intranet_domains, 'IntranetDomains', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.intranet_domains_shrink):
            body['IntranetDomains'] = request.intranet_domains_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DissociateInstanceWithPrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateInstanceWithPrivateDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_instance_with_private_dnswith_options_async(
        self,
        tmp_req: main_models.DissociateInstanceWithPrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateInstanceWithPrivateDNSResponse:
        tmp_req.validate()
        request = main_models.DissociateInstanceWithPrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intranet_domains):
            request.intranet_domains_shrink = Utils.array_to_string_with_specified_style(tmp_req.intranet_domains, 'IntranetDomains', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.intranet_domains_shrink):
            body['IntranetDomains'] = request.intranet_domains_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DissociateInstanceWithPrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateInstanceWithPrivateDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_instance_with_private_dns(
        self,
        request: main_models.DissociateInstanceWithPrivateDNSRequest,
    ) -> main_models.DissociateInstanceWithPrivateDNSResponse:
        runtime = RuntimeOptions()
        return self.dissociate_instance_with_private_dnswith_options(request, runtime)

    async def dissociate_instance_with_private_dns_async(
        self,
        request: main_models.DissociateInstanceWithPrivateDNSRequest,
    ) -> main_models.DissociateInstanceWithPrivateDNSResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_instance_with_private_dnswith_options_async(request, runtime)

    def dry_run_swagger_with_options(
        self,
        tmp_req: main_models.DryRunSwaggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DryRunSwaggerResponse:
        tmp_req.validate()
        request = main_models.DryRunSwaggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_condition):
            request.global_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.data_format):
            query['DataFormat'] = request.data_format
        if not DaraCore.is_null(request.global_condition_shrink):
            query['GlobalCondition'] = request.global_condition_shrink
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DryRunSwagger',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DryRunSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dry_run_swagger_with_options_async(
        self,
        tmp_req: main_models.DryRunSwaggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DryRunSwaggerResponse:
        tmp_req.validate()
        request = main_models.DryRunSwaggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_condition):
            request.global_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.data_format):
            query['DataFormat'] = request.data_format
        if not DaraCore.is_null(request.global_condition_shrink):
            query['GlobalCondition'] = request.global_condition_shrink
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DryRunSwagger',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DryRunSwaggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dry_run_swagger(
        self,
        request: main_models.DryRunSwaggerRequest,
    ) -> main_models.DryRunSwaggerResponse:
        runtime = RuntimeOptions()
        return self.dry_run_swagger_with_options(request, runtime)

    async def dry_run_swagger_async(
        self,
        request: main_models.DryRunSwaggerRequest,
    ) -> main_models.DryRunSwaggerResponse:
        runtime = RuntimeOptions()
        return await self.dry_run_swagger_with_options_async(request, runtime)

    def enable_instance_access_control_with_options(
        self,
        request: main_models.EnableInstanceAccessControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInstanceAccessControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInstanceAccessControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInstanceAccessControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_access_control_with_options_async(
        self,
        request: main_models.EnableInstanceAccessControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInstanceAccessControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInstanceAccessControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInstanceAccessControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_instance_access_control(
        self,
        request: main_models.EnableInstanceAccessControlRequest,
    ) -> main_models.EnableInstanceAccessControlResponse:
        runtime = RuntimeOptions()
        return self.enable_instance_access_control_with_options(request, runtime)

    async def enable_instance_access_control_async(
        self,
        request: main_models.EnableInstanceAccessControlRequest,
    ) -> main_models.EnableInstanceAccessControlResponse:
        runtime = RuntimeOptions()
        return await self.enable_instance_access_control_with_options_async(request, runtime)

    def export_oaswith_options(
        self,
        tmp_req: main_models.ExportOASRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportOASResponse:
        tmp_req.validate()
        request = main_models.ExportOASShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_id_list):
            request.api_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_id_list, 'ApiIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.api_id_list_shrink):
            query['ApiIdList'] = request.api_id_list_shrink
        if not DaraCore.is_null(request.data_format):
            query['DataFormat'] = request.data_format
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.oas_version):
            query['OasVersion'] = request.oas_version
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.with_xextensions):
            query['WithXExtensions'] = request.with_xextensions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportOAS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportOASResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_oaswith_options_async(
        self,
        tmp_req: main_models.ExportOASRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportOASResponse:
        tmp_req.validate()
        request = main_models.ExportOASShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_id_list):
            request.api_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_id_list, 'ApiIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.api_id_list_shrink):
            query['ApiIdList'] = request.api_id_list_shrink
        if not DaraCore.is_null(request.data_format):
            query['DataFormat'] = request.data_format
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.oas_version):
            query['OasVersion'] = request.oas_version
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.with_xextensions):
            query['WithXExtensions'] = request.with_xextensions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportOAS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportOASResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_oas(
        self,
        request: main_models.ExportOASRequest,
    ) -> main_models.ExportOASResponse:
        runtime = RuntimeOptions()
        return self.export_oaswith_options(request, runtime)

    async def export_oas_async(
        self,
        request: main_models.ExportOASRequest,
    ) -> main_models.ExportOASResponse:
        runtime = RuntimeOptions()
        return await self.export_oaswith_options_async(request, runtime)

    def import_oaswith_options(
        self,
        request: main_models.ImportOASRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportOASResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ignore_warning):
            query['IgnoreWarning'] = request.ignore_warning
        if not DaraCore.is_null(request.oasversion):
            query['OASVersion'] = request.oasversion
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.request_mode):
            query['RequestMode'] = request.request_mode
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.skip_dry_run):
            query['SkipDryRun'] = request.skip_dry_run
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportOAS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportOASResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_oaswith_options_async(
        self,
        request: main_models.ImportOASRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportOASResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ignore_warning):
            query['IgnoreWarning'] = request.ignore_warning
        if not DaraCore.is_null(request.oasversion):
            query['OASVersion'] = request.oasversion
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.request_mode):
            query['RequestMode'] = request.request_mode
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.skip_dry_run):
            query['SkipDryRun'] = request.skip_dry_run
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportOAS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportOASResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_oas(
        self,
        request: main_models.ImportOASRequest,
    ) -> main_models.ImportOASResponse:
        runtime = RuntimeOptions()
        return self.import_oaswith_options(request, runtime)

    async def import_oas_async(
        self,
        request: main_models.ImportOASRequest,
    ) -> main_models.ImportOASResponse:
        runtime = RuntimeOptions()
        return await self.import_oaswith_options_async(request, runtime)

    def import_swagger_with_options(
        self,
        tmp_req: main_models.ImportSwaggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportSwaggerResponse:
        tmp_req.validate()
        request = main_models.ImportSwaggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_condition):
            request.global_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.data_format):
            query['DataFormat'] = request.data_format
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.global_condition_shrink):
            query['GlobalCondition'] = request.global_condition_shrink
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportSwagger',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_swagger_with_options_async(
        self,
        tmp_req: main_models.ImportSwaggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportSwaggerResponse:
        tmp_req.validate()
        request = main_models.ImportSwaggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_condition):
            request.global_condition_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        if not DaraCore.is_null(request.data_format):
            query['DataFormat'] = request.data_format
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.global_condition_shrink):
            query['GlobalCondition'] = request.global_condition_shrink
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportSwagger',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportSwaggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_swagger(
        self,
        request: main_models.ImportSwaggerRequest,
    ) -> main_models.ImportSwaggerResponse:
        runtime = RuntimeOptions()
        return self.import_swagger_with_options(request, runtime)

    async def import_swagger_async(
        self,
        request: main_models.ImportSwaggerRequest,
    ) -> main_models.ImportSwaggerResponse:
        runtime = RuntimeOptions()
        return await self.import_swagger_with_options_async(request, runtime)

    def list_private_dnswith_options(
        self,
        request: main_models.ListPrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_dnswith_options_async(
        self,
        request: main_models.ListPrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateDNSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_dns(
        self,
        request: main_models.ListPrivateDNSRequest,
    ) -> main_models.ListPrivateDNSResponse:
        runtime = RuntimeOptions()
        return self.list_private_dnswith_options(request, runtime)

    async def list_private_dns_async(
        self,
        request: main_models.ListPrivateDNSRequest,
    ) -> main_models.ListPrivateDNSResponse:
        runtime = RuntimeOptions()
        return await self.list_private_dnswith_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
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
            version = '2016-07-14',
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
            version = '2016-07-14',
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

    def modify_api_with_options(
        self,
        request: main_models.ModifyApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_enable):
            query['BackendEnable'] = request.backend_enable
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not DaraCore.is_null(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not DaraCore.is_null(request.request_config):
            query['RequestConfig'] = request.request_config
        if not DaraCore.is_null(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        if not DaraCore.is_null(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        body = {}
        if not DaraCore.is_null(request.constant_parameters):
            body['ConstantParameters'] = request.constant_parameters
        if not DaraCore.is_null(request.error_code_samples):
            body['ErrorCodeSamples'] = request.error_code_samples
        if not DaraCore.is_null(request.fail_result_sample):
            body['FailResultSample'] = request.fail_result_sample
        if not DaraCore.is_null(request.request_parameters):
            body['RequestParameters'] = request.request_parameters
        if not DaraCore.is_null(request.result_descriptions):
            body['ResultDescriptions'] = request.result_descriptions
        if not DaraCore.is_null(request.result_sample):
            body['ResultSample'] = request.result_sample
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        if not DaraCore.is_null(request.service_parameters_map):
            body['ServiceParametersMap'] = request.service_parameters_map
        if not DaraCore.is_null(request.system_parameters):
            body['SystemParameters'] = request.system_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_with_options_async(
        self,
        request: main_models.ModifyApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_enable):
            query['BackendEnable'] = request.backend_enable
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not DaraCore.is_null(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not DaraCore.is_null(request.request_config):
            query['RequestConfig'] = request.request_config
        if not DaraCore.is_null(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        if not DaraCore.is_null(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        body = {}
        if not DaraCore.is_null(request.constant_parameters):
            body['ConstantParameters'] = request.constant_parameters
        if not DaraCore.is_null(request.error_code_samples):
            body['ErrorCodeSamples'] = request.error_code_samples
        if not DaraCore.is_null(request.fail_result_sample):
            body['FailResultSample'] = request.fail_result_sample
        if not DaraCore.is_null(request.request_parameters):
            body['RequestParameters'] = request.request_parameters
        if not DaraCore.is_null(request.result_descriptions):
            body['ResultDescriptions'] = request.result_descriptions
        if not DaraCore.is_null(request.result_sample):
            body['ResultSample'] = request.result_sample
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        if not DaraCore.is_null(request.service_parameters_map):
            body['ServiceParametersMap'] = request.service_parameters_map
        if not DaraCore.is_null(request.system_parameters):
            body['SystemParameters'] = request.system_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api(
        self,
        request: main_models.ModifyApiRequest,
    ) -> main_models.ModifyApiResponse:
        runtime = RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    async def modify_api_async(
        self,
        request: main_models.ModifyApiRequest,
    ) -> main_models.ModifyApiResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_with_options_async(request, runtime)

    def modify_api_configuration_with_options(
        self,
        request: main_models.ModifyApiConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.body_format):
            query['BodyFormat'] = request.body_format
        if not DaraCore.is_null(request.body_model):
            query['BodyModel'] = request.body_model
        if not DaraCore.is_null(request.content_type_category):
            query['ContentTypeCategory'] = request.content_type_category
        if not DaraCore.is_null(request.content_type_value):
            query['ContentTypeValue'] = request.content_type_value
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not DaraCore.is_null(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not DaraCore.is_null(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not DaraCore.is_null(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not DaraCore.is_null(request.function_compute_config):
            query['FunctionComputeConfig'] = request.function_compute_config
        if not DaraCore.is_null(request.http_config):
            query['HttpConfig'] = request.http_config
        if not DaraCore.is_null(request.mock_config):
            query['MockConfig'] = request.mock_config
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.oss_config):
            query['OssConfig'] = request.oss_config
        if not DaraCore.is_null(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not DaraCore.is_null(request.request_http_method):
            query['RequestHttpMethod'] = request.request_http_method
        if not DaraCore.is_null(request.request_mode):
            query['RequestMode'] = request.request_mode
        if not DaraCore.is_null(request.request_parameters):
            query['RequestParameters'] = request.request_parameters
        if not DaraCore.is_null(request.request_path):
            query['RequestPath'] = request.request_path
        if not DaraCore.is_null(request.request_protocol):
            query['RequestProtocol'] = request.request_protocol
        if not DaraCore.is_null(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not DaraCore.is_null(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not DaraCore.is_null(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not DaraCore.is_null(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not DaraCore.is_null(request.use_backend_service):
            query['UseBackendService'] = request.use_backend_service
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        if not DaraCore.is_null(request.vpc_config):
            query['VpcConfig'] = request.vpc_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiConfiguration',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_configuration_with_options_async(
        self,
        request: main_models.ModifyApiConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.body_format):
            query['BodyFormat'] = request.body_format
        if not DaraCore.is_null(request.body_model):
            query['BodyModel'] = request.body_model
        if not DaraCore.is_null(request.content_type_category):
            query['ContentTypeCategory'] = request.content_type_category
        if not DaraCore.is_null(request.content_type_value):
            query['ContentTypeValue'] = request.content_type_value
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not DaraCore.is_null(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not DaraCore.is_null(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not DaraCore.is_null(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not DaraCore.is_null(request.function_compute_config):
            query['FunctionComputeConfig'] = request.function_compute_config
        if not DaraCore.is_null(request.http_config):
            query['HttpConfig'] = request.http_config
        if not DaraCore.is_null(request.mock_config):
            query['MockConfig'] = request.mock_config
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.oss_config):
            query['OssConfig'] = request.oss_config
        if not DaraCore.is_null(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not DaraCore.is_null(request.request_http_method):
            query['RequestHttpMethod'] = request.request_http_method
        if not DaraCore.is_null(request.request_mode):
            query['RequestMode'] = request.request_mode
        if not DaraCore.is_null(request.request_parameters):
            query['RequestParameters'] = request.request_parameters
        if not DaraCore.is_null(request.request_path):
            query['RequestPath'] = request.request_path
        if not DaraCore.is_null(request.request_protocol):
            query['RequestProtocol'] = request.request_protocol
        if not DaraCore.is_null(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not DaraCore.is_null(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not DaraCore.is_null(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not DaraCore.is_null(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not DaraCore.is_null(request.use_backend_service):
            query['UseBackendService'] = request.use_backend_service
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        if not DaraCore.is_null(request.vpc_config):
            query['VpcConfig'] = request.vpc_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiConfiguration',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_configuration(
        self,
        request: main_models.ModifyApiConfigurationRequest,
    ) -> main_models.ModifyApiConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_api_configuration_with_options(request, runtime)

    async def modify_api_configuration_async(
        self,
        request: main_models.ModifyApiConfigurationRequest,
    ) -> main_models.ModifyApiConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_configuration_with_options_async(request, runtime)

    def modify_api_group_with_options(
        self,
        request: main_models.ModifyApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_path):
            query['BasePath'] = request.base_path
        if not DaraCore.is_null(request.compatible_flags):
            query['CompatibleFlags'] = request.compatible_flags
        if not DaraCore.is_null(request.custom_app_code_config):
            query['CustomAppCodeConfig'] = request.custom_app_code_config
        if not DaraCore.is_null(request.custom_trace_config):
            query['CustomTraceConfig'] = request.custom_trace_config
        if not DaraCore.is_null(request.customer_configs):
            query['CustomerConfigs'] = request.customer_configs
        if not DaraCore.is_null(request.default_domain):
            query['DefaultDomain'] = request.default_domain
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.filter_app_code_for_backend):
            query['FilterAppCodeForBackend'] = request.filter_app_code_for_backend
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.passthrough_headers):
            query['PassthroughHeaders'] = request.passthrough_headers
        if not DaraCore.is_null(request.rpc_pattern):
            query['RpcPattern'] = request.rpc_pattern
        if not DaraCore.is_null(request.rps_limit_for_serverless):
            query['RpsLimitForServerless'] = request.rps_limit_for_serverless
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.support_sse):
            query['SupportSSE'] = request.support_sse
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_log_config):
            query['UserLogConfig'] = request.user_log_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_with_options_async(
        self,
        request: main_models.ModifyApiGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_path):
            query['BasePath'] = request.base_path
        if not DaraCore.is_null(request.compatible_flags):
            query['CompatibleFlags'] = request.compatible_flags
        if not DaraCore.is_null(request.custom_app_code_config):
            query['CustomAppCodeConfig'] = request.custom_app_code_config
        if not DaraCore.is_null(request.custom_trace_config):
            query['CustomTraceConfig'] = request.custom_trace_config
        if not DaraCore.is_null(request.customer_configs):
            query['CustomerConfigs'] = request.customer_configs
        if not DaraCore.is_null(request.default_domain):
            query['DefaultDomain'] = request.default_domain
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.filter_app_code_for_backend):
            query['FilterAppCodeForBackend'] = request.filter_app_code_for_backend
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.passthrough_headers):
            query['PassthroughHeaders'] = request.passthrough_headers
        if not DaraCore.is_null(request.rpc_pattern):
            query['RpcPattern'] = request.rpc_pattern
        if not DaraCore.is_null(request.rps_limit_for_serverless):
            query['RpsLimitForServerless'] = request.rps_limit_for_serverless
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.support_sse):
            query['SupportSSE'] = request.support_sse
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_log_config):
            query['UserLogConfig'] = request.user_log_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group(
        self,
        request: main_models.ModifyApiGroupRequest,
    ) -> main_models.ModifyApiGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    async def modify_api_group_async(
        self,
        request: main_models.ModifyApiGroupRequest,
    ) -> main_models.ModifyApiGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_group_with_options_async(request, runtime)

    def modify_api_group_instance_with_options(
        self,
        request: main_models.ModifyApiGroupInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroupInstance',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_instance_with_options_async(
        self,
        request: main_models.ModifyApiGroupInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroupInstance',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group_instance(
        self,
        request: main_models.ModifyApiGroupInstanceRequest,
    ) -> main_models.ModifyApiGroupInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_api_group_instance_with_options(request, runtime)

    async def modify_api_group_instance_async(
        self,
        request: main_models.ModifyApiGroupInstanceRequest,
    ) -> main_models.ModifyApiGroupInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_group_instance_with_options_async(request, runtime)

    def modify_api_group_network_policy_with_options(
        self,
        request: main_models.ModifyApiGroupNetworkPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupNetworkPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not DaraCore.is_null(request.inner_domain_enable):
            query['InnerDomainEnable'] = request.inner_domain_enable
        if not DaraCore.is_null(request.internet_enable):
            query['InternetEnable'] = request.internet_enable
        if not DaraCore.is_null(request.internet_ipv6enable):
            query['InternetIPV6Enable'] = request.internet_ipv6enable
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_intranet_enable):
            query['VpcIntranetEnable'] = request.vpc_intranet_enable
        if not DaraCore.is_null(request.vpc_slb_intranet_enable):
            query['VpcSlbIntranetEnable'] = request.vpc_slb_intranet_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroupNetworkPolicy',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupNetworkPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_network_policy_with_options_async(
        self,
        request: main_models.ModifyApiGroupNetworkPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupNetworkPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not DaraCore.is_null(request.inner_domain_enable):
            query['InnerDomainEnable'] = request.inner_domain_enable
        if not DaraCore.is_null(request.internet_enable):
            query['InternetEnable'] = request.internet_enable
        if not DaraCore.is_null(request.internet_ipv6enable):
            query['InternetIPV6Enable'] = request.internet_ipv6enable
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_intranet_enable):
            query['VpcIntranetEnable'] = request.vpc_intranet_enable
        if not DaraCore.is_null(request.vpc_slb_intranet_enable):
            query['VpcSlbIntranetEnable'] = request.vpc_slb_intranet_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroupNetworkPolicy',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupNetworkPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group_network_policy(
        self,
        request: main_models.ModifyApiGroupNetworkPolicyRequest,
    ) -> main_models.ModifyApiGroupNetworkPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_api_group_network_policy_with_options(request, runtime)

    async def modify_api_group_network_policy_async(
        self,
        request: main_models.ModifyApiGroupNetworkPolicyRequest,
    ) -> main_models.ModifyApiGroupNetworkPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_group_network_policy_with_options_async(request, runtime)

    def modify_api_group_vpc_whitelist_with_options(
        self,
        request: main_models.ModifyApiGroupVpcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupVpcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroupVpcWhitelist',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupVpcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_vpc_whitelist_with_options_async(
        self,
        request: main_models.ModifyApiGroupVpcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiGroupVpcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiGroupVpcWhitelist',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiGroupVpcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group_vpc_whitelist(
        self,
        request: main_models.ModifyApiGroupVpcWhitelistRequest,
    ) -> main_models.ModifyApiGroupVpcWhitelistResponse:
        runtime = RuntimeOptions()
        return self.modify_api_group_vpc_whitelist_with_options(request, runtime)

    async def modify_api_group_vpc_whitelist_async(
        self,
        request: main_models.ModifyApiGroupVpcWhitelistRequest,
    ) -> main_models.ModifyApiGroupVpcWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_group_vpc_whitelist_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_backend_with_options(
        self,
        request: main_models.ModifyBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backend_with_options_async(
        self,
        request: main_models.ModifyBackendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_name):
            query['BackendName'] = request.backend_name
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackend',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backend(
        self,
        request: main_models.ModifyBackendRequest,
    ) -> main_models.ModifyBackendResponse:
        runtime = RuntimeOptions()
        return self.modify_backend_with_options(request, runtime)

    async def modify_backend_async(
        self,
        request: main_models.ModifyBackendRequest,
    ) -> main_models.ModifyBackendResponse:
        runtime = RuntimeOptions()
        return await self.modify_backend_with_options_async(request, runtime)

    def modify_backend_model_with_options(
        self,
        request: main_models.ModifyBackendModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackendModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_model_data):
            query['BackendModelData'] = request.backend_model_data
        if not DaraCore.is_null(request.backend_model_id):
            query['BackendModelId'] = request.backend_model_id
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackendModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackendModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backend_model_with_options_async(
        self,
        request: main_models.ModifyBackendModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackendModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_id):
            query['BackendId'] = request.backend_id
        if not DaraCore.is_null(request.backend_model_data):
            query['BackendModelData'] = request.backend_model_data
        if not DaraCore.is_null(request.backend_model_id):
            query['BackendModelId'] = request.backend_model_id
        if not DaraCore.is_null(request.backend_type):
            query['BackendType'] = request.backend_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackendModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackendModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backend_model(
        self,
        request: main_models.ModifyBackendModelRequest,
    ) -> main_models.ModifyBackendModelResponse:
        runtime = RuntimeOptions()
        return self.modify_backend_model_with_options(request, runtime)

    async def modify_backend_model_async(
        self,
        request: main_models.ModifyBackendModelRequest,
    ) -> main_models.ModifyBackendModelResponse:
        runtime = RuntimeOptions()
        return await self.modify_backend_model_with_options_async(request, runtime)

    def modify_dataset_with_options(
        self,
        request: main_models.ModifyDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataset',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dataset_with_options_async(
        self,
        request: main_models.ModifyDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataset',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dataset(
        self,
        request: main_models.ModifyDatasetRequest,
    ) -> main_models.ModifyDatasetResponse:
        runtime = RuntimeOptions()
        return self.modify_dataset_with_options(request, runtime)

    async def modify_dataset_async(
        self,
        request: main_models.ModifyDatasetRequest,
    ) -> main_models.ModifyDatasetResponse:
        runtime = RuntimeOptions()
        return await self.modify_dataset_with_options_async(request, runtime)

    def modify_dataset_item_with_options(
        self,
        request: main_models.ModifyDatasetItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatasetItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatasetItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatasetItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dataset_item_with_options_async(
        self,
        request: main_models.ModifyDatasetItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatasetItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatasetItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatasetItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dataset_item(
        self,
        request: main_models.ModifyDatasetItemRequest,
    ) -> main_models.ModifyDatasetItemResponse:
        runtime = RuntimeOptions()
        return self.modify_dataset_item_with_options(request, runtime)

    async def modify_dataset_item_async(
        self,
        request: main_models.ModifyDatasetItemRequest,
    ) -> main_models.ModifyDatasetItemResponse:
        runtime = RuntimeOptions()
        return await self.modify_dataset_item_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        tmp_req: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.to_connect_vpc_ip_block):
            request.to_connect_vpc_ip_block_shrink = Utils.array_to_string_with_specified_style(tmp_req.to_connect_vpc_ip_block, 'ToConnectVpcIpBlock', 'json')
        query = {}
        if not DaraCore.is_null(request.delete_vpc_ip_block):
            query['DeleteVpcIpBlock'] = request.delete_vpc_ip_block
        if not DaraCore.is_null(request.egress_ipv_6enable):
            query['EgressIpv6Enable'] = request.egress_ipv_6enable
        if not DaraCore.is_null(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not DaraCore.is_null(request.ipv6enabled):
            query['IPV6Enabled'] = request.ipv6enabled
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.intranet_segments):
            query['IntranetSegments'] = request.intranet_segments
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not DaraCore.is_null(request.to_connect_vpc_ip_block_shrink):
            query['ToConnectVpcIpBlock'] = request.to_connect_vpc_ip_block_shrink
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vpc_slb_intranet_enable):
            query['VpcSlbIntranetEnable'] = request.vpc_slb_intranet_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2016-07-14',
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
        tmp_req: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        tmp_req.validate()
        request = main_models.ModifyInstanceAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.to_connect_vpc_ip_block):
            request.to_connect_vpc_ip_block_shrink = Utils.array_to_string_with_specified_style(tmp_req.to_connect_vpc_ip_block, 'ToConnectVpcIpBlock', 'json')
        query = {}
        if not DaraCore.is_null(request.delete_vpc_ip_block):
            query['DeleteVpcIpBlock'] = request.delete_vpc_ip_block
        if not DaraCore.is_null(request.egress_ipv_6enable):
            query['EgressIpv6Enable'] = request.egress_ipv_6enable
        if not DaraCore.is_null(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not DaraCore.is_null(request.ipv6enabled):
            query['IPV6Enabled'] = request.ipv6enabled
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.intranet_segments):
            query['IntranetSegments'] = request.intranet_segments
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not DaraCore.is_null(request.to_connect_vpc_ip_block_shrink):
            query['ToConnectVpcIpBlock'] = request.to_connect_vpc_ip_block_shrink
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vpc_slb_intranet_enable):
            query['VpcSlbIntranetEnable'] = request.vpc_slb_intranet_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2016-07-14',
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

    def modify_instance_spec_with_options(
        self,
        request: main_models.ModifyInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.modify_action):
            query['ModifyAction'] = request.modify_action
        if not DaraCore.is_null(request.skip_wait_switch):
            query['SkipWaitSwitch'] = request.skip_wait_switch
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceSpec',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: main_models.ModifyInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.modify_action):
            query['ModifyAction'] = request.modify_action
        if not DaraCore.is_null(request.skip_wait_switch):
            query['SkipWaitSwitch'] = request.skip_wait_switch
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceSpec',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_spec(
        self,
        request: main_models.ModifyInstanceSpecRequest,
    ) -> main_models.ModifyInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: main_models.ModifyInstanceSpecRequest,
    ) -> main_models.ModifyInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_vpc_attribute_for_console_with_options(
        self,
        request: main_models.ModifyInstanceVpcAttributeForConsoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceVpcAttributeForConsoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_vpc_access):
            query['DeleteVpcAccess'] = request.delete_vpc_access
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceVpcAttributeForConsole',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceVpcAttributeForConsoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vpc_attribute_for_console_with_options_async(
        self,
        request: main_models.ModifyInstanceVpcAttributeForConsoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceVpcAttributeForConsoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_vpc_access):
            query['DeleteVpcAccess'] = request.delete_vpc_access
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceVpcAttributeForConsole',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceVpcAttributeForConsoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vpc_attribute_for_console(
        self,
        request: main_models.ModifyInstanceVpcAttributeForConsoleRequest,
    ) -> main_models.ModifyInstanceVpcAttributeForConsoleResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_vpc_attribute_for_console_with_options(request, runtime)

    async def modify_instance_vpc_attribute_for_console_async(
        self,
        request: main_models.ModifyInstanceVpcAttributeForConsoleRequest,
    ) -> main_models.ModifyInstanceVpcAttributeForConsoleResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_vpc_attribute_for_console_with_options_async(request, runtime)

    def modify_intranet_domain_policy_with_options(
        self,
        request: main_models.ModifyIntranetDomainPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIntranetDomainPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_intranet_enable):
            query['VpcIntranetEnable'] = request.vpc_intranet_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIntranetDomainPolicy',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIntranetDomainPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_intranet_domain_policy_with_options_async(
        self,
        request: main_models.ModifyIntranetDomainPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIntranetDomainPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_intranet_enable):
            query['VpcIntranetEnable'] = request.vpc_intranet_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIntranetDomainPolicy',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIntranetDomainPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_intranet_domain_policy(
        self,
        request: main_models.ModifyIntranetDomainPolicyRequest,
    ) -> main_models.ModifyIntranetDomainPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_intranet_domain_policy_with_options(request, runtime)

    async def modify_intranet_domain_policy_async(
        self,
        request: main_models.ModifyIntranetDomainPolicyRequest,
    ) -> main_models.ModifyIntranetDomainPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_intranet_domain_policy_with_options_async(request, runtime)

    def modify_ip_control_with_options(
        self,
        request: main_models.ModifyIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_control_with_options_async(
        self,
        request: main_models.ModifyIpControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_control(
        self,
        request: main_models.ModifyIpControlRequest,
    ) -> main_models.ModifyIpControlResponse:
        runtime = RuntimeOptions()
        return self.modify_ip_control_with_options(request, runtime)

    async def modify_ip_control_async(
        self,
        request: main_models.ModifyIpControlRequest,
    ) -> main_models.ModifyIpControlResponse:
        runtime = RuntimeOptions()
        return await self.modify_ip_control_with_options_async(request, runtime)

    def modify_ip_control_policy_item_with_options(
        self,
        request: main_models.ModifyIpControlPolicyItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpControlPolicyItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpControlPolicyItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_control_policy_item_with_options_async(
        self,
        request: main_models.ModifyIpControlPolicyItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpControlPolicyItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpControlPolicyItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_control_policy_item(
        self,
        request: main_models.ModifyIpControlPolicyItemRequest,
    ) -> main_models.ModifyIpControlPolicyItemResponse:
        runtime = RuntimeOptions()
        return self.modify_ip_control_policy_item_with_options(request, runtime)

    async def modify_ip_control_policy_item_async(
        self,
        request: main_models.ModifyIpControlPolicyItemRequest,
    ) -> main_models.ModifyIpControlPolicyItemResponse:
        runtime = RuntimeOptions()
        return await self.modify_ip_control_policy_item_with_options_async(request, runtime)

    def modify_log_config_with_options(
        self,
        request: main_models.ModifyLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not DaraCore.is_null(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_config_with_options_async(
        self,
        request: main_models.ModifyLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not DaraCore.is_null(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogConfig',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_config(
        self,
        request: main_models.ModifyLogConfigRequest,
    ) -> main_models.ModifyLogConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_log_config_with_options(request, runtime)

    async def modify_log_config_async(
        self,
        request: main_models.ModifyLogConfigRequest,
    ) -> main_models.ModifyLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_log_config_with_options_async(request, runtime)

    def modify_model_with_options(
        self,
        request: main_models.ModifyModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.new_model_name):
            query['NewModelName'] = request.new_model_name
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_model_with_options_async(
        self,
        request: main_models.ModifyModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.new_model_name):
            query['NewModelName'] = request.new_model_name
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyModel',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_model(
        self,
        request: main_models.ModifyModelRequest,
    ) -> main_models.ModifyModelResponse:
        runtime = RuntimeOptions()
        return self.modify_model_with_options(request, runtime)

    async def modify_model_async(
        self,
        request: main_models.ModifyModelRequest,
    ) -> main_models.ModifyModelResponse:
        runtime = RuntimeOptions()
        return await self.modify_model_with_options_async(request, runtime)

    def modify_plugin_with_options(
        self,
        request: main_models.ModifyPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.plugin_data):
            query['PluginData'] = request.plugin_data
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_plugin_with_options_async(
        self,
        request: main_models.ModifyPluginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.plugin_data):
            query['PluginData'] = request.plugin_data
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPlugin',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_plugin(
        self,
        request: main_models.ModifyPluginRequest,
    ) -> main_models.ModifyPluginResponse:
        runtime = RuntimeOptions()
        return self.modify_plugin_with_options(request, runtime)

    async def modify_plugin_async(
        self,
        request: main_models.ModifyPluginRequest,
    ) -> main_models.ModifyPluginResponse:
        runtime = RuntimeOptions()
        return await self.modify_plugin_with_options_async(request, runtime)

    def modify_signature_with_options(
        self,
        request: main_models.ModifySignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.signature_key):
            query['SignatureKey'] = request.signature_key
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        if not DaraCore.is_null(request.signature_secret):
            query['SignatureSecret'] = request.signature_secret
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_signature_with_options_async(
        self,
        request: main_models.ModifySignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.signature_key):
            query['SignatureKey'] = request.signature_key
        if not DaraCore.is_null(request.signature_name):
            query['SignatureName'] = request.signature_name
        if not DaraCore.is_null(request.signature_secret):
            query['SignatureSecret'] = request.signature_secret
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySignature',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_signature(
        self,
        request: main_models.ModifySignatureRequest,
    ) -> main_models.ModifySignatureResponse:
        runtime = RuntimeOptions()
        return self.modify_signature_with_options(request, runtime)

    async def modify_signature_async(
        self,
        request: main_models.ModifySignatureRequest,
    ) -> main_models.ModifySignatureResponse:
        runtime = RuntimeOptions()
        return await self.modify_signature_with_options_async(request, runtime)

    def modify_traffic_control_with_options(
        self,
        request: main_models.ModifyTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_default):
            query['ApiDefault'] = request.api_default
        if not DaraCore.is_null(request.app_default):
            query['AppDefault'] = request.app_default
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not DaraCore.is_null(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not DaraCore.is_null(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not DaraCore.is_null(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_traffic_control_with_options_async(
        self,
        request: main_models.ModifyTrafficControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrafficControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_default):
            query['ApiDefault'] = request.api_default
        if not DaraCore.is_null(request.app_default):
            query['AppDefault'] = request.app_default
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not DaraCore.is_null(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not DaraCore.is_null(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not DaraCore.is_null(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrafficControl',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_traffic_control(
        self,
        request: main_models.ModifyTrafficControlRequest,
    ) -> main_models.ModifyTrafficControlResponse:
        runtime = RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

    async def modify_traffic_control_async(
        self,
        request: main_models.ModifyTrafficControlRequest,
    ) -> main_models.ModifyTrafficControlResponse:
        runtime = RuntimeOptions()
        return await self.modify_traffic_control_with_options_async(request, runtime)

    def modify_vpc_access_and_update_apis_with_options(
        self,
        request: main_models.ModifyVpcAccessAndUpdateApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcAccessAndUpdateApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.refresh):
            query['Refresh'] = request.refresh
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_target_host_name):
            query['VpcTargetHostName'] = request.vpc_target_host_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcAccessAndUpdateApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcAccessAndUpdateApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_access_and_update_apis_with_options_async(
        self,
        request: main_models.ModifyVpcAccessAndUpdateApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcAccessAndUpdateApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.refresh):
            query['Refresh'] = request.refresh
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_target_host_name):
            query['VpcTargetHostName'] = request.vpc_target_host_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcAccessAndUpdateApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcAccessAndUpdateApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_access_and_update_apis(
        self,
        request: main_models.ModifyVpcAccessAndUpdateApisRequest,
    ) -> main_models.ModifyVpcAccessAndUpdateApisResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_access_and_update_apis_with_options(request, runtime)

    async def modify_vpc_access_and_update_apis_async(
        self,
        request: main_models.ModifyVpcAccessAndUpdateApisRequest,
    ) -> main_models.ModifyVpcAccessAndUpdateApisResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_access_and_update_apis_with_options_async(request, runtime)

    def open_api_gateway_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenApiGatewayServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenApiGatewayService',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenApiGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_api_gateway_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenApiGatewayServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenApiGatewayService',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenApiGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_api_gateway_service(self) -> main_models.OpenApiGatewayServiceResponse:
        runtime = RuntimeOptions()
        return self.open_api_gateway_service_with_options(runtime)

    async def open_api_gateway_service_async(self) -> main_models.OpenApiGatewayServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_api_gateway_service_with_options_async(runtime)

    def query_request_logs_with_options(
        self,
        request: main_models.QueryRequestLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRequestLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.request_log_id):
            query['RequestLogId'] = request.request_log_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRequestLogs',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRequestLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_request_logs_with_options_async(
        self,
        request: main_models.QueryRequestLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRequestLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.request_log_id):
            query['RequestLogId'] = request.request_log_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRequestLogs',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRequestLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_request_logs(
        self,
        request: main_models.QueryRequestLogsRequest,
    ) -> main_models.QueryRequestLogsResponse:
        runtime = RuntimeOptions()
        return self.query_request_logs_with_options(request, runtime)

    async def query_request_logs_async(
        self,
        request: main_models.QueryRequestLogsRequest,
    ) -> main_models.QueryRequestLogsResponse:
        runtime = RuntimeOptions()
        return await self.query_request_logs_with_options_async(request, runtime)

    def reactivate_domain_with_options(
        self,
        request: main_models.ReactivateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReactivateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReactivateDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReactivateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reactivate_domain_with_options_async(
        self,
        request: main_models.ReactivateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReactivateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReactivateDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReactivateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reactivate_domain(
        self,
        request: main_models.ReactivateDomainRequest,
    ) -> main_models.ReactivateDomainResponse:
        runtime = RuntimeOptions()
        return self.reactivate_domain_with_options(request, runtime)

    async def reactivate_domain_async(
        self,
        request: main_models.ReactivateDomainRequest,
    ) -> main_models.ReactivateDomainResponse:
        runtime = RuntimeOptions()
        return await self.reactivate_domain_with_options_async(request, runtime)

    def remove_access_control_list_entry_with_options(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAccessControlListEntry',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_control_list_entry_with_options_async(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAccessControlListEntry',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAccessControlListEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_control_list_entry(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return self.remove_access_control_list_entry_with_options(request, runtime)

    async def remove_access_control_list_entry_async(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return await self.remove_access_control_list_entry_with_options_async(request, runtime)

    def remove_api_products_authorities_with_options(
        self,
        tmp_req: main_models.RemoveApiProductsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApiProductsAuthoritiesResponse:
        tmp_req.validate()
        request = main_models.RemoveApiProductsAuthoritiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_product_ids):
            request.api_product_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_product_ids, 'ApiProductIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.api_product_ids_shrink):
            query['ApiProductIds'] = request.api_product_ids_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApiProductsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApiProductsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_api_products_authorities_with_options_async(
        self,
        tmp_req: main_models.RemoveApiProductsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApiProductsAuthoritiesResponse:
        tmp_req.validate()
        request = main_models.RemoveApiProductsAuthoritiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_product_ids):
            request.api_product_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_product_ids, 'ApiProductIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.api_product_ids_shrink):
            query['ApiProductIds'] = request.api_product_ids_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApiProductsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApiProductsAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_api_products_authorities(
        self,
        request: main_models.RemoveApiProductsAuthoritiesRequest,
    ) -> main_models.RemoveApiProductsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return self.remove_api_products_authorities_with_options(request, runtime)

    async def remove_api_products_authorities_async(
        self,
        request: main_models.RemoveApiProductsAuthoritiesRequest,
    ) -> main_models.RemoveApiProductsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return await self.remove_api_products_authorities_with_options_async(request, runtime)

    def remove_apis_authorities_with_options(
        self,
        request: main_models.RemoveApisAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApisAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApisAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_apis_authorities_with_options_async(
        self,
        request: main_models.RemoveApisAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApisAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApisAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApisAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_apis_authorities(
        self,
        request: main_models.RemoveApisAuthoritiesRequest,
    ) -> main_models.RemoveApisAuthoritiesResponse:
        runtime = RuntimeOptions()
        return self.remove_apis_authorities_with_options(request, runtime)

    async def remove_apis_authorities_async(
        self,
        request: main_models.RemoveApisAuthoritiesRequest,
    ) -> main_models.RemoveApisAuthoritiesResponse:
        runtime = RuntimeOptions()
        return await self.remove_apis_authorities_with_options_async(request, runtime)

    def remove_apps_authorities_with_options(
        self,
        request: main_models.RemoveAppsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAppsAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAppsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_apps_authorities_with_options_async(
        self,
        request: main_models.RemoveAppsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAppsAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAppsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAppsAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_apps_authorities(
        self,
        request: main_models.RemoveAppsAuthoritiesRequest,
    ) -> main_models.RemoveAppsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return self.remove_apps_authorities_with_options(request, runtime)

    async def remove_apps_authorities_async(
        self,
        request: main_models.RemoveAppsAuthoritiesRequest,
    ) -> main_models.RemoveAppsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return await self.remove_apps_authorities_with_options_async(request, runtime)

    def remove_ip_control_apis_with_options(
        self,
        request: main_models.RemoveIpControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_control_apis_with_options_async(
        self,
        request: main_models.RemoveIpControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_control_apis(
        self,
        request: main_models.RemoveIpControlApisRequest,
    ) -> main_models.RemoveIpControlApisResponse:
        runtime = RuntimeOptions()
        return self.remove_ip_control_apis_with_options(request, runtime)

    async def remove_ip_control_apis_async(
        self,
        request: main_models.RemoveIpControlApisRequest,
    ) -> main_models.RemoveIpControlApisResponse:
        runtime = RuntimeOptions()
        return await self.remove_ip_control_apis_with_options_async(request, runtime)

    def remove_ip_control_policy_item_with_options(
        self,
        request: main_models.RemoveIpControlPolicyItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpControlPolicyItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.policy_item_ids):
            query['PolicyItemIds'] = request.policy_item_ids
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpControlPolicyItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_control_policy_item_with_options_async(
        self,
        request: main_models.RemoveIpControlPolicyItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpControlPolicyItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.policy_item_ids):
            query['PolicyItemIds'] = request.policy_item_ids
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpControlPolicyItem',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_control_policy_item(
        self,
        request: main_models.RemoveIpControlPolicyItemRequest,
    ) -> main_models.RemoveIpControlPolicyItemResponse:
        runtime = RuntimeOptions()
        return self.remove_ip_control_policy_item_with_options(request, runtime)

    async def remove_ip_control_policy_item_async(
        self,
        request: main_models.RemoveIpControlPolicyItemRequest,
    ) -> main_models.RemoveIpControlPolicyItemResponse:
        runtime = RuntimeOptions()
        return await self.remove_ip_control_policy_item_with_options_async(request, runtime)

    def remove_signature_apis_with_options(
        self,
        request: main_models.RemoveSignatureApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSignatureApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSignatureApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_signature_apis_with_options_async(
        self,
        request: main_models.RemoveSignatureApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSignatureApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSignatureApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSignatureApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_signature_apis(
        self,
        request: main_models.RemoveSignatureApisRequest,
    ) -> main_models.RemoveSignatureApisResponse:
        runtime = RuntimeOptions()
        return self.remove_signature_apis_with_options(request, runtime)

    async def remove_signature_apis_async(
        self,
        request: main_models.RemoveSignatureApisRequest,
    ) -> main_models.RemoveSignatureApisResponse:
        runtime = RuntimeOptions()
        return await self.remove_signature_apis_with_options_async(request, runtime)

    def remove_traffic_control_apis_with_options(
        self,
        request: main_models.RemoveTrafficControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTrafficControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTrafficControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_traffic_control_apis_with_options_async(
        self,
        request: main_models.RemoveTrafficControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTrafficControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTrafficControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTrafficControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_traffic_control_apis(
        self,
        request: main_models.RemoveTrafficControlApisRequest,
    ) -> main_models.RemoveTrafficControlApisResponse:
        runtime = RuntimeOptions()
        return self.remove_traffic_control_apis_with_options(request, runtime)

    async def remove_traffic_control_apis_async(
        self,
        request: main_models.RemoveTrafficControlApisRequest,
    ) -> main_models.RemoveTrafficControlApisResponse:
        runtime = RuntimeOptions()
        return await self.remove_traffic_control_apis_with_options_async(request, runtime)

    def remove_vpc_access_with_options(
        self,
        request: main_models.RemoveVpcAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveVpcAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveVpcAccess',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vpc_access_with_options_async(
        self,
        request: main_models.RemoveVpcAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveVpcAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveVpcAccess',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveVpcAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vpc_access(
        self,
        request: main_models.RemoveVpcAccessRequest,
    ) -> main_models.RemoveVpcAccessResponse:
        runtime = RuntimeOptions()
        return self.remove_vpc_access_with_options(request, runtime)

    async def remove_vpc_access_async(
        self,
        request: main_models.RemoveVpcAccessRequest,
    ) -> main_models.RemoveVpcAccessResponse:
        runtime = RuntimeOptions()
        return await self.remove_vpc_access_with_options_async(request, runtime)

    def remove_vpc_access_and_abolish_apis_with_options(
        self,
        request: main_models.RemoveVpcAccessAndAbolishApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveVpcAccessAndAbolishApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveVpcAccessAndAbolishApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveVpcAccessAndAbolishApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vpc_access_and_abolish_apis_with_options_async(
        self,
        request: main_models.RemoveVpcAccessAndAbolishApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveVpcAccessAndAbolishApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveVpcAccessAndAbolishApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveVpcAccessAndAbolishApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vpc_access_and_abolish_apis(
        self,
        request: main_models.RemoveVpcAccessAndAbolishApisRequest,
    ) -> main_models.RemoveVpcAccessAndAbolishApisResponse:
        runtime = RuntimeOptions()
        return self.remove_vpc_access_and_abolish_apis_with_options(request, runtime)

    async def remove_vpc_access_and_abolish_apis_async(
        self,
        request: main_models.RemoveVpcAccessAndAbolishApisRequest,
    ) -> main_models.RemoveVpcAccessAndAbolishApisResponse:
        runtime = RuntimeOptions()
        return await self.remove_vpc_access_and_abolish_apis_with_options_async(request, runtime)

    def reset_app_code_with_options(
        self,
        request: main_models.ResetAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.new_app_code):
            query['NewAppCode'] = request.new_app_code
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_code_with_options_async(
        self,
        request: main_models.ResetAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.new_app_code):
            query['NewAppCode'] = request.new_app_code
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_code(
        self,
        request: main_models.ResetAppCodeRequest,
    ) -> main_models.ResetAppCodeResponse:
        runtime = RuntimeOptions()
        return self.reset_app_code_with_options(request, runtime)

    async def reset_app_code_async(
        self,
        request: main_models.ResetAppCodeRequest,
    ) -> main_models.ResetAppCodeResponse:
        runtime = RuntimeOptions()
        return await self.reset_app_code_with_options_async(request, runtime)

    def reset_app_secret_with_options(
        self,
        request: main_models.ResetAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.new_app_key):
            query['NewAppKey'] = request.new_app_key
        if not DaraCore.is_null(request.new_app_secret):
            query['NewAppSecret'] = request.new_app_secret
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAppSecret',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_secret_with_options_async(
        self,
        request: main_models.ResetAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.new_app_key):
            query['NewAppKey'] = request.new_app_key
        if not DaraCore.is_null(request.new_app_secret):
            query['NewAppSecret'] = request.new_app_secret
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAppSecret',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_secret(
        self,
        request: main_models.ResetAppSecretRequest,
    ) -> main_models.ResetAppSecretResponse:
        runtime = RuntimeOptions()
        return self.reset_app_secret_with_options(request, runtime)

    async def reset_app_secret_async(
        self,
        request: main_models.ResetAppSecretRequest,
    ) -> main_models.ResetAppSecretResponse:
        runtime = RuntimeOptions()
        return await self.reset_app_secret_with_options_async(request, runtime)

    def sdk_generate_by_app_with_options(
        self,
        request: main_models.SdkGenerateByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdkGenerateByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdkGenerateByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SdkGenerateByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_app_with_options_async(
        self,
        request: main_models.SdkGenerateByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdkGenerateByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdkGenerateByApp',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SdkGenerateByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_app(
        self,
        request: main_models.SdkGenerateByAppRequest,
    ) -> main_models.SdkGenerateByAppResponse:
        runtime = RuntimeOptions()
        return self.sdk_generate_by_app_with_options(request, runtime)

    async def sdk_generate_by_app_async(
        self,
        request: main_models.SdkGenerateByAppRequest,
    ) -> main_models.SdkGenerateByAppResponse:
        runtime = RuntimeOptions()
        return await self.sdk_generate_by_app_with_options_async(request, runtime)

    def sdk_generate_by_app_for_region_with_options(
        self,
        request: main_models.SdkGenerateByAppForRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdkGenerateByAppForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdkGenerateByAppForRegion',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SdkGenerateByAppForRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_app_for_region_with_options_async(
        self,
        request: main_models.SdkGenerateByAppForRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdkGenerateByAppForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdkGenerateByAppForRegion',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SdkGenerateByAppForRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_app_for_region(
        self,
        request: main_models.SdkGenerateByAppForRegionRequest,
    ) -> main_models.SdkGenerateByAppForRegionResponse:
        runtime = RuntimeOptions()
        return self.sdk_generate_by_app_for_region_with_options(request, runtime)

    async def sdk_generate_by_app_for_region_async(
        self,
        request: main_models.SdkGenerateByAppForRegionRequest,
    ) -> main_models.SdkGenerateByAppForRegionResponse:
        runtime = RuntimeOptions()
        return await self.sdk_generate_by_app_for_region_with_options_async(request, runtime)

    def sdk_generate_by_group_with_options(
        self,
        request: main_models.SdkGenerateByGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdkGenerateByGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdkGenerateByGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SdkGenerateByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_group_with_options_async(
        self,
        request: main_models.SdkGenerateByGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SdkGenerateByGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SdkGenerateByGroup',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SdkGenerateByGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_group(
        self,
        request: main_models.SdkGenerateByGroupRequest,
    ) -> main_models.SdkGenerateByGroupResponse:
        runtime = RuntimeOptions()
        return self.sdk_generate_by_group_with_options(request, runtime)

    async def sdk_generate_by_group_async(
        self,
        request: main_models.SdkGenerateByGroupRequest,
    ) -> main_models.SdkGenerateByGroupResponse:
        runtime = RuntimeOptions()
        return await self.sdk_generate_by_group_with_options_async(request, runtime)

    def set_access_control_list_attribute_with_options(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccessControlListAttribute',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_control_list_attribute_with_options_async(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccessControlListAttribute',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccessControlListAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_control_list_attribute(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
    ) -> main_models.SetAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_access_control_list_attribute_with_options(request, runtime)

    async def set_access_control_list_attribute_async(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
    ) -> main_models.SetAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_access_control_list_attribute_with_options_async(request, runtime)

    def set_api_products_authorities_with_options(
        self,
        tmp_req: main_models.SetApiProductsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApiProductsAuthoritiesResponse:
        tmp_req.validate()
        request = main_models.SetApiProductsAuthoritiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_product_ids):
            request.api_product_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_product_ids, 'ApiProductIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.api_product_ids_shrink):
            query['ApiProductIds'] = request.api_product_ids_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApiProductsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApiProductsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_api_products_authorities_with_options_async(
        self,
        tmp_req: main_models.SetApiProductsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApiProductsAuthoritiesResponse:
        tmp_req.validate()
        request = main_models.SetApiProductsAuthoritiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_product_ids):
            request.api_product_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_product_ids, 'ApiProductIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.api_product_ids_shrink):
            query['ApiProductIds'] = request.api_product_ids_shrink
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApiProductsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApiProductsAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_api_products_authorities(
        self,
        request: main_models.SetApiProductsAuthoritiesRequest,
    ) -> main_models.SetApiProductsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return self.set_api_products_authorities_with_options(request, runtime)

    async def set_api_products_authorities_async(
        self,
        request: main_models.SetApiProductsAuthoritiesRequest,
    ) -> main_models.SetApiProductsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return await self.set_api_products_authorities_with_options_async(request, runtime)

    def set_apis_authorities_with_options(
        self,
        request: main_models.SetApisAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApisAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApisAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_apis_authorities_with_options_async(
        self,
        request: main_models.SetApisAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApisAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApisAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApisAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_apis_authorities(
        self,
        request: main_models.SetApisAuthoritiesRequest,
    ) -> main_models.SetApisAuthoritiesResponse:
        runtime = RuntimeOptions()
        return self.set_apis_authorities_with_options(request, runtime)

    async def set_apis_authorities_async(
        self,
        request: main_models.SetApisAuthoritiesRequest,
    ) -> main_models.SetApisAuthoritiesResponse:
        runtime = RuntimeOptions()
        return await self.set_apis_authorities_with_options_async(request, runtime)

    def set_apps_auth_to_api_product_with_options(
        self,
        request: main_models.SetAppsAuthToApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppsAuthToApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppsAuthToApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppsAuthToApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_apps_auth_to_api_product_with_options_async(
        self,
        request: main_models.SetAppsAuthToApiProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppsAuthToApiProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppsAuthToApiProduct',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppsAuthToApiProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_apps_auth_to_api_product(
        self,
        request: main_models.SetAppsAuthToApiProductRequest,
    ) -> main_models.SetAppsAuthToApiProductResponse:
        runtime = RuntimeOptions()
        return self.set_apps_auth_to_api_product_with_options(request, runtime)

    async def set_apps_auth_to_api_product_async(
        self,
        request: main_models.SetAppsAuthToApiProductRequest,
    ) -> main_models.SetAppsAuthToApiProductResponse:
        runtime = RuntimeOptions()
        return await self.set_apps_auth_to_api_product_with_options_async(request, runtime)

    def set_apps_authorities_with_options(
        self,
        request: main_models.SetAppsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppsAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_apps_authorities_with_options_async(
        self,
        request: main_models.SetAppsAuthoritiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppsAuthoritiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppsAuthorities',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppsAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_apps_authorities(
        self,
        request: main_models.SetAppsAuthoritiesRequest,
    ) -> main_models.SetAppsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return self.set_apps_authorities_with_options(request, runtime)

    async def set_apps_authorities_async(
        self,
        request: main_models.SetAppsAuthoritiesRequest,
    ) -> main_models.SetAppsAuthoritiesResponse:
        runtime = RuntimeOptions()
        return await self.set_apps_authorities_with_options_async(request, runtime)

    def set_domain_with_options(
        self,
        request: main_models.SetDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_stage_name):
            query['BindStageName'] = request.bind_stage_name
        if not DaraCore.is_null(request.custom_domain_type):
            query['CustomDomainType'] = request.custom_domain_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_force):
            query['IsForce'] = request.is_force
        if not DaraCore.is_null(request.is_http_redirect_to_https):
            query['IsHttpRedirectToHttps'] = request.is_http_redirect_to_https
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_with_options_async(
        self,
        request: main_models.SetDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_stage_name):
            query['BindStageName'] = request.bind_stage_name
        if not DaraCore.is_null(request.custom_domain_type):
            query['CustomDomainType'] = request.custom_domain_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_force):
            query['IsForce'] = request.is_force
        if not DaraCore.is_null(request.is_http_redirect_to_https):
            query['IsHttpRedirectToHttps'] = request.is_http_redirect_to_https
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomain',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain(
        self,
        request: main_models.SetDomainRequest,
    ) -> main_models.SetDomainResponse:
        runtime = RuntimeOptions()
        return self.set_domain_with_options(request, runtime)

    async def set_domain_async(
        self,
        request: main_models.SetDomainRequest,
    ) -> main_models.SetDomainResponse:
        runtime = RuntimeOptions()
        return await self.set_domain_with_options_async(request, runtime)

    def set_domain_certificate_with_options(
        self,
        request: main_models.SetDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_certificate_body):
            query['CaCertificateBody'] = request.ca_certificate_body
        if not DaraCore.is_null(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not DaraCore.is_null(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not DaraCore.is_null(request.certificate_private_key):
            query['CertificatePrivateKey'] = request.certificate_private_key
        if not DaraCore.is_null(request.client_cert_sdn_pass_through):
            query['ClientCertSDnPassThrough'] = request.client_cert_sdn_pass_through
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.ssl_ocsp_cache_enable):
            query['SslOcspCacheEnable'] = request.ssl_ocsp_cache_enable
        if not DaraCore.is_null(request.ssl_ocsp_enable):
            query['SslOcspEnable'] = request.ssl_ocsp_enable
        if not DaraCore.is_null(request.ssl_verify_depth):
            query['SslVerifyDepth'] = request.ssl_verify_depth
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainCertificate',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_certificate_with_options_async(
        self,
        request: main_models.SetDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_certificate_body):
            query['CaCertificateBody'] = request.ca_certificate_body
        if not DaraCore.is_null(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not DaraCore.is_null(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not DaraCore.is_null(request.certificate_private_key):
            query['CertificatePrivateKey'] = request.certificate_private_key
        if not DaraCore.is_null(request.client_cert_sdn_pass_through):
            query['ClientCertSDnPassThrough'] = request.client_cert_sdn_pass_through
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.ssl_ocsp_cache_enable):
            query['SslOcspCacheEnable'] = request.ssl_ocsp_cache_enable
        if not DaraCore.is_null(request.ssl_ocsp_enable):
            query['SslOcspEnable'] = request.ssl_ocsp_enable
        if not DaraCore.is_null(request.ssl_verify_depth):
            query['SslVerifyDepth'] = request.ssl_verify_depth
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainCertificate',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_certificate(
        self,
        request: main_models.SetDomainCertificateRequest,
    ) -> main_models.SetDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    async def set_domain_certificate_async(
        self,
        request: main_models.SetDomainCertificateRequest,
    ) -> main_models.SetDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_domain_certificate_with_options_async(request, runtime)

    def set_domain_web_socket_status_with_options(
        self,
        request: main_models.SetDomainWebSocketStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainWebSocketStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_value):
            query['ActionValue'] = request.action_value
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.wssenable):
            query['WSSEnable'] = request.wssenable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainWebSocketStatus',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainWebSocketStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_web_socket_status_with_options_async(
        self,
        request: main_models.SetDomainWebSocketStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainWebSocketStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_value):
            query['ActionValue'] = request.action_value
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.wssenable):
            query['WSSEnable'] = request.wssenable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainWebSocketStatus',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainWebSocketStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_web_socket_status(
        self,
        request: main_models.SetDomainWebSocketStatusRequest,
    ) -> main_models.SetDomainWebSocketStatusResponse:
        runtime = RuntimeOptions()
        return self.set_domain_web_socket_status_with_options(request, runtime)

    async def set_domain_web_socket_status_async(
        self,
        request: main_models.SetDomainWebSocketStatusRequest,
    ) -> main_models.SetDomainWebSocketStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_domain_web_socket_status_with_options_async(request, runtime)

    def set_group_auth_app_code_with_options(
        self,
        request: main_models.SetGroupAuthAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGroupAuthAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_app_code):
            query['AuthAppCode'] = request.auth_app_code
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGroupAuthAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGroupAuthAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_group_auth_app_code_with_options_async(
        self,
        request: main_models.SetGroupAuthAppCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetGroupAuthAppCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_app_code):
            query['AuthAppCode'] = request.auth_app_code
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetGroupAuthAppCode',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetGroupAuthAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_group_auth_app_code(
        self,
        request: main_models.SetGroupAuthAppCodeRequest,
    ) -> main_models.SetGroupAuthAppCodeResponse:
        runtime = RuntimeOptions()
        return self.set_group_auth_app_code_with_options(request, runtime)

    async def set_group_auth_app_code_async(
        self,
        request: main_models.SetGroupAuthAppCodeRequest,
    ) -> main_models.SetGroupAuthAppCodeResponse:
        runtime = RuntimeOptions()
        return await self.set_group_auth_app_code_with_options_async(request, runtime)

    def set_ip_control_apis_with_options(
        self,
        request: main_models.SetIpControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIpControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIpControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ip_control_apis_with_options_async(
        self,
        request: main_models.SetIpControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIpControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIpControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIpControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ip_control_apis(
        self,
        request: main_models.SetIpControlApisRequest,
    ) -> main_models.SetIpControlApisResponse:
        runtime = RuntimeOptions()
        return self.set_ip_control_apis_with_options(request, runtime)

    async def set_ip_control_apis_async(
        self,
        request: main_models.SetIpControlApisRequest,
    ) -> main_models.SetIpControlApisResponse:
        runtime = RuntimeOptions()
        return await self.set_ip_control_apis_with_options_async(request, runtime)

    def set_signature_apis_with_options(
        self,
        request: main_models.SetSignatureApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSignatureApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSignatureApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_signature_apis_with_options_async(
        self,
        request: main_models.SetSignatureApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSignatureApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSignatureApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSignatureApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_signature_apis(
        self,
        request: main_models.SetSignatureApisRequest,
    ) -> main_models.SetSignatureApisResponse:
        runtime = RuntimeOptions()
        return self.set_signature_apis_with_options(request, runtime)

    async def set_signature_apis_async(
        self,
        request: main_models.SetSignatureApisRequest,
    ) -> main_models.SetSignatureApisResponse:
        runtime = RuntimeOptions()
        return await self.set_signature_apis_with_options_async(request, runtime)

    def set_traffic_control_apis_with_options(
        self,
        request: main_models.SetTrafficControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTrafficControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTrafficControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_traffic_control_apis_with_options_async(
        self,
        request: main_models.SetTrafficControlApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTrafficControlApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        if not DaraCore.is_null(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTrafficControlApis',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTrafficControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_traffic_control_apis(
        self,
        request: main_models.SetTrafficControlApisRequest,
    ) -> main_models.SetTrafficControlApisResponse:
        runtime = RuntimeOptions()
        return self.set_traffic_control_apis_with_options(request, runtime)

    async def set_traffic_control_apis_async(
        self,
        request: main_models.SetTrafficControlApisRequest,
    ) -> main_models.SetTrafficControlApisResponse:
        runtime = RuntimeOptions()
        return await self.set_traffic_control_apis_with_options_async(request, runtime)

    def set_vpc_access_with_options(
        self,
        request: main_models.SetVpcAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVpcAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_target_host_name):
            query['VpcTargetHostName'] = request.vpc_target_host_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVpcAccess',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vpc_access_with_options_async(
        self,
        request: main_models.SetVpcAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVpcAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_target_host_name):
            query['VpcTargetHostName'] = request.vpc_target_host_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVpcAccess',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVpcAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vpc_access(
        self,
        request: main_models.SetVpcAccessRequest,
    ) -> main_models.SetVpcAccessResponse:
        runtime = RuntimeOptions()
        return self.set_vpc_access_with_options(request, runtime)

    async def set_vpc_access_async(
        self,
        request: main_models.SetVpcAccessRequest,
    ) -> main_models.SetVpcAccessResponse:
        runtime = RuntimeOptions()
        return await self.set_vpc_access_with_options_async(request, runtime)

    def set_wildcard_domain_patterns_with_options(
        self,
        request: main_models.SetWildcardDomainPatternsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWildcardDomainPatternsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.wildcard_domain_patterns):
            query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWildcardDomainPatterns',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWildcardDomainPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_wildcard_domain_patterns_with_options_async(
        self,
        request: main_models.SetWildcardDomainPatternsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWildcardDomainPatternsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.wildcard_domain_patterns):
            query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWildcardDomainPatterns',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWildcardDomainPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_wildcard_domain_patterns(
        self,
        request: main_models.SetWildcardDomainPatternsRequest,
    ) -> main_models.SetWildcardDomainPatternsResponse:
        runtime = RuntimeOptions()
        return self.set_wildcard_domain_patterns_with_options(request, runtime)

    async def set_wildcard_domain_patterns_async(
        self,
        request: main_models.SetWildcardDomainPatternsRequest,
    ) -> main_models.SetWildcardDomainPatternsResponse:
        runtime = RuntimeOptions()
        return await self.set_wildcard_domain_patterns_with_options_async(request, runtime)

    def switch_api_with_options(
        self,
        request: main_models.SwitchApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_api_with_options_async(
        self,
        request: main_models.SwitchApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchApi',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_api(
        self,
        request: main_models.SwitchApiRequest,
    ) -> main_models.SwitchApiResponse:
        runtime = RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    async def switch_api_async(
        self,
        request: main_models.SwitchApiRequest,
    ) -> main_models.SwitchApiResponse:
        runtime = RuntimeOptions()
        return await self.switch_api_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2016-07-14',
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
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2016-07-14',
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
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2016-07-14',
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
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2016-07-14',
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

    def update_private_dnswith_options(
        self,
        tmp_req: main_models.UpdatePrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateDNSResponse:
        tmp_req.validate()
        request = main_models.UpdatePrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.records):
            request.records_shrink = Utils.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.records_shrink):
            body['Records'] = request.records_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateDNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_dnswith_options_async(
        self,
        tmp_req: main_models.UpdatePrivateDNSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateDNSResponse:
        tmp_req.validate()
        request = main_models.UpdatePrivateDNSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.records):
            request.records_shrink = Utils.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not DaraCore.is_null(request.intranet_domain):
            query['IntranetDomain'] = request.intranet_domain
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.records_shrink):
            body['Records'] = request.records_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateDNS',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateDNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_dns(
        self,
        request: main_models.UpdatePrivateDNSRequest,
    ) -> main_models.UpdatePrivateDNSResponse:
        runtime = RuntimeOptions()
        return self.update_private_dnswith_options(request, runtime)

    async def update_private_dns_async(
        self,
        request: main_models.UpdatePrivateDNSRequest,
    ) -> main_models.UpdatePrivateDNSResponse:
        runtime = RuntimeOptions()
        return await self.update_private_dnswith_options_async(request, runtime)

    def validate_vpc_connectivity_with_options(
        self,
        request: main_models.ValidateVpcConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateVpcConnectivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_access_id):
            query['VpcAccessId'] = request.vpc_access_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateVpcConnectivity',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateVpcConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_vpc_connectivity_with_options_async(
        self,
        request: main_models.ValidateVpcConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateVpcConnectivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_access_id):
            query['VpcAccessId'] = request.vpc_access_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateVpcConnectivity',
            version = '2016-07-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateVpcConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_vpc_connectivity(
        self,
        request: main_models.ValidateVpcConnectivityRequest,
    ) -> main_models.ValidateVpcConnectivityResponse:
        runtime = RuntimeOptions()
        return self.validate_vpc_connectivity_with_options(request, runtime)

    async def validate_vpc_connectivity_async(
        self,
        request: main_models.ValidateVpcConnectivityRequest,
    ) -> main_models.ValidateVpcConnectivityResponse:
        runtime = RuntimeOptions()
        return await self.validate_vpc_connectivity_with_options_async(request, runtime)
