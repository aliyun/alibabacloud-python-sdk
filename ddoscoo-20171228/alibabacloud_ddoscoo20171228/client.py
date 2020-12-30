# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddoscoo20171228 import models as ddoscoo_20171228_models
from alibabacloud_tea_util import models as util_models


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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.AddLayer7CCRuleResponse().from_map(
            self.do_rpcrequest('AddLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.AddLayer7CCRuleResponse().from_map(
            await self.do_rpcrequest_async('AddLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_layer_7ccrule_with_options(request, runtime)

    async def add_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_layer_7ccrule_with_options_async(request, runtime)

    def close_domain_sls_config_with_options(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CloseDomainSlsConfigResponse().from_map(
            self.do_rpcrequest('CloseDomainSlsConfig', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_domain_sls_config_with_options_async(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CloseDomainSlsConfigResponse().from_map(
            await self.do_rpcrequest_async('CloseDomainSlsConfig', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_domain_sls_config(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_domain_sls_config_with_options(request, runtime)

    async def close_domain_sls_config_async(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_domain_sls_config_with_options_async(request, runtime)

    def config_domain_access_mode_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigDomainAccessModeResponse().from_map(
            self.do_rpcrequest('ConfigDomainAccessMode', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_domain_access_mode_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigDomainAccessModeResponse().from_map(
            await self.do_rpcrequest_async('ConfigDomainAccessMode', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_domain_access_mode(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_domain_access_mode_with_options(request, runtime)

    async def config_domain_access_mode_async(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_domain_access_mode_with_options_async(request, runtime)

    def config_health_check_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigHealthCheckResponse().from_map(
            self.do_rpcrequest('ConfigHealthCheck', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_health_check_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigHealthCheckResponse().from_map(
            await self.do_rpcrequest_async('ConfigHealthCheck', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_health_check(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_health_check_with_options(request, runtime)

    async def config_health_check_async(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_health_check_with_options_async(request, runtime)

    def config_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer4RuleResponse().from_map(
            self.do_rpcrequest('ConfigLayer4Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer4RuleResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer4Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_4rule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_with_options(request, runtime)

    async def config_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_with_options_async(request, runtime)

    def config_layer_4rule_attribute_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse().from_map(
            self.do_rpcrequest('ConfigLayer4RuleAttribute', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_4rule_attribute_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer4RuleAttribute', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_4rule_attribute(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_attribute_with_options(request, runtime)

    async def config_layer_4rule_attribute_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_attribute_with_options_async(request, runtime)

    def config_layer_7black_white_list_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse().from_map(
            self.do_rpcrequest('ConfigLayer7BlackWhiteList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_7black_white_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer7BlackWhiteList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_7black_white_list(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7black_white_list_with_options(request, runtime)

    async def config_layer_7black_white_list_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7black_white_list_with_options_async(request, runtime)

    def config_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7CCRuleResponse().from_map(
            self.do_rpcrequest('ConfigLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7CCRuleResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7ccrule_with_options(request, runtime)

    async def config_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7ccrule_with_options_async(request, runtime)

    def config_layer_7cctemplate_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse().from_map(
            self.do_rpcrequest('ConfigLayer7CCTemplate', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_7cctemplate_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer7CCTemplate', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_7cctemplate(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cctemplate_with_options(request, runtime)

    async def config_layer_7cctemplate_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7cctemplate_with_options_async(request, runtime)

    def config_layer_7cert_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7CertResponse().from_map(
            self.do_rpcrequest('ConfigLayer7Cert', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_7cert_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7CertResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer7Cert', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_7cert(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cert_with_options(request, runtime)

    async def config_layer_7cert_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7cert_with_options_async(request, runtime)

    def config_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7RuleResponse().from_map(
            self.do_rpcrequest('ConfigLayer7Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ConfigLayer7RuleResponse().from_map(
            await self.do_rpcrequest_async('ConfigLayer7Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_layer_7rule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7rule_with_options(request, runtime)

    async def config_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7rule_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CreateAsyncTaskResponse().from_map(
            self.do_rpcrequest('CreateAsyncTask', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CreateAsyncTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateAsyncTask', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_async_task(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def create_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CreateLayer4RuleResponse().from_map(
            self.do_rpcrequest('CreateLayer4Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CreateLayer4RuleResponse().from_map(
            await self.do_rpcrequest_async('CreateLayer4Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_layer_4rule(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_layer_4rule_with_options(request, runtime)

    async def create_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_4rule_with_options_async(request, runtime)

    def create_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CreateLayer7RuleResponse().from_map(
            self.do_rpcrequest('CreateLayer7Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.CreateLayer7RuleResponse().from_map(
            await self.do_rpcrequest_async('CreateLayer7Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_layer_7rule(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_layer_7rule_with_options(request, runtime)

    async def create_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_7rule_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteAsyncTaskResponse().from_map(
            self.do_rpcrequest('DeleteAsyncTask', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteAsyncTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteAsyncTask', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_async_task(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def delete_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteLayer4RuleResponse().from_map(
            self.do_rpcrequest('DeleteLayer4Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteLayer4RuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteLayer4Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_layer_4rule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_4rule_with_options(request, runtime)

    async def delete_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_4rule_with_options_async(request, runtime)

    def delete_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteLayer7CCRuleResponse().from_map(
            self.do_rpcrequest('DeleteLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteLayer7CCRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7ccrule_with_options(request, runtime)

    async def delete_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_7ccrule_with_options_async(request, runtime)

    def delete_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteLayer7RuleResponse().from_map(
            self.do_rpcrequest('DeleteLayer7Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DeleteLayer7RuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteLayer7Rule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_layer_7rule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7rule_with_options(request, runtime)

    async def delete_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_7rule_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeBackSourceCidrResponse().from_map(
            self.do_rpcrequest('DescribeBackSourceCidr', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeBackSourceCidrResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackSourceCidr', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_back_source_cidr(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_batch_sls_dispatch_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse().from_map(
            self.do_rpcrequest('DescribeBatchSlsDispatchStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_batch_sls_dispatch_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeBatchSlsDispatchStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_batch_sls_dispatch_status(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_sls_dispatch_status_with_options(request, runtime)

    async def describe_batch_sls_dispatch_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_sls_dispatch_status_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDDoSEventsResponse().from_map(
            self.do_rpcrequest('DescribeDDoSEvents', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDDoSEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDoSEvents', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddo_sevents(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def describe_ddo_straffic_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDDoSTrafficResponse().from_map(
            self.do_rpcrequest('DescribeDDoSTraffic', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddo_straffic_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDDoSTrafficResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDoSTraffic', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddo_straffic(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_straffic_with_options(request, runtime)

    async def describe_ddo_straffic_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_straffic_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDefenseCountStatistics', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDefenseCountStatistics', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_defense_count_statistics(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def describe_domain_access_mode_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainAccessModeResponse().from_map(
            self.do_rpcrequest('DescribeDomainAccessMode', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_access_mode_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainAccessModeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainAccessMode', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_access_mode(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_access_mode_with_options(request, runtime)

    async def describe_domain_access_mode_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_access_mode_with_options_async(request, runtime)

    def describe_domain_attack_events_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainAttackEventsResponse().from_map(
            self.do_rpcrequest('DescribeDomainAttackEvents', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_attack_events_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainAttackEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainAttackEvents', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_attack_events(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    async def describe_domain_attack_events_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_events_with_options_async(request, runtime)

    def describe_domain_qps_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainQpsResponse().from_map(
            self.do_rpcrequest('DescribeDomainQps', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_qps_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainQpsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainQps', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_qps(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_options(request, runtime)

    async def describe_domain_qps_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_with_options_async(request, runtime)

    def describe_domain_qps_with_cache_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse().from_map(
            self.do_rpcrequest('DescribeDomainQpsWithCache', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_qps_with_cache_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainQpsWithCache', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_qps_with_cache(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    async def describe_domain_qps_with_cache_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_with_cache_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDomains', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomains', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domains(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_domain_sls_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainSlsStatusResponse().from_map(
            self.do_rpcrequest('DescribeDomainSlsStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_sls_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeDomainSlsStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSlsStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_sls_status(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_sls_status_with_options(request, runtime)

    async def describe_domain_sls_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_sls_status_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse().from_map(
            self.do_rpcrequest('DescribeElasticBandwidthSpec', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse().from_map(
            await self.do_rpcrequest_async('DescribeElasticBandwidthSpec', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elastic_bandwidth_spec(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeHealthCheckListResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_check_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeHealthCheckListResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthCheckList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_list(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_health_check_status_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckStatusList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_check_status_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthCheckStatusList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_status_list(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_list_with_options(request, runtime)

    async def describe_health_check_status_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_status_list_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstanceDetailsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceDetails', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_details_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstanceDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceDetails', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_details(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstanceSpecsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceSpecs', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstanceSpecsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceSpecs', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_specs(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstanceStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatistics', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeInstanceStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceStatistics', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_statistics(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_ip_traffic_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeIpTrafficResponse().from_map(
            self.do_rpcrequest('DescribeIpTraffic', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_traffic_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeIpTrafficResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpTraffic', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_traffic(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_traffic_with_options(request, runtime)

    async def describe_ip_traffic_async(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_traffic_with_options_async(request, runtime)

    def describe_layer_4rule_attributes_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse().from_map(
            self.do_rpcrequest('DescribeLayer4RuleAttributes', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_layer_4rule_attributes_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeLayer4RuleAttributes', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_layer_4rule_attributes(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rule_attributes_with_options(request, runtime)

    async def describe_layer_4rule_attributes_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rule_attributes_with_options_async(request, runtime)

    def describe_layer_4rules_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLayer4RulesResponse().from_map(
            self.do_rpcrequest('DescribeLayer4Rules', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_layer_4rules_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLayer4RulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeLayer4Rules', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_layer_4rules(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rules_with_options(request, runtime)

    async def describe_layer_4rules_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rules_with_options_async(request, runtime)

    def describe_layer_7ccrules_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLayer7CCRulesResponse().from_map(
            self.do_rpcrequest('DescribeLayer7CCRules', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_layer_7ccrules_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLayer7CCRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeLayer7CCRules', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_layer_7ccrules(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_7ccrules_with_options(request, runtime)

    async def describe_layer_7ccrules_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_7ccrules_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse().from_map(
            self.do_rpcrequest('DescribeLogStoreExistStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeLogStoreExistStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_store_exist_status(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeOpEntitiesResponse().from_map(
            self.do_rpcrequest('DescribeOpEntities', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeOpEntitiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeOpEntities', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_op_entities(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_simple_domains_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSimpleDomainsResponse().from_map(
            self.do_rpcrequest('DescribeSimpleDomains', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_simple_domains_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSimpleDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSimpleDomains', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_simple_domains(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_simple_domains_with_options(request, runtime)

    async def describe_simple_domains_async(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_simple_domains_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsAuthStatusResponse().from_map(
            self.do_rpcrequest('DescribeSlsAuthStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsAuthStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsAuthStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_empty_count_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsEmptyCountResponse().from_map(
            self.do_rpcrequest('DescribeSlsEmptyCount', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_empty_count_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsEmptyCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsEmptyCount', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_empty_count(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_empty_count_with_options(request, runtime)

    async def describe_sls_empty_count_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_empty_count_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse().from_map(
            self.do_rpcrequest('DescribeSlsLogstoreInfo', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsLogstoreInfo', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_logstore_info(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsOpenStatusResponse().from_map(
            self.do_rpcrequest('DescribeSlsOpenStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_open_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribeSlsOpenStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsOpenStatus', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_open_status(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describle_cert_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribleCertListResponse().from_map(
            self.do_rpcrequest('DescribleCertList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describle_cert_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribleCertListResponse().from_map(
            await self.do_rpcrequest_async('DescribleCertList', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describle_cert_list(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describle_cert_list_with_options(request, runtime)

    async def describle_cert_list_async(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describle_cert_list_with_options_async(request, runtime)

    def describle_layer_7instance_relations_with_options(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse().from_map(
            self.do_rpcrequest('DescribleLayer7InstanceRelations', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describle_layer_7instance_relations_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse().from_map(
            await self.do_rpcrequest_async('DescribleLayer7InstanceRelations', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describle_layer_7instance_relations(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describle_layer_7instance_relations_with_options(request, runtime)

    async def describle_layer_7instance_relations_async(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describle_layer_7instance_relations_with_options_async(request, runtime)

    def disable_layer_7ccwith_options(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DisableLayer7CCResponse().from_map(
            self.do_rpcrequest('DisableLayer7CC', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_layer_7ccwith_options_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DisableLayer7CCResponse().from_map(
            await self.do_rpcrequest_async('DisableLayer7CC', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_layer_7cc(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccwith_options(request, runtime)

    async def disable_layer_7cc_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_layer_7ccwith_options_async(request, runtime)

    def disable_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DisableLayer7CCRuleResponse().from_map(
            self.do_rpcrequest('DisableLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.DisableLayer7CCRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccrule_with_options(request, runtime)

    async def disable_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_layer_7ccrule_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.EmptySlsLogstoreResponse().from_map(
            self.do_rpcrequest('EmptySlsLogstore', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def empty_sls_logstore_with_options_async(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.EmptySlsLogstoreResponse().from_map(
            await self.do_rpcrequest_async('EmptySlsLogstore', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_sls_logstore(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def enable_layer_7ccwith_options(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.EnableLayer7CCResponse().from_map(
            self.do_rpcrequest('EnableLayer7CC', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_layer_7ccwith_options_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.EnableLayer7CCResponse().from_map(
            await self.do_rpcrequest_async('EnableLayer7CC', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_layer_7cc(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccwith_options(request, runtime)

    async def enable_layer_7cc_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_layer_7ccwith_options_async(request, runtime)

    def enable_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.EnableLayer7CCRuleResponse().from_map(
            self.do_rpcrequest('EnableLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.EnableLayer7CCRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableLayer7CCRule', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccrule_with_options(request, runtime)

    async def enable_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_layer_7ccrule_with_options_async(request, runtime)

    def list_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListAsyncTaskResponse().from_map(
            self.do_rpcrequest('ListAsyncTask', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListAsyncTaskResponse().from_map(
            await self.do_rpcrequest_async('ListAsyncTask', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_async_task(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_async_task_with_options(request, runtime)

    async def list_async_task_async(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_async_task_with_options_async(request, runtime)

    def list_layer_7custom_ports_with_options(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListLayer7CustomPortsResponse().from_map(
            self.do_rpcrequest('ListLayer7CustomPorts', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_layer_7custom_ports_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListLayer7CustomPortsResponse().from_map(
            await self.do_rpcrequest_async('ListLayer7CustomPorts', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_layer_7custom_ports(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_layer_7custom_ports_with_options(request, runtime)

    async def list_layer_7custom_ports_async(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_layer_7custom_ports_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_value_added_with_options(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListValueAddedResponse().from_map(
            self.do_rpcrequest('ListValueAdded', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_value_added_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ListValueAddedResponse().from_map(
            await self.do_rpcrequest_async('ListValueAdded', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_value_added(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_value_added_with_options(request, runtime)

    async def list_value_added_async(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_value_added_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ModifyElasticBandWidthResponse().from_map(
            self.do_rpcrequest('ModifyElasticBandWidth', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ModifyElasticBandWidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyElasticBandWidth', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elastic_band_width(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def modify_full_log_ttl_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ModifyFullLogTtlResponse().from_map(
            self.do_rpcrequest('ModifyFullLogTtl', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ModifyFullLogTtlResponse().from_map(
            await self.do_rpcrequest_async('ModifyFullLogTtl', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_full_log_ttl(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ModifyInstanceRemarkResponse().from_map(
            self.do_rpcrequest('ModifyInstanceRemark', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_remark_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ModifyInstanceRemarkResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceRemark', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_remark(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def open_domain_sls_config_with_options(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.OpenDomainSlsConfigResponse().from_map(
            self.do_rpcrequest('OpenDomainSlsConfig', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_domain_sls_config_with_options_async(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.OpenDomainSlsConfigResponse().from_map(
            await self.do_rpcrequest_async('OpenDomainSlsConfig', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_domain_sls_config(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_domain_sls_config_with_options(request, runtime)

    async def open_domain_sls_config_async(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_domain_sls_config_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ReleaseInstanceResponse().from_map(
            self.do_rpcrequest('ReleaseInstance', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ReleaseInstanceResponse().from_map(
            await self.do_rpcrequest_async('ReleaseInstance', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def release_value_added_with_options(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ReleaseValueAddedResponse().from_map(
            self.do_rpcrequest('ReleaseValueAdded', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_value_added_with_options_async(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.ReleaseValueAddedResponse().from_map(
            await self.do_rpcrequest_async('ReleaseValueAdded', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_value_added(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_value_added_with_options(request, runtime)

    async def release_value_added_async(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_value_added_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20171228_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2017-12-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
