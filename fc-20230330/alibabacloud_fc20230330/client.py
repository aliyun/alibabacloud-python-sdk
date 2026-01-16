# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_fc20230330 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL
from darabonba.utils.stream import Stream as DaraStream

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/resource-groups',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/resource-groups',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_alias_with_options(
        self,
        function_name: str,
        request: main_models.CreateAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAliasResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        function_name: str,
        request: main_models.CreateAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAliasResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alias(
        self,
        function_name: str,
        request: main_models.CreateAliasRequest,
    ) -> main_models.CreateAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_alias_with_options(function_name, request, headers, runtime)

    async def create_alias_async(
        self,
        function_name: str,
        request: main_models.CreateAliasRequest,
    ) -> main_models.CreateAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_alias_with_options_async(function_name, request, headers, runtime)

    def create_custom_domain_with_options(
        self,
        request: main_models.CreateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomDomainResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_domain_with_options_async(
        self,
        request: main_models.CreateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomDomainResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_domain(
        self,
        request: main_models.CreateCustomDomainRequest,
    ) -> main_models.CreateCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_custom_domain_with_options(request, headers, runtime)

    async def create_custom_domain_async(
        self,
        request: main_models.CreateCustomDomainRequest,
    ) -> main_models.CreateCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_custom_domain_with_options_async(request, headers, runtime)

    def create_function_with_options(
        self,
        request: main_models.CreateFunctionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: main_models.CreateFunctionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        request: main_models.CreateFunctionRequest,
    ) -> main_models.CreateFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_function_with_options(request, headers, runtime)

    async def create_function_async(
        self,
        request: main_models.CreateFunctionRequest,
    ) -> main_models.CreateFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_function_with_options_async(request, headers, runtime)

    def create_layer_version_with_options(
        self,
        layer_name: str,
        request: main_models.CreateLayerVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayerVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayerVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_version_with_options_async(
        self,
        layer_name: str,
        request: main_models.CreateLayerVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayerVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayerVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer_version(
        self,
        layer_name: str,
        request: main_models.CreateLayerVersionRequest,
    ) -> main_models.CreateLayerVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_layer_version_with_options(layer_name, request, headers, runtime)

    async def create_layer_version_async(
        self,
        layer_name: str,
        request: main_models.CreateLayerVersionRequest,
    ) -> main_models.CreateLayerVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_layer_version_with_options_async(layer_name, request, headers, runtime)

    def create_session_with_options(
        self,
        function_name: str,
        request: main_models.CreateSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_with_options_async(
        self,
        function_name: str,
        request: main_models.CreateSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session(
        self,
        function_name: str,
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_session_with_options(function_name, request, headers, runtime)

    async def create_session_async(
        self,
        function_name: str,
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_session_with_options_async(function_name, request, headers, runtime)

    def create_trigger_with_options(
        self,
        function_name: str,
        request: main_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTriggerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        function_name: str,
        request: main_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTriggerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        function_name: str,
        request: main_models.CreateTriggerRequest,
    ) -> main_models.CreateTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(function_name, request, headers, runtime)

    async def create_trigger_async(
        self,
        function_name: str,
        request: main_models.CreateTriggerRequest,
    ) -> main_models.CreateTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_trigger_with_options_async(function_name, request, headers, runtime)

    def create_vpc_binding_with_options(
        self,
        function_name: str,
        request: main_models.CreateVpcBindingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcBindingResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcBinding',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/vpc-bindings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_binding_with_options_async(
        self,
        function_name: str,
        request: main_models.CreateVpcBindingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcBindingResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcBinding',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/vpc-bindings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateVpcBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_binding(
        self,
        function_name: str,
        request: main_models.CreateVpcBindingRequest,
    ) -> main_models.CreateVpcBindingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_vpc_binding_with_options(function_name, request, headers, runtime)

    async def create_vpc_binding_async(
        self,
        function_name: str,
        request: main_models.CreateVpcBindingRequest,
    ) -> main_models.CreateVpcBindingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_vpc_binding_with_options_async(function_name, request, headers, runtime)

    def delete_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAliasResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases/{DaraURL.percent_encode(alias_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAliasResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases/{DaraURL.percent_encode(alias_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alias(
        self,
        function_name: str,
        alias_name: str,
    ) -> main_models.DeleteAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_alias_with_options(function_name, alias_name, headers, runtime)

    async def delete_alias_async(
        self,
        function_name: str,
        alias_name: str,
    ) -> main_models.DeleteAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_alias_with_options_async(function_name, alias_name, headers, runtime)

    def delete_async_invoke_config_with_options(
        self,
        function_name: str,
        request: main_models.DeleteAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsyncInvokeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsyncInvokeConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-invoke-config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_async_invoke_config_with_options_async(
        self,
        function_name: str,
        request: main_models.DeleteAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsyncInvokeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsyncInvokeConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-invoke-config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_async_invoke_config(
        self,
        function_name: str,
        request: main_models.DeleteAsyncInvokeConfigRequest,
    ) -> main_models.DeleteAsyncInvokeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_async_invoke_config_with_options(function_name, request, headers, runtime)

    async def delete_async_invoke_config_async(
        self,
        function_name: str,
        request: main_models.DeleteAsyncInvokeConfigRequest,
    ) -> main_models.DeleteAsyncInvokeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def delete_concurrency_config_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConcurrencyConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConcurrencyConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/concurrency',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_concurrency_config_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConcurrencyConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConcurrencyConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/concurrency',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConcurrencyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_concurrency_config(
        self,
        function_name: str,
    ) -> main_models.DeleteConcurrencyConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_concurrency_config_with_options(function_name, headers, runtime)

    async def delete_concurrency_config_async(
        self,
        function_name: str,
    ) -> main_models.DeleteConcurrencyConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_concurrency_config_with_options_async(function_name, headers, runtime)

    def delete_custom_domain_with_options(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_domain_with_options_async(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_domain(
        self,
        domain_name: str,
    ) -> main_models.DeleteCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_custom_domain_with_options(domain_name, headers, runtime)

    async def delete_custom_domain_async(
        self,
        domain_name: str,
    ) -> main_models.DeleteCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_custom_domain_with_options_async(domain_name, headers, runtime)

    def delete_function_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        function_name: str,
    ) -> main_models.DeleteFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_function_with_options(function_name, headers, runtime)

    async def delete_function_async(
        self,
        function_name: str,
    ) -> main_models.DeleteFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_function_with_options_async(function_name, headers, runtime)

    def delete_function_version_with_options(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/versions/{DaraURL.percent_encode(version_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_version_with_options_async(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/versions/{DaraURL.percent_encode(version_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_version(
        self,
        function_name: str,
        version_id: str,
    ) -> main_models.DeleteFunctionVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_function_version_with_options(function_name, version_id, headers, runtime)

    async def delete_function_version_async(
        self,
        function_name: str,
        version_id: str,
    ) -> main_models.DeleteFunctionVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_function_version_with_options_async(function_name, version_id, headers, runtime)

    def delete_layer_version_with_options(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayerVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayerVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions/{DaraURL.percent_encode(version)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_version_with_options_async(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayerVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayerVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions/{DaraURL.percent_encode(version)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer_version(
        self,
        layer_name: str,
        version: str,
    ) -> main_models.DeleteLayerVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_layer_version_with_options(layer_name, version, headers, runtime)

    async def delete_layer_version_async(
        self,
        layer_name: str,
        version: str,
    ) -> main_models.DeleteLayerVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_layer_version_with_options_async(layer_name, version, headers, runtime)

    def delete_provision_config_with_options(
        self,
        function_name: str,
        request: main_models.DeleteProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProvisionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProvisionConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/provision-config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_provision_config_with_options_async(
        self,
        function_name: str,
        request: main_models.DeleteProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProvisionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProvisionConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/provision-config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_provision_config(
        self,
        function_name: str,
        request: main_models.DeleteProvisionConfigRequest,
    ) -> main_models.DeleteProvisionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_provision_config_with_options(function_name, request, headers, runtime)

    async def delete_provision_config_async(
        self,
        function_name: str,
        request: main_models.DeleteProvisionConfigRequest,
    ) -> main_models.DeleteProvisionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_provision_config_with_options_async(function_name, request, headers, runtime)

    def delete_scaling_config_with_options(
        self,
        function_name: str,
        request: main_models.DeleteScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/scaling-config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_config_with_options_async(
        self,
        function_name: str,
        request: main_models.DeleteScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/scaling-config',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_config(
        self,
        function_name: str,
        request: main_models.DeleteScalingConfigRequest,
    ) -> main_models.DeleteScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_scaling_config_with_options(function_name, request, headers, runtime)

    async def delete_scaling_config_async(
        self,
        function_name: str,
        request: main_models.DeleteScalingConfigRequest,
    ) -> main_models.DeleteScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_scaling_config_with_options_async(function_name, request, headers, runtime)

    def delete_session_with_options(
        self,
        function_name: str,
        session_id: str,
        request: main_models.DeleteSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_session_with_options_async(
        self,
        function_name: str,
        session_id: str,
        request: main_models.DeleteSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_session(
        self,
        function_name: str,
        session_id: str,
        request: main_models.DeleteSessionRequest,
    ) -> main_models.DeleteSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_session_with_options(function_name, session_id, request, headers, runtime)

    async def delete_session_async(
        self,
        function_name: str,
        session_id: str,
        request: main_models.DeleteSessionRequest,
    ) -> main_models.DeleteSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_session_with_options_async(function_name, session_id, request, headers, runtime)

    def delete_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers/{DaraURL.percent_encode(trigger_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers/{DaraURL.percent_encode(trigger_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        function_name: str,
        trigger_name: str,
    ) -> main_models.DeleteTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(function_name, trigger_name, headers, runtime)

    async def delete_trigger_async(
        self,
        function_name: str,
        trigger_name: str,
    ) -> main_models.DeleteTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_trigger_with_options_async(function_name, trigger_name, headers, runtime)

    def delete_vpc_binding_with_options(
        self,
        function_name: str,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcBindingResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcBinding',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/vpc-bindings/{DaraURL.percent_encode(vpc_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_binding_with_options_async(
        self,
        function_name: str,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcBindingResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcBinding',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/vpc-bindings/{DaraURL.percent_encode(vpc_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_binding(
        self,
        function_name: str,
        vpc_id: str,
    ) -> main_models.DeleteVpcBindingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_vpc_binding_with_options(function_name, vpc_id, headers, runtime)

    async def delete_vpc_binding_async(
        self,
        function_name: str,
        vpc_id: str,
    ) -> main_models.DeleteVpcBindingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_vpc_binding_with_options_async(function_name, vpc_id, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def disable_function_invocation_with_options(
        self,
        function_name: str,
        request: main_models.DisableFunctionInvocationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableFunctionInvocationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abort_ongoing_request):
            body['abortOngoingRequest'] = request.abort_ongoing_request
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableFunctionInvocation',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/invoke/disable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFunctionInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_function_invocation_with_options_async(
        self,
        function_name: str,
        request: main_models.DisableFunctionInvocationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableFunctionInvocationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abort_ongoing_request):
            body['abortOngoingRequest'] = request.abort_ongoing_request
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableFunctionInvocation',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/invoke/disable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFunctionInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_function_invocation(
        self,
        function_name: str,
        request: main_models.DisableFunctionInvocationRequest,
    ) -> main_models.DisableFunctionInvocationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_function_invocation_with_options(function_name, request, headers, runtime)

    async def disable_function_invocation_async(
        self,
        function_name: str,
        request: main_models.DisableFunctionInvocationRequest,
    ) -> main_models.DisableFunctionInvocationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_function_invocation_with_options_async(function_name, request, headers, runtime)

    def enable_function_invocation_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableFunctionInvocationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableFunctionInvocation',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/invoke/enable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFunctionInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_function_invocation_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableFunctionInvocationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableFunctionInvocation',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/invoke/enable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFunctionInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_function_invocation(
        self,
        function_name: str,
    ) -> main_models.EnableFunctionInvocationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_function_invocation_with_options(function_name, headers, runtime)

    async def enable_function_invocation_async(
        self,
        function_name: str,
    ) -> main_models.EnableFunctionInvocationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_function_invocation_with_options_async(function_name, headers, runtime)

    def get_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAliasResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases/{DaraURL.percent_encode(alias_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alias_with_options_async(
        self,
        function_name: str,
        alias_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAliasResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases/{DaraURL.percent_encode(alias_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alias(
        self,
        function_name: str,
        alias_name: str,
    ) -> main_models.GetAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_alias_with_options(function_name, alias_name, headers, runtime)

    async def get_alias_async(
        self,
        function_name: str,
        alias_name: str,
    ) -> main_models.GetAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_alias_with_options_async(function_name, alias_name, headers, runtime)

    def get_async_invoke_config_with_options(
        self,
        function_name: str,
        request: main_models.GetAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncInvokeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncInvokeConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-invoke-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_invoke_config_with_options_async(
        self,
        function_name: str,
        request: main_models.GetAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncInvokeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncInvokeConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-invoke-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_invoke_config(
        self,
        function_name: str,
        request: main_models.GetAsyncInvokeConfigRequest,
    ) -> main_models.GetAsyncInvokeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_async_invoke_config_with_options(function_name, request, headers, runtime)

    async def get_async_invoke_config_async(
        self,
        function_name: str,
        request: main_models.GetAsyncInvokeConfigRequest,
    ) -> main_models.GetAsyncInvokeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def get_async_task_with_options(
        self,
        function_name: str,
        task_id: str,
        request: main_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncTask',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_task_with_options_async(
        self,
        function_name: str,
        task_id: str,
        request: main_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncTask',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_task(
        self,
        function_name: str,
        task_id: str,
        request: main_models.GetAsyncTaskRequest,
    ) -> main_models.GetAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(function_name, task_id, request, headers, runtime)

    async def get_async_task_async(
        self,
        function_name: str,
        task_id: str,
        request: main_models.GetAsyncTaskRequest,
    ) -> main_models.GetAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_async_task_with_options_async(function_name, task_id, request, headers, runtime)

    def get_concurrency_config_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConcurrencyConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConcurrencyConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/concurrency',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_concurrency_config_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConcurrencyConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConcurrencyConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/concurrency',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConcurrencyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_concurrency_config(
        self,
        function_name: str,
    ) -> main_models.GetConcurrencyConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_concurrency_config_with_options(function_name, headers, runtime)

    async def get_concurrency_config_async(
        self,
        function_name: str,
    ) -> main_models.GetConcurrencyConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_concurrency_config_with_options_async(function_name, headers, runtime)

    def get_custom_domain_with_options(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_domain_with_options_async(
        self,
        domain_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_domain(
        self,
        domain_name: str,
    ) -> main_models.GetCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_custom_domain_with_options(domain_name, headers, runtime)

    async def get_custom_domain_async(
        self,
        domain_name: str,
    ) -> main_models.GetCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_custom_domain_with_options_async(domain_name, headers, runtime)

    def get_function_with_options(
        self,
        function_name: str,
        request: main_models.GetFunctionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        function_name: str,
        request: main_models.GetFunctionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        function_name: str,
        request: main_models.GetFunctionRequest,
    ) -> main_models.GetFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_with_options(function_name, request, headers, runtime)

    async def get_function_async(
        self,
        function_name: str,
        request: main_models.GetFunctionRequest,
    ) -> main_models.GetFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_with_options_async(function_name, request, headers, runtime)

    def get_function_code_with_options(
        self,
        function_name: str,
        request: main_models.GetFunctionCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionCode',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/code',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_code_with_options_async(
        self,
        function_name: str,
        request: main_models.GetFunctionCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionCode',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/code',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_code(
        self,
        function_name: str,
        request: main_models.GetFunctionCodeRequest,
    ) -> main_models.GetFunctionCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_code_with_options(function_name, request, headers, runtime)

    async def get_function_code_async(
        self,
        function_name: str,
        request: main_models.GetFunctionCodeRequest,
    ) -> main_models.GetFunctionCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_code_with_options_async(function_name, request, headers, runtime)

    def get_layer_version_with_options(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLayerVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLayerVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions/{DaraURL.percent_encode(version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_version_with_options_async(
        self,
        layer_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLayerVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLayerVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions/{DaraURL.percent_encode(version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayerVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer_version(
        self,
        layer_name: str,
        version: str,
    ) -> main_models.GetLayerVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_layer_version_with_options(layer_name, version, headers, runtime)

    async def get_layer_version_async(
        self,
        layer_name: str,
        version: str,
    ) -> main_models.GetLayerVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_layer_version_with_options_async(layer_name, version, headers, runtime)

    def get_layer_version_by_arn_with_options(
        self,
        arn: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLayerVersionByArnResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLayerVersionByArn',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layerarn/{DaraURL.percent_encode(arn)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayerVersionByArnResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_version_by_arn_with_options_async(
        self,
        arn: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLayerVersionByArnResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLayerVersionByArn',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layerarn/{DaraURL.percent_encode(arn)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayerVersionByArnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer_version_by_arn(
        self,
        arn: str,
    ) -> main_models.GetLayerVersionByArnResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_layer_version_by_arn_with_options(arn, headers, runtime)

    async def get_layer_version_by_arn_async(
        self,
        arn: str,
    ) -> main_models.GetLayerVersionByArnResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_layer_version_by_arn_with_options_async(arn, headers, runtime)

    def get_provision_config_with_options(
        self,
        function_name: str,
        request: main_models.GetProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProvisionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProvisionConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/provision-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provision_config_with_options_async(
        self,
        function_name: str,
        request: main_models.GetProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProvisionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProvisionConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/provision-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provision_config(
        self,
        function_name: str,
        request: main_models.GetProvisionConfigRequest,
    ) -> main_models.GetProvisionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_provision_config_with_options(function_name, request, headers, runtime)

    async def get_provision_config_async(
        self,
        function_name: str,
        request: main_models.GetProvisionConfigRequest,
    ) -> main_models.GetProvisionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_provision_config_with_options_async(function_name, request, headers, runtime)

    def get_scaling_config_with_options(
        self,
        function_name: str,
        request: main_models.GetScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScalingConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/scaling-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scaling_config_with_options_async(
        self,
        function_name: str,
        request: main_models.GetScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScalingConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/scaling-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scaling_config(
        self,
        function_name: str,
        request: main_models.GetScalingConfigRequest,
    ) -> main_models.GetScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scaling_config_with_options(function_name, request, headers, runtime)

    async def get_scaling_config_async(
        self,
        function_name: str,
        request: main_models.GetScalingConfigRequest,
    ) -> main_models.GetScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scaling_config_with_options_async(function_name, request, headers, runtime)

    def get_session_with_options(
        self,
        function_name: str,
        session_id: str,
        request: main_models.GetSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_with_options_async(
        self,
        function_name: str,
        session_id: str,
        request: main_models.GetSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session(
        self,
        function_name: str,
        session_id: str,
        request: main_models.GetSessionRequest,
    ) -> main_models.GetSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_session_with_options(function_name, session_id, request, headers, runtime)

    async def get_session_async(
        self,
        function_name: str,
        session_id: str,
        request: main_models.GetSessionRequest,
    ) -> main_models.GetSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_session_with_options_async(function_name, session_id, request, headers, runtime)

    def get_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers/{DaraURL.percent_encode(trigger_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trigger_with_options_async(
        self,
        function_name: str,
        trigger_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers/{DaraURL.percent_encode(trigger_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trigger(
        self,
        function_name: str,
        trigger_name: str,
    ) -> main_models.GetTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_trigger_with_options(function_name, trigger_name, headers, runtime)

    async def get_trigger_async(
        self,
        function_name: str,
        trigger_name: str,
    ) -> main_models.GetTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_trigger_with_options_async(function_name, trigger_name, headers, runtime)

    def invoke_function_with_options(
        self,
        function_name: str,
        request: main_models.InvokeFunctionRequest,
        headers: main_models.InvokeFunctionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_fc_async_task_id):
            real_headers['x-fc-async-task-id'] = str(headers.x_fc_async_task_id)
        if not DaraCore.is_null(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = str(headers.x_fc_invocation_type)
        if not DaraCore.is_null(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = str(headers.x_fc_log_type)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = request.body,
            stream = request.body
        )
        params = open_api_util_models.Params(
            action = 'InvokeFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/invocations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'binary'
        )
        res = main_models.InvokeFunctionResponse()
        tmp = self.call_api(params, req, runtime)
        if not DaraCore.is_null(tmp.get("body")):
            resp_body = DaraStream.to_readable(tmp.get("body"))
            res.body = resp_body
        if not DaraCore.is_null(tmp.get("headers")):
            resp_headers = tmp.get("headers")
            res.headers = Utils.stringify_map_value(resp_headers)
        if not DaraCore.is_null(tmp.get("statusCode")):
            status_code = int(tmp.get("statusCode"))
            res.status_code = status_code
        return res

    async def invoke_function_with_options_async(
        self,
        function_name: str,
        request: main_models.InvokeFunctionRequest,
        headers: main_models.InvokeFunctionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_fc_async_task_id):
            real_headers['x-fc-async-task-id'] = str(headers.x_fc_async_task_id)
        if not DaraCore.is_null(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = str(headers.x_fc_invocation_type)
        if not DaraCore.is_null(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = str(headers.x_fc_log_type)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = request.body,
            stream = request.body
        )
        params = open_api_util_models.Params(
            action = 'InvokeFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/invocations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'binary'
        )
        res = main_models.InvokeFunctionResponse()
        tmp = await self.call_api_async(params, req, runtime)
        if not DaraCore.is_null(tmp.get("body")):
            resp_body = DaraStream.to_readable(tmp.get("body"))
            res.body = resp_body
        if not DaraCore.is_null(tmp.get("headers")):
            resp_headers = tmp.get("headers")
            res.headers = Utils.stringify_map_value(resp_headers)
        if not DaraCore.is_null(tmp.get("statusCode")):
            status_code = int(tmp.get("statusCode"))
            res.status_code = status_code
        return res

    def invoke_function(
        self,
        function_name: str,
        request: main_models.InvokeFunctionRequest,
    ) -> main_models.InvokeFunctionResponse:
        runtime = RuntimeOptions()
        headers = main_models.InvokeFunctionHeaders()
        return self.invoke_function_with_options(function_name, request, headers, runtime)

    async def invoke_function_async(
        self,
        function_name: str,
        request: main_models.InvokeFunctionRequest,
    ) -> main_models.InvokeFunctionResponse:
        runtime = RuntimeOptions()
        headers = main_models.InvokeFunctionHeaders()
        return await self.invoke_function_with_options_async(function_name, request, headers, runtime)

    def list_aliases_with_options(
        self,
        function_name: str,
        request: main_models.ListAliasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAliasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAliases',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        function_name: str,
        request: main_models.ListAliasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAliasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAliases',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases(
        self,
        function_name: str,
        request: main_models.ListAliasesRequest,
    ) -> main_models.ListAliasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_aliases_with_options(function_name, request, headers, runtime)

    async def list_aliases_async(
        self,
        function_name: str,
        request: main_models.ListAliasesRequest,
    ) -> main_models.ListAliasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_aliases_with_options_async(function_name, request, headers, runtime)

    def list_async_invoke_configs_with_options(
        self,
        request: main_models.ListAsyncInvokeConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncInvokeConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncInvokeConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/async-invoke-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncInvokeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_invoke_configs_with_options_async(
        self,
        request: main_models.ListAsyncInvokeConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncInvokeConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncInvokeConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/async-invoke-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncInvokeConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_invoke_configs(
        self,
        request: main_models.ListAsyncInvokeConfigsRequest,
    ) -> main_models.ListAsyncInvokeConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_async_invoke_configs_with_options(request, headers, runtime)

    async def list_async_invoke_configs_async(
        self,
        request: main_models.ListAsyncInvokeConfigsRequest,
    ) -> main_models.ListAsyncInvokeConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_async_invoke_configs_with_options_async(request, headers, runtime)

    def list_async_tasks_with_options(
        self,
        function_name: str,
        request: main_models.ListAsyncTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_payload):
            query['includePayload'] = request.include_payload
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        if not DaraCore.is_null(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not DaraCore.is_null(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not DaraCore.is_null(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTasks',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_tasks_with_options_async(
        self,
        function_name: str,
        request: main_models.ListAsyncTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_payload):
            query['includePayload'] = request.include_payload
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        if not DaraCore.is_null(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not DaraCore.is_null(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not DaraCore.is_null(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTasks',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_tasks(
        self,
        function_name: str,
        request: main_models.ListAsyncTasksRequest,
    ) -> main_models.ListAsyncTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_async_tasks_with_options(function_name, request, headers, runtime)

    async def list_async_tasks_async(
        self,
        function_name: str,
        request: main_models.ListAsyncTasksRequest,
    ) -> main_models.ListAsyncTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_async_tasks_with_options_async(function_name, request, headers, runtime)

    def list_concurrency_configs_with_options(
        self,
        request: main_models.ListConcurrencyConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConcurrencyConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConcurrencyConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/concurrency-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConcurrencyConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_concurrency_configs_with_options_async(
        self,
        request: main_models.ListConcurrencyConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConcurrencyConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConcurrencyConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/concurrency-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConcurrencyConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_concurrency_configs(
        self,
        request: main_models.ListConcurrencyConfigsRequest,
    ) -> main_models.ListConcurrencyConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_concurrency_configs_with_options(request, headers, runtime)

    async def list_concurrency_configs_async(
        self,
        request: main_models.ListConcurrencyConfigsRequest,
    ) -> main_models.ListConcurrencyConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_concurrency_configs_with_options_async(request, headers, runtime)

    def list_custom_domains_with_options(
        self,
        request: main_models.ListCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomDomains',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_domains_with_options_async(
        self,
        request: main_models.ListCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomDomains',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_domains(
        self,
        request: main_models.ListCustomDomainsRequest,
    ) -> main_models.ListCustomDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_custom_domains_with_options(request, headers, runtime)

    async def list_custom_domains_async(
        self,
        request: main_models.ListCustomDomainsRequest,
    ) -> main_models.ListCustomDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_custom_domains_with_options_async(request, headers, runtime)

    def list_function_versions_with_options(
        self,
        function_name: str,
        request: main_models.ListFunctionVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionVersions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_versions_with_options_async(
        self,
        function_name: str,
        request: main_models.ListFunctionVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionVersions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_versions(
        self,
        function_name: str,
        request: main_models.ListFunctionVersionsRequest,
    ) -> main_models.ListFunctionVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_function_versions_with_options(function_name, request, headers, runtime)

    async def list_function_versions_async(
        self,
        function_name: str,
        request: main_models.ListFunctionVersionsRequest,
    ) -> main_models.ListFunctionVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_function_versions_with_options_async(function_name, request, headers, runtime)

    def list_functions_with_options(
        self,
        tmp_req: main_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionsResponse:
        tmp_req.validate()
        request = main_models.ListFunctionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.fc_version):
            query['fcVersion'] = request.fc_version
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.gpu_type):
            query['gpuType'] = request.gpu_type
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.runtime):
            query['runtime'] = request.runtime
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        tmp_req: main_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionsResponse:
        tmp_req.validate()
        request = main_models.ListFunctionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.fc_version):
            query['fcVersion'] = request.fc_version
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.gpu_type):
            query['gpuType'] = request.gpu_type
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.runtime):
            query['runtime'] = request.runtime
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        request: main_models.ListFunctionsRequest,
    ) -> main_models.ListFunctionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(request, headers, runtime)

    async def list_functions_async(
        self,
        request: main_models.ListFunctionsRequest,
    ) -> main_models.ListFunctionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_functions_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        function_name: str,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'instanceIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_status):
            request.instance_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_status, 'instanceStatus', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time_ms):
            query['endTimeMs'] = request.end_time_ms
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['instanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.instance_status_shrink):
            query['instanceStatus'] = request.instance_status_shrink
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        if not DaraCore.is_null(request.start_key):
            query['startKey'] = request.start_key
        if not DaraCore.is_null(request.start_time_ms):
            query['startTimeMs'] = request.start_time_ms
        if not DaraCore.is_null(request.with_all_active):
            query['withAllActive'] = request.with_all_active
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        function_name: str,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'instanceIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_status):
            request.instance_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_status, 'instanceStatus', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time_ms):
            query['endTimeMs'] = request.end_time_ms
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['instanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.instance_status_shrink):
            query['instanceStatus'] = request.instance_status_shrink
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        if not DaraCore.is_null(request.start_key):
            query['startKey'] = request.start_key
        if not DaraCore.is_null(request.start_time_ms):
            query['startTimeMs'] = request.start_time_ms
        if not DaraCore.is_null(request.with_all_active):
            query['withAllActive'] = request.with_all_active
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        function_name: str,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(function_name, request, headers, runtime)

    async def list_instances_async(
        self,
        function_name: str,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(function_name, request, headers, runtime)

    def list_layer_versions_with_options(
        self,
        layer_name: str,
        request: main_models.ListLayerVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLayerVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.start_version):
            query['startVersion'] = request.start_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayerVersions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayerVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layer_versions_with_options_async(
        self,
        layer_name: str,
        request: main_models.ListLayerVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLayerVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.start_version):
            query['startVersion'] = request.start_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayerVersions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayerVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layer_versions(
        self,
        layer_name: str,
        request: main_models.ListLayerVersionsRequest,
    ) -> main_models.ListLayerVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_layer_versions_with_options(layer_name, request, headers, runtime)

    async def list_layer_versions_async(
        self,
        layer_name: str,
        request: main_models.ListLayerVersionsRequest,
    ) -> main_models.ListLayerVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_layer_versions_with_options_async(layer_name, request, headers, runtime)

    def list_layers_with_options(
        self,
        request: main_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLayersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.official):
            query['official'] = request.official
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.public):
            query['public'] = request.public
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayers',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layers_with_options_async(
        self,
        request: main_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLayersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.official):
            query['official'] = request.official
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.public):
            query['public'] = request.public
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayers',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layers(
        self,
        request: main_models.ListLayersRequest,
    ) -> main_models.ListLayersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: main_models.ListLayersRequest,
    ) -> main_models.ListLayersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_provision_configs_with_options(
        self,
        request: main_models.ListProvisionConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/provision-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provision_configs_with_options_async(
        self,
        request: main_models.ListProvisionConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/provision-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provision_configs(
        self,
        request: main_models.ListProvisionConfigsRequest,
    ) -> main_models.ListProvisionConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_provision_configs_with_options(request, headers, runtime)

    async def list_provision_configs_async(
        self,
        request: main_models.ListProvisionConfigsRequest,
    ) -> main_models.ListProvisionConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_provision_configs_with_options_async(request, headers, runtime)

    def list_scaling_configs_with_options(
        self,
        request: main_models.ListScalingConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScalingConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScalingConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/scaling-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScalingConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scaling_configs_with_options_async(
        self,
        request: main_models.ListScalingConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScalingConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScalingConfigs',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/scaling-configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScalingConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scaling_configs(
        self,
        request: main_models.ListScalingConfigsRequest,
    ) -> main_models.ListScalingConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_scaling_configs_with_options(request, headers, runtime)

    async def list_scaling_configs_async(
        self,
        request: main_models.ListScalingConfigsRequest,
    ) -> main_models.ListScalingConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_scaling_configs_with_options_async(request, headers, runtime)

    def list_sessions_with_options(
        self,
        function_name: str,
        request: main_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.session_status):
            query['sessionStatus'] = request.session_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sessions_with_options_async(
        self,
        function_name: str,
        request: main_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.session_status):
            query['sessionStatus'] = request.session_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessions',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sessions(
        self,
        function_name: str,
        request: main_models.ListSessionsRequest,
    ) -> main_models.ListSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sessions_with_options(function_name, request, headers, runtime)

    async def list_sessions_async(
        self,
        function_name: str,
        request: main_models.ListSessionsRequest,
    ) -> main_models.ListSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sessions_with_options_async(function_name, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/tags-v2',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/tags-v2',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_triggers_with_options(
        self,
        function_name: str,
        request: main_models.ListTriggersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTriggersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTriggers',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        function_name: str,
        request: main_models.ListTriggersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTriggersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTriggers',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_triggers(
        self,
        function_name: str,
        request: main_models.ListTriggersRequest,
    ) -> main_models.ListTriggersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_triggers_with_options(function_name, request, headers, runtime)

    async def list_triggers_async(
        self,
        function_name: str,
        request: main_models.ListTriggersRequest,
    ) -> main_models.ListTriggersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_triggers_with_options_async(function_name, request, headers, runtime)

    def list_vpc_bindings_with_options(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcBindingsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListVpcBindings',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/vpc-bindings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_bindings_with_options_async(
        self,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcBindingsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListVpcBindings',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/vpc-bindings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_bindings(
        self,
        function_name: str,
    ) -> main_models.ListVpcBindingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vpc_bindings_with_options(function_name, headers, runtime)

    async def list_vpc_bindings_async(
        self,
        function_name: str,
    ) -> main_models.ListVpcBindingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vpc_bindings_with_options_async(function_name, headers, runtime)

    def publish_function_version_with_options(
        self,
        function_name: str,
        request: main_models.PublishFunctionVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishFunctionVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PublishFunctionVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_function_version_with_options_async(
        self,
        function_name: str,
        request: main_models.PublishFunctionVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishFunctionVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PublishFunctionVersion',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFunctionVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_function_version(
        self,
        function_name: str,
        request: main_models.PublishFunctionVersionRequest,
    ) -> main_models.PublishFunctionVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_function_version_with_options(function_name, request, headers, runtime)

    async def publish_function_version_async(
        self,
        function_name: str,
        request: main_models.PublishFunctionVersionRequest,
    ) -> main_models.PublishFunctionVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_function_version_with_options_async(function_name, request, headers, runtime)

    def put_async_invoke_config_with_options(
        self,
        function_name: str,
        request: main_models.PutAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutAsyncInvokeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutAsyncInvokeConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-invoke-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_async_invoke_config_with_options_async(
        self,
        function_name: str,
        request: main_models.PutAsyncInvokeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutAsyncInvokeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutAsyncInvokeConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-invoke-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutAsyncInvokeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_async_invoke_config(
        self,
        function_name: str,
        request: main_models.PutAsyncInvokeConfigRequest,
    ) -> main_models.PutAsyncInvokeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_async_invoke_config_with_options(function_name, request, headers, runtime)

    async def put_async_invoke_config_async(
        self,
        function_name: str,
        request: main_models.PutAsyncInvokeConfigRequest,
    ) -> main_models.PutAsyncInvokeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_async_invoke_config_with_options_async(function_name, request, headers, runtime)

    def put_concurrency_config_with_options(
        self,
        function_name: str,
        request: main_models.PutConcurrencyConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutConcurrencyConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutConcurrencyConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/concurrency',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_concurrency_config_with_options_async(
        self,
        function_name: str,
        request: main_models.PutConcurrencyConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutConcurrencyConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutConcurrencyConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/concurrency',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutConcurrencyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_concurrency_config(
        self,
        function_name: str,
        request: main_models.PutConcurrencyConfigRequest,
    ) -> main_models.PutConcurrencyConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_concurrency_config_with_options(function_name, request, headers, runtime)

    async def put_concurrency_config_async(
        self,
        function_name: str,
        request: main_models.PutConcurrencyConfigRequest,
    ) -> main_models.PutConcurrencyConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_concurrency_config_with_options_async(function_name, request, headers, runtime)

    def put_layer_aclwith_options(
        self,
        layer_name: str,
        request: main_models.PutLayerACLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutLayerACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl):
            query['acl'] = request.acl
        if not DaraCore.is_null(request.public):
            query['public'] = request.public
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutLayerACL',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/acl',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutLayerACLResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_layer_aclwith_options_async(
        self,
        layer_name: str,
        request: main_models.PutLayerACLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutLayerACLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl):
            query['acl'] = request.acl
        if not DaraCore.is_null(request.public):
            query['public'] = request.public
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutLayerACL',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/layers/{DaraURL.percent_encode(layer_name)}/acl',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutLayerACLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_layer_acl(
        self,
        layer_name: str,
        request: main_models.PutLayerACLRequest,
    ) -> main_models.PutLayerACLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_layer_aclwith_options(layer_name, request, headers, runtime)

    async def put_layer_acl_async(
        self,
        layer_name: str,
        request: main_models.PutLayerACLRequest,
    ) -> main_models.PutLayerACLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_layer_aclwith_options_async(layer_name, request, headers, runtime)

    def put_provision_config_with_options(
        self,
        function_name: str,
        request: main_models.PutProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutProvisionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutProvisionConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/provision-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_provision_config_with_options_async(
        self,
        function_name: str,
        request: main_models.PutProvisionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutProvisionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutProvisionConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/provision-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutProvisionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_provision_config(
        self,
        function_name: str,
        request: main_models.PutProvisionConfigRequest,
    ) -> main_models.PutProvisionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_provision_config_with_options(function_name, request, headers, runtime)

    async def put_provision_config_async(
        self,
        function_name: str,
        request: main_models.PutProvisionConfigRequest,
    ) -> main_models.PutProvisionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_provision_config_with_options_async(function_name, request, headers, runtime)

    def put_scaling_config_with_options(
        self,
        function_name: str,
        request: main_models.PutScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutScalingConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/scaling-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_scaling_config_with_options_async(
        self,
        function_name: str,
        request: main_models.PutScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutScalingConfig',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/scaling-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_scaling_config(
        self,
        function_name: str,
        request: main_models.PutScalingConfigRequest,
    ) -> main_models.PutScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_scaling_config_with_options(function_name, request, headers, runtime)

    async def put_scaling_config_async(
        self,
        function_name: str,
        request: main_models.PutScalingConfigRequest,
    ) -> main_models.PutScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_scaling_config_with_options_async(function_name, request, headers, runtime)

    def stop_async_task_with_options(
        self,
        function_name: str,
        task_id: str,
        request: main_models.StopAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAsyncTask',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-tasks/{DaraURL.percent_encode(task_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_async_task_with_options_async(
        self,
        function_name: str,
        task_id: str,
        request: main_models.StopAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAsyncTask',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/async-tasks/{DaraURL.percent_encode(task_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_async_task(
        self,
        function_name: str,
        task_id: str,
        request: main_models.StopAsyncTaskRequest,
    ) -> main_models.StopAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_async_task_with_options(function_name, task_id, request, headers, runtime)

    async def stop_async_task_async(
        self,
        function_name: str,
        task_id: str,
        request: main_models.StopAsyncTaskRequest,
    ) -> main_models.StopAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_async_task_with_options_async(function_name, task_id, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/tags-v2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/tags-v2',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
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
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/tags-v2',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/tags-v2',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
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
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_alias_with_options(
        self,
        function_name: str,
        alias_name: str,
        request: main_models.UpdateAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAliasResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases/{DaraURL.percent_encode(alias_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        function_name: str,
        alias_name: str,
        request: main_models.UpdateAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAliasResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlias',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/aliases/{DaraURL.percent_encode(alias_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alias(
        self,
        function_name: str,
        alias_name: str,
        request: main_models.UpdateAliasRequest,
    ) -> main_models.UpdateAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_alias_with_options(function_name, alias_name, request, headers, runtime)

    async def update_alias_async(
        self,
        function_name: str,
        alias_name: str,
        request: main_models.UpdateAliasRequest,
    ) -> main_models.UpdateAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_alias_with_options_async(function_name, alias_name, request, headers, runtime)

    def update_custom_domain_with_options(
        self,
        domain_name: str,
        request: main_models.UpdateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomDomainResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: main_models.UpdateCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomDomainResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomDomain',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_domain(
        self,
        domain_name: str,
        request: main_models.UpdateCustomDomainRequest,
    ) -> main_models.UpdateCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_custom_domain_with_options(domain_name, request, headers, runtime)

    async def update_custom_domain_async(
        self,
        domain_name: str,
        request: main_models.UpdateCustomDomainRequest,
    ) -> main_models.UpdateCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def update_function_with_options(
        self,
        function_name: str,
        request: main_models.UpdateFunctionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        function_name: str,
        request: main_models.UpdateFunctionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunction',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        function_name: str,
        request: main_models.UpdateFunctionRequest,
    ) -> main_models.UpdateFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_function_with_options(function_name, request, headers, runtime)

    async def update_function_async(
        self,
        function_name: str,
        request: main_models.UpdateFunctionRequest,
    ) -> main_models.UpdateFunctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_function_with_options_async(function_name, request, headers, runtime)

    def update_session_with_options(
        self,
        function_name: str,
        session_id: str,
        request: main_models.UpdateSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_session_with_options_async(
        self,
        function_name: str,
        session_id: str,
        request: main_models.UpdateSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSession',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_session(
        self,
        function_name: str,
        session_id: str,
        request: main_models.UpdateSessionRequest,
    ) -> main_models.UpdateSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_session_with_options(function_name, session_id, request, headers, runtime)

    async def update_session_async(
        self,
        function_name: str,
        session_id: str,
        request: main_models.UpdateSessionRequest,
    ) -> main_models.UpdateSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_session_with_options_async(function_name, session_id, request, headers, runtime)

    def update_trigger_with_options(
        self,
        function_name: str,
        trigger_name: str,
        request: main_models.UpdateTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTriggerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers/{DaraURL.percent_encode(trigger_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        function_name: str,
        trigger_name: str,
        request: main_models.UpdateTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTriggerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrigger',
            version = '2023-03-30',
            protocol = 'HTTPS',
            pathname = f'/2023-03-30/functions/{DaraURL.percent_encode(function_name)}/triggers/{DaraURL.percent_encode(trigger_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trigger(
        self,
        function_name: str,
        trigger_name: str,
        request: main_models.UpdateTriggerRequest,
    ) -> main_models.UpdateTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_trigger_with_options(function_name, trigger_name, request, headers, runtime)

    async def update_trigger_async(
        self,
        function_name: str,
        trigger_name: str,
        request: main_models.UpdateTriggerRequest,
    ) -> main_models.UpdateTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_trigger_with_options_async(function_name, trigger_name, request, headers, runtime)
