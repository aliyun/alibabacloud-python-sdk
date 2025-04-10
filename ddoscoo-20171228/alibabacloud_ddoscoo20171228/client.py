# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddoscoo20171228 import models as ddoscoo_20171228_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        """
        @param request: AddLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.AddLayer7CCRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.AddLayer7CCRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def add_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        """
        @param request: AddLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.AddLayer7CCRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.AddLayer7CCRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        """
        @param request: AddLayer7CCRuleRequest
        @return: AddLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_layer_7ccrule_with_options(request, runtime)

    async def add_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        """
        @param request: AddLayer7CCRuleRequest
        @return: AddLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_layer_7ccrule_with_options_async(request, runtime)

    def close_domain_sls_config_with_options(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        """
        @param request: CloseDomainSlsConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseDomainSlsConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseDomainSlsConfig',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CloseDomainSlsConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CloseDomainSlsConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def close_domain_sls_config_with_options_async(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        """
        @param request: CloseDomainSlsConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseDomainSlsConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseDomainSlsConfig',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CloseDomainSlsConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CloseDomainSlsConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def close_domain_sls_config(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        """
        @param request: CloseDomainSlsConfigRequest
        @return: CloseDomainSlsConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_domain_sls_config_with_options(request, runtime)

    async def close_domain_sls_config_async(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        """
        @param request: CloseDomainSlsConfigRequest
        @return: CloseDomainSlsConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_domain_sls_config_with_options_async(request, runtime)

    def config_health_check_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        """
        @param request: ConfigHealthCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigHealthCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigHealthCheck',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigHealthCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigHealthCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def config_health_check_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        """
        @param request: ConfigHealthCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigHealthCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigHealthCheck',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigHealthCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigHealthCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_health_check(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        """
        @param request: ConfigHealthCheckRequest
        @return: ConfigHealthCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_health_check_with_options(request, runtime)

    async def config_health_check_async(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        """
        @param request: ConfigHealthCheckRequest
        @return: ConfigHealthCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_health_check_with_options_async(request, runtime)

    def config_layer_4rule_with_options(
        self,
        tmp_req: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        """
        @param tmp_req: ConfigLayer4RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddoscoo_20171228_models.ConfigLayer4RuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.us_timeout):
            request.us_timeout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not UtilClient.is_unset(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_4rule_with_options_async(
        self,
        tmp_req: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        """
        @param tmp_req: ConfigLayer4RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddoscoo_20171228_models.ConfigLayer4RuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.us_timeout):
            request.us_timeout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not UtilClient.is_unset(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_4rule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        """
        @param request: ConfigLayer4RuleRequest
        @return: ConfigLayer4RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_with_options(request, runtime)

    async def config_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        """
        @param request: ConfigLayer4RuleRequest
        @return: ConfigLayer4RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_with_options_async(request, runtime)

    def config_layer_4rule_attribute_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        """
        @param request: ConfigLayer4RuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RuleAttribute',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_4rule_attribute_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        """
        @param request: ConfigLayer4RuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RuleAttribute',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_4rule_attribute(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        """
        @param request: ConfigLayer4RuleAttributeRequest
        @return: ConfigLayer4RuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_attribute_with_options(request, runtime)

    async def config_layer_4rule_attribute_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        """
        @param request: ConfigLayer4RuleAttributeRequest
        @return: ConfigLayer4RuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_attribute_with_options_async(request, runtime)

    def config_layer_7black_white_list_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        """
        @param request: ConfigLayer7BlackWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7BlackWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_list):
            query['BlackList'] = request.black_list
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7BlackWhiteList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_7black_white_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        """
        @param request: ConfigLayer7BlackWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7BlackWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_list):
            query['BlackList'] = request.black_list
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7BlackWhiteList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_7black_white_list(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        """
        @param request: ConfigLayer7BlackWhiteListRequest
        @return: ConfigLayer7BlackWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7black_white_list_with_options(request, runtime)

    async def config_layer_7black_white_list_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        """
        @param request: ConfigLayer7BlackWhiteListRequest
        @return: ConfigLayer7BlackWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7black_white_list_with_options_async(request, runtime)

    def config_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        """
        @param request: ConfigLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        """
        @param request: ConfigLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        """
        @param request: ConfigLayer7CCRuleRequest
        @return: ConfigLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7ccrule_with_options(request, runtime)

    async def config_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        """
        @param request: ConfigLayer7CCRuleRequest
        @return: ConfigLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7ccrule_with_options_async(request, runtime)

    def config_layer_7cctemplate_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        """
        @param request: ConfigLayer7CCTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7CCTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7CCTemplate',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_7cctemplate_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        """
        @param request: ConfigLayer7CCTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7CCTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7CCTemplate',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_7cctemplate(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        """
        @param request: ConfigLayer7CCTemplateRequest
        @return: ConfigLayer7CCTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cctemplate_with_options(request, runtime)

    async def config_layer_7cctemplate_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        """
        @param request: ConfigLayer7CCTemplateRequest
        @return: ConfigLayer7CCTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7cctemplate_with_options_async(request, runtime)

    def config_layer_7cert_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        """
        @param request: ConfigLayer7CertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7CertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7Cert',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CertResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_7cert_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        """
        @param request: ConfigLayer7CertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7CertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7Cert',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7CertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_7cert(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        """
        @param request: ConfigLayer7CertRequest
        @return: ConfigLayer7CertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cert_with_options(request, runtime)

    async def config_layer_7cert_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        """
        @param request: ConfigLayer7CertRequest
        @return: ConfigLayer7CertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7cert_with_options_async(request, runtime)

    def config_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        """
        @param request: ConfigLayer7RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_type_list):
            query['ProxyTypeList'] = request.proxy_type_list
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7RuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7RuleResponse(),
                self.execute(params, req, runtime)
            )

    async def config_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        """
        @param request: ConfigLayer7RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer7RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_type_list):
            query['ProxyTypeList'] = request.proxy_type_list
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer7Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7RuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ConfigLayer7RuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def config_layer_7rule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        """
        @param request: ConfigLayer7RuleRequest
        @return: ConfigLayer7RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7rule_with_options(request, runtime)

    async def config_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        """
        @param request: ConfigLayer7RuleRequest
        @return: ConfigLayer7RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7rule_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        """
        @param request: CreateAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_params):
            query['TaskParams'] = request.task_params
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateAsyncTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateAsyncTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def create_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        """
        @param request: CreateAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_params):
            query['TaskParams'] = request.task_params
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateAsyncTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateAsyncTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_async_task(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        """
        @param request: CreateAsyncTaskRequest
        @return: CreateAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        """
        @param request: CreateAsyncTaskRequest
        @return: CreateAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def create_layer_4rule_with_options(
        self,
        tmp_req: ddoscoo_20171228_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        """
        @param tmp_req: CreateLayer4RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayer4RuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddoscoo_20171228_models.CreateLayer4RuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.us_timeout):
            request.us_timeout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not UtilClient.is_unset(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLayer4Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer4RuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer4RuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_layer_4rule_with_options_async(
        self,
        tmp_req: ddoscoo_20171228_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        """
        @param tmp_req: CreateLayer4RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayer4RuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddoscoo_20171228_models.CreateLayer4RuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.us_timeout):
            request.us_timeout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.us_timeout, 'UsTimeout', 'json')
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not UtilClient.is_unset(request.us_timeout_shrink):
            query['UsTimeout'] = request.us_timeout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLayer4Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer4RuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer4RuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_layer_4rule(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        """
        @param request: CreateLayer4RuleRequest
        @return: CreateLayer4RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_layer_4rule_with_options(request, runtime)

    async def create_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        """
        @param request: CreateLayer4RuleRequest
        @return: CreateLayer4RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_4rule_with_options_async(request, runtime)

    def create_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        """
        @param request: CreateLayer7RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayer7RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLayer7Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer7RuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer7RuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        """
        @param request: CreateLayer7RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayer7RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLayer7Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer7RuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.CreateLayer7RuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_layer_7rule(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        """
        @param request: CreateLayer7RuleRequest
        @return: CreateLayer7RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_layer_7rule_with_options(request, runtime)

    async def create_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        """
        @param request: CreateLayer7RuleRequest
        @return: CreateLayer7RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_7rule_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        """
        @param request: DeleteAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteAsyncTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteAsyncTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        """
        @param request: DeleteAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteAsyncTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteAsyncTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_async_task(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        """
        @param request: DeleteAsyncTaskRequest
        @return: DeleteAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        """
        @param request: DeleteAsyncTaskRequest
        @return: DeleteAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def delete_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        """
        @param request: DeleteLayer4RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayer4RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer4Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer4RuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer4RuleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        """
        @param request: DeleteLayer4RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayer4RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer4Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer4RuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer4RuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_layer_4rule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        """
        @param request: DeleteLayer4RuleRequest
        @return: DeleteLayer4RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_4rule_with_options(request, runtime)

    async def delete_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        """
        @param request: DeleteLayer4RuleRequest
        @return: DeleteLayer4RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_4rule_with_options_async(request, runtime)

    def delete_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        """
        @param request: DeleteLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7CCRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7CCRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        """
        @param request: DeleteLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7CCRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7CCRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        """
        @param request: DeleteLayer7CCRuleRequest
        @return: DeleteLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7ccrule_with_options(request, runtime)

    async def delete_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        """
        @param request: DeleteLayer7CCRuleRequest
        @return: DeleteLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_7ccrule_with_options_async(request, runtime)

    def delete_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        """
        @param request: DeleteLayer7RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayer7RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer7Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7RuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7RuleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        """
        @param request: DeleteLayer7RuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayer7RuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer7Rule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7RuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DeleteLayer7RuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_layer_7rule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        """
        @param request: DeleteLayer7RuleRequest
        @return: DeleteLayer7RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7rule_with_options(request, runtime)

    async def delete_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        """
        @param request: DeleteLayer7RuleRequest
        @return: DeleteLayer7RuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_7rule_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        """
        @param request: DescribeBackSourceCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackSourceCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBackSourceCidrResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBackSourceCidrResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        """
        @param request: DescribeBackSourceCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackSourceCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBackSourceCidrResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBackSourceCidrResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_back_source_cidr(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        """
        @param request: DescribeBackSourceCidrRequest
        @return: DescribeBackSourceCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        """
        @param request: DescribeBackSourceCidrRequest
        @return: DescribeBackSourceCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_batch_sls_dispatch_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        """
        @summary rosetta迁移
        
        @param request: DescribeBatchSlsDispatchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBatchSlsDispatchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchSlsDispatchStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_batch_sls_dispatch_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        """
        @summary rosetta迁移
        
        @param request: DescribeBatchSlsDispatchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBatchSlsDispatchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchSlsDispatchStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_batch_sls_dispatch_status(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        """
        @summary rosetta迁移
        
        @param request: DescribeBatchSlsDispatchStatusRequest
        @return: DescribeBatchSlsDispatchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_sls_dispatch_status_with_options(request, runtime)

    async def describe_batch_sls_dispatch_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        """
        @summary rosetta迁移
        
        @param request: DescribeBatchSlsDispatchStatusRequest
        @return: DescribeBatchSlsDispatchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_sls_dispatch_status_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        """
        @param request: DescribeDDoSEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip):
            query['Eip'] = request.eip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSEventsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSEventsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        """
        @param request: DescribeDDoSEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip):
            query['Eip'] = request.eip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSEventsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSEventsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ddo_sevents(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        """
        @param request: DescribeDDoSEventsRequest
        @return: DescribeDDoSEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        """
        @param request: DescribeDDoSEventsRequest
        @return: DescribeDDoSEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def describe_ddo_straffic_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        """
        @param request: DescribeDDoSTrafficRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip):
            query['Eip'] = request.eip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSTraffic',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSTrafficResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSTrafficResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ddo_straffic_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        """
        @param request: DescribeDDoSTrafficRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip):
            query['Eip'] = request.eip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSTraffic',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSTrafficResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDDoSTrafficResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ddo_straffic(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        """
        @param request: DescribeDDoSTrafficRequest
        @return: DescribeDDoSTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_straffic_with_options(request, runtime)

    async def describe_ddo_straffic_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        """
        @param request: DescribeDDoSTrafficRequest
        @return: DescribeDDoSTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_straffic_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        """
        @param request: DescribeDefenseCountStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseCountStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        """
        @param request: DescribeDefenseCountStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseCountStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_defense_count_statistics(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        """
        @param request: DescribeDefenseCountStatisticsRequest
        @return: DescribeDefenseCountStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        """
        @param request: DescribeDefenseCountStatisticsRequest
        @return: DescribeDefenseCountStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def describe_domain_access_mode_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        """
        @param request: DescribeDomainAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAccessMode',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAccessModeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAccessModeResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_access_mode_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        """
        @param request: DescribeDomainAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAccessMode',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAccessModeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAccessModeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_access_mode(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        """
        @param request: DescribeDomainAccessModeRequest
        @return: DescribeDomainAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_access_mode_with_options(request, runtime)

    async def describe_domain_access_mode_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        """
        @param request: DescribeDomainAccessModeRequest
        @return: DescribeDomainAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_access_mode_with_options_async(request, runtime)

    def describe_domain_attack_event_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventListResponse:
        """
        @param request: DescribeDomainAttackEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAttackEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEventList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackEventListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackEventListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_attack_event_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventListResponse:
        """
        @param request: DescribeDomainAttackEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAttackEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEventList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackEventListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackEventListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_attack_event_list(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventListRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventListResponse:
        """
        @param request: DescribeDomainAttackEventListRequest
        @return: DescribeDomainAttackEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_event_list_with_options(request, runtime)

    async def describe_domain_attack_event_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventListRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventListResponse:
        """
        @param request: DescribeDomainAttackEventListRequest
        @return: DescribeDomainAttackEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_event_list_with_options_async(request, runtime)

    def describe_domain_attack_max_qps_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackMaxQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse:
        """
        @param request: DescribeDomainAttackMaxQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAttackMaxQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackMaxQps',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_attack_max_qps_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackMaxQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse:
        """
        @param request: DescribeDomainAttackMaxQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAttackMaxQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackMaxQps',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_attack_max_qps(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackMaxQpsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse:
        """
        @param request: DescribeDomainAttackMaxQpsRequest
        @return: DescribeDomainAttackMaxQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_max_qps_with_options(request, runtime)

    async def describe_domain_attack_max_qps_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackMaxQpsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackMaxQpsResponse:
        """
        @param request: DescribeDomainAttackMaxQpsRequest
        @return: DescribeDomainAttackMaxQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_max_qps_with_options_async(request, runtime)

    def describe_domain_overview_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainOverviewResponse:
        """
        @param request: DescribeDomainOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainOverviewResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainOverviewResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_overview_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainOverviewResponse:
        """
        @param request: DescribeDomainOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainOverviewResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainOverviewResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_overview(
        self,
        request: ddoscoo_20171228_models.DescribeDomainOverviewRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainOverviewResponse:
        """
        @param request: DescribeDomainOverviewRequest
        @return: DescribeDomainOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    async def describe_domain_overview_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainOverviewRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainOverviewResponse:
        """
        @param request: DescribeDomainOverviewRequest
        @return: DescribeDomainOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_overview_with_options_async(request, runtime)

    def describe_domain_qps_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsListResponse:
        """
        @param request: DescribeDomainQpsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_qps_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsListResponse:
        """
        @param request: DescribeDomainQpsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_qps_list(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsListRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsListResponse:
        """
        @param request: DescribeDomainQpsListRequest
        @return: DescribeDomainQpsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_list_with_options(request, runtime)

    async def describe_domain_qps_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsListRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsListResponse:
        """
        @param request: DescribeDomainQpsListRequest
        @return: DescribeDomainQpsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_list_with_options_async(request, runtime)

    def describe_domain_qps_with_cache_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        """
        @param request: DescribeDomainQpsWithCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsWithCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsWithCache',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_qps_with_cache_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        """
        @param request: DescribeDomainQpsWithCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsWithCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsWithCache',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_qps_with_cache(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        """
        @param request: DescribeDomainQpsWithCacheRequest
        @return: DescribeDomainQpsWithCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    async def describe_domain_qps_with_cache_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        """
        @param request: DescribeDomainQpsWithCacheRequest
        @return: DescribeDomainQpsWithCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_with_cache_with_options_async(request, runtime)

    def describe_domain_sls_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        """
        @param request: DescribeDomainSlsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSlsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSlsStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainSlsStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainSlsStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_sls_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        """
        @param request: DescribeDomainSlsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSlsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSlsStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainSlsStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainSlsStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_sls_status(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        """
        @param request: DescribeDomainSlsStatusRequest
        @return: DescribeDomainSlsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_sls_status_with_options(request, runtime)

    async def describe_domain_sls_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        """
        @param request: DescribeDomainSlsStatusRequest
        @return: DescribeDomainSlsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_sls_status_with_options_async(request, runtime)

    def describe_domain_status_code_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainStatusCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse:
        """
        @summary 查询网站业务的响应状态码统计信息
        
        @param request: DescribeDomainStatusCodeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatusCodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domain_status_code_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainStatusCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse:
        """
        @summary 查询网站业务的响应状态码统计信息
        
        @param request: DescribeDomainStatusCodeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatusCodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domain_status_code_list(
        self,
        request: ddoscoo_20171228_models.DescribeDomainStatusCodeListRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse:
        """
        @summary 查询网站业务的响应状态码统计信息
        
        @param request: DescribeDomainStatusCodeListRequest
        @return: DescribeDomainStatusCodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    async def describe_domain_status_code_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainStatusCodeListRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainStatusCodeListResponse:
        """
        @summary 查询网站业务的响应状态码统计信息
        
        @param request: DescribeDomainStatusCodeListRequest
        @return: DescribeDomainStatusCodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_status_code_list_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        """
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_domains_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        """
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeDomainsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_domains(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        """
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        """
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        """
        @param request: DescribeElasticBandwidthSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticBandwidthSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        """
        @param request: DescribeElasticBandwidthSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticBandwidthSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_elastic_bandwidth_spec(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        """
        @param request: DescribeElasticBandwidthSpecRequest
        @return: DescribeElasticBandwidthSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        """
        @param request: DescribeElasticBandwidthSpecRequest
        @return: DescribeElasticBandwidthSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        """
        @param request: DescribeHealthCheckListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_health_check_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        """
        @param request: DescribeHealthCheckListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_health_check_list(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        """
        @param request: DescribeHealthCheckListRequest
        @return: DescribeHealthCheckListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        """
        @param request: DescribeHealthCheckListRequest
        @return: DescribeHealthCheckListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_health_check_status_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        """
        @param request: DescribeHealthCheckStatusListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckStatusListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatusList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_health_check_status_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        """
        @param request: DescribeHealthCheckStatusListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckStatusListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatusList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_health_check_status_list(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        """
        @param request: DescribeHealthCheckStatusListRequest
        @return: DescribeHealthCheckStatusListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_list_with_options(request, runtime)

    async def describe_health_check_status_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        """
        @param request: DescribeHealthCheckStatusListRequest
        @return: DescribeHealthCheckStatusListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_status_list_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        """
        @param request: DescribeInstanceDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_details_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        """
        @param request: DescribeInstanceDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_details(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        """
        @param request: DescribeInstanceDetailsRequest
        @return: DescribeInstanceDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        """
        @param request: DescribeInstanceDetailsRequest
        @return: DescribeInstanceDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceSpecsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceSpecsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceSpecsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceSpecsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_specs(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @return: DescribeInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @return: DescribeInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        """
        @param request: DescribeInstanceStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceStatisticsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceStatisticsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_statistics_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        """
        @param request: DescribeInstanceStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceStatisticsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstanceStatisticsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_statistics(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        """
        @param request: DescribeInstanceStatisticsRequest
        @return: DescribeInstanceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        """
        @param request: DescribeInstanceStatisticsRequest
        @return: DescribeInstanceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not UtilClient.is_unset(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instances_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not UtilClient.is_unset(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instances(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        """
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_ip_traffic_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        """
        @param request: DescribeIpTrafficRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip):
            query['Eip'] = request.eip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.query_protocol):
            query['QueryProtocol'] = request.query_protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpTraffic',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeIpTrafficResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeIpTrafficResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ip_traffic_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        """
        @param request: DescribeIpTrafficRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip):
            query['Eip'] = request.eip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.query_protocol):
            query['QueryProtocol'] = request.query_protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpTraffic',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeIpTrafficResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeIpTrafficResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ip_traffic(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        """
        @param request: DescribeIpTrafficRequest
        @return: DescribeIpTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_traffic_with_options(request, runtime)

    async def describe_ip_traffic_async(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        """
        @param request: DescribeIpTrafficRequest
        @return: DescribeIpTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_traffic_with_options_async(request, runtime)

    def describe_layer_4rule_attributes_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        """
        @param request: DescribeLayer4RuleAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer4RuleAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4RuleAttributes',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_layer_4rule_attributes_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        """
        @param request: DescribeLayer4RuleAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer4RuleAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4RuleAttributes',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_layer_4rule_attributes(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        """
        @param request: DescribeLayer4RuleAttributesRequest
        @return: DescribeLayer4RuleAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rule_attributes_with_options(request, runtime)

    async def describe_layer_4rule_attributes_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        """
        @param request: DescribeLayer4RuleAttributesRequest
        @return: DescribeLayer4RuleAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rule_attributes_with_options_async(request, runtime)

    def describe_layer_4rules_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        """
        @summary Call DescribeLayer4Rules to query the detailed configuration of port forwarding rules for DDoS protection instances.
        
        @param request: DescribeLayer4RulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer4RulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4Rules',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RulesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_layer_4rules_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        """
        @summary Call DescribeLayer4Rules to query the detailed configuration of port forwarding rules for DDoS protection instances.
        
        @param request: DescribeLayer4RulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer4RulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4Rules',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer4RulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_layer_4rules(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        """
        @summary Call DescribeLayer4Rules to query the detailed configuration of port forwarding rules for DDoS protection instances.
        
        @param request: DescribeLayer4RulesRequest
        @return: DescribeLayer4RulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rules_with_options(request, runtime)

    async def describe_layer_4rules_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        """
        @summary Call DescribeLayer4Rules to query the detailed configuration of port forwarding rules for DDoS protection instances.
        
        @param request: DescribeLayer4RulesRequest
        @return: DescribeLayer4RulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rules_with_options_async(request, runtime)

    def describe_layer_7ccrules_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        """
        @param request: DescribeLayer7CCRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer7CCRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer7CCRules',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer7CCRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer7CCRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_layer_7ccrules_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        """
        @param request: DescribeLayer7CCRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer7CCRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer7CCRules',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer7CCRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLayer7CCRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_layer_7ccrules(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        """
        @param request: DescribeLayer7CCRulesRequest
        @return: DescribeLayer7CCRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_7ccrules_with_options(request, runtime)

    async def describe_layer_7ccrules_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        """
        @param request: DescribeLayer7CCRulesRequest
        @return: DescribeLayer7CCRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_7ccrules_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        """
        @param request: DescribeLogStoreExistStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogStoreExistStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        """
        @param request: DescribeLogStoreExistStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogStoreExistStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_log_store_exist_status(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        """
        @param request: DescribeLogStoreExistStatusRequest
        @return: DescribeLogStoreExistStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        """
        @param request: DescribeLogStoreExistStatusRequest
        @return: DescribeLogStoreExistStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        """
        @param request: DescribeOpEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.op_action):
            query['OpAction'] = request.op_action
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeOpEntitiesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeOpEntitiesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_op_entities_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        """
        @param request: DescribeOpEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.op_action):
            query['OpAction'] = request.op_action
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeOpEntitiesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeOpEntitiesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_op_entities(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        """
        @param request: DescribeOpEntitiesRequest
        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        """
        @param request: DescribeOpEntitiesRequest
        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_simple_domains_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        """
        @param request: DescribeSimpleDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSimpleDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimpleDomains',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSimpleDomainsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSimpleDomainsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_simple_domains_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        """
        @param request: DescribeSimpleDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSimpleDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimpleDomains',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSimpleDomainsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSimpleDomainsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_simple_domains(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        """
        @param request: DescribeSimpleDomainsRequest
        @return: DescribeSimpleDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_simple_domains_with_options(request, runtime)

    async def describe_simple_domains_async(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        """
        @param request: DescribeSimpleDomainsRequest
        @return: DescribeSimpleDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_simple_domains_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        """
        @param request: DescribeSlsAuthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsAuthStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsAuthStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        """
        @param request: DescribeSlsAuthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsAuthStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsAuthStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sls_auth_status(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        """
        @param request: DescribeSlsAuthStatusRequest
        @return: DescribeSlsAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        """
        @param request: DescribeSlsAuthStatusRequest
        @return: DescribeSlsAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_empty_count_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        """
        @param request: DescribeSlsEmptyCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsEmptyCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsEmptyCount',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsEmptyCountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsEmptyCountResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sls_empty_count_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        """
        @param request: DescribeSlsEmptyCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsEmptyCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsEmptyCount',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsEmptyCountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsEmptyCountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sls_empty_count(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        """
        @param request: DescribeSlsEmptyCountRequest
        @return: DescribeSlsEmptyCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_empty_count_with_options(request, runtime)

    async def describe_sls_empty_count_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        """
        @param request: DescribeSlsEmptyCountRequest
        @return: DescribeSlsEmptyCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_empty_count_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        """
        @param request: DescribeSlsLogstoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogstoreInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        """
        @param request: DescribeSlsLogstoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogstoreInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sls_logstore_info(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        """
        @param request: DescribeSlsLogstoreInfoRequest
        @return: DescribeSlsLogstoreInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        """
        @param request: DescribeSlsLogstoreInfoRequest
        @return: DescribeSlsLogstoreInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        """
        @param request: DescribeSlsOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsOpenStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsOpenStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sls_open_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        """
        @param request: DescribeSlsOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsOpenStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribeSlsOpenStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sls_open_status(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        """
        @param request: DescribeSlsOpenStatusRequest
        @return: DescribeSlsOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        """
        @param request: DescribeSlsOpenStatusRequest
        @return: DescribeSlsOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describle_cert_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        """
        @param request: DescribleCertListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribleCertListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribleCertList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleCertListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleCertListResponse(),
                self.execute(params, req, runtime)
            )

    async def describle_cert_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        """
        @param request: DescribleCertListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribleCertListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribleCertList',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleCertListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleCertListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describle_cert_list(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        """
        @param request: DescribleCertListRequest
        @return: DescribleCertListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describle_cert_list_with_options(request, runtime)

    async def describle_cert_list_async(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        """
        @param request: DescribleCertListRequest
        @return: DescribleCertListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describle_cert_list_with_options_async(request, runtime)

    def describle_layer_7instance_relations_with_options(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        """
        @param request: DescribleLayer7InstanceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribleLayer7InstanceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribleLayer7InstanceRelations',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse(),
                self.execute(params, req, runtime)
            )

    async def describle_layer_7instance_relations_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        """
        @param request: DescribleLayer7InstanceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribleLayer7InstanceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribleLayer7InstanceRelations',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describle_layer_7instance_relations(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        """
        @param request: DescribleLayer7InstanceRelationsRequest
        @return: DescribleLayer7InstanceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describle_layer_7instance_relations_with_options(request, runtime)

    async def describle_layer_7instance_relations_async(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        """
        @param request: DescribleLayer7InstanceRelationsRequest
        @return: DescribleLayer7InstanceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describle_layer_7instance_relations_with_options_async(request, runtime)

    def disable_layer_7ccwith_options(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        """
        @param request: DisableLayer7CCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLayer7CCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLayer7CC',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_layer_7ccwith_options_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        """
        @param request: DisableLayer7CCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLayer7CCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLayer7CC',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_layer_7cc(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        """
        @param request: DisableLayer7CCRequest
        @return: DisableLayer7CCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccwith_options(request, runtime)

    async def disable_layer_7cc_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        """
        @param request: DisableLayer7CCRequest
        @return: DisableLayer7CCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_layer_7ccwith_options_async(request, runtime)

    def disable_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        """
        @param request: DisableLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        """
        @param request: DisableLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.DisableLayer7CCRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        """
        @param request: DisableLayer7CCRuleRequest
        @return: DisableLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccrule_with_options(request, runtime)

    async def disable_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        """
        @param request: DisableLayer7CCRuleRequest
        @return: DisableLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_layer_7ccrule_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        """
        @param request: EmptySlsLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptySlsLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.EmptySlsLogstoreResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.EmptySlsLogstoreResponse(),
                self.execute(params, req, runtime)
            )

    async def empty_sls_logstore_with_options_async(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        """
        @param request: EmptySlsLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptySlsLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.EmptySlsLogstoreResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.EmptySlsLogstoreResponse(),
                await self.execute_async(params, req, runtime)
            )

    def empty_sls_logstore(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        """
        @param request: EmptySlsLogstoreRequest
        @return: EmptySlsLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        """
        @param request: EmptySlsLogstoreRequest
        @return: EmptySlsLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def enable_layer_7ccwith_options(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        """
        @param request: EnableLayer7CCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLayer7CCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLayer7CC',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_layer_7ccwith_options_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        """
        @param request: EnableLayer7CCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLayer7CCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLayer7CC',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_layer_7cc(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        """
        @param request: EnableLayer7CCRequest
        @return: EnableLayer7CCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccwith_options(request, runtime)

    async def enable_layer_7cc_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        """
        @param request: EnableLayer7CCRequest
        @return: EnableLayer7CCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_layer_7ccwith_options_async(request, runtime)

    def enable_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        """
        @param request: EnableLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        """
        @param request: EnableLayer7CCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLayer7CCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLayer7CCRule',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.EnableLayer7CCRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        """
        @param request: EnableLayer7CCRuleRequest
        @return: EnableLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccrule_with_options(request, runtime)

    async def enable_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        """
        @param request: EnableLayer7CCRuleRequest
        @return: EnableLayer7CCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_layer_7ccrule_with_options_async(request, runtime)

    def list_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        """
        @param request: ListAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncTask',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListAsyncTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListAsyncTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def list_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        """
        @param request: ListAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncTask',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListAsyncTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListAsyncTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_async_task(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        """
        @param request: ListAsyncTaskRequest
        @return: ListAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_async_task_with_options(request, runtime)

    async def list_async_task_async(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        """
        @param request: ListAsyncTaskRequest
        @return: ListAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_async_task_with_options_async(request, runtime)

    def list_layer_7custom_ports_with_options(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        """
        @param request: ListLayer7CustomPortsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayer7CustomPortsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayer7CustomPorts',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListLayer7CustomPortsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListLayer7CustomPortsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_layer_7custom_ports_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        """
        @param request: ListLayer7CustomPortsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayer7CustomPortsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayer7CustomPorts',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListLayer7CustomPortsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListLayer7CustomPortsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_layer_7custom_ports(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        """
        @param request: ListLayer7CustomPortsRequest
        @return: ListLayer7CustomPortsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_layer_7custom_ports_with_options(request, runtime)

    async def list_layer_7custom_ports_async(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        """
        @param request: ListLayer7CustomPortsRequest
        @return: ListLayer7CustomPortsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_layer_7custom_ports_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        """
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_keys_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        """
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_keys(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        """
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        """
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_value_added_with_options(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        """
        @param request: ListValueAddedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListValueAddedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListValueAdded',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListValueAddedResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListValueAddedResponse(),
                self.execute(params, req, runtime)
            )

    async def list_value_added_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        """
        @param request: ListValueAddedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListValueAddedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListValueAdded',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListValueAddedResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ListValueAddedResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_value_added(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        """
        @param request: ListValueAddedRequest
        @return: ListValueAddedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_value_added_with_options(request, runtime)

    async def list_value_added_async(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        """
        @param request: ListValueAddedRequest
        @return: ListValueAddedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_value_added_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        """
        @param request: ModifyElasticBandWidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBandWidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyElasticBandWidthResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyElasticBandWidthResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        """
        @param request: ModifyElasticBandWidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBandWidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyElasticBandWidthResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyElasticBandWidthResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_elastic_band_width(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        """
        @param request: ModifyElasticBandWidthRequest
        @return: ModifyElasticBandWidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        """
        @param request: ModifyElasticBandWidthRequest
        @return: ModifyElasticBandWidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def modify_full_log_ttl_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        """
        @param request: ModifyFullLogTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFullLogTtlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyFullLogTtlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyFullLogTtlResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        """
        @param request: ModifyFullLogTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFullLogTtlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyFullLogTtlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyFullLogTtlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_full_log_ttl(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        """
        @param request: ModifyFullLogTtlRequest
        @return: ModifyFullLogTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        """
        @param request: ModifyFullLogTtlRequest
        @return: ModifyFullLogTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        """
        @param request: ModifyInstanceRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyInstanceRemarkResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyInstanceRemarkResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_remark_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        """
        @param request: ModifyInstanceRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyInstanceRemarkResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ModifyInstanceRemarkResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_remark(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        """
        @param request: ModifyInstanceRemarkRequest
        @return: ModifyInstanceRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        """
        @param request: ModifyInstanceRemarkRequest
        @return: ModifyInstanceRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def open_domain_sls_config_with_options(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        """
        @param request: OpenDomainSlsConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDomainSlsConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDomainSlsConfig',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.OpenDomainSlsConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.OpenDomainSlsConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def open_domain_sls_config_with_options_async(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        """
        @param request: OpenDomainSlsConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDomainSlsConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDomainSlsConfig',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.OpenDomainSlsConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.OpenDomainSlsConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def open_domain_sls_config(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        """
        @param request: OpenDomainSlsConfigRequest
        @return: OpenDomainSlsConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_domain_sls_config_with_options(request, runtime)

    async def open_domain_sls_config_async(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        """
        @param request: OpenDomainSlsConfigRequest
        @return: OpenDomainSlsConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_domain_sls_config_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def release_instance_with_options_async(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_instance(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def release_value_added_with_options(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        """
        @param request: ReleaseValueAddedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseValueAddedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseValueAdded',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseValueAddedResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseValueAddedResponse(),
                self.execute(params, req, runtime)
            )

    async def release_value_added_with_options_async(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        """
        @param request: ReleaseValueAddedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseValueAddedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseValueAdded',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseValueAddedResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.ReleaseValueAddedResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_value_added(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        """
        @param request: ReleaseValueAddedRequest
        @return: ReleaseValueAddedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_value_added_with_options(request, runtime)

    async def release_value_added_async(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        """
        @param request: ReleaseValueAddedRequest
        @return: ReleaseValueAddedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_value_added_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ddoscoo_20171228_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ddoscoo_20171228_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
