# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ddoscoo20171228 import models as main_models
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
        self._endpoint = self.get_endpoint('ddoscoo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_layer_7ccrule_with_options(
        self,
        request: main_models.AddLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddLayer7CCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_layer_7ccrule_with_options_async(
        self,
        request: main_models.AddLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddLayer7CCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_layer_7ccrule(
        self,
        request: main_models.AddLayer7CCRuleRequest,
    ) -> main_models.AddLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return self.add_layer_7ccrule_with_options(request, runtime)

    async def add_layer_7ccrule_async(
        self,
        request: main_models.AddLayer7CCRuleRequest,
    ) -> main_models.AddLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return await self.add_layer_7ccrule_with_options_async(request, runtime)

    def close_domain_sls_config_with_options(
        self,
        request: main_models.CloseDomainSlsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseDomainSlsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseDomainSlsConfig',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseDomainSlsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_domain_sls_config_with_options_async(
        self,
        request: main_models.CloseDomainSlsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseDomainSlsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseDomainSlsConfig',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseDomainSlsConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_domain_sls_config(
        self,
        request: main_models.CloseDomainSlsConfigRequest,
    ) -> main_models.CloseDomainSlsConfigResponse:
        runtime = RuntimeOptions()
        return self.close_domain_sls_config_with_options(request, runtime)

    async def close_domain_sls_config_async(
        self,
        request: main_models.CloseDomainSlsConfigRequest,
    ) -> main_models.CloseDomainSlsConfigResponse:
        runtime = RuntimeOptions()
        return await self.close_domain_sls_config_with_options_async(request, runtime)

    def config_health_check_with_options(
        self,
        request: main_models.ConfigHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigHealthCheck',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_health_check_with_options_async(
        self,
        request: main_models.ConfigHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigHealthCheck',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_health_check(
        self,
        request: main_models.ConfigHealthCheckRequest,
    ) -> main_models.ConfigHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.config_health_check_with_options(request, runtime)

    async def config_health_check_async(
        self,
        request: main_models.ConfigHealthCheckRequest,
    ) -> main_models.ConfigHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.config_health_check_with_options_async(request, runtime)

    def config_layer_4rule_with_options(
        self,
        tmp_req: main_models.ConfigLayer4RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RuleResponse:
        tmp_req.validate()
        request = main_models.ConfigLayer4RuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.us_timeout):
            request.us_timeout_shrink = Utils.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4rule_with_options_async(
        self,
        tmp_req: main_models.ConfigLayer4RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RuleResponse:
        tmp_req.validate()
        request = main_models.ConfigLayer4RuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.us_timeout):
            request.us_timeout_shrink = Utils.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4rule(
        self,
        request: main_models.ConfigLayer4RuleRequest,
    ) -> main_models.ConfigLayer4RuleResponse:
        runtime = RuntimeOptions()
        return self.config_layer_4rule_with_options(request, runtime)

    async def config_layer_4rule_async(
        self,
        request: main_models.ConfigLayer4RuleRequest,
    ) -> main_models.ConfigLayer4RuleResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_4rule_with_options_async(request, runtime)

    def config_layer_4rule_attribute_with_options(
        self,
        request: main_models.ConfigLayer4RuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RuleAttribute',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4rule_attribute_with_options_async(
        self,
        request: main_models.ConfigLayer4RuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RuleAttribute',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4rule_attribute(
        self,
        request: main_models.ConfigLayer4RuleAttributeRequest,
    ) -> main_models.ConfigLayer4RuleAttributeResponse:
        runtime = RuntimeOptions()
        return self.config_layer_4rule_attribute_with_options(request, runtime)

    async def config_layer_4rule_attribute_async(
        self,
        request: main_models.ConfigLayer4RuleAttributeRequest,
    ) -> main_models.ConfigLayer4RuleAttributeResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_4rule_attribute_with_options_async(request, runtime)

    def config_layer_7black_white_list_with_options(
        self,
        request: main_models.ConfigLayer7BlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7BlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_list):
            query['BlackList'] = request.black_list
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7BlackWhiteList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7BlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_7black_white_list_with_options_async(
        self,
        request: main_models.ConfigLayer7BlackWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7BlackWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_list):
            query['BlackList'] = request.black_list
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7BlackWhiteList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7BlackWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_7black_white_list(
        self,
        request: main_models.ConfigLayer7BlackWhiteListRequest,
    ) -> main_models.ConfigLayer7BlackWhiteListResponse:
        runtime = RuntimeOptions()
        return self.config_layer_7black_white_list_with_options(request, runtime)

    async def config_layer_7black_white_list_async(
        self,
        request: main_models.ConfigLayer7BlackWhiteListRequest,
    ) -> main_models.ConfigLayer7BlackWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_7black_white_list_with_options_async(request, runtime)

    def config_layer_7ccrule_with_options(
        self,
        request: main_models.ConfigLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7CCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_7ccrule_with_options_async(
        self,
        request: main_models.ConfigLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7CCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_7ccrule(
        self,
        request: main_models.ConfigLayer7CCRuleRequest,
    ) -> main_models.ConfigLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return self.config_layer_7ccrule_with_options(request, runtime)

    async def config_layer_7ccrule_async(
        self,
        request: main_models.ConfigLayer7CCRuleRequest,
    ) -> main_models.ConfigLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_7ccrule_with_options_async(request, runtime)

    def config_layer_7cctemplate_with_options(
        self,
        request: main_models.ConfigLayer7CCTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7CCTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7CCTemplate',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7CCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_7cctemplate_with_options_async(
        self,
        request: main_models.ConfigLayer7CCTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7CCTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7CCTemplate',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7CCTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_7cctemplate(
        self,
        request: main_models.ConfigLayer7CCTemplateRequest,
    ) -> main_models.ConfigLayer7CCTemplateResponse:
        runtime = RuntimeOptions()
        return self.config_layer_7cctemplate_with_options(request, runtime)

    async def config_layer_7cctemplate_async(
        self,
        request: main_models.ConfigLayer7CCTemplateRequest,
    ) -> main_models.ConfigLayer7CCTemplateResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_7cctemplate_with_options_async(request, runtime)

    def config_layer_7cert_with_options(
        self,
        request: main_models.ConfigLayer7CertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7CertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert):
            query['Cert'] = request.cert
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7Cert',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7CertResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_7cert_with_options_async(
        self,
        request: main_models.ConfigLayer7CertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7CertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert):
            query['Cert'] = request.cert
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7Cert',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7CertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_7cert(
        self,
        request: main_models.ConfigLayer7CertRequest,
    ) -> main_models.ConfigLayer7CertResponse:
        runtime = RuntimeOptions()
        return self.config_layer_7cert_with_options(request, runtime)

    async def config_layer_7cert_async(
        self,
        request: main_models.ConfigLayer7CertRequest,
    ) -> main_models.ConfigLayer7CertResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_7cert_with_options_async(request, runtime)

    def config_layer_7rule_with_options(
        self,
        request: main_models.ConfigLayer7RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_type_list):
            query['ProxyTypeList'] = request.proxy_type_list
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7RuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_7rule_with_options_async(
        self,
        request: main_models.ConfigLayer7RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer7RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_type_list):
            query['ProxyTypeList'] = request.proxy_type_list
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer7Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer7RuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_7rule(
        self,
        request: main_models.ConfigLayer7RuleRequest,
    ) -> main_models.ConfigLayer7RuleResponse:
        runtime = RuntimeOptions()
        return self.config_layer_7rule_with_options(request, runtime)

    async def config_layer_7rule_async(
        self,
        request: main_models.ConfigLayer7RuleRequest,
    ) -> main_models.ConfigLayer7RuleResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_7rule_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: main_models.CreateAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_params):
            query['TaskParams'] = request.task_params
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsyncTask',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_async_task_with_options_async(
        self,
        request: main_models.CreateAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_params):
            query['TaskParams'] = request.task_params
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsyncTask',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_async_task(
        self,
        request: main_models.CreateAsyncTaskRequest,
    ) -> main_models.CreateAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: main_models.CreateAsyncTaskRequest,
    ) -> main_models.CreateAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def create_layer_4rule_with_options(
        self,
        tmp_req: main_models.CreateLayer4RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayer4RuleResponse:
        tmp_req.validate()
        request = main_models.CreateLayer4RuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.us_timeout):
            request.us_timeout_shrink = Utils.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayer4Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayer4RuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_4rule_with_options_async(
        self,
        tmp_req: main_models.CreateLayer4RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayer4RuleResponse:
        tmp_req.validate()
        request = main_models.CreateLayer4RuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.us_timeout):
            request.us_timeout_shrink = Utils.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayer4Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayer4RuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer_4rule(
        self,
        request: main_models.CreateLayer4RuleRequest,
    ) -> main_models.CreateLayer4RuleResponse:
        runtime = RuntimeOptions()
        return self.create_layer_4rule_with_options(request, runtime)

    async def create_layer_4rule_async(
        self,
        request: main_models.CreateLayer4RuleRequest,
    ) -> main_models.CreateLayer4RuleResponse:
        runtime = RuntimeOptions()
        return await self.create_layer_4rule_with_options_async(request, runtime)

    def create_layer_7rule_with_options(
        self,
        request: main_models.CreateLayer7RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayer7RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayer7Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayer7RuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_7rule_with_options_async(
        self,
        request: main_models.CreateLayer7RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayer7RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayer7Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayer7RuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer_7rule(
        self,
        request: main_models.CreateLayer7RuleRequest,
    ) -> main_models.CreateLayer7RuleResponse:
        runtime = RuntimeOptions()
        return self.create_layer_7rule_with_options(request, runtime)

    async def create_layer_7rule_async(
        self,
        request: main_models.CreateLayer7RuleRequest,
    ) -> main_models.CreateLayer7RuleResponse:
        runtime = RuntimeOptions()
        return await self.create_layer_7rule_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: main_models.DeleteAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsyncTask',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_async_task_with_options_async(
        self,
        request: main_models.DeleteAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsyncTask',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_async_task(
        self,
        request: main_models.DeleteAsyncTaskRequest,
    ) -> main_models.DeleteAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: main_models.DeleteAsyncTaskRequest,
    ) -> main_models.DeleteAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def delete_layer_4rule_with_options(
        self,
        request: main_models.DeleteLayer4RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayer4RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer4Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayer4RuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_4rule_with_options_async(
        self,
        request: main_models.DeleteLayer4RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayer4RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer4Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayer4RuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer_4rule(
        self,
        request: main_models.DeleteLayer4RuleRequest,
    ) -> main_models.DeleteLayer4RuleResponse:
        runtime = RuntimeOptions()
        return self.delete_layer_4rule_with_options(request, runtime)

    async def delete_layer_4rule_async(
        self,
        request: main_models.DeleteLayer4RuleRequest,
    ) -> main_models.DeleteLayer4RuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_layer_4rule_with_options_async(request, runtime)

    def delete_layer_7ccrule_with_options(
        self,
        request: main_models.DeleteLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayer7CCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_7ccrule_with_options_async(
        self,
        request: main_models.DeleteLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayer7CCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer_7ccrule(
        self,
        request: main_models.DeleteLayer7CCRuleRequest,
    ) -> main_models.DeleteLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_layer_7ccrule_with_options(request, runtime)

    async def delete_layer_7ccrule_async(
        self,
        request: main_models.DeleteLayer7CCRuleRequest,
    ) -> main_models.DeleteLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_layer_7ccrule_with_options_async(request, runtime)

    def delete_layer_7rule_with_options(
        self,
        request: main_models.DeleteLayer7RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayer7RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer7Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayer7RuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_7rule_with_options_async(
        self,
        request: main_models.DeleteLayer7RuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayer7RuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer7Rule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayer7RuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer_7rule(
        self,
        request: main_models.DeleteLayer7RuleRequest,
    ) -> main_models.DeleteLayer7RuleResponse:
        runtime = RuntimeOptions()
        return self.delete_layer_7rule_with_options(request, runtime)

    async def delete_layer_7rule_async(
        self,
        request: main_models.DeleteLayer7RuleRequest,
    ) -> main_models.DeleteLayer7RuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_layer_7rule_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackSourceCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackSourceCidr',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackSourceCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackSourceCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackSourceCidr',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackSourceCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_back_source_cidr(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
    ) -> main_models.DescribeBackSourceCidrResponse:
        runtime = RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
    ) -> main_models.DescribeBackSourceCidrResponse:
        runtime = RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_batch_sls_dispatch_status_with_options(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchSlsDispatchStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchSlsDispatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_batch_sls_dispatch_status_with_options_async(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchSlsDispatchStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchSlsDispatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_batch_sls_dispatch_status(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_batch_sls_dispatch_status_with_options(request, runtime)

    async def describe_batch_sls_dispatch_status_async(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_batch_sls_dispatch_status_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: main_models.DescribeDDoSEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eip):
            query['Eip'] = request.eip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSEvents',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: main_models.DescribeDDoSEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eip):
            query['Eip'] = request.eip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSEvents',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddo_sevents(
        self,
        request: main_models.DescribeDDoSEventsRequest,
    ) -> main_models.DescribeDDoSEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: main_models.DescribeDDoSEventsRequest,
    ) -> main_models.DescribeDDoSEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def describe_ddo_straffic_with_options(
        self,
        request: main_models.DescribeDDoSTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eip):
            query['Eip'] = request.eip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSTraffic',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddo_straffic_with_options_async(
        self,
        request: main_models.DescribeDDoSTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eip):
            query['Eip'] = request.eip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSTraffic',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddo_straffic(
        self,
        request: main_models.DescribeDDoSTrafficRequest,
    ) -> main_models.DescribeDDoSTrafficResponse:
        runtime = RuntimeOptions()
        return self.describe_ddo_straffic_with_options(request, runtime)

    async def describe_ddo_straffic_async(
        self,
        request: main_models.DescribeDDoSTrafficRequest,
    ) -> main_models.DescribeDDoSTrafficResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddo_straffic_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseCountStatistics',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseCountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseCountStatistics',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseCountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_count_statistics(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def describe_domain_access_mode_with_options(
        self,
        request: main_models.DescribeDomainAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAccessMode',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_access_mode_with_options_async(
        self,
        request: main_models.DescribeDomainAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAccessMode',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_access_mode(
        self,
        request: main_models.DescribeDomainAccessModeRequest,
    ) -> main_models.DescribeDomainAccessModeResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_access_mode_with_options(request, runtime)

    async def describe_domain_access_mode_async(
        self,
        request: main_models.DescribeDomainAccessModeRequest,
    ) -> main_models.DescribeDomainAccessModeResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_access_mode_with_options_async(request, runtime)

    def describe_domain_attack_event_list_with_options(
        self,
        request: main_models.DescribeDomainAttackEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAttackEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAttackEventList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAttackEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_attack_event_list_with_options_async(
        self,
        request: main_models.DescribeDomainAttackEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAttackEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAttackEventList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAttackEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_attack_event_list(
        self,
        request: main_models.DescribeDomainAttackEventListRequest,
    ) -> main_models.DescribeDomainAttackEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_attack_event_list_with_options(request, runtime)

    async def describe_domain_attack_event_list_async(
        self,
        request: main_models.DescribeDomainAttackEventListRequest,
    ) -> main_models.DescribeDomainAttackEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_attack_event_list_with_options_async(request, runtime)

    def describe_domain_attack_max_qps_with_options(
        self,
        request: main_models.DescribeDomainAttackMaxQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAttackMaxQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAttackMaxQps',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAttackMaxQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_attack_max_qps_with_options_async(
        self,
        request: main_models.DescribeDomainAttackMaxQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAttackMaxQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAttackMaxQps',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAttackMaxQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_attack_max_qps(
        self,
        request: main_models.DescribeDomainAttackMaxQpsRequest,
    ) -> main_models.DescribeDomainAttackMaxQpsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_attack_max_qps_with_options(request, runtime)

    async def describe_domain_attack_max_qps_async(
        self,
        request: main_models.DescribeDomainAttackMaxQpsRequest,
    ) -> main_models.DescribeDomainAttackMaxQpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_attack_max_qps_with_options_async(request, runtime)

    def describe_domain_overview_with_options(
        self,
        request: main_models.DescribeDomainOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainOverview',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_overview_with_options_async(
        self,
        request: main_models.DescribeDomainOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainOverview',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_overview(
        self,
        request: main_models.DescribeDomainOverviewRequest,
    ) -> main_models.DescribeDomainOverviewResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    async def describe_domain_overview_async(
        self,
        request: main_models.DescribeDomainOverviewRequest,
    ) -> main_models.DescribeDomainOverviewResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_overview_with_options_async(request, runtime)

    def describe_domain_qps_list_with_options(
        self,
        request: main_models.DescribeDomainQpsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainQpsList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_list_with_options_async(
        self,
        request: main_models.DescribeDomainQpsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainQpsList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_list(
        self,
        request: main_models.DescribeDomainQpsListRequest,
    ) -> main_models.DescribeDomainQpsListResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_qps_list_with_options(request, runtime)

    async def describe_domain_qps_list_async(
        self,
        request: main_models.DescribeDomainQpsListRequest,
    ) -> main_models.DescribeDomainQpsListResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_qps_list_with_options_async(request, runtime)

    def describe_domain_qps_with_cache_with_options(
        self,
        request: main_models.DescribeDomainQpsWithCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsWithCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainQpsWithCache',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsWithCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_with_cache_with_options_async(
        self,
        request: main_models.DescribeDomainQpsWithCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQpsWithCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainQpsWithCache',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQpsWithCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_with_cache(
        self,
        request: main_models.DescribeDomainQpsWithCacheRequest,
    ) -> main_models.DescribeDomainQpsWithCacheResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    async def describe_domain_qps_with_cache_async(
        self,
        request: main_models.DescribeDomainQpsWithCacheRequest,
    ) -> main_models.DescribeDomainQpsWithCacheResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_qps_with_cache_with_options_async(request, runtime)

    def describe_domain_sls_status_with_options(
        self,
        request: main_models.DescribeDomainSlsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSlsStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainSlsStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSlsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_sls_status_with_options_async(
        self,
        request: main_models.DescribeDomainSlsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSlsStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainSlsStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSlsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_sls_status(
        self,
        request: main_models.DescribeDomainSlsStatusRequest,
    ) -> main_models.DescribeDomainSlsStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_sls_status_with_options(request, runtime)

    async def describe_domain_sls_status_async(
        self,
        request: main_models.DescribeDomainSlsStatusRequest,
    ) -> main_models.DescribeDomainSlsStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_sls_status_with_options_async(request, runtime)

    def describe_domain_status_code_list_with_options(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatusCodeList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatusCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_status_code_list_with_options_async(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatusCodeList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatusCodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_status_code_list(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    async def describe_domain_status_code_list_async(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_status_code_list_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticBandwidthSpec',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticBandwidthSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticBandwidthSpec',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticBandwidthSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_bandwidth_spec(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: main_models.DescribeHealthCheckListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_list_with_options_async(
        self,
        request: main_models.DescribeHealthCheckListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_check_list(
        self,
        request: main_models.DescribeHealthCheckListRequest,
    ) -> main_models.DescribeHealthCheckListResponse:
        runtime = RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: main_models.DescribeHealthCheckListRequest,
    ) -> main_models.DescribeHealthCheckListResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_health_check_status_list_with_options(
        self,
        request: main_models.DescribeHealthCheckStatusListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckStatusListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckStatusList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckStatusListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_status_list_with_options_async(
        self,
        request: main_models.DescribeHealthCheckStatusListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckStatusListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckStatusList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckStatusListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_check_status_list(
        self,
        request: main_models.DescribeHealthCheckStatusListRequest,
    ) -> main_models.DescribeHealthCheckStatusListResponse:
        runtime = RuntimeOptions()
        return self.describe_health_check_status_list_with_options(request, runtime)

    async def describe_health_check_status_list_async(
        self,
        request: main_models.DescribeHealthCheckStatusListRequest,
    ) -> main_models.DescribeHealthCheckStatusListResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_check_status_list_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDetails',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_details_with_options_async(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDetails',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_details(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
    ) -> main_models.DescribeInstanceDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
    ) -> main_models.DescribeInstanceDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecs',
            version = '2017-12-28',
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
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecs',
            version = '2017-12-28',
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

    def describe_instance_statistics_with_options(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStatistics',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStatistics',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_statistics(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not DaraCore.is_null(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2017-12-28',
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
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not DaraCore.is_null(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2017-12-28',
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

    def describe_ip_traffic_with_options(
        self,
        request: main_models.DescribeIpTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eip):
            query['Eip'] = request.eip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.query_protocol):
            query['QueryProtocol'] = request.query_protocol
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpTraffic',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_traffic_with_options_async(
        self,
        request: main_models.DescribeIpTrafficRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eip):
            query['Eip'] = request.eip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.query_protocol):
            query['QueryProtocol'] = request.query_protocol
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpTraffic',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_traffic(
        self,
        request: main_models.DescribeIpTrafficRequest,
    ) -> main_models.DescribeIpTrafficResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_traffic_with_options(request, runtime)

    async def describe_ip_traffic_async(
        self,
        request: main_models.DescribeIpTrafficRequest,
    ) -> main_models.DescribeIpTrafficResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_traffic_with_options_async(request, runtime)

    def describe_layer_4rule_attributes_with_options(
        self,
        request: main_models.DescribeLayer4RuleAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer4RuleAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer4RuleAttributes',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer4RuleAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_layer_4rule_attributes_with_options_async(
        self,
        request: main_models.DescribeLayer4RuleAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer4RuleAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer4RuleAttributes',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer4RuleAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_layer_4rule_attributes(
        self,
        request: main_models.DescribeLayer4RuleAttributesRequest,
    ) -> main_models.DescribeLayer4RuleAttributesResponse:
        runtime = RuntimeOptions()
        return self.describe_layer_4rule_attributes_with_options(request, runtime)

    async def describe_layer_4rule_attributes_async(
        self,
        request: main_models.DescribeLayer4RuleAttributesRequest,
    ) -> main_models.DescribeLayer4RuleAttributesResponse:
        runtime = RuntimeOptions()
        return await self.describe_layer_4rule_attributes_with_options_async(request, runtime)

    def describe_layer_4rules_with_options(
        self,
        request: main_models.DescribeLayer4RulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer4RulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer4Rules',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer4RulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_layer_4rules_with_options_async(
        self,
        request: main_models.DescribeLayer4RulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer4RulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer4Rules',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer4RulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_layer_4rules(
        self,
        request: main_models.DescribeLayer4RulesRequest,
    ) -> main_models.DescribeLayer4RulesResponse:
        runtime = RuntimeOptions()
        return self.describe_layer_4rules_with_options(request, runtime)

    async def describe_layer_4rules_async(
        self,
        request: main_models.DescribeLayer4RulesRequest,
    ) -> main_models.DescribeLayer4RulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_layer_4rules_with_options_async(request, runtime)

    def describe_layer_7ccrules_with_options(
        self,
        request: main_models.DescribeLayer7CCRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer7CCRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer7CCRules',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer7CCRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_layer_7ccrules_with_options_async(
        self,
        request: main_models.DescribeLayer7CCRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer7CCRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer7CCRules',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer7CCRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_layer_7ccrules(
        self,
        request: main_models.DescribeLayer7CCRulesRequest,
    ) -> main_models.DescribeLayer7CCRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_layer_7ccrules_with_options(request, runtime)

    async def describe_layer_7ccrules_async(
        self,
        request: main_models.DescribeLayer7CCRulesRequest,
    ) -> main_models.DescribeLayer7CCRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_layer_7ccrules_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreExistStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreExistStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreExistStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreExistStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_exist_status(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: main_models.DescribeOpEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.op_action):
            query['OpAction'] = request.op_action
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpEntities',
            version = '2017-12-28',
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
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.op_action):
            query['OpAction'] = request.op_action
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpEntities',
            version = '2017-12-28',
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

    def describe_simple_domains_with_options(
        self,
        request: main_models.DescribeSimpleDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimpleDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimpleDomains',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimpleDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_simple_domains_with_options_async(
        self,
        request: main_models.DescribeSimpleDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSimpleDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSimpleDomains',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSimpleDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_simple_domains(
        self,
        request: main_models.DescribeSimpleDomainsRequest,
    ) -> main_models.DescribeSimpleDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_simple_domains_with_options(request, runtime)

    async def describe_simple_domains_async(
        self,
        request: main_models.DescribeSimpleDomainsRequest,
    ) -> main_models.DescribeSimpleDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_simple_domains_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAuthStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAuthStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_empty_count_with_options(
        self,
        request: main_models.DescribeSlsEmptyCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsEmptyCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsEmptyCount',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsEmptyCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_empty_count_with_options_async(
        self,
        request: main_models.DescribeSlsEmptyCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsEmptyCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsEmptyCount',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsEmptyCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_empty_count(
        self,
        request: main_models.DescribeSlsEmptyCountRequest,
    ) -> main_models.DescribeSlsEmptyCountResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_empty_count_with_options(request, runtime)

    async def describe_sls_empty_count_async(
        self,
        request: main_models.DescribeSlsEmptyCountRequest,
    ) -> main_models.DescribeSlsEmptyCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_empty_count_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogstoreInfo',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogstoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogstoreInfo',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogstoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_logstore_info(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsOpenStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_open_status_with_options_async(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsOpenStatus',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_open_status(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describle_cert_list_with_options(
        self,
        request: main_models.DescribleCertListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribleCertListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribleCertList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribleCertListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describle_cert_list_with_options_async(
        self,
        request: main_models.DescribleCertListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribleCertListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribleCertList',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribleCertListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describle_cert_list(
        self,
        request: main_models.DescribleCertListRequest,
    ) -> main_models.DescribleCertListResponse:
        runtime = RuntimeOptions()
        return self.describle_cert_list_with_options(request, runtime)

    async def describle_cert_list_async(
        self,
        request: main_models.DescribleCertListRequest,
    ) -> main_models.DescribleCertListResponse:
        runtime = RuntimeOptions()
        return await self.describle_cert_list_with_options_async(request, runtime)

    def describle_layer_7instance_relations_with_options(
        self,
        request: main_models.DescribleLayer7InstanceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribleLayer7InstanceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribleLayer7InstanceRelations',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribleLayer7InstanceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describle_layer_7instance_relations_with_options_async(
        self,
        request: main_models.DescribleLayer7InstanceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribleLayer7InstanceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribleLayer7InstanceRelations',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribleLayer7InstanceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describle_layer_7instance_relations(
        self,
        request: main_models.DescribleLayer7InstanceRelationsRequest,
    ) -> main_models.DescribleLayer7InstanceRelationsResponse:
        runtime = RuntimeOptions()
        return self.describle_layer_7instance_relations_with_options(request, runtime)

    async def describle_layer_7instance_relations_async(
        self,
        request: main_models.DescribleLayer7InstanceRelationsRequest,
    ) -> main_models.DescribleLayer7InstanceRelationsResponse:
        runtime = RuntimeOptions()
        return await self.describle_layer_7instance_relations_with_options_async(request, runtime)

    def disable_layer_7ccwith_options(
        self,
        request: main_models.DisableLayer7CCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLayer7CCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLayer7CC',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLayer7CCResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_layer_7ccwith_options_async(
        self,
        request: main_models.DisableLayer7CCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLayer7CCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLayer7CC',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLayer7CCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_layer_7cc(
        self,
        request: main_models.DisableLayer7CCRequest,
    ) -> main_models.DisableLayer7CCResponse:
        runtime = RuntimeOptions()
        return self.disable_layer_7ccwith_options(request, runtime)

    async def disable_layer_7cc_async(
        self,
        request: main_models.DisableLayer7CCRequest,
    ) -> main_models.DisableLayer7CCResponse:
        runtime = RuntimeOptions()
        return await self.disable_layer_7ccwith_options_async(request, runtime)

    def disable_layer_7ccrule_with_options(
        self,
        request: main_models.DisableLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLayer7CCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_layer_7ccrule_with_options_async(
        self,
        request: main_models.DisableLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLayer7CCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_layer_7ccrule(
        self,
        request: main_models.DisableLayer7CCRuleRequest,
    ) -> main_models.DisableLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_layer_7ccrule_with_options(request, runtime)

    async def disable_layer_7ccrule_async(
        self,
        request: main_models.DisableLayer7CCRuleRequest,
    ) -> main_models.DisableLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_layer_7ccrule_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: main_models.EmptySlsLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptySlsLogstoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptySlsLogstore',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptySlsLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_sls_logstore_with_options_async(
        self,
        request: main_models.EmptySlsLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptySlsLogstoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptySlsLogstore',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptySlsLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def empty_sls_logstore(
        self,
        request: main_models.EmptySlsLogstoreRequest,
    ) -> main_models.EmptySlsLogstoreResponse:
        runtime = RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: main_models.EmptySlsLogstoreRequest,
    ) -> main_models.EmptySlsLogstoreResponse:
        runtime = RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def enable_layer_7ccwith_options(
        self,
        request: main_models.EnableLayer7CCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLayer7CCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLayer7CC',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLayer7CCResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_layer_7ccwith_options_async(
        self,
        request: main_models.EnableLayer7CCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLayer7CCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLayer7CC',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLayer7CCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_layer_7cc(
        self,
        request: main_models.EnableLayer7CCRequest,
    ) -> main_models.EnableLayer7CCResponse:
        runtime = RuntimeOptions()
        return self.enable_layer_7ccwith_options(request, runtime)

    async def enable_layer_7cc_async(
        self,
        request: main_models.EnableLayer7CCRequest,
    ) -> main_models.EnableLayer7CCResponse:
        runtime = RuntimeOptions()
        return await self.enable_layer_7ccwith_options_async(request, runtime)

    def enable_layer_7ccrule_with_options(
        self,
        request: main_models.EnableLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLayer7CCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_layer_7ccrule_with_options_async(
        self,
        request: main_models.EnableLayer7CCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLayer7CCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLayer7CCRule',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLayer7CCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_layer_7ccrule(
        self,
        request: main_models.EnableLayer7CCRuleRequest,
    ) -> main_models.EnableLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_layer_7ccrule_with_options(request, runtime)

    async def enable_layer_7ccrule_async(
        self,
        request: main_models.EnableLayer7CCRuleRequest,
    ) -> main_models.EnableLayer7CCRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_layer_7ccrule_with_options_async(request, runtime)

    def list_async_task_with_options(
        self,
        request: main_models.ListAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTask',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_task_with_options_async(
        self,
        request: main_models.ListAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTask',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_task(
        self,
        request: main_models.ListAsyncTaskRequest,
    ) -> main_models.ListAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.list_async_task_with_options(request, runtime)

    async def list_async_task_async(
        self,
        request: main_models.ListAsyncTaskRequest,
    ) -> main_models.ListAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_async_task_with_options_async(request, runtime)

    def list_layer_7custom_ports_with_options(
        self,
        request: main_models.ListLayer7CustomPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLayer7CustomPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayer7CustomPorts',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayer7CustomPortsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layer_7custom_ports_with_options_async(
        self,
        request: main_models.ListLayer7CustomPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLayer7CustomPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayer7CustomPorts',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayer7CustomPortsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layer_7custom_ports(
        self,
        request: main_models.ListLayer7CustomPortsRequest,
    ) -> main_models.ListLayer7CustomPortsResponse:
        runtime = RuntimeOptions()
        return self.list_layer_7custom_ports_with_options(request, runtime)

    async def list_layer_7custom_ports_async(
        self,
        request: main_models.ListLayer7CustomPortsRequest,
    ) -> main_models.ListLayer7CustomPortsResponse:
        runtime = RuntimeOptions()
        return await self.list_layer_7custom_ports_with_options_async(request, runtime)

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
            version = '2017-12-28',
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
            version = '2017-12-28',
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
            version = '2017-12-28',
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
            version = '2017-12-28',
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

    def list_value_added_with_options(
        self,
        request: main_models.ListValueAddedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListValueAddedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListValueAdded',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListValueAddedResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_value_added_with_options_async(
        self,
        request: main_models.ListValueAddedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListValueAddedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListValueAdded',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListValueAddedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_value_added(
        self,
        request: main_models.ListValueAddedRequest,
    ) -> main_models.ListValueAddedResponse:
        runtime = RuntimeOptions()
        return self.list_value_added_with_options(request, runtime)

    async def list_value_added_async(
        self,
        request: main_models.ListValueAddedRequest,
    ) -> main_models.ListValueAddedResponse:
        runtime = RuntimeOptions()
        return await self.list_value_added_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBandWidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBandWidth',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBandWidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBandWidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBandWidth',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBandWidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_band_width(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
    ) -> main_models.ModifyElasticBandWidthResponse:
        runtime = RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
    ) -> main_models.ModifyElasticBandWidthResponse:
        runtime = RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def modify_full_log_ttl_with_options(
        self,
        request: main_models.ModifyFullLogTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFullLogTtlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFullLogTtl',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFullLogTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: main_models.ModifyFullLogTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFullLogTtlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFullLogTtl',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFullLogTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_full_log_ttl(
        self,
        request: main_models.ModifyFullLogTtlRequest,
    ) -> main_models.ModifyFullLogTtlResponse:
        runtime = RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: main_models.ModifyFullLogTtlRequest,
    ) -> main_models.ModifyFullLogTtlResponse:
        runtime = RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceRemark',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_remark_with_options_async(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceRemark',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_remark(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
    ) -> main_models.ModifyInstanceRemarkResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
    ) -> main_models.ModifyInstanceRemarkResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def open_domain_sls_config_with_options(
        self,
        request: main_models.OpenDomainSlsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenDomainSlsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenDomainSlsConfig',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDomainSlsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_domain_sls_config_with_options_async(
        self,
        request: main_models.OpenDomainSlsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenDomainSlsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenDomainSlsConfig',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDomainSlsConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_domain_sls_config(
        self,
        request: main_models.OpenDomainSlsConfigRequest,
    ) -> main_models.OpenDomainSlsConfigResponse:
        runtime = RuntimeOptions()
        return self.open_domain_sls_config_with_options(request, runtime)

    async def open_domain_sls_config_async(
        self,
        request: main_models.OpenDomainSlsConfigRequest,
    ) -> main_models.OpenDomainSlsConfigResponse:
        runtime = RuntimeOptions()
        return await self.open_domain_sls_config_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2017-12-28',
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
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2017-12-28',
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

    def release_value_added_with_options(
        self,
        request: main_models.ReleaseValueAddedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseValueAddedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseValueAdded',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseValueAddedResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_value_added_with_options_async(
        self,
        request: main_models.ReleaseValueAddedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseValueAddedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseValueAdded',
            version = '2017-12-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseValueAddedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_value_added(
        self,
        request: main_models.ReleaseValueAddedRequest,
    ) -> main_models.ReleaseValueAddedResponse:
        runtime = RuntimeOptions()
        return self.release_value_added_with_options(request, runtime)

    async def release_value_added_async(
        self,
        request: main_models.ReleaseValueAddedRequest,
    ) -> main_models.ReleaseValueAddedResponse:
        runtime = RuntimeOptions()
        return await self.release_value_added_with_options_async(request, runtime)

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
            version = '2017-12-28',
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
            version = '2017-12-28',
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
            version = '2017-12-28',
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
            version = '2017-12-28',
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
