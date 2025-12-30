# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pvtz20180101 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('pvtz', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_custom_line_with_options(
        self,
        request: main_models.AddCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_category):
            query['DnsCategory'] = request.dns_category
        if not DaraCore.is_null(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.share_scope):
            query['ShareScope'] = request.share_scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomLine',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_line_with_options_async(
        self,
        request: main_models.AddCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_category):
            query['DnsCategory'] = request.dns_category
        if not DaraCore.is_null(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.share_scope):
            query['ShareScope'] = request.share_scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomLine',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_line(
        self,
        request: main_models.AddCustomLineRequest,
    ) -> main_models.AddCustomLineResponse:
        runtime = RuntimeOptions()
        return self.add_custom_line_with_options(request, runtime)

    async def add_custom_line_async(
        self,
        request: main_models.AddCustomLineRequest,
    ) -> main_models.AddCustomLineResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_line_with_options_async(request, runtime)

    def add_resolver_endpoint_with_options(
        self,
        request: main_models.AddResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_resolver_endpoint_with_options_async(
        self,
        request: main_models.AddResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_resolver_endpoint(
        self,
        request: main_models.AddResolverEndpointRequest,
    ) -> main_models.AddResolverEndpointResponse:
        runtime = RuntimeOptions()
        return self.add_resolver_endpoint_with_options(request, runtime)

    async def add_resolver_endpoint_async(
        self,
        request: main_models.AddResolverEndpointRequest,
    ) -> main_models.AddResolverEndpointResponse:
        runtime = RuntimeOptions()
        return await self.add_resolver_endpoint_with_options_async(request, runtime)

    def add_resolver_rule_with_options(
        self,
        request: main_models.AddResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edge_dns_clusters):
            query['EdgeDnsClusters'] = request.edge_dns_clusters
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vpcs):
            query['Vpcs'] = request.vpcs
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_resolver_rule_with_options_async(
        self,
        request: main_models.AddResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edge_dns_clusters):
            query['EdgeDnsClusters'] = request.edge_dns_clusters
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vpcs):
            query['Vpcs'] = request.vpcs
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_resolver_rule(
        self,
        request: main_models.AddResolverRuleRequest,
    ) -> main_models.AddResolverRuleResponse:
        runtime = RuntimeOptions()
        return self.add_resolver_rule_with_options(request, runtime)

    async def add_resolver_rule_async(
        self,
        request: main_models.AddResolverRuleRequest,
    ) -> main_models.AddResolverRuleResponse:
        runtime = RuntimeOptions()
        return await self.add_resolver_rule_with_options_async(request, runtime)

    def add_user_vpc_authorization_with_options(
        self,
        request: main_models.AddUserVpcAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserVpcAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_channel):
            query['AuthChannel'] = request.auth_channel
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserVpcAuthorization',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserVpcAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_vpc_authorization_with_options_async(
        self,
        request: main_models.AddUserVpcAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserVpcAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_channel):
            query['AuthChannel'] = request.auth_channel
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserVpcAuthorization',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserVpcAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_vpc_authorization(
        self,
        request: main_models.AddUserVpcAuthorizationRequest,
    ) -> main_models.AddUserVpcAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.add_user_vpc_authorization_with_options(request, runtime)

    async def add_user_vpc_authorization_async(
        self,
        request: main_models.AddUserVpcAuthorizationRequest,
    ) -> main_models.AddUserVpcAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.add_user_vpc_authorization_with_options_async(request, runtime)

    def add_zone_with_options(
        self,
        request: main_models.AddZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        if not DaraCore.is_null(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not DaraCore.is_null(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddZone',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_with_options_async(
        self,
        request: main_models.AddZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        if not DaraCore.is_null(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not DaraCore.is_null(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddZone',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_zone(
        self,
        request: main_models.AddZoneRequest,
    ) -> main_models.AddZoneResponse:
        runtime = RuntimeOptions()
        return self.add_zone_with_options(request, runtime)

    async def add_zone_async(
        self,
        request: main_models.AddZoneRequest,
    ) -> main_models.AddZoneResponse:
        runtime = RuntimeOptions()
        return await self.add_zone_with_options_async(request, runtime)

    def add_zone_record_with_options(
        self,
        request: main_models.AddZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_record_with_options_async(
        self,
        request: main_models.AddZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_zone_record(
        self,
        request: main_models.AddZoneRecordRequest,
    ) -> main_models.AddZoneRecordResponse:
        runtime = RuntimeOptions()
        return self.add_zone_record_with_options(request, runtime)

    async def add_zone_record_async(
        self,
        request: main_models.AddZoneRecordRequest,
    ) -> main_models.AddZoneRecordResponse:
        runtime = RuntimeOptions()
        return await self.add_zone_record_with_options_async(request, runtime)

    def bind_resolver_rule_vpc_with_options(
        self,
        request: main_models.BindResolverRuleVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindResolverRuleVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.vpc):
            query['Vpc'] = request.vpc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindResolverRuleVpc',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindResolverRuleVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_resolver_rule_vpc_with_options_async(
        self,
        request: main_models.BindResolverRuleVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindResolverRuleVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.vpc):
            query['Vpc'] = request.vpc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindResolverRuleVpc',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindResolverRuleVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_resolver_rule_vpc(
        self,
        request: main_models.BindResolverRuleVpcRequest,
    ) -> main_models.BindResolverRuleVpcResponse:
        runtime = RuntimeOptions()
        return self.bind_resolver_rule_vpc_with_options(request, runtime)

    async def bind_resolver_rule_vpc_async(
        self,
        request: main_models.BindResolverRuleVpcRequest,
    ) -> main_models.BindResolverRuleVpcResponse:
        runtime = RuntimeOptions()
        return await self.bind_resolver_rule_vpc_with_options_async(request, runtime)

    def bind_zone_vpc_with_options(
        self,
        request: main_models.BindZoneVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindZoneVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.vpcs):
            query['Vpcs'] = request.vpcs
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindZoneVpc',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindZoneVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_zone_vpc_with_options_async(
        self,
        request: main_models.BindZoneVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindZoneVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.vpcs):
            query['Vpcs'] = request.vpcs
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindZoneVpc',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindZoneVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_zone_vpc(
        self,
        request: main_models.BindZoneVpcRequest,
    ) -> main_models.BindZoneVpcResponse:
        runtime = RuntimeOptions()
        return self.bind_zone_vpc_with_options(request, runtime)

    async def bind_zone_vpc_async(
        self,
        request: main_models.BindZoneVpcRequest,
    ) -> main_models.BindZoneVpcResponse:
        runtime = RuntimeOptions()
        return await self.bind_zone_vpc_with_options_async(request, runtime)

    def change_zone_dns_group_with_options(
        self,
        request: main_models.ChangeZoneDnsGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeZoneDnsGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeZoneDnsGroup',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeZoneDnsGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_zone_dns_group_with_options_async(
        self,
        request: main_models.ChangeZoneDnsGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeZoneDnsGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dns_group):
            query['DnsGroup'] = request.dns_group
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeZoneDnsGroup',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeZoneDnsGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_zone_dns_group(
        self,
        request: main_models.ChangeZoneDnsGroupRequest,
    ) -> main_models.ChangeZoneDnsGroupResponse:
        runtime = RuntimeOptions()
        return self.change_zone_dns_group_with_options(request, runtime)

    async def change_zone_dns_group_async(
        self,
        request: main_models.ChangeZoneDnsGroupRequest,
    ) -> main_models.ChangeZoneDnsGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_zone_dns_group_with_options_async(request, runtime)

    def check_zone_name_with_options(
        self,
        request: main_models.CheckZoneNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckZoneNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckZoneName',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckZoneNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_zone_name_with_options_async(
        self,
        request: main_models.CheckZoneNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckZoneNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_name):
            query['ZoneName'] = request.zone_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckZoneName',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckZoneNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_zone_name(
        self,
        request: main_models.CheckZoneNameRequest,
    ) -> main_models.CheckZoneNameResponse:
        runtime = RuntimeOptions()
        return self.check_zone_name_with_options(request, runtime)

    async def check_zone_name_async(
        self,
        request: main_models.CheckZoneNameRequest,
    ) -> main_models.CheckZoneNameResponse:
        runtime = RuntimeOptions()
        return await self.check_zone_name_with_options_async(request, runtime)

    def delete_custom_line_with_options(
        self,
        request: main_models.DeleteCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomLine',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_line_with_options_async(
        self,
        request: main_models.DeleteCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomLine',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_line(
        self,
        request: main_models.DeleteCustomLineRequest,
    ) -> main_models.DeleteCustomLineResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_line_with_options(request, runtime)

    async def delete_custom_line_async(
        self,
        request: main_models.DeleteCustomLineRequest,
    ) -> main_models.DeleteCustomLineResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_line_with_options_async(request, runtime)

    def delete_resolver_endpoint_with_options(
        self,
        request: main_models.DeleteResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resolver_endpoint_with_options_async(
        self,
        request: main_models.DeleteResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resolver_endpoint(
        self,
        request: main_models.DeleteResolverEndpointRequest,
    ) -> main_models.DeleteResolverEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_resolver_endpoint_with_options(request, runtime)

    async def delete_resolver_endpoint_async(
        self,
        request: main_models.DeleteResolverEndpointRequest,
    ) -> main_models.DeleteResolverEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_resolver_endpoint_with_options_async(request, runtime)

    def delete_resolver_rule_with_options(
        self,
        request: main_models.DeleteResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resolver_rule_with_options_async(
        self,
        request: main_models.DeleteResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resolver_rule(
        self,
        request: main_models.DeleteResolverRuleRequest,
    ) -> main_models.DeleteResolverRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_resolver_rule_with_options(request, runtime)

    async def delete_resolver_rule_async(
        self,
        request: main_models.DeleteResolverRuleRequest,
    ) -> main_models.DeleteResolverRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_resolver_rule_with_options_async(request, runtime)

    def delete_user_vpc_authorization_with_options(
        self,
        request: main_models.DeleteUserVpcAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserVpcAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserVpcAuthorization',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserVpcAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_vpc_authorization_with_options_async(
        self,
        request: main_models.DeleteUserVpcAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserVpcAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserVpcAuthorization',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserVpcAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_vpc_authorization(
        self,
        request: main_models.DeleteUserVpcAuthorizationRequest,
    ) -> main_models.DeleteUserVpcAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.delete_user_vpc_authorization_with_options(request, runtime)

    async def delete_user_vpc_authorization_async(
        self,
        request: main_models.DeleteUserVpcAuthorizationRequest,
    ) -> main_models.DeleteUserVpcAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_vpc_authorization_with_options_async(request, runtime)

    def delete_zone_with_options(
        self,
        request: main_models.DeleteZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteZone',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_zone_with_options_async(
        self,
        request: main_models.DeleteZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteZone',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_zone(
        self,
        request: main_models.DeleteZoneRequest,
    ) -> main_models.DeleteZoneResponse:
        runtime = RuntimeOptions()
        return self.delete_zone_with_options(request, runtime)

    async def delete_zone_async(
        self,
        request: main_models.DeleteZoneRequest,
    ) -> main_models.DeleteZoneResponse:
        runtime = RuntimeOptions()
        return await self.delete_zone_with_options_async(request, runtime)

    def delete_zone_record_with_options(
        self,
        request: main_models.DeleteZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_zone_record_with_options_async(
        self,
        request: main_models.DeleteZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_zone_record(
        self,
        request: main_models.DeleteZoneRecordRequest,
    ) -> main_models.DeleteZoneRecordResponse:
        runtime = RuntimeOptions()
        return self.delete_zone_record_with_options(request, runtime)

    async def delete_zone_record_async(
        self,
        request: main_models.DeleteZoneRecordRequest,
    ) -> main_models.DeleteZoneRecordResponse:
        runtime = RuntimeOptions()
        return await self.delete_zone_record_with_options_async(request, runtime)

    def describe_change_logs_with_options(
        self,
        request: main_models.DescribeChangeLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChangeLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChangeLogs',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChangeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_change_logs_with_options_async(
        self,
        request: main_models.DescribeChangeLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChangeLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChangeLogs',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChangeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_change_logs(
        self,
        request: main_models.DescribeChangeLogsRequest,
    ) -> main_models.DescribeChangeLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_change_logs_with_options(request, runtime)

    async def describe_change_logs_async(
        self,
        request: main_models.DescribeChangeLogsRequest,
    ) -> main_models.DescribeChangeLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_change_logs_with_options_async(request, runtime)

    def describe_custom_line_info_with_options(
        self,
        request: main_models.DescribeCustomLineInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLineInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLineInfo',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLineInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_line_info_with_options_async(
        self,
        request: main_models.DescribeCustomLineInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLineInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLineInfo',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLineInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_line_info(
        self,
        request: main_models.DescribeCustomLineInfoRequest,
    ) -> main_models.DescribeCustomLineInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_line_info_with_options(request, runtime)

    async def describe_custom_line_info_async(
        self,
        request: main_models.DescribeCustomLineInfoRequest,
    ) -> main_models.DescribeCustomLineInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_line_info_with_options_async(request, runtime)

    def describe_custom_lines_with_options(
        self,
        request: main_models.DescribeCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLines',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_lines_with_options_async(
        self,
        request: main_models.DescribeCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomLines',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_lines(
        self,
        request: main_models.DescribeCustomLinesRequest,
    ) -> main_models.DescribeCustomLinesResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_lines_with_options(request, runtime)

    async def describe_custom_lines_async(
        self,
        request: main_models.DescribeCustomLinesRequest,
    ) -> main_models.DescribeCustomLinesResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_lines_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.vpc_type):
            query['VpcType'] = request.vpc_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.vpc_type):
            query['VpcType'] = request.vpc_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-01-01',
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

    def describe_request_graph_with_options(
        self,
        request: main_models.DescribeRequestGraphRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRequestGraphResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRequestGraph',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRequestGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_request_graph_with_options_async(
        self,
        request: main_models.DescribeRequestGraphRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRequestGraphResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRequestGraph',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRequestGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_request_graph(
        self,
        request: main_models.DescribeRequestGraphRequest,
    ) -> main_models.DescribeRequestGraphResponse:
        runtime = RuntimeOptions()
        return self.describe_request_graph_with_options(request, runtime)

    async def describe_request_graph_async(
        self,
        request: main_models.DescribeRequestGraphRequest,
    ) -> main_models.DescribeRequestGraphResponse:
        runtime = RuntimeOptions()
        return await self.describe_request_graph_with_options_async(request, runtime)

    def describe_resolver_available_zones_with_options(
        self,
        request: main_models.DescribeResolverAvailableZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverAvailableZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.az_id):
            query['AzId'] = request.az_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resolver_region_id):
            query['ResolverRegionId'] = request.resolver_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverAvailableZones',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_available_zones_with_options_async(
        self,
        request: main_models.DescribeResolverAvailableZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverAvailableZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.az_id):
            query['AzId'] = request.az_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resolver_region_id):
            query['ResolverRegionId'] = request.resolver_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverAvailableZones',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_available_zones(
        self,
        request: main_models.DescribeResolverAvailableZonesRequest,
    ) -> main_models.DescribeResolverAvailableZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_resolver_available_zones_with_options(request, runtime)

    async def describe_resolver_available_zones_async(
        self,
        request: main_models.DescribeResolverAvailableZonesRequest,
    ) -> main_models.DescribeResolverAvailableZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_resolver_available_zones_with_options_async(request, runtime)

    def describe_resolver_endpoint_with_options(
        self,
        request: main_models.DescribeResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_endpoint_with_options_async(
        self,
        request: main_models.DescribeResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_endpoint(
        self,
        request: main_models.DescribeResolverEndpointRequest,
    ) -> main_models.DescribeResolverEndpointResponse:
        runtime = RuntimeOptions()
        return self.describe_resolver_endpoint_with_options(request, runtime)

    async def describe_resolver_endpoint_async(
        self,
        request: main_models.DescribeResolverEndpointRequest,
    ) -> main_models.DescribeResolverEndpointResponse:
        runtime = RuntimeOptions()
        return await self.describe_resolver_endpoint_with_options_async(request, runtime)

    def describe_resolver_endpoints_with_options(
        self,
        request: main_models.DescribeResolverEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverEndpoints',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_endpoints_with_options_async(
        self,
        request: main_models.DescribeResolverEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverEndpoints',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_endpoints(
        self,
        request: main_models.DescribeResolverEndpointsRequest,
    ) -> main_models.DescribeResolverEndpointsResponse:
        runtime = RuntimeOptions()
        return self.describe_resolver_endpoints_with_options(request, runtime)

    async def describe_resolver_endpoints_async(
        self,
        request: main_models.DescribeResolverEndpointsRequest,
    ) -> main_models.DescribeResolverEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.describe_resolver_endpoints_with_options_async(request, runtime)

    def describe_resolver_rule_with_options(
        self,
        request: main_models.DescribeResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_rule_with_options_async(
        self,
        request: main_models.DescribeResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_rule(
        self,
        request: main_models.DescribeResolverRuleRequest,
    ) -> main_models.DescribeResolverRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_resolver_rule_with_options(request, runtime)

    async def describe_resolver_rule_async(
        self,
        request: main_models.DescribeResolverRuleRequest,
    ) -> main_models.DescribeResolverRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_resolver_rule_with_options_async(request, runtime)

    def describe_resolver_rules_with_options(
        self,
        request: main_models.DescribeResolverRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverRules',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resolver_rules_with_options_async(
        self,
        request: main_models.DescribeResolverRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResolverRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResolverRules',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResolverRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resolver_rules(
        self,
        request: main_models.DescribeResolverRulesRequest,
    ) -> main_models.DescribeResolverRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_resolver_rules_with_options(request, runtime)

    async def describe_resolver_rules_async(
        self,
        request: main_models.DescribeResolverRulesRequest,
    ) -> main_models.DescribeResolverRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_resolver_rules_with_options_async(request, runtime)

    def describe_statistic_summary_with_options(
        self,
        request: main_models.DescribeStatisticSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStatisticSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStatisticSummary',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStatisticSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistic_summary_with_options_async(
        self,
        request: main_models.DescribeStatisticSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStatisticSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStatisticSummary',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStatisticSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_statistic_summary(
        self,
        request: main_models.DescribeStatisticSummaryRequest,
    ) -> main_models.DescribeStatisticSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_statistic_summary_with_options(request, runtime)

    async def describe_statistic_summary_async(
        self,
        request: main_models.DescribeStatisticSummaryRequest,
    ) -> main_models.DescribeStatisticSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_statistic_summary_with_options_async(request, runtime)

    def describe_sync_ecs_host_task_with_options(
        self,
        request: main_models.DescribeSyncEcsHostTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncEcsHostTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncEcsHostTask',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncEcsHostTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_ecs_host_task_with_options_async(
        self,
        request: main_models.DescribeSyncEcsHostTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncEcsHostTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncEcsHostTask',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncEcsHostTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_ecs_host_task(
        self,
        request: main_models.DescribeSyncEcsHostTaskRequest,
    ) -> main_models.DescribeSyncEcsHostTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_sync_ecs_host_task_with_options(request, runtime)

    async def describe_sync_ecs_host_task_async(
        self,
        request: main_models.DescribeSyncEcsHostTaskRequest,
    ) -> main_models.DescribeSyncEcsHostTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_sync_ecs_host_task_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_user_service_status_with_options(
        self,
        request: main_models.DescribeUserServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserServiceStatus',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_service_status_with_options_async(
        self,
        request: main_models.DescribeUserServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserServiceStatus',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_service_status(
        self,
        request: main_models.DescribeUserServiceStatusRequest,
    ) -> main_models.DescribeUserServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_service_status_with_options(request, runtime)

    async def describe_user_service_status_async(
        self,
        request: main_models.DescribeUserServiceStatusRequest,
    ) -> main_models.DescribeUserServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_service_status_with_options_async(request, runtime)

    def describe_user_vpc_authorizations_with_options(
        self,
        request: main_models.DescribeUserVpcAuthorizationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserVpcAuthorizationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserVpcAuthorizations',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserVpcAuthorizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_vpc_authorizations_with_options_async(
        self,
        request: main_models.DescribeUserVpcAuthorizationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserVpcAuthorizationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.authorized_user_id):
            query['AuthorizedUserId'] = request.authorized_user_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserVpcAuthorizations',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserVpcAuthorizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_vpc_authorizations(
        self,
        request: main_models.DescribeUserVpcAuthorizationsRequest,
    ) -> main_models.DescribeUserVpcAuthorizationsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_vpc_authorizations_with_options(request, runtime)

    async def describe_user_vpc_authorizations_async(
        self,
        request: main_models.DescribeUserVpcAuthorizationsRequest,
    ) -> main_models.DescribeUserVpcAuthorizationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_vpc_authorizations_with_options_async(request, runtime)

    def describe_zone_info_with_options(
        self,
        request: main_models.DescribeZoneInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneInfo',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_info_with_options_async(
        self,
        request: main_models.DescribeZoneInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneInfo',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_info(
        self,
        request: main_models.DescribeZoneInfoRequest,
    ) -> main_models.DescribeZoneInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_zone_info_with_options(request, runtime)

    async def describe_zone_info_async(
        self,
        request: main_models.DescribeZoneInfoRequest,
    ) -> main_models.DescribeZoneInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_zone_info_with_options_async(request, runtime)

    def describe_zone_record_with_options(
        self,
        request: main_models.DescribeZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_record_with_options_async(
        self,
        request: main_models.DescribeZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_record(
        self,
        request: main_models.DescribeZoneRecordRequest,
    ) -> main_models.DescribeZoneRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_zone_record_with_options(request, runtime)

    async def describe_zone_record_async(
        self,
        request: main_models.DescribeZoneRecordRequest,
    ) -> main_models.DescribeZoneRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_zone_record_with_options_async(request, runtime)

    def describe_zone_records_with_options(
        self,
        request: main_models.DescribeZoneRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneRecords',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_records_with_options_async(
        self,
        request: main_models.DescribeZoneRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneRecords',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_records(
        self,
        request: main_models.DescribeZoneRecordsRequest,
    ) -> main_models.DescribeZoneRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_zone_records_with_options(request, runtime)

    async def describe_zone_records_async(
        self,
        request: main_models.DescribeZoneRecordsRequest,
    ) -> main_models.DescribeZoneRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_zone_records_with_options_async(request, runtime)

    def describe_zone_vpc_tree_with_options(
        self,
        request: main_models.DescribeZoneVpcTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneVpcTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneVpcTree',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneVpcTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_vpc_tree_with_options_async(
        self,
        request: main_models.DescribeZoneVpcTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZoneVpcTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZoneVpcTree',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZoneVpcTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zone_vpc_tree(
        self,
        request: main_models.DescribeZoneVpcTreeRequest,
    ) -> main_models.DescribeZoneVpcTreeResponse:
        runtime = RuntimeOptions()
        return self.describe_zone_vpc_tree_with_options(request, runtime)

    async def describe_zone_vpc_tree_async(
        self,
        request: main_models.DescribeZoneVpcTreeRequest,
    ) -> main_models.DescribeZoneVpcTreeResponse:
        runtime = RuntimeOptions()
        return await self.describe_zone_vpc_tree_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_region_id):
            query['QueryRegionId'] = request.query_region_id
        if not DaraCore.is_null(request.query_vpc_id):
            query['QueryVpcId'] = request.query_vpc_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_tag):
            query['ResourceTag'] = request.resource_tag
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not DaraCore.is_null(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_region_id):
            query['QueryRegionId'] = request.query_region_id
        if not DaraCore.is_null(request.query_vpc_id):
            query['QueryVpcId'] = request.query_vpc_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_tag):
            query['ResourceTag'] = request.resource_tag
        if not DaraCore.is_null(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not DaraCore.is_null(request.zone_tag):
            query['ZoneTag'] = request.zone_tag
        if not DaraCore.is_null(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2018-01-01',
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

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-01-01',
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

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2018-01-01',
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

    def search_custom_lines_with_options(
        self,
        request: main_models.SearchCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_timestamp_end):
            query['CreateTimestampEnd'] = request.create_timestamp_end
        if not DaraCore.is_null(request.create_timestamp_start):
            query['CreateTimestampStart'] = request.create_timestamp_start
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.ipv_4):
            query['Ipv4'] = request.ipv_4
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.update_timestamp_end):
            query['UpdateTimestampEnd'] = request.update_timestamp_end
        if not DaraCore.is_null(request.update_timestamp_start):
            query['UpdateTimestampStart'] = request.update_timestamp_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCustomLines',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_custom_lines_with_options_async(
        self,
        request: main_models.SearchCustomLinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchCustomLinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_timestamp_end):
            query['CreateTimestampEnd'] = request.create_timestamp_end
        if not DaraCore.is_null(request.create_timestamp_start):
            query['CreateTimestampStart'] = request.create_timestamp_start
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.ipv_4):
            query['Ipv4'] = request.ipv_4
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.update_timestamp_end):
            query['UpdateTimestampEnd'] = request.update_timestamp_end
        if not DaraCore.is_null(request.update_timestamp_start):
            query['UpdateTimestampStart'] = request.update_timestamp_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchCustomLines',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchCustomLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_custom_lines(
        self,
        request: main_models.SearchCustomLinesRequest,
    ) -> main_models.SearchCustomLinesResponse:
        runtime = RuntimeOptions()
        return self.search_custom_lines_with_options(request, runtime)

    async def search_custom_lines_async(
        self,
        request: main_models.SearchCustomLinesRequest,
    ) -> main_models.SearchCustomLinesResponse:
        runtime = RuntimeOptions()
        return await self.search_custom_lines_with_options_async(request, runtime)

    def set_proxy_pattern_with_options(
        self,
        request: main_models.SetProxyPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetProxyPatternResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetProxyPattern',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetProxyPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_proxy_pattern_with_options_async(
        self,
        request: main_models.SetProxyPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetProxyPatternResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_pattern):
            query['ProxyPattern'] = request.proxy_pattern
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetProxyPattern',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetProxyPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_proxy_pattern(
        self,
        request: main_models.SetProxyPatternRequest,
    ) -> main_models.SetProxyPatternResponse:
        runtime = RuntimeOptions()
        return self.set_proxy_pattern_with_options(request, runtime)

    async def set_proxy_pattern_async(
        self,
        request: main_models.SetProxyPatternRequest,
    ) -> main_models.SetProxyPatternResponse:
        runtime = RuntimeOptions()
        return await self.set_proxy_pattern_with_options_async(request, runtime)

    def set_zone_record_status_with_options(
        self,
        request: main_models.SetZoneRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetZoneRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetZoneRecordStatus',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetZoneRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_zone_record_status_with_options_async(
        self,
        request: main_models.SetZoneRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetZoneRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetZoneRecordStatus',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetZoneRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_zone_record_status(
        self,
        request: main_models.SetZoneRecordStatusRequest,
    ) -> main_models.SetZoneRecordStatusResponse:
        runtime = RuntimeOptions()
        return self.set_zone_record_status_with_options(request, runtime)

    async def set_zone_record_status_async(
        self,
        request: main_models.SetZoneRecordStatusRequest,
    ) -> main_models.SetZoneRecordStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_zone_record_status_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.over_write):
            query['OverWrite'] = request.over_write
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
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.over_write):
            query['OverWrite'] = request.over_write
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
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
            version = '2018-01-01',
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
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
            version = '2018-01-01',
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

    def update_custom_line_with_options(
        self,
        request: main_models.UpdateCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_category):
            query['DnsCategory'] = request.dns_category
        if not DaraCore.is_null(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomLine',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_line_with_options_async(
        self,
        request: main_models.UpdateCustomLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_category):
            query['DnsCategory'] = request.dns_category
        if not DaraCore.is_null(request.ipv_4s):
            query['Ipv4s'] = request.ipv_4s
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line_id):
            query['LineId'] = request.line_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomLine',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_line(
        self,
        request: main_models.UpdateCustomLineRequest,
    ) -> main_models.UpdateCustomLineResponse:
        runtime = RuntimeOptions()
        return self.update_custom_line_with_options(request, runtime)

    async def update_custom_line_async(
        self,
        request: main_models.UpdateCustomLineRequest,
    ) -> main_models.UpdateCustomLineResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_line_with_options_async(request, runtime)

    def update_record_remark_with_options(
        self,
        request: main_models.UpdateRecordRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordRemark',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_remark_with_options_async(
        self,
        request: main_models.UpdateRecordRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordRemark',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_remark(
        self,
        request: main_models.UpdateRecordRemarkRequest,
    ) -> main_models.UpdateRecordRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_record_remark_with_options(request, runtime)

    async def update_record_remark_async(
        self,
        request: main_models.UpdateRecordRemarkRequest,
    ) -> main_models.UpdateRecordRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_record_remark_with_options_async(request, runtime)

    def update_resolver_endpoint_with_options(
        self,
        request: main_models.UpdateResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResolverEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resolver_endpoint_with_options_async(
        self,
        request: main_models.UpdateResolverEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResolverEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.ip_config):
            query['IpConfig'] = request.ip_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResolverEndpoint',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResolverEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resolver_endpoint(
        self,
        request: main_models.UpdateResolverEndpointRequest,
    ) -> main_models.UpdateResolverEndpointResponse:
        runtime = RuntimeOptions()
        return self.update_resolver_endpoint_with_options(request, runtime)

    async def update_resolver_endpoint_async(
        self,
        request: main_models.UpdateResolverEndpointRequest,
    ) -> main_models.UpdateResolverEndpointResponse:
        runtime = RuntimeOptions()
        return await self.update_resolver_endpoint_with_options_async(request, runtime)

    def update_resolver_rule_with_options(
        self,
        request: main_models.UpdateResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.priority_forward_configs):
            query['PriorityForwardConfigs'] = request.priority_forward_configs
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResolverRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resolver_rule_with_options_async(
        self,
        request: main_models.UpdateResolverRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResolverRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.forward_ip):
            query['ForwardIp'] = request.forward_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.priority_forward_configs):
            query['PriorityForwardConfigs'] = request.priority_forward_configs
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResolverRule',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResolverRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resolver_rule(
        self,
        request: main_models.UpdateResolverRuleRequest,
    ) -> main_models.UpdateResolverRuleResponse:
        runtime = RuntimeOptions()
        return self.update_resolver_rule_with_options(request, runtime)

    async def update_resolver_rule_async(
        self,
        request: main_models.UpdateResolverRuleRequest,
    ) -> main_models.UpdateResolverRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_resolver_rule_with_options_async(request, runtime)

    def update_sync_ecs_host_task_with_options(
        self,
        request: main_models.UpdateSyncEcsHostTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSyncEcsHostTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSyncEcsHostTask',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSyncEcsHostTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sync_ecs_host_task_with_options_async(
        self,
        request: main_models.UpdateSyncEcsHostTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSyncEcsHostTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSyncEcsHostTask',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSyncEcsHostTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sync_ecs_host_task(
        self,
        request: main_models.UpdateSyncEcsHostTaskRequest,
    ) -> main_models.UpdateSyncEcsHostTaskResponse:
        runtime = RuntimeOptions()
        return self.update_sync_ecs_host_task_with_options(request, runtime)

    async def update_sync_ecs_host_task_async(
        self,
        request: main_models.UpdateSyncEcsHostTaskRequest,
    ) -> main_models.UpdateSyncEcsHostTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_sync_ecs_host_task_with_options_async(request, runtime)

    def update_zone_record_with_options(
        self,
        request: main_models.UpdateZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_zone_record_with_options_async(
        self,
        request: main_models.UpdateZoneRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateZoneRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        if not DaraCore.is_null(request.rr):
            query['Rr'] = request.rr
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        if not DaraCore.is_null(request.weight):
            query['Weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateZoneRecord',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_zone_record(
        self,
        request: main_models.UpdateZoneRecordRequest,
    ) -> main_models.UpdateZoneRecordResponse:
        runtime = RuntimeOptions()
        return self.update_zone_record_with_options(request, runtime)

    async def update_zone_record_async(
        self,
        request: main_models.UpdateZoneRecordRequest,
    ) -> main_models.UpdateZoneRecordResponse:
        runtime = RuntimeOptions()
        return await self.update_zone_record_with_options_async(request, runtime)

    def update_zone_remark_with_options(
        self,
        request: main_models.UpdateZoneRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateZoneRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateZoneRemark',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateZoneRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_zone_remark_with_options_async(
        self,
        request: main_models.UpdateZoneRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateZoneRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateZoneRemark',
            version = '2018-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateZoneRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_zone_remark(
        self,
        request: main_models.UpdateZoneRemarkRequest,
    ) -> main_models.UpdateZoneRemarkResponse:
        runtime = RuntimeOptions()
        return self.update_zone_remark_with_options(request, runtime)

    async def update_zone_remark_async(
        self,
        request: main_models.UpdateZoneRemarkRequest,
    ) -> main_models.UpdateZoneRemarkResponse:
        runtime = RuntimeOptions()
        return await self.update_zone_remark_with_options_async(request, runtime)
