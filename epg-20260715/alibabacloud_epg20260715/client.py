# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_epg20260715 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self._endpoint = self.get_endpoint('epg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ip_addresses_to_egress_proxy_ip_pool_with_options(
        self,
        request: main_models.AddIpAddressesToEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpAddressesToEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        body_flat = {}
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddIpAddressesToEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpAddressesToEgressProxyIpPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ip_addresses_to_egress_proxy_ip_pool_with_options_async(
        self,
        request: main_models.AddIpAddressesToEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpAddressesToEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        body_flat = {}
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddIpAddressesToEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpAddressesToEgressProxyIpPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ip_addresses_to_egress_proxy_ip_pool(
        self,
        request: main_models.AddIpAddressesToEgressProxyIpPoolRequest,
    ) -> main_models.AddIpAddressesToEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return self.add_ip_addresses_to_egress_proxy_ip_pool_with_options(request, runtime)

    async def add_ip_addresses_to_egress_proxy_ip_pool_async(
        self,
        request: main_models.AddIpAddressesToEgressProxyIpPoolRequest,
    ) -> main_models.AddIpAddressesToEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return await self.add_ip_addresses_to_egress_proxy_ip_pool_with_options_async(request, runtime)

    def attach_egress_proxy_rule_groups_to_configuration_with_options(
        self,
        request: main_models.AttachEgressProxyRuleGroupsToConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachEgressProxyRuleGroupsToConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_groups):
            body_flat['EgressProxyRuleGroups'] = request.egress_proxy_rule_groups
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachEgressProxyRuleGroupsToConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachEgressProxyRuleGroupsToConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_egress_proxy_rule_groups_to_configuration_with_options_async(
        self,
        request: main_models.AttachEgressProxyRuleGroupsToConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachEgressProxyRuleGroupsToConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_groups):
            body_flat['EgressProxyRuleGroups'] = request.egress_proxy_rule_groups
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachEgressProxyRuleGroupsToConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachEgressProxyRuleGroupsToConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_egress_proxy_rule_groups_to_configuration(
        self,
        request: main_models.AttachEgressProxyRuleGroupsToConfigurationRequest,
    ) -> main_models.AttachEgressProxyRuleGroupsToConfigurationResponse:
        runtime = RuntimeOptions()
        return self.attach_egress_proxy_rule_groups_to_configuration_with_options(request, runtime)

    async def attach_egress_proxy_rule_groups_to_configuration_async(
        self,
        request: main_models.AttachEgressProxyRuleGroupsToConfigurationRequest,
    ) -> main_models.AttachEgressProxyRuleGroupsToConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.attach_egress_proxy_rule_groups_to_configuration_with_options_async(request, runtime)

    def create_egress_proxy_configuration_with_options(
        self,
        request: main_models.CreateEgressProxyConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.default_rule_phase_actions):
            body_flat['DefaultRulePhaseActions'] = request.default_rule_phase_actions
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_name):
            body['EgressProxyConfigurationName'] = request.egress_proxy_configuration_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_egress_proxy_configuration_with_options_async(
        self,
        request: main_models.CreateEgressProxyConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.default_rule_phase_actions):
            body_flat['DefaultRulePhaseActions'] = request.default_rule_phase_actions
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_name):
            body['EgressProxyConfigurationName'] = request.egress_proxy_configuration_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_egress_proxy_configuration(
        self,
        request: main_models.CreateEgressProxyConfigurationRequest,
    ) -> main_models.CreateEgressProxyConfigurationResponse:
        runtime = RuntimeOptions()
        return self.create_egress_proxy_configuration_with_options(request, runtime)

    async def create_egress_proxy_configuration_async(
        self,
        request: main_models.CreateEgressProxyConfigurationRequest,
    ) -> main_models.CreateEgressProxyConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.create_egress_proxy_configuration_with_options_async(request, runtime)

    def create_egress_proxy_gateway_with_options(
        self,
        request: main_models.CreateEgressProxyGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        if not DaraCore.is_null(request.egress_proxy_gateway_name):
            body['EgressProxyGatewayName'] = request.egress_proxy_gateway_name
        body_flat = {}
        if not DaraCore.is_null(request.listener_properties):
            body_flat['ListenerProperties'] = request.listener_properties
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.tls_intercept_properties):
            body_flat['TlsInterceptProperties'] = request.tls_intercept_properties
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyGateway',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_egress_proxy_gateway_with_options_async(
        self,
        request: main_models.CreateEgressProxyGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        if not DaraCore.is_null(request.egress_proxy_gateway_name):
            body['EgressProxyGatewayName'] = request.egress_proxy_gateway_name
        body_flat = {}
        if not DaraCore.is_null(request.listener_properties):
            body_flat['ListenerProperties'] = request.listener_properties
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.tls_intercept_properties):
            body_flat['TlsInterceptProperties'] = request.tls_intercept_properties
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyGateway',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_egress_proxy_gateway(
        self,
        request: main_models.CreateEgressProxyGatewayRequest,
    ) -> main_models.CreateEgressProxyGatewayResponse:
        runtime = RuntimeOptions()
        return self.create_egress_proxy_gateway_with_options(request, runtime)

    async def create_egress_proxy_gateway_async(
        self,
        request: main_models.CreateEgressProxyGatewayRequest,
    ) -> main_models.CreateEgressProxyGatewayResponse:
        runtime = RuntimeOptions()
        return await self.create_egress_proxy_gateway_with_options_async(request, runtime)

    def create_egress_proxy_ip_pool_with_options(
        self,
        request: main_models.CreateEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        if not DaraCore.is_null(request.egress_proxy_ip_pool_name):
            body['EgressProxyIpPoolName'] = request.egress_proxy_ip_pool_name
        if not DaraCore.is_null(request.hash_factor):
            body['HashFactor'] = request.hash_factor
        if not DaraCore.is_null(request.hash_header_name):
            body['HashHeaderName'] = request.hash_header_name
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        body_flat = {}
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyIpPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_egress_proxy_ip_pool_with_options_async(
        self,
        request: main_models.CreateEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        if not DaraCore.is_null(request.egress_proxy_ip_pool_name):
            body['EgressProxyIpPoolName'] = request.egress_proxy_ip_pool_name
        if not DaraCore.is_null(request.hash_factor):
            body['HashFactor'] = request.hash_factor
        if not DaraCore.is_null(request.hash_header_name):
            body['HashHeaderName'] = request.hash_header_name
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        body_flat = {}
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyIpPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_egress_proxy_ip_pool(
        self,
        request: main_models.CreateEgressProxyIpPoolRequest,
    ) -> main_models.CreateEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return self.create_egress_proxy_ip_pool_with_options(request, runtime)

    async def create_egress_proxy_ip_pool_async(
        self,
        request: main_models.CreateEgressProxyIpPoolRequest,
    ) -> main_models.CreateEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return await self.create_egress_proxy_ip_pool_with_options_async(request, runtime)

    def create_egress_proxy_rule_group_with_options(
        self,
        request: main_models.CreateEgressProxyRuleGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyRuleGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.egress_proxy_rule_group_name):
            body['EgressProxyRuleGroupName'] = request.egress_proxy_rule_group_name
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rules):
            body_flat['EgressProxyRules'] = request.egress_proxy_rules
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyRuleGroup',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyRuleGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_egress_proxy_rule_group_with_options_async(
        self,
        request: main_models.CreateEgressProxyRuleGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyRuleGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.egress_proxy_rule_group_name):
            body['EgressProxyRuleGroupName'] = request.egress_proxy_rule_group_name
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rules):
            body_flat['EgressProxyRules'] = request.egress_proxy_rules
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyRuleGroup',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyRuleGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_egress_proxy_rule_group(
        self,
        request: main_models.CreateEgressProxyRuleGroupRequest,
    ) -> main_models.CreateEgressProxyRuleGroupResponse:
        runtime = RuntimeOptions()
        return self.create_egress_proxy_rule_group_with_options(request, runtime)

    async def create_egress_proxy_rule_group_async(
        self,
        request: main_models.CreateEgressProxyRuleGroupRequest,
    ) -> main_models.CreateEgressProxyRuleGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_egress_proxy_rule_group_with_options_async(request, runtime)

    def create_egress_proxy_rules_with_options(
        self,
        request: main_models.CreateEgressProxyRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rules):
            body_flat['EgressProxyRules'] = request.egress_proxy_rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyRules',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_egress_proxy_rules_with_options_async(
        self,
        request: main_models.CreateEgressProxyRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEgressProxyRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rules):
            body_flat['EgressProxyRules'] = request.egress_proxy_rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEgressProxyRules',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEgressProxyRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_egress_proxy_rules(
        self,
        request: main_models.CreateEgressProxyRulesRequest,
    ) -> main_models.CreateEgressProxyRulesResponse:
        runtime = RuntimeOptions()
        return self.create_egress_proxy_rules_with_options(request, runtime)

    async def create_egress_proxy_rules_async(
        self,
        request: main_models.CreateEgressProxyRulesRequest,
    ) -> main_models.CreateEgressProxyRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_egress_proxy_rules_with_options_async(request, runtime)

    def delete_egress_proxy_configuration_with_options(
        self,
        request: main_models.DeleteEgressProxyConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_egress_proxy_configuration_with_options_async(
        self,
        request: main_models.DeleteEgressProxyConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_egress_proxy_configuration(
        self,
        request: main_models.DeleteEgressProxyConfigurationRequest,
    ) -> main_models.DeleteEgressProxyConfigurationResponse:
        runtime = RuntimeOptions()
        return self.delete_egress_proxy_configuration_with_options(request, runtime)

    async def delete_egress_proxy_configuration_async(
        self,
        request: main_models.DeleteEgressProxyConfigurationRequest,
    ) -> main_models.DeleteEgressProxyConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.delete_egress_proxy_configuration_with_options_async(request, runtime)

    def delete_egress_proxy_gateway_with_options(
        self,
        request: main_models.DeleteEgressProxyGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyGateway',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_egress_proxy_gateway_with_options_async(
        self,
        request: main_models.DeleteEgressProxyGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyGateway',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_egress_proxy_gateway(
        self,
        request: main_models.DeleteEgressProxyGatewayRequest,
    ) -> main_models.DeleteEgressProxyGatewayResponse:
        runtime = RuntimeOptions()
        return self.delete_egress_proxy_gateway_with_options(request, runtime)

    async def delete_egress_proxy_gateway_async(
        self,
        request: main_models.DeleteEgressProxyGatewayRequest,
    ) -> main_models.DeleteEgressProxyGatewayResponse:
        runtime = RuntimeOptions()
        return await self.delete_egress_proxy_gateway_with_options_async(request, runtime)

    def delete_egress_proxy_ip_pool_with_options(
        self,
        request: main_models.DeleteEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyIpPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_egress_proxy_ip_pool_with_options_async(
        self,
        request: main_models.DeleteEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyIpPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_egress_proxy_ip_pool(
        self,
        request: main_models.DeleteEgressProxyIpPoolRequest,
    ) -> main_models.DeleteEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return self.delete_egress_proxy_ip_pool_with_options(request, runtime)

    async def delete_egress_proxy_ip_pool_async(
        self,
        request: main_models.DeleteEgressProxyIpPoolRequest,
    ) -> main_models.DeleteEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_egress_proxy_ip_pool_with_options_async(request, runtime)

    def delete_egress_proxy_rule_group_with_options(
        self,
        request: main_models.DeleteEgressProxyRuleGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyRuleGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyRuleGroup',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyRuleGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_egress_proxy_rule_group_with_options_async(
        self,
        request: main_models.DeleteEgressProxyRuleGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyRuleGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyRuleGroup',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyRuleGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_egress_proxy_rule_group(
        self,
        request: main_models.DeleteEgressProxyRuleGroupRequest,
    ) -> main_models.DeleteEgressProxyRuleGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_egress_proxy_rule_group_with_options(request, runtime)

    async def delete_egress_proxy_rule_group_async(
        self,
        request: main_models.DeleteEgressProxyRuleGroupRequest,
    ) -> main_models.DeleteEgressProxyRuleGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_egress_proxy_rule_group_with_options_async(request, runtime)

    def delete_egress_proxy_rules_with_options(
        self,
        request: main_models.DeleteEgressProxyRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_ids):
            body_flat['EgressProxyRuleIds'] = request.egress_proxy_rule_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyRules',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_egress_proxy_rules_with_options_async(
        self,
        request: main_models.DeleteEgressProxyRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEgressProxyRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_ids):
            body_flat['EgressProxyRuleIds'] = request.egress_proxy_rule_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEgressProxyRules',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEgressProxyRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_egress_proxy_rules(
        self,
        request: main_models.DeleteEgressProxyRulesRequest,
    ) -> main_models.DeleteEgressProxyRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_egress_proxy_rules_with_options(request, runtime)

    async def delete_egress_proxy_rules_async(
        self,
        request: main_models.DeleteEgressProxyRulesRequest,
    ) -> main_models.DeleteEgressProxyRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_egress_proxy_rules_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-07-15',
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

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2026-07-15',
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

    def detach_egress_proxy_rule_groups_from_configuration_with_options(
        self,
        request: main_models.DetachEgressProxyRuleGroupsFromConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachEgressProxyRuleGroupsFromConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_group_ids):
            body_flat['EgressProxyRuleGroupIds'] = request.egress_proxy_rule_group_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachEgressProxyRuleGroupsFromConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachEgressProxyRuleGroupsFromConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_egress_proxy_rule_groups_from_configuration_with_options_async(
        self,
        request: main_models.DetachEgressProxyRuleGroupsFromConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachEgressProxyRuleGroupsFromConfigurationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_group_ids):
            body_flat['EgressProxyRuleGroupIds'] = request.egress_proxy_rule_group_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachEgressProxyRuleGroupsFromConfiguration',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachEgressProxyRuleGroupsFromConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_egress_proxy_rule_groups_from_configuration(
        self,
        request: main_models.DetachEgressProxyRuleGroupsFromConfigurationRequest,
    ) -> main_models.DetachEgressProxyRuleGroupsFromConfigurationResponse:
        runtime = RuntimeOptions()
        return self.detach_egress_proxy_rule_groups_from_configuration_with_options(request, runtime)

    async def detach_egress_proxy_rule_groups_from_configuration_async(
        self,
        request: main_models.DetachEgressProxyRuleGroupsFromConfigurationRequest,
    ) -> main_models.DetachEgressProxyRuleGroupsFromConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.detach_egress_proxy_rule_groups_from_configuration_with_options_async(request, runtime)

    def get_egress_proxy_configuration_attribute_with_options(
        self,
        request: main_models.GetEgressProxyConfigurationAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyConfigurationAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyConfigurationAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyConfigurationAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_egress_proxy_configuration_attribute_with_options_async(
        self,
        request: main_models.GetEgressProxyConfigurationAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyConfigurationAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyConfigurationAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyConfigurationAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_egress_proxy_configuration_attribute(
        self,
        request: main_models.GetEgressProxyConfigurationAttributeRequest,
    ) -> main_models.GetEgressProxyConfigurationAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_egress_proxy_configuration_attribute_with_options(request, runtime)

    async def get_egress_proxy_configuration_attribute_async(
        self,
        request: main_models.GetEgressProxyConfigurationAttributeRequest,
    ) -> main_models.GetEgressProxyConfigurationAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_egress_proxy_configuration_attribute_with_options_async(request, runtime)

    def get_egress_proxy_gateway_attribute_with_options(
        self,
        request: main_models.GetEgressProxyGatewayAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyGatewayAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyGatewayAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyGatewayAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_egress_proxy_gateway_attribute_with_options_async(
        self,
        request: main_models.GetEgressProxyGatewayAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyGatewayAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyGatewayAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyGatewayAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_egress_proxy_gateway_attribute(
        self,
        request: main_models.GetEgressProxyGatewayAttributeRequest,
    ) -> main_models.GetEgressProxyGatewayAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_egress_proxy_gateway_attribute_with_options(request, runtime)

    async def get_egress_proxy_gateway_attribute_async(
        self,
        request: main_models.GetEgressProxyGatewayAttributeRequest,
    ) -> main_models.GetEgressProxyGatewayAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_egress_proxy_gateway_attribute_with_options_async(request, runtime)

    def get_egress_proxy_ip_pool_attribute_with_options(
        self,
        request: main_models.GetEgressProxyIpPoolAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyIpPoolAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyIpPoolAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyIpPoolAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_egress_proxy_ip_pool_attribute_with_options_async(
        self,
        request: main_models.GetEgressProxyIpPoolAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyIpPoolAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyIpPoolAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyIpPoolAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_egress_proxy_ip_pool_attribute(
        self,
        request: main_models.GetEgressProxyIpPoolAttributeRequest,
    ) -> main_models.GetEgressProxyIpPoolAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_egress_proxy_ip_pool_attribute_with_options(request, runtime)

    async def get_egress_proxy_ip_pool_attribute_async(
        self,
        request: main_models.GetEgressProxyIpPoolAttributeRequest,
    ) -> main_models.GetEgressProxyIpPoolAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_egress_proxy_ip_pool_attribute_with_options_async(request, runtime)

    def get_egress_proxy_rule_group_attribute_with_options(
        self,
        request: main_models.GetEgressProxyRuleGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyRuleGroupAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyRuleGroupAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyRuleGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_egress_proxy_rule_group_attribute_with_options_async(
        self,
        request: main_models.GetEgressProxyRuleGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEgressProxyRuleGroupAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEgressProxyRuleGroupAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEgressProxyRuleGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_egress_proxy_rule_group_attribute(
        self,
        request: main_models.GetEgressProxyRuleGroupAttributeRequest,
    ) -> main_models.GetEgressProxyRuleGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_egress_proxy_rule_group_attribute_with_options(request, runtime)

    async def get_egress_proxy_rule_group_attribute_async(
        self,
        request: main_models.GetEgressProxyRuleGroupAttributeRequest,
    ) -> main_models.GetEgressProxyRuleGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_egress_proxy_rule_group_attribute_with_options_async(request, runtime)

    def list_egress_proxy_configurations_with_options(
        self,
        request: main_models.ListEgressProxyConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyConfigurationsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_configuration_ids):
            body_flat['EgressProxyConfigurationIds'] = request.egress_proxy_configuration_ids
        if not DaraCore.is_null(request.egress_proxy_configuration_names):
            body_flat['EgressProxyConfigurationNames'] = request.egress_proxy_configuration_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyConfigurations',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_egress_proxy_configurations_with_options_async(
        self,
        request: main_models.ListEgressProxyConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyConfigurationsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_configuration_ids):
            body_flat['EgressProxyConfigurationIds'] = request.egress_proxy_configuration_ids
        if not DaraCore.is_null(request.egress_proxy_configuration_names):
            body_flat['EgressProxyConfigurationNames'] = request.egress_proxy_configuration_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyConfigurations',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_egress_proxy_configurations(
        self,
        request: main_models.ListEgressProxyConfigurationsRequest,
    ) -> main_models.ListEgressProxyConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.list_egress_proxy_configurations_with_options(request, runtime)

    async def list_egress_proxy_configurations_async(
        self,
        request: main_models.ListEgressProxyConfigurationsRequest,
    ) -> main_models.ListEgressProxyConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.list_egress_proxy_configurations_with_options_async(request, runtime)

    def list_egress_proxy_gateways_with_options(
        self,
        request: main_models.ListEgressProxyGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyGatewaysResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_configuration_ids):
            body_flat['EgressProxyConfigurationIds'] = request.egress_proxy_configuration_ids
        if not DaraCore.is_null(request.egress_proxy_gateway_ids):
            body_flat['EgressProxyGatewayIds'] = request.egress_proxy_gateway_ids
        if not DaraCore.is_null(request.egress_proxy_gateway_names):
            body_flat['EgressProxyGatewayNames'] = request.egress_proxy_gateway_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_ids):
            body_flat['VpcIds'] = request.vpc_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyGateways',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_egress_proxy_gateways_with_options_async(
        self,
        request: main_models.ListEgressProxyGatewaysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyGatewaysResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_configuration_ids):
            body_flat['EgressProxyConfigurationIds'] = request.egress_proxy_configuration_ids
        if not DaraCore.is_null(request.egress_proxy_gateway_ids):
            body_flat['EgressProxyGatewayIds'] = request.egress_proxy_gateway_ids
        if not DaraCore.is_null(request.egress_proxy_gateway_names):
            body_flat['EgressProxyGatewayNames'] = request.egress_proxy_gateway_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_ids):
            body_flat['VpcIds'] = request.vpc_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyGateways',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_egress_proxy_gateways(
        self,
        request: main_models.ListEgressProxyGatewaysRequest,
    ) -> main_models.ListEgressProxyGatewaysResponse:
        runtime = RuntimeOptions()
        return self.list_egress_proxy_gateways_with_options(request, runtime)

    async def list_egress_proxy_gateways_async(
        self,
        request: main_models.ListEgressProxyGatewaysRequest,
    ) -> main_models.ListEgressProxyGatewaysResponse:
        runtime = RuntimeOptions()
        return await self.list_egress_proxy_gateways_with_options_async(request, runtime)

    def list_egress_proxy_ip_pools_with_options(
        self,
        request: main_models.ListEgressProxyIpPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyIpPoolsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_gateway_ids):
            body_flat['EgressProxyGatewayIds'] = request.egress_proxy_gateway_ids
        if not DaraCore.is_null(request.egress_proxy_ip_pool_ids):
            body_flat['EgressProxyIpPoolIds'] = request.egress_proxy_ip_pool_ids
        if not DaraCore.is_null(request.egress_proxy_ip_pool_names):
            body_flat['EgressProxyIpPoolNames'] = request.egress_proxy_ip_pool_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyIpPools',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyIpPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_egress_proxy_ip_pools_with_options_async(
        self,
        request: main_models.ListEgressProxyIpPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyIpPoolsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_gateway_ids):
            body_flat['EgressProxyGatewayIds'] = request.egress_proxy_gateway_ids
        if not DaraCore.is_null(request.egress_proxy_ip_pool_ids):
            body_flat['EgressProxyIpPoolIds'] = request.egress_proxy_ip_pool_ids
        if not DaraCore.is_null(request.egress_proxy_ip_pool_names):
            body_flat['EgressProxyIpPoolNames'] = request.egress_proxy_ip_pool_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyIpPools',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyIpPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_egress_proxy_ip_pools(
        self,
        request: main_models.ListEgressProxyIpPoolsRequest,
    ) -> main_models.ListEgressProxyIpPoolsResponse:
        runtime = RuntimeOptions()
        return self.list_egress_proxy_ip_pools_with_options(request, runtime)

    async def list_egress_proxy_ip_pools_async(
        self,
        request: main_models.ListEgressProxyIpPoolsRequest,
    ) -> main_models.ListEgressProxyIpPoolsResponse:
        runtime = RuntimeOptions()
        return await self.list_egress_proxy_ip_pools_with_options_async(request, runtime)

    def list_egress_proxy_rule_groups_with_options(
        self,
        request: main_models.ListEgressProxyRuleGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyRuleGroupsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_group_ids):
            body_flat['EgressProxyRuleGroupIds'] = request.egress_proxy_rule_group_ids
        if not DaraCore.is_null(request.egress_proxy_rule_group_names):
            body_flat['EgressProxyRuleGroupNames'] = request.egress_proxy_rule_group_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyRuleGroups',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyRuleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_egress_proxy_rule_groups_with_options_async(
        self,
        request: main_models.ListEgressProxyRuleGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEgressProxyRuleGroupsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rule_group_ids):
            body_flat['EgressProxyRuleGroupIds'] = request.egress_proxy_rule_group_ids
        if not DaraCore.is_null(request.egress_proxy_rule_group_names):
            body_flat['EgressProxyRuleGroupNames'] = request.egress_proxy_rule_group_names
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEgressProxyRuleGroups',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEgressProxyRuleGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_egress_proxy_rule_groups(
        self,
        request: main_models.ListEgressProxyRuleGroupsRequest,
    ) -> main_models.ListEgressProxyRuleGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_egress_proxy_rule_groups_with_options(request, runtime)

    async def list_egress_proxy_rule_groups_async(
        self,
        request: main_models.ListEgressProxyRuleGroupsRequest,
    ) -> main_models.ListEgressProxyRuleGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_egress_proxy_rule_groups_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2026-07-15',
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

    def remove_ip_addresses_from_egress_proxy_ip_pool_with_options(
        self,
        request: main_models.RemoveIpAddressesFromEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpAddressesFromEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        body_flat = {}
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpAddressesFromEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpAddressesFromEgressProxyIpPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_addresses_from_egress_proxy_ip_pool_with_options_async(
        self,
        request: main_models.RemoveIpAddressesFromEgressProxyIpPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpAddressesFromEgressProxyIpPoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        body_flat = {}
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpAddressesFromEgressProxyIpPool',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpAddressesFromEgressProxyIpPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_addresses_from_egress_proxy_ip_pool(
        self,
        request: main_models.RemoveIpAddressesFromEgressProxyIpPoolRequest,
    ) -> main_models.RemoveIpAddressesFromEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return self.remove_ip_addresses_from_egress_proxy_ip_pool_with_options(request, runtime)

    async def remove_ip_addresses_from_egress_proxy_ip_pool_async(
        self,
        request: main_models.RemoveIpAddressesFromEgressProxyIpPoolRequest,
    ) -> main_models.RemoveIpAddressesFromEgressProxyIpPoolResponse:
        runtime = RuntimeOptions()
        return await self.remove_ip_addresses_from_egress_proxy_ip_pool_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2026-07-15',
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
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2026-07-15',
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

    def update_egress_proxy_configuration_attribute_with_options(
        self,
        request: main_models.UpdateEgressProxyConfigurationAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyConfigurationAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.default_rule_phase_actions):
            body_flat['DefaultRulePhaseActions'] = request.default_rule_phase_actions
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        if not DaraCore.is_null(request.egress_proxy_configuration_name):
            body['EgressProxyConfigurationName'] = request.egress_proxy_configuration_name
        if not DaraCore.is_null(request.egress_proxy_rule_groups):
            body_flat['EgressProxyRuleGroups'] = request.egress_proxy_rule_groups
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyConfigurationAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyConfigurationAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_egress_proxy_configuration_attribute_with_options_async(
        self,
        request: main_models.UpdateEgressProxyConfigurationAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyConfigurationAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.default_rule_phase_actions):
            body_flat['DefaultRulePhaseActions'] = request.default_rule_phase_actions
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_configuration_id):
            body['EgressProxyConfigurationId'] = request.egress_proxy_configuration_id
        if not DaraCore.is_null(request.egress_proxy_configuration_name):
            body['EgressProxyConfigurationName'] = request.egress_proxy_configuration_name
        if not DaraCore.is_null(request.egress_proxy_rule_groups):
            body_flat['EgressProxyRuleGroups'] = request.egress_proxy_rule_groups
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyConfigurationAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyConfigurationAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_egress_proxy_configuration_attribute(
        self,
        request: main_models.UpdateEgressProxyConfigurationAttributeRequest,
    ) -> main_models.UpdateEgressProxyConfigurationAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_egress_proxy_configuration_attribute_with_options(request, runtime)

    async def update_egress_proxy_configuration_attribute_async(
        self,
        request: main_models.UpdateEgressProxyConfigurationAttributeRequest,
    ) -> main_models.UpdateEgressProxyConfigurationAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_egress_proxy_configuration_attribute_with_options_async(request, runtime)

    def update_egress_proxy_gateway_attribute_with_options(
        self,
        request: main_models.UpdateEgressProxyGatewayAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyGatewayAttributeResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.add_listener_properties):
            body_flat['AddListenerProperties'] = request.add_listener_properties
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_egress_proxy_ip_pool_id):
            body['DefaultEgressProxyIpPoolId'] = request.default_egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        if not DaraCore.is_null(request.egress_proxy_gateway_name):
            body['EgressProxyGatewayName'] = request.egress_proxy_gateway_name
        if not DaraCore.is_null(request.remove_listener_properties):
            body_flat['RemoveListenerProperties'] = request.remove_listener_properties
        if not DaraCore.is_null(request.tls_intercept_properties):
            body_flat['TlsInterceptProperties'] = request.tls_intercept_properties
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyGatewayAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyGatewayAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_egress_proxy_gateway_attribute_with_options_async(
        self,
        request: main_models.UpdateEgressProxyGatewayAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyGatewayAttributeResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.add_listener_properties):
            body_flat['AddListenerProperties'] = request.add_listener_properties
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_egress_proxy_ip_pool_id):
            body['DefaultEgressProxyIpPoolId'] = request.default_egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_gateway_id):
            body['EgressProxyGatewayId'] = request.egress_proxy_gateway_id
        if not DaraCore.is_null(request.egress_proxy_gateway_name):
            body['EgressProxyGatewayName'] = request.egress_proxy_gateway_name
        if not DaraCore.is_null(request.remove_listener_properties):
            body_flat['RemoveListenerProperties'] = request.remove_listener_properties
        if not DaraCore.is_null(request.tls_intercept_properties):
            body_flat['TlsInterceptProperties'] = request.tls_intercept_properties
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyGatewayAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyGatewayAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_egress_proxy_gateway_attribute(
        self,
        request: main_models.UpdateEgressProxyGatewayAttributeRequest,
    ) -> main_models.UpdateEgressProxyGatewayAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_egress_proxy_gateway_attribute_with_options(request, runtime)

    async def update_egress_proxy_gateway_attribute_async(
        self,
        request: main_models.UpdateEgressProxyGatewayAttributeRequest,
    ) -> main_models.UpdateEgressProxyGatewayAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_egress_proxy_gateway_attribute_with_options_async(request, runtime)

    def update_egress_proxy_ip_pool_attribute_with_options(
        self,
        request: main_models.UpdateEgressProxyIpPoolAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyIpPoolAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.egress_proxy_ip_pool_name):
            body['EgressProxyIpPoolName'] = request.egress_proxy_ip_pool_name
        if not DaraCore.is_null(request.hash_factor):
            body['HashFactor'] = request.hash_factor
        if not DaraCore.is_null(request.hash_header_name):
            body['HashHeaderName'] = request.hash_header_name
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyIpPoolAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyIpPoolAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_egress_proxy_ip_pool_attribute_with_options_async(
        self,
        request: main_models.UpdateEgressProxyIpPoolAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyIpPoolAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.egress_proxy_ip_pool_name):
            body['EgressProxyIpPoolName'] = request.egress_proxy_ip_pool_name
        if not DaraCore.is_null(request.hash_factor):
            body['HashFactor'] = request.hash_factor
        if not DaraCore.is_null(request.hash_header_name):
            body['HashHeaderName'] = request.hash_header_name
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyIpPoolAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyIpPoolAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_egress_proxy_ip_pool_attribute(
        self,
        request: main_models.UpdateEgressProxyIpPoolAttributeRequest,
    ) -> main_models.UpdateEgressProxyIpPoolAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_egress_proxy_ip_pool_attribute_with_options(request, runtime)

    async def update_egress_proxy_ip_pool_attribute_async(
        self,
        request: main_models.UpdateEgressProxyIpPoolAttributeRequest,
    ) -> main_models.UpdateEgressProxyIpPoolAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_egress_proxy_ip_pool_attribute_with_options_async(request, runtime)

    def update_egress_proxy_rule_group_attribute_with_options(
        self,
        request: main_models.UpdateEgressProxyRuleGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyRuleGroupAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        if not DaraCore.is_null(request.egress_proxy_rule_group_name):
            body['EgressProxyRuleGroupName'] = request.egress_proxy_rule_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyRuleGroupAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyRuleGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_egress_proxy_rule_group_attribute_with_options_async(
        self,
        request: main_models.UpdateEgressProxyRuleGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyRuleGroupAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_ip_pool_id):
            body['EgressProxyIpPoolId'] = request.egress_proxy_ip_pool_id
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        if not DaraCore.is_null(request.egress_proxy_rule_group_name):
            body['EgressProxyRuleGroupName'] = request.egress_proxy_rule_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyRuleGroupAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyRuleGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_egress_proxy_rule_group_attribute(
        self,
        request: main_models.UpdateEgressProxyRuleGroupAttributeRequest,
    ) -> main_models.UpdateEgressProxyRuleGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_egress_proxy_rule_group_attribute_with_options(request, runtime)

    async def update_egress_proxy_rule_group_attribute_async(
        self,
        request: main_models.UpdateEgressProxyRuleGroupAttributeRequest,
    ) -> main_models.UpdateEgressProxyRuleGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_egress_proxy_rule_group_attribute_with_options_async(request, runtime)

    def update_egress_proxy_rules_attribute_with_options(
        self,
        request: main_models.UpdateEgressProxyRulesAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyRulesAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rules):
            body_flat['EgressProxyRules'] = request.egress_proxy_rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyRulesAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyRulesAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_egress_proxy_rules_attribute_with_options_async(
        self,
        request: main_models.UpdateEgressProxyRulesAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEgressProxyRulesAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.egress_proxy_rule_group_id):
            body['EgressProxyRuleGroupId'] = request.egress_proxy_rule_group_id
        body_flat = {}
        if not DaraCore.is_null(request.egress_proxy_rules):
            body_flat['EgressProxyRules'] = request.egress_proxy_rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEgressProxyRulesAttribute',
            version = '2026-07-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEgressProxyRulesAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_egress_proxy_rules_attribute(
        self,
        request: main_models.UpdateEgressProxyRulesAttributeRequest,
    ) -> main_models.UpdateEgressProxyRulesAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_egress_proxy_rules_attribute_with_options(request, runtime)

    async def update_egress_proxy_rules_attribute_async(
        self,
        request: main_models.UpdateEgressProxyRulesAttributeRequest,
    ) -> main_models.UpdateEgressProxyRulesAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_egress_proxy_rules_attribute_with_options_async(request, runtime)
