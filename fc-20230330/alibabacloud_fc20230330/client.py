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
        @summary 创建函数别名。
        
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
        @summary 创建函数别名。
        
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
        @summary 创建函数别名。
        
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
        @summary 创建函数别名。
        
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
        @summary 创建自定义域名。
        
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
        @summary 创建自定义域名。
        
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
        @summary 创建自定义域名。
        
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
        @summary 创建自定义域名。
        
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
        @summary Creates a function.
        
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
        @summary Creates a function.
        
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
        @summary Creates a function.
        
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
        @summary Creates a function.
        
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
        @summary 创建层版本。
        
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
        @summary 创建层版本。
        
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
        @summary 创建层版本。
        
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
        @summary 创建层版本。
        
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
        @summary 创建函数触发器。
        
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
        @summary 创建函数触发器。
        
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
        @summary 创建函数触发器。
        
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
        @summary 创建函数触发器。
        
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
        @summary Creates a VPC connection.
        
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
        @summary Creates a VPC connection.
        
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
        @summary Creates a VPC connection.
        
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
        @summary Creates a VPC connection.
        
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
        @summary Deletes an alias.
        
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
        @summary Deletes an alias.
        
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
        @summary Deletes an alias.
        
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
        @summary Deletes an alias.
        
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
        @summary Deletes an asynchronous invocation configuration.
        
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
        @summary Deletes an asynchronous invocation configuration.
        
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
        @summary Deletes an asynchronous invocation configuration.
        
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
        @summary Deletes an asynchronous invocation configuration.
        
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
        @summary Deletes a concurrency configuration.
        
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
        @summary Deletes a concurrency configuration.
        
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
        @summary Deletes a concurrency configuration.
        
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
        @summary Deletes a concurrency configuration.
        
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
        @summary Deletes a custom domain name.
        
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
        @summary Deletes a custom domain name.
        
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
        @summary Deletes a custom domain name.
        
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
        @summary Deletes a custom domain name.
        
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
        @summary Deletes a function.
        
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
        @summary Deletes a function.
        
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
        @summary Deletes a function.
        
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
        @summary Deletes a function.
        
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
        @summary Deletes a function version.
        
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
        @summary Deletes a function version.
        
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
        @summary Deletes a function version.
        
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
        @summary Deletes a function version.
        
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
        @summary Deletes a layer version.
        
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
        @summary Deletes a layer version.
        
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
        @summary Deletes a layer version.
        
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
        @summary Deletes a layer version.
        
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
        @summary Deletes a provisioned configuration.
        
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
        @summary Deletes a provisioned configuration.
        
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
        @summary Deletes a provisioned configuration.
        
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
        @summary Deletes a provisioned configuration.
        
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
        @summary Deletes a trigger.
        
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
        @summary Deletes a trigger.
        
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
        @summary Deletes a trigger.
        
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
        @summary Deletes a trigger.
        
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
        @summary Deletes an access control policy from a specified policy group for a VPC firewall.
        
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
        @summary Deletes an access control policy from a specified policy group for a VPC firewall.
        
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
        @summary Deletes an access control policy from a specified policy group for a VPC firewall.
        
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
        @summary Deletes an access control policy from a specified policy group for a VPC firewall.
        
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
        @summary Queries information about an alias.
        
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
        @summary Queries information about an alias.
        
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
        @summary Queries information about an alias.
        
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
        @summary Queries information about an alias.
        
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
        @summary Gets asynchronous invocation configurations of a function.
        
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
        @summary Gets asynchronous invocation configurations of a function.
        
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
        @summary Gets asynchronous invocation configurations of a function.
        
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
        @summary Gets asynchronous invocation configurations of a function.
        
        @param request: GetAsyncInvokeConfigRequest
        @return: GetAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def get_async_task_with_options(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncTaskResponse
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
            action='GetAsyncTask',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_task_with_options_async(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncTaskResponse
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
            action='GetAsyncTask',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_task(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.GetAsyncTaskRequest,
    ) -> fc20230330_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @return: GetAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(function_name, task_id, request, headers, runtime)

    async def get_async_task_async(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.GetAsyncTaskRequest,
    ) -> fc20230330_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @return: GetAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_async_task_with_options_async(function_name, task_id, request, headers, runtime)

    def get_concurrency_config_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetConcurrencyConfigResponse:
        """
        @summary Obtains a concurrency configuration.
        
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
        @summary Obtains a concurrency configuration.
        
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
        @summary Obtains a concurrency configuration.
        
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
        @summary Obtains a concurrency configuration.
        
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
        @summary Queries information about a custom domain name.
        
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
        @summary Queries information about a custom domain name.
        
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
        @summary Queries information about a custom domain name.
        
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
        @summary Queries information about a custom domain name.
        
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
        @summary Queries information about a function.
        
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
        @summary Queries information about a function.
        
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
        @summary Queries information about a function.
        
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
        @summary Queries information about a function.
        
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
        @summary Queries a code package of a function.
        
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
        @summary Queries a code package of a function.
        
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
        @summary Queries a code package of a function.
        
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
        @summary Queries a code package of a function.
        
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
        @summary Queries versions of a layer.
        
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
        @summary Queries versions of a layer.
        
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
        @summary Queries versions of a layer.
        
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
        @summary Queries versions of a layer.
        
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
        @summary Obtain version information of a layer by using ARNs.
        
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
        @summary Obtain version information of a layer by using ARNs.
        
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
        @summary Obtain version information of a layer by using ARNs.
        
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
        @summary Obtain version information of a layer by using ARNs.
        
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
        @summary Queries provisioned configurations.
        
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
        @summary Queries provisioned configurations.
        
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
        @summary Queries provisioned configurations.
        
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
        @summary Queries provisioned configurations.
        
        @param request: GetProvisionConfigRequest
        @return: GetProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_provision_config_with_options_async(function_name, request, headers, runtime)

    def get_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.GetTriggerResponse:
        """
        @summary Queries information about a trigger.
        
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
        @summary Queries information about a trigger.
        
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
        @summary Queries information about a trigger.
        
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
        @summary Queries information about a trigger.
        
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
        @summary Invokes a function.
        
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
        if not UtilClient.is_unset(headers.x_fc_async_task_id):
            real_headers['x-fc-async-task-id'] = UtilClient.to_jsonstring(headers.x_fc_async_task_id)
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
        @summary Invokes a function.
        
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
        if not UtilClient.is_unset(headers.x_fc_async_task_id):
            real_headers['x-fc-async-task-id'] = UtilClient.to_jsonstring(headers.x_fc_async_task_id)
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
        @summary Invokes a function.
        
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
        @summary Invokes a function.
        
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
        @summary Queries aliases.
        
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
        @summary Queries aliases.
        
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
        @summary Queries aliases.
        
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
        @summary Queries aliases.
        
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
        @summary Queries all asynchronous configurations of a function.
        
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
        @summary Queries all asynchronous configurations of a function.
        
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
        @summary Queries all asynchronous configurations of a function.
        
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
        @summary Queries all asynchronous configurations of a function.
        
        @param request: ListAsyncInvokeConfigsRequest
        @return: ListAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_async_invoke_configs_with_options_async(request, headers, runtime)

    def list_async_tasks_with_options(
        self,
        function_name: str,
        request: fc20230330_models.ListAsyncTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListAsyncTasksResponse:
        """
        @summary Lists asynchronous tasks.
        
        @param request: ListAsyncTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_payload):
            query['includePayload'] = request.include_payload
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not UtilClient.is_unset(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not UtilClient.is_unset(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_tasks_with_options_async(
        self,
        function_name: str,
        request: fc20230330_models.ListAsyncTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListAsyncTasksResponse:
        """
        @summary Lists asynchronous tasks.
        
        @param request: ListAsyncTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_payload):
            query['includePayload'] = request.include_payload
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not UtilClient.is_unset(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not UtilClient.is_unset(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_tasks(
        self,
        function_name: str,
        request: fc20230330_models.ListAsyncTasksRequest,
    ) -> fc20230330_models.ListAsyncTasksResponse:
        """
        @summary Lists asynchronous tasks.
        
        @param request: ListAsyncTasksRequest
        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_async_tasks_with_options(function_name, request, headers, runtime)

    async def list_async_tasks_async(
        self,
        function_name: str,
        request: fc20230330_models.ListAsyncTasksRequest,
    ) -> fc20230330_models.ListAsyncTasksResponse:
        """
        @summary Lists asynchronous tasks.
        
        @param request: ListAsyncTasksRequest
        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_async_tasks_with_options_async(function_name, request, headers, runtime)

    def list_concurrency_configs_with_options(
        self,
        request: fc20230330_models.ListConcurrencyConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListConcurrencyConfigsResponse:
        """
        @summary 列出函数并发度配置。
        
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
        @summary 列出函数并发度配置。
        
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
        @summary 列出函数并发度配置。
        
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
        @summary 列出函数并发度配置。
        
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
        @summary Queries custom domain names.
        
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
        @summary Queries custom domain names.
        
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
        @summary Queries custom domain names.
        
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
        @summary Queries custom domain names.
        
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
        @summary Queries versions of a function.
        
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
        @summary Queries versions of a function.
        
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
        @summary Queries versions of a function.
        
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
        @summary Queries versions of a function.
        
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
        @summary 列出函数。
        
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
        @summary 列出函数。
        
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
        @summary 列出函数。
        
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
        @summary 列出函数。
        
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
        @summary Queries a list of function instances.
        
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
        @summary Queries a list of function instances.
        
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
        @summary Queries a list of function instances.
        
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
        @summary Queries a list of function instances.
        
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
        @summary Gets a list of layer versions.
        
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
        @summary Gets a list of layer versions.
        
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
        @summary Gets a list of layer versions.
        
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
        @summary Gets a list of layer versions.
        
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
        @summary Gets a list of layers.
        
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
        @summary Gets a list of layers.
        
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
        @summary Gets a list of layers.
        
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
        @summary Gets a list of layers.
        
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
        @summary Queries a list of provisioned configurations.
        
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
        @summary Queries a list of provisioned configurations.
        
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
        @summary Queries a list of provisioned configurations.
        
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
        @summary Queries a list of provisioned configurations.
        
        @param request: ListProvisionConfigsRequest
        @return: ListProvisionConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_provision_configs_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: fc20230330_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTagResourcesResponse:
        """
        @summary Lists all tagged resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags-v2',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: fc20230330_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTagResourcesResponse:
        """
        @summary Lists all tagged resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags-v2',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: fc20230330_models.ListTagResourcesRequest,
    ) -> fc20230330_models.ListTagResourcesResponse:
        """
        @summary Lists all tagged resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: fc20230330_models.ListTagResourcesRequest,
    ) -> fc20230330_models.ListTagResourcesResponse:
        """
        @summary Lists all tagged resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_triggers_with_options(
        self,
        function_name: str,
        request: fc20230330_models.ListTriggersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.ListTriggersResponse:
        """
        @summary Queries the triggers of a function.
        
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
        @summary Queries the triggers of a function.
        
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
        @summary Queries the triggers of a function.
        
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
        @summary Queries the triggers of a function.
        
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
        @summary Queries a list of existing VPC connections.
        
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
        @summary Queries a list of existing VPC connections.
        
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
        @summary Queries a list of existing VPC connections.
        
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
        @summary Queries a list of existing VPC connections.
        
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
        @summary Publishes a function version.
        
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
        @summary Publishes a function version.
        
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
        @summary Publishes a function version.
        
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
        @summary Publishes a function version.
        
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
        @summary Creates or modifies an asynchronous invocation configuration for a function.
        
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
        @summary Creates or modifies an asynchronous invocation configuration for a function.
        
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
        @summary Creates or modifies an asynchronous invocation configuration for a function.
        
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
        @summary Creates or modifies an asynchronous invocation configuration for a function.
        
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
        @summary Configures concurrency of a function.
        
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
        @summary Configures concurrency of a function.
        
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
        @summary Configures concurrency of a function.
        
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
        @summary Configures concurrency of a function.
        
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
        @summary Modifies permissions of a layer.
        
        @param request: PutLayerACLRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutLayerACLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl):
            query['acl'] = request.acl
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
        @summary Modifies permissions of a layer.
        
        @param request: PutLayerACLRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutLayerACLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl):
            query['acl'] = request.acl
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
        @summary Modifies permissions of a layer.
        
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
        @summary Modifies permissions of a layer.
        
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
        @summary Creates provisioned configurations.
        
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
        @summary Creates provisioned configurations.
        
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
        @summary Creates provisioned configurations.
        
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
        @summary Creates provisioned configurations.
        
        @param request: PutProvisionConfigRequest
        @return: PutProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_provision_config_with_options_async(function_name, request, headers, runtime)

    def stop_async_task_with_options(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.StopAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.StopAsyncTaskResponse:
        """
        @summary Stops an asynchronous task.
        
        @param request: StopAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAsyncTaskResponse
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
            action='StopAsyncTask',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-tasks/{OpenApiUtilClient.get_encode_param(task_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.StopAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_async_task_with_options_async(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.StopAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.StopAsyncTaskResponse:
        """
        @summary Stops an asynchronous task.
        
        @param request: StopAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAsyncTaskResponse
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
            action='StopAsyncTask',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/functions/{OpenApiUtilClient.get_encode_param(function_name)}/async-tasks/{OpenApiUtilClient.get_encode_param(task_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.StopAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_async_task(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.StopAsyncTaskRequest,
    ) -> fc20230330_models.StopAsyncTaskResponse:
        """
        @summary Stops an asynchronous task.
        
        @param request: StopAsyncTaskRequest
        @return: StopAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_async_task_with_options(function_name, task_id, request, headers, runtime)

    async def stop_async_task_async(
        self,
        function_name: str,
        task_id: str,
        request: fc20230330_models.StopAsyncTaskRequest,
    ) -> fc20230330_models.StopAsyncTaskResponse:
        """
        @summary Stops an asynchronous task.
        
        @param request: StopAsyncTaskRequest
        @return: StopAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_async_task_with_options_async(function_name, task_id, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: fc20230330_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.TagResourcesResponse:
        """
        @summary Adds tags to a resource.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags-v2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: fc20230330_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.TagResourcesResponse:
        """
        @summary Adds tags to a resource.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags-v2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: fc20230330_models.TagResourcesRequest,
    ) -> fc20230330_models.TagResourcesResponse:
        """
        @summary Adds tags to a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: fc20230330_models.TagResourcesRequest,
    ) -> fc20230330_models.TagResourcesResponse:
        """
        @summary Adds tags to a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: fc20230330_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags-v2',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: fc20230330_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname=f'/2023-03-30/tags-v2',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: fc20230330_models.UntagResourcesRequest,
    ) -> fc20230330_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: fc20230330_models.UntagResourcesRequest,
    ) -> fc20230330_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        request: fc20230330_models.UpdateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fc20230330_models.UpdateAliasResponse:
        """
        @summary Updates an alias.
        
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
        @summary Updates an alias.
        
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
        @summary Updates an alias.
        
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
        @summary Updates an alias.
        
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
        @summary Update a custom domain name.
        
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
        @summary Update a custom domain name.
        
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
        @summary Update a custom domain name.
        
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
        @summary Update a custom domain name.
        
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
        @summary Updates the information about a function.
        
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
        @summary Updates the information about a function.
        
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
        @summary Updates the information about a function.
        
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
        @summary Updates the information about a function.
        
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
        @summary Modifies a trigger.
        
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
        @summary Modifies a trigger.
        
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
        @summary Modifies a trigger.
        
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
        @summary Modifies a trigger.
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_trigger_with_options_async(function_name, trigger_name, request, headers, runtime)
