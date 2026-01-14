# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_mse20190531 import models as main_models
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
        self._endpoint = self.get_endpoint('mse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_auth_policy_with_options(
        self,
        request: main_models.AddAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_rule):
            query['AuthRule'] = request.auth_rule
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.k_8s_namespace):
            query['K8sNamespace'] = request.k_8s_namespace
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuthPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_auth_policy_with_options_async(
        self,
        request: main_models.AddAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_rule):
            query['AuthRule'] = request.auth_rule
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.k_8s_namespace):
            query['K8sNamespace'] = request.k_8s_namespace
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuthPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_auth_policy(
        self,
        request: main_models.AddAuthPolicyRequest,
    ) -> main_models.AddAuthPolicyResponse:
        runtime = RuntimeOptions()
        return self.add_auth_policy_with_options(request, runtime)

    async def add_auth_policy_async(
        self,
        request: main_models.AddAuthPolicyRequest,
    ) -> main_models.AddAuthPolicyResponse:
        runtime = RuntimeOptions()
        return await self.add_auth_policy_with_options_async(request, runtime)

    def add_auth_resource_with_options(
        self,
        tmp_req: main_models.AddAuthResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuthResourceResponse:
        tmp_req.validate()
        request = main_models.AddAuthResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_resource_header_list):
            request.auth_resource_header_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_resource_header_list, 'AuthResourceHeaderList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_id):
            query['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.auth_resource_header_list_shrink):
            query['AuthResourceHeaderList'] = request.auth_resource_header_list_shrink
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.ignore_case):
            query['IgnoreCase'] = request.ignore_case
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAuthResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuthResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_auth_resource_with_options_async(
        self,
        tmp_req: main_models.AddAuthResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuthResourceResponse:
        tmp_req.validate()
        request = main_models.AddAuthResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_resource_header_list):
            request.auth_resource_header_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_resource_header_list, 'AuthResourceHeaderList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_id):
            query['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.auth_resource_header_list_shrink):
            query['AuthResourceHeaderList'] = request.auth_resource_header_list_shrink
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.ignore_case):
            query['IgnoreCase'] = request.ignore_case
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAuthResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuthResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_auth_resource(
        self,
        request: main_models.AddAuthResourceRequest,
    ) -> main_models.AddAuthResourceResponse:
        runtime = RuntimeOptions()
        return self.add_auth_resource_with_options(request, runtime)

    async def add_auth_resource_async(
        self,
        request: main_models.AddAuthResourceRequest,
    ) -> main_models.AddAuthResourceResponse:
        runtime = RuntimeOptions()
        return await self.add_auth_resource_with_options_async(request, runtime)

    def add_black_white_list_with_options(
        self,
        request: main_models.AddBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.resource_id_json_list):
            query['ResourceIdJsonList'] = request.resource_id_json_list
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_black_white_list_with_options_async(
        self,
        request: main_models.AddBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.resource_id_json_list):
            query['ResourceIdJsonList'] = request.resource_id_json_list
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBlackWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_black_white_list(
        self,
        request: main_models.AddBlackWhiteListRequest,
    ) -> main_models.AddBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return self.add_black_white_list_with_options(request, runtime)

    async def add_black_white_list_async(
        self,
        request: main_models.AddBlackWhiteListRequest,
    ) -> main_models.AddBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.add_black_white_list_with_options_async(request, runtime)

    def add_gateway_with_options(
        self,
        tmp_req: main_models.AddGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayResponse:
        tmp_req.validate()
        request = main_models.AddGatewayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.zone_info):
            request.zone_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.zone_info, 'ZoneInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.clb_network_type):
            query['ClbNetworkType'] = request.clb_network_type
        if not DaraCore.is_null(request.enable_hardware_acceleration):
            query['EnableHardwareAcceleration'] = request.enable_hardware_acceleration
        if not DaraCore.is_null(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not DaraCore.is_null(request.enable_xtrace):
            query['EnableXtrace'] = request.enable_xtrace
        if not DaraCore.is_null(request.enterprise_security_group):
            query['EnterpriseSecurityGroup'] = request.enterprise_security_group
        if not DaraCore.is_null(request.internet_slb_spec):
            query['InternetSlbSpec'] = request.internet_slb_spec
        if not DaraCore.is_null(request.managed_entry_network_type):
            query['ManagedEntryNetworkType'] = request.managed_entry_network_type
        if not DaraCore.is_null(request.mser_version):
            query['MserVersion'] = request.mser_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nlb_network_type):
            query['NlbNetworkType'] = request.nlb_network_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.replica):
            query['Replica'] = request.replica
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slb_spec):
            query['SlbSpec'] = request.slb_spec
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_id_2):
            query['VSwitchId2'] = request.v_switch_id_2
        if not DaraCore.is_null(request.vpc):
            query['Vpc'] = request.vpc
        if not DaraCore.is_null(request.xtrace_ratio):
            query['XtraceRatio'] = request.xtrace_ratio
        if not DaraCore.is_null(request.zone_info_shrink):
            query['ZoneInfo'] = request.zone_info_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_with_options_async(
        self,
        tmp_req: main_models.AddGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayResponse:
        tmp_req.validate()
        request = main_models.AddGatewayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.zone_info):
            request.zone_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.zone_info, 'ZoneInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.clb_network_type):
            query['ClbNetworkType'] = request.clb_network_type
        if not DaraCore.is_null(request.enable_hardware_acceleration):
            query['EnableHardwareAcceleration'] = request.enable_hardware_acceleration
        if not DaraCore.is_null(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not DaraCore.is_null(request.enable_xtrace):
            query['EnableXtrace'] = request.enable_xtrace
        if not DaraCore.is_null(request.enterprise_security_group):
            query['EnterpriseSecurityGroup'] = request.enterprise_security_group
        if not DaraCore.is_null(request.internet_slb_spec):
            query['InternetSlbSpec'] = request.internet_slb_spec
        if not DaraCore.is_null(request.managed_entry_network_type):
            query['ManagedEntryNetworkType'] = request.managed_entry_network_type
        if not DaraCore.is_null(request.mser_version):
            query['MserVersion'] = request.mser_version
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nlb_network_type):
            query['NlbNetworkType'] = request.nlb_network_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.replica):
            query['Replica'] = request.replica
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.slb_spec):
            query['SlbSpec'] = request.slb_spec
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_id_2):
            query['VSwitchId2'] = request.v_switch_id_2
        if not DaraCore.is_null(request.vpc):
            query['Vpc'] = request.vpc
        if not DaraCore.is_null(request.xtrace_ratio):
            query['XtraceRatio'] = request.xtrace_ratio
        if not DaraCore.is_null(request.zone_info_shrink):
            query['ZoneInfo'] = request.zone_info_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway(
        self,
        request: main_models.AddGatewayRequest,
    ) -> main_models.AddGatewayResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_with_options(request, runtime)

    async def add_gateway_async(
        self,
        request: main_models.AddGatewayRequest,
    ) -> main_models.AddGatewayResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_with_options_async(request, runtime)

    def add_gateway_auth_with_options(
        self,
        tmp_req: main_models.AddGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayAuthResponse:
        tmp_req.validate()
        request = main_models.AddGatewayAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_resource_list):
            request.auth_resource_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_resource_list, 'AuthResourceList', 'json')
        if not DaraCore.is_null(tmp_req.external_auth_zjson):
            request.external_auth_zjsonshrink = Utils.array_to_string_with_specified_style(tmp_req.external_auth_zjson, 'ExternalAuthZJSON', 'json')
        if not DaraCore.is_null(tmp_req.scopes_list):
            request.scopes_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scopes_list, 'ScopesList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_resource_config):
            query['AuthResourceConfig'] = request.auth_resource_config
        if not DaraCore.is_null(request.auth_resource_list_shrink):
            query['AuthResourceList'] = request.auth_resource_list_shrink
        if not DaraCore.is_null(request.auth_resource_mode):
            query['AuthResourceMode'] = request.auth_resource_mode
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['ClientSecret'] = request.client_secret
        if not DaraCore.is_null(request.cookie_domain):
            query['CookieDomain'] = request.cookie_domain
        if not DaraCore.is_null(request.external_auth_zjsonshrink):
            query['ExternalAuthZJSON'] = request.external_auth_zjsonshrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.issuer):
            query['Issuer'] = request.issuer
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.login_url):
            query['LoginUrl'] = request.login_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.redirect_url):
            query['RedirectUrl'] = request.redirect_url
        if not DaraCore.is_null(request.scopes_list_shrink):
            query['ScopesList'] = request.scopes_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub):
            query['Sub'] = request.sub
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_name_prefix):
            query['TokenNamePrefix'] = request.token_name_prefix
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_auth_with_options_async(
        self,
        tmp_req: main_models.AddGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayAuthResponse:
        tmp_req.validate()
        request = main_models.AddGatewayAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_resource_list):
            request.auth_resource_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_resource_list, 'AuthResourceList', 'json')
        if not DaraCore.is_null(tmp_req.external_auth_zjson):
            request.external_auth_zjsonshrink = Utils.array_to_string_with_specified_style(tmp_req.external_auth_zjson, 'ExternalAuthZJSON', 'json')
        if not DaraCore.is_null(tmp_req.scopes_list):
            request.scopes_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scopes_list, 'ScopesList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_resource_config):
            query['AuthResourceConfig'] = request.auth_resource_config
        if not DaraCore.is_null(request.auth_resource_list_shrink):
            query['AuthResourceList'] = request.auth_resource_list_shrink
        if not DaraCore.is_null(request.auth_resource_mode):
            query['AuthResourceMode'] = request.auth_resource_mode
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['ClientSecret'] = request.client_secret
        if not DaraCore.is_null(request.cookie_domain):
            query['CookieDomain'] = request.cookie_domain
        if not DaraCore.is_null(request.external_auth_zjsonshrink):
            query['ExternalAuthZJSON'] = request.external_auth_zjsonshrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.issuer):
            query['Issuer'] = request.issuer
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.login_url):
            query['LoginUrl'] = request.login_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.redirect_url):
            query['RedirectUrl'] = request.redirect_url
        if not DaraCore.is_null(request.scopes_list_shrink):
            query['ScopesList'] = request.scopes_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub):
            query['Sub'] = request.sub
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_name_prefix):
            query['TokenNamePrefix'] = request.token_name_prefix
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_auth(
        self,
        request: main_models.AddGatewayAuthRequest,
    ) -> main_models.AddGatewayAuthResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_auth_with_options(request, runtime)

    async def add_gateway_auth_async(
        self,
        request: main_models.AddGatewayAuthRequest,
    ) -> main_models.AddGatewayAuthResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_auth_with_options_async(request, runtime)

    def add_gateway_auth_consumer_with_options(
        self,
        request: main_models.AddGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.key_value):
            query['KeyValue'] = request.key_value
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.token_prefix):
            query['TokenPrefix'] = request.token_prefix
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayAuthConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_auth_consumer_with_options_async(
        self,
        request: main_models.AddGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.key_value):
            query['KeyValue'] = request.key_value
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.token_prefix):
            query['TokenPrefix'] = request.token_prefix
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayAuthConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_auth_consumer(
        self,
        request: main_models.AddGatewayAuthConsumerRequest,
    ) -> main_models.AddGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_auth_consumer_with_options(request, runtime)

    async def add_gateway_auth_consumer_async(
        self,
        request: main_models.AddGatewayAuthConsumerRequest,
    ) -> main_models.AddGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_auth_consumer_with_options_async(request, runtime)

    def add_gateway_domain_with_options(
        self,
        tmp_req: main_models.AddGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.AddGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tls_cipher_suites_config_json):
            request.tls_cipher_suites_config_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.tls_cipher_suites_config_json, 'TlsCipherSuitesConfigJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_2):
            query['Http2'] = request.http_2
        if not DaraCore.is_null(request.must_https):
            query['MustHttps'] = request.must_https
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config_jsonshrink):
            query['TlsCipherSuitesConfigJSON'] = request.tls_cipher_suites_config_jsonshrink
        if not DaraCore.is_null(request.tls_max):
            query['TlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            query['TlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_domain_with_options_async(
        self,
        tmp_req: main_models.AddGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.AddGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tls_cipher_suites_config_json):
            request.tls_cipher_suites_config_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.tls_cipher_suites_config_json, 'TlsCipherSuitesConfigJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_2):
            query['Http2'] = request.http_2
        if not DaraCore.is_null(request.must_https):
            query['MustHttps'] = request.must_https
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config_jsonshrink):
            query['TlsCipherSuitesConfigJSON'] = request.tls_cipher_suites_config_jsonshrink
        if not DaraCore.is_null(request.tls_max):
            query['TlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            query['TlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_domain(
        self,
        request: main_models.AddGatewayDomainRequest,
    ) -> main_models.AddGatewayDomainResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_domain_with_options(request, runtime)

    async def add_gateway_domain_async(
        self,
        request: main_models.AddGatewayDomainRequest,
    ) -> main_models.AddGatewayDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_domain_with_options_async(request, runtime)

    def add_gateway_route_with_options(
        self,
        tmp_req: main_models.AddGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayRouteResponse:
        tmp_req.validate()
        request = main_models.AddGatewayRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.direct_response_json):
            request.direct_response_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.direct_response_json, 'DirectResponseJSON', 'json')
        if not DaraCore.is_null(tmp_req.fallback_services):
            request.fallback_services_shrink = Utils.array_to_string_with_specified_style(tmp_req.fallback_services, 'FallbackServices', 'json')
        if not DaraCore.is_null(tmp_req.predicates):
            request.predicates_shrink = Utils.array_to_string_with_specified_style(tmp_req.predicates, 'Predicates', 'json')
        if not DaraCore.is_null(tmp_req.redirect_json):
            request.redirect_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_json, 'RedirectJSON', 'json')
        if not DaraCore.is_null(tmp_req.services):
            request.services_shrink = Utils.array_to_string_with_specified_style(tmp_req.services, 'Services', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direct_response_jsonshrink):
            query['DirectResponseJSON'] = request.direct_response_jsonshrink
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_id_list_json):
            query['DomainIdListJSON'] = request.domain_id_list_json
        if not DaraCore.is_null(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not DaraCore.is_null(request.fallback):
            query['Fallback'] = request.fallback
        if not DaraCore.is_null(request.fallback_services_shrink):
            query['FallbackServices'] = request.fallback_services_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policies):
            query['Policies'] = request.policies
        if not DaraCore.is_null(request.predicates_shrink):
            query['Predicates'] = request.predicates_shrink
        if not DaraCore.is_null(request.redirect_jsonshrink):
            query['RedirectJSON'] = request.redirect_jsonshrink
        if not DaraCore.is_null(request.route_order):
            query['RouteOrder'] = request.route_order
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        if not DaraCore.is_null(request.services_shrink):
            query['Services'] = request.services_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_route_with_options_async(
        self,
        tmp_req: main_models.AddGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayRouteResponse:
        tmp_req.validate()
        request = main_models.AddGatewayRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.direct_response_json):
            request.direct_response_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.direct_response_json, 'DirectResponseJSON', 'json')
        if not DaraCore.is_null(tmp_req.fallback_services):
            request.fallback_services_shrink = Utils.array_to_string_with_specified_style(tmp_req.fallback_services, 'FallbackServices', 'json')
        if not DaraCore.is_null(tmp_req.predicates):
            request.predicates_shrink = Utils.array_to_string_with_specified_style(tmp_req.predicates, 'Predicates', 'json')
        if not DaraCore.is_null(tmp_req.redirect_json):
            request.redirect_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_json, 'RedirectJSON', 'json')
        if not DaraCore.is_null(tmp_req.services):
            request.services_shrink = Utils.array_to_string_with_specified_style(tmp_req.services, 'Services', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direct_response_jsonshrink):
            query['DirectResponseJSON'] = request.direct_response_jsonshrink
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_id_list_json):
            query['DomainIdListJSON'] = request.domain_id_list_json
        if not DaraCore.is_null(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not DaraCore.is_null(request.fallback):
            query['Fallback'] = request.fallback
        if not DaraCore.is_null(request.fallback_services_shrink):
            query['FallbackServices'] = request.fallback_services_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policies):
            query['Policies'] = request.policies
        if not DaraCore.is_null(request.predicates_shrink):
            query['Predicates'] = request.predicates_shrink
        if not DaraCore.is_null(request.redirect_jsonshrink):
            query['RedirectJSON'] = request.redirect_jsonshrink
        if not DaraCore.is_null(request.route_order):
            query['RouteOrder'] = request.route_order
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        if not DaraCore.is_null(request.services_shrink):
            query['Services'] = request.services_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_route(
        self,
        request: main_models.AddGatewayRouteRequest,
    ) -> main_models.AddGatewayRouteResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_route_with_options(request, runtime)

    async def add_gateway_route_async(
        self,
        request: main_models.AddGatewayRouteRequest,
    ) -> main_models.AddGatewayRouteResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_route_with_options_async(request, runtime)

    def add_gateway_service_version_with_options(
        self,
        request: main_models.AddGatewayServiceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayServiceVersion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_service_version_with_options_async(
        self,
        request: main_models.AddGatewayServiceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayServiceVersion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_service_version(
        self,
        request: main_models.AddGatewayServiceVersionRequest,
    ) -> main_models.AddGatewayServiceVersionResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_service_version_with_options(request, runtime)

    async def add_gateway_service_version_async(
        self,
        request: main_models.AddGatewayServiceVersionRequest,
    ) -> main_models.AddGatewayServiceVersionResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_service_version_with_options_async(request, runtime)

    def add_gateway_slb_with_options(
        self,
        tmp_req: main_models.AddGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewaySlbResponse:
        tmp_req.validate()
        request = main_models.AddGatewaySlbShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vservice_list):
            request.vservice_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.vservice_list, 'VServiceList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_port):
            query['HttpPort'] = request.http_port
        if not DaraCore.is_null(request.https_port):
            query['HttpsPort'] = request.https_port
        if not DaraCore.is_null(request.https_vserver_group_id):
            query['HttpsVServerGroupId'] = request.https_vserver_group_id
        if not DaraCore.is_null(request.service_weight):
            query['ServiceWeight'] = request.service_weight
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.vservice_list_shrink):
            query['VServiceList'] = request.vservice_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_slb_with_options_async(
        self,
        tmp_req: main_models.AddGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewaySlbResponse:
        tmp_req.validate()
        request = main_models.AddGatewaySlbShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vservice_list):
            request.vservice_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.vservice_list, 'VServiceList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_port):
            query['HttpPort'] = request.http_port
        if not DaraCore.is_null(request.https_port):
            query['HttpsPort'] = request.https_port
        if not DaraCore.is_null(request.https_vserver_group_id):
            query['HttpsVServerGroupId'] = request.https_vserver_group_id
        if not DaraCore.is_null(request.service_weight):
            query['ServiceWeight'] = request.service_weight
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.vservice_list_shrink):
            query['VServiceList'] = request.vservice_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewaySlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_slb(
        self,
        request: main_models.AddGatewaySlbRequest,
    ) -> main_models.AddGatewaySlbResponse:
        runtime = RuntimeOptions()
        return self.add_gateway_slb_with_options(request, runtime)

    async def add_gateway_slb_async(
        self,
        request: main_models.AddGatewaySlbRequest,
    ) -> main_models.AddGatewaySlbResponse:
        runtime = RuntimeOptions()
        return await self.add_gateway_slb_with_options_async(request, runtime)

    def add_migration_task_with_options(
        self,
        request: main_models.AddMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.origin_instance_address):
            query['OriginInstanceAddress'] = request.origin_instance_address
        if not DaraCore.is_null(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not DaraCore.is_null(request.origin_instance_namespace):
            query['OriginInstanceNamespace'] = request.origin_instance_namespace
        if not DaraCore.is_null(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.sync_type):
            query['SyncType'] = request.sync_type
        if not DaraCore.is_null(request.target_cluster_name):
            query['TargetClusterName'] = request.target_cluster_name
        if not DaraCore.is_null(request.target_cluster_url):
            query['TargetClusterUrl'] = request.target_cluster_url
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_migration_task_with_options_async(
        self,
        request: main_models.AddMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.origin_instance_address):
            query['OriginInstanceAddress'] = request.origin_instance_address
        if not DaraCore.is_null(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not DaraCore.is_null(request.origin_instance_namespace):
            query['OriginInstanceNamespace'] = request.origin_instance_namespace
        if not DaraCore.is_null(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.sync_type):
            query['SyncType'] = request.sync_type
        if not DaraCore.is_null(request.target_cluster_name):
            query['TargetClusterName'] = request.target_cluster_name
        if not DaraCore.is_null(request.target_cluster_url):
            query['TargetClusterUrl'] = request.target_cluster_url
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_migration_task(
        self,
        request: main_models.AddMigrationTaskRequest,
    ) -> main_models.AddMigrationTaskResponse:
        runtime = RuntimeOptions()
        return self.add_migration_task_with_options(request, runtime)

    async def add_migration_task_async(
        self,
        request: main_models.AddMigrationTaskRequest,
    ) -> main_models.AddMigrationTaskResponse:
        runtime = RuntimeOptions()
        return await self.add_migration_task_with_options_async(request, runtime)

    def add_mock_rule_with_options(
        self,
        request: main_models.AddMockRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMockRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_app_ids):
            query['ConsumerAppIds'] = request.consumer_app_ids
        if not DaraCore.is_null(request.dubbo_mock_items):
            query['DubboMockItems'] = request.dubbo_mock_items
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.extra_json):
            query['ExtraJson'] = request.extra_json
        if not DaraCore.is_null(request.mock_type):
            query['MockType'] = request.mock_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.provider_app_id):
            query['ProviderAppId'] = request.provider_app_id
        if not DaraCore.is_null(request.provider_app_name):
            query['ProviderAppName'] = request.provider_app_name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sc_mock_items):
            query['ScMockItems'] = request.sc_mock_items
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMockRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMockRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mock_rule_with_options_async(
        self,
        request: main_models.AddMockRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMockRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_app_ids):
            query['ConsumerAppIds'] = request.consumer_app_ids
        if not DaraCore.is_null(request.dubbo_mock_items):
            query['DubboMockItems'] = request.dubbo_mock_items
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.extra_json):
            query['ExtraJson'] = request.extra_json
        if not DaraCore.is_null(request.mock_type):
            query['MockType'] = request.mock_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.provider_app_id):
            query['ProviderAppId'] = request.provider_app_id
        if not DaraCore.is_null(request.provider_app_name):
            query['ProviderAppName'] = request.provider_app_name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sc_mock_items):
            query['ScMockItems'] = request.sc_mock_items
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMockRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMockRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mock_rule(
        self,
        request: main_models.AddMockRuleRequest,
    ) -> main_models.AddMockRuleResponse:
        runtime = RuntimeOptions()
        return self.add_mock_rule_with_options(request, runtime)

    async def add_mock_rule_async(
        self,
        request: main_models.AddMockRuleRequest,
    ) -> main_models.AddMockRuleResponse:
        runtime = RuntimeOptions()
        return await self.add_mock_rule_with_options_async(request, runtime)

    def add_sslcert_with_options(
        self,
        request: main_models.AddSSLCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSSLCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSSLCert',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSSLCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sslcert_with_options_async(
        self,
        request: main_models.AddSSLCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSSLCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSSLCert',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSSLCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sslcert(
        self,
        request: main_models.AddSSLCertRequest,
    ) -> main_models.AddSSLCertResponse:
        runtime = RuntimeOptions()
        return self.add_sslcert_with_options(request, runtime)

    async def add_sslcert_async(
        self,
        request: main_models.AddSSLCertRequest,
    ) -> main_models.AddSSLCertResponse:
        runtime = RuntimeOptions()
        return await self.add_sslcert_with_options_async(request, runtime)

    def add_security_group_rule_with_options(
        self,
        request: main_models.AddSecurityGroupRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.port_range):
            query['PortRange'] = request.port_range
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSecurityGroupRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_security_group_rule_with_options_async(
        self,
        request: main_models.AddSecurityGroupRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.port_range):
            query['PortRange'] = request.port_range
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSecurityGroupRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_security_group_rule(
        self,
        request: main_models.AddSecurityGroupRuleRequest,
    ) -> main_models.AddSecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        return self.add_security_group_rule_with_options(request, runtime)

    async def add_security_group_rule_async(
        self,
        request: main_models.AddSecurityGroupRuleRequest,
    ) -> main_models.AddSecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        return await self.add_security_group_rule_with_options_async(request, runtime)

    def add_service_source_with_options(
        self,
        tmp_req: main_models.AddServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServiceSourceResponse:
        tmp_req.validate()
        request = main_models.AddServiceSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_list):
            request.group_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_list, 'GroupList', 'json')
        if not DaraCore.is_null(tmp_req.ingress_options_request):
            request.ingress_options_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.ingress_options_request, 'IngressOptionsRequest', 'json')
        if not DaraCore.is_null(tmp_req.path_list):
            request.path_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.path_list, 'PathList', 'json')
        if not DaraCore.is_null(tmp_req.to_authorize_security_groups):
            request.to_authorize_security_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.to_authorize_security_groups, 'ToAuthorizeSecurityGroups', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.group_list_shrink):
            query['GroupList'] = request.group_list_shrink
        if not DaraCore.is_null(request.ingress_options_request_shrink):
            query['IngressOptionsRequest'] = request.ingress_options_request_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.path_list_shrink):
            query['PathList'] = request.path_list_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.to_authorize_security_groups_shrink):
            query['ToAuthorizeSecurityGroups'] = request.to_authorize_security_groups_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_service_source_with_options_async(
        self,
        tmp_req: main_models.AddServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServiceSourceResponse:
        tmp_req.validate()
        request = main_models.AddServiceSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_list):
            request.group_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_list, 'GroupList', 'json')
        if not DaraCore.is_null(tmp_req.ingress_options_request):
            request.ingress_options_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.ingress_options_request, 'IngressOptionsRequest', 'json')
        if not DaraCore.is_null(tmp_req.path_list):
            request.path_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.path_list, 'PathList', 'json')
        if not DaraCore.is_null(tmp_req.to_authorize_security_groups):
            request.to_authorize_security_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.to_authorize_security_groups, 'ToAuthorizeSecurityGroups', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.group_list_shrink):
            query['GroupList'] = request.group_list_shrink
        if not DaraCore.is_null(request.ingress_options_request_shrink):
            query['IngressOptionsRequest'] = request.ingress_options_request_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.path_list_shrink):
            query['PathList'] = request.path_list_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.to_authorize_security_groups_shrink):
            query['ToAuthorizeSecurityGroups'] = request.to_authorize_security_groups_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_service_source(
        self,
        request: main_models.AddServiceSourceRequest,
    ) -> main_models.AddServiceSourceResponse:
        runtime = RuntimeOptions()
        return self.add_service_source_with_options(request, runtime)

    async def add_service_source_async(
        self,
        request: main_models.AddServiceSourceRequest,
    ) -> main_models.AddServiceSourceResponse:
        runtime = RuntimeOptions()
        return await self.add_service_source_with_options_async(request, runtime)

    def apply_gateway_route_with_options(
        self,
        request: main_models.ApplyGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyGatewayRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_gateway_route_with_options_async(
        self,
        request: main_models.ApplyGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyGatewayRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_gateway_route(
        self,
        request: main_models.ApplyGatewayRouteRequest,
    ) -> main_models.ApplyGatewayRouteResponse:
        runtime = RuntimeOptions()
        return self.apply_gateway_route_with_options(request, runtime)

    async def apply_gateway_route_async(
        self,
        request: main_models.ApplyGatewayRouteRequest,
    ) -> main_models.ApplyGatewayRouteResponse:
        runtime = RuntimeOptions()
        return await self.apply_gateway_route_with_options_async(request, runtime)

    def apply_tag_policies_with_options(
        self,
        tmp_req: main_models.ApplyTagPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyTagPoliciesResponse:
        tmp_req.validate()
        request = main_models.ApplyTagPoliciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyTagPolicies',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyTagPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_tag_policies_with_options_async(
        self,
        tmp_req: main_models.ApplyTagPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyTagPoliciesResponse:
        tmp_req.validate()
        request = main_models.ApplyTagPoliciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyTagPolicies',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyTagPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_tag_policies(
        self,
        request: main_models.ApplyTagPoliciesRequest,
    ) -> main_models.ApplyTagPoliciesResponse:
        runtime = RuntimeOptions()
        return self.apply_tag_policies_with_options(request, runtime)

    async def apply_tag_policies_async(
        self,
        request: main_models.ApplyTagPoliciesRequest,
    ) -> main_models.ApplyTagPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.apply_tag_policies_with_options_async(request, runtime)

    def bind_sentinel_block_fallback_definition_with_options(
        self,
        request: main_models.BindSentinelBlockFallbackDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSentinelBlockFallbackDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.fallback_id):
            query['FallbackId'] = request.fallback_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSentinelBlockFallbackDefinition',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSentinelBlockFallbackDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_sentinel_block_fallback_definition_with_options_async(
        self,
        request: main_models.BindSentinelBlockFallbackDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSentinelBlockFallbackDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.fallback_id):
            query['FallbackId'] = request.fallback_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSentinelBlockFallbackDefinition',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSentinelBlockFallbackDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_sentinel_block_fallback_definition(
        self,
        request: main_models.BindSentinelBlockFallbackDefinitionRequest,
    ) -> main_models.BindSentinelBlockFallbackDefinitionResponse:
        runtime = RuntimeOptions()
        return self.bind_sentinel_block_fallback_definition_with_options(request, runtime)

    async def bind_sentinel_block_fallback_definition_async(
        self,
        request: main_models.BindSentinelBlockFallbackDefinitionRequest,
    ) -> main_models.BindSentinelBlockFallbackDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.bind_sentinel_block_fallback_definition_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'ChangeResourceGroup',
            version = '2019-05-31',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'ChangeResourceGroup',
            version = '2019-05-31',
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

    def clone_nacos_config_with_options(
        self,
        request: main_models.CloneNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_ids):
            query['DataIds'] = request.data_ids
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.origin_namespace_id):
            query['OriginNamespaceId'] = request.origin_namespace_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.target_namespace_id):
            query['TargetNamespaceId'] = request.target_namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_nacos_config_with_options_async(
        self,
        request: main_models.CloneNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_ids):
            query['DataIds'] = request.data_ids
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.origin_namespace_id):
            query['OriginNamespaceId'] = request.origin_namespace_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.target_namespace_id):
            query['TargetNamespaceId'] = request.target_namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_nacos_config(
        self,
        request: main_models.CloneNacosConfigRequest,
    ) -> main_models.CloneNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.clone_nacos_config_with_options(request, runtime)

    async def clone_nacos_config_async(
        self,
        request: main_models.CloneNacosConfigRequest,
    ) -> main_models.CloneNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.clone_nacos_config_with_options_async(request, runtime)

    def clone_sentinel_rule_from_ahas_with_options(
        self,
        request: main_models.CloneSentinelRuleFromAhasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneSentinelRuleFromAhasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ahas_namespace):
            query['AhasNamespace'] = request.ahas_namespace
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.is_ahaspublic_region):
            query['IsAHASPublicRegion'] = request.is_ahaspublic_region
        if not DaraCore.is_null(request.mse_app_name):
            query['MseAppName'] = request.mse_app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneSentinelRuleFromAhas',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneSentinelRuleFromAhasResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_sentinel_rule_from_ahas_with_options_async(
        self,
        request: main_models.CloneSentinelRuleFromAhasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloneSentinelRuleFromAhasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ahas_namespace):
            query['AhasNamespace'] = request.ahas_namespace
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.is_ahaspublic_region):
            query['IsAHASPublicRegion'] = request.is_ahaspublic_region
        if not DaraCore.is_null(request.mse_app_name):
            query['MseAppName'] = request.mse_app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloneSentinelRuleFromAhas',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneSentinelRuleFromAhasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_sentinel_rule_from_ahas(
        self,
        request: main_models.CloneSentinelRuleFromAhasRequest,
    ) -> main_models.CloneSentinelRuleFromAhasResponse:
        runtime = RuntimeOptions()
        return self.clone_sentinel_rule_from_ahas_with_options(request, runtime)

    async def clone_sentinel_rule_from_ahas_async(
        self,
        request: main_models.CloneSentinelRuleFromAhasRequest,
    ) -> main_models.CloneSentinelRuleFromAhasResponse:
        runtime = RuntimeOptions()
        return await self.clone_sentinel_rule_from_ahas_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        tmp_req: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_circuit_breaker_rule_with_options(
        self,
        request: main_models.CreateCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.half_open_base_amount_per_step):
            query['HalfOpenBaseAmountPerStep'] = request.half_open_base_amount_per_step
        if not DaraCore.is_null(request.half_open_recovery_step_num):
            query['HalfOpenRecoveryStepNum'] = request.half_open_recovery_step_num
        if not DaraCore.is_null(request.max_allowed_rt_ms):
            query['MaxAllowedRtMs'] = request.max_allowed_rt_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.retry_timeout_ms):
            query['RetryTimeoutMs'] = request.retry_timeout_ms
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCircuitBreakerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_circuit_breaker_rule_with_options_async(
        self,
        request: main_models.CreateCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.half_open_base_amount_per_step):
            query['HalfOpenBaseAmountPerStep'] = request.half_open_base_amount_per_step
        if not DaraCore.is_null(request.half_open_recovery_step_num):
            query['HalfOpenRecoveryStepNum'] = request.half_open_recovery_step_num
        if not DaraCore.is_null(request.max_allowed_rt_ms):
            query['MaxAllowedRtMs'] = request.max_allowed_rt_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.retry_timeout_ms):
            query['RetryTimeoutMs'] = request.retry_timeout_ms
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCircuitBreakerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_circuit_breaker_rule(
        self,
        request: main_models.CreateCircuitBreakerRuleRequest,
    ) -> main_models.CreateCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return self.create_circuit_breaker_rule_with_options(request, runtime)

    async def create_circuit_breaker_rule_async(
        self,
        request: main_models.CreateCircuitBreakerRuleRequest,
    ) -> main_models.CreateCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_circuit_breaker_rule_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_specification):
            query['ClusterSpecification'] = request.cluster_specification
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['ClusterVersion'] = request.cluster_version
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.eip_enabled):
            query['EipEnabled'] = request.eip_enabled
        if not DaraCore.is_null(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.net_type):
            query['NetType'] = request.net_type
        if not DaraCore.is_null(request.private_slb_specification):
            query['PrivateSlbSpecification'] = request.private_slb_specification
        if not DaraCore.is_null(request.pub_network_flow):
            query['PubNetworkFlow'] = request.pub_network_flow
        if not DaraCore.is_null(request.pub_slb_specification):
            query['PubSlbSpecification'] = request.pub_slb_specification
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_type):
            query['SecurityGroupType'] = request.security_group_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_specification):
            query['ClusterSpecification'] = request.cluster_specification
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['ClusterVersion'] = request.cluster_version
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.eip_enabled):
            query['EipEnabled'] = request.eip_enabled
        if not DaraCore.is_null(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.net_type):
            query['NetType'] = request.net_type
        if not DaraCore.is_null(request.private_slb_specification):
            query['PrivateSlbSpecification'] = request.private_slb_specification
        if not DaraCore.is_null(request.pub_network_flow):
            query['PubNetworkFlow'] = request.pub_network_flow
        if not DaraCore.is_null(request.pub_slb_specification):
            query['PubSlbSpecification'] = request.pub_slb_specification
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_type):
            query['SecurityGroupType'] = request.security_group_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_engine_namespace_with_options(
        self,
        request: main_models.CreateEngineNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEngineNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_count):
            query['ServiceCount'] = request.service_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEngineNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_engine_namespace_with_options_async(
        self,
        request: main_models.CreateEngineNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEngineNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_count):
            query['ServiceCount'] = request.service_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEngineNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEngineNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_engine_namespace(
        self,
        request: main_models.CreateEngineNamespaceRequest,
    ) -> main_models.CreateEngineNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_engine_namespace_with_options(request, runtime)

    async def create_engine_namespace_async(
        self,
        request: main_models.CreateEngineNamespaceRequest,
    ) -> main_models.CreateEngineNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_engine_namespace_with_options_async(request, runtime)

    def create_flow_rule_with_options(
        self,
        request: main_models.CreateFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_rule_with_options_async(
        self,
        request: main_models.CreateFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_rule(
        self,
        request: main_models.CreateFlowRuleRequest,
    ) -> main_models.CreateFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.create_flow_rule_with_options(request, runtime)

    async def create_flow_rule_async(
        self,
        request: main_models.CreateFlowRuleRequest,
    ) -> main_models.CreateFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_rule_with_options_async(request, runtime)

    def create_gateway_circuit_breaker_rule_with_options(
        self,
        request: main_models.CreateGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.max_allowed_ms):
            query['MaxAllowedMs'] = request.max_allowed_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.recovery_timeout_sec):
            query['RecoveryTimeoutSec'] = request.recovery_timeout_sec
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.stat_duration_sec):
            query['StatDurationSec'] = request.stat_duration_sec
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.trigger_ratio):
            query['TriggerRatio'] = request.trigger_ratio
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayCircuitBreakerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_circuit_breaker_rule_with_options_async(
        self,
        request: main_models.CreateGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.max_allowed_ms):
            query['MaxAllowedMs'] = request.max_allowed_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.recovery_timeout_sec):
            query['RecoveryTimeoutSec'] = request.recovery_timeout_sec
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.stat_duration_sec):
            query['StatDurationSec'] = request.stat_duration_sec
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.trigger_ratio):
            query['TriggerRatio'] = request.trigger_ratio
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayCircuitBreakerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_circuit_breaker_rule(
        self,
        request: main_models.CreateGatewayCircuitBreakerRuleRequest,
    ) -> main_models.CreateGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return self.create_gateway_circuit_breaker_rule_with_options(request, runtime)

    async def create_gateway_circuit_breaker_rule_async(
        self,
        request: main_models.CreateGatewayCircuitBreakerRuleRequest,
    ) -> main_models.CreateGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_gateway_circuit_breaker_rule_with_options_async(request, runtime)

    def create_gateway_flow_rule_with_options(
        self,
        request: main_models.CreateGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_flow_rule_with_options_async(
        self,
        request: main_models.CreateGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_flow_rule(
        self,
        request: main_models.CreateGatewayFlowRuleRequest,
    ) -> main_models.CreateGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.create_gateway_flow_rule_with_options(request, runtime)

    async def create_gateway_flow_rule_async(
        self,
        request: main_models.CreateGatewayFlowRuleRequest,
    ) -> main_models.CreateGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_gateway_flow_rule_with_options_async(request, runtime)

    def create_gateway_isolation_rule_with_options(
        self,
        request: main_models.CreateGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayIsolationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_isolation_rule_with_options_async(
        self,
        request: main_models.CreateGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayIsolationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_isolation_rule(
        self,
        request: main_models.CreateGatewayIsolationRuleRequest,
    ) -> main_models.CreateGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return self.create_gateway_isolation_rule_with_options(request, runtime)

    async def create_gateway_isolation_rule_async(
        self,
        request: main_models.CreateGatewayIsolationRuleRequest,
    ) -> main_models.CreateGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_gateway_isolation_rule_with_options_async(request, runtime)

    def create_isolation_rule_with_options(
        self,
        request: main_models.CreateIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIsolationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_isolation_rule_with_options_async(
        self,
        request: main_models.CreateIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIsolationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_isolation_rule(
        self,
        request: main_models.CreateIsolationRuleRequest,
    ) -> main_models.CreateIsolationRuleResponse:
        runtime = RuntimeOptions()
        return self.create_isolation_rule_with_options(request, runtime)

    async def create_isolation_rule_async(
        self,
        request: main_models.CreateIsolationRuleRequest,
    ) -> main_models.CreateIsolationRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_isolation_rule_with_options_async(request, runtime)

    def create_mse_service_application_with_options(
        self,
        request: main_models.CreateMseServiceApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMseServiceApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMseServiceApplication',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMseServiceApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mse_service_application_with_options_async(
        self,
        request: main_models.CreateMseServiceApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMseServiceApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMseServiceApplication',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMseServiceApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mse_service_application(
        self,
        request: main_models.CreateMseServiceApplicationRequest,
    ) -> main_models.CreateMseServiceApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_mse_service_application_with_options(request, runtime)

    async def create_mse_service_application_async(
        self,
        request: main_models.CreateMseServiceApplicationRequest,
    ) -> main_models.CreateMseServiceApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_mse_service_application_with_options_async(request, runtime)

    def create_nacos_config_with_options(
        self,
        request: main_models.CreateNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.beta_ips):
            query['BetaIps'] = request.beta_ips
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nacos_config_with_options_async(
        self,
        request: main_models.CreateNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.beta_ips):
            query['BetaIps'] = request.beta_ips
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nacos_config(
        self,
        request: main_models.CreateNacosConfigRequest,
    ) -> main_models.CreateNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.create_nacos_config_with_options(request, runtime)

    async def create_nacos_config_async(
        self,
        request: main_models.CreateNacosConfigRequest,
    ) -> main_models.CreateNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_nacos_config_with_options_async(request, runtime)

    def create_nacos_instance_with_options(
        self,
        request: main_models.CreateNacosInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        body = {}
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosInstance',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nacos_instance_with_options_async(
        self,
        request: main_models.CreateNacosInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        body = {}
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosInstance',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nacos_instance(
        self,
        request: main_models.CreateNacosInstanceRequest,
    ) -> main_models.CreateNacosInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_nacos_instance_with_options(request, runtime)

    async def create_nacos_instance_async(
        self,
        request: main_models.CreateNacosInstanceRequest,
    ) -> main_models.CreateNacosInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_nacos_instance_with_options_async(request, runtime)

    def create_nacos_mcp_server_with_options(
        self,
        request: main_models.CreateNacosMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.encrypt_tool_spec):
            query['EncryptToolSpec'] = request.encrypt_tool_spec
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.server_name):
            query['ServerName'] = request.server_name
        body = {}
        if not DaraCore.is_null(request.endpoint_specification):
            body['EndpointSpecification'] = request.endpoint_specification
        if not DaraCore.is_null(request.server_specification):
            body['ServerSpecification'] = request.server_specification
        if not DaraCore.is_null(request.tool_specification):
            body['ToolSpecification'] = request.tool_specification
        if not DaraCore.is_null(request.yaml_config):
            body['YamlConfig'] = request.yaml_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosMcpServer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nacos_mcp_server_with_options_async(
        self,
        request: main_models.CreateNacosMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.encrypt_tool_spec):
            query['EncryptToolSpec'] = request.encrypt_tool_spec
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.server_name):
            query['ServerName'] = request.server_name
        body = {}
        if not DaraCore.is_null(request.endpoint_specification):
            body['EndpointSpecification'] = request.endpoint_specification
        if not DaraCore.is_null(request.server_specification):
            body['ServerSpecification'] = request.server_specification
        if not DaraCore.is_null(request.tool_specification):
            body['ToolSpecification'] = request.tool_specification
        if not DaraCore.is_null(request.yaml_config):
            body['YamlConfig'] = request.yaml_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosMcpServer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nacos_mcp_server(
        self,
        request: main_models.CreateNacosMcpServerRequest,
    ) -> main_models.CreateNacosMcpServerResponse:
        runtime = RuntimeOptions()
        return self.create_nacos_mcp_server_with_options(request, runtime)

    async def create_nacos_mcp_server_async(
        self,
        request: main_models.CreateNacosMcpServerRequest,
    ) -> main_models.CreateNacosMcpServerResponse:
        runtime = RuntimeOptions()
        return await self.create_nacos_mcp_server_with_options_async(request, runtime)

    def create_nacos_service_with_options(
        self,
        request: main_models.CreateNacosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.protect_threshold):
            query['ProtectThreshold'] = request.protect_threshold
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nacos_service_with_options_async(
        self,
        request: main_models.CreateNacosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNacosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.protect_threshold):
            query['ProtectThreshold'] = request.protect_threshold
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNacosService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNacosServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nacos_service(
        self,
        request: main_models.CreateNacosServiceRequest,
    ) -> main_models.CreateNacosServiceResponse:
        runtime = RuntimeOptions()
        return self.create_nacos_service_with_options(request, runtime)

    async def create_nacos_service_async(
        self,
        request: main_models.CreateNacosServiceRequest,
    ) -> main_models.CreateNacosServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_nacos_service_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        tmp_req: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        tmp_req.validate()
        request = main_models.CreateNamespaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        tmp_req: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        tmp_req.validate()
        request = main_models.CreateNamespaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_or_update_swimming_lane_with_options(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gateway_swimming_lane_route_json):
            request.gateway_swimming_lane_route_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.gateway_swimming_lane_route_json, 'GatewaySwimmingLaneRouteJson', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not DaraCore.is_null(request.entry_rule):
            query['EntryRule'] = request.entry_rule
        if not DaraCore.is_null(request.gateway_swimming_lane_route_json_shrink):
            query['GatewaySwimmingLaneRouteJson'] = request.gateway_swimming_lane_route_json_shrink
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.path_independent_percentage_enable):
            query['PathIndependentPercentageEnable'] = request.path_independent_percentage_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.entry_rules):
            body['EntryRules'] = request.entry_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLane',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_swimming_lane_with_options_async(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gateway_swimming_lane_route_json):
            request.gateway_swimming_lane_route_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.gateway_swimming_lane_route_json, 'GatewaySwimmingLaneRouteJson', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not DaraCore.is_null(request.entry_rule):
            query['EntryRule'] = request.entry_rule
        if not DaraCore.is_null(request.gateway_swimming_lane_route_json_shrink):
            query['GatewaySwimmingLaneRouteJson'] = request.gateway_swimming_lane_route_json_shrink
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.path_independent_percentage_enable):
            query['PathIndependentPercentageEnable'] = request.path_independent_percentage_enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.entry_rules):
            body['EntryRules'] = request.entry_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLane',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_swimming_lane(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_swimming_lane_with_options(request, runtime)

    async def create_or_update_swimming_lane_async(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_swimming_lane_with_options_async(request, runtime)

    def create_or_update_swimming_lane_group_with_options(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.paths):
            request.paths_shrink = Utils.array_to_string_with_specified_style(tmp_req.paths, 'Paths', 'json')
        if not DaraCore.is_null(tmp_req.route_ids):
            request.route_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.route_ids, 'RouteIds', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.canary_model):
            query['CanaryModel'] = request.canary_model
        if not DaraCore.is_null(request.db_gray_enable):
            query['DbGrayEnable'] = request.db_gray_enable
        if not DaraCore.is_null(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.message_queue_filter_side):
            query['MessageQueueFilterSide'] = request.message_queue_filter_side
        if not DaraCore.is_null(request.message_queue_gray_enable):
            query['MessageQueueGrayEnable'] = request.message_queue_gray_enable
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.paths_shrink):
            query['Paths'] = request.paths_shrink
        if not DaraCore.is_null(request.record_canary_detail):
            query['RecordCanaryDetail'] = request.record_canary_detail
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.route_ids_shrink):
            query['RouteIds'] = request.route_ids_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.swim_version):
            query['SwimVersion'] = request.swim_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLaneGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_swimming_lane_group_with_options_async(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.paths):
            request.paths_shrink = Utils.array_to_string_with_specified_style(tmp_req.paths, 'Paths', 'json')
        if not DaraCore.is_null(tmp_req.route_ids):
            request.route_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.route_ids, 'RouteIds', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.canary_model):
            query['CanaryModel'] = request.canary_model
        if not DaraCore.is_null(request.db_gray_enable):
            query['DbGrayEnable'] = request.db_gray_enable
        if not DaraCore.is_null(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.message_queue_filter_side):
            query['MessageQueueFilterSide'] = request.message_queue_filter_side
        if not DaraCore.is_null(request.message_queue_gray_enable):
            query['MessageQueueGrayEnable'] = request.message_queue_gray_enable
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.paths_shrink):
            query['Paths'] = request.paths_shrink
        if not DaraCore.is_null(request.record_canary_detail):
            query['RecordCanaryDetail'] = request.record_canary_detail
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.route_ids_shrink):
            query['RouteIds'] = request.route_ids_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.swim_version):
            query['SwimVersion'] = request.swim_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLaneGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_swimming_lane_group(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_swimming_lane_group_with_options(request, runtime)

    async def create_or_update_swimming_lane_group_async(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_swimming_lane_group_with_options_async(request, runtime)

    def create_plugin_config_with_options(
        self,
        tmp_req: main_models.CreatePluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginConfigResponse:
        tmp_req.validate()
        request = main_models.CreatePluginConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id_list):
            request.resource_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id_list, 'ResourceIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.resource_id_list_shrink):
            query['ResourceIdList'] = request.resource_id_list_shrink
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_config_with_options_async(
        self,
        tmp_req: main_models.CreatePluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginConfigResponse:
        tmp_req.validate()
        request = main_models.CreatePluginConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id_list):
            request.resource_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id_list, 'ResourceIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.resource_id_list_shrink):
            query['ResourceIdList'] = request.resource_id_list_shrink
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin_config(
        self,
        request: main_models.CreatePluginConfigRequest,
    ) -> main_models.CreatePluginConfigResponse:
        runtime = RuntimeOptions()
        return self.create_plugin_config_with_options(request, runtime)

    async def create_plugin_config_async(
        self,
        request: main_models.CreatePluginConfigRequest,
    ) -> main_models.CreatePluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_plugin_config_with_options_async(request, runtime)

    def create_sentinel_block_fallback_definition_with_options(
        self,
        request: main_models.CreateSentinelBlockFallbackDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSentinelBlockFallbackDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.fallback_behavior):
            query['FallbackBehavior'] = request.fallback_behavior
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_classification):
            query['ResourceClassification'] = request.resource_classification
        if not DaraCore.is_null(request.scenario):
            query['Scenario'] = request.scenario
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSentinelBlockFallbackDefinition',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSentinelBlockFallbackDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sentinel_block_fallback_definition_with_options_async(
        self,
        request: main_models.CreateSentinelBlockFallbackDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSentinelBlockFallbackDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.fallback_behavior):
            query['FallbackBehavior'] = request.fallback_behavior
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_classification):
            query['ResourceClassification'] = request.resource_classification
        if not DaraCore.is_null(request.scenario):
            query['Scenario'] = request.scenario
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSentinelBlockFallbackDefinition',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSentinelBlockFallbackDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sentinel_block_fallback_definition(
        self,
        request: main_models.CreateSentinelBlockFallbackDefinitionRequest,
    ) -> main_models.CreateSentinelBlockFallbackDefinitionResponse:
        runtime = RuntimeOptions()
        return self.create_sentinel_block_fallback_definition_with_options(request, runtime)

    async def create_sentinel_block_fallback_definition_async(
        self,
        request: main_models.CreateSentinelBlockFallbackDefinitionRequest,
    ) -> main_models.CreateSentinelBlockFallbackDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.create_sentinel_block_fallback_definition_with_options_async(request, runtime)

    def create_web_flow_rule_with_options(
        self,
        request: main_models.CreateWebFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.burst):
            query['Burst'] = request.burst
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.param_item):
            query['ParamItem'] = request.param_item
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_mode):
            query['ResourceMode'] = request.resource_mode
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_flow_rule_with_options_async(
        self,
        request: main_models.CreateWebFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.burst):
            query['Burst'] = request.burst
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.param_item):
            query['ParamItem'] = request.param_item
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_mode):
            query['ResourceMode'] = request.resource_mode
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_flow_rule(
        self,
        request: main_models.CreateWebFlowRuleRequest,
    ) -> main_models.CreateWebFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.create_web_flow_rule_with_options(request, runtime)

    async def create_web_flow_rule_async(
        self,
        request: main_models.CreateWebFlowRuleRequest,
    ) -> main_models.CreateWebFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_web_flow_rule_with_options_async(request, runtime)

    def create_znode_with_options(
        self,
        request: main_models.CreateZnodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateZnodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateZnode',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_znode_with_options_async(
        self,
        request: main_models.CreateZnodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateZnodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateZnode',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateZnodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_znode(
        self,
        request: main_models.CreateZnodeRequest,
    ) -> main_models.CreateZnodeResponse:
        runtime = RuntimeOptions()
        return self.create_znode_with_options(request, runtime)

    async def create_znode_async(
        self,
        request: main_models.CreateZnodeRequest,
    ) -> main_models.CreateZnodeResponse:
        runtime = RuntimeOptions()
        return await self.create_znode_with_options_async(request, runtime)

    def delete_auth_resource_with_options(
        self,
        request: main_models.DeleteAuthResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAuthResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAuthResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAuthResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auth_resource_with_options_async(
        self,
        request: main_models.DeleteAuthResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAuthResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAuthResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAuthResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auth_resource(
        self,
        request: main_models.DeleteAuthResourceRequest,
    ) -> main_models.DeleteAuthResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_auth_resource_with_options(request, runtime)

    async def delete_auth_resource_async(
        self,
        request: main_models.DeleteAuthResourceRequest,
    ) -> main_models.DeleteAuthResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_auth_resource_with_options_async(request, runtime)

    def delete_black_white_list_with_options(
        self,
        request: main_models.DeleteBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_black_white_list_with_options_async(
        self,
        request: main_models.DeleteBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBlackWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_black_white_list(
        self,
        request: main_models.DeleteBlackWhiteListRequest,
    ) -> main_models.DeleteBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return self.delete_black_white_list_with_options(request, runtime)

    async def delete_black_white_list_async(
        self,
        request: main_models.DeleteBlackWhiteListRequest,
    ) -> main_models.DeleteBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.delete_black_white_list_with_options_async(request, runtime)

    def delete_circuit_breaker_rules_with_options(
        self,
        tmp_req: main_models.DeleteCircuitBreakerRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCircuitBreakerRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteCircuitBreakerRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCircuitBreakerRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCircuitBreakerRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_circuit_breaker_rules_with_options_async(
        self,
        tmp_req: main_models.DeleteCircuitBreakerRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCircuitBreakerRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteCircuitBreakerRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCircuitBreakerRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCircuitBreakerRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_circuit_breaker_rules(
        self,
        request: main_models.DeleteCircuitBreakerRulesRequest,
    ) -> main_models.DeleteCircuitBreakerRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_circuit_breaker_rules_with_options(request, runtime)

    async def delete_circuit_breaker_rules_async(
        self,
        request: main_models.DeleteCircuitBreakerRulesRequest,
    ) -> main_models.DeleteCircuitBreakerRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_circuit_breaker_rules_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_engine_namespace_with_options(
        self,
        request: main_models.DeleteEngineNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEngineNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEngineNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_engine_namespace_with_options_async(
        self,
        request: main_models.DeleteEngineNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEngineNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEngineNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEngineNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_engine_namespace(
        self,
        request: main_models.DeleteEngineNamespaceRequest,
    ) -> main_models.DeleteEngineNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_engine_namespace_with_options(request, runtime)

    async def delete_engine_namespace_async(
        self,
        request: main_models.DeleteEngineNamespaceRequest,
    ) -> main_models.DeleteEngineNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_engine_namespace_with_options_async(request, runtime)

    def delete_flow_rules_with_options(
        self,
        tmp_req: main_models.DeleteFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteFlowRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_rules_with_options_async(
        self,
        tmp_req: main_models.DeleteFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteFlowRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_rules(
        self,
        request: main_models.DeleteFlowRulesRequest,
    ) -> main_models.DeleteFlowRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_rules_with_options(request, runtime)

    async def delete_flow_rules_async(
        self,
        request: main_models.DeleteFlowRulesRequest,
    ) -> main_models.DeleteFlowRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_rules_with_options_async(request, runtime)

    def delete_gateway_with_options(
        self,
        request: main_models.DeleteGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.delete_slb):
            query['DeleteSlb'] = request.delete_slb
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        request: main_models.DeleteGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.delete_slb):
            query['DeleteSlb'] = request.delete_slb
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        request: main_models.DeleteGatewayRequest,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_with_options(request, runtime)

    async def delete_gateway_async(
        self,
        request: main_models.DeleteGatewayRequest,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_with_options_async(request, runtime)

    def delete_gateway_auth_with_options(
        self,
        request: main_models.DeleteGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_auth_with_options_async(
        self,
        request: main_models.DeleteGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_auth(
        self,
        request: main_models.DeleteGatewayAuthRequest,
    ) -> main_models.DeleteGatewayAuthResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_auth_with_options(request, runtime)

    async def delete_gateway_auth_async(
        self,
        request: main_models.DeleteGatewayAuthRequest,
    ) -> main_models.DeleteGatewayAuthResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_auth_with_options_async(request, runtime)

    def delete_gateway_auth_consumer_with_options(
        self,
        request: main_models.DeleteGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayAuthConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_auth_consumer_with_options_async(
        self,
        request: main_models.DeleteGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayAuthConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_auth_consumer(
        self,
        request: main_models.DeleteGatewayAuthConsumerRequest,
    ) -> main_models.DeleteGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_auth_consumer_with_options(request, runtime)

    async def delete_gateway_auth_consumer_async(
        self,
        request: main_models.DeleteGatewayAuthConsumerRequest,
    ) -> main_models.DeleteGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_auth_consumer_with_options_async(request, runtime)

    def delete_gateway_auth_consumer_resource_with_options(
        self,
        request: main_models.DeleteGatewayAuthConsumerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayAuthConsumerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id_list):
            query['IdList'] = request.id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayAuthConsumerResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayAuthConsumerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_auth_consumer_resource_with_options_async(
        self,
        request: main_models.DeleteGatewayAuthConsumerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayAuthConsumerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id_list):
            query['IdList'] = request.id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayAuthConsumerResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayAuthConsumerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_auth_consumer_resource(
        self,
        request: main_models.DeleteGatewayAuthConsumerResourceRequest,
    ) -> main_models.DeleteGatewayAuthConsumerResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_auth_consumer_resource_with_options(request, runtime)

    async def delete_gateway_auth_consumer_resource_async(
        self,
        request: main_models.DeleteGatewayAuthConsumerResourceRequest,
    ) -> main_models.DeleteGatewayAuthConsumerResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_auth_consumer_resource_with_options_async(request, runtime)

    def delete_gateway_circuit_breaker_rule_with_options(
        self,
        request: main_models.DeleteGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayCircuitBreakerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_circuit_breaker_rule_with_options_async(
        self,
        request: main_models.DeleteGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayCircuitBreakerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_circuit_breaker_rule(
        self,
        request: main_models.DeleteGatewayCircuitBreakerRuleRequest,
    ) -> main_models.DeleteGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_circuit_breaker_rule_with_options(request, runtime)

    async def delete_gateway_circuit_breaker_rule_async(
        self,
        request: main_models.DeleteGatewayCircuitBreakerRuleRequest,
    ) -> main_models.DeleteGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_circuit_breaker_rule_with_options_async(request, runtime)

    def delete_gateway_domain_with_options(
        self,
        request: main_models.DeleteGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_domain_with_options_async(
        self,
        request: main_models.DeleteGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_domain(
        self,
        request: main_models.DeleteGatewayDomainRequest,
    ) -> main_models.DeleteGatewayDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_domain_with_options(request, runtime)

    async def delete_gateway_domain_async(
        self,
        request: main_models.DeleteGatewayDomainRequest,
    ) -> main_models.DeleteGatewayDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_domain_with_options_async(request, runtime)

    def delete_gateway_flow_rule_with_options(
        self,
        request: main_models.DeleteGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_flow_rule_with_options_async(
        self,
        request: main_models.DeleteGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_flow_rule(
        self,
        request: main_models.DeleteGatewayFlowRuleRequest,
    ) -> main_models.DeleteGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_flow_rule_with_options(request, runtime)

    async def delete_gateway_flow_rule_async(
        self,
        request: main_models.DeleteGatewayFlowRuleRequest,
    ) -> main_models.DeleteGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_flow_rule_with_options_async(request, runtime)

    def delete_gateway_isolation_rule_with_options(
        self,
        request: main_models.DeleteGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayIsolationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_isolation_rule_with_options_async(
        self,
        request: main_models.DeleteGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayIsolationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_isolation_rule(
        self,
        request: main_models.DeleteGatewayIsolationRuleRequest,
    ) -> main_models.DeleteGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_isolation_rule_with_options(request, runtime)

    async def delete_gateway_isolation_rule_async(
        self,
        request: main_models.DeleteGatewayIsolationRuleRequest,
    ) -> main_models.DeleteGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_isolation_rule_with_options_async(request, runtime)

    def delete_gateway_route_with_options(
        self,
        request: main_models.DeleteGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_route_with_options_async(
        self,
        request: main_models.DeleteGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_route(
        self,
        request: main_models.DeleteGatewayRouteRequest,
    ) -> main_models.DeleteGatewayRouteResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_route_with_options(request, runtime)

    async def delete_gateway_route_async(
        self,
        request: main_models.DeleteGatewayRouteRequest,
    ) -> main_models.DeleteGatewayRouteResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_route_with_options_async(request, runtime)

    def delete_gateway_service_with_options(
        self,
        request: main_models.DeleteGatewayServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_service_with_options_async(
        self,
        request: main_models.DeleteGatewayServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_service(
        self,
        request: main_models.DeleteGatewayServiceRequest,
    ) -> main_models.DeleteGatewayServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_service_with_options(request, runtime)

    async def delete_gateway_service_async(
        self,
        request: main_models.DeleteGatewayServiceRequest,
    ) -> main_models.DeleteGatewayServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_service_with_options_async(request, runtime)

    def delete_gateway_service_version_with_options(
        self,
        request: main_models.DeleteGatewayServiceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayServiceVersion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_service_version_with_options_async(
        self,
        request: main_models.DeleteGatewayServiceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayServiceVersion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_service_version(
        self,
        request: main_models.DeleteGatewayServiceVersionRequest,
    ) -> main_models.DeleteGatewayServiceVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_service_version_with_options(request, runtime)

    async def delete_gateway_service_version_async(
        self,
        request: main_models.DeleteGatewayServiceVersionRequest,
    ) -> main_models.DeleteGatewayServiceVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_service_version_with_options_async(request, runtime)

    def delete_gateway_slb_with_options(
        self,
        request: main_models.DeleteGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewaySlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.delete_slb):
            query['DeleteSlb'] = request.delete_slb
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_slb_with_options_async(
        self,
        request: main_models.DeleteGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewaySlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.delete_slb):
            query['DeleteSlb'] = request.delete_slb
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewaySlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_slb(
        self,
        request: main_models.DeleteGatewaySlbRequest,
    ) -> main_models.DeleteGatewaySlbResponse:
        runtime = RuntimeOptions()
        return self.delete_gateway_slb_with_options(request, runtime)

    async def delete_gateway_slb_async(
        self,
        request: main_models.DeleteGatewaySlbRequest,
    ) -> main_models.DeleteGatewaySlbResponse:
        runtime = RuntimeOptions()
        return await self.delete_gateway_slb_with_options_async(request, runtime)

    def delete_isolation_rules_with_options(
        self,
        tmp_req: main_models.DeleteIsolationRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIsolationRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteIsolationRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIsolationRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIsolationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_isolation_rules_with_options_async(
        self,
        tmp_req: main_models.DeleteIsolationRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIsolationRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteIsolationRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIsolationRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIsolationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_isolation_rules(
        self,
        request: main_models.DeleteIsolationRulesRequest,
    ) -> main_models.DeleteIsolationRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_isolation_rules_with_options(request, runtime)

    async def delete_isolation_rules_async(
        self,
        request: main_models.DeleteIsolationRulesRequest,
    ) -> main_models.DeleteIsolationRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_isolation_rules_with_options_async(request, runtime)

    def delete_migration_task_with_options(
        self,
        request: main_models.DeleteMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_task_with_options_async(
        self,
        request: main_models.DeleteMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_task(
        self,
        request: main_models.DeleteMigrationTaskRequest,
    ) -> main_models.DeleteMigrationTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_migration_task_with_options(request, runtime)

    async def delete_migration_task_async(
        self,
        request: main_models.DeleteMigrationTaskRequest,
    ) -> main_models.DeleteMigrationTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_migration_task_with_options_async(request, runtime)

    def delete_nacos_config_with_options(
        self,
        request: main_models.DeleteNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.beta):
            query['Beta'] = request.beta
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_config_with_options_async(
        self,
        request: main_models.DeleteNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.beta):
            query['Beta'] = request.beta
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_config(
        self,
        request: main_models.DeleteNacosConfigRequest,
    ) -> main_models.DeleteNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_nacos_config_with_options(request, runtime)

    async def delete_nacos_config_async(
        self,
        request: main_models.DeleteNacosConfigRequest,
    ) -> main_models.DeleteNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_nacos_config_with_options_async(request, runtime)

    def delete_nacos_configs_with_options(
        self,
        request: main_models.DeleteNacosConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosConfigs',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_configs_with_options_async(
        self,
        request: main_models.DeleteNacosConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosConfigs',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_configs(
        self,
        request: main_models.DeleteNacosConfigsRequest,
    ) -> main_models.DeleteNacosConfigsResponse:
        runtime = RuntimeOptions()
        return self.delete_nacos_configs_with_options(request, runtime)

    async def delete_nacos_configs_async(
        self,
        request: main_models.DeleteNacosConfigsRequest,
    ) -> main_models.DeleteNacosConfigsResponse:
        runtime = RuntimeOptions()
        return await self.delete_nacos_configs_with_options_async(request, runtime)

    def delete_nacos_instance_with_options(
        self,
        request: main_models.DeleteNacosInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosInstance',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_instance_with_options_async(
        self,
        request: main_models.DeleteNacosInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosInstance',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_instance(
        self,
        request: main_models.DeleteNacosInstanceRequest,
    ) -> main_models.DeleteNacosInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_nacos_instance_with_options(request, runtime)

    async def delete_nacos_instance_async(
        self,
        request: main_models.DeleteNacosInstanceRequest,
    ) -> main_models.DeleteNacosInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_nacos_instance_with_options_async(request, runtime)

    def delete_nacos_mcp_server_with_options(
        self,
        request: main_models.DeleteNacosMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosMcpServer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_mcp_server_with_options_async(
        self,
        request: main_models.DeleteNacosMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosMcpServer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_mcp_server(
        self,
        request: main_models.DeleteNacosMcpServerRequest,
    ) -> main_models.DeleteNacosMcpServerResponse:
        runtime = RuntimeOptions()
        return self.delete_nacos_mcp_server_with_options(request, runtime)

    async def delete_nacos_mcp_server_async(
        self,
        request: main_models.DeleteNacosMcpServerRequest,
    ) -> main_models.DeleteNacosMcpServerResponse:
        runtime = RuntimeOptions()
        return await self.delete_nacos_mcp_server_with_options_async(request, runtime)

    def delete_nacos_service_with_options(
        self,
        request: main_models.DeleteNacosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_service_with_options_async(
        self,
        request: main_models.DeleteNacosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNacosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNacosService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNacosServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_service(
        self,
        request: main_models.DeleteNacosServiceRequest,
    ) -> main_models.DeleteNacosServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_nacos_service_with_options(request, runtime)

    async def delete_nacos_service_async(
        self,
        request: main_models.DeleteNacosServiceRequest,
    ) -> main_models.DeleteNacosServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_nacos_service_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_plugin_config_with_options(
        self,
        request: main_models.DeletePluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.plugin_config_id):
            query['PluginConfigId'] = request.plugin_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_config_with_options_async(
        self,
        request: main_models.DeletePluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.plugin_config_id):
            query['PluginConfigId'] = request.plugin_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin_config(
        self,
        request: main_models.DeletePluginConfigRequest,
    ) -> main_models.DeletePluginConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_plugin_config_with_options(request, runtime)

    async def delete_plugin_config_async(
        self,
        request: main_models.DeletePluginConfigRequest,
    ) -> main_models.DeletePluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_plugin_config_with_options_async(request, runtime)

    def delete_security_group_rule_with_options(
        self,
        request: main_models.DeleteSecurityGroupRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cascading_delete):
            query['CascadingDelete'] = request.cascading_delete
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityGroupRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_group_rule_with_options_async(
        self,
        request: main_models.DeleteSecurityGroupRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cascading_delete):
            query['CascadingDelete'] = request.cascading_delete
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityGroupRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_group_rule(
        self,
        request: main_models.DeleteSecurityGroupRuleRequest,
    ) -> main_models.DeleteSecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_security_group_rule_with_options(request, runtime)

    async def delete_security_group_rule_async(
        self,
        request: main_models.DeleteSecurityGroupRuleRequest,
    ) -> main_models.DeleteSecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_group_rule_with_options_async(request, runtime)

    def delete_service_source_with_options(
        self,
        request: main_models.DeleteServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_source_with_options_async(
        self,
        request: main_models.DeleteServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_source(
        self,
        request: main_models.DeleteServiceSourceRequest,
    ) -> main_models.DeleteServiceSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_service_source_with_options(request, runtime)

    async def delete_service_source_async(
        self,
        request: main_models.DeleteServiceSourceRequest,
    ) -> main_models.DeleteServiceSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_source_with_options_async(request, runtime)

    def delete_swimming_lane_with_options(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLane',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swimming_lane_with_options_async(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLane',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swimming_lane(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
    ) -> main_models.DeleteSwimmingLaneResponse:
        runtime = RuntimeOptions()
        return self.delete_swimming_lane_with_options(request, runtime)

    async def delete_swimming_lane_async(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
    ) -> main_models.DeleteSwimmingLaneResponse:
        runtime = RuntimeOptions()
        return await self.delete_swimming_lane_with_options_async(request, runtime)

    def delete_swimming_lane_group_with_options(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLaneGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swimming_lane_group_with_options_async(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLaneGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swimming_lane_group(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_swimming_lane_group_with_options(request, runtime)

    async def delete_swimming_lane_group_async(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_swimming_lane_group_with_options_async(request, runtime)

    def delete_web_flow_rules_with_options(
        self,
        request: main_models.DeleteWebFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebFlowRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebFlowRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_flow_rules_with_options_async(
        self,
        request: main_models.DeleteWebFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebFlowRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebFlowRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_flow_rules(
        self,
        request: main_models.DeleteWebFlowRulesRequest,
    ) -> main_models.DeleteWebFlowRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_web_flow_rules_with_options(request, runtime)

    async def delete_web_flow_rules_async(
        self,
        request: main_models.DeleteWebFlowRulesRequest,
    ) -> main_models.DeleteWebFlowRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_web_flow_rules_with_options_async(request, runtime)

    def delete_znode_with_options(
        self,
        request: main_models.DeleteZnodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteZnodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteZnode',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_znode_with_options_async(
        self,
        request: main_models.DeleteZnodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteZnodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteZnode',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteZnodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_znode(
        self,
        request: main_models.DeleteZnodeRequest,
    ) -> main_models.DeleteZnodeResponse:
        runtime = RuntimeOptions()
        return self.delete_znode_with_options(request, runtime)

    async def delete_znode_async(
        self,
        request: main_models.DeleteZnodeRequest,
    ) -> main_models.DeleteZnodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_znode_with_options_async(request, runtime)

    def enable_http_2with_options(
        self,
        request: main_models.EnableHttp2Request,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHttp2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHttp2',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHttp2Response(),
            self.call_api(params, req, runtime)
        )

    async def enable_http_2with_options_async(
        self,
        request: main_models.EnableHttp2Request,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHttp2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHttp2',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHttp2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_http_2(
        self,
        request: main_models.EnableHttp2Request,
    ) -> main_models.EnableHttp2Response:
        runtime = RuntimeOptions()
        return self.enable_http_2with_options(request, runtime)

    async def enable_http_2_async(
        self,
        request: main_models.EnableHttp2Request,
    ) -> main_models.EnableHttp2Response:
        runtime = RuntimeOptions()
        return await self.enable_http_2with_options_async(request, runtime)

    def enable_proxy_protocol_with_options(
        self,
        request: main_models.EnableProxyProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableProxyProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable_proxy_protocol):
            query['EnableProxyProtocol'] = request.enable_proxy_protocol
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableProxyProtocol',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableProxyProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_proxy_protocol_with_options_async(
        self,
        request: main_models.EnableProxyProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableProxyProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable_proxy_protocol):
            query['EnableProxyProtocol'] = request.enable_proxy_protocol
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableProxyProtocol',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableProxyProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_proxy_protocol(
        self,
        request: main_models.EnableProxyProtocolRequest,
    ) -> main_models.EnableProxyProtocolResponse:
        runtime = RuntimeOptions()
        return self.enable_proxy_protocol_with_options(request, runtime)

    async def enable_proxy_protocol_async(
        self,
        request: main_models.EnableProxyProtocolRequest,
    ) -> main_models.EnableProxyProtocolResponse:
        runtime = RuntimeOptions()
        return await self.enable_proxy_protocol_with_options_async(request, runtime)

    def export_nacos_config_with_options(
        self,
        request: main_models.ExportNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.data_ids):
            query['DataIds'] = request.data_ids
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_nacos_config_with_options_async(
        self,
        request: main_models.ExportNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.data_ids):
            query['DataIds'] = request.data_ids
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_nacos_config(
        self,
        request: main_models.ExportNacosConfigRequest,
    ) -> main_models.ExportNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.export_nacos_config_with_options(request, runtime)

    async def export_nacos_config_async(
        self,
        request: main_models.ExportNacosConfigRequest,
    ) -> main_models.ExportNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.export_nacos_config_with_options_async(request, runtime)

    def export_zookeeper_data_with_options(
        self,
        request: main_models.ExportZookeeperDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportZookeeperDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportZookeeperData',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportZookeeperDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_zookeeper_data_with_options_async(
        self,
        request: main_models.ExportZookeeperDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportZookeeperDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportZookeeperData',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportZookeeperDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_zookeeper_data(
        self,
        request: main_models.ExportZookeeperDataRequest,
    ) -> main_models.ExportZookeeperDataResponse:
        runtime = RuntimeOptions()
        return self.export_zookeeper_data_with_options(request, runtime)

    async def export_zookeeper_data_async(
        self,
        request: main_models.ExportZookeeperDataRequest,
    ) -> main_models.ExportZookeeperDataResponse:
        runtime = RuntimeOptions()
        return await self.export_zookeeper_data_with_options_async(request, runtime)

    def fetch_lossless_rule_list_with_options(
        self,
        request: main_models.FetchLosslessRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchLosslessRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
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
            action = 'FetchLosslessRuleList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchLosslessRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_lossless_rule_list_with_options_async(
        self,
        request: main_models.FetchLosslessRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchLosslessRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
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
            action = 'FetchLosslessRuleList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchLosslessRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_lossless_rule_list(
        self,
        request: main_models.FetchLosslessRuleListRequest,
    ) -> main_models.FetchLosslessRuleListResponse:
        runtime = RuntimeOptions()
        return self.fetch_lossless_rule_list_with_options(request, runtime)

    async def fetch_lossless_rule_list_async(
        self,
        request: main_models.FetchLosslessRuleListRequest,
    ) -> main_models.FetchLosslessRuleListResponse:
        runtime = RuntimeOptions()
        return await self.fetch_lossless_rule_list_with_options_async(request, runtime)

    def gateway_black_white_list_with_options(
        self,
        tmp_req: main_models.GatewayBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GatewayBlackWhiteListResponse:
        tmp_req.validate()
        request = main_models.GatewayBlackWhiteListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GatewayBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GatewayBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def gateway_black_white_list_with_options_async(
        self,
        tmp_req: main_models.GatewayBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GatewayBlackWhiteListResponse:
        tmp_req.validate()
        request = main_models.GatewayBlackWhiteListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GatewayBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GatewayBlackWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gateway_black_white_list(
        self,
        request: main_models.GatewayBlackWhiteListRequest,
    ) -> main_models.GatewayBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return self.gateway_black_white_list_with_options(request, runtime)

    async def gateway_black_white_list_async(
        self,
        request: main_models.GatewayBlackWhiteListRequest,
    ) -> main_models.GatewayBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.gateway_black_white_list_with_options_async(request, runtime)

    def get_app_message_queue_route_with_options(
        self,
        request: main_models.GetAppMessageQueueRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppMessageQueueRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppMessageQueueRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppMessageQueueRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_message_queue_route_with_options_async(
        self,
        request: main_models.GetAppMessageQueueRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppMessageQueueRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppMessageQueueRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppMessageQueueRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_message_queue_route(
        self,
        request: main_models.GetAppMessageQueueRouteRequest,
    ) -> main_models.GetAppMessageQueueRouteResponse:
        runtime = RuntimeOptions()
        return self.get_app_message_queue_route_with_options(request, runtime)

    async def get_app_message_queue_route_async(
        self,
        request: main_models.GetAppMessageQueueRouteRequest,
    ) -> main_models.GetAppMessageQueueRouteResponse:
        runtime = RuntimeOptions()
        return await self.get_app_message_queue_route_with_options_async(request, runtime)

    def get_application_instance_list_with_options(
        self,
        request: main_models.GetApplicationInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationInstanceList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_instance_list_with_options_async(
        self,
        request: main_models.GetApplicationInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationInstanceList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_instance_list(
        self,
        request: main_models.GetApplicationInstanceListRequest,
    ) -> main_models.GetApplicationInstanceListResponse:
        runtime = RuntimeOptions()
        return self.get_application_instance_list_with_options(request, runtime)

    async def get_application_instance_list_async(
        self,
        request: main_models.GetApplicationInstanceListRequest,
    ) -> main_models.GetApplicationInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.get_application_instance_list_with_options_async(request, runtime)

    def get_application_list_with_options(
        self,
        tmp_req: main_models.GetApplicationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationListResponse:
        tmp_req.validate()
        request = main_models.GetApplicationListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_list_with_options_async(
        self,
        tmp_req: main_models.GetApplicationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationListResponse:
        tmp_req.validate()
        request = main_models.GetApplicationListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_list(
        self,
        request: main_models.GetApplicationListRequest,
    ) -> main_models.GetApplicationListResponse:
        runtime = RuntimeOptions()
        return self.get_application_list_with_options(request, runtime)

    async def get_application_list_async(
        self,
        request: main_models.GetApplicationListRequest,
    ) -> main_models.GetApplicationListResponse:
        runtime = RuntimeOptions()
        return await self.get_application_list_with_options_async(request, runtime)

    def get_black_white_list_with_options(
        self,
        request: main_models.GetBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_black_white_list_with_options_async(
        self,
        request: main_models.GetBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBlackWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_black_white_list(
        self,
        request: main_models.GetBlackWhiteListRequest,
    ) -> main_models.GetBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return self.get_black_white_list_with_options(request, runtime)

    async def get_black_white_list_async(
        self,
        request: main_models.GetBlackWhiteListRequest,
    ) -> main_models.GetBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.get_black_white_list_with_options_async(request, runtime)

    def get_engine_namepace_with_options(
        self,
        request: main_models.GetEngineNamepaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEngineNamepaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEngineNamepace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEngineNamepaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_engine_namepace_with_options_async(
        self,
        request: main_models.GetEngineNamepaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEngineNamepaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEngineNamepace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEngineNamepaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_engine_namepace(
        self,
        request: main_models.GetEngineNamepaceRequest,
    ) -> main_models.GetEngineNamepaceResponse:
        runtime = RuntimeOptions()
        return self.get_engine_namepace_with_options(request, runtime)

    async def get_engine_namepace_async(
        self,
        request: main_models.GetEngineNamepaceRequest,
    ) -> main_models.GetEngineNamepaceResponse:
        runtime = RuntimeOptions()
        return await self.get_engine_namepace_with_options_async(request, runtime)

    def get_gateway_with_options(
        self,
        request: main_models.GetGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        request: main_models.GetGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway(
        self,
        request: main_models.GetGatewayRequest,
    ) -> main_models.GetGatewayResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_with_options(request, runtime)

    async def get_gateway_async(
        self,
        request: main_models.GetGatewayRequest,
    ) -> main_models.GetGatewayResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_with_options_async(request, runtime)

    def get_gateway_auth_consumer_detail_with_options(
        self,
        request: main_models.GetGatewayAuthConsumerDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayAuthConsumerDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayAuthConsumerDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayAuthConsumerDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_auth_consumer_detail_with_options_async(
        self,
        request: main_models.GetGatewayAuthConsumerDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayAuthConsumerDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayAuthConsumerDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayAuthConsumerDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_auth_consumer_detail(
        self,
        request: main_models.GetGatewayAuthConsumerDetailRequest,
    ) -> main_models.GetGatewayAuthConsumerDetailResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_auth_consumer_detail_with_options(request, runtime)

    async def get_gateway_auth_consumer_detail_async(
        self,
        request: main_models.GetGatewayAuthConsumerDetailRequest,
    ) -> main_models.GetGatewayAuthConsumerDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_auth_consumer_detail_with_options_async(request, runtime)

    def get_gateway_auth_detail_with_options(
        self,
        request: main_models.GetGatewayAuthDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayAuthDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayAuthDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayAuthDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_auth_detail_with_options_async(
        self,
        request: main_models.GetGatewayAuthDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayAuthDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayAuthDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayAuthDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_auth_detail(
        self,
        request: main_models.GetGatewayAuthDetailRequest,
    ) -> main_models.GetGatewayAuthDetailResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_auth_detail_with_options(request, runtime)

    async def get_gateway_auth_detail_async(
        self,
        request: main_models.GetGatewayAuthDetailRequest,
    ) -> main_models.GetGatewayAuthDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_auth_detail_with_options_async(request, runtime)

    def get_gateway_config_with_options(
        self,
        request: main_models.GetGatewayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_config_with_options_async(
        self,
        request: main_models.GetGatewayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_config(
        self,
        request: main_models.GetGatewayConfigRequest,
    ) -> main_models.GetGatewayConfigResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_config_with_options(request, runtime)

    async def get_gateway_config_async(
        self,
        request: main_models.GetGatewayConfigRequest,
    ) -> main_models.GetGatewayConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_config_with_options_async(request, runtime)

    def get_gateway_domain_detail_with_options(
        self,
        request: main_models.GetGatewayDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayDomainDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_domain_detail_with_options_async(
        self,
        request: main_models.GetGatewayDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayDomainDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_domain_detail(
        self,
        request: main_models.GetGatewayDomainDetailRequest,
    ) -> main_models.GetGatewayDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_domain_detail_with_options(request, runtime)

    async def get_gateway_domain_detail_async(
        self,
        request: main_models.GetGatewayDomainDetailRequest,
    ) -> main_models.GetGatewayDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_domain_detail_with_options_async(request, runtime)

    def get_gateway_option_with_options(
        self,
        request: main_models.GetGatewayOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayOptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayOption',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_option_with_options_async(
        self,
        request: main_models.GetGatewayOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayOptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayOption',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_option(
        self,
        request: main_models.GetGatewayOptionRequest,
    ) -> main_models.GetGatewayOptionResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_option_with_options(request, runtime)

    async def get_gateway_option_async(
        self,
        request: main_models.GetGatewayOptionRequest,
    ) -> main_models.GetGatewayOptionResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_option_with_options_async(request, runtime)

    def get_gateway_route_detail_with_options(
        self,
        request: main_models.GetGatewayRouteDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayRouteDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayRouteDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayRouteDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_route_detail_with_options_async(
        self,
        request: main_models.GetGatewayRouteDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayRouteDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayRouteDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayRouteDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_route_detail(
        self,
        request: main_models.GetGatewayRouteDetailRequest,
    ) -> main_models.GetGatewayRouteDetailResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_route_detail_with_options(request, runtime)

    async def get_gateway_route_detail_async(
        self,
        request: main_models.GetGatewayRouteDetailRequest,
    ) -> main_models.GetGatewayRouteDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_route_detail_with_options_async(request, runtime)

    def get_gateway_service_detail_with_options(
        self,
        request: main_models.GetGatewayServiceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayServiceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayServiceDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_service_detail_with_options_async(
        self,
        request: main_models.GetGatewayServiceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayServiceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayServiceDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_service_detail(
        self,
        request: main_models.GetGatewayServiceDetailRequest,
    ) -> main_models.GetGatewayServiceDetailResponse:
        runtime = RuntimeOptions()
        return self.get_gateway_service_detail_with_options(request, runtime)

    async def get_gateway_service_detail_async(
        self,
        request: main_models.GetGatewayServiceDetailRequest,
    ) -> main_models.GetGatewayServiceDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_gateway_service_detail_with_options_async(request, runtime)

    def get_governance_kubernetes_cluster_with_options(
        self,
        request: main_models.GetGovernanceKubernetesClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceKubernetesClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGovernanceKubernetesCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_kubernetes_cluster_with_options_async(
        self,
        request: main_models.GetGovernanceKubernetesClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceKubernetesClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGovernanceKubernetesCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceKubernetesClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_kubernetes_cluster(
        self,
        request: main_models.GetGovernanceKubernetesClusterRequest,
    ) -> main_models.GetGovernanceKubernetesClusterResponse:
        runtime = RuntimeOptions()
        return self.get_governance_kubernetes_cluster_with_options(request, runtime)

    async def get_governance_kubernetes_cluster_async(
        self,
        request: main_models.GetGovernanceKubernetesClusterRequest,
    ) -> main_models.GetGovernanceKubernetesClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_governance_kubernetes_cluster_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        request: main_models.GetImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        request: main_models.GetImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        request: main_models.GetImageRequest,
    ) -> main_models.GetImageResponse:
        runtime = RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    async def get_image_async(
        self,
        request: main_models.GetImageRequest,
    ) -> main_models.GetImageResponse:
        runtime = RuntimeOptions()
        return await self.get_image_with_options_async(request, runtime)

    def get_import_file_url_with_options(
        self,
        request: main_models.GetImportFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImportFileUrl',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_import_file_url_with_options_async(
        self,
        request: main_models.GetImportFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImportFileUrl',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImportFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_import_file_url(
        self,
        request: main_models.GetImportFileUrlRequest,
    ) -> main_models.GetImportFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_import_file_url_with_options(request, runtime)

    async def get_import_file_url_async(
        self,
        request: main_models.GetImportFileUrlRequest,
    ) -> main_models.GetImportFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_import_file_url_with_options_async(request, runtime)

    def get_kubernetes_source_with_options(
        self,
        request: main_models.GetKubernetesSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKubernetesSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_all):
            query['IsAll'] = request.is_all
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKubernetesSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKubernetesSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kubernetes_source_with_options_async(
        self,
        request: main_models.GetKubernetesSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKubernetesSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.is_all):
            query['IsAll'] = request.is_all
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKubernetesSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKubernetesSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kubernetes_source(
        self,
        request: main_models.GetKubernetesSourceRequest,
    ) -> main_models.GetKubernetesSourceResponse:
        runtime = RuntimeOptions()
        return self.get_kubernetes_source_with_options(request, runtime)

    async def get_kubernetes_source_async(
        self,
        request: main_models.GetKubernetesSourceRequest,
    ) -> main_models.GetKubernetesSourceResponse:
        runtime = RuntimeOptions()
        return await self.get_kubernetes_source_with_options_async(request, runtime)

    def get_locality_rule_with_options(
        self,
        request: main_models.GetLocalityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLocalityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLocalityRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLocalityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_locality_rule_with_options_async(
        self,
        request: main_models.GetLocalityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLocalityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLocalityRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLocalityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_locality_rule(
        self,
        request: main_models.GetLocalityRuleRequest,
    ) -> main_models.GetLocalityRuleResponse:
        runtime = RuntimeOptions()
        return self.get_locality_rule_with_options(request, runtime)

    async def get_locality_rule_async(
        self,
        request: main_models.GetLocalityRuleRequest,
    ) -> main_models.GetLocalityRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_locality_rule_with_options_async(request, runtime)

    def get_lossless_rule_by_app_with_options(
        self,
        request: main_models.GetLosslessRuleByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLosslessRuleByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLosslessRuleByApp',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLosslessRuleByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lossless_rule_by_app_with_options_async(
        self,
        request: main_models.GetLosslessRuleByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLosslessRuleByAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLosslessRuleByApp',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLosslessRuleByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lossless_rule_by_app(
        self,
        request: main_models.GetLosslessRuleByAppRequest,
    ) -> main_models.GetLosslessRuleByAppResponse:
        runtime = RuntimeOptions()
        return self.get_lossless_rule_by_app_with_options(request, runtime)

    async def get_lossless_rule_by_app_async(
        self,
        request: main_models.GetLosslessRuleByAppRequest,
    ) -> main_models.GetLosslessRuleByAppResponse:
        runtime = RuntimeOptions()
        return await self.get_lossless_rule_by_app_with_options_async(request, runtime)

    def get_mse_feature_switch_with_options(
        self,
        request: main_models.GetMseFeatureSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMseFeatureSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMseFeatureSwitch',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMseFeatureSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mse_feature_switch_with_options_async(
        self,
        request: main_models.GetMseFeatureSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMseFeatureSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMseFeatureSwitch',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMseFeatureSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mse_feature_switch(
        self,
        request: main_models.GetMseFeatureSwitchRequest,
    ) -> main_models.GetMseFeatureSwitchResponse:
        runtime = RuntimeOptions()
        return self.get_mse_feature_switch_with_options(request, runtime)

    async def get_mse_feature_switch_async(
        self,
        request: main_models.GetMseFeatureSwitchRequest,
    ) -> main_models.GetMseFeatureSwitchResponse:
        runtime = RuntimeOptions()
        return await self.get_mse_feature_switch_with_options_async(request, runtime)

    def get_mse_source_with_options(
        self,
        request: main_models.GetMseSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMseSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMseSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mse_source_with_options_async(
        self,
        request: main_models.GetMseSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMseSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMseSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMseSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mse_source(
        self,
        request: main_models.GetMseSourceRequest,
    ) -> main_models.GetMseSourceResponse:
        runtime = RuntimeOptions()
        return self.get_mse_source_with_options(request, runtime)

    async def get_mse_source_async(
        self,
        request: main_models.GetMseSourceRequest,
    ) -> main_models.GetMseSourceResponse:
        runtime = RuntimeOptions()
        return await self.get_mse_source_with_options_async(request, runtime)

    def get_nacos_config_with_options(
        self,
        request: main_models.GetNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.beta):
            query['Beta'] = request.beta
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nacos_config_with_options_async(
        self,
        request: main_models.GetNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.beta):
            query['Beta'] = request.beta
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nacos_config(
        self,
        request: main_models.GetNacosConfigRequest,
    ) -> main_models.GetNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.get_nacos_config_with_options(request, runtime)

    async def get_nacos_config_async(
        self,
        request: main_models.GetNacosConfigRequest,
    ) -> main_models.GetNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_nacos_config_with_options_async(request, runtime)

    def get_nacos_history_config_with_options(
        self,
        request: main_models.GetNacosHistoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNacosHistoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.nid):
            query['Nid'] = request.nid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNacosHistoryConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNacosHistoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nacos_history_config_with_options_async(
        self,
        request: main_models.GetNacosHistoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNacosHistoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.nid):
            query['Nid'] = request.nid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNacosHistoryConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNacosHistoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nacos_history_config(
        self,
        request: main_models.GetNacosHistoryConfigRequest,
    ) -> main_models.GetNacosHistoryConfigResponse:
        runtime = RuntimeOptions()
        return self.get_nacos_history_config_with_options(request, runtime)

    async def get_nacos_history_config_async(
        self,
        request: main_models.GetNacosHistoryConfigRequest,
    ) -> main_models.GetNacosHistoryConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_nacos_history_config_with_options_async(request, runtime)

    def get_nacos_mcp_server_with_options(
        self,
        request: main_models.GetNacosMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNacosMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.mcp_server_version):
            query['McpServerVersion'] = request.mcp_server_version
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNacosMcpServer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNacosMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nacos_mcp_server_with_options_async(
        self,
        request: main_models.GetNacosMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNacosMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.mcp_server_version):
            query['McpServerVersion'] = request.mcp_server_version
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNacosMcpServer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNacosMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nacos_mcp_server(
        self,
        request: main_models.GetNacosMcpServerRequest,
    ) -> main_models.GetNacosMcpServerResponse:
        runtime = RuntimeOptions()
        return self.get_nacos_mcp_server_with_options(request, runtime)

    async def get_nacos_mcp_server_async(
        self,
        request: main_models.GetNacosMcpServerRequest,
    ) -> main_models.GetNacosMcpServerResponse:
        runtime = RuntimeOptions()
        return await self.get_nacos_mcp_server_with_options_async(request, runtime)

    def get_overview_with_options(
        self,
        request: main_models.GetOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOverview',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_overview_with_options_async(
        self,
        request: main_models.GetOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOverview',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_overview(
        self,
        request: main_models.GetOverviewRequest,
    ) -> main_models.GetOverviewResponse:
        runtime = RuntimeOptions()
        return self.get_overview_with_options(request, runtime)

    async def get_overview_async(
        self,
        request: main_models.GetOverviewRequest,
    ) -> main_models.GetOverviewResponse:
        runtime = RuntimeOptions()
        return await self.get_overview_with_options_async(request, runtime)

    def get_plugin_config_with_options(
        self,
        request: main_models.GetPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugin_config_with_options_async(
        self,
        request: main_models.GetPluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugin_config(
        self,
        request: main_models.GetPluginConfigRequest,
    ) -> main_models.GetPluginConfigResponse:
        runtime = RuntimeOptions()
        return self.get_plugin_config_with_options(request, runtime)

    async def get_plugin_config_async(
        self,
        request: main_models.GetPluginConfigRequest,
    ) -> main_models.GetPluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_plugin_config_with_options_async(request, runtime)

    def get_plugins_with_options(
        self,
        request: main_models.GetPluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.enable_only):
            query['EnableOnly'] = request.enable_only
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPlugins',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugins_with_options_async(
        self,
        request: main_models.GetPluginsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.enable_only):
            query['EnableOnly'] = request.enable_only
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPlugins',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugins(
        self,
        request: main_models.GetPluginsRequest,
    ) -> main_models.GetPluginsResponse:
        runtime = RuntimeOptions()
        return self.get_plugins_with_options(request, runtime)

    async def get_plugins_async(
        self,
        request: main_models.GetPluginsRequest,
    ) -> main_models.GetPluginsResponse:
        runtime = RuntimeOptions()
        return await self.get_plugins_with_options_async(request, runtime)

    def get_service_list_with_options(
        self,
        request: main_models.GetServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_list_with_options_async(
        self,
        request: main_models.GetServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_list(
        self,
        request: main_models.GetServiceListRequest,
    ) -> main_models.GetServiceListResponse:
        runtime = RuntimeOptions()
        return self.get_service_list_with_options(request, runtime)

    async def get_service_list_async(
        self,
        request: main_models.GetServiceListRequest,
    ) -> main_models.GetServiceListResponse:
        runtime = RuntimeOptions()
        return await self.get_service_list_with_options_async(request, runtime)

    def get_service_list_page_with_options(
        self,
        request: main_models.GetServiceListPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceListPage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_list_page_with_options_async(
        self,
        request: main_models.GetServiceListPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceListPage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_list_page(
        self,
        request: main_models.GetServiceListPageRequest,
    ) -> main_models.GetServiceListPageResponse:
        runtime = RuntimeOptions()
        return self.get_service_list_page_with_options(request, runtime)

    async def get_service_list_page_async(
        self,
        request: main_models.GetServiceListPageRequest,
    ) -> main_models.GetServiceListPageResponse:
        runtime = RuntimeOptions()
        return await self.get_service_list_page_with_options_async(request, runtime)

    def get_service_listeners_with_options(
        self,
        request: main_models.GetServiceListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListenersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.has_ip_count):
            query['HasIpCount'] = request.has_ip_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceListeners',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_listeners_with_options_async(
        self,
        request: main_models.GetServiceListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListenersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.has_ip_count):
            query['HasIpCount'] = request.has_ip_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceListeners',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_listeners(
        self,
        request: main_models.GetServiceListenersRequest,
    ) -> main_models.GetServiceListenersResponse:
        runtime = RuntimeOptions()
        return self.get_service_listeners_with_options(request, runtime)

    async def get_service_listeners_async(
        self,
        request: main_models.GetServiceListenersRequest,
    ) -> main_models.GetServiceListenersResponse:
        runtime = RuntimeOptions()
        return await self.get_service_listeners_with_options_async(request, runtime)

    def get_service_method_page_with_options(
        self,
        request: main_models.GetServiceMethodPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceMethodPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.method_controller):
            query['MethodController'] = request.method_controller
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceMethodPage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceMethodPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_method_page_with_options_async(
        self,
        request: main_models.GetServiceMethodPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceMethodPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.method_controller):
            query['MethodController'] = request.method_controller
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceMethodPage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceMethodPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_method_page(
        self,
        request: main_models.GetServiceMethodPageRequest,
    ) -> main_models.GetServiceMethodPageResponse:
        runtime = RuntimeOptions()
        return self.get_service_method_page_with_options(request, runtime)

    async def get_service_method_page_async(
        self,
        request: main_models.GetServiceMethodPageRequest,
    ) -> main_models.GetServiceMethodPageResponse:
        runtime = RuntimeOptions()
        return await self.get_service_method_page_with_options_async(request, runtime)

    def get_tags_by_swimming_lane_group_id_with_options(
        self,
        request: main_models.GetTagsBySwimmingLaneGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTagsBySwimmingLaneGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTagsBySwimmingLaneGroupId',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTagsBySwimmingLaneGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tags_by_swimming_lane_group_id_with_options_async(
        self,
        request: main_models.GetTagsBySwimmingLaneGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTagsBySwimmingLaneGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTagsBySwimmingLaneGroupId',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTagsBySwimmingLaneGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tags_by_swimming_lane_group_id(
        self,
        request: main_models.GetTagsBySwimmingLaneGroupIdRequest,
    ) -> main_models.GetTagsBySwimmingLaneGroupIdResponse:
        runtime = RuntimeOptions()
        return self.get_tags_by_swimming_lane_group_id_with_options(request, runtime)

    async def get_tags_by_swimming_lane_group_id_async(
        self,
        request: main_models.GetTagsBySwimmingLaneGroupIdRequest,
    ) -> main_models.GetTagsBySwimmingLaneGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.get_tags_by_swimming_lane_group_id_with_options_async(request, runtime)

    def get_zookeeper_data_import_url_with_options(
        self,
        request: main_models.GetZookeeperDataImportUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetZookeeperDataImportUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetZookeeperDataImportUrl',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetZookeeperDataImportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_zookeeper_data_import_url_with_options_async(
        self,
        request: main_models.GetZookeeperDataImportUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetZookeeperDataImportUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetZookeeperDataImportUrl',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetZookeeperDataImportUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_zookeeper_data_import_url(
        self,
        request: main_models.GetZookeeperDataImportUrlRequest,
    ) -> main_models.GetZookeeperDataImportUrlResponse:
        runtime = RuntimeOptions()
        return self.get_zookeeper_data_import_url_with_options(request, runtime)

    async def get_zookeeper_data_import_url_async(
        self,
        request: main_models.GetZookeeperDataImportUrlRequest,
    ) -> main_models.GetZookeeperDataImportUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_zookeeper_data_import_url_with_options_async(request, runtime)

    def import_nacos_config_with_options(
        self,
        request: main_models.ImportNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_nacos_config_with_options_async(
        self,
        request: main_models.ImportNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_nacos_config(
        self,
        request: main_models.ImportNacosConfigRequest,
    ) -> main_models.ImportNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.import_nacos_config_with_options(request, runtime)

    async def import_nacos_config_async(
        self,
        request: main_models.ImportNacosConfigRequest,
    ) -> main_models.ImportNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.import_nacos_config_with_options_async(request, runtime)

    def import_services_with_options(
        self,
        tmp_req: main_models.ImportServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportServicesResponse:
        tmp_req.validate()
        request = main_models.ImportServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.service_list):
            request.service_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.service_list, 'ServiceList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.fc_alias):
            query['FcAlias'] = request.fc_alias
        if not DaraCore.is_null(request.fc_service_name):
            query['FcServiceName'] = request.fc_service_name
        if not DaraCore.is_null(request.fc_version):
            query['FcVersion'] = request.fc_version
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_list_shrink):
            query['ServiceList'] = request.service_list_shrink
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.tls_setting):
            query['TlsSetting'] = request.tls_setting
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_services_with_options_async(
        self,
        tmp_req: main_models.ImportServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportServicesResponse:
        tmp_req.validate()
        request = main_models.ImportServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.service_list):
            request.service_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.service_list, 'ServiceList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.fc_alias):
            query['FcAlias'] = request.fc_alias
        if not DaraCore.is_null(request.fc_service_name):
            query['FcServiceName'] = request.fc_service_name
        if not DaraCore.is_null(request.fc_version):
            query['FcVersion'] = request.fc_version
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_list_shrink):
            query['ServiceList'] = request.service_list_shrink
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.tls_setting):
            query['TlsSetting'] = request.tls_setting
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_services(
        self,
        request: main_models.ImportServicesRequest,
    ) -> main_models.ImportServicesResponse:
        runtime = RuntimeOptions()
        return self.import_services_with_options(request, runtime)

    async def import_services_async(
        self,
        request: main_models.ImportServicesRequest,
    ) -> main_models.ImportServicesResponse:
        runtime = RuntimeOptions()
        return await self.import_services_with_options_async(request, runtime)

    def import_zookeeper_data_with_options(
        self,
        request: main_models.ImportZookeeperDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportZookeeperDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportZookeeperData',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportZookeeperDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_zookeeper_data_with_options_async(
        self,
        request: main_models.ImportZookeeperDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportZookeeperDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportZookeeperData',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportZookeeperDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_zookeeper_data(
        self,
        request: main_models.ImportZookeeperDataRequest,
    ) -> main_models.ImportZookeeperDataResponse:
        runtime = RuntimeOptions()
        return self.import_zookeeper_data_with_options(request, runtime)

    async def import_zookeeper_data_async(
        self,
        request: main_models.ImportZookeeperDataRequest,
    ) -> main_models.ImportZookeeperDataResponse:
        runtime = RuntimeOptions()
        return await self.import_zookeeper_data_with_options_async(request, runtime)

    def initialize_service_link_role_with_options(
        self,
        request: main_models.InitializeServiceLinkRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeServiceLinkRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitializeServiceLinkRole',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeServiceLinkRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_service_link_role_with_options_async(
        self,
        request: main_models.InitializeServiceLinkRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeServiceLinkRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitializeServiceLinkRole',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeServiceLinkRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_service_link_role(
        self,
        request: main_models.InitializeServiceLinkRoleRequest,
    ) -> main_models.InitializeServiceLinkRoleResponse:
        runtime = RuntimeOptions()
        return self.initialize_service_link_role_with_options(request, runtime)

    async def initialize_service_link_role_async(
        self,
        request: main_models.InitializeServiceLinkRoleRequest,
    ) -> main_models.InitializeServiceLinkRoleResponse:
        runtime = RuntimeOptions()
        return await self.initialize_service_link_role_with_options_async(request, runtime)

    def list_ans_instances_with_options(
        self,
        request: main_models.ListAnsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnsInstances',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ans_instances_with_options_async(
        self,
        request: main_models.ListAnsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnsInstances',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ans_instances(
        self,
        request: main_models.ListAnsInstancesRequest,
    ) -> main_models.ListAnsInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_ans_instances_with_options(request, runtime)

    async def list_ans_instances_async(
        self,
        request: main_models.ListAnsInstancesRequest,
    ) -> main_models.ListAnsInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_ans_instances_with_options_async(request, runtime)

    def list_ans_service_clusters_with_options(
        self,
        request: main_models.ListAnsServiceClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnsServiceClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnsServiceClusters',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnsServiceClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ans_service_clusters_with_options_async(
        self,
        request: main_models.ListAnsServiceClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnsServiceClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnsServiceClusters',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnsServiceClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ans_service_clusters(
        self,
        request: main_models.ListAnsServiceClustersRequest,
    ) -> main_models.ListAnsServiceClustersResponse:
        runtime = RuntimeOptions()
        return self.list_ans_service_clusters_with_options(request, runtime)

    async def list_ans_service_clusters_async(
        self,
        request: main_models.ListAnsServiceClustersRequest,
    ) -> main_models.ListAnsServiceClustersResponse:
        runtime = RuntimeOptions()
        return await self.list_ans_service_clusters_with_options_async(request, runtime)

    def list_ans_services_with_options(
        self,
        request: main_models.ListAnsServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnsServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.has_ip_count):
            query['HasIpCount'] = request.has_ip_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnsServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnsServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ans_services_with_options_async(
        self,
        request: main_models.ListAnsServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnsServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.has_ip_count):
            query['HasIpCount'] = request.has_ip_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnsServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnsServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ans_services(
        self,
        request: main_models.ListAnsServicesRequest,
    ) -> main_models.ListAnsServicesResponse:
        runtime = RuntimeOptions()
        return self.list_ans_services_with_options(request, runtime)

    async def list_ans_services_async(
        self,
        request: main_models.ListAnsServicesRequest,
    ) -> main_models.ListAnsServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_ans_services_with_options_async(request, runtime)

    def list_app_by_swimming_lane_group_tag_with_options(
        self,
        request: main_models.ListAppBySwimmingLaneGroupTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppBySwimmingLaneGroupTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppBySwimmingLaneGroupTag',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppBySwimmingLaneGroupTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_by_swimming_lane_group_tag_with_options_async(
        self,
        request: main_models.ListAppBySwimmingLaneGroupTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppBySwimmingLaneGroupTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppBySwimmingLaneGroupTag',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppBySwimmingLaneGroupTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_by_swimming_lane_group_tag(
        self,
        request: main_models.ListAppBySwimmingLaneGroupTagRequest,
    ) -> main_models.ListAppBySwimmingLaneGroupTagResponse:
        runtime = RuntimeOptions()
        return self.list_app_by_swimming_lane_group_tag_with_options(request, runtime)

    async def list_app_by_swimming_lane_group_tag_async(
        self,
        request: main_models.ListAppBySwimmingLaneGroupTagRequest,
    ) -> main_models.ListAppBySwimmingLaneGroupTagResponse:
        runtime = RuntimeOptions()
        return await self.list_app_by_swimming_lane_group_tag_with_options_async(request, runtime)

    def list_app_by_swimming_lane_group_tags_with_options(
        self,
        tmp_req: main_models.ListAppBySwimmingLaneGroupTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppBySwimmingLaneGroupTagsResponse:
        tmp_req.validate()
        request = main_models.ListAppBySwimmingLaneGroupTagsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppBySwimmingLaneGroupTags',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppBySwimmingLaneGroupTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_by_swimming_lane_group_tags_with_options_async(
        self,
        tmp_req: main_models.ListAppBySwimmingLaneGroupTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppBySwimmingLaneGroupTagsResponse:
        tmp_req.validate()
        request = main_models.ListAppBySwimmingLaneGroupTagsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppBySwimmingLaneGroupTags',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppBySwimmingLaneGroupTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_by_swimming_lane_group_tags(
        self,
        request: main_models.ListAppBySwimmingLaneGroupTagsRequest,
    ) -> main_models.ListAppBySwimmingLaneGroupTagsResponse:
        runtime = RuntimeOptions()
        return self.list_app_by_swimming_lane_group_tags_with_options(request, runtime)

    async def list_app_by_swimming_lane_group_tags_async(
        self,
        request: main_models.ListAppBySwimmingLaneGroupTagsRequest,
    ) -> main_models.ListAppBySwimmingLaneGroupTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_by_swimming_lane_group_tags_with_options_async(request, runtime)

    def list_applications_with_tag_rules_with_options(
        self,
        request: main_models.ListApplicationsWithTagRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsWithTagRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsWithTagRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsWithTagRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_tag_rules_with_options_async(
        self,
        request: main_models.ListApplicationsWithTagRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsWithTagRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsWithTagRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsWithTagRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_with_tag_rules(
        self,
        request: main_models.ListApplicationsWithTagRulesRequest,
    ) -> main_models.ListApplicationsWithTagRulesResponse:
        runtime = RuntimeOptions()
        return self.list_applications_with_tag_rules_with_options(request, runtime)

    async def list_applications_with_tag_rules_async(
        self,
        request: main_models.ListApplicationsWithTagRulesRequest,
    ) -> main_models.ListApplicationsWithTagRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_with_tag_rules_with_options_async(request, runtime)

    def list_auth_policy_with_options(
        self,
        request: main_models.ListAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auth_policy_with_options_async(
        self,
        request: main_models.ListAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auth_policy(
        self,
        request: main_models.ListAuthPolicyRequest,
    ) -> main_models.ListAuthPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_auth_policy_with_options(request, runtime)

    async def list_auth_policy_async(
        self,
        request: main_models.ListAuthPolicyRequest,
    ) -> main_models.ListAuthPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_auth_policy_with_options_async(request, runtime)

    def list_circuit_breaker_rules_with_options(
        self,
        request: main_models.ListCircuitBreakerRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCircuitBreakerRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCircuitBreakerRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCircuitBreakerRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_circuit_breaker_rules_with_options_async(
        self,
        request: main_models.ListCircuitBreakerRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCircuitBreakerRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCircuitBreakerRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCircuitBreakerRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_circuit_breaker_rules(
        self,
        request: main_models.ListCircuitBreakerRulesRequest,
    ) -> main_models.ListCircuitBreakerRulesResponse:
        runtime = RuntimeOptions()
        return self.list_circuit_breaker_rules_with_options(request, runtime)

    async def list_circuit_breaker_rules_async(
        self,
        request: main_models.ListCircuitBreakerRulesRequest,
    ) -> main_models.ListCircuitBreakerRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_circuit_breaker_rules_with_options_async(request, runtime)

    def list_cluster_connection_types_with_options(
        self,
        request: main_models.ListClusterConnectionTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterConnectionTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterConnectionTypes',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterConnectionTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_connection_types_with_options_async(
        self,
        request: main_models.ListClusterConnectionTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterConnectionTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterConnectionTypes',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterConnectionTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_connection_types(
        self,
        request: main_models.ListClusterConnectionTypesRequest,
    ) -> main_models.ListClusterConnectionTypesResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_connection_types_with_options(request, runtime)

    async def list_cluster_connection_types_async(
        self,
        request: main_models.ListClusterConnectionTypesRequest,
    ) -> main_models.ListClusterConnectionTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_connection_types_with_options_async(request, runtime)

    def list_cluster_health_check_task_with_options(
        self,
        request: main_models.ListClusterHealthCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterHealthCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterHealthCheckTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterHealthCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_health_check_task_with_options_async(
        self,
        request: main_models.ListClusterHealthCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterHealthCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterHealthCheckTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterHealthCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_health_check_task(
        self,
        request: main_models.ListClusterHealthCheckTaskRequest,
    ) -> main_models.ListClusterHealthCheckTaskResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_health_check_task_with_options(request, runtime)

    async def list_cluster_health_check_task_async(
        self,
        request: main_models.ListClusterHealthCheckTaskRequest,
    ) -> main_models.ListClusterHealthCheckTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_health_check_task_with_options_async(request, runtime)

    def list_cluster_types_with_options(
        self,
        request: main_models.ListClusterTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterTypes',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_types_with_options_async(
        self,
        request: main_models.ListClusterTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterTypes',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_types(
        self,
        request: main_models.ListClusterTypesRequest,
    ) -> main_models.ListClusterTypesResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_types_with_options(request, runtime)

    async def list_cluster_types_async(
        self,
        request: main_models.ListClusterTypesRequest,
    ) -> main_models.ListClusterTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_types_with_options_async(request, runtime)

    def list_cluster_versions_with_options(
        self,
        request: main_models.ListClusterVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterVersions',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_versions_with_options_async(
        self,
        request: main_models.ListClusterVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterVersions',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_versions(
        self,
        request: main_models.ListClusterVersionsRequest,
    ) -> main_models.ListClusterVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_versions_with_options(request, runtime)

    async def list_cluster_versions_async(
        self,
        request: main_models.ListClusterVersionsRequest,
    ) -> main_models.ListClusterVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_versions_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_alias_name):
            query['ClusterAliasName'] = request.cluster_alias_name
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_alias_name):
            query['ClusterAliasName'] = request.cluster_alias_name
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_config_track_with_options(
        self,
        request: main_models.ListConfigTrackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigTrackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigTrack',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigTrackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_track_with_options_async(
        self,
        request: main_models.ListConfigTrackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigTrackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigTrack',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigTrackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_track(
        self,
        request: main_models.ListConfigTrackRequest,
    ) -> main_models.ListConfigTrackResponse:
        runtime = RuntimeOptions()
        return self.list_config_track_with_options(request, runtime)

    async def list_config_track_async(
        self,
        request: main_models.ListConfigTrackRequest,
    ) -> main_models.ListConfigTrackResponse:
        runtime = RuntimeOptions()
        return await self.list_config_track_with_options_async(request, runtime)

    def list_engine_namespaces_with_options(
        self,
        request: main_models.ListEngineNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEngineNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEngineNamespaces',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEngineNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_namespaces_with_options_async(
        self,
        request: main_models.ListEngineNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEngineNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEngineNamespaces',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEngineNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_namespaces(
        self,
        request: main_models.ListEngineNamespacesRequest,
    ) -> main_models.ListEngineNamespacesResponse:
        runtime = RuntimeOptions()
        return self.list_engine_namespaces_with_options(request, runtime)

    async def list_engine_namespaces_async(
        self,
        request: main_models.ListEngineNamespacesRequest,
    ) -> main_models.ListEngineNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.list_engine_namespaces_with_options_async(request, runtime)

    def list_eureka_instances_with_options(
        self,
        request: main_models.ListEurekaInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEurekaInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEurekaInstances',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEurekaInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eureka_instances_with_options_async(
        self,
        request: main_models.ListEurekaInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEurekaInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEurekaInstances',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEurekaInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eureka_instances(
        self,
        request: main_models.ListEurekaInstancesRequest,
    ) -> main_models.ListEurekaInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_eureka_instances_with_options(request, runtime)

    async def list_eureka_instances_async(
        self,
        request: main_models.ListEurekaInstancesRequest,
    ) -> main_models.ListEurekaInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_eureka_instances_with_options_async(request, runtime)

    def list_eureka_services_with_options(
        self,
        request: main_models.ListEurekaServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEurekaServicesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEurekaServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEurekaServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eureka_services_with_options_async(
        self,
        request: main_models.ListEurekaServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEurekaServicesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEurekaServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEurekaServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eureka_services(
        self,
        request: main_models.ListEurekaServicesRequest,
    ) -> main_models.ListEurekaServicesResponse:
        runtime = RuntimeOptions()
        return self.list_eureka_services_with_options(request, runtime)

    async def list_eureka_services_async(
        self,
        request: main_models.ListEurekaServicesRequest,
    ) -> main_models.ListEurekaServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_eureka_services_with_options_async(request, runtime)

    def list_export_zookeeper_data_with_options(
        self,
        request: main_models.ListExportZookeeperDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExportZookeeperDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExportZookeeperData',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExportZookeeperDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_export_zookeeper_data_with_options_async(
        self,
        request: main_models.ListExportZookeeperDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExportZookeeperDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExportZookeeperData',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExportZookeeperDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_export_zookeeper_data(
        self,
        request: main_models.ListExportZookeeperDataRequest,
    ) -> main_models.ListExportZookeeperDataResponse:
        runtime = RuntimeOptions()
        return self.list_export_zookeeper_data_with_options(request, runtime)

    async def list_export_zookeeper_data_async(
        self,
        request: main_models.ListExportZookeeperDataRequest,
    ) -> main_models.ListExportZookeeperDataResponse:
        runtime = RuntimeOptions()
        return await self.list_export_zookeeper_data_with_options_async(request, runtime)

    def list_flow_rules_with_options(
        self,
        request: main_models.ListFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_rules_with_options_async(
        self,
        request: main_models.ListFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_rules(
        self,
        request: main_models.ListFlowRulesRequest,
    ) -> main_models.ListFlowRulesResponse:
        runtime = RuntimeOptions()
        return self.list_flow_rules_with_options(request, runtime)

    async def list_flow_rules_async(
        self,
        request: main_models.ListFlowRulesRequest,
    ) -> main_models.ListFlowRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_flow_rules_with_options_async(request, runtime)

    def list_gateway_with_options(
        self,
        tmp_req: main_models.ListGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayResponse:
        tmp_req.validate()
        request = main_models.ListGatewayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_with_options_async(
        self,
        tmp_req: main_models.ListGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayResponse:
        tmp_req.validate()
        request = main_models.ListGatewayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateway',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway(
        self,
        request: main_models.ListGatewayRequest,
    ) -> main_models.ListGatewayResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_with_options(request, runtime)

    async def list_gateway_async(
        self,
        request: main_models.ListGatewayRequest,
    ) -> main_models.ListGatewayResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_with_options_async(request, runtime)

    def list_gateway_auth_with_options(
        self,
        tmp_req: main_models.ListGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthResponse:
        tmp_req.validate()
        request = main_models.ListGatewayAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_auth_with_options_async(
        self,
        tmp_req: main_models.ListGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthResponse:
        tmp_req.validate()
        request = main_models.ListGatewayAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_auth(
        self,
        request: main_models.ListGatewayAuthRequest,
    ) -> main_models.ListGatewayAuthResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_auth_with_options(request, runtime)

    async def list_gateway_auth_async(
        self,
        request: main_models.ListGatewayAuthRequest,
    ) -> main_models.ListGatewayAuthResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_auth_with_options_async(request, runtime)

    def list_gateway_auth_consumer_with_options(
        self,
        request: main_models.ListGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_status):
            query['ConsumerStatus'] = request.consumer_status
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_auth_consumer_with_options_async(
        self,
        request: main_models.ListGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_status):
            query['ConsumerStatus'] = request.consumer_status
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_auth_consumer(
        self,
        request: main_models.ListGatewayAuthConsumerRequest,
    ) -> main_models.ListGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_auth_consumer_with_options(request, runtime)

    async def list_gateway_auth_consumer_async(
        self,
        request: main_models.ListGatewayAuthConsumerRequest,
    ) -> main_models.ListGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_auth_consumer_with_options_async(request, runtime)

    def list_gateway_auth_consumer_resource_with_options(
        self,
        request: main_models.ListGatewayAuthConsumerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthConsumerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_status):
            query['ResourceStatus'] = request.resource_status
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthConsumerResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthConsumerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_auth_consumer_resource_with_options_async(
        self,
        request: main_models.ListGatewayAuthConsumerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthConsumerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_status):
            query['ResourceStatus'] = request.resource_status
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthConsumerResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthConsumerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_auth_consumer_resource(
        self,
        request: main_models.ListGatewayAuthConsumerResourceRequest,
    ) -> main_models.ListGatewayAuthConsumerResourceResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_auth_consumer_resource_with_options(request, runtime)

    async def list_gateway_auth_consumer_resource_async(
        self,
        request: main_models.ListGatewayAuthConsumerResourceRequest,
    ) -> main_models.ListGatewayAuthConsumerResourceResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_auth_consumer_resource_with_options_async(request, runtime)

    def list_gateway_circuit_breaker_rule_with_options(
        self,
        request: main_models.ListGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_params):
            query['FilterParams'] = request.filter_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayCircuitBreakerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_circuit_breaker_rule_with_options_async(
        self,
        request: main_models.ListGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_params):
            query['FilterParams'] = request.filter_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayCircuitBreakerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_circuit_breaker_rule(
        self,
        request: main_models.ListGatewayCircuitBreakerRuleRequest,
    ) -> main_models.ListGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_circuit_breaker_rule_with_options(request, runtime)

    async def list_gateway_circuit_breaker_rule_async(
        self,
        request: main_models.ListGatewayCircuitBreakerRuleRequest,
    ) -> main_models.ListGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_circuit_breaker_rule_with_options_async(request, runtime)

    def list_gateway_domain_with_options(
        self,
        request: main_models.ListGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_domain_with_options_async(
        self,
        request: main_models.ListGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_domain(
        self,
        request: main_models.ListGatewayDomainRequest,
    ) -> main_models.ListGatewayDomainResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_domain_with_options(request, runtime)

    async def list_gateway_domain_async(
        self,
        request: main_models.ListGatewayDomainRequest,
    ) -> main_models.ListGatewayDomainResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_domain_with_options_async(request, runtime)

    def list_gateway_flow_rule_with_options(
        self,
        request: main_models.ListGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_params):
            query['FilterParams'] = request.filter_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_flow_rule_with_options_async(
        self,
        request: main_models.ListGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_params):
            query['FilterParams'] = request.filter_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_flow_rule(
        self,
        request: main_models.ListGatewayFlowRuleRequest,
    ) -> main_models.ListGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_flow_rule_with_options(request, runtime)

    async def list_gateway_flow_rule_async(
        self,
        request: main_models.ListGatewayFlowRuleRequest,
    ) -> main_models.ListGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_flow_rule_with_options_async(request, runtime)

    def list_gateway_isolation_rule_with_options(
        self,
        request: main_models.ListGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_params):
            query['FilterParams'] = request.filter_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIsolationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_isolation_rule_with_options_async(
        self,
        request: main_models.ListGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_params):
            query['FilterParams'] = request.filter_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayIsolationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_isolation_rule(
        self,
        request: main_models.ListGatewayIsolationRuleRequest,
    ) -> main_models.ListGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_isolation_rule_with_options(request, runtime)

    async def list_gateway_isolation_rule_async(
        self,
        request: main_models.ListGatewayIsolationRuleRequest,
    ) -> main_models.ListGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_isolation_rule_with_options_async(request, runtime)

    def list_gateway_route_with_options(
        self,
        tmp_req: main_models.ListGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayRouteResponse:
        tmp_req.validate()
        request = main_models.ListGatewayRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_route_with_options_async(
        self,
        tmp_req: main_models.ListGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayRouteResponse:
        tmp_req.validate()
        request = main_models.ListGatewayRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_route(
        self,
        request: main_models.ListGatewayRouteRequest,
    ) -> main_models.ListGatewayRouteResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_route_with_options(request, runtime)

    async def list_gateway_route_async(
        self,
        request: main_models.ListGatewayRouteRequest,
    ) -> main_models.ListGatewayRouteResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_route_with_options_async(request, runtime)

    def list_gateway_route_on_auth_with_options(
        self,
        request: main_models.ListGatewayRouteOnAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayRouteOnAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayRouteOnAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayRouteOnAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_route_on_auth_with_options_async(
        self,
        request: main_models.ListGatewayRouteOnAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayRouteOnAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayRouteOnAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayRouteOnAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_route_on_auth(
        self,
        request: main_models.ListGatewayRouteOnAuthRequest,
    ) -> main_models.ListGatewayRouteOnAuthResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_route_on_auth_with_options(request, runtime)

    async def list_gateway_route_on_auth_async(
        self,
        request: main_models.ListGatewayRouteOnAuthRequest,
    ) -> main_models.ListGatewayRouteOnAuthResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_route_on_auth_with_options_async(request, runtime)

    def list_gateway_service_with_options(
        self,
        tmp_req: main_models.ListGatewayServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayServiceResponse:
        tmp_req.validate()
        request = main_models.ListGatewayServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_service_with_options_async(
        self,
        tmp_req: main_models.ListGatewayServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayServiceResponse:
        tmp_req.validate()
        request = main_models.ListGatewayServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_params):
            request.filter_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not DaraCore.is_null(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not DaraCore.is_null(request.order_item):
            query['OrderItem'] = request.order_item
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_service(
        self,
        request: main_models.ListGatewayServiceRequest,
    ) -> main_models.ListGatewayServiceResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_service_with_options(request, runtime)

    async def list_gateway_service_async(
        self,
        request: main_models.ListGatewayServiceRequest,
    ) -> main_models.ListGatewayServiceResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_service_with_options_async(request, runtime)

    def list_gateway_slb_with_options(
        self,
        request: main_models.ListGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewaySlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_slb_with_options_async(
        self,
        request: main_models.ListGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewaySlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewaySlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_slb(
        self,
        request: main_models.ListGatewaySlbRequest,
    ) -> main_models.ListGatewaySlbResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_slb_with_options(request, runtime)

    async def list_gateway_slb_async(
        self,
        request: main_models.ListGatewaySlbRequest,
    ) -> main_models.ListGatewaySlbResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_slb_with_options_async(request, runtime)

    def list_gateway_zone_with_options(
        self,
        request: main_models.ListGatewayZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayZone',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_zone_with_options_async(
        self,
        request: main_models.ListGatewayZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayZone',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_zone(
        self,
        request: main_models.ListGatewayZoneRequest,
    ) -> main_models.ListGatewayZoneResponse:
        runtime = RuntimeOptions()
        return self.list_gateway_zone_with_options(request, runtime)

    async def list_gateway_zone_async(
        self,
        request: main_models.ListGatewayZoneRequest,
    ) -> main_models.ListGatewayZoneResponse:
        runtime = RuntimeOptions()
        return await self.list_gateway_zone_with_options_async(request, runtime)

    def list_instance_count_with_options(
        self,
        request: main_models.ListInstanceCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceCount',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_count_with_options_async(
        self,
        request: main_models.ListInstanceCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceCount',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_count(
        self,
        request: main_models.ListInstanceCountRequest,
    ) -> main_models.ListInstanceCountResponse:
        runtime = RuntimeOptions()
        return self.list_instance_count_with_options(request, runtime)

    async def list_instance_count_async(
        self,
        request: main_models.ListInstanceCountRequest,
    ) -> main_models.ListInstanceCountResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_count_with_options_async(request, runtime)

    def list_isolation_rules_with_options(
        self,
        request: main_models.ListIsolationRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIsolationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIsolationRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIsolationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_isolation_rules_with_options_async(
        self,
        request: main_models.ListIsolationRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIsolationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIsolationRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIsolationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_isolation_rules(
        self,
        request: main_models.ListIsolationRulesRequest,
    ) -> main_models.ListIsolationRulesResponse:
        runtime = RuntimeOptions()
        return self.list_isolation_rules_with_options(request, runtime)

    async def list_isolation_rules_async(
        self,
        request: main_models.ListIsolationRulesRequest,
    ) -> main_models.ListIsolationRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_isolation_rules_with_options_async(request, runtime)

    def list_listeners_by_config_with_options(
        self,
        tmp_req: main_models.ListListenersByConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersByConfigResponse:
        tmp_req.validate()
        request = main_models.ListListenersByConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext_gray_rules):
            request.ext_gray_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext_gray_rules, 'ExtGrayRules', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.ext_gray_rules_shrink):
            query['ExtGrayRules'] = request.ext_gray_rules_shrink
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenersByConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenersByConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_by_config_with_options_async(
        self,
        tmp_req: main_models.ListListenersByConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersByConfigResponse:
        tmp_req.validate()
        request = main_models.ListListenersByConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext_gray_rules):
            request.ext_gray_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext_gray_rules, 'ExtGrayRules', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.ext_gray_rules_shrink):
            query['ExtGrayRules'] = request.ext_gray_rules_shrink
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenersByConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenersByConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners_by_config(
        self,
        request: main_models.ListListenersByConfigRequest,
    ) -> main_models.ListListenersByConfigResponse:
        runtime = RuntimeOptions()
        return self.list_listeners_by_config_with_options(request, runtime)

    async def list_listeners_by_config_async(
        self,
        request: main_models.ListListenersByConfigRequest,
    ) -> main_models.ListListenersByConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_listeners_by_config_with_options_async(request, runtime)

    def list_listeners_by_ip_with_options(
        self,
        request: main_models.ListListenersByIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersByIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenersByIp',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenersByIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_by_ip_with_options_async(
        self,
        request: main_models.ListListenersByIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersByIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenersByIp',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenersByIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners_by_ip(
        self,
        request: main_models.ListListenersByIpRequest,
    ) -> main_models.ListListenersByIpResponse:
        runtime = RuntimeOptions()
        return self.list_listeners_by_ip_with_options(request, runtime)

    async def list_listeners_by_ip_async(
        self,
        request: main_models.ListListenersByIpRequest,
    ) -> main_models.ListListenersByIpResponse:
        runtime = RuntimeOptions()
        return await self.list_listeners_by_ip_with_options_async(request, runtime)

    def list_migration_task_with_options(
        self,
        request: main_models.ListMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_migration_task_with_options_async(
        self,
        request: main_models.ListMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_migration_task(
        self,
        request: main_models.ListMigrationTaskRequest,
    ) -> main_models.ListMigrationTaskResponse:
        runtime = RuntimeOptions()
        return self.list_migration_task_with_options(request, runtime)

    async def list_migration_task_async(
        self,
        request: main_models.ListMigrationTaskRequest,
    ) -> main_models.ListMigrationTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_migration_task_with_options_async(request, runtime)

    def list_nacos_configs_with_options(
        self,
        request: main_models.ListNacosConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacosConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacosConfigs',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacosConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nacos_configs_with_options_async(
        self,
        request: main_models.ListNacosConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacosConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacosConfigs',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacosConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nacos_configs(
        self,
        request: main_models.ListNacosConfigsRequest,
    ) -> main_models.ListNacosConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_nacos_configs_with_options(request, runtime)

    async def list_nacos_configs_async(
        self,
        request: main_models.ListNacosConfigsRequest,
    ) -> main_models.ListNacosConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_nacos_configs_with_options_async(request, runtime)

    def list_nacos_history_configs_with_options(
        self,
        request: main_models.ListNacosHistoryConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacosHistoryConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacosHistoryConfigs',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacosHistoryConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nacos_history_configs_with_options_async(
        self,
        request: main_models.ListNacosHistoryConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacosHistoryConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacosHistoryConfigs',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacosHistoryConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nacos_history_configs(
        self,
        request: main_models.ListNacosHistoryConfigsRequest,
    ) -> main_models.ListNacosHistoryConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_nacos_history_configs_with_options(request, runtime)

    async def list_nacos_history_configs_async(
        self,
        request: main_models.ListNacosHistoryConfigsRequest,
    ) -> main_models.ListNacosHistoryConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_nacos_history_configs_with_options_async(request, runtime)

    def list_nacos_mcp_servers_with_options(
        self,
        request: main_models.ListNacosMcpServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacosMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacosMcpServers',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacosMcpServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nacos_mcp_servers_with_options_async(
        self,
        request: main_models.ListNacosMcpServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacosMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacosMcpServers',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacosMcpServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nacos_mcp_servers(
        self,
        request: main_models.ListNacosMcpServersRequest,
    ) -> main_models.ListNacosMcpServersResponse:
        runtime = RuntimeOptions()
        return self.list_nacos_mcp_servers_with_options(request, runtime)

    async def list_nacos_mcp_servers_async(
        self,
        request: main_models.ListNacosMcpServersRequest,
    ) -> main_models.ListNacosMcpServersResponse:
        runtime = RuntimeOptions()
        return await self.list_nacos_mcp_servers_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        tmp_req: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        tmp_req.validate()
        request = main_models.ListNamespacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        tmp_req: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        tmp_req.validate()
        request = main_models.ListNamespacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_naming_track_with_options(
        self,
        request: main_models.ListNamingTrackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamingTrackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamingTrack',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamingTrackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_naming_track_with_options_async(
        self,
        request: main_models.ListNamingTrackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamingTrackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamingTrack',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamingTrackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_naming_track(
        self,
        request: main_models.ListNamingTrackRequest,
    ) -> main_models.ListNamingTrackResponse:
        runtime = RuntimeOptions()
        return self.list_naming_track_with_options(request, runtime)

    async def list_naming_track_async(
        self,
        request: main_models.ListNamingTrackRequest,
    ) -> main_models.ListNamingTrackResponse:
        runtime = RuntimeOptions()
        return await self.list_naming_track_with_options_async(request, runtime)

    def list_sslcert_with_options(
        self,
        request: main_models.ListSSLCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSSLCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSSLCert',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSSLCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sslcert_with_options_async(
        self,
        request: main_models.ListSSLCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSSLCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSSLCert',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSSLCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sslcert(
        self,
        request: main_models.ListSSLCertRequest,
    ) -> main_models.ListSSLCertResponse:
        runtime = RuntimeOptions()
        return self.list_sslcert_with_options(request, runtime)

    async def list_sslcert_async(
        self,
        request: main_models.ListSSLCertRequest,
    ) -> main_models.ListSSLCertResponse:
        runtime = RuntimeOptions()
        return await self.list_sslcert_with_options_async(request, runtime)

    def list_security_group_with_options(
        self,
        request: main_models.ListSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_group_with_options_async(
        self,
        request: main_models.ListSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_group(
        self,
        request: main_models.ListSecurityGroupRequest,
    ) -> main_models.ListSecurityGroupResponse:
        runtime = RuntimeOptions()
        return self.list_security_group_with_options(request, runtime)

    async def list_security_group_async(
        self,
        request: main_models.ListSecurityGroupRequest,
    ) -> main_models.ListSecurityGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_security_group_with_options_async(request, runtime)

    def list_security_group_rule_with_options(
        self,
        request: main_models.ListSecurityGroupRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityGroupRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_group_rule_with_options_async(
        self,
        request: main_models.ListSecurityGroupRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityGroupRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_group_rule(
        self,
        request: main_models.ListSecurityGroupRuleRequest,
    ) -> main_models.ListSecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        return self.list_security_group_rule_with_options(request, runtime)

    async def list_security_group_rule_async(
        self,
        request: main_models.ListSecurityGroupRuleRequest,
    ) -> main_models.ListSecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_security_group_rule_with_options_async(request, runtime)

    def list_sentinel_block_fallback_definitions_with_options(
        self,
        tmp_req: main_models.ListSentinelBlockFallbackDefinitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSentinelBlockFallbackDefinitionsResponse:
        tmp_req.validate()
        request = main_models.ListSentinelBlockFallbackDefinitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.classification_set):
            request.classification_set_shrink = Utils.array_to_string_with_specified_style(tmp_req.classification_set, 'ClassificationSet', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.classification_set_shrink):
            query['ClassificationSet'] = request.classification_set_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSentinelBlockFallbackDefinitions',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSentinelBlockFallbackDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sentinel_block_fallback_definitions_with_options_async(
        self,
        tmp_req: main_models.ListSentinelBlockFallbackDefinitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSentinelBlockFallbackDefinitionsResponse:
        tmp_req.validate()
        request = main_models.ListSentinelBlockFallbackDefinitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.classification_set):
            request.classification_set_shrink = Utils.array_to_string_with_specified_style(tmp_req.classification_set, 'ClassificationSet', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.classification_set_shrink):
            query['ClassificationSet'] = request.classification_set_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSentinelBlockFallbackDefinitions',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSentinelBlockFallbackDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sentinel_block_fallback_definitions(
        self,
        request: main_models.ListSentinelBlockFallbackDefinitionsRequest,
    ) -> main_models.ListSentinelBlockFallbackDefinitionsResponse:
        runtime = RuntimeOptions()
        return self.list_sentinel_block_fallback_definitions_with_options(request, runtime)

    async def list_sentinel_block_fallback_definitions_async(
        self,
        request: main_models.ListSentinelBlockFallbackDefinitionsRequest,
    ) -> main_models.ListSentinelBlockFallbackDefinitionsResponse:
        runtime = RuntimeOptions()
        return await self.list_sentinel_block_fallback_definitions_with_options_async(request, runtime)

    def list_service_source_with_options(
        self,
        request: main_models.ListServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_source_with_options_async(
        self,
        request: main_models.ListServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_source(
        self,
        request: main_models.ListServiceSourceRequest,
    ) -> main_models.ListServiceSourceResponse:
        runtime = RuntimeOptions()
        return self.list_service_source_with_options(request, runtime)

    async def list_service_source_async(
        self,
        request: main_models.ListServiceSourceRequest,
    ) -> main_models.ListServiceSourceResponse:
        runtime = RuntimeOptions()
        return await self.list_service_source_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version = '2019-05-31',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version = '2019-05-31',
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

    def list_web_flow_rules_with_options(
        self,
        request: main_models.ListWebFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWebFlowRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebFlowRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_flow_rules_with_options_async(
        self,
        request: main_models.ListWebFlowRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWebFlowRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_search_key):
            query['ResourceSearchKey'] = request.resource_search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebFlowRules',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebFlowRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_flow_rules(
        self,
        request: main_models.ListWebFlowRulesRequest,
    ) -> main_models.ListWebFlowRulesResponse:
        runtime = RuntimeOptions()
        return self.list_web_flow_rules_with_options(request, runtime)

    async def list_web_flow_rules_async(
        self,
        request: main_models.ListWebFlowRulesRequest,
    ) -> main_models.ListWebFlowRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_web_flow_rules_with_options_async(request, runtime)

    def list_zk_track_with_options(
        self,
        request: main_models.ListZkTrackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListZkTrackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListZkTrack',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZkTrackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zk_track_with_options_async(
        self,
        request: main_models.ListZkTrackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListZkTrackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListZkTrack',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZkTrackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zk_track(
        self,
        request: main_models.ListZkTrackRequest,
    ) -> main_models.ListZkTrackResponse:
        runtime = RuntimeOptions()
        return self.list_zk_track_with_options(request, runtime)

    async def list_zk_track_async(
        self,
        request: main_models.ListZkTrackRequest,
    ) -> main_models.ListZkTrackResponse:
        runtime = RuntimeOptions()
        return await self.list_zk_track_with_options_async(request, runtime)

    def list_znode_children_with_options(
        self,
        request: main_models.ListZnodeChildrenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListZnodeChildrenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListZnodeChildren',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZnodeChildrenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_znode_children_with_options_async(
        self,
        request: main_models.ListZnodeChildrenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListZnodeChildrenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListZnodeChildren',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZnodeChildrenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_znode_children(
        self,
        request: main_models.ListZnodeChildrenRequest,
    ) -> main_models.ListZnodeChildrenResponse:
        runtime = RuntimeOptions()
        return self.list_znode_children_with_options(request, runtime)

    async def list_znode_children_async(
        self,
        request: main_models.ListZnodeChildrenRequest,
    ) -> main_models.ListZnodeChildrenResponse:
        runtime = RuntimeOptions()
        return await self.list_znode_children_with_options_async(request, runtime)

    def modify_governance_kubernetes_cluster_with_options(
        self,
        tmp_req: main_models.ModifyGovernanceKubernetesClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGovernanceKubernetesClusterResponse:
        tmp_req.validate()
        request = main_models.ModifyGovernanceKubernetesClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespace_infos):
            request.namespace_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespace_infos, 'NamespaceInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.namespace_infos_shrink):
            body['NamespaceInfos'] = request.namespace_infos_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGovernanceKubernetesCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_governance_kubernetes_cluster_with_options_async(
        self,
        tmp_req: main_models.ModifyGovernanceKubernetesClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGovernanceKubernetesClusterResponse:
        tmp_req.validate()
        request = main_models.ModifyGovernanceKubernetesClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespace_infos):
            request.namespace_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespace_infos, 'NamespaceInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.namespace_infos_shrink):
            body['NamespaceInfos'] = request.namespace_infos_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGovernanceKubernetesCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGovernanceKubernetesClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_governance_kubernetes_cluster(
        self,
        request: main_models.ModifyGovernanceKubernetesClusterRequest,
    ) -> main_models.ModifyGovernanceKubernetesClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_governance_kubernetes_cluster_with_options(request, runtime)

    async def modify_governance_kubernetes_cluster_async(
        self,
        request: main_models.ModifyGovernanceKubernetesClusterRequest,
    ) -> main_models.ModifyGovernanceKubernetesClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_governance_kubernetes_cluster_with_options_async(request, runtime)

    def modify_lossless_rule_with_options(
        self,
        request: main_models.ModifyLosslessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLosslessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.aligned):
            query['Aligned'] = request.aligned
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.delay_time):
            query['DelayTime'] = request.delay_time
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.func_type):
            query['FuncType'] = request.func_type
        if not DaraCore.is_null(request.loss_less_detail):
            query['LossLessDetail'] = request.loss_less_detail
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.notice):
            query['Notice'] = request.notice
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.related):
            query['Related'] = request.related
        if not DaraCore.is_null(request.warmup_time):
            query['WarmupTime'] = request.warmup_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLosslessRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLosslessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lossless_rule_with_options_async(
        self,
        request: main_models.ModifyLosslessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLosslessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.aligned):
            query['Aligned'] = request.aligned
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.delay_time):
            query['DelayTime'] = request.delay_time
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.func_type):
            query['FuncType'] = request.func_type
        if not DaraCore.is_null(request.loss_less_detail):
            query['LossLessDetail'] = request.loss_less_detail
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.notice):
            query['Notice'] = request.notice
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.related):
            query['Related'] = request.related
        if not DaraCore.is_null(request.warmup_time):
            query['WarmupTime'] = request.warmup_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLosslessRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLosslessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lossless_rule(
        self,
        request: main_models.ModifyLosslessRuleRequest,
    ) -> main_models.ModifyLosslessRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_lossless_rule_with_options(request, runtime)

    async def modify_lossless_rule_async(
        self,
        request: main_models.ModifyLosslessRuleRequest,
    ) -> main_models.ModifyLosslessRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_lossless_rule_with_options_async(request, runtime)

    def offline_gateway_route_with_options(
        self,
        request: main_models.OfflineGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineGatewayRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_gateway_route_with_options_async(
        self,
        request: main_models.OfflineGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineGatewayRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_gateway_route(
        self,
        request: main_models.OfflineGatewayRouteRequest,
    ) -> main_models.OfflineGatewayRouteResponse:
        runtime = RuntimeOptions()
        return self.offline_gateway_route_with_options(request, runtime)

    async def offline_gateway_route_async(
        self,
        request: main_models.OfflineGatewayRouteRequest,
    ) -> main_models.OfflineGatewayRouteResponse:
        runtime = RuntimeOptions()
        return await self.offline_gateway_route_with_options_async(request, runtime)

    def order_cluster_health_check_risk_notice_with_options(
        self,
        request: main_models.OrderClusterHealthCheckRiskNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OrderClusterHealthCheckRiskNoticeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mute):
            query['Mute'] = request.mute
        if not DaraCore.is_null(request.notice_type):
            query['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.risk_code):
            query['RiskCode'] = request.risk_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OrderClusterHealthCheckRiskNotice',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OrderClusterHealthCheckRiskNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_cluster_health_check_risk_notice_with_options_async(
        self,
        request: main_models.OrderClusterHealthCheckRiskNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OrderClusterHealthCheckRiskNoticeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mute):
            query['Mute'] = request.mute
        if not DaraCore.is_null(request.notice_type):
            query['NoticeType'] = request.notice_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.risk_code):
            query['RiskCode'] = request.risk_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OrderClusterHealthCheckRiskNotice',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OrderClusterHealthCheckRiskNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_cluster_health_check_risk_notice(
        self,
        request: main_models.OrderClusterHealthCheckRiskNoticeRequest,
    ) -> main_models.OrderClusterHealthCheckRiskNoticeResponse:
        runtime = RuntimeOptions()
        return self.order_cluster_health_check_risk_notice_with_options(request, runtime)

    async def order_cluster_health_check_risk_notice_async(
        self,
        request: main_models.OrderClusterHealthCheckRiskNoticeRequest,
    ) -> main_models.OrderClusterHealthCheckRiskNoticeResponse:
        runtime = RuntimeOptions()
        return await self.order_cluster_health_check_risk_notice_with_options_async(request, runtime)

    def preserve_header_format_with_options(
        self,
        request: main_models.PreserveHeaderFormatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreserveHeaderFormatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.preserve_header_format):
            query['PreserveHeaderFormat'] = request.preserve_header_format
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreserveHeaderFormat',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreserveHeaderFormatResponse(),
            self.call_api(params, req, runtime)
        )

    async def preserve_header_format_with_options_async(
        self,
        request: main_models.PreserveHeaderFormatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreserveHeaderFormatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.preserve_header_format):
            query['PreserveHeaderFormat'] = request.preserve_header_format
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreserveHeaderFormat',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreserveHeaderFormatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preserve_header_format(
        self,
        request: main_models.PreserveHeaderFormatRequest,
    ) -> main_models.PreserveHeaderFormatResponse:
        runtime = RuntimeOptions()
        return self.preserve_header_format_with_options(request, runtime)

    async def preserve_header_format_async(
        self,
        request: main_models.PreserveHeaderFormatRequest,
    ) -> main_models.PreserveHeaderFormatResponse:
        runtime = RuntimeOptions()
        return await self.preserve_header_format_with_options_async(request, runtime)

    def pull_services_with_options(
        self,
        request: main_models.PullServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PullServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PullServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PullServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def pull_services_with_options_async(
        self,
        request: main_models.PullServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PullServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PullServices',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PullServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pull_services(
        self,
        request: main_models.PullServicesRequest,
    ) -> main_models.PullServicesResponse:
        runtime = RuntimeOptions()
        return self.pull_services_with_options(request, runtime)

    async def pull_services_async(
        self,
        request: main_models.PullServicesRequest,
    ) -> main_models.PullServicesResponse:
        runtime = RuntimeOptions()
        return await self.pull_services_with_options_async(request, runtime)

    def put_cluster_health_check_task_with_options(
        self,
        request: main_models.PutClusterHealthCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutClusterHealthCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutClusterHealthCheckTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutClusterHealthCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_cluster_health_check_task_with_options_async(
        self,
        request: main_models.PutClusterHealthCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutClusterHealthCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutClusterHealthCheckTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutClusterHealthCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_cluster_health_check_task(
        self,
        request: main_models.PutClusterHealthCheckTaskRequest,
    ) -> main_models.PutClusterHealthCheckTaskResponse:
        runtime = RuntimeOptions()
        return self.put_cluster_health_check_task_with_options(request, runtime)

    async def put_cluster_health_check_task_async(
        self,
        request: main_models.PutClusterHealthCheckTaskRequest,
    ) -> main_models.PutClusterHealthCheckTaskResponse:
        runtime = RuntimeOptions()
        return await self.put_cluster_health_check_task_with_options_async(request, runtime)

    def query_all_swimming_lane_with_options(
        self,
        request: main_models.QueryAllSwimmingLaneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAllSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAllSwimmingLane',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAllSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_all_swimming_lane_with_options_async(
        self,
        request: main_models.QueryAllSwimmingLaneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAllSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAllSwimmingLane',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAllSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_all_swimming_lane(
        self,
        request: main_models.QueryAllSwimmingLaneRequest,
    ) -> main_models.QueryAllSwimmingLaneResponse:
        runtime = RuntimeOptions()
        return self.query_all_swimming_lane_with_options(request, runtime)

    async def query_all_swimming_lane_async(
        self,
        request: main_models.QueryAllSwimmingLaneRequest,
    ) -> main_models.QueryAllSwimmingLaneResponse:
        runtime = RuntimeOptions()
        return await self.query_all_swimming_lane_with_options_async(request, runtime)

    def query_all_swimming_lane_group_with_options(
        self,
        request: main_models.QueryAllSwimmingLaneGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAllSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAllSwimmingLaneGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAllSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_all_swimming_lane_group_with_options_async(
        self,
        request: main_models.QueryAllSwimmingLaneGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAllSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAllSwimmingLaneGroup',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAllSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_all_swimming_lane_group(
        self,
        request: main_models.QueryAllSwimmingLaneGroupRequest,
    ) -> main_models.QueryAllSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        return self.query_all_swimming_lane_group_with_options(request, runtime)

    async def query_all_swimming_lane_group_async(
        self,
        request: main_models.QueryAllSwimmingLaneGroupRequest,
    ) -> main_models.QueryAllSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        return await self.query_all_swimming_lane_group_with_options_async(request, runtime)

    def query_business_locations_with_options(
        self,
        request: main_models.QueryBusinessLocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBusinessLocationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBusinessLocations',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBusinessLocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_business_locations_with_options_async(
        self,
        request: main_models.QueryBusinessLocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBusinessLocationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBusinessLocations',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBusinessLocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_business_locations(
        self,
        request: main_models.QueryBusinessLocationsRequest,
    ) -> main_models.QueryBusinessLocationsResponse:
        runtime = RuntimeOptions()
        return self.query_business_locations_with_options(request, runtime)

    async def query_business_locations_async(
        self,
        request: main_models.QueryBusinessLocationsRequest,
    ) -> main_models.QueryBusinessLocationsResponse:
        runtime = RuntimeOptions()
        return await self.query_business_locations_with_options_async(request, runtime)

    def query_cluster_detail_with_options(
        self,
        request: main_models.QueryClusterDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.acl_switch):
            query['AclSwitch'] = request.acl_switch
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_detail_with_options_async(
        self,
        request: main_models.QueryClusterDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.acl_switch):
            query['AclSwitch'] = request.acl_switch
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_detail(
        self,
        request: main_models.QueryClusterDetailRequest,
    ) -> main_models.QueryClusterDetailResponse:
        runtime = RuntimeOptions()
        return self.query_cluster_detail_with_options(request, runtime)

    async def query_cluster_detail_async(
        self,
        request: main_models.QueryClusterDetailRequest,
    ) -> main_models.QueryClusterDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_cluster_detail_with_options_async(request, runtime)

    def query_cluster_disk_specification_with_options(
        self,
        request: main_models.QueryClusterDiskSpecificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterDiskSpecificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterDiskSpecification',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterDiskSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_disk_specification_with_options_async(
        self,
        request: main_models.QueryClusterDiskSpecificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterDiskSpecificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterDiskSpecification',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterDiskSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_disk_specification(
        self,
        request: main_models.QueryClusterDiskSpecificationRequest,
    ) -> main_models.QueryClusterDiskSpecificationResponse:
        runtime = RuntimeOptions()
        return self.query_cluster_disk_specification_with_options(request, runtime)

    async def query_cluster_disk_specification_async(
        self,
        request: main_models.QueryClusterDiskSpecificationRequest,
    ) -> main_models.QueryClusterDiskSpecificationResponse:
        runtime = RuntimeOptions()
        return await self.query_cluster_disk_specification_with_options_async(request, runtime)

    def query_cluster_info_with_options(
        self,
        request: main_models.QueryClusterInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.acl_switch):
            query['AclSwitch'] = request.acl_switch
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterInfo',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_info_with_options_async(
        self,
        request: main_models.QueryClusterInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.acl_switch):
            query['AclSwitch'] = request.acl_switch
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterInfo',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_info(
        self,
        request: main_models.QueryClusterInfoRequest,
    ) -> main_models.QueryClusterInfoResponse:
        runtime = RuntimeOptions()
        return self.query_cluster_info_with_options(request, runtime)

    async def query_cluster_info_async(
        self,
        request: main_models.QueryClusterInfoRequest,
    ) -> main_models.QueryClusterInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_cluster_info_with_options_async(request, runtime)

    def query_cluster_specification_with_options(
        self,
        request: main_models.QueryClusterSpecificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterSpecificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterSpecification',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_specification_with_options_async(
        self,
        request: main_models.QueryClusterSpecificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryClusterSpecificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryClusterSpecification',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryClusterSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_specification(
        self,
        request: main_models.QueryClusterSpecificationRequest,
    ) -> main_models.QueryClusterSpecificationResponse:
        runtime = RuntimeOptions()
        return self.query_cluster_specification_with_options(request, runtime)

    async def query_cluster_specification_async(
        self,
        request: main_models.QueryClusterSpecificationRequest,
    ) -> main_models.QueryClusterSpecificationResponse:
        runtime = RuntimeOptions()
        return await self.query_cluster_specification_with_options_async(request, runtime)

    def query_config_with_options(
        self,
        request: main_models.QueryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_running_conf):
            query['NeedRunningConf'] = request.need_running_conf
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_config_with_options_async(
        self,
        request: main_models.QueryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_running_conf):
            query['NeedRunningConf'] = request.need_running_conf
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_config(
        self,
        request: main_models.QueryConfigRequest,
    ) -> main_models.QueryConfigResponse:
        runtime = RuntimeOptions()
        return self.query_config_with_options(request, runtime)

    async def query_config_async(
        self,
        request: main_models.QueryConfigRequest,
    ) -> main_models.QueryConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_config_with_options_async(request, runtime)

    def query_gateway_region_with_options(
        self,
        request: main_models.QueryGatewayRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGatewayRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGatewayRegion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGatewayRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gateway_region_with_options_async(
        self,
        request: main_models.QueryGatewayRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGatewayRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGatewayRegion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGatewayRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gateway_region(
        self,
        request: main_models.QueryGatewayRegionRequest,
    ) -> main_models.QueryGatewayRegionResponse:
        runtime = RuntimeOptions()
        return self.query_gateway_region_with_options(request, runtime)

    async def query_gateway_region_async(
        self,
        request: main_models.QueryGatewayRegionRequest,
    ) -> main_models.QueryGatewayRegionResponse:
        runtime = RuntimeOptions()
        return await self.query_gateway_region_with_options_async(request, runtime)

    def query_gateway_type_with_options(
        self,
        request: main_models.QueryGatewayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGatewayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGatewayType',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGatewayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gateway_type_with_options_async(
        self,
        request: main_models.QueryGatewayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGatewayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGatewayType',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGatewayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gateway_type(
        self,
        request: main_models.QueryGatewayTypeRequest,
    ) -> main_models.QueryGatewayTypeResponse:
        runtime = RuntimeOptions()
        return self.query_gateway_type_with_options(request, runtime)

    async def query_gateway_type_async(
        self,
        request: main_models.QueryGatewayTypeRequest,
    ) -> main_models.QueryGatewayTypeResponse:
        runtime = RuntimeOptions()
        return await self.query_gateway_type_with_options_async(request, runtime)

    def query_governance_kubernetes_cluster_with_options(
        self,
        request: main_models.QueryGovernanceKubernetesClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGovernanceKubernetesClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGovernanceKubernetesCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_governance_kubernetes_cluster_with_options_async(
        self,
        request: main_models.QueryGovernanceKubernetesClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGovernanceKubernetesClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGovernanceKubernetesCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGovernanceKubernetesClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_governance_kubernetes_cluster(
        self,
        request: main_models.QueryGovernanceKubernetesClusterRequest,
    ) -> main_models.QueryGovernanceKubernetesClusterResponse:
        runtime = RuntimeOptions()
        return self.query_governance_kubernetes_cluster_with_options(request, runtime)

    async def query_governance_kubernetes_cluster_async(
        self,
        request: main_models.QueryGovernanceKubernetesClusterRequest,
    ) -> main_models.QueryGovernanceKubernetesClusterResponse:
        runtime = RuntimeOptions()
        return await self.query_governance_kubernetes_cluster_with_options_async(request, runtime)

    def query_instances_info_with_options(
        self,
        request: main_models.QueryInstancesInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstancesInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstancesInfo',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstancesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instances_info_with_options_async(
        self,
        request: main_models.QueryInstancesInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstancesInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstancesInfo',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstancesInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instances_info(
        self,
        request: main_models.QueryInstancesInfoRequest,
    ) -> main_models.QueryInstancesInfoResponse:
        runtime = RuntimeOptions()
        return self.query_instances_info_with_options(request, runtime)

    async def query_instances_info_async(
        self,
        request: main_models.QueryInstancesInfoRequest,
    ) -> main_models.QueryInstancesInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_instances_info_with_options_async(request, runtime)

    def query_monitor_with_options(
        self,
        request: main_models.QueryMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.monitor_type):
            query['MonitorType'] = request.monitor_type
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.step):
            query['Step'] = request.step
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMonitor',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monitor_with_options_async(
        self,
        request: main_models.QueryMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.monitor_type):
            query['MonitorType'] = request.monitor_type
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.step):
            query['Step'] = request.step
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMonitor',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monitor(
        self,
        request: main_models.QueryMonitorRequest,
    ) -> main_models.QueryMonitorResponse:
        runtime = RuntimeOptions()
        return self.query_monitor_with_options(request, runtime)

    async def query_monitor_async(
        self,
        request: main_models.QueryMonitorRequest,
    ) -> main_models.QueryMonitorResponse:
        runtime = RuntimeOptions()
        return await self.query_monitor_with_options_async(request, runtime)

    def query_nacos_gray_config_with_options(
        self,
        request: main_models.QueryNacosGrayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryNacosGrayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.gray_name):
            query['GrayName'] = request.gray_name
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryNacosGrayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryNacosGrayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_nacos_gray_config_with_options_async(
        self,
        request: main_models.QueryNacosGrayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryNacosGrayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.gray_name):
            query['GrayName'] = request.gray_name
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryNacosGrayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryNacosGrayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_nacos_gray_config(
        self,
        request: main_models.QueryNacosGrayConfigRequest,
    ) -> main_models.QueryNacosGrayConfigResponse:
        runtime = RuntimeOptions()
        return self.query_nacos_gray_config_with_options(request, runtime)

    async def query_nacos_gray_config_async(
        self,
        request: main_models.QueryNacosGrayConfigRequest,
    ) -> main_models.QueryNacosGrayConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_nacos_gray_config_with_options_async(request, runtime)

    def query_namespace_with_options(
        self,
        request: main_models.QueryNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_namespace_with_options_async(
        self,
        request: main_models.QueryNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_namespace(
        self,
        request: main_models.QueryNamespaceRequest,
    ) -> main_models.QueryNamespaceResponse:
        runtime = RuntimeOptions()
        return self.query_namespace_with_options(request, runtime)

    async def query_namespace_async(
        self,
        request: main_models.QueryNamespaceRequest,
    ) -> main_models.QueryNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.query_namespace_with_options_async(request, runtime)

    def query_slb_spec_with_options(
        self,
        request: main_models.QuerySlbSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySlbSpecResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySlbSpec',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySlbSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_slb_spec_with_options_async(
        self,
        request: main_models.QuerySlbSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySlbSpecResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySlbSpec',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySlbSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_slb_spec(
        self,
        request: main_models.QuerySlbSpecRequest,
    ) -> main_models.QuerySlbSpecResponse:
        runtime = RuntimeOptions()
        return self.query_slb_spec_with_options(request, runtime)

    async def query_slb_spec_async(
        self,
        request: main_models.QuerySlbSpecRequest,
    ) -> main_models.QuerySlbSpecResponse:
        runtime = RuntimeOptions()
        return await self.query_slb_spec_with_options_async(request, runtime)

    def query_swimming_lane_by_id_with_options(
        self,
        request: main_models.QuerySwimmingLaneByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySwimmingLaneByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySwimmingLaneById',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySwimmingLaneByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_swimming_lane_by_id_with_options_async(
        self,
        request: main_models.QuerySwimmingLaneByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySwimmingLaneByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySwimmingLaneById',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySwimmingLaneByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_swimming_lane_by_id(
        self,
        request: main_models.QuerySwimmingLaneByIdRequest,
    ) -> main_models.QuerySwimmingLaneByIdResponse:
        runtime = RuntimeOptions()
        return self.query_swimming_lane_by_id_with_options(request, runtime)

    async def query_swimming_lane_by_id_async(
        self,
        request: main_models.QuerySwimmingLaneByIdRequest,
    ) -> main_models.QuerySwimmingLaneByIdResponse:
        runtime = RuntimeOptions()
        return await self.query_swimming_lane_by_id_with_options_async(request, runtime)

    def query_znode_detail_with_options(
        self,
        request: main_models.QueryZnodeDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryZnodeDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryZnodeDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryZnodeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_znode_detail_with_options_async(
        self,
        request: main_models.QueryZnodeDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryZnodeDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryZnodeDetail',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryZnodeDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_znode_detail(
        self,
        request: main_models.QueryZnodeDetailRequest,
    ) -> main_models.QueryZnodeDetailResponse:
        runtime = RuntimeOptions()
        return self.query_znode_detail_with_options(request, runtime)

    async def query_znode_detail_async(
        self,
        request: main_models.QueryZnodeDetailRequest,
    ) -> main_models.QueryZnodeDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_znode_detail_with_options_async(request, runtime)

    def remove_application_with_options(
        self,
        request: main_models.RemoveApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApplication',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_application_with_options_async(
        self,
        request: main_models.RemoveApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApplication',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_application(
        self,
        request: main_models.RemoveApplicationRequest,
    ) -> main_models.RemoveApplicationResponse:
        runtime = RuntimeOptions()
        return self.remove_application_with_options(request, runtime)

    async def remove_application_async(
        self,
        request: main_models.RemoveApplicationRequest,
    ) -> main_models.RemoveApplicationResponse:
        runtime = RuntimeOptions()
        return await self.remove_application_with_options_async(request, runtime)

    def remove_auth_policy_with_options(
        self,
        request: main_models.RemoveAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAuthPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_auth_policy_with_options_async(
        self,
        request: main_models.RemoveAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAuthPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_auth_policy(
        self,
        request: main_models.RemoveAuthPolicyRequest,
    ) -> main_models.RemoveAuthPolicyResponse:
        runtime = RuntimeOptions()
        return self.remove_auth_policy_with_options(request, runtime)

    async def remove_auth_policy_async(
        self,
        request: main_models.RemoveAuthPolicyRequest,
    ) -> main_models.RemoveAuthPolicyResponse:
        runtime = RuntimeOptions()
        return await self.remove_auth_policy_with_options_async(request, runtime)

    def restart_cluster_with_options(
        self,
        request: main_models.RestartClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pod_name_list):
            query['PodNameList'] = request.pod_name_list
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_cluster_with_options_async(
        self,
        request: main_models.RestartClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pod_name_list):
            query['PodNameList'] = request.pod_name_list
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_cluster(
        self,
        request: main_models.RestartClusterRequest,
    ) -> main_models.RestartClusterResponse:
        runtime = RuntimeOptions()
        return self.restart_cluster_with_options(request, runtime)

    async def restart_cluster_async(
        self,
        request: main_models.RestartClusterRequest,
    ) -> main_models.RestartClusterResponse:
        runtime = RuntimeOptions()
        return await self.restart_cluster_with_options_async(request, runtime)

    def retry_cluster_with_options(
        self,
        request: main_models.RetryClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_cluster_with_options_async(
        self,
        request: main_models.RetryClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_cluster(
        self,
        request: main_models.RetryClusterRequest,
    ) -> main_models.RetryClusterResponse:
        runtime = RuntimeOptions()
        return self.retry_cluster_with_options(request, runtime)

    async def retry_cluster_async(
        self,
        request: main_models.RetryClusterRequest,
    ) -> main_models.RetryClusterResponse:
        runtime = RuntimeOptions()
        return await self.retry_cluster_with_options_async(request, runtime)

    def select_gateway_slb_with_options(
        self,
        request: main_models.SelectGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SelectGatewaySlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SelectGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_gateway_slb_with_options_async(
        self,
        request: main_models.SelectGatewaySlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SelectGatewaySlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SelectGatewaySlb',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectGatewaySlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_gateway_slb(
        self,
        request: main_models.SelectGatewaySlbRequest,
    ) -> main_models.SelectGatewaySlbResponse:
        runtime = RuntimeOptions()
        return self.select_gateway_slb_with_options(request, runtime)

    async def select_gateway_slb_async(
        self,
        request: main_models.SelectGatewaySlbRequest,
    ) -> main_models.SelectGatewaySlbResponse:
        runtime = RuntimeOptions()
        return await self.select_gateway_slb_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version = '2019-05-31',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version = '2019-05-31',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version = '2019-05-31',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            version = '2019-05-31',
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

    def update_acl_with_options(
        self,
        request: main_models.UpdateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.acl_entry_list):
            query['AclEntryList'] = request.acl_entry_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcl',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_acl_with_options_async(
        self,
        request: main_models.UpdateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.acl_entry_list):
            query['AclEntryList'] = request.acl_entry_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcl',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_acl(
        self,
        request: main_models.UpdateAclRequest,
    ) -> main_models.UpdateAclResponse:
        runtime = RuntimeOptions()
        return self.update_acl_with_options(request, runtime)

    async def update_acl_async(
        self,
        request: main_models.UpdateAclRequest,
    ) -> main_models.UpdateAclResponse:
        runtime = RuntimeOptions()
        return await self.update_acl_with_options_async(request, runtime)

    def update_auth_policy_with_options(
        self,
        request: main_models.UpdateAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_rule):
            query['AuthRule'] = request.auth_rule
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.k_8s_namespace):
            query['K8sNamespace'] = request.k_8s_namespace
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuthPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auth_policy_with_options_async(
        self,
        request: main_models.UpdateAuthPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuthPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_rule):
            query['AuthRule'] = request.auth_rule
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.k_8s_namespace):
            query['K8sNamespace'] = request.k_8s_namespace
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuthPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuthPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auth_policy(
        self,
        request: main_models.UpdateAuthPolicyRequest,
    ) -> main_models.UpdateAuthPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_auth_policy_with_options(request, runtime)

    async def update_auth_policy_async(
        self,
        request: main_models.UpdateAuthPolicyRequest,
    ) -> main_models.UpdateAuthPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_auth_policy_with_options_async(request, runtime)

    def update_black_white_list_with_options(
        self,
        request: main_models.UpdateBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.resource_id_json_list):
            query['ResourceIdJsonList'] = request.resource_id_json_list
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_black_white_list_with_options_async(
        self,
        request: main_models.UpdateBlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.resource_id_json_list):
            query['ResourceIdJsonList'] = request.resource_id_json_list
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBlackWhiteList',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBlackWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_black_white_list(
        self,
        request: main_models.UpdateBlackWhiteListRequest,
    ) -> main_models.UpdateBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return self.update_black_white_list_with_options(request, runtime)

    async def update_black_white_list_async(
        self,
        request: main_models.UpdateBlackWhiteListRequest,
    ) -> main_models.UpdateBlackWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.update_black_white_list_with_options_async(request, runtime)

    def update_circuit_breaker_rule_with_options(
        self,
        request: main_models.UpdateCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.half_open_base_amount_per_step):
            query['HalfOpenBaseAmountPerStep'] = request.half_open_base_amount_per_step
        if not DaraCore.is_null(request.half_open_recovery_step_num):
            query['HalfOpenRecoveryStepNum'] = request.half_open_recovery_step_num
        if not DaraCore.is_null(request.max_allowed_rt_ms):
            query['MaxAllowedRtMs'] = request.max_allowed_rt_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.retry_timeout_ms):
            query['RetryTimeoutMs'] = request.retry_timeout_ms
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCircuitBreakerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_circuit_breaker_rule_with_options_async(
        self,
        request: main_models.UpdateCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.half_open_base_amount_per_step):
            query['HalfOpenBaseAmountPerStep'] = request.half_open_base_amount_per_step
        if not DaraCore.is_null(request.half_open_recovery_step_num):
            query['HalfOpenRecoveryStepNum'] = request.half_open_recovery_step_num
        if not DaraCore.is_null(request.max_allowed_rt_ms):
            query['MaxAllowedRtMs'] = request.max_allowed_rt_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.retry_timeout_ms):
            query['RetryTimeoutMs'] = request.retry_timeout_ms
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCircuitBreakerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_circuit_breaker_rule(
        self,
        request: main_models.UpdateCircuitBreakerRuleRequest,
    ) -> main_models.UpdateCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return self.update_circuit_breaker_rule_with_options(request, runtime)

    async def update_circuit_breaker_rule_async(
        self,
        request: main_models.UpdateCircuitBreakerRuleRequest,
    ) -> main_models.UpdateCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_circuit_breaker_rule_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        request: main_models.UpdateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_alias_name):
            query['ClusterAliasName'] = request.cluster_alias_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.maintenance_end_time):
            query['MaintenanceEndTime'] = request.maintenance_end_time
        if not DaraCore.is_null(request.maintenance_start_time):
            query['MaintenanceStartTime'] = request.maintenance_start_time
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        request: main_models.UpdateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_alias_name):
            query['ClusterAliasName'] = request.cluster_alias_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.maintenance_end_time):
            query['MaintenanceEndTime'] = request.maintenance_end_time
        if not DaraCore.is_null(request.maintenance_start_time):
            query['MaintenanceStartTime'] = request.maintenance_start_time
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster(
        self,
        request: main_models.UpdateClusterRequest,
    ) -> main_models.UpdateClusterResponse:
        runtime = RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: main_models.UpdateClusterRequest,
    ) -> main_models.UpdateClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_cluster_spec_with_options(
        self,
        request: main_models.UpdateClusterSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_specification):
            query['ClusterSpecification'] = request.cluster_specification
        if not DaraCore.is_null(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.pub_network_flow):
            query['PubNetworkFlow'] = request.pub_network_flow
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterSpec',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_spec_with_options_async(
        self,
        request: main_models.UpdateClusterSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_specification):
            query['ClusterSpecification'] = request.cluster_specification
        if not DaraCore.is_null(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not DaraCore.is_null(request.pub_network_flow):
            query['PubNetworkFlow'] = request.pub_network_flow
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterSpec',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_spec(
        self,
        request: main_models.UpdateClusterSpecRequest,
    ) -> main_models.UpdateClusterSpecResponse:
        runtime = RuntimeOptions()
        return self.update_cluster_spec_with_options(request, runtime)

    async def update_cluster_spec_async(
        self,
        request: main_models.UpdateClusterSpecRequest,
    ) -> main_models.UpdateClusterSpecResponse:
        runtime = RuntimeOptions()
        return await self.update_cluster_spec_with_options_async(request, runtime)

    def update_config_with_options(
        self,
        request: main_models.UpdateConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_enabled):
            query['AuthEnabled'] = request.auth_enabled
        if not DaraCore.is_null(request.autopurge_purge_interval):
            query['AutopurgePurgeInterval'] = request.autopurge_purge_interval
        if not DaraCore.is_null(request.autopurge_snap_retain_count):
            query['AutopurgeSnapRetainCount'] = request.autopurge_snap_retain_count
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_auth_enabled):
            query['ConfigAuthEnabled'] = request.config_auth_enabled
        if not DaraCore.is_null(request.config_secret_enabled):
            query['ConfigSecretEnabled'] = request.config_secret_enabled
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.console_uienabled):
            query['ConsoleUIEnabled'] = request.console_uienabled
        if not DaraCore.is_null(request.enable_4lw):
            query['Enable4lw'] = request.enable_4lw
        if not DaraCore.is_null(request.eureka_supported):
            query['EurekaSupported'] = request.eureka_supported
        if not DaraCore.is_null(request.extended_types_enable):
            query['ExtendedTypesEnable'] = request.extended_types_enable
        if not DaraCore.is_null(request.init_limit):
            query['InitLimit'] = request.init_limit
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.jute_maxbuffer):
            query['JuteMaxbuffer'] = request.jute_maxbuffer
        if not DaraCore.is_null(request.mcpenabled):
            query['MCPEnabled'] = request.mcpenabled
        if not DaraCore.is_null(request.max_client_cnxns):
            query['MaxClientCnxns'] = request.max_client_cnxns
        if not DaraCore.is_null(request.max_session_timeout):
            query['MaxSessionTimeout'] = request.max_session_timeout
        if not DaraCore.is_null(request.min_session_timeout):
            query['MinSessionTimeout'] = request.min_session_timeout
        if not DaraCore.is_null(request.naming_auth_enabled):
            query['NamingAuthEnabled'] = request.naming_auth_enabled
        if not DaraCore.is_null(request.pass_word):
            query['PassWord'] = request.pass_word
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.snapshot_count):
            query['SnapshotCount'] = request.snapshot_count
        if not DaraCore.is_null(request.sync_limit):
            query['SyncLimit'] = request.sync_limit
        if not DaraCore.is_null(request.tlsenabled):
            query['TLSEnabled'] = request.tlsenabled
        if not DaraCore.is_null(request.tick_time):
            query['TickTime'] = request.tick_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not DaraCore.is_null(request.open_super_acl):
            body['OpenSuperAcl'] = request.open_super_acl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        request: main_models.UpdateConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_enabled):
            query['AuthEnabled'] = request.auth_enabled
        if not DaraCore.is_null(request.autopurge_purge_interval):
            query['AutopurgePurgeInterval'] = request.autopurge_purge_interval
        if not DaraCore.is_null(request.autopurge_snap_retain_count):
            query['AutopurgeSnapRetainCount'] = request.autopurge_snap_retain_count
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_auth_enabled):
            query['ConfigAuthEnabled'] = request.config_auth_enabled
        if not DaraCore.is_null(request.config_secret_enabled):
            query['ConfigSecretEnabled'] = request.config_secret_enabled
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.console_uienabled):
            query['ConsoleUIEnabled'] = request.console_uienabled
        if not DaraCore.is_null(request.enable_4lw):
            query['Enable4lw'] = request.enable_4lw
        if not DaraCore.is_null(request.eureka_supported):
            query['EurekaSupported'] = request.eureka_supported
        if not DaraCore.is_null(request.extended_types_enable):
            query['ExtendedTypesEnable'] = request.extended_types_enable
        if not DaraCore.is_null(request.init_limit):
            query['InitLimit'] = request.init_limit
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.jute_maxbuffer):
            query['JuteMaxbuffer'] = request.jute_maxbuffer
        if not DaraCore.is_null(request.mcpenabled):
            query['MCPEnabled'] = request.mcpenabled
        if not DaraCore.is_null(request.max_client_cnxns):
            query['MaxClientCnxns'] = request.max_client_cnxns
        if not DaraCore.is_null(request.max_session_timeout):
            query['MaxSessionTimeout'] = request.max_session_timeout
        if not DaraCore.is_null(request.min_session_timeout):
            query['MinSessionTimeout'] = request.min_session_timeout
        if not DaraCore.is_null(request.naming_auth_enabled):
            query['NamingAuthEnabled'] = request.naming_auth_enabled
        if not DaraCore.is_null(request.pass_word):
            query['PassWord'] = request.pass_word
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.snapshot_count):
            query['SnapshotCount'] = request.snapshot_count
        if not DaraCore.is_null(request.sync_limit):
            query['SyncLimit'] = request.sync_limit
        if not DaraCore.is_null(request.tlsenabled):
            query['TLSEnabled'] = request.tlsenabled
        if not DaraCore.is_null(request.tick_time):
            query['TickTime'] = request.tick_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not DaraCore.is_null(request.open_super_acl):
            body['OpenSuperAcl'] = request.open_super_acl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config(
        self,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        return self.update_config_with_options(request, runtime)

    async def update_config_async(
        self,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_config_with_options_async(request, runtime)

    def update_engine_namespace_with_options(
        self,
        request: main_models.UpdateEngineNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEngineNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_count):
            query['ServiceCount'] = request.service_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEngineNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_engine_namespace_with_options_async(
        self,
        request: main_models.UpdateEngineNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEngineNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_count):
            query['ServiceCount'] = request.service_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEngineNamespace',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEngineNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_engine_namespace(
        self,
        request: main_models.UpdateEngineNamespaceRequest,
    ) -> main_models.UpdateEngineNamespaceResponse:
        runtime = RuntimeOptions()
        return self.update_engine_namespace_with_options(request, runtime)

    async def update_engine_namespace_async(
        self,
        request: main_models.UpdateEngineNamespaceRequest,
    ) -> main_models.UpdateEngineNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.update_engine_namespace_with_options_async(request, runtime)

    def update_flow_rule_with_options(
        self,
        request: main_models.UpdateFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_rule_with_options_async(
        self,
        request: main_models.UpdateFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_rule(
        self,
        request: main_models.UpdateFlowRuleRequest,
    ) -> main_models.UpdateFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.update_flow_rule_with_options(request, runtime)

    async def update_flow_rule_async(
        self,
        request: main_models.UpdateFlowRuleRequest,
    ) -> main_models.UpdateFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_flow_rule_with_options_async(request, runtime)

    def update_gateway_auth_with_options(
        self,
        tmp_req: main_models.UpdateGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_resource_list):
            request.auth_resource_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_resource_list, 'AuthResourceList', 'json')
        if not DaraCore.is_null(tmp_req.delete_resource_id_list):
            request.delete_resource_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_resource_id_list, 'DeleteResourceIdList', 'json')
        if not DaraCore.is_null(tmp_req.external_auth_zjson):
            request.external_auth_zjsonshrink = Utils.array_to_string_with_specified_style(tmp_req.external_auth_zjson, 'ExternalAuthZJSON', 'json')
        if not DaraCore.is_null(tmp_req.scopes_list):
            request.scopes_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scopes_list, 'ScopesList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_resource_config):
            query['AuthResourceConfig'] = request.auth_resource_config
        if not DaraCore.is_null(request.auth_resource_list_shrink):
            query['AuthResourceList'] = request.auth_resource_list_shrink
        if not DaraCore.is_null(request.auth_resource_mode):
            query['AuthResourceMode'] = request.auth_resource_mode
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['ClientSecret'] = request.client_secret
        if not DaraCore.is_null(request.cookie_domain):
            query['CookieDomain'] = request.cookie_domain
        if not DaraCore.is_null(request.delete_resource_id_list_shrink):
            query['DeleteResourceIdList'] = request.delete_resource_id_list_shrink
        if not DaraCore.is_null(request.external_auth_zjsonshrink):
            query['ExternalAuthZJSON'] = request.external_auth_zjsonshrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.issuer):
            query['Issuer'] = request.issuer
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.login_url):
            query['LoginUrl'] = request.login_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.redirect_url):
            query['RedirectUrl'] = request.redirect_url
        if not DaraCore.is_null(request.scopes_list_shrink):
            query['ScopesList'] = request.scopes_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub):
            query['Sub'] = request.sub
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_name_prefix):
            query['TokenNamePrefix'] = request.token_name_prefix
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_auth_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_resource_list):
            request.auth_resource_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_resource_list, 'AuthResourceList', 'json')
        if not DaraCore.is_null(tmp_req.delete_resource_id_list):
            request.delete_resource_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_resource_id_list, 'DeleteResourceIdList', 'json')
        if not DaraCore.is_null(tmp_req.external_auth_zjson):
            request.external_auth_zjsonshrink = Utils.array_to_string_with_specified_style(tmp_req.external_auth_zjson, 'ExternalAuthZJSON', 'json')
        if not DaraCore.is_null(tmp_req.scopes_list):
            request.scopes_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.scopes_list, 'ScopesList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_resource_config):
            query['AuthResourceConfig'] = request.auth_resource_config
        if not DaraCore.is_null(request.auth_resource_list_shrink):
            query['AuthResourceList'] = request.auth_resource_list_shrink
        if not DaraCore.is_null(request.auth_resource_mode):
            query['AuthResourceMode'] = request.auth_resource_mode
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['ClientSecret'] = request.client_secret
        if not DaraCore.is_null(request.cookie_domain):
            query['CookieDomain'] = request.cookie_domain
        if not DaraCore.is_null(request.delete_resource_id_list_shrink):
            query['DeleteResourceIdList'] = request.delete_resource_id_list_shrink
        if not DaraCore.is_null(request.external_auth_zjsonshrink):
            query['ExternalAuthZJSON'] = request.external_auth_zjsonshrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.is_white):
            query['IsWhite'] = request.is_white
        if not DaraCore.is_null(request.issuer):
            query['Issuer'] = request.issuer
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.login_url):
            query['LoginUrl'] = request.login_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.redirect_url):
            query['RedirectUrl'] = request.redirect_url
        if not DaraCore.is_null(request.scopes_list_shrink):
            query['ScopesList'] = request.scopes_list_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub):
            query['Sub'] = request.sub
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_name_prefix):
            query['TokenNamePrefix'] = request.token_name_prefix
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_auth(
        self,
        request: main_models.UpdateGatewayAuthRequest,
    ) -> main_models.UpdateGatewayAuthResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_auth_with_options(request, runtime)

    async def update_gateway_auth_async(
        self,
        request: main_models.UpdateGatewayAuthRequest,
    ) -> main_models.UpdateGatewayAuthResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_auth_with_options_async(request, runtime)

    def update_gateway_auth_consumer_with_options(
        self,
        request: main_models.UpdateGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.key_value):
            query['KeyValue'] = request.key_value
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.token_prefix):
            query['TokenPrefix'] = request.token_prefix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_auth_consumer_with_options_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encode_type):
            query['EncodeType'] = request.encode_type
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.jwks):
            query['Jwks'] = request.jwks
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.key_value):
            query['KeyValue'] = request.key_value
        if not DaraCore.is_null(request.token_name):
            query['TokenName'] = request.token_name
        if not DaraCore.is_null(request.token_pass):
            query['TokenPass'] = request.token_pass
        if not DaraCore.is_null(request.token_position):
            query['TokenPosition'] = request.token_position
        if not DaraCore.is_null(request.token_prefix):
            query['TokenPrefix'] = request.token_prefix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumer',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_auth_consumer(
        self,
        request: main_models.UpdateGatewayAuthConsumerRequest,
    ) -> main_models.UpdateGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_auth_consumer_with_options(request, runtime)

    async def update_gateway_auth_consumer_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerRequest,
    ) -> main_models.UpdateGatewayAuthConsumerResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_auth_consumer_with_options_async(request, runtime)

    def update_gateway_auth_consumer_resource_with_options(
        self,
        tmp_req: main_models.UpdateGatewayAuthConsumerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerResourceResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayAuthConsumerResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_list):
            request.resource_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_list, 'ResourceList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.resource_list_shrink):
            query['ResourceList'] = request.resource_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumerResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_auth_consumer_resource_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayAuthConsumerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerResourceResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayAuthConsumerResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_list):
            request.resource_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_list, 'ResourceList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.resource_list_shrink):
            query['ResourceList'] = request.resource_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumerResource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_auth_consumer_resource(
        self,
        request: main_models.UpdateGatewayAuthConsumerResourceRequest,
    ) -> main_models.UpdateGatewayAuthConsumerResourceResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_auth_consumer_resource_with_options(request, runtime)

    async def update_gateway_auth_consumer_resource_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerResourceRequest,
    ) -> main_models.UpdateGatewayAuthConsumerResourceResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_auth_consumer_resource_with_options_async(request, runtime)

    def update_gateway_auth_consumer_resource_status_with_options(
        self,
        request: main_models.UpdateGatewayAuthConsumerResourceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerResourceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id_list):
            query['IdList'] = request.id_list
        if not DaraCore.is_null(request.resource_status):
            query['ResourceStatus'] = request.resource_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumerResourceStatus',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerResourceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_auth_consumer_resource_status_with_options_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerResourceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerResourceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id_list):
            query['IdList'] = request.id_list
        if not DaraCore.is_null(request.resource_status):
            query['ResourceStatus'] = request.resource_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumerResourceStatus',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerResourceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_auth_consumer_resource_status(
        self,
        request: main_models.UpdateGatewayAuthConsumerResourceStatusRequest,
    ) -> main_models.UpdateGatewayAuthConsumerResourceStatusResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_auth_consumer_resource_status_with_options(request, runtime)

    async def update_gateway_auth_consumer_resource_status_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerResourceStatusRequest,
    ) -> main_models.UpdateGatewayAuthConsumerResourceStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_auth_consumer_resource_status_with_options_async(request, runtime)

    def update_gateway_auth_consumer_status_with_options(
        self,
        request: main_models.UpdateGatewayAuthConsumerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_status):
            query['ConsumerStatus'] = request.consumer_status
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumerStatus',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_auth_consumer_status_with_options_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayAuthConsumerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.consumer_status):
            query['ConsumerStatus'] = request.consumer_status
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayAuthConsumerStatus',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayAuthConsumerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_auth_consumer_status(
        self,
        request: main_models.UpdateGatewayAuthConsumerStatusRequest,
    ) -> main_models.UpdateGatewayAuthConsumerStatusResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_auth_consumer_status_with_options(request, runtime)

    async def update_gateway_auth_consumer_status_async(
        self,
        request: main_models.UpdateGatewayAuthConsumerStatusRequest,
    ) -> main_models.UpdateGatewayAuthConsumerStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_auth_consumer_status_with_options_async(request, runtime)

    def update_gateway_circuit_breaker_rule_with_options(
        self,
        request: main_models.UpdateGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.max_allowed_ms):
            query['MaxAllowedMs'] = request.max_allowed_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.recovery_timeout_sec):
            query['RecoveryTimeoutSec'] = request.recovery_timeout_sec
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.stat_duration_sec):
            query['StatDurationSec'] = request.stat_duration_sec
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.trigger_ratio):
            query['TriggerRatio'] = request.trigger_ratio
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayCircuitBreakerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_circuit_breaker_rule_with_options_async(
        self,
        request: main_models.UpdateGatewayCircuitBreakerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayCircuitBreakerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.max_allowed_ms):
            query['MaxAllowedMs'] = request.max_allowed_ms
        if not DaraCore.is_null(request.min_request_amount):
            query['MinRequestAmount'] = request.min_request_amount
        if not DaraCore.is_null(request.recovery_timeout_sec):
            query['RecoveryTimeoutSec'] = request.recovery_timeout_sec
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.stat_duration_sec):
            query['StatDurationSec'] = request.stat_duration_sec
        if not DaraCore.is_null(request.strategy):
            query['Strategy'] = request.strategy
        if not DaraCore.is_null(request.trigger_ratio):
            query['TriggerRatio'] = request.trigger_ratio
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayCircuitBreakerRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayCircuitBreakerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_circuit_breaker_rule(
        self,
        request: main_models.UpdateGatewayCircuitBreakerRuleRequest,
    ) -> main_models.UpdateGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_circuit_breaker_rule_with_options(request, runtime)

    async def update_gateway_circuit_breaker_rule_async(
        self,
        request: main_models.UpdateGatewayCircuitBreakerRuleRequest,
    ) -> main_models.UpdateGatewayCircuitBreakerRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_circuit_breaker_rule_with_options_async(request, runtime)

    def update_gateway_config_with_options(
        self,
        request: main_models.UpdateGatewayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_config_with_options_async(
        self,
        request: main_models.UpdateGatewayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_config(
        self,
        request: main_models.UpdateGatewayConfigRequest,
    ) -> main_models.UpdateGatewayConfigResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_config_with_options(request, runtime)

    async def update_gateway_config_async(
        self,
        request: main_models.UpdateGatewayConfigRequest,
    ) -> main_models.UpdateGatewayConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_config_with_options_async(request, runtime)

    def update_gateway_domain_with_options(
        self,
        tmp_req: main_models.UpdateGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tls_cipher_suites_config_json):
            request.tls_cipher_suites_config_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.tls_cipher_suites_config_json, 'TlsCipherSuitesConfigJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_2):
            query['Http2'] = request.http_2
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.must_https):
            query['MustHttps'] = request.must_https
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config_jsonshrink):
            query['TlsCipherSuitesConfigJSON'] = request.tls_cipher_suites_config_jsonshrink
        if not DaraCore.is_null(request.tls_max):
            query['TlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            query['TlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_domain_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayDomainResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tls_cipher_suites_config_json):
            request.tls_cipher_suites_config_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.tls_cipher_suites_config_json, 'TlsCipherSuitesConfigJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_2):
            query['Http2'] = request.http_2
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.must_https):
            query['MustHttps'] = request.must_https
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config_jsonshrink):
            query['TlsCipherSuitesConfigJSON'] = request.tls_cipher_suites_config_jsonshrink
        if not DaraCore.is_null(request.tls_max):
            query['TlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            query['TlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayDomain',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_domain(
        self,
        request: main_models.UpdateGatewayDomainRequest,
    ) -> main_models.UpdateGatewayDomainResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_domain_with_options(request, runtime)

    async def update_gateway_domain_async(
        self,
        request: main_models.UpdateGatewayDomainRequest,
    ) -> main_models.UpdateGatewayDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_domain_with_options_async(request, runtime)

    def update_gateway_flow_rule_with_options(
        self,
        request: main_models.UpdateGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_flow_rule_with_options_async(
        self,
        request: main_models.UpdateGatewayFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_flow_rule(
        self,
        request: main_models.UpdateGatewayFlowRuleRequest,
    ) -> main_models.UpdateGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_flow_rule_with_options(request, runtime)

    async def update_gateway_flow_rule_async(
        self,
        request: main_models.UpdateGatewayFlowRuleRequest,
    ) -> main_models.UpdateGatewayFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_flow_rule_with_options_async(request, runtime)

    def update_gateway_isolation_rule_with_options(
        self,
        request: main_models.UpdateGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayIsolationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_isolation_rule_with_options_async(
        self,
        request: main_models.UpdateGatewayIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.behavior_type):
            query['BehaviorType'] = request.behavior_type
        if not DaraCore.is_null(request.body_encoding):
            query['BodyEncoding'] = request.body_encoding
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.response_content_body):
            query['ResponseContentBody'] = request.response_content_body
        if not DaraCore.is_null(request.response_redirect_url):
            query['ResponseRedirectUrl'] = request.response_redirect_url
        if not DaraCore.is_null(request.response_status_code):
            query['ResponseStatusCode'] = request.response_status_code
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        if not DaraCore.is_null(request.route_name):
            query['RouteName'] = request.route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayIsolationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_isolation_rule(
        self,
        request: main_models.UpdateGatewayIsolationRuleRequest,
    ) -> main_models.UpdateGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_isolation_rule_with_options(request, runtime)

    async def update_gateway_isolation_rule_async(
        self,
        request: main_models.UpdateGatewayIsolationRuleRequest,
    ) -> main_models.UpdateGatewayIsolationRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_isolation_rule_with_options_async(request, runtime)

    def update_gateway_name_with_options(
        self,
        request: main_models.UpdateGatewayNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayName',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_name_with_options_async(
        self,
        request: main_models.UpdateGatewayNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayName',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_name(
        self,
        request: main_models.UpdateGatewayNameRequest,
    ) -> main_models.UpdateGatewayNameResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_name_with_options(request, runtime)

    async def update_gateway_name_async(
        self,
        request: main_models.UpdateGatewayNameRequest,
    ) -> main_models.UpdateGatewayNameResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_name_with_options_async(request, runtime)

    def update_gateway_option_with_options(
        self,
        tmp_req: main_models.UpdateGatewayOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayOptionResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayOptionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gateway_option):
            request.gateway_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.gateway_option, 'GatewayOption', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_option_shrink):
            query['GatewayOption'] = request.gateway_option_shrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayOption',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_option_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayOptionResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayOptionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gateway_option):
            request.gateway_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.gateway_option, 'GatewayOption', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_option_shrink):
            query['GatewayOption'] = request.gateway_option_shrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayOption',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_option(
        self,
        request: main_models.UpdateGatewayOptionRequest,
    ) -> main_models.UpdateGatewayOptionResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_option_with_options(request, runtime)

    async def update_gateway_option_async(
        self,
        request: main_models.UpdateGatewayOptionRequest,
    ) -> main_models.UpdateGatewayOptionResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_option_with_options_async(request, runtime)

    def update_gateway_route_with_options(
        self,
        tmp_req: main_models.UpdateGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.direct_response_json):
            request.direct_response_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.direct_response_json, 'DirectResponseJSON', 'json')
        if not DaraCore.is_null(tmp_req.fallback_services):
            request.fallback_services_shrink = Utils.array_to_string_with_specified_style(tmp_req.fallback_services, 'FallbackServices', 'json')
        if not DaraCore.is_null(tmp_req.predicates):
            request.predicates_shrink = Utils.array_to_string_with_specified_style(tmp_req.predicates, 'Predicates', 'json')
        if not DaraCore.is_null(tmp_req.redirect_json):
            request.redirect_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_json, 'RedirectJSON', 'json')
        if not DaraCore.is_null(tmp_req.services):
            request.services_shrink = Utils.array_to_string_with_specified_style(tmp_req.services, 'Services', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direct_response_jsonshrink):
            query['DirectResponseJSON'] = request.direct_response_jsonshrink
        if not DaraCore.is_null(request.domain_id_list_json):
            query['DomainIdListJSON'] = request.domain_id_list_json
        if not DaraCore.is_null(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not DaraCore.is_null(request.fallback):
            query['Fallback'] = request.fallback
        if not DaraCore.is_null(request.fallback_services_shrink):
            query['FallbackServices'] = request.fallback_services_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.predicates_shrink):
            query['Predicates'] = request.predicates_shrink
        if not DaraCore.is_null(request.redirect_jsonshrink):
            query['RedirectJSON'] = request.redirect_jsonshrink
        if not DaraCore.is_null(request.route_order):
            query['RouteOrder'] = request.route_order
        if not DaraCore.is_null(request.services_shrink):
            query['Services'] = request.services_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.direct_response_json):
            request.direct_response_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.direct_response_json, 'DirectResponseJSON', 'json')
        if not DaraCore.is_null(tmp_req.fallback_services):
            request.fallback_services_shrink = Utils.array_to_string_with_specified_style(tmp_req.fallback_services, 'FallbackServices', 'json')
        if not DaraCore.is_null(tmp_req.predicates):
            request.predicates_shrink = Utils.array_to_string_with_specified_style(tmp_req.predicates, 'Predicates', 'json')
        if not DaraCore.is_null(tmp_req.redirect_json):
            request.redirect_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.redirect_json, 'RedirectJSON', 'json')
        if not DaraCore.is_null(tmp_req.services):
            request.services_shrink = Utils.array_to_string_with_specified_style(tmp_req.services, 'Services', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direct_response_jsonshrink):
            query['DirectResponseJSON'] = request.direct_response_jsonshrink
        if not DaraCore.is_null(request.domain_id_list_json):
            query['DomainIdListJSON'] = request.domain_id_list_json
        if not DaraCore.is_null(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not DaraCore.is_null(request.fallback):
            query['Fallback'] = request.fallback
        if not DaraCore.is_null(request.fallback_services_shrink):
            query['FallbackServices'] = request.fallback_services_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.predicates_shrink):
            query['Predicates'] = request.predicates_shrink
        if not DaraCore.is_null(request.redirect_jsonshrink):
            query['RedirectJSON'] = request.redirect_jsonshrink
        if not DaraCore.is_null(request.route_order):
            query['RouteOrder'] = request.route_order
        if not DaraCore.is_null(request.services_shrink):
            query['Services'] = request.services_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route(
        self,
        request: main_models.UpdateGatewayRouteRequest,
    ) -> main_models.UpdateGatewayRouteResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_with_options(request, runtime)

    async def update_gateway_route_async(
        self,
        request: main_models.UpdateGatewayRouteRequest,
    ) -> main_models.UpdateGatewayRouteResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_with_options_async(request, runtime)

    def update_gateway_route_auth_with_options(
        self,
        tmp_req: main_models.UpdateGatewayRouteAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteAuthResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_json):
            request.auth_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.auth_json, 'AuthJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_jsonshrink):
            query['AuthJSON'] = request.auth_jsonshrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_auth_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayRouteAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteAuthResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteAuthShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_json):
            request.auth_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.auth_json, 'AuthJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.auth_jsonshrink):
            query['AuthJSON'] = request.auth_jsonshrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteAuth',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_auth(
        self,
        request: main_models.UpdateGatewayRouteAuthRequest,
    ) -> main_models.UpdateGatewayRouteAuthResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_auth_with_options(request, runtime)

    async def update_gateway_route_auth_async(
        self,
        request: main_models.UpdateGatewayRouteAuthRequest,
    ) -> main_models.UpdateGatewayRouteAuthResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_auth_with_options_async(request, runtime)

    def update_gateway_route_corswith_options(
        self,
        tmp_req: main_models.UpdateGatewayRouteCORSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteCORSResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteCORSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cors_json):
            request.cors_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.cors_json, 'CorsJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cors_jsonshrink):
            query['CorsJSON'] = request.cors_jsonshrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteCORS',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteCORSResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_corswith_options_async(
        self,
        tmp_req: main_models.UpdateGatewayRouteCORSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteCORSResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteCORSShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cors_json):
            request.cors_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.cors_json, 'CorsJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cors_jsonshrink):
            query['CorsJSON'] = request.cors_jsonshrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteCORS',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteCORSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_cors(
        self,
        request: main_models.UpdateGatewayRouteCORSRequest,
    ) -> main_models.UpdateGatewayRouteCORSResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_corswith_options(request, runtime)

    async def update_gateway_route_cors_async(
        self,
        request: main_models.UpdateGatewayRouteCORSRequest,
    ) -> main_models.UpdateGatewayRouteCORSResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_corswith_options_async(request, runtime)

    def update_gateway_route_httprewrite_with_options(
        self,
        request: main_models.UpdateGatewayRouteHTTPRewriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteHTTPRewriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_rewrite_json):
            query['HttpRewriteJSON'] = request.http_rewrite_json
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteHTTPRewrite',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteHTTPRewriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_httprewrite_with_options_async(
        self,
        request: main_models.UpdateGatewayRouteHTTPRewriteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteHTTPRewriteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.http_rewrite_json):
            query['HttpRewriteJSON'] = request.http_rewrite_json
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteHTTPRewrite',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteHTTPRewriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_httprewrite(
        self,
        request: main_models.UpdateGatewayRouteHTTPRewriteRequest,
    ) -> main_models.UpdateGatewayRouteHTTPRewriteResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_httprewrite_with_options(request, runtime)

    async def update_gateway_route_httprewrite_async(
        self,
        request: main_models.UpdateGatewayRouteHTTPRewriteRequest,
    ) -> main_models.UpdateGatewayRouteHTTPRewriteResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_httprewrite_with_options_async(request, runtime)

    def update_gateway_route_header_op_with_options(
        self,
        request: main_models.UpdateGatewayRouteHeaderOpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteHeaderOpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.header_op_json):
            query['HeaderOpJSON'] = request.header_op_json
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteHeaderOp',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteHeaderOpResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_header_op_with_options_async(
        self,
        request: main_models.UpdateGatewayRouteHeaderOpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteHeaderOpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.header_op_json):
            query['HeaderOpJSON'] = request.header_op_json
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteHeaderOp',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteHeaderOpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_header_op(
        self,
        request: main_models.UpdateGatewayRouteHeaderOpRequest,
    ) -> main_models.UpdateGatewayRouteHeaderOpResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_header_op_with_options(request, runtime)

    async def update_gateway_route_header_op_async(
        self,
        request: main_models.UpdateGatewayRouteHeaderOpRequest,
    ) -> main_models.UpdateGatewayRouteHeaderOpResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_header_op_with_options_async(request, runtime)

    def update_gateway_route_retry_with_options(
        self,
        tmp_req: main_models.UpdateGatewayRouteRetryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteRetryResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteRetryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.retry_json):
            request.retry_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.retry_json, 'RetryJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.retry_jsonshrink):
            query['RetryJSON'] = request.retry_jsonshrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteRetry',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteRetryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_retry_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayRouteRetryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteRetryResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteRetryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.retry_json):
            request.retry_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.retry_json, 'RetryJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.retry_jsonshrink):
            query['RetryJSON'] = request.retry_jsonshrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteRetry',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteRetryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_retry(
        self,
        request: main_models.UpdateGatewayRouteRetryRequest,
    ) -> main_models.UpdateGatewayRouteRetryResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_retry_with_options(request, runtime)

    async def update_gateway_route_retry_async(
        self,
        request: main_models.UpdateGatewayRouteRetryRequest,
    ) -> main_models.UpdateGatewayRouteRetryResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_retry_with_options_async(request, runtime)

    def update_gateway_route_timeout_with_options(
        self,
        tmp_req: main_models.UpdateGatewayRouteTimeoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteTimeoutResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteTimeoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.timeout_json):
            request.timeout_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.timeout_json, 'TimeoutJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.timeout_jsonshrink):
            query['TimeoutJSON'] = request.timeout_jsonshrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteTimeout',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_timeout_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayRouteTimeoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteTimeoutResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayRouteTimeoutShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.timeout_json):
            request.timeout_jsonshrink = Utils.array_to_string_with_specified_style(tmp_req.timeout_json, 'TimeoutJSON', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.timeout_jsonshrink):
            query['TimeoutJSON'] = request.timeout_jsonshrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteTimeout',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteTimeoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_timeout(
        self,
        request: main_models.UpdateGatewayRouteTimeoutRequest,
    ) -> main_models.UpdateGatewayRouteTimeoutResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_timeout_with_options(request, runtime)

    async def update_gateway_route_timeout_async(
        self,
        request: main_models.UpdateGatewayRouteTimeoutRequest,
    ) -> main_models.UpdateGatewayRouteTimeoutResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_timeout_with_options_async(request, runtime)

    def update_gateway_route_waf_status_with_options(
        self,
        request: main_models.UpdateGatewayRouteWafStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteWafStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteWafStatus',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteWafStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_waf_status_with_options_async(
        self,
        request: main_models.UpdateGatewayRouteWafStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayRouteWafStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayRouteWafStatus',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayRouteWafStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_waf_status(
        self,
        request: main_models.UpdateGatewayRouteWafStatusRequest,
    ) -> main_models.UpdateGatewayRouteWafStatusResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_route_waf_status_with_options(request, runtime)

    async def update_gateway_route_waf_status_async(
        self,
        request: main_models.UpdateGatewayRouteWafStatusRequest,
    ) -> main_models.UpdateGatewayRouteWafStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_route_waf_status_with_options_async(request, runtime)

    def update_gateway_service_with_options(
        self,
        tmp_req: main_models.UpdateGatewayServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dns_server_list):
            request.dns_server_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.dns_server_list, 'DnsServerList', 'json')
        if not DaraCore.is_null(tmp_req.ip_list):
            request.ip_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_list, 'IpList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.dns_server_list_shrink):
            query['DnsServerList'] = request.dns_server_list_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip_list_shrink):
            query['IpList'] = request.ip_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_port):
            query['ServicePort'] = request.service_port
        if not DaraCore.is_null(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not DaraCore.is_null(request.tls_setting):
            query['TlsSetting'] = request.tls_setting
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_service_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dns_server_list):
            request.dns_server_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.dns_server_list, 'DnsServerList', 'json')
        if not DaraCore.is_null(tmp_req.ip_list):
            request.ip_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_list, 'IpList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.dns_server_list_shrink):
            query['DnsServerList'] = request.dns_server_list_shrink
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip_list_shrink):
            query['IpList'] = request.ip_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_port):
            query['ServicePort'] = request.service_port
        if not DaraCore.is_null(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not DaraCore.is_null(request.tls_setting):
            query['TlsSetting'] = request.tls_setting
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_service(
        self,
        request: main_models.UpdateGatewayServiceRequest,
    ) -> main_models.UpdateGatewayServiceResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_service_with_options(request, runtime)

    async def update_gateway_service_async(
        self,
        request: main_models.UpdateGatewayServiceRequest,
    ) -> main_models.UpdateGatewayServiceResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_service_with_options_async(request, runtime)

    def update_gateway_service_check_with_options(
        self,
        tmp_req: main_models.UpdateGatewayServiceCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceCheckResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayServiceCheckShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.expected_statuses):
            request.expected_statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.expected_statuses, 'ExpectedStatuses', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.check):
            query['Check'] = request.check
        if not DaraCore.is_null(request.expected_statuses_shrink):
            query['ExpectedStatuses'] = request.expected_statuses_shrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.http_host):
            query['HttpHost'] = request.http_host
        if not DaraCore.is_null(request.http_path):
            query['HttpPath'] = request.http_path
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayServiceCheck',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_service_check_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayServiceCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceCheckResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayServiceCheckShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.expected_statuses):
            request.expected_statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.expected_statuses, 'ExpectedStatuses', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.check):
            query['Check'] = request.check
        if not DaraCore.is_null(request.expected_statuses_shrink):
            query['ExpectedStatuses'] = request.expected_statuses_shrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.http_host):
            query['HttpHost'] = request.http_host
        if not DaraCore.is_null(request.http_path):
            query['HttpPath'] = request.http_path
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayServiceCheck',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_service_check(
        self,
        request: main_models.UpdateGatewayServiceCheckRequest,
    ) -> main_models.UpdateGatewayServiceCheckResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_service_check_with_options(request, runtime)

    async def update_gateway_service_check_async(
        self,
        request: main_models.UpdateGatewayServiceCheckRequest,
    ) -> main_models.UpdateGatewayServiceCheckResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_service_check_with_options_async(request, runtime)

    def update_gateway_service_traffic_policy_with_options(
        self,
        tmp_req: main_models.UpdateGatewayServiceTrafficPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceTrafficPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayServiceTrafficPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gateway_traffic_policy):
            request.gateway_traffic_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.gateway_traffic_policy, 'GatewayTrafficPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_traffic_policy_shrink):
            query['GatewayTrafficPolicy'] = request.gateway_traffic_policy_shrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayServiceTrafficPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceTrafficPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_service_traffic_policy_with_options_async(
        self,
        tmp_req: main_models.UpdateGatewayServiceTrafficPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceTrafficPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateGatewayServiceTrafficPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gateway_traffic_policy):
            request.gateway_traffic_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.gateway_traffic_policy, 'GatewayTrafficPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_traffic_policy_shrink):
            query['GatewayTrafficPolicy'] = request.gateway_traffic_policy_shrink
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayServiceTrafficPolicy',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceTrafficPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_service_traffic_policy(
        self,
        request: main_models.UpdateGatewayServiceTrafficPolicyRequest,
    ) -> main_models.UpdateGatewayServiceTrafficPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_service_traffic_policy_with_options(request, runtime)

    async def update_gateway_service_traffic_policy_async(
        self,
        request: main_models.UpdateGatewayServiceTrafficPolicyRequest,
    ) -> main_models.UpdateGatewayServiceTrafficPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_service_traffic_policy_with_options_async(request, runtime)

    def update_gateway_service_version_with_options(
        self,
        request: main_models.UpdateGatewayServiceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayServiceVersion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_service_version_with_options_async(
        self,
        request: main_models.UpdateGatewayServiceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayServiceVersion',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_service_version(
        self,
        request: main_models.UpdateGatewayServiceVersionRequest,
    ) -> main_models.UpdateGatewayServiceVersionResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_service_version_with_options(request, runtime)

    async def update_gateway_service_version_async(
        self,
        request: main_models.UpdateGatewayServiceVersionRequest,
    ) -> main_models.UpdateGatewayServiceVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_service_version_with_options_async(request, runtime)

    def update_gateway_spec_with_options(
        self,
        request: main_models.UpdateGatewaySpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewaySpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.replica):
            query['Replica'] = request.replica
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewaySpec',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewaySpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_spec_with_options_async(
        self,
        request: main_models.UpdateGatewaySpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewaySpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.replica):
            query['Replica'] = request.replica
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewaySpec',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewaySpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_spec(
        self,
        request: main_models.UpdateGatewaySpecRequest,
    ) -> main_models.UpdateGatewaySpecResponse:
        runtime = RuntimeOptions()
        return self.update_gateway_spec_with_options(request, runtime)

    async def update_gateway_spec_async(
        self,
        request: main_models.UpdateGatewaySpecRequest,
    ) -> main_models.UpdateGatewaySpecResponse:
        runtime = RuntimeOptions()
        return await self.update_gateway_spec_with_options_async(request, runtime)

    def update_image_with_options(
        self,
        request: main_models.UpdateImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        request: main_models.UpdateImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImage',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image(
        self,
        request: main_models.UpdateImageRequest,
    ) -> main_models.UpdateImageResponse:
        runtime = RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    async def update_image_async(
        self,
        request: main_models.UpdateImageRequest,
    ) -> main_models.UpdateImageResponse:
        runtime = RuntimeOptions()
        return await self.update_image_with_options_async(request, runtime)

    def update_isolation_rule_with_options(
        self,
        request: main_models.UpdateIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIsolationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_isolation_rule_with_options_async(
        self,
        request: main_models.UpdateIsolationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIsolationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.limit_app):
            query['LimitApp'] = request.limit_app
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIsolationRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIsolationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_isolation_rule(
        self,
        request: main_models.UpdateIsolationRuleRequest,
    ) -> main_models.UpdateIsolationRuleResponse:
        runtime = RuntimeOptions()
        return self.update_isolation_rule_with_options(request, runtime)

    async def update_isolation_rule_async(
        self,
        request: main_models.UpdateIsolationRuleRequest,
    ) -> main_models.UpdateIsolationRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_isolation_rule_with_options_async(request, runtime)

    def update_locality_rule_with_options(
        self,
        request: main_models.UpdateLocalityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLocalityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLocalityRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLocalityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_locality_rule_with_options_async(
        self,
        request: main_models.UpdateLocalityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLocalityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLocalityRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLocalityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_locality_rule(
        self,
        request: main_models.UpdateLocalityRuleRequest,
    ) -> main_models.UpdateLocalityRuleResponse:
        runtime = RuntimeOptions()
        return self.update_locality_rule_with_options(request, runtime)

    async def update_locality_rule_async(
        self,
        request: main_models.UpdateLocalityRuleRequest,
    ) -> main_models.UpdateLocalityRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_locality_rule_with_options_async(request, runtime)

    def update_message_queue_route_with_options(
        self,
        tmp_req: main_models.UpdateMessageQueueRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageQueueRouteResponse:
        tmp_req.validate()
        request = main_models.UpdateMessageQueueRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gray_base_tags):
            request.gray_base_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.gray_base_tags, 'GrayBaseTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.filter_side):
            query['FilterSide'] = request.filter_side
        if not DaraCore.is_null(request.gray_base_tags_shrink):
            query['GrayBaseTags'] = request.gray_base_tags_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageQueueRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageQueueRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_message_queue_route_with_options_async(
        self,
        tmp_req: main_models.UpdateMessageQueueRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageQueueRouteResponse:
        tmp_req.validate()
        request = main_models.UpdateMessageQueueRouteShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.gray_base_tags):
            request.gray_base_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.gray_base_tags, 'GrayBaseTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.filter_side):
            query['FilterSide'] = request.filter_side
        if not DaraCore.is_null(request.gray_base_tags_shrink):
            query['GrayBaseTags'] = request.gray_base_tags_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageQueueRoute',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageQueueRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_message_queue_route(
        self,
        request: main_models.UpdateMessageQueueRouteRequest,
    ) -> main_models.UpdateMessageQueueRouteResponse:
        runtime = RuntimeOptions()
        return self.update_message_queue_route_with_options(request, runtime)

    async def update_message_queue_route_async(
        self,
        request: main_models.UpdateMessageQueueRouteRequest,
    ) -> main_models.UpdateMessageQueueRouteResponse:
        runtime = RuntimeOptions()
        return await self.update_message_queue_route_with_options_async(request, runtime)

    def update_migration_task_with_options(
        self,
        request: main_models.UpdateMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.origin_instance_address):
            query['OriginInstanceAddress'] = request.origin_instance_address
        if not DaraCore.is_null(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not DaraCore.is_null(request.origin_instance_namespace):
            query['OriginInstanceNamespace'] = request.origin_instance_namespace
        if not DaraCore.is_null(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.sync_type):
            query['SyncType'] = request.sync_type
        if not DaraCore.is_null(request.target_cluster_name):
            query['TargetClusterName'] = request.target_cluster_name
        if not DaraCore.is_null(request.target_cluster_url):
            query['TargetClusterUrl'] = request.target_cluster_url
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_migration_task_with_options_async(
        self,
        request: main_models.UpdateMigrationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMigrationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.origin_instance_address):
            query['OriginInstanceAddress'] = request.origin_instance_address
        if not DaraCore.is_null(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not DaraCore.is_null(request.origin_instance_namespace):
            query['OriginInstanceNamespace'] = request.origin_instance_namespace
        if not DaraCore.is_null(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.sync_type):
            query['SyncType'] = request.sync_type
        if not DaraCore.is_null(request.target_cluster_name):
            query['TargetClusterName'] = request.target_cluster_name
        if not DaraCore.is_null(request.target_cluster_url):
            query['TargetClusterUrl'] = request.target_cluster_url
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMigrationTask',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_migration_task(
        self,
        request: main_models.UpdateMigrationTaskRequest,
    ) -> main_models.UpdateMigrationTaskResponse:
        runtime = RuntimeOptions()
        return self.update_migration_task_with_options(request, runtime)

    async def update_migration_task_async(
        self,
        request: main_models.UpdateMigrationTaskRequest,
    ) -> main_models.UpdateMigrationTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_migration_task_with_options_async(request, runtime)

    def update_nacos_cluster_with_options(
        self,
        request: main_models.UpdateNacosClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.check_port):
            query['CheckPort'] = request.check_port
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.health_checker):
            query['HealthChecker'] = request.health_checker
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.use_instance_port_for_check):
            query['UseInstancePortForCheck'] = request.use_instance_port_for_check
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_cluster_with_options_async(
        self,
        request: main_models.UpdateNacosClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.check_port):
            query['CheckPort'] = request.check_port
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.health_checker):
            query['HealthChecker'] = request.health_checker
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.use_instance_port_for_check):
            query['UseInstancePortForCheck'] = request.use_instance_port_for_check
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_cluster(
        self,
        request: main_models.UpdateNacosClusterRequest,
    ) -> main_models.UpdateNacosClusterResponse:
        runtime = RuntimeOptions()
        return self.update_nacos_cluster_with_options(request, runtime)

    async def update_nacos_cluster_async(
        self,
        request: main_models.UpdateNacosClusterRequest,
    ) -> main_models.UpdateNacosClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_nacos_cluster_with_options_async(request, runtime)

    def update_nacos_config_with_options(
        self,
        request: main_models.UpdateNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.beta_ips):
            query['BetaIps'] = request.beta_ips
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.encrypted_data_key):
            query['EncryptedDataKey'] = request.encrypted_data_key
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_config_with_options_async(
        self,
        request: main_models.UpdateNacosConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.beta_ips):
            query['BetaIps'] = request.beta_ips
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.encrypted_data_key):
            query['EncryptedDataKey'] = request.encrypted_data_key
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_config(
        self,
        request: main_models.UpdateNacosConfigRequest,
    ) -> main_models.UpdateNacosConfigResponse:
        runtime = RuntimeOptions()
        return self.update_nacos_config_with_options(request, runtime)

    async def update_nacos_config_async(
        self,
        request: main_models.UpdateNacosConfigRequest,
    ) -> main_models.UpdateNacosConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_nacos_config_with_options_async(request, runtime)

    def update_nacos_gray_config_with_options(
        self,
        request: main_models.UpdateNacosGrayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosGrayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.gray_rule):
            query['GrayRule'] = request.gray_rule
        if not DaraCore.is_null(request.gray_rule_name):
            query['GrayRuleName'] = request.gray_rule_name
        if not DaraCore.is_null(request.gray_rule_priority):
            query['GrayRulePriority'] = request.gray_rule_priority
        if not DaraCore.is_null(request.gray_type):
            query['GrayType'] = request.gray_type
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.op_type):
            query['OpType'] = request.op_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.stop_gray):
            query['StopGray'] = request.stop_gray
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosGrayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosGrayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_gray_config_with_options_async(
        self,
        request: main_models.UpdateNacosGrayConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosGrayConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.gray_rule):
            query['GrayRule'] = request.gray_rule
        if not DaraCore.is_null(request.gray_rule_name):
            query['GrayRuleName'] = request.gray_rule_name
        if not DaraCore.is_null(request.gray_rule_priority):
            query['GrayRulePriority'] = request.gray_rule_priority
        if not DaraCore.is_null(request.gray_type):
            query['GrayType'] = request.gray_type
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.op_type):
            query['OpType'] = request.op_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.stop_gray):
            query['StopGray'] = request.stop_gray
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosGrayConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosGrayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_gray_config(
        self,
        request: main_models.UpdateNacosGrayConfigRequest,
    ) -> main_models.UpdateNacosGrayConfigResponse:
        runtime = RuntimeOptions()
        return self.update_nacos_gray_config_with_options(request, runtime)

    async def update_nacos_gray_config_async(
        self,
        request: main_models.UpdateNacosGrayConfigRequest,
    ) -> main_models.UpdateNacosGrayConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_nacos_gray_config_with_options_async(request, runtime)

    def update_nacos_instance_with_options(
        self,
        request: main_models.UpdateNacosInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        body = {}
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosInstance',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_instance_with_options_async(
        self,
        request: main_models.UpdateNacosInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        body = {}
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosInstance',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_instance(
        self,
        request: main_models.UpdateNacosInstanceRequest,
    ) -> main_models.UpdateNacosInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_nacos_instance_with_options(request, runtime)

    async def update_nacos_instance_async(
        self,
        request: main_models.UpdateNacosInstanceRequest,
    ) -> main_models.UpdateNacosInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_nacos_instance_with_options_async(request, runtime)

    def update_nacos_service_with_options(
        self,
        request: main_models.UpdateNacosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.protect_threshold):
            query['ProtectThreshold'] = request.protect_threshold
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_service_with_options_async(
        self,
        request: main_models.UpdateNacosServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacosServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.protect_threshold):
            query['ProtectThreshold'] = request.protect_threshold
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacosService',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacosServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_service(
        self,
        request: main_models.UpdateNacosServiceRequest,
    ) -> main_models.UpdateNacosServiceResponse:
        runtime = RuntimeOptions()
        return self.update_nacos_service_with_options(request, runtime)

    async def update_nacos_service_async(
        self,
        request: main_models.UpdateNacosServiceRequest,
    ) -> main_models.UpdateNacosServiceResponse:
        runtime = RuntimeOptions()
        return await self.update_nacos_service_with_options_async(request, runtime)

    def update_plugin_config_with_options(
        self,
        tmp_req: main_models.UpdatePluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePluginConfigResponse:
        tmp_req.validate()
        request = main_models.UpdatePluginConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id_list):
            request.resource_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id_list, 'ResourceIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.resource_id_list_shrink):
            query['ResourceIdList'] = request.resource_id_list_shrink
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_plugin_config_with_options_async(
        self,
        tmp_req: main_models.UpdatePluginConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePluginConfigResponse:
        tmp_req.validate()
        request = main_models.UpdatePluginConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id_list):
            request.resource_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id_list, 'ResourceIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not DaraCore.is_null(request.resource_id_list_shrink):
            query['ResourceIdList'] = request.resource_id_list_shrink
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePluginConfig',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePluginConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_plugin_config(
        self,
        request: main_models.UpdatePluginConfigRequest,
    ) -> main_models.UpdatePluginConfigResponse:
        runtime = RuntimeOptions()
        return self.update_plugin_config_with_options(request, runtime)

    async def update_plugin_config_async(
        self,
        request: main_models.UpdatePluginConfigRequest,
    ) -> main_models.UpdatePluginConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_plugin_config_with_options_async(request, runtime)

    def update_sslcert_with_options(
        self,
        request: main_models.UpdateSSLCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSSLCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSSLCert',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSSLCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sslcert_with_options_async(
        self,
        request: main_models.UpdateSSLCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSSLCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSSLCert',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSSLCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sslcert(
        self,
        request: main_models.UpdateSSLCertRequest,
    ) -> main_models.UpdateSSLCertResponse:
        runtime = RuntimeOptions()
        return self.update_sslcert_with_options(request, runtime)

    async def update_sslcert_async(
        self,
        request: main_models.UpdateSSLCertRequest,
    ) -> main_models.UpdateSSLCertResponse:
        runtime = RuntimeOptions()
        return await self.update_sslcert_with_options_async(request, runtime)

    def update_service_source_with_options(
        self,
        tmp_req: main_models.UpdateServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceSourceResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ingress_options_request):
            request.ingress_options_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.ingress_options_request, 'IngressOptionsRequest', 'json')
        if not DaraCore.is_null(tmp_req.path_list):
            request.path_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.path_list, 'PathList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ingress_options_request_shrink):
            query['IngressOptionsRequest'] = request.ingress_options_request_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.path_list_shrink):
            query['PathList'] = request.path_list_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_source_with_options_async(
        self,
        tmp_req: main_models.UpdateServiceSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceSourceResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ingress_options_request):
            request.ingress_options_request_shrink = Utils.array_to_string_with_specified_style(tmp_req.ingress_options_request, 'IngressOptionsRequest', 'json')
        if not DaraCore.is_null(tmp_req.path_list):
            request.path_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.path_list, 'PathList', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ingress_options_request_shrink):
            query['IngressOptionsRequest'] = request.ingress_options_request_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.path_list_shrink):
            query['PathList'] = request.path_list_shrink
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceSource',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_source(
        self,
        request: main_models.UpdateServiceSourceRequest,
    ) -> main_models.UpdateServiceSourceResponse:
        runtime = RuntimeOptions()
        return self.update_service_source_with_options(request, runtime)

    async def update_service_source_async(
        self,
        request: main_models.UpdateServiceSourceRequest,
    ) -> main_models.UpdateServiceSourceResponse:
        runtime = RuntimeOptions()
        return await self.update_service_source_with_options_async(request, runtime)

    def update_web_flow_rule_with_options(
        self,
        request: main_models.UpdateWebFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.burst):
            query['Burst'] = request.burst
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.param_item):
            query['ParamItem'] = request.param_item
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_mode):
            query['ResourceMode'] = request.resource_mode
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebFlowRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_flow_rule_with_options_async(
        self,
        request: main_models.UpdateWebFlowRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebFlowRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.burst):
            query['Burst'] = request.burst
        if not DaraCore.is_null(request.control_behavior):
            query['ControlBehavior'] = request.control_behavior
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.max_queueing_time_ms):
            query['MaxQueueingTimeMs'] = request.max_queueing_time_ms
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.param_item):
            query['ParamItem'] = request.param_item
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_mode):
            query['ResourceMode'] = request.resource_mode
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.stat_interval_ms):
            query['StatIntervalMs'] = request.stat_interval_ms
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebFlowRule',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebFlowRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_flow_rule(
        self,
        request: main_models.UpdateWebFlowRuleRequest,
    ) -> main_models.UpdateWebFlowRuleResponse:
        runtime = RuntimeOptions()
        return self.update_web_flow_rule_with_options(request, runtime)

    async def update_web_flow_rule_async(
        self,
        request: main_models.UpdateWebFlowRuleRequest,
    ) -> main_models.UpdateWebFlowRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_web_flow_rule_with_options_async(request, runtime)

    def update_znode_with_options(
        self,
        request: main_models.UpdateZnodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateZnodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateZnode',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_znode_with_options_async(
        self,
        request: main_models.UpdateZnodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateZnodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateZnode',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateZnodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_znode(
        self,
        request: main_models.UpdateZnodeRequest,
    ) -> main_models.UpdateZnodeResponse:
        runtime = RuntimeOptions()
        return self.update_znode_with_options(request, runtime)

    async def update_znode_async(
        self,
        request: main_models.UpdateZnodeRequest,
    ) -> main_models.UpdateZnodeResponse:
        runtime = RuntimeOptions()
        return await self.update_znode_with_options_async(request, runtime)

    def upgrade_cluster_with_options(
        self,
        request: main_models.UpgradeClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_with_options_async(
        self,
        request: main_models.UpgradeClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not DaraCore.is_null(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeCluster',
            version = '2019-05-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster(
        self,
        request: main_models.UpgradeClusterRequest,
    ) -> main_models.UpgradeClusterResponse:
        runtime = RuntimeOptions()
        return self.upgrade_cluster_with_options(request, runtime)

    async def upgrade_cluster_async(
        self,
        request: main_models.UpgradeClusterRequest,
    ) -> main_models.UpgradeClusterResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_cluster_with_options_async(request, runtime)
