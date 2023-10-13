# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fc20230330 import models as fc20230330_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('fc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_alias_with_options(
        self,
        function_name: str,
        request: fc20230330_models.CreateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateAliasResponse:
        """
        创建函数别名。
        
        @param request: CreateAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.CreateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateAliasResponse:
        """
        创建函数别名。
        
        @param request: CreateAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alias(
        self,
        function_name: str,
        request: fc20230330_models.CreateAliasRequest,
    ) -> fc20230330_models.CreateAliasResponse:
        """
        创建函数别名。
        
        @param request: CreateAliasRequest
        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_alias_with_options(function_name, request, headers, runtime)

    async def create_alias_async(
        self,
        function_name: str,
        request: fc20230330_models.CreateAliasRequest,
    ) -> fc20230330_models.CreateAliasResponse:
        """
        创建函数别名。
        
        @param request: CreateAliasRequest
        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_alias_with_options_async(function_name, request, headers, runtime)

    def create_custom_domain_with_options(
        self,
        request: fc20230330_models.CreateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateCustomDomainResponse:
        """
        创建自定义域名。
        
        @param request: CreateCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_domain_with_options_async(
        self,
        request: fc20230330_models.CreateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateCustomDomainResponse:
        """
        创建自定义域名。
        
        @param request: CreateCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_domain(
        self,
        request: fc20230330_models.CreateCustomDomainRequest,
    ) -> fc20230330_models.CreateCustomDomainResponse:
        """
        创建自定义域名。
        
        @param request: CreateCustomDomainRequest
        @return: CreateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_custom_domain_with_options(request, headers, runtime)

    async def create_custom_domain_async(
        self,
        request: fc20230330_models.CreateCustomDomainRequest,
    ) -> fc20230330_models.CreateCustomDomainResponse:
        """
        创建自定义域名。
        
        @param request: CreateCustomDomainRequest
        @return: CreateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_custom_domain_with_options_async(request, headers, runtime)

    def create_function_with_options(
        self,
        request: fc20230330_models.CreateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateFunctionResponse:
        """
        创建函数。
        
        @param request: CreateFunctionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: fc20230330_models.CreateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateFunctionResponse:
        """
        创建函数。
        
        @param request: CreateFunctionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        request: fc20230330_models.CreateFunctionRequest,
    ) -> fc20230330_models.CreateFunctionResponse:
        """
        创建函数。
        
        @param request: CreateFunctionRequest
        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_with_options(request, headers, runtime)

    async def create_function_async(
        self,
        request: fc20230330_models.CreateFunctionRequest,
    ) -> fc20230330_models.CreateFunctionResponse:
        """
        创建函数。
        
        @param request: CreateFunctionRequest
        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_function_with_options_async(request, headers, runtime)

    def create_layer_version_with_options(
        self,
        layer_name: str,
        request: fc20230330_models.CreateLayerVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateLayerVersionResponse:
        """
        创建层版本。
        
        @param request: CreateLayerVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayerVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_version_with_options_async(
        self,
        layer_name: str,
        request: fc20230330_models.CreateLayerVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateLayerVersionResponse:
        """
        创建层版本。
        
        @param request: CreateLayerVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayerVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer_version(
        self,
        layer_name: str,
        request: fc20230330_models.CreateLayerVersionRequest,
    ) -> fc20230330_models.CreateLayerVersionResponse:
        """
        创建层版本。
        
        @param request: CreateLayerVersionRequest
        @return: CreateLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_version_with_options(layer_name, request, headers, runtime)

    async def create_layer_version_async(
        self,
        layer_name: str,
        request: fc20230330_models.CreateLayerVersionRequest,
    ) -> fc20230330_models.CreateLayerVersionResponse:
        """
        创建层版本。
        
        @param request: CreateLayerVersionRequest
        @return: CreateLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_layer_version_with_options_async(layer_name, request, headers, runtime)

    def create_trigger_with_options(
        self,
        function_name: str,
        request: fc20230330_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateTriggerResponse:
        """
        创建函数触发器。
        
        @param request: CreateTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateTriggerResponse:
        """
        创建函数触发器。
        
        @param request: CreateTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        function_name: str,
        request: fc20230330_models.CreateTriggerRequest,
    ) -> fc20230330_models.CreateTriggerResponse:
        """
        创建函数触发器。
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(function_name, request, headers, runtime)

    async def create_trigger_async(
        self,
        function_name: str,
        request: fc20230330_models.CreateTriggerRequest,
    ) -> fc20230330_models.CreateTriggerResponse:
        """
        创建函数触发器。
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_trigger_with_options_async(function_name, request, headers, runtime)

    def create_vpc_binding_with_options(
        self,
        function_name: str,
        request: fc20230330_models.CreateVpcBindingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateVpcBindingResponse:
        """
        创建VPC绑定。
        
        @param request: CreateVpcBindingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcBindingResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVpcBinding',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/vpc-bindings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_binding_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.CreateVpcBindingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.CreateVpcBindingResponse:
        """
        创建VPC绑定。
        
        @param request: CreateVpcBindingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcBindingResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVpcBinding',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/vpc-bindings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateVpcBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_binding(
        self,
        function_name: str,
        request: fc20230330_models.CreateVpcBindingRequest,
    ) -> fc20230330_models.CreateVpcBindingResponse:
        """
        创建VPC绑定。
        
        @param request: CreateVpcBindingRequest
        @return: CreateVpcBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_vpc_binding_with_options(function_name, request, headers, runtime)

    async def create_vpc_binding_async(
        self,
        function_name: str,
        request: fc20230330_models.CreateVpcBindingRequest,
    ) -> fc20230330_models.CreateVpcBindingResponse:
        """
        创建VPC绑定。
        
        @param request: CreateVpcBindingRequest
        @return: CreateVpcBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_vpc_binding_with_options_async(function_name, request, headers, runtime)

    def delete_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteAliasResponse:
        """
        删除函数别名。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteAliasResponse:
        """
        删除函数别名。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alias(
        self,
        function_name: str,
        alias_name: str,
    ) -> fc20230330_models.DeleteAliasResponse:
        """
        删除函数别名。
        
        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alias_with_options(function_name, alias_name, headers, runtime)

    async def delete_alias_async(
        self,
        function_name: str,
        alias_name: str,
    ) -> fc20230330_models.DeleteAliasResponse:
        """
        删除函数别名。
        
        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_alias_with_options_async(function_name, alias_name, headers, runtime)

    def delete_async_invoke_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.DeleteAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteAsyncInvokeConfigResponse:
        """
        删除函数异步调用配置。
        
        @param request: DeleteAsyncInvokeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_async_invoke_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.DeleteAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteAsyncInvokeConfigResponse:
        """
        删除函数异步调用配置。
        
        @param request: DeleteAsyncInvokeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_async_invoke_config(
        self,
        function_name: str,
        request: fc20230330_models.DeleteAsyncInvokeConfigRequest,
    ) -> fc20230330_models.DeleteAsyncInvokeConfigResponse:
        """
        删除函数异步调用配置。
        
        @param request: DeleteAsyncInvokeConfigRequest
        @return: DeleteAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_async_invoke_config_with_options(function_name, request, headers, runtime)

    async def delete_async_invoke_config_async(
        self,
        function_name: str,
        request: fc20230330_models.DeleteAsyncInvokeConfigRequest,
    ) -> fc20230330_models.DeleteAsyncInvokeConfigResponse:
        """
        删除函数异步调用配置。
        
        @param request: DeleteAsyncInvokeConfigRequest
        @return: DeleteAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def delete_concurrency_config_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteConcurrencyConfigResponse:
        """
        删除函数并发度配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConcurrencyConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/concurrency',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_concurrency_config_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteConcurrencyConfigResponse:
        """
        删除函数并发度配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConcurrencyConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/concurrency',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteConcurrencyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_concurrency_config(
        self,
        function_name: str,
    ) -> fc20230330_models.DeleteConcurrencyConfigResponse:
        """
        删除函数并发度配置。
        
        @return: DeleteConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_concurrency_config_with_options(function_name, headers, runtime)

    async def delete_concurrency_config_async(
        self,
        function_name: str,
    ) -> fc20230330_models.DeleteConcurrencyConfigResponse:
        """
        删除函数并发度配置。
        
        @return: DeleteConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_concurrency_config_with_options_async(function_name, headers, runtime)

    def delete_custom_domain_with_options(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteCustomDomainResponse:
        """
        删除自定义域名。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_domain_with_options_async(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteCustomDomainResponse:
        """
        删除自定义域名。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_domain(
        self,
        domain_name: str,
    ) -> fc20230330_models.DeleteCustomDomainResponse:
        """
        删除自定义域名。
        
        @return: DeleteCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_custom_domain_with_options(domain_name, headers, runtime)

    async def delete_custom_domain_async(
        self,
        domain_name: str,
    ) -> fc20230330_models.DeleteCustomDomainResponse:
        """
        删除自定义域名。
        
        @return: DeleteCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_custom_domain_with_options_async(domain_name, headers, runtime)

    def delete_function_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteFunctionResponse:
        """
        删除函数。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteFunctionResponse:
        """
        删除函数。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        function_name: str,
    ) -> fc20230330_models.DeleteFunctionResponse:
        """
        删除函数。
        
        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_with_options(function_name, headers, runtime)

    async def delete_function_async(
        self,
        function_name: str,
    ) -> fc20230330_models.DeleteFunctionResponse:
        """
        删除函数。
        
        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_function_with_options_async(function_name, headers, runtime)

    def delete_function_version_with_options(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteFunctionVersionResponse:
        """
        删除函数版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_version_with_options_async(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteFunctionVersionResponse:
        """
        删除函数版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteFunctionVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_version(
        self,
        function_name: str,
        version_id: str,
    ) -> fc20230330_models.DeleteFunctionVersionResponse:
        """
        删除函数版本。
        
        @return: DeleteFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_version_with_options(function_name, version_id, headers, runtime)

    async def delete_function_version_async(
        self,
        function_name: str,
        version_id: str,
    ) -> fc20230330_models.DeleteFunctionVersionResponse:
        """
        删除函数版本。
        
        @return: DeleteFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_function_version_with_options_async(function_name, version_id, headers, runtime)

    def delete_layer_version_with_options(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteLayerVersionResponse:
        """
        删除层版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayerVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_version_with_options_async(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteLayerVersionResponse:
        """
        删除层版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayerVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer_version(
        self,
        layer_name: str,
        version: str,
    ) -> fc20230330_models.DeleteLayerVersionResponse:
        """
        删除层版本。
        
        @return: DeleteLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_version_with_options(layer_name, version, headers, runtime)

    async def delete_layer_version_async(
        self,
        layer_name: str,
        version: str,
    ) -> fc20230330_models.DeleteLayerVersionResponse:
        """
        删除层版本。
        
        @return: DeleteLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_layer_version_with_options_async(layer_name, version, headers, runtime)

    def delete_provision_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.DeleteProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteProvisionConfigResponse:
        """
        删除函数预留配置。
        
        @param request: DeleteProvisionConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_provision_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.DeleteProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteProvisionConfigResponse:
        """
        删除函数预留配置。
        
        @param request: DeleteProvisionConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_provision_config(
        self,
        function_name: str,
        request: fc20230330_models.DeleteProvisionConfigRequest,
    ) -> fc20230330_models.DeleteProvisionConfigResponse:
        """
        删除函数预留配置。
        
        @param request: DeleteProvisionConfigRequest
        @return: DeleteProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_provision_config_with_options(function_name, request, headers, runtime)

    async def delete_provision_config_async(
        self,
        function_name: str,
        request: fc20230330_models.DeleteProvisionConfigRequest,
    ) -> fc20230330_models.DeleteProvisionConfigResponse:
        """
        删除函数预留配置。
        
        @param request: DeleteProvisionConfigRequest
        @return: DeleteProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_provision_config_with_options_async(function_name, request, headers, runtime)

    def delete_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteTriggerResponse:
        """
        删除函数触发器。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteTriggerResponse:
        """
        删除函数触发器。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        function_name: str,
        trigger_name: str,
    ) -> fc20230330_models.DeleteTriggerResponse:
        """
        删除函数触发器。
        
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(function_name, trigger_name, headers, runtime)

    async def delete_trigger_async(
        self,
        function_name: str,
        trigger_name: str,
    ) -> fc20230330_models.DeleteTriggerResponse:
        """
        删除函数触发器。
        
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_trigger_with_options_async(function_name, trigger_name, headers, runtime)

    def delete_vpc_binding_with_options(
        self,
        function_name: str,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteVpcBindingResponse:
        """
        删除VPC绑定。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcBindingResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVpcBinding',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/vpc-bindings/{OpenApiUtilClient.get_encode_param(vpc_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_binding_with_options_async(
        self,
        function_name: str,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.DeleteVpcBindingResponse:
        """
        删除VPC绑定。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcBindingResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVpcBinding',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/vpc-bindings/{OpenApiUtilClient.get_encode_param(vpc_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteVpcBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_binding(
        self,
        function_name: str,
        vpc_id: str,
    ) -> fc20230330_models.DeleteVpcBindingResponse:
        """
        删除VPC绑定。
        
        @return: DeleteVpcBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_vpc_binding_with_options(function_name, vpc_id, headers, runtime)

    async def delete_vpc_binding_async(
        self,
        function_name: str,
        vpc_id: str,
    ) -> fc20230330_models.DeleteVpcBindingResponse:
        """
        删除VPC绑定。
        
        @return: DeleteVpcBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_vpc_binding_with_options_async(function_name, vpc_id, headers, runtime)

    def get_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetAliasResponse:
        """
        获取函数别名信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alias_with_options_async(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetAliasResponse:
        """
        获取函数别名信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alias(
        self,
        function_name: str,
        alias_name: str,
    ) -> fc20230330_models.GetAliasResponse:
        """
        获取函数别名信息。
        
        @return: GetAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alias_with_options(function_name, alias_name, headers, runtime)

    async def get_alias_async(
        self,
        function_name: str,
        alias_name: str,
    ) -> fc20230330_models.GetAliasResponse:
        """
        获取函数别名信息。
        
        @return: GetAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_alias_with_options_async(function_name, alias_name, headers, runtime)

    def get_async_invoke_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.GetAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetAsyncInvokeConfigResponse:
        """
        获取函数异步调用配置。
        
        @param request: GetAsyncInvokeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_invoke_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.GetAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetAsyncInvokeConfigResponse:
        """
        获取函数异步调用配置。
        
        @param request: GetAsyncInvokeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_invoke_config(
        self,
        function_name: str,
        request: fc20230330_models.GetAsyncInvokeConfigRequest,
    ) -> fc20230330_models.GetAsyncInvokeConfigResponse:
        """
        获取函数异步调用配置。
        
        @param request: GetAsyncInvokeConfigRequest
        @return: GetAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_invoke_config_with_options(function_name, request, headers, runtime)

    async def get_async_invoke_config_async(
        self,
        function_name: str,
        request: fc20230330_models.GetAsyncInvokeConfigRequest,
    ) -> fc20230330_models.GetAsyncInvokeConfigResponse:
        """
        获取函数异步调用配置。
        
        @param request: GetAsyncInvokeConfigRequest
        @return: GetAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def get_concurrency_config_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetConcurrencyConfigResponse:
        """
        获取函数并发度配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConcurrencyConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/concurrency',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_concurrency_config_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetConcurrencyConfigResponse:
        """
        获取函数并发度配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConcurrencyConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/concurrency',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetConcurrencyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_concurrency_config(
        self,
        function_name: str,
    ) -> fc20230330_models.GetConcurrencyConfigResponse:
        """
        获取函数并发度配置。
        
        @return: GetConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_concurrency_config_with_options(function_name, headers, runtime)

    async def get_concurrency_config_async(
        self,
        function_name: str,
    ) -> fc20230330_models.GetConcurrencyConfigResponse:
        """
        获取函数并发度配置。
        
        @return: GetConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_concurrency_config_with_options_async(function_name, headers, runtime)

    def get_custom_domain_with_options(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetCustomDomainResponse:
        """
        获取自定义域名。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_domain_with_options_async(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetCustomDomainResponse:
        """
        获取自定义域名。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_domain(
        self,
        domain_name: str,
    ) -> fc20230330_models.GetCustomDomainResponse:
        """
        获取自定义域名。
        
        @return: GetCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_domain_with_options(domain_name, headers, runtime)

    async def get_custom_domain_async(
        self,
        domain_name: str,
    ) -> fc20230330_models.GetCustomDomainResponse:
        """
        获取自定义域名。
        
        @return: GetCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_custom_domain_with_options_async(domain_name, headers, runtime)

    def get_function_with_options(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetFunctionResponse:
        """
        获取函数信息。
        
        @param request: GetFunctionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetFunctionResponse:
        """
        获取函数信息。
        
        @param request: GetFunctionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionRequest,
    ) -> fc20230330_models.GetFunctionResponse:
        """
        获取函数信息。
        
        @param request: GetFunctionRequest
        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_with_options(function_name, request, headers, runtime)

    async def get_function_async(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionRequest,
    ) -> fc20230330_models.GetFunctionResponse:
        """
        获取函数信息。
        
        @param request: GetFunctionRequest
        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_with_options_async(function_name, request, headers, runtime)

    def get_function_code_with_options(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetFunctionCodeResponse:
        """
        获取函数代码。
        
        @param request: GetFunctionCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCode',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/code',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetFunctionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_code_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetFunctionCodeResponse:
        """
        获取函数代码。
        
        @param request: GetFunctionCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCode',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/code',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetFunctionCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_code(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionCodeRequest,
    ) -> fc20230330_models.GetFunctionCodeResponse:
        """
        获取函数代码。
        
        @param request: GetFunctionCodeRequest
        @return: GetFunctionCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_code_with_options(function_name, request, headers, runtime)

    async def get_function_code_async(
        self,
        function_name: str,
        request: fc20230330_models.GetFunctionCodeRequest,
    ) -> fc20230330_models.GetFunctionCodeResponse:
        """
        获取函数代码。
        
        @param request: GetFunctionCodeRequest
        @return: GetFunctionCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_code_with_options_async(function_name, request, headers, runtime)

    def get_layer_version_with_options(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetLayerVersionResponse:
        """
        获取层版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_version_with_options_async(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetLayerVersionResponse:
        """
        获取层版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions/{OpenApiUtilClient.get_encode_param(version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer_version(
        self,
        layer_name: str,
        version: str,
    ) -> fc20230330_models.GetLayerVersionResponse:
        """
        获取层版本。
        
        @return: GetLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_with_options(layer_name, version, headers, runtime)

    async def get_layer_version_async(
        self,
        layer_name: str,
        version: str,
    ) -> fc20230330_models.GetLayerVersionResponse:
        """
        获取层版本。
        
        @return: GetLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_layer_version_with_options_async(layer_name, version, headers, runtime)

    def get_layer_version_by_arn_with_options(
        self,
        arn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetLayerVersionByArnResponse:
        """
        根据资源标识获取层版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerVersionByArnResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayerVersionByArn',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layerarn/{OpenApiUtilClient.get_encode_param(arn)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetLayerVersionByArnResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_version_by_arn_with_options_async(
        self,
        arn: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetLayerVersionByArnResponse:
        """
        根据资源标识获取层版本。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerVersionByArnResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayerVersionByArn',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layerarn/{OpenApiUtilClient.get_encode_param(arn)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetLayerVersionByArnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer_version_by_arn(
        self,
        arn: str,
    ) -> fc20230330_models.GetLayerVersionByArnResponse:
        """
        根据资源标识获取层版本。
        
        @return: GetLayerVersionByArnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_by_arn_with_options(arn, headers, runtime)

    async def get_layer_version_by_arn_async(
        self,
        arn: str,
    ) -> fc20230330_models.GetLayerVersionByArnResponse:
        """
        根据资源标识获取层版本。
        
        @return: GetLayerVersionByArnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_layer_version_by_arn_with_options_async(arn, headers, runtime)

    def get_provision_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.GetProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetProvisionConfigResponse:
        """
        获取函数预留配置。
        
        @param request: GetProvisionConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provision_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.GetProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetProvisionConfigResponse:
        """
        获取函数预留配置。
        
        @param request: GetProvisionConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provision_config(
        self,
        function_name: str,
        request: fc20230330_models.GetProvisionConfigRequest,
    ) -> fc20230330_models.GetProvisionConfigResponse:
        """
        获取函数预留配置。
        
        @param request: GetProvisionConfigRequest
        @return: GetProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_provision_config_with_options(function_name, request, headers, runtime)

    async def get_provision_config_async(
        self,
        function_name: str,
        request: fc20230330_models.GetProvisionConfigRequest,
    ) -> fc20230330_models.GetProvisionConfigResponse:
        """
        获取函数预留配置。
        
        @param request: GetProvisionConfigRequest
        @return: GetProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_provision_config_with_options_async(function_name, request, headers, runtime)

    def get_resource_tags_with_options(
        self,
        request: fc20230330_models.GetResourceTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetResourceTagsResponse:
        """
        获取资源标签。
        
        @param request: GetResourceTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arn):
            query['arn'] = request.arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTags',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_tags_with_options_async(
        self,
        request: fc20230330_models.GetResourceTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetResourceTagsResponse:
        """
        获取资源标签。
        
        @param request: GetResourceTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arn):
            query['arn'] = request.arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTags',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetResourceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_tags(
        self,
        request: fc20230330_models.GetResourceTagsRequest,
    ) -> fc20230330_models.GetResourceTagsResponse:
        """
        获取资源标签。
        
        @param request: GetResourceTagsRequest
        @return: GetResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_tags_with_options(request, headers, runtime)

    async def get_resource_tags_async(
        self,
        request: fc20230330_models.GetResourceTagsRequest,
    ) -> fc20230330_models.GetResourceTagsResponse:
        """
        获取资源标签。
        
        @param request: GetResourceTagsRequest
        @return: GetResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_tags_with_options_async(request, headers, runtime)

    def get_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetTriggerResponse:
        """
        获取函数触发器。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trigger_with_options_async(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetTriggerResponse:
        """
        获取函数触发器。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trigger(
        self,
        function_name: str,
        trigger_name: str,
    ) -> fc20230330_models.GetTriggerResponse:
        """
        获取函数触发器。
        
        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trigger_with_options(function_name, trigger_name, headers, runtime)

    async def get_trigger_async(
        self,
        function_name: str,
        trigger_name: str,
    ) -> fc20230330_models.GetTriggerResponse:
        """
        获取函数触发器。
        
        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_trigger_with_options_async(function_name, trigger_name, headers, runtime)

    def invoke_function_with_options(
        self,
        function_name: str,
        request: fc20230330_models.InvokeFunctionRequest,
        headers: fc20230330_models.InvokeFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.InvokeFunctionResponse:
        """
        调用函数。
        
        @param request: InvokeFunctionRequest
        @param headers: InvokeFunctionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='InvokeFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/invocations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='binary'
        )
        res = fc20230330_models.InvokeFunctionResponse()
        tmp = UtilClient.assert_as_map(self.call_api(params, req, runtime))
        if not UtilClient.is_unset(tmp.get('body')):
            resp_body = UtilClient.assert_as_readable(tmp.get('body'))
            res.body = resp_body
        if not UtilClient.is_unset(tmp.get('headers')):
            resp_headers = UtilClient.assert_as_map(tmp.get('headers'))
            res.headers = UtilClient.stringify_map_value(resp_headers)
        if not UtilClient.is_unset(tmp.get('statusCode')):
            status_code = UtilClient.assert_as_integer(tmp.get('statusCode'))
            res.status_code = status_code
        return res

    async def invoke_function_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.InvokeFunctionRequest,
        headers: fc20230330_models.InvokeFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.InvokeFunctionResponse:
        """
        调用函数。
        
        @param request: InvokeFunctionRequest
        @param headers: InvokeFunctionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='InvokeFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/invocations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='binary'
        )
        res = fc20230330_models.InvokeFunctionResponse()
        tmp = UtilClient.assert_as_map(await self.call_api_async(params, req, runtime))
        if not UtilClient.is_unset(tmp.get('body')):
            resp_body = UtilClient.assert_as_readable(tmp.get('body'))
            res.body = resp_body
        if not UtilClient.is_unset(tmp.get('headers')):
            resp_headers = UtilClient.assert_as_map(tmp.get('headers'))
            res.headers = UtilClient.stringify_map_value(resp_headers)
        if not UtilClient.is_unset(tmp.get('statusCode')):
            status_code = UtilClient.assert_as_integer(tmp.get('statusCode'))
            res.status_code = status_code
        return res

    def invoke_function(
        self,
        function_name: str,
        request: fc20230330_models.InvokeFunctionRequest,
    ) -> fc20230330_models.InvokeFunctionResponse:
        """
        调用函数。
        
        @param request: InvokeFunctionRequest
        @return: InvokeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc20230330_models.InvokeFunctionHeaders()
        return self.invoke_function_with_options(function_name, request, headers, runtime)

    async def invoke_function_async(
        self,
        function_name: str,
        request: fc20230330_models.InvokeFunctionRequest,
    ) -> fc20230330_models.InvokeFunctionResponse:
        """
        调用函数。
        
        @param request: InvokeFunctionRequest
        @return: InvokeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc20230330_models.InvokeFunctionHeaders()
        return await self.invoke_function_with_options_async(function_name, request, headers, runtime)

    def list_aliases_with_options(
        self,
        function_name: str,
        request: fc20230330_models.ListAliasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListAliasesResponse:
        """
        列出函数别名。
        
        @param request: ListAliasesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.ListAliasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListAliasesResponse:
        """
        列出函数别名。
        
        @param request: ListAliasesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases(
        self,
        function_name: str,
        request: fc20230330_models.ListAliasesRequest,
    ) -> fc20230330_models.ListAliasesResponse:
        """
        列出函数别名。
        
        @param request: ListAliasesRequest
        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aliases_with_options(function_name, request, headers, runtime)

    async def list_aliases_async(
        self,
        function_name: str,
        request: fc20230330_models.ListAliasesRequest,
    ) -> fc20230330_models.ListAliasesResponse:
        """
        列出函数别名。
        
        @param request: ListAliasesRequest
        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_aliases_with_options_async(function_name, request, headers, runtime)

    def list_async_invoke_configs_with_options(
        self,
        request: fc20230330_models.ListAsyncInvokeConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListAsyncInvokeConfigsResponse:
        """
        列出函数异步调用配置。
        
        @param request: ListAsyncInvokeConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncInvokeConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncInvokeConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/async-invoke-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAsyncInvokeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_invoke_configs_with_options_async(
        self,
        request: fc20230330_models.ListAsyncInvokeConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListAsyncInvokeConfigsResponse:
        """
        列出函数异步调用配置。
        
        @param request: ListAsyncInvokeConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncInvokeConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncInvokeConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/async-invoke-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAsyncInvokeConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_invoke_configs(
        self,
        request: fc20230330_models.ListAsyncInvokeConfigsRequest,
    ) -> fc20230330_models.ListAsyncInvokeConfigsResponse:
        """
        列出函数异步调用配置。
        
        @param request: ListAsyncInvokeConfigsRequest
        @return: ListAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_async_invoke_configs_with_options(request, headers, runtime)

    async def list_async_invoke_configs_async(
        self,
        request: fc20230330_models.ListAsyncInvokeConfigsRequest,
    ) -> fc20230330_models.ListAsyncInvokeConfigsResponse:
        """
        列出函数异步调用配置。
        
        @param request: ListAsyncInvokeConfigsRequest
        @return: ListAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_async_invoke_configs_with_options_async(request, headers, runtime)

    def list_concurrency_configs_with_options(
        self,
        request: fc20230330_models.ListConcurrencyConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListConcurrencyConfigsResponse:
        """
        列出函数并发度配置。
        
        @param request: ListConcurrencyConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConcurrencyConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConcurrencyConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/concurrency-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListConcurrencyConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_concurrency_configs_with_options_async(
        self,
        request: fc20230330_models.ListConcurrencyConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListConcurrencyConfigsResponse:
        """
        列出函数并发度配置。
        
        @param request: ListConcurrencyConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConcurrencyConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConcurrencyConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/concurrency-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListConcurrencyConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_concurrency_configs(
        self,
        request: fc20230330_models.ListConcurrencyConfigsRequest,
    ) -> fc20230330_models.ListConcurrencyConfigsResponse:
        """
        列出函数并发度配置。
        
        @param request: ListConcurrencyConfigsRequest
        @return: ListConcurrencyConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_concurrency_configs_with_options(request, headers, runtime)

    async def list_concurrency_configs_async(
        self,
        request: fc20230330_models.ListConcurrencyConfigsRequest,
    ) -> fc20230330_models.ListConcurrencyConfigsResponse:
        """
        列出函数并发度配置。
        
        @param request: ListConcurrencyConfigsRequest
        @return: ListConcurrencyConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_concurrency_configs_with_options_async(request, headers, runtime)

    def list_custom_domains_with_options(
        self,
        request: fc20230330_models.ListCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListCustomDomainsResponse:
        """
        列出自定义域名。
        
        @param request: ListCustomDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomDomains',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_domains_with_options_async(
        self,
        request: fc20230330_models.ListCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListCustomDomainsResponse:
        """
        列出自定义域名。
        
        @param request: ListCustomDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomDomains',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListCustomDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_domains(
        self,
        request: fc20230330_models.ListCustomDomainsRequest,
    ) -> fc20230330_models.ListCustomDomainsResponse:
        """
        列出自定义域名。
        
        @param request: ListCustomDomainsRequest
        @return: ListCustomDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_custom_domains_with_options(request, headers, runtime)

    async def list_custom_domains_async(
        self,
        request: fc20230330_models.ListCustomDomainsRequest,
    ) -> fc20230330_models.ListCustomDomainsResponse:
        """
        列出自定义域名。
        
        @param request: ListCustomDomainsRequest
        @return: ListCustomDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_custom_domains_with_options_async(request, headers, runtime)

    def list_function_versions_with_options(
        self,
        function_name: str,
        request: fc20230330_models.ListFunctionVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListFunctionVersionsResponse:
        """
        列出函数版本。
        
        @param request: ListFunctionVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionVersions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListFunctionVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_versions_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.ListFunctionVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListFunctionVersionsResponse:
        """
        列出函数版本。
        
        @param request: ListFunctionVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionVersions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListFunctionVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_versions(
        self,
        function_name: str,
        request: fc20230330_models.ListFunctionVersionsRequest,
    ) -> fc20230330_models.ListFunctionVersionsResponse:
        """
        列出函数版本。
        
        @param request: ListFunctionVersionsRequest
        @return: ListFunctionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_versions_with_options(function_name, request, headers, runtime)

    async def list_function_versions_async(
        self,
        function_name: str,
        request: fc20230330_models.ListFunctionVersionsRequest,
    ) -> fc20230330_models.ListFunctionVersionsResponse:
        """
        列出函数版本。
        
        @param request: ListFunctionVersionsRequest
        @return: ListFunctionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_function_versions_with_options_async(function_name, request, headers, runtime)

    def list_functions_with_options(
        self,
        request: fc20230330_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListFunctionsResponse:
        """
        列出函数。
        
        @param request: ListFunctionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        request: fc20230330_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListFunctionsResponse:
        """
        列出函数。
        
        @param request: ListFunctionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        request: fc20230330_models.ListFunctionsRequest,
    ) -> fc20230330_models.ListFunctionsResponse:
        """
        列出函数。
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(request, headers, runtime)

    async def list_functions_async(
        self,
        request: fc20230330_models.ListFunctionsRequest,
    ) -> fc20230330_models.ListFunctionsResponse:
        """
        列出函数。
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_functions_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        function_name: str,
        request: fc20230330_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListInstancesResponse:
        """
        列出函数实例。
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.with_all_active):
            query['withAllActive'] = request.with_all_active
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListInstancesResponse:
        """
        列出函数实例。
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.with_all_active):
            query['withAllActive'] = request.with_all_active
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        function_name: str,
        request: fc20230330_models.ListInstancesRequest,
    ) -> fc20230330_models.ListInstancesResponse:
        """
        列出函数实例。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(function_name, request, headers, runtime)

    async def list_instances_async(
        self,
        function_name: str,
        request: fc20230330_models.ListInstancesRequest,
    ) -> fc20230330_models.ListInstancesResponse:
        """
        列出函数实例。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(function_name, request, headers, runtime)

    def list_layer_versions_with_options(
        self,
        layer_name: str,
        request: fc20230330_models.ListLayerVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListLayerVersionsResponse:
        """
        列出层版本。
        
        @param request: ListLayerVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayerVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.start_version):
            query['startVersion'] = request.start_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayerVersions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListLayerVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layer_versions_with_options_async(
        self,
        layer_name: str,
        request: fc20230330_models.ListLayerVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListLayerVersionsResponse:
        """
        列出层版本。
        
        @param request: ListLayerVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayerVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.start_version):
            query['startVersion'] = request.start_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayerVersions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListLayerVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layer_versions(
        self,
        layer_name: str,
        request: fc20230330_models.ListLayerVersionsRequest,
    ) -> fc20230330_models.ListLayerVersionsResponse:
        """
        列出层版本。
        
        @param request: ListLayerVersionsRequest
        @return: ListLayerVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layer_versions_with_options(layer_name, request, headers, runtime)

    async def list_layer_versions_async(
        self,
        layer_name: str,
        request: fc20230330_models.ListLayerVersionsRequest,
    ) -> fc20230330_models.ListLayerVersionsResponse:
        """
        列出层版本。
        
        @param request: ListLayerVersionsRequest
        @return: ListLayerVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_layer_versions_with_options_async(layer_name, request, headers, runtime)

    def list_layers_with_options(
        self,
        request: fc20230330_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListLayersResponse:
        """
        列出层。
        
        @param request: ListLayersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.official):
            query['official'] = request.official
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layers_with_options_async(
        self,
        request: fc20230330_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListLayersResponse:
        """
        列出层。
        
        @param request: ListLayersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.official):
            query['official'] = request.official
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layers(
        self,
        request: fc20230330_models.ListLayersRequest,
    ) -> fc20230330_models.ListLayersResponse:
        """
        列出层。
        
        @param request: ListLayersRequest
        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: fc20230330_models.ListLayersRequest,
    ) -> fc20230330_models.ListLayersResponse:
        """
        列出层。
        
        @param request: ListLayersRequest
        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_provision_configs_with_options(
        self,
        request: fc20230330_models.ListProvisionConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListProvisionConfigsResponse:
        """
        列出函数预留配置。
        
        @param request: ListProvisionConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProvisionConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/provision-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListProvisionConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provision_configs_with_options_async(
        self,
        request: fc20230330_models.ListProvisionConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListProvisionConfigsResponse:
        """
        列出函数预留配置。
        
        @param request: ListProvisionConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProvisionConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/provision-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListProvisionConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provision_configs(
        self,
        request: fc20230330_models.ListProvisionConfigsRequest,
    ) -> fc20230330_models.ListProvisionConfigsResponse:
        """
        列出函数预留配置。
        
        @param request: ListProvisionConfigsRequest
        @return: ListProvisionConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_provision_configs_with_options(request, headers, runtime)

    async def list_provision_configs_async(
        self,
        request: fc20230330_models.ListProvisionConfigsRequest,
    ) -> fc20230330_models.ListProvisionConfigsResponse:
        """
        列出函数预留配置。
        
        @param request: ListProvisionConfigsRequest
        @return: ListProvisionConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_provision_configs_with_options_async(request, headers, runtime)

    def list_tagged_resources_with_options(
        self,
        request: fc20230330_models.ListTaggedResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTaggedResourcesResponse:
        """
        列出具有标签的资源。
        
        @param request: ListTaggedResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaggedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaggedResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTaggedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tagged_resources_with_options_async(
        self,
        request: fc20230330_models.ListTaggedResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTaggedResourcesResponse:
        """
        列出具有标签的资源。
        
        @param request: ListTaggedResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaggedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaggedResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTaggedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tagged_resources(
        self,
        request: fc20230330_models.ListTaggedResourcesRequest,
    ) -> fc20230330_models.ListTaggedResourcesResponse:
        """
        列出具有标签的资源。
        
        @param request: ListTaggedResourcesRequest
        @return: ListTaggedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tagged_resources_with_options(request, headers, runtime)

    async def list_tagged_resources_async(
        self,
        request: fc20230330_models.ListTaggedResourcesRequest,
    ) -> fc20230330_models.ListTaggedResourcesResponse:
        """
        列出具有标签的资源。
        
        @param request: ListTaggedResourcesRequest
        @return: ListTaggedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tagged_resources_with_options_async(request, headers, runtime)

    def list_triggers_with_options(
        self,
        function_name: str,
        request: fc20230330_models.ListTriggersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTriggersResponse:
        """
        列出函数触发器。
        
        @param request: ListTriggersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.ListTriggersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTriggersResponse:
        """
        列出函数触发器。
        
        @param request: ListTriggersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_triggers(
        self,
        function_name: str,
        request: fc20230330_models.ListTriggersRequest,
    ) -> fc20230330_models.ListTriggersResponse:
        """
        列出函数触发器。
        
        @param request: ListTriggersRequest
        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_triggers_with_options(function_name, request, headers, runtime)

    async def list_triggers_async(
        self,
        function_name: str,
        request: fc20230330_models.ListTriggersRequest,
    ) -> fc20230330_models.ListTriggersResponse:
        """
        列出函数触发器。
        
        @param request: ListTriggersRequest
        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_triggers_with_options_async(function_name, request, headers, runtime)

    def list_vpc_bindings_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListVpcBindingsResponse:
        """
        列出VPC绑定配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpcBindingsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListVpcBindings',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/vpc-bindings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListVpcBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_bindings_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListVpcBindingsResponse:
        """
        列出VPC绑定配置。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpcBindingsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListVpcBindings',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/vpc-bindings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListVpcBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_bindings(
        self,
        function_name: str,
    ) -> fc20230330_models.ListVpcBindingsResponse:
        """
        列出VPC绑定配置。
        
        @return: ListVpcBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_bindings_with_options(function_name, headers, runtime)

    async def list_vpc_bindings_async(
        self,
        function_name: str,
    ) -> fc20230330_models.ListVpcBindingsResponse:
        """
        列出VPC绑定配置。
        
        @return: ListVpcBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_vpc_bindings_with_options_async(function_name, headers, runtime)

    def publish_function_version_with_options(
        self,
        function_name: str,
        request: fc20230330_models.PublishFunctionVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PublishFunctionVersionResponse:
        """
        发布函数版本。
        
        @param request: PublishFunctionVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFunctionVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishFunctionVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PublishFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_function_version_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.PublishFunctionVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PublishFunctionVersionResponse:
        """
        发布函数版本。
        
        @param request: PublishFunctionVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFunctionVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishFunctionVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PublishFunctionVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_function_version(
        self,
        function_name: str,
        request: fc20230330_models.PublishFunctionVersionRequest,
    ) -> fc20230330_models.PublishFunctionVersionResponse:
        """
        发布函数版本。
        
        @param request: PublishFunctionVersionRequest
        @return: PublishFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_function_version_with_options(function_name, request, headers, runtime)

    async def publish_function_version_async(
        self,
        function_name: str,
        request: fc20230330_models.PublishFunctionVersionRequest,
    ) -> fc20230330_models.PublishFunctionVersionResponse:
        """
        发布函数版本。
        
        @param request: PublishFunctionVersionRequest
        @return: PublishFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_function_version_with_options_async(function_name, request, headers, runtime)

    def put_async_invoke_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.PutAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutAsyncInvokeConfigResponse:
        """
        设置函数异步调用配置。
        
        @param request: PutAsyncInvokeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_async_invoke_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.PutAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutAsyncInvokeConfigResponse:
        """
        设置函数异步调用配置。
        
        @param request: PutAsyncInvokeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-invoke-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_async_invoke_config(
        self,
        function_name: str,
        request: fc20230330_models.PutAsyncInvokeConfigRequest,
    ) -> fc20230330_models.PutAsyncInvokeConfigResponse:
        """
        设置函数异步调用配置。
        
        @param request: PutAsyncInvokeConfigRequest
        @return: PutAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_async_invoke_config_with_options(function_name, request, headers, runtime)

    async def put_async_invoke_config_async(
        self,
        function_name: str,
        request: fc20230330_models.PutAsyncInvokeConfigRequest,
    ) -> fc20230330_models.PutAsyncInvokeConfigResponse:
        """
        设置函数异步调用配置。
        
        @param request: PutAsyncInvokeConfigRequest
        @return: PutAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def put_concurrency_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.PutConcurrencyConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutConcurrencyConfigResponse:
        """
        设置函数并发度配置。
        
        @param request: PutConcurrencyConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutConcurrencyConfigResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/concurrency',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_concurrency_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.PutConcurrencyConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutConcurrencyConfigResponse:
        """
        设置函数并发度配置。
        
        @param request: PutConcurrencyConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutConcurrencyConfigResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/concurrency',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutConcurrencyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_concurrency_config(
        self,
        function_name: str,
        request: fc20230330_models.PutConcurrencyConfigRequest,
    ) -> fc20230330_models.PutConcurrencyConfigResponse:
        """
        设置函数并发度配置。
        
        @param request: PutConcurrencyConfigRequest
        @return: PutConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_concurrency_config_with_options(function_name, request, headers, runtime)

    async def put_concurrency_config_async(
        self,
        function_name: str,
        request: fc20230330_models.PutConcurrencyConfigRequest,
    ) -> fc20230330_models.PutConcurrencyConfigResponse:
        """
        设置函数并发度配置。
        
        @param request: PutConcurrencyConfigRequest
        @return: PutConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_concurrency_config_with_options_async(function_name, request, headers, runtime)

    def put_layer_aclwith_options(
        self,
        layer_name: str,
        request: fc20230330_models.PutLayerACLRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutLayerACLResponse:
        """
        设置层的访问权限。
        
        @param request: PutLayerACLRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutLayerACLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLayerACL',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.PutLayerACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_layer_aclwith_options_async(
        self,
        layer_name: str,
        request: fc20230330_models.PutLayerACLRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutLayerACLResponse:
        """
        设置层的访问权限。
        
        @param request: PutLayerACLRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutLayerACLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLayerACL',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/layers/{OpenApiUtilClient.get_encode_param(layer_name)}/acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.PutLayerACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_layer_acl(
        self,
        layer_name: str,
        request: fc20230330_models.PutLayerACLRequest,
    ) -> fc20230330_models.PutLayerACLResponse:
        """
        设置层的访问权限。
        
        @param request: PutLayerACLRequest
        @return: PutLayerACLResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_layer_aclwith_options(layer_name, request, headers, runtime)

    async def put_layer_acl_async(
        self,
        layer_name: str,
        request: fc20230330_models.PutLayerACLRequest,
    ) -> fc20230330_models.PutLayerACLResponse:
        """
        设置层的访问权限。
        
        @param request: PutLayerACLRequest
        @return: PutLayerACLResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_layer_aclwith_options_async(layer_name, request, headers, runtime)

    def put_provision_config_with_options(
        self,
        function_name: str,
        request: fc20230330_models.PutProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutProvisionConfigResponse:
        """
        设置函数预留配置。
        
        @param request: PutProvisionConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_provision_config_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.PutProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.PutProvisionConfigResponse:
        """
        设置函数预留配置。
        
        @param request: PutProvisionConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/provision-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_provision_config(
        self,
        function_name: str,
        request: fc20230330_models.PutProvisionConfigRequest,
    ) -> fc20230330_models.PutProvisionConfigResponse:
        """
        设置函数预留配置。
        
        @param request: PutProvisionConfigRequest
        @return: PutProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_provision_config_with_options(function_name, request, headers, runtime)

    async def put_provision_config_async(
        self,
        function_name: str,
        request: fc20230330_models.PutProvisionConfigRequest,
    ) -> fc20230330_models.PutProvisionConfigResponse:
        """
        设置函数预留配置。
        
        @param request: PutProvisionConfigRequest
        @return: PutProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_provision_config_with_options_async(function_name, request, headers, runtime)

    def tag_resource_with_options(
        self,
        request: fc20230330_models.TagResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.TagResourceResponse:
        """
        设置资源标签。
        
        @param request: TagResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.TagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resource_with_options_async(
        self,
        request: fc20230330_models.TagResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.TagResourceResponse:
        """
        设置资源标签。
        
        @param request: TagResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.TagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resource(
        self,
        request: fc20230330_models.TagResourceRequest,
    ) -> fc20230330_models.TagResourceResponse:
        """
        设置资源标签。
        
        @param request: TagResourceRequest
        @return: TagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resource_with_options(request, headers, runtime)

    async def tag_resource_async(
        self,
        request: fc20230330_models.TagResourceRequest,
    ) -> fc20230330_models.TagResourceResponse:
        """
        设置资源标签。
        
        @param request: TagResourceRequest
        @return: TagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resource_with_options_async(request, headers, runtime)

    def untag_resource_with_options(
        self,
        request: fc20230330_models.UntagResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UntagResourceResponse:
        """
        删除资源标签。
        
        @param request: UntagResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.arn):
            query['arn'] = request.arn
        if not UtilClient.is_unset(request.tag_keys):
            query['tagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tag',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.UntagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resource_with_options_async(
        self,
        request: fc20230330_models.UntagResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UntagResourceResponse:
        """
        删除资源标签。
        
        @param request: UntagResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.arn):
            query['arn'] = request.arn
        if not UtilClient.is_unset(request.tag_keys):
            query['tagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tag',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.UntagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resource(
        self,
        request: fc20230330_models.UntagResourceRequest,
    ) -> fc20230330_models.UntagResourceResponse:
        """
        删除资源标签。
        
        @param request: UntagResourceRequest
        @return: UntagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resource_with_options(request, headers, runtime)

    async def untag_resource_async(
        self,
        request: fc20230330_models.UntagResourceRequest,
    ) -> fc20230330_models.UntagResourceResponse:
        """
        删除资源标签。
        
        @param request: UntagResourceRequest
        @return: UntagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resource_with_options_async(request, headers, runtime)

    def update_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        request: fc20230330_models.UpdateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateAliasResponse:
        """
        更新函数别名。
        
        @param request: UpdateAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        function_name: str,
        alias_name: str,
        request: fc20230330_models.UpdateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateAliasResponse:
        """
        更新函数别名。
        
        @param request: UpdateAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/aliases/{OpenApiUtilClient.get_encode_param(alias_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alias(
        self,
        function_name: str,
        alias_name: str,
        request: fc20230330_models.UpdateAliasRequest,
    ) -> fc20230330_models.UpdateAliasResponse:
        """
        更新函数别名。
        
        @param request: UpdateAliasRequest
        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_alias_with_options(function_name, alias_name, request, headers, runtime)

    async def update_alias_async(
        self,
        function_name: str,
        alias_name: str,
        request: fc20230330_models.UpdateAliasRequest,
    ) -> fc20230330_models.UpdateAliasResponse:
        """
        更新函数别名。
        
        @param request: UpdateAliasRequest
        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_alias_with_options_async(function_name, alias_name, request, headers, runtime)

    def update_custom_domain_with_options(
        self,
        domain_name: str,
        request: fc20230330_models.UpdateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateCustomDomainResponse:
        """
        更新自定义域名。
        
        @param request: UpdateCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: fc20230330_models.UpdateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateCustomDomainResponse:
        """
        更新自定义域名。
        
        @param request: UpdateCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_domain(
        self,
        domain_name: str,
        request: fc20230330_models.UpdateCustomDomainRequest,
    ) -> fc20230330_models.UpdateCustomDomainResponse:
        """
        更新自定义域名。
        
        @param request: UpdateCustomDomainRequest
        @return: UpdateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_custom_domain_with_options(domain_name, request, headers, runtime)

    async def update_custom_domain_async(
        self,
        domain_name: str,
        request: fc20230330_models.UpdateCustomDomainRequest,
    ) -> fc20230330_models.UpdateCustomDomainResponse:
        """
        更新自定义域名。
        
        @param request: UpdateCustomDomainRequest
        @return: UpdateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def update_function_with_options(
        self,
        function_name: str,
        request: fc20230330_models.UpdateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateFunctionResponse:
        """
        更新函数。
        
        @param request: UpdateFunctionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.UpdateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateFunctionResponse:
        """
        更新函数。
        
        @param request: UpdateFunctionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        function_name: str,
        request: fc20230330_models.UpdateFunctionRequest,
    ) -> fc20230330_models.UpdateFunctionResponse:
        """
        更新函数。
        
        @param request: UpdateFunctionRequest
        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_with_options(function_name, request, headers, runtime)

    async def update_function_async(
        self,
        function_name: str,
        request: fc20230330_models.UpdateFunctionRequest,
    ) -> fc20230330_models.UpdateFunctionResponse:
        """
        更新函数。
        
        @param request: UpdateFunctionRequest
        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_function_with_options_async(function_name, request, headers, runtime)

    def update_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        request: fc20230330_models.UpdateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateTriggerResponse:
        """
        更新函数触发器。
        
        @param request: UpdateTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        function_name: str,
        trigger_name: str,
        request: fc20230330_models.UpdateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateTriggerResponse:
        """
        更新函数触发器。
        
        @param request: UpdateTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/triggers/{OpenApiUtilClient.get_encode_param(trigger_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trigger(
        self,
        function_name: str,
        trigger_name: str,
        request: fc20230330_models.UpdateTriggerRequest,
    ) -> fc20230330_models.UpdateTriggerResponse:
        """
        更新函数触发器。
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_trigger_with_options(function_name, trigger_name, request, headers, runtime)

    async def update_trigger_async(
        self,
        function_name: str,
        trigger_name: str,
        request: fc20230330_models.UpdateTriggerRequest,
    ) -> fc20230330_models.UpdateTriggerResponse:
        """
        更新函数触发器。
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_trigger_with_options_async(function_name, trigger_name, request, headers, runtime)
