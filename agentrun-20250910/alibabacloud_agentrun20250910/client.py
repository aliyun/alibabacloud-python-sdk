# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentrun20250910 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('agentrun', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_template_mcpwith_options(
        self,
        template_name: str,
        request: main_models.ActivateTemplateMCPRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActivateTemplateMCPResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled_tools):
            body['enabledTools'] = request.enabled_tools
        if not DaraCore.is_null(request.transport):
            body['transport'] = request.transport
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActivateTemplateMCP',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}/mcp/activate',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateTemplateMCPResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_template_mcpwith_options_async(
        self,
        template_name: str,
        request: main_models.ActivateTemplateMCPRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActivateTemplateMCPResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enabled_tools):
            body['enabledTools'] = request.enabled_tools
        if not DaraCore.is_null(request.transport):
            body['transport'] = request.transport
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActivateTemplateMCP',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}/mcp/activate',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateTemplateMCPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_template_mcp(
        self,
        template_name: str,
        request: main_models.ActivateTemplateMCPRequest,
    ) -> main_models.ActivateTemplateMCPResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.activate_template_mcpwith_options(template_name, request, headers, runtime)

    async def activate_template_mcp_async(
        self,
        template_name: str,
        request: main_models.ActivateTemplateMCPRequest,
    ) -> main_models.ActivateTemplateMCPResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.activate_template_mcpwith_options_async(template_name, request, headers, runtime)

    def create_agent_runtime_with_options(
        self,
        request: main_models.CreateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentRuntimeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_runtime_with_options_async(
        self,
        request: main_models.CreateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentRuntimeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_runtime(
        self,
        request: main_models.CreateAgentRuntimeRequest,
    ) -> main_models.CreateAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_runtime_with_options(request, headers, runtime)

    async def create_agent_runtime_async(
        self,
        request: main_models.CreateAgentRuntimeRequest,
    ) -> main_models.CreateAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_runtime_with_options_async(request, headers, runtime)

    def create_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        request: main_models.CreateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentRuntimeEndpointResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        request: main_models.CreateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentRuntimeEndpointResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        request: main_models.CreateAgentRuntimeEndpointRequest,
    ) -> main_models.CreateAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_runtime_endpoint_with_options(agent_runtime_id, request, headers, runtime)

    async def create_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        request: main_models.CreateAgentRuntimeEndpointRequest,
    ) -> main_models.CreateAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_runtime_endpoint_with_options_async(agent_runtime_id, request, headers, runtime)

    def create_browser_with_options(
        self,
        request: main_models.CreateBrowserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBrowserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBrowser',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_browser_with_options_async(
        self,
        request: main_models.CreateBrowserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBrowserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBrowser',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_browser(
        self,
        request: main_models.CreateBrowserRequest,
    ) -> main_models.CreateBrowserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_browser_with_options(request, headers, runtime)

    async def create_browser_async(
        self,
        request: main_models.CreateBrowserRequest,
    ) -> main_models.CreateBrowserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_browser_with_options_async(request, headers, runtime)

    def create_code_interpreter_with_options(
        self,
        request: main_models.CreateCodeInterpreterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCodeInterpreterResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCodeInterpreter',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCodeInterpreterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_code_interpreter_with_options_async(
        self,
        request: main_models.CreateCodeInterpreterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCodeInterpreterResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCodeInterpreter',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCodeInterpreterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_code_interpreter(
        self,
        request: main_models.CreateCodeInterpreterRequest,
    ) -> main_models.CreateCodeInterpreterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_code_interpreter_with_options(request, headers, runtime)

    async def create_code_interpreter_async(
        self,
        request: main_models.CreateCodeInterpreterRequest,
    ) -> main_models.CreateCodeInterpreterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_code_interpreter_with_options_async(request, headers, runtime)

    def create_credential_with_options(
        self,
        request: main_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_credential_with_options_async(
        self,
        request: main_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_credential(
        self,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_credential_with_options(request, headers, runtime)

    async def create_credential_async(
        self,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_credential_with_options_async(request, headers, runtime)

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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains',
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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains',
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

    def create_knowledge_base_with_options(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_base_with_options_async(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKnowledgeBaseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_knowledge_base(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
    ) -> main_models.CreateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_knowledge_base_with_options(request, headers, runtime)

    async def create_knowledge_base_async(
        self,
        request: main_models.CreateKnowledgeBaseRequest,
    ) -> main_models.CreateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_knowledge_base_with_options_async(request, headers, runtime)

    def create_memory_collection_with_options(
        self,
        request: main_models.CreateMemoryCollectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryCollectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_collection_with_options_async(
        self,
        request: main_models.CreateMemoryCollectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryCollectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory_collection(
        self,
        request: main_models.CreateMemoryCollectionRequest,
    ) -> main_models.CreateMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_memory_collection_with_options(request, headers, runtime)

    async def create_memory_collection_async(
        self,
        request: main_models.CreateMemoryCollectionRequest,
    ) -> main_models.CreateMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_memory_collection_with_options_async(request, headers, runtime)

    def create_model_proxy_with_options(
        self,
        request: main_models.CreateModelProxyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelProxyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_proxy_with_options_async(
        self,
        request: main_models.CreateModelProxyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelProxyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_proxy(
        self,
        request: main_models.CreateModelProxyRequest,
    ) -> main_models.CreateModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_proxy_with_options(request, headers, runtime)

    async def create_model_proxy_async(
        self,
        request: main_models.CreateModelProxyRequest,
    ) -> main_models.CreateModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_proxy_with_options_async(request, headers, runtime)

    def create_model_service_with_options(
        self,
        request: main_models.CreateModelServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_service_with_options_async(
        self,
        request: main_models.CreateModelServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_service(
        self,
        request: main_models.CreateModelServiceRequest,
    ) -> main_models.CreateModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_service_with_options(request, headers, runtime)

    async def create_model_service_async(
        self,
        request: main_models.CreateModelServiceRequest,
    ) -> main_models.CreateModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_service_with_options_async(request, headers, runtime)

    def create_sandbox_with_options(
        self,
        request: main_models.CreateSandboxRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSandboxResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sandbox_with_options_async(
        self,
        request: main_models.CreateSandboxRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSandboxResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sandbox(
        self,
        request: main_models.CreateSandboxRequest,
    ) -> main_models.CreateSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sandbox_with_options(request, headers, runtime)

    async def create_sandbox_async(
        self,
        request: main_models.CreateSandboxRequest,
    ) -> main_models.CreateSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sandbox_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def delete_agent_runtime_with_options(
        self,
        agent_runtime_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentRuntimeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_runtime_with_options_async(
        self,
        agent_runtime_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentRuntimeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_runtime(
        self,
        agent_runtime_id: str,
    ) -> main_models.DeleteAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_runtime_with_options(agent_runtime_id, headers, runtime)

    async def delete_agent_runtime_async(
        self,
        agent_runtime_id: str,
    ) -> main_models.DeleteAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_runtime_with_options_async(agent_runtime_id, headers, runtime)

    def delete_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentRuntimeEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints/{DaraURL.percent_encode(agent_runtime_endpoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentRuntimeEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints/{DaraURL.percent_encode(agent_runtime_endpoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> main_models.DeleteAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_runtime_endpoint_with_options(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    async def delete_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> main_models.DeleteAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_runtime_endpoint_with_options_async(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    def delete_browser_with_options(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBrowserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteBrowser',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers/{DaraURL.percent_encode(browser_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_browser_with_options_async(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBrowserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteBrowser',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers/{DaraURL.percent_encode(browser_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_browser(
        self,
        browser_id: str,
    ) -> main_models.DeleteBrowserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_browser_with_options(browser_id, headers, runtime)

    async def delete_browser_async(
        self,
        browser_id: str,
    ) -> main_models.DeleteBrowserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_browser_with_options_async(browser_id, headers, runtime)

    def delete_code_interpreter_with_options(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCodeInterpreterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCodeInterpreter',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters/{DaraURL.percent_encode(code_interpreter_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCodeInterpreterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_code_interpreter_with_options_async(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCodeInterpreterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCodeInterpreter',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters/{DaraURL.percent_encode(code_interpreter_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCodeInterpreterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_code_interpreter(
        self,
        code_interpreter_id: str,
    ) -> main_models.DeleteCodeInterpreterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_code_interpreter_with_options(code_interpreter_id, headers, runtime)

    async def delete_code_interpreter_async(
        self,
        code_interpreter_id: str,
    ) -> main_models.DeleteCodeInterpreterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_code_interpreter_with_options_async(code_interpreter_id, headers, runtime)

    def delete_credential_with_options(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials/{DaraURL.percent_encode(credential_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_credential_with_options_async(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials/{DaraURL.percent_encode(credential_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_credential(
        self,
        credential_name: str,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_credential_with_options(credential_name, headers, runtime)

    async def delete_credential_async(
        self,
        credential_name: str,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_credential_with_options_async(credential_name, headers, runtime)

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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
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

    def delete_knowledge_base_with_options(
        self,
        knowledge_base_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases/{DaraURL.percent_encode(knowledge_base_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_knowledge_base_with_options_async(
        self,
        knowledge_base_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases/{DaraURL.percent_encode(knowledge_base_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_knowledge_base(
        self,
        knowledge_base_name: str,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_knowledge_base_with_options(knowledge_base_name, headers, runtime)

    async def delete_knowledge_base_async(
        self,
        knowledge_base_name: str,
    ) -> main_models.DeleteKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_knowledge_base_with_options_async(knowledge_base_name, headers, runtime)

    def delete_memory_collection_with_options(
        self,
        memory_collection_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryCollectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections/{DaraURL.percent_encode(memory_collection_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_collection_with_options_async(
        self,
        memory_collection_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryCollectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections/{DaraURL.percent_encode(memory_collection_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory_collection(
        self,
        memory_collection_name: str,
    ) -> main_models.DeleteMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_memory_collection_with_options(memory_collection_name, headers, runtime)

    async def delete_memory_collection_async(
        self,
        memory_collection_name: str,
    ) -> main_models.DeleteMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_memory_collection_with_options_async(memory_collection_name, headers, runtime)

    def delete_model_proxy_with_options(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelProxyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies/{DaraURL.percent_encode(model_proxy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_proxy_with_options_async(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelProxyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies/{DaraURL.percent_encode(model_proxy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_proxy(
        self,
        model_proxy_name: str,
    ) -> main_models.DeleteModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_proxy_with_options(model_proxy_name, headers, runtime)

    async def delete_model_proxy_async(
        self,
        model_proxy_name: str,
    ) -> main_models.DeleteModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_proxy_with_options_async(model_proxy_name, headers, runtime)

    def delete_model_service_with_options(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services/{DaraURL.percent_encode(model_service_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_service_with_options_async(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services/{DaraURL.percent_encode(model_service_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_service(
        self,
        model_service_name: str,
    ) -> main_models.DeleteModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_service_with_options(model_service_name, headers, runtime)

    async def delete_model_service_async(
        self,
        model_service_name: str,
    ) -> main_models.DeleteModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_service_with_options_async(model_service_name, headers, runtime)

    def delete_sandbox_with_options(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSandboxResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes/{DaraURL.percent_encode(sandbox_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sandbox_with_options_async(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSandboxResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes/{DaraURL.percent_encode(sandbox_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sandbox(
        self,
        sandbox_id: str,
    ) -> main_models.DeleteSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_sandbox_with_options(sandbox_id, headers, runtime)

    async def delete_sandbox_async(
        self,
        sandbox_id: str,
    ) -> main_models.DeleteSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_sandbox_with_options_async(sandbox_id, headers, runtime)

    def delete_template_with_options(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        template_name: str,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_name, headers, runtime)

    async def delete_template_async(
        self,
        template_name: str,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(template_name, headers, runtime)

    def get_access_token_with_options(
        self,
        request: main_models.GetAccessTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessToken',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/accessToken',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_token_with_options_async(
        self,
        request: main_models.GetAccessTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessToken',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/accessToken',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_token(
        self,
        request: main_models.GetAccessTokenRequest,
    ) -> main_models.GetAccessTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_access_token_with_options(request, headers, runtime)

    async def get_access_token_async(
        self,
        request: main_models.GetAccessTokenRequest,
    ) -> main_models.GetAccessTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_access_token_with_options_async(request, headers, runtime)

    def get_agent_runtime_with_options(
        self,
        agent_runtime_id: str,
        request: main_models.GetAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentRuntimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_runtime_version):
            query['agentRuntimeVersion'] = request.agent_runtime_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_runtime_with_options_async(
        self,
        agent_runtime_id: str,
        request: main_models.GetAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentRuntimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_runtime_version):
            query['agentRuntimeVersion'] = request.agent_runtime_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_runtime(
        self,
        agent_runtime_id: str,
        request: main_models.GetAgentRuntimeRequest,
    ) -> main_models.GetAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_runtime_with_options(agent_runtime_id, request, headers, runtime)

    async def get_agent_runtime_async(
        self,
        agent_runtime_id: str,
        request: main_models.GetAgentRuntimeRequest,
    ) -> main_models.GetAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_runtime_with_options_async(agent_runtime_id, request, headers, runtime)

    def get_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentRuntimeEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints/{DaraURL.percent_encode(agent_runtime_endpoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentRuntimeEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints/{DaraURL.percent_encode(agent_runtime_endpoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> main_models.GetAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_runtime_endpoint_with_options(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    async def get_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> main_models.GetAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_runtime_endpoint_with_options_async(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    def get_browser_with_options(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBrowserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBrowser',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers/{DaraURL.percent_encode(browser_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_browser_with_options_async(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBrowserResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBrowser',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers/{DaraURL.percent_encode(browser_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_browser(
        self,
        browser_id: str,
    ) -> main_models.GetBrowserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_browser_with_options(browser_id, headers, runtime)

    async def get_browser_async(
        self,
        browser_id: str,
    ) -> main_models.GetBrowserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_browser_with_options_async(browser_id, headers, runtime)

    def get_code_interpreter_with_options(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCodeInterpreterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCodeInterpreter',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters/{DaraURL.percent_encode(code_interpreter_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCodeInterpreterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_interpreter_with_options_async(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCodeInterpreterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCodeInterpreter',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters/{DaraURL.percent_encode(code_interpreter_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCodeInterpreterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_interpreter(
        self,
        code_interpreter_id: str,
    ) -> main_models.GetCodeInterpreterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_code_interpreter_with_options(code_interpreter_id, headers, runtime)

    async def get_code_interpreter_async(
        self,
        code_interpreter_id: str,
    ) -> main_models.GetCodeInterpreterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_code_interpreter_with_options_async(code_interpreter_id, headers, runtime)

    def get_credential_with_options(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials/{DaraURL.percent_encode(credential_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_with_options_async(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials/{DaraURL.percent_encode(credential_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential(
        self,
        credential_name: str,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_credential_with_options(credential_name, headers, runtime)

    async def get_credential_async(
        self,
        credential_name: str,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_credential_with_options_async(credential_name, headers, runtime)

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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains/{DaraURL.percent_encode(domain_name)}',
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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains/{DaraURL.percent_encode(domain_name)}',
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

    def get_knowledge_base_with_options(
        self,
        knowledge_base_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases/{DaraURL.percent_encode(knowledge_base_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_knowledge_base_with_options_async(
        self,
        knowledge_base_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKnowledgeBaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases/{DaraURL.percent_encode(knowledge_base_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_knowledge_base(
        self,
        knowledge_base_name: str,
    ) -> main_models.GetKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_knowledge_base_with_options(knowledge_base_name, headers, runtime)

    async def get_knowledge_base_async(
        self,
        knowledge_base_name: str,
    ) -> main_models.GetKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_knowledge_base_with_options_async(knowledge_base_name, headers, runtime)

    def get_memory_collection_with_options(
        self,
        memory_collection_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemoryCollectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections/{DaraURL.percent_encode(memory_collection_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemoryCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_collection_with_options_async(
        self,
        memory_collection_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemoryCollectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections/{DaraURL.percent_encode(memory_collection_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemoryCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory_collection(
        self,
        memory_collection_name: str,
    ) -> main_models.GetMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_memory_collection_with_options(memory_collection_name, headers, runtime)

    async def get_memory_collection_async(
        self,
        memory_collection_name: str,
    ) -> main_models.GetMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_memory_collection_with_options_async(memory_collection_name, headers, runtime)

    def get_model_proxy_with_options(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelProxyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies/{DaraURL.percent_encode(model_proxy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_proxy_with_options_async(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelProxyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies/{DaraURL.percent_encode(model_proxy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_proxy(
        self,
        model_proxy_name: str,
    ) -> main_models.GetModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_proxy_with_options(model_proxy_name, headers, runtime)

    async def get_model_proxy_async(
        self,
        model_proxy_name: str,
    ) -> main_models.GetModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_proxy_with_options_async(model_proxy_name, headers, runtime)

    def get_model_service_with_options(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services/{DaraURL.percent_encode(model_service_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_service_with_options_async(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services/{DaraURL.percent_encode(model_service_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_service(
        self,
        model_service_name: str,
    ) -> main_models.GetModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_service_with_options(model_service_name, headers, runtime)

    async def get_model_service_async(
        self,
        model_service_name: str,
    ) -> main_models.GetModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_service_with_options_async(model_service_name, headers, runtime)

    def get_sandbox_with_options(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSandboxResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes/{DaraURL.percent_encode(sandbox_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sandbox_with_options_async(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSandboxResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes/{DaraURL.percent_encode(sandbox_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sandbox(
        self,
        sandbox_id: str,
    ) -> main_models.GetSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sandbox_with_options(sandbox_id, headers, runtime)

    async def get_sandbox_async(
        self,
        sandbox_id: str,
    ) -> main_models.GetSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sandbox_with_options_async(sandbox_id, headers, runtime)

    def get_template_with_options(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        template_name: str,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_template_with_options(template_name, headers, runtime)

    async def get_template_async(
        self,
        template_name: str,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(template_name, headers, runtime)

    def list_agent_runtime_endpoints_with_options(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentRuntimeEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_name):
            query['endpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['searchMode'] = request.search_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentRuntimeEndpoints',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentRuntimeEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_runtime_endpoints_with_options_async(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentRuntimeEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_name):
            query['endpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['searchMode'] = request.search_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentRuntimeEndpoints',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentRuntimeEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_runtime_endpoints(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeEndpointsRequest,
    ) -> main_models.ListAgentRuntimeEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_runtime_endpoints_with_options(agent_runtime_id, request, headers, runtime)

    async def list_agent_runtime_endpoints_async(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeEndpointsRequest,
    ) -> main_models.ListAgentRuntimeEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_runtime_endpoints_with_options_async(agent_runtime_id, request, headers, runtime)

    def list_agent_runtime_versions_with_options(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentRuntimeVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentRuntimeVersions',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentRuntimeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_runtime_versions_with_options_async(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentRuntimeVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentRuntimeVersions',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentRuntimeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_runtime_versions(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeVersionsRequest,
    ) -> main_models.ListAgentRuntimeVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_runtime_versions_with_options(agent_runtime_id, request, headers, runtime)

    async def list_agent_runtime_versions_async(
        self,
        agent_runtime_id: str,
        request: main_models.ListAgentRuntimeVersionsRequest,
    ) -> main_models.ListAgentRuntimeVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_runtime_versions_with_options_async(agent_runtime_id, request, headers, runtime)

    def list_agent_runtimes_with_options(
        self,
        request: main_models.ListAgentRuntimesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentRuntimesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_runtime_name):
            query['agentRuntimeName'] = request.agent_runtime_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['searchMode'] = request.search_mode
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentRuntimes',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentRuntimesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_runtimes_with_options_async(
        self,
        request: main_models.ListAgentRuntimesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentRuntimesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_runtime_name):
            query['agentRuntimeName'] = request.agent_runtime_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.search_mode):
            query['searchMode'] = request.search_mode
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentRuntimes',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentRuntimesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_runtimes(
        self,
        request: main_models.ListAgentRuntimesRequest,
    ) -> main_models.ListAgentRuntimesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_runtimes_with_options(request, headers, runtime)

    async def list_agent_runtimes_async(
        self,
        request: main_models.ListAgentRuntimesRequest,
    ) -> main_models.ListAgentRuntimesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_runtimes_with_options_async(request, headers, runtime)

    def list_browsers_with_options(
        self,
        request: main_models.ListBrowsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBrowsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.browser_name):
            query['browserName'] = request.browser_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBrowsers',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBrowsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_browsers_with_options_async(
        self,
        request: main_models.ListBrowsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBrowsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.browser_name):
            query['browserName'] = request.browser_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBrowsers',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/browsers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBrowsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_browsers(
        self,
        request: main_models.ListBrowsersRequest,
    ) -> main_models.ListBrowsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_browsers_with_options(request, headers, runtime)

    async def list_browsers_async(
        self,
        request: main_models.ListBrowsersRequest,
    ) -> main_models.ListBrowsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_browsers_with_options_async(request, headers, runtime)

    def list_code_interpreters_with_options(
        self,
        request: main_models.ListCodeInterpretersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCodeInterpretersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code_interpreter_name):
            query['codeInterpreterName'] = request.code_interpreter_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCodeInterpreters',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCodeInterpretersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_code_interpreters_with_options_async(
        self,
        request: main_models.ListCodeInterpretersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCodeInterpretersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code_interpreter_name):
            query['codeInterpreterName'] = request.code_interpreter_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCodeInterpreters',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/code-interpreters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCodeInterpretersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_code_interpreters(
        self,
        request: main_models.ListCodeInterpretersRequest,
    ) -> main_models.ListCodeInterpretersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_code_interpreters_with_options(request, headers, runtime)

    async def list_code_interpreters_async(
        self,
        request: main_models.ListCodeInterpretersRequest,
    ) -> main_models.ListCodeInterpretersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_code_interpreters_with_options_async(request, headers, runtime)

    def list_credentials_with_options(
        self,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_auth_type):
            query['credentialAuthType'] = request.credential_auth_type
        if not DaraCore.is_null(request.credential_name):
            query['credentialName'] = request.credential_name
        if not DaraCore.is_null(request.credential_source_type):
            query['credentialSourceType'] = request.credential_source_type
        if not DaraCore.is_null(request.enabled):
            query['enabled'] = request.enabled
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_credentials_with_options_async(
        self,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_auth_type):
            query['credentialAuthType'] = request.credential_auth_type
        if not DaraCore.is_null(request.credential_name):
            query['credentialName'] = request.credential_name
        if not DaraCore.is_null(request.credential_source_type):
            query['credentialSourceType'] = request.credential_source_type
        if not DaraCore.is_null(request.enabled):
            query['enabled'] = request.enabled
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_credentials(
        self,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_credentials_with_options(request, headers, runtime)

    async def list_credentials_async(
        self,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_credentials_with_options_async(request, headers, runtime)

    def list_custom_domains_with_options(
        self,
        request: main_models.ListCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomDomains',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains',
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
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomDomains',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains',
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

    def list_knowledge_bases_with_options(
        self,
        request: main_models.ListKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBases',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_bases_with_options_async(
        self,
        request: main_models.ListKnowledgeBasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBases',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_bases(
        self,
        request: main_models.ListKnowledgeBasesRequest,
    ) -> main_models.ListKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_knowledge_bases_with_options(request, headers, runtime)

    async def list_knowledge_bases_async(
        self,
        request: main_models.ListKnowledgeBasesRequest,
    ) -> main_models.ListKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_knowledge_bases_with_options_async(request, headers, runtime)

    def list_memory_collections_with_options(
        self,
        request: main_models.ListMemoryCollectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMemoryCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.memory_collection_name):
            query['memoryCollectionName'] = request.memory_collection_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMemoryCollections',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMemoryCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memory_collections_with_options_async(
        self,
        request: main_models.ListMemoryCollectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMemoryCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.memory_collection_name):
            query['memoryCollectionName'] = request.memory_collection_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMemoryCollections',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMemoryCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memory_collections(
        self,
        request: main_models.ListMemoryCollectionsRequest,
    ) -> main_models.ListMemoryCollectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_memory_collections_with_options(request, headers, runtime)

    async def list_memory_collections_async(
        self,
        request: main_models.ListMemoryCollectionsRequest,
    ) -> main_models.ListMemoryCollectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_memory_collections_with_options_async(request, headers, runtime)

    def list_model_providers_with_options(
        self,
        request: main_models.ListModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_name):
            query['modelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelProviders',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_providers_with_options_async(
        self,
        request: main_models.ListModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_name):
            query['modelName'] = request.model_name
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelProviders',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_providers(
        self,
        request: main_models.ListModelProvidersRequest,
    ) -> main_models.ListModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_providers_with_options(request, headers, runtime)

    async def list_model_providers_async(
        self,
        request: main_models.ListModelProvidersRequest,
    ) -> main_models.ListModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_providers_with_options_async(request, headers, runtime)

    def list_model_proxies_with_options(
        self,
        request: main_models.ListModelProxiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelProxiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_mode):
            query['proxyMode'] = request.proxy_mode
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelProxies',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelProxiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_proxies_with_options_async(
        self,
        request: main_models.ListModelProxiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelProxiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_mode):
            query['proxyMode'] = request.proxy_mode
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelProxies',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelProxiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_proxies(
        self,
        request: main_models.ListModelProxiesRequest,
    ) -> main_models.ListModelProxiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_proxies_with_options(request, headers, runtime)

    async def list_model_proxies_async(
        self,
        request: main_models.ListModelProxiesRequest,
    ) -> main_models.ListModelProxiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_proxies_with_options_async(request, headers, runtime)

    def list_model_services_with_options(
        self,
        request: main_models.ListModelServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        if not DaraCore.is_null(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelServices',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_services_with_options_async(
        self,
        request: main_models.ListModelServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        if not DaraCore.is_null(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelServices',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_services(
        self,
        request: main_models.ListModelServicesRequest,
    ) -> main_models.ListModelServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_services_with_options(request, headers, runtime)

    async def list_model_services_async(
        self,
        request: main_models.ListModelServicesRequest,
    ) -> main_models.ListModelServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_services_with_options_async(request, headers, runtime)

    def list_sandboxes_with_options(
        self,
        request: main_models.ListSandboxesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSandboxesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSandboxes',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSandboxesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sandboxes_with_options_async(
        self,
        request: main_models.ListSandboxesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSandboxesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSandboxes',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSandboxesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sandboxes(
        self,
        request: main_models.ListSandboxesRequest,
    ) -> main_models.ListSandboxesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sandboxes_with_options(request, headers, runtime)

    async def list_sandboxes_async(
        self,
        request: main_models.ListSandboxesRequest,
    ) -> main_models.ListSandboxesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sandboxes_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: main_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: main_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def publish_runtime_version_with_options(
        self,
        agent_runtime_id: str,
        request: main_models.PublishRuntimeVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishRuntimeVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRuntimeVersion',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRuntimeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_runtime_version_with_options_async(
        self,
        agent_runtime_id: str,
        request: main_models.PublishRuntimeVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishRuntimeVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRuntimeVersion',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRuntimeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_runtime_version(
        self,
        agent_runtime_id: str,
        request: main_models.PublishRuntimeVersionRequest,
    ) -> main_models.PublishRuntimeVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_runtime_version_with_options(agent_runtime_id, request, headers, runtime)

    async def publish_runtime_version_async(
        self,
        agent_runtime_id: str,
        request: main_models.PublishRuntimeVersionRequest,
    ) -> main_models.PublishRuntimeVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_runtime_version_with_options_async(agent_runtime_id, request, headers, runtime)

    def stop_sandbox_with_options(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSandboxResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes/{DaraURL.percent_encode(sandbox_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_sandbox_with_options_async(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSandboxResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopSandbox',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/sandboxes/{DaraURL.percent_encode(sandbox_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_sandbox(
        self,
        sandbox_id: str,
    ) -> main_models.StopSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_sandbox_with_options(sandbox_id, headers, runtime)

    async def stop_sandbox_async(
        self,
        sandbox_id: str,
    ) -> main_models.StopSandboxResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_sandbox_with_options_async(sandbox_id, headers, runtime)

    def stop_template_mcpwith_options(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTemplateMCPResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopTemplateMCP',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}/mcp/stop',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTemplateMCPResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_template_mcpwith_options_async(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTemplateMCPResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopTemplateMCP',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}/mcp/stop',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTemplateMCPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_template_mcp(
        self,
        template_name: str,
    ) -> main_models.StopTemplateMCPResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_template_mcpwith_options(template_name, headers, runtime)

    async def stop_template_mcp_async(
        self,
        template_name: str,
    ) -> main_models.StopTemplateMCPResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_template_mcpwith_options_async(template_name, headers, runtime)

    def update_agent_runtime_with_options(
        self,
        agent_runtime_id: str,
        request: main_models.UpdateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentRuntimeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_runtime_with_options_async(
        self,
        agent_runtime_id: str,
        request: main_models.UpdateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentRuntimeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentRuntime',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_runtime(
        self,
        agent_runtime_id: str,
        request: main_models.UpdateAgentRuntimeRequest,
    ) -> main_models.UpdateAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_runtime_with_options(agent_runtime_id, request, headers, runtime)

    async def update_agent_runtime_async(
        self,
        agent_runtime_id: str,
        request: main_models.UpdateAgentRuntimeRequest,
    ) -> main_models.UpdateAgentRuntimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_runtime_with_options_async(agent_runtime_id, request, headers, runtime)

    def update_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: main_models.UpdateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentRuntimeEndpointResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints/{DaraURL.percent_encode(agent_runtime_endpoint_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: main_models.UpdateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentRuntimeEndpointResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentRuntimeEndpoint',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/runtimes/{DaraURL.percent_encode(agent_runtime_id)}/endpoints/{DaraURL.percent_encode(agent_runtime_endpoint_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: main_models.UpdateAgentRuntimeEndpointRequest,
    ) -> main_models.UpdateAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_runtime_endpoint_with_options(agent_runtime_id, agent_runtime_endpoint_id, request, headers, runtime)

    async def update_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: main_models.UpdateAgentRuntimeEndpointRequest,
    ) -> main_models.UpdateAgentRuntimeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_runtime_endpoint_with_options_async(agent_runtime_id, agent_runtime_endpoint_id, request, headers, runtime)

    def update_credential_with_options(
        self,
        credential_name: str,
        request: main_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials/{DaraURL.percent_encode(credential_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credential_with_options_async(
        self,
        credential_name: str,
        request: main_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/credentials/{DaraURL.percent_encode(credential_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credential(
        self,
        credential_name: str,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_credential_with_options(credential_name, request, headers, runtime)

    async def update_credential_async(
        self,
        credential_name: str,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_credential_with_options_async(credential_name, request, headers, runtime)

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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains/{DaraURL.percent_encode(domain_name)}',
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
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/custom-domains/{DaraURL.percent_encode(domain_name)}',
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

    def update_knowledge_base_with_options(
        self,
        knowledge_base_name: str,
        request: main_models.UpdateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases/{DaraURL.percent_encode(knowledge_base_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_with_options_async(
        self,
        knowledge_base_name: str,
        request: main_models.UpdateKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBase',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/knowledgebases/{DaraURL.percent_encode(knowledge_base_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base(
        self,
        knowledge_base_name: str,
        request: main_models.UpdateKnowledgeBaseRequest,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_knowledge_base_with_options(knowledge_base_name, request, headers, runtime)

    async def update_knowledge_base_async(
        self,
        knowledge_base_name: str,
        request: main_models.UpdateKnowledgeBaseRequest,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_knowledge_base_with_options_async(knowledge_base_name, request, headers, runtime)

    def update_memory_collection_with_options(
        self,
        memory_collection_name: str,
        request: main_models.UpdateMemoryCollectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryCollectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections/{DaraURL.percent_encode(memory_collection_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_collection_with_options_async(
        self,
        memory_collection_name: str,
        request: main_models.UpdateMemoryCollectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryCollectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemoryCollection',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/memory-collections/{DaraURL.percent_encode(memory_collection_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory_collection(
        self,
        memory_collection_name: str,
        request: main_models.UpdateMemoryCollectionRequest,
    ) -> main_models.UpdateMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_memory_collection_with_options(memory_collection_name, request, headers, runtime)

    async def update_memory_collection_async(
        self,
        memory_collection_name: str,
        request: main_models.UpdateMemoryCollectionRequest,
    ) -> main_models.UpdateMemoryCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_memory_collection_with_options_async(memory_collection_name, request, headers, runtime)

    def update_model_proxy_with_options(
        self,
        model_proxy_name: str,
        request: main_models.UpdateModelProxyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelProxyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies/{DaraURL.percent_encode(model_proxy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_proxy_with_options_async(
        self,
        model_proxy_name: str,
        request: main_models.UpdateModelProxyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelProxyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelProxy',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-proxies/{DaraURL.percent_encode(model_proxy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_proxy(
        self,
        model_proxy_name: str,
        request: main_models.UpdateModelProxyRequest,
    ) -> main_models.UpdateModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_proxy_with_options(model_proxy_name, request, headers, runtime)

    async def update_model_proxy_async(
        self,
        model_proxy_name: str,
        request: main_models.UpdateModelProxyRequest,
    ) -> main_models.UpdateModelProxyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_proxy_with_options_async(model_proxy_name, request, headers, runtime)

    def update_model_service_with_options(
        self,
        model_service_name: str,
        request: main_models.UpdateModelServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services/{DaraURL.percent_encode(model_service_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_service_with_options_async(
        self,
        model_service_name: str,
        request: main_models.UpdateModelServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelService',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/agents/model-services/{DaraURL.percent_encode(model_service_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_service(
        self,
        model_service_name: str,
        request: main_models.UpdateModelServiceRequest,
    ) -> main_models.UpdateModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_service_with_options(model_service_name, request, headers, runtime)

    async def update_model_service_async(
        self,
        model_service_name: str,
        request: main_models.UpdateModelServiceRequest,
    ) -> main_models.UpdateModelServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_service_with_options_async(model_service_name, request, headers, runtime)

    def update_template_with_options(
        self,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2025-09-10',
            protocol = 'HTTPS',
            pathname = f'/2025-09-10/templates/{DaraURL.percent_encode(template_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_name, request, headers, runtime)

    async def update_template_async(
        self,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(template_name, request, headers, runtime)
