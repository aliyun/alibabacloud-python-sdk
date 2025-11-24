# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_agentrun20250910 import models as agent_run_20250910_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_template_mcpwith_options(
        self,
        template_name: str,
        request: agent_run_20250910_models.ActivateTemplateMCPRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ActivateTemplateMCPResponse:
        """
        @summary 启动模板的MCP服务器
        
        @param request: ActivateTemplateMCPRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateTemplateMCPResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enabled_tools):
            body['enabledTools'] = request.enabled_tools
        if not UtilClient.is_unset(request.transport):
            body['transport'] = request.transport
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateTemplateMCP',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}/mcp/activate',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ActivateTemplateMCPResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_template_mcpwith_options_async(
        self,
        template_name: str,
        request: agent_run_20250910_models.ActivateTemplateMCPRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ActivateTemplateMCPResponse:
        """
        @summary 启动模板的MCP服务器
        
        @param request: ActivateTemplateMCPRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateTemplateMCPResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enabled_tools):
            body['enabledTools'] = request.enabled_tools
        if not UtilClient.is_unset(request.transport):
            body['transport'] = request.transport
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateTemplateMCP',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}/mcp/activate',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ActivateTemplateMCPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_template_mcp(
        self,
        template_name: str,
        request: agent_run_20250910_models.ActivateTemplateMCPRequest,
    ) -> agent_run_20250910_models.ActivateTemplateMCPResponse:
        """
        @summary 启动模板的MCP服务器
        
        @param request: ActivateTemplateMCPRequest
        @return: ActivateTemplateMCPResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.activate_template_mcpwith_options(template_name, request, headers, runtime)

    async def activate_template_mcp_async(
        self,
        template_name: str,
        request: agent_run_20250910_models.ActivateTemplateMCPRequest,
    ) -> agent_run_20250910_models.ActivateTemplateMCPResponse:
        """
        @summary 启动模板的MCP服务器
        
        @param request: ActivateTemplateMCPRequest
        @return: ActivateTemplateMCPResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.activate_template_mcpwith_options_async(template_name, request, headers, runtime)

    def create_agent_runtime_with_options(
        self,
        request: agent_run_20250910_models.CreateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateAgentRuntimeResponse:
        """
        @summary Create an agent runtime
        
        @description 创建一个新的智能体运行时实例，用于执行AI代理任务。智能体运行时是AgentRun服务的核心组件，提供代码执行、浏览器操作、内存管理等能力。
        
        @param request: CreateAgentRuntimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentRuntimeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_runtime_with_options_async(
        self,
        request: agent_run_20250910_models.CreateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateAgentRuntimeResponse:
        """
        @summary Create an agent runtime
        
        @description 创建一个新的智能体运行时实例，用于执行AI代理任务。智能体运行时是AgentRun服务的核心组件，提供代码执行、浏览器操作、内存管理等能力。
        
        @param request: CreateAgentRuntimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentRuntimeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_runtime(
        self,
        request: agent_run_20250910_models.CreateAgentRuntimeRequest,
    ) -> agent_run_20250910_models.CreateAgentRuntimeResponse:
        """
        @summary Create an agent runtime
        
        @description 创建一个新的智能体运行时实例，用于执行AI代理任务。智能体运行时是AgentRun服务的核心组件，提供代码执行、浏览器操作、内存管理等能力。
        
        @param request: CreateAgentRuntimeRequest
        @return: CreateAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_agent_runtime_with_options(request, headers, runtime)

    async def create_agent_runtime_async(
        self,
        request: agent_run_20250910_models.CreateAgentRuntimeRequest,
    ) -> agent_run_20250910_models.CreateAgentRuntimeResponse:
        """
        @summary Create an agent runtime
        
        @description 创建一个新的智能体运行时实例，用于执行AI代理任务。智能体运行时是AgentRun服务的核心组件，提供代码执行、浏览器操作、内存管理等能力。
        
        @param request: CreateAgentRuntimeRequest
        @return: CreateAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_agent_runtime_with_options_async(request, headers, runtime)

    def create_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.CreateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateAgentRuntimeEndpointResponse:
        """
        @summary 创建智能体运行时端点
        
        @description 为指定的智能体运行时创建新的端点，用于外部访问和调用。端点是智能体运行时对外提供服务的入口。
        
        @param request: CreateAgentRuntimeEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentRuntimeEndpointResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.CreateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateAgentRuntimeEndpointResponse:
        """
        @summary 创建智能体运行时端点
        
        @description 为指定的智能体运行时创建新的端点，用于外部访问和调用。端点是智能体运行时对外提供服务的入口。
        
        @param request: CreateAgentRuntimeEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentRuntimeEndpointResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.CreateAgentRuntimeEndpointRequest,
    ) -> agent_run_20250910_models.CreateAgentRuntimeEndpointResponse:
        """
        @summary 创建智能体运行时端点
        
        @description 为指定的智能体运行时创建新的端点，用于外部访问和调用。端点是智能体运行时对外提供服务的入口。
        
        @param request: CreateAgentRuntimeEndpointRequest
        @return: CreateAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_agent_runtime_endpoint_with_options(agent_runtime_id, request, headers, runtime)

    async def create_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.CreateAgentRuntimeEndpointRequest,
    ) -> agent_run_20250910_models.CreateAgentRuntimeEndpointResponse:
        """
        @summary 创建智能体运行时端点
        
        @description 为指定的智能体运行时创建新的端点，用于外部访问和调用。端点是智能体运行时对外提供服务的入口。
        
        @param request: CreateAgentRuntimeEndpointRequest
        @return: CreateAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_agent_runtime_endpoint_with_options_async(agent_runtime_id, request, headers, runtime)

    def create_browser_with_options(
        self,
        request: agent_run_20250910_models.CreateBrowserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateBrowserResponse:
        """
        @summary 创建浏览器实例
        
        @description 创建一个新的浏览器实例，用于执行网页自动化任务。浏览器实例提供网页浏览、元素操作、截图录制等功能。
        
        @param request: CreateBrowserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBrowserResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateBrowser',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_browser_with_options_async(
        self,
        request: agent_run_20250910_models.CreateBrowserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateBrowserResponse:
        """
        @summary 创建浏览器实例
        
        @description 创建一个新的浏览器实例，用于执行网页自动化任务。浏览器实例提供网页浏览、元素操作、截图录制等功能。
        
        @param request: CreateBrowserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBrowserResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateBrowser',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_browser(
        self,
        request: agent_run_20250910_models.CreateBrowserRequest,
    ) -> agent_run_20250910_models.CreateBrowserResponse:
        """
        @summary 创建浏览器实例
        
        @description 创建一个新的浏览器实例，用于执行网页自动化任务。浏览器实例提供网页浏览、元素操作、截图录制等功能。
        
        @param request: CreateBrowserRequest
        @return: CreateBrowserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_browser_with_options(request, headers, runtime)

    async def create_browser_async(
        self,
        request: agent_run_20250910_models.CreateBrowserRequest,
    ) -> agent_run_20250910_models.CreateBrowserResponse:
        """
        @summary 创建浏览器实例
        
        @description 创建一个新的浏览器实例，用于执行网页自动化任务。浏览器实例提供网页浏览、元素操作、截图录制等功能。
        
        @param request: CreateBrowserRequest
        @return: CreateBrowserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_browser_with_options_async(request, headers, runtime)

    def create_code_interpreter_with_options(
        self,
        request: agent_run_20250910_models.CreateCodeInterpreterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateCodeInterpreterResponse:
        """
        @summary 创建代码解释器
        
        @description 创建一个新的代码解释器实例，用于执行代码解释和运行任务。代码解释器提供Python代码执行、数据处理、机器学习等功能。
        
        @param request: CreateCodeInterpreterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCodeInterpreterResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCodeInterpreter',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateCodeInterpreterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_code_interpreter_with_options_async(
        self,
        request: agent_run_20250910_models.CreateCodeInterpreterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateCodeInterpreterResponse:
        """
        @summary 创建代码解释器
        
        @description 创建一个新的代码解释器实例，用于执行代码解释和运行任务。代码解释器提供Python代码执行、数据处理、机器学习等功能。
        
        @param request: CreateCodeInterpreterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCodeInterpreterResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCodeInterpreter',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateCodeInterpreterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_code_interpreter(
        self,
        request: agent_run_20250910_models.CreateCodeInterpreterRequest,
    ) -> agent_run_20250910_models.CreateCodeInterpreterResponse:
        """
        @summary 创建代码解释器
        
        @description 创建一个新的代码解释器实例，用于执行代码解释和运行任务。代码解释器提供Python代码执行、数据处理、机器学习等功能。
        
        @param request: CreateCodeInterpreterRequest
        @return: CreateCodeInterpreterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_code_interpreter_with_options(request, headers, runtime)

    async def create_code_interpreter_async(
        self,
        request: agent_run_20250910_models.CreateCodeInterpreterRequest,
    ) -> agent_run_20250910_models.CreateCodeInterpreterResponse:
        """
        @summary 创建代码解释器
        
        @description 创建一个新的代码解释器实例，用于执行代码解释和运行任务。代码解释器提供Python代码执行、数据处理、机器学习等功能。
        
        @param request: CreateCodeInterpreterRequest
        @return: CreateCodeInterpreterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_code_interpreter_with_options_async(request, headers, runtime)

    def create_credential_with_options(
        self,
        request: agent_run_20250910_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateCredentialResponse:
        """
        @summary Create a credential
        
        @param request: CreateCredentialRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCredentialResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_credential_with_options_async(
        self,
        request: agent_run_20250910_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateCredentialResponse:
        """
        @summary Create a credential
        
        @param request: CreateCredentialRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCredentialResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_credential(
        self,
        request: agent_run_20250910_models.CreateCredentialRequest,
    ) -> agent_run_20250910_models.CreateCredentialResponse:
        """
        @summary Create a credential
        
        @param request: CreateCredentialRequest
        @return: CreateCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_credential_with_options(request, headers, runtime)

    async def create_credential_async(
        self,
        request: agent_run_20250910_models.CreateCredentialRequest,
    ) -> agent_run_20250910_models.CreateCredentialResponse:
        """
        @summary Create a credential
        
        @param request: CreateCredentialRequest
        @return: CreateCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_credential_with_options_async(request, headers, runtime)

    def create_memory_with_options(
        self,
        request: agent_run_20250910_models.CreateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateMemoryResponse:
        """
        @summary create memory store
        
        @param request: CreateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.long_ttl):
            body['longTtl'] = request.long_ttl
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.short_ttl):
            body['shortTtl'] = request.short_ttl
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_with_options_async(
        self,
        request: agent_run_20250910_models.CreateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateMemoryResponse:
        """
        @summary create memory store
        
        @param request: CreateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.long_ttl):
            body['longTtl'] = request.long_ttl
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.short_ttl):
            body['shortTtl'] = request.short_ttl
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory(
        self,
        request: agent_run_20250910_models.CreateMemoryRequest,
    ) -> agent_run_20250910_models.CreateMemoryResponse:
        """
        @summary create memory store
        
        @param request: CreateMemoryRequest
        @return: CreateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_memory_with_options(request, headers, runtime)

    async def create_memory_async(
        self,
        request: agent_run_20250910_models.CreateMemoryRequest,
    ) -> agent_run_20250910_models.CreateMemoryResponse:
        """
        @summary create memory store
        
        @param request: CreateMemoryRequest
        @return: CreateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_memory_with_options_async(request, headers, runtime)

    def create_memory_event_with_options(
        self,
        memory_name: str,
        request: agent_run_20250910_models.CreateMemoryEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateMemoryEventResponse:
        """
        @summary create event
        
        @param request: CreateMemoryEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.events):
            body['events'] = request.events
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMemoryEvent',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateMemoryEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_event_with_options_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.CreateMemoryEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateMemoryEventResponse:
        """
        @summary create event
        
        @param request: CreateMemoryEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemoryEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.events):
            body['events'] = request.events
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMemoryEvent',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateMemoryEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory_event(
        self,
        memory_name: str,
        request: agent_run_20250910_models.CreateMemoryEventRequest,
    ) -> agent_run_20250910_models.CreateMemoryEventResponse:
        """
        @summary create event
        
        @param request: CreateMemoryEventRequest
        @return: CreateMemoryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_memory_event_with_options(memory_name, request, headers, runtime)

    async def create_memory_event_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.CreateMemoryEventRequest,
    ) -> agent_run_20250910_models.CreateMemoryEventResponse:
        """
        @summary create event
        
        @param request: CreateMemoryEventRequest
        @return: CreateMemoryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_memory_event_with_options_async(memory_name, request, headers, runtime)

    def create_model_proxy_with_options(
        self,
        request: agent_run_20250910_models.CreateModelProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateModelProxyResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelProxyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelProxyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_proxy_with_options_async(
        self,
        request: agent_run_20250910_models.CreateModelProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateModelProxyResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelProxyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelProxyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_proxy(
        self,
        request: agent_run_20250910_models.CreateModelProxyRequest,
    ) -> agent_run_20250910_models.CreateModelProxyResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelProxyRequest
        @return: CreateModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_proxy_with_options(request, headers, runtime)

    async def create_model_proxy_async(
        self,
        request: agent_run_20250910_models.CreateModelProxyRequest,
    ) -> agent_run_20250910_models.CreateModelProxyResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelProxyRequest
        @return: CreateModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_proxy_with_options_async(request, headers, runtime)

    def create_model_service_with_options(
        self,
        request: agent_run_20250910_models.CreateModelServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateModelServiceResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelServiceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_service_with_options_async(
        self,
        request: agent_run_20250910_models.CreateModelServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateModelServiceResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelServiceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_service(
        self,
        request: agent_run_20250910_models.CreateModelServiceRequest,
    ) -> agent_run_20250910_models.CreateModelServiceResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelServiceRequest
        @return: CreateModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_service_with_options(request, headers, runtime)

    async def create_model_service_async(
        self,
        request: agent_run_20250910_models.CreateModelServiceRequest,
    ) -> agent_run_20250910_models.CreateModelServiceResponse:
        """
        @summary 新增模型
        
        @param request: CreateModelServiceRequest
        @return: CreateModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_service_with_options_async(request, headers, runtime)

    def create_sandbox_with_options(
        self,
        request: agent_run_20250910_models.CreateSandboxRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateSandboxResponse:
        """
        @summary 创建沙箱
        
        @description 根据模板创建一个新的沙箱实例。沙箱是运行时的执行环境，可以执行代码或运行浏览器。
        
        @param request: CreateSandboxRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSandboxResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sandbox_with_options_async(
        self,
        request: agent_run_20250910_models.CreateSandboxRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateSandboxResponse:
        """
        @summary 创建沙箱
        
        @description 根据模板创建一个新的沙箱实例。沙箱是运行时的执行环境，可以执行代码或运行浏览器。
        
        @param request: CreateSandboxRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSandboxResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sandbox(
        self,
        request: agent_run_20250910_models.CreateSandboxRequest,
    ) -> agent_run_20250910_models.CreateSandboxResponse:
        """
        @summary 创建沙箱
        
        @description 根据模板创建一个新的沙箱实例。沙箱是运行时的执行环境，可以执行代码或运行浏览器。
        
        @param request: CreateSandboxRequest
        @return: CreateSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sandbox_with_options(request, headers, runtime)

    async def create_sandbox_async(
        self,
        request: agent_run_20250910_models.CreateSandboxRequest,
    ) -> agent_run_20250910_models.CreateSandboxResponse:
        """
        @summary 创建沙箱
        
        @description 根据模板创建一个新的沙箱实例。沙箱是运行时的执行环境，可以执行代码或运行浏览器。
        
        @param request: CreateSandboxRequest
        @return: CreateSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sandbox_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: agent_run_20250910_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateTemplateResponse:
        """
        @summary 创建模板
        
        @description 创建一个新的模板，用于后续创建沙箱。模板定义了沙箱的运行时环境、资源配置等。
        
        @param request: CreateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: agent_run_20250910_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.CreateTemplateResponse:
        """
        @summary 创建模板
        
        @description 创建一个新的模板，用于后续创建沙箱。模板定义了沙箱的运行时环境、资源配置等。
        
        @param request: CreateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: agent_run_20250910_models.CreateTemplateRequest,
    ) -> agent_run_20250910_models.CreateTemplateResponse:
        """
        @summary 创建模板
        
        @description 创建一个新的模板，用于后续创建沙箱。模板定义了沙箱的运行时环境、资源配置等。
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: agent_run_20250910_models.CreateTemplateRequest,
    ) -> agent_run_20250910_models.CreateTemplateResponse:
        """
        @summary 创建模板
        
        @description 创建一个新的模板，用于后续创建沙箱。模板定义了沙箱的运行时环境、资源配置等。
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def delete_agent_runtime_with_options(
        self,
        agent_runtime_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeResponse:
        """
        @summary 删除智能体运行时
        
        @description 删除指定的智能体运行时实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentRuntimeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_runtime_with_options_async(
        self,
        agent_runtime_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeResponse:
        """
        @summary 删除智能体运行时
        
        @description 删除指定的智能体运行时实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentRuntimeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_runtime(
        self,
        agent_runtime_id: str,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeResponse:
        """
        @summary 删除智能体运行时
        
        @description 删除指定的智能体运行时实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @return: DeleteAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_agent_runtime_with_options(agent_runtime_id, headers, runtime)

    async def delete_agent_runtime_async(
        self,
        agent_runtime_id: str,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeResponse:
        """
        @summary 删除智能体运行时
        
        @description 删除指定的智能体运行时实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @return: DeleteAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_agent_runtime_with_options_async(agent_runtime_id, headers, runtime)

    def delete_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeEndpointResponse:
        """
        @summary Delete an agent runtime endpoint
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentRuntimeEndpointResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints/{OpenApiUtilClient.get_encode_param(agent_runtime_endpoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeEndpointResponse:
        """
        @summary Delete an agent runtime endpoint
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentRuntimeEndpointResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints/{OpenApiUtilClient.get_encode_param(agent_runtime_endpoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeEndpointResponse:
        """
        @summary Delete an agent runtime endpoint
        
        @return: DeleteAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_agent_runtime_endpoint_with_options(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    async def delete_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> agent_run_20250910_models.DeleteAgentRuntimeEndpointResponse:
        """
        @summary Delete an agent runtime endpoint
        
        @return: DeleteAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_agent_runtime_endpoint_with_options_async(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    def delete_browser_with_options(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteBrowserResponse:
        """
        @summary 删除浏览器实例
        
        @description 删除指定的浏览器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBrowserResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBrowser',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers/{OpenApiUtilClient.get_encode_param(browser_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_browser_with_options_async(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteBrowserResponse:
        """
        @summary 删除浏览器实例
        
        @description 删除指定的浏览器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBrowserResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBrowser',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers/{OpenApiUtilClient.get_encode_param(browser_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_browser(
        self,
        browser_id: str,
    ) -> agent_run_20250910_models.DeleteBrowserResponse:
        """
        @summary 删除浏览器实例
        
        @description 删除指定的浏览器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @return: DeleteBrowserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_browser_with_options(browser_id, headers, runtime)

    async def delete_browser_async(
        self,
        browser_id: str,
    ) -> agent_run_20250910_models.DeleteBrowserResponse:
        """
        @summary 删除浏览器实例
        
        @description 删除指定的浏览器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @return: DeleteBrowserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_browser_with_options_async(browser_id, headers, runtime)

    def delete_code_interpreter_with_options(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteCodeInterpreterResponse:
        """
        @summary 删除代码解释器
        
        @description 删除指定的代码解释器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCodeInterpreterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeInterpreter',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters/{OpenApiUtilClient.get_encode_param(code_interpreter_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteCodeInterpreterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_code_interpreter_with_options_async(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteCodeInterpreterResponse:
        """
        @summary 删除代码解释器
        
        @description 删除指定的代码解释器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCodeInterpreterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeInterpreter',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters/{OpenApiUtilClient.get_encode_param(code_interpreter_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteCodeInterpreterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_code_interpreter(
        self,
        code_interpreter_id: str,
    ) -> agent_run_20250910_models.DeleteCodeInterpreterResponse:
        """
        @summary 删除代码解释器
        
        @description 删除指定的代码解释器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @return: DeleteCodeInterpreterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_code_interpreter_with_options(code_interpreter_id, headers, runtime)

    async def delete_code_interpreter_async(
        self,
        code_interpreter_id: str,
    ) -> agent_run_20250910_models.DeleteCodeInterpreterResponse:
        """
        @summary 删除代码解释器
        
        @description 删除指定的代码解释器实例，包括其所有相关资源和数据。删除操作不可逆，请谨慎操作。
        
        @return: DeleteCodeInterpreterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_code_interpreter_with_options_async(code_interpreter_id, headers, runtime)

    def delete_credential_with_options(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteCredentialResponse:
        """
        @summary Delete a credential
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials/{OpenApiUtilClient.get_encode_param(credential_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_credential_with_options_async(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteCredentialResponse:
        """
        @summary Delete a credential
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials/{OpenApiUtilClient.get_encode_param(credential_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_credential(
        self,
        credential_name: str,
    ) -> agent_run_20250910_models.DeleteCredentialResponse:
        """
        @summary Delete a credential
        
        @return: DeleteCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_credential_with_options(credential_name, headers, runtime)

    async def delete_credential_async(
        self,
        credential_name: str,
    ) -> agent_run_20250910_models.DeleteCredentialResponse:
        """
        @summary Delete a credential
        
        @return: DeleteCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_credential_with_options_async(credential_name, headers, runtime)

    def delete_memory_with_options(
        self,
        memory_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteMemoryResponse:
        """
        @summary delete memory store
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_with_options_async(
        self,
        memory_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteMemoryResponse:
        """
        @summary delete memory store
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory(
        self,
        memory_name: str,
    ) -> agent_run_20250910_models.DeleteMemoryResponse:
        """
        @summary delete memory store
        
        @return: DeleteMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_memory_with_options(memory_name, headers, runtime)

    async def delete_memory_async(
        self,
        memory_name: str,
    ) -> agent_run_20250910_models.DeleteMemoryResponse:
        """
        @summary delete memory store
        
        @return: DeleteMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_memory_with_options_async(memory_name, headers, runtime)

    def delete_model_proxy_with_options(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteModelProxyResponse:
        """
        @summary 删除模型
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelProxyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies/{OpenApiUtilClient.get_encode_param(model_proxy_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_proxy_with_options_async(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteModelProxyResponse:
        """
        @summary 删除模型
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelProxyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies/{OpenApiUtilClient.get_encode_param(model_proxy_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_proxy(
        self,
        model_proxy_name: str,
    ) -> agent_run_20250910_models.DeleteModelProxyResponse:
        """
        @summary 删除模型
        
        @return: DeleteModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_proxy_with_options(model_proxy_name, headers, runtime)

    async def delete_model_proxy_async(
        self,
        model_proxy_name: str,
    ) -> agent_run_20250910_models.DeleteModelProxyResponse:
        """
        @summary 删除模型
        
        @return: DeleteModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_proxy_with_options_async(model_proxy_name, headers, runtime)

    def delete_model_service_with_options(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteModelServiceResponse:
        """
        @summary 删除模型
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services/{OpenApiUtilClient.get_encode_param(model_service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_service_with_options_async(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteModelServiceResponse:
        """
        @summary 删除模型
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services/{OpenApiUtilClient.get_encode_param(model_service_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_service(
        self,
        model_service_name: str,
    ) -> agent_run_20250910_models.DeleteModelServiceResponse:
        """
        @summary 删除模型
        
        @return: DeleteModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_service_with_options(model_service_name, headers, runtime)

    async def delete_model_service_async(
        self,
        model_service_name: str,
    ) -> agent_run_20250910_models.DeleteModelServiceResponse:
        """
        @summary 删除模型
        
        @return: DeleteModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_service_with_options_async(model_service_name, headers, runtime)

    def delete_sandbox_with_options(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteSandboxResponse:
        """
        @summary 删除Sandbox
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSandboxResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes/{OpenApiUtilClient.get_encode_param(sandbox_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sandbox_with_options_async(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteSandboxResponse:
        """
        @summary 删除Sandbox
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSandboxResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes/{OpenApiUtilClient.get_encode_param(sandbox_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sandbox(
        self,
        sandbox_id: str,
    ) -> agent_run_20250910_models.DeleteSandboxResponse:
        """
        @summary 删除Sandbox
        
        @return: DeleteSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sandbox_with_options(sandbox_id, headers, runtime)

    async def delete_sandbox_async(
        self,
        sandbox_id: str,
    ) -> agent_run_20250910_models.DeleteSandboxResponse:
        """
        @summary 删除Sandbox
        
        @return: DeleteSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sandbox_with_options_async(sandbox_id, headers, runtime)

    def delete_template_with_options(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteTemplateResponse:
        """
        @summary 删除模板
        
        @description 删除指定的模板。删除后，该模板将无法再用于创建新的沙箱。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.DeleteTemplateResponse:
        """
        @summary 删除模板
        
        @description 删除指定的模板。删除后，该模板将无法再用于创建新的沙箱。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        template_name: str,
    ) -> agent_run_20250910_models.DeleteTemplateResponse:
        """
        @summary 删除模板
        
        @description 删除指定的模板。删除后，该模板将无法再用于创建新的沙箱。
        
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_name, headers, runtime)

    async def delete_template_async(
        self,
        template_name: str,
    ) -> agent_run_20250910_models.DeleteTemplateResponse:
        """
        @summary 删除模板
        
        @description 删除指定的模板。删除后，该模板将无法再用于创建新的沙箱。
        
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(template_name, headers, runtime)

    def get_access_token_with_options(
        self,
        request: agent_run_20250910_models.GetAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetAccessTokenResponse:
        """
        @summary Get access token for a resource
        
        @param request: GetAccessTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessToken',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/accessToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_token_with_options_async(
        self,
        request: agent_run_20250910_models.GetAccessTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetAccessTokenResponse:
        """
        @summary Get access token for a resource
        
        @param request: GetAccessTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['resourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessToken',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/accessToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_token(
        self,
        request: agent_run_20250910_models.GetAccessTokenRequest,
    ) -> agent_run_20250910_models.GetAccessTokenResponse:
        """
        @summary Get access token for a resource
        
        @param request: GetAccessTokenRequest
        @return: GetAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_access_token_with_options(request, headers, runtime)

    async def get_access_token_async(
        self,
        request: agent_run_20250910_models.GetAccessTokenRequest,
    ) -> agent_run_20250910_models.GetAccessTokenResponse:
        """
        @summary Get access token for a resource
        
        @param request: GetAccessTokenRequest
        @return: GetAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_access_token_with_options_async(request, headers, runtime)

    def get_agent_runtime_with_options(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.GetAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetAgentRuntimeResponse:
        """
        @summary 获取智能体运行时详情
        
        @description 根据智能体运行时ID获取指定智能体运行时的详细信息，包括配置、状态、资源使用情况等。
        
        @param request: GetAgentRuntimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentRuntimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_runtime_version):
            query['agentRuntimeVersion'] = request.agent_runtime_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_runtime_with_options_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.GetAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetAgentRuntimeResponse:
        """
        @summary 获取智能体运行时详情
        
        @description 根据智能体运行时ID获取指定智能体运行时的详细信息，包括配置、状态、资源使用情况等。
        
        @param request: GetAgentRuntimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentRuntimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_runtime_version):
            query['agentRuntimeVersion'] = request.agent_runtime_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_runtime(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.GetAgentRuntimeRequest,
    ) -> agent_run_20250910_models.GetAgentRuntimeResponse:
        """
        @summary 获取智能体运行时详情
        
        @description 根据智能体运行时ID获取指定智能体运行时的详细信息，包括配置、状态、资源使用情况等。
        
        @param request: GetAgentRuntimeRequest
        @return: GetAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agent_runtime_with_options(agent_runtime_id, request, headers, runtime)

    async def get_agent_runtime_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.GetAgentRuntimeRequest,
    ) -> agent_run_20250910_models.GetAgentRuntimeResponse:
        """
        @summary 获取智能体运行时详情
        
        @description 根据智能体运行时ID获取指定智能体运行时的详细信息，包括配置、状态、资源使用情况等。
        
        @param request: GetAgentRuntimeRequest
        @return: GetAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agent_runtime_with_options_async(agent_runtime_id, request, headers, runtime)

    def get_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetAgentRuntimeEndpointResponse:
        """
        @summary Get an agent runtime endpoint
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentRuntimeEndpointResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints/{OpenApiUtilClient.get_encode_param(agent_runtime_endpoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetAgentRuntimeEndpointResponse:
        """
        @summary Get an agent runtime endpoint
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentRuntimeEndpointResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints/{OpenApiUtilClient.get_encode_param(agent_runtime_endpoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> agent_run_20250910_models.GetAgentRuntimeEndpointResponse:
        """
        @summary Get an agent runtime endpoint
        
        @return: GetAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agent_runtime_endpoint_with_options(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    async def get_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
    ) -> agent_run_20250910_models.GetAgentRuntimeEndpointResponse:
        """
        @summary Get an agent runtime endpoint
        
        @return: GetAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agent_runtime_endpoint_with_options_async(agent_runtime_id, agent_runtime_endpoint_id, headers, runtime)

    def get_browser_with_options(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetBrowserResponse:
        """
        @summary 获取浏览器实例详情
        
        @description 根据浏览器ID获取指定浏览器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBrowserResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBrowser',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers/{OpenApiUtilClient.get_encode_param(browser_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_browser_with_options_async(
        self,
        browser_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetBrowserResponse:
        """
        @summary 获取浏览器实例详情
        
        @description 根据浏览器ID获取指定浏览器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBrowserResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBrowser',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers/{OpenApiUtilClient.get_encode_param(browser_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_browser(
        self,
        browser_id: str,
    ) -> agent_run_20250910_models.GetBrowserResponse:
        """
        @summary 获取浏览器实例详情
        
        @description 根据浏览器ID获取指定浏览器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @return: GetBrowserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_browser_with_options(browser_id, headers, runtime)

    async def get_browser_async(
        self,
        browser_id: str,
    ) -> agent_run_20250910_models.GetBrowserResponse:
        """
        @summary 获取浏览器实例详情
        
        @description 根据浏览器ID获取指定浏览器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @return: GetBrowserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_browser_with_options_async(browser_id, headers, runtime)

    def get_code_interpreter_with_options(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetCodeInterpreterResponse:
        """
        @summary 获取代码解释器详情
        
        @description 根据代码解释器ID获取指定代码解释器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCodeInterpreterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeInterpreter',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters/{OpenApiUtilClient.get_encode_param(code_interpreter_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetCodeInterpreterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_interpreter_with_options_async(
        self,
        code_interpreter_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetCodeInterpreterResponse:
        """
        @summary 获取代码解释器详情
        
        @description 根据代码解释器ID获取指定代码解释器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCodeInterpreterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeInterpreter',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters/{OpenApiUtilClient.get_encode_param(code_interpreter_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetCodeInterpreterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_interpreter(
        self,
        code_interpreter_id: str,
    ) -> agent_run_20250910_models.GetCodeInterpreterResponse:
        """
        @summary 获取代码解释器详情
        
        @description 根据代码解释器ID获取指定代码解释器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @return: GetCodeInterpreterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_code_interpreter_with_options(code_interpreter_id, headers, runtime)

    async def get_code_interpreter_async(
        self,
        code_interpreter_id: str,
    ) -> agent_run_20250910_models.GetCodeInterpreterResponse:
        """
        @summary 获取代码解释器详情
        
        @description 根据代码解释器ID获取指定代码解释器实例的详细信息，包括配置、状态、资源使用情况等。
        
        @return: GetCodeInterpreterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_code_interpreter_with_options_async(code_interpreter_id, headers, runtime)

    def get_credential_with_options(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetCredentialResponse:
        """
        @summary Get a credential
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials/{OpenApiUtilClient.get_encode_param(credential_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_with_options_async(
        self,
        credential_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetCredentialResponse:
        """
        @summary Get a credential
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials/{OpenApiUtilClient.get_encode_param(credential_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential(
        self,
        credential_name: str,
    ) -> agent_run_20250910_models.GetCredentialResponse:
        """
        @summary Get a credential
        
        @return: GetCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_credential_with_options(credential_name, headers, runtime)

    async def get_credential_async(
        self,
        credential_name: str,
    ) -> agent_run_20250910_models.GetCredentialResponse:
        """
        @summary Get a credential
        
        @return: GetCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_credential_with_options_async(credential_name, headers, runtime)

    def get_memory_with_options(
        self,
        memory_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetMemoryResponse:
        """
        @summary GetMemory
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_with_options_async(
        self,
        memory_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetMemoryResponse:
        """
        @summary GetMemory
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory(
        self,
        memory_name: str,
    ) -> agent_run_20250910_models.GetMemoryResponse:
        """
        @summary GetMemory
        
        @return: GetMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_memory_with_options(memory_name, headers, runtime)

    async def get_memory_async(
        self,
        memory_name: str,
    ) -> agent_run_20250910_models.GetMemoryResponse:
        """
        @summary GetMemory
        
        @return: GetMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_memory_with_options_async(memory_name, headers, runtime)

    def get_memory_event_with_options(
        self,
        memory_name: str,
        session_id: str,
        event_id: str,
        request: agent_run_20250910_models.GetMemoryEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetMemoryEventResponse:
        """
        @summary get event
        
        @param request: GetMemoryEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMemoryEvent',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions/{OpenApiUtilClient.get_encode_param(session_id)}/events/{OpenApiUtilClient.get_encode_param(event_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetMemoryEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_event_with_options_async(
        self,
        memory_name: str,
        session_id: str,
        event_id: str,
        request: agent_run_20250910_models.GetMemoryEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetMemoryEventResponse:
        """
        @summary get event
        
        @param request: GetMemoryEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemoryEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMemoryEvent',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions/{OpenApiUtilClient.get_encode_param(session_id)}/events/{OpenApiUtilClient.get_encode_param(event_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetMemoryEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory_event(
        self,
        memory_name: str,
        session_id: str,
        event_id: str,
        request: agent_run_20250910_models.GetMemoryEventRequest,
    ) -> agent_run_20250910_models.GetMemoryEventResponse:
        """
        @summary get event
        
        @param request: GetMemoryEventRequest
        @return: GetMemoryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_memory_event_with_options(memory_name, session_id, event_id, request, headers, runtime)

    async def get_memory_event_async(
        self,
        memory_name: str,
        session_id: str,
        event_id: str,
        request: agent_run_20250910_models.GetMemoryEventRequest,
    ) -> agent_run_20250910_models.GetMemoryEventResponse:
        """
        @summary get event
        
        @param request: GetMemoryEventRequest
        @return: GetMemoryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_memory_event_with_options_async(memory_name, session_id, event_id, request, headers, runtime)

    def get_memory_session_with_options(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.GetMemorySessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetMemorySessionResponse:
        """
        @summary 获取内存会话详情
        
        @description 根据会话ID获取指定内存会话的详细信息，包括会话中的事件记录、时间戳等。用于查看和管理对话历史。
        
        @param request: GetMemorySessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemorySessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMemorySession',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions/{OpenApiUtilClient.get_encode_param(session_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetMemorySessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_session_with_options_async(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.GetMemorySessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetMemorySessionResponse:
        """
        @summary 获取内存会话详情
        
        @description 根据会话ID获取指定内存会话的详细信息，包括会话中的事件记录、时间戳等。用于查看和管理对话历史。
        
        @param request: GetMemorySessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemorySessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMemorySession',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions/{OpenApiUtilClient.get_encode_param(session_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetMemorySessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory_session(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.GetMemorySessionRequest,
    ) -> agent_run_20250910_models.GetMemorySessionResponse:
        """
        @summary 获取内存会话详情
        
        @description 根据会话ID获取指定内存会话的详细信息，包括会话中的事件记录、时间戳等。用于查看和管理对话历史。
        
        @param request: GetMemorySessionRequest
        @return: GetMemorySessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_memory_session_with_options(memory_name, session_id, request, headers, runtime)

    async def get_memory_session_async(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.GetMemorySessionRequest,
    ) -> agent_run_20250910_models.GetMemorySessionResponse:
        """
        @summary 获取内存会话详情
        
        @description 根据会话ID获取指定内存会话的详细信息，包括会话中的事件记录、时间戳等。用于查看和管理对话历史。
        
        @param request: GetMemorySessionRequest
        @return: GetMemorySessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_memory_session_with_options_async(memory_name, session_id, request, headers, runtime)

    def get_model_proxy_with_options(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetModelProxyResponse:
        """
        @summary 查看model
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelProxyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies/{OpenApiUtilClient.get_encode_param(model_proxy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_proxy_with_options_async(
        self,
        model_proxy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetModelProxyResponse:
        """
        @summary 查看model
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelProxyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies/{OpenApiUtilClient.get_encode_param(model_proxy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_proxy(
        self,
        model_proxy_name: str,
    ) -> agent_run_20250910_models.GetModelProxyResponse:
        """
        @summary 查看model
        
        @return: GetModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_proxy_with_options(model_proxy_name, headers, runtime)

    async def get_model_proxy_async(
        self,
        model_proxy_name: str,
    ) -> agent_run_20250910_models.GetModelProxyResponse:
        """
        @summary 查看model
        
        @return: GetModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_proxy_with_options_async(model_proxy_name, headers, runtime)

    def get_model_service_with_options(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetModelServiceResponse:
        """
        @summary 查看model
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services/{OpenApiUtilClient.get_encode_param(model_service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_service_with_options_async(
        self,
        model_service_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetModelServiceResponse:
        """
        @summary 查看model
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services/{OpenApiUtilClient.get_encode_param(model_service_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_service(
        self,
        model_service_name: str,
    ) -> agent_run_20250910_models.GetModelServiceResponse:
        """
        @summary 查看model
        
        @return: GetModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_service_with_options(model_service_name, headers, runtime)

    async def get_model_service_async(
        self,
        model_service_name: str,
    ) -> agent_run_20250910_models.GetModelServiceResponse:
        """
        @summary 查看model
        
        @return: GetModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_service_with_options_async(model_service_name, headers, runtime)

    def get_sandbox_with_options(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetSandboxResponse:
        """
        @summary 获取沙箱
        
        @description 根据沙箱ID获取指定沙箱的详细信息，包括状态、配置等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSandboxResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes/{OpenApiUtilClient.get_encode_param(sandbox_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sandbox_with_options_async(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetSandboxResponse:
        """
        @summary 获取沙箱
        
        @description 根据沙箱ID获取指定沙箱的详细信息，包括状态、配置等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSandboxResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes/{OpenApiUtilClient.get_encode_param(sandbox_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sandbox(
        self,
        sandbox_id: str,
    ) -> agent_run_20250910_models.GetSandboxResponse:
        """
        @summary 获取沙箱
        
        @description 根据沙箱ID获取指定沙箱的详细信息，包括状态、配置等。
        
        @return: GetSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sandbox_with_options(sandbox_id, headers, runtime)

    async def get_sandbox_async(
        self,
        sandbox_id: str,
    ) -> agent_run_20250910_models.GetSandboxResponse:
        """
        @summary 获取沙箱
        
        @description 根据沙箱ID获取指定沙箱的详细信息，包括状态、配置等。
        
        @return: GetSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sandbox_with_options_async(sandbox_id, headers, runtime)

    def get_template_with_options(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetTemplateResponse:
        """
        @summary 获取模板
        
        @description 根据模板名称获取指定模板的详细信息，包括配置、状态等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.GetTemplateResponse:
        """
        @summary 获取模板
        
        @description 根据模板名称获取指定模板的详细信息，包括配置、状态等。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        template_name: str,
    ) -> agent_run_20250910_models.GetTemplateResponse:
        """
        @summary 获取模板
        
        @description 根据模板名称获取指定模板的详细信息，包括配置、状态等。
        
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(template_name, headers, runtime)

    async def get_template_async(
        self,
        template_name: str,
    ) -> agent_run_20250910_models.GetTemplateResponse:
        """
        @summary 获取模板
        
        @description 根据模板名称获取指定模板的详细信息，包括配置、状态等。
        
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(template_name, headers, runtime)

    def list_agent_runtime_endpoints_with_options(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListAgentRuntimeEndpointsResponse:
        """
        @summary 列出智能体运行时端点
        
        @description 获取指定智能体运行时的所有端点列表，支持按名称过滤和分页查询。端点用于外部系统访问智能体运行时服务。
        
        @param request: ListAgentRuntimeEndpointsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentRuntimeEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_name):
            query['endpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['searchMode'] = request.search_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentRuntimeEndpoints',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListAgentRuntimeEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_runtime_endpoints_with_options_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListAgentRuntimeEndpointsResponse:
        """
        @summary 列出智能体运行时端点
        
        @description 获取指定智能体运行时的所有端点列表，支持按名称过滤和分页查询。端点用于外部系统访问智能体运行时服务。
        
        @param request: ListAgentRuntimeEndpointsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentRuntimeEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_name):
            query['endpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['searchMode'] = request.search_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentRuntimeEndpoints',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListAgentRuntimeEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_runtime_endpoints(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeEndpointsRequest,
    ) -> agent_run_20250910_models.ListAgentRuntimeEndpointsResponse:
        """
        @summary 列出智能体运行时端点
        
        @description 获取指定智能体运行时的所有端点列表，支持按名称过滤和分页查询。端点用于外部系统访问智能体运行时服务。
        
        @param request: ListAgentRuntimeEndpointsRequest
        @return: ListAgentRuntimeEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agent_runtime_endpoints_with_options(agent_runtime_id, request, headers, runtime)

    async def list_agent_runtime_endpoints_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeEndpointsRequest,
    ) -> agent_run_20250910_models.ListAgentRuntimeEndpointsResponse:
        """
        @summary 列出智能体运行时端点
        
        @description 获取指定智能体运行时的所有端点列表，支持按名称过滤和分页查询。端点用于外部系统访问智能体运行时服务。
        
        @param request: ListAgentRuntimeEndpointsRequest
        @return: ListAgentRuntimeEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agent_runtime_endpoints_with_options_async(agent_runtime_id, request, headers, runtime)

    def list_agent_runtime_versions_with_options(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListAgentRuntimeVersionsResponse:
        """
        @summary List agent runtime versions
        
        @param request: ListAgentRuntimeVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentRuntimeVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentRuntimeVersions',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListAgentRuntimeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_runtime_versions_with_options_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListAgentRuntimeVersionsResponse:
        """
        @summary List agent runtime versions
        
        @param request: ListAgentRuntimeVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentRuntimeVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentRuntimeVersions',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListAgentRuntimeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_runtime_versions(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeVersionsRequest,
    ) -> agent_run_20250910_models.ListAgentRuntimeVersionsResponse:
        """
        @summary List agent runtime versions
        
        @param request: ListAgentRuntimeVersionsRequest
        @return: ListAgentRuntimeVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agent_runtime_versions_with_options(agent_runtime_id, request, headers, runtime)

    async def list_agent_runtime_versions_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.ListAgentRuntimeVersionsRequest,
    ) -> agent_run_20250910_models.ListAgentRuntimeVersionsResponse:
        """
        @summary List agent runtime versions
        
        @param request: ListAgentRuntimeVersionsRequest
        @return: ListAgentRuntimeVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agent_runtime_versions_with_options_async(agent_runtime_id, request, headers, runtime)

    def list_agent_runtimes_with_options(
        self,
        request: agent_run_20250910_models.ListAgentRuntimesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListAgentRuntimesResponse:
        """
        @summary 列出智能体运行时
        
        @description 获取当前用户的所有智能体运行时列表，支持按名称、标签等条件过滤，支持分页查询。
        
        @param request: ListAgentRuntimesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentRuntimesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_runtime_name):
            query['agentRuntimeName'] = request.agent_runtime_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['searchMode'] = request.search_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentRuntimes',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListAgentRuntimesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_runtimes_with_options_async(
        self,
        request: agent_run_20250910_models.ListAgentRuntimesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListAgentRuntimesResponse:
        """
        @summary 列出智能体运行时
        
        @description 获取当前用户的所有智能体运行时列表，支持按名称、标签等条件过滤，支持分页查询。
        
        @param request: ListAgentRuntimesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentRuntimesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_runtime_name):
            query['agentRuntimeName'] = request.agent_runtime_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['searchMode'] = request.search_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentRuntimes',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListAgentRuntimesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_runtimes(
        self,
        request: agent_run_20250910_models.ListAgentRuntimesRequest,
    ) -> agent_run_20250910_models.ListAgentRuntimesResponse:
        """
        @summary 列出智能体运行时
        
        @description 获取当前用户的所有智能体运行时列表，支持按名称、标签等条件过滤，支持分页查询。
        
        @param request: ListAgentRuntimesRequest
        @return: ListAgentRuntimesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agent_runtimes_with_options(request, headers, runtime)

    async def list_agent_runtimes_async(
        self,
        request: agent_run_20250910_models.ListAgentRuntimesRequest,
    ) -> agent_run_20250910_models.ListAgentRuntimesResponse:
        """
        @summary 列出智能体运行时
        
        @description 获取当前用户的所有智能体运行时列表，支持按名称、标签等条件过滤，支持分页查询。
        
        @param request: ListAgentRuntimesRequest
        @return: ListAgentRuntimesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agent_runtimes_with_options_async(request, headers, runtime)

    def list_browsers_with_options(
        self,
        request: agent_run_20250910_models.ListBrowsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListBrowsersResponse:
        """
        @summary 列出浏览器实例
        
        @description 获取当前用户的所有浏览器实例列表，支持按名称、状态等条件过滤，支持分页查询。
        
        @param request: ListBrowsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBrowsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.browser_name):
            query['browserName'] = request.browser_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBrowsers',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListBrowsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_browsers_with_options_async(
        self,
        request: agent_run_20250910_models.ListBrowsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListBrowsersResponse:
        """
        @summary 列出浏览器实例
        
        @description 获取当前用户的所有浏览器实例列表，支持按名称、状态等条件过滤，支持分页查询。
        
        @param request: ListBrowsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBrowsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.browser_name):
            query['browserName'] = request.browser_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBrowsers',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/browsers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListBrowsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_browsers(
        self,
        request: agent_run_20250910_models.ListBrowsersRequest,
    ) -> agent_run_20250910_models.ListBrowsersResponse:
        """
        @summary 列出浏览器实例
        
        @description 获取当前用户的所有浏览器实例列表，支持按名称、状态等条件过滤，支持分页查询。
        
        @param request: ListBrowsersRequest
        @return: ListBrowsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_browsers_with_options(request, headers, runtime)

    async def list_browsers_async(
        self,
        request: agent_run_20250910_models.ListBrowsersRequest,
    ) -> agent_run_20250910_models.ListBrowsersResponse:
        """
        @summary 列出浏览器实例
        
        @description 获取当前用户的所有浏览器实例列表，支持按名称、状态等条件过滤，支持分页查询。
        
        @param request: ListBrowsersRequest
        @return: ListBrowsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_browsers_with_options_async(request, headers, runtime)

    def list_code_interpreters_with_options(
        self,
        request: agent_run_20250910_models.ListCodeInterpretersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListCodeInterpretersResponse:
        """
        @summary 列出代码解释器
        
        @description 获取当前用户的所有代码解释器实例列表，支持按名称等条件过滤，支持分页查询。
        
        @param request: ListCodeInterpretersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCodeInterpretersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_interpreter_name):
            query['codeInterpreterName'] = request.code_interpreter_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeInterpreters',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListCodeInterpretersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_code_interpreters_with_options_async(
        self,
        request: agent_run_20250910_models.ListCodeInterpretersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListCodeInterpretersResponse:
        """
        @summary 列出代码解释器
        
        @description 获取当前用户的所有代码解释器实例列表，支持按名称等条件过滤，支持分页查询。
        
        @param request: ListCodeInterpretersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCodeInterpretersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_interpreter_name):
            query['codeInterpreterName'] = request.code_interpreter_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeInterpreters',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/code-interpreters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListCodeInterpretersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_code_interpreters(
        self,
        request: agent_run_20250910_models.ListCodeInterpretersRequest,
    ) -> agent_run_20250910_models.ListCodeInterpretersResponse:
        """
        @summary 列出代码解释器
        
        @description 获取当前用户的所有代码解释器实例列表，支持按名称等条件过滤，支持分页查询。
        
        @param request: ListCodeInterpretersRequest
        @return: ListCodeInterpretersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_code_interpreters_with_options(request, headers, runtime)

    async def list_code_interpreters_async(
        self,
        request: agent_run_20250910_models.ListCodeInterpretersRequest,
    ) -> agent_run_20250910_models.ListCodeInterpretersResponse:
        """
        @summary 列出代码解释器
        
        @description 获取当前用户的所有代码解释器实例列表，支持按名称等条件过滤，支持分页查询。
        
        @param request: ListCodeInterpretersRequest
        @return: ListCodeInterpretersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_code_interpreters_with_options_async(request, headers, runtime)

    def list_credentials_with_options(
        self,
        request: agent_run_20250910_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListCredentialsResponse:
        """
        @summary List credentials
        
        @param request: ListCredentialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_auth_type):
            query['credentialAuthType'] = request.credential_auth_type
        if not UtilClient.is_unset(request.credential_name):
            query['credentialName'] = request.credential_name
        if not UtilClient.is_unset(request.credential_source_type):
            query['credentialSourceType'] = request.credential_source_type
        if not UtilClient.is_unset(request.enabled):
            query['enabled'] = request.enabled
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCredentials',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_credentials_with_options_async(
        self,
        request: agent_run_20250910_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListCredentialsResponse:
        """
        @summary List credentials
        
        @param request: ListCredentialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_auth_type):
            query['credentialAuthType'] = request.credential_auth_type
        if not UtilClient.is_unset(request.credential_name):
            query['credentialName'] = request.credential_name
        if not UtilClient.is_unset(request.credential_source_type):
            query['credentialSourceType'] = request.credential_source_type
        if not UtilClient.is_unset(request.enabled):
            query['enabled'] = request.enabled
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCredentials',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_credentials(
        self,
        request: agent_run_20250910_models.ListCredentialsRequest,
    ) -> agent_run_20250910_models.ListCredentialsResponse:
        """
        @summary List credentials
        
        @param request: ListCredentialsRequest
        @return: ListCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_credentials_with_options(request, headers, runtime)

    async def list_credentials_async(
        self,
        request: agent_run_20250910_models.ListCredentialsRequest,
    ) -> agent_run_20250910_models.ListCredentialsResponse:
        """
        @summary List credentials
        
        @param request: ListCredentialsRequest
        @return: ListCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_credentials_with_options_async(request, headers, runtime)

    def list_memory_with_options(
        self,
        request: agent_run_20250910_models.ListMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListMemoryResponse:
        """
        @summary ListMemory
        
        @param request: ListMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern):
            query['pattern'] = request.pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memory_with_options_async(
        self,
        request: agent_run_20250910_models.ListMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListMemoryResponse:
        """
        @summary ListMemory
        
        @param request: ListMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern):
            query['pattern'] = request.pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memory(
        self,
        request: agent_run_20250910_models.ListMemoryRequest,
    ) -> agent_run_20250910_models.ListMemoryResponse:
        """
        @summary ListMemory
        
        @param request: ListMemoryRequest
        @return: ListMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_memory_with_options(request, headers, runtime)

    async def list_memory_async(
        self,
        request: agent_run_20250910_models.ListMemoryRequest,
    ) -> agent_run_20250910_models.ListMemoryResponse:
        """
        @summary ListMemory
        
        @param request: ListMemoryRequest
        @return: ListMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_memory_with_options_async(request, headers, runtime)

    def list_memory_event_with_options(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.ListMemoryEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListMemoryEventResponse:
        """
        @summary list events
        
        @param request: ListMemoryEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoryEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemoryEvent',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions/{OpenApiUtilClient.get_encode_param(session_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListMemoryEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memory_event_with_options_async(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.ListMemoryEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListMemoryEventResponse:
        """
        @summary list events
        
        @param request: ListMemoryEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemoryEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemoryEvent',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions/{OpenApiUtilClient.get_encode_param(session_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListMemoryEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memory_event(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.ListMemoryEventRequest,
    ) -> agent_run_20250910_models.ListMemoryEventResponse:
        """
        @summary list events
        
        @param request: ListMemoryEventRequest
        @return: ListMemoryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_memory_event_with_options(memory_name, session_id, request, headers, runtime)

    async def list_memory_event_async(
        self,
        memory_name: str,
        session_id: str,
        request: agent_run_20250910_models.ListMemoryEventRequest,
    ) -> agent_run_20250910_models.ListMemoryEventResponse:
        """
        @summary list events
        
        @param request: ListMemoryEventRequest
        @return: ListMemoryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_memory_event_with_options_async(memory_name, session_id, request, headers, runtime)

    def list_memory_sessions_with_options(
        self,
        memory_name: str,
        request: agent_run_20250910_models.ListMemorySessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListMemorySessionsResponse:
        """
        @summary 列出内存会话
        
        @description 获取指定内存实例的所有会话列表，支持按时间范围过滤和分页查询。会话是AgentRun中用于存储对话历史和管理上下文的重要组件。
        
        @param request: ListMemorySessionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemorySessionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemorySessions',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListMemorySessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memory_sessions_with_options_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.ListMemorySessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListMemorySessionsResponse:
        """
        @summary 列出内存会话
        
        @description 获取指定内存实例的所有会话列表，支持按时间范围过滤和分页查询。会话是AgentRun中用于存储对话历史和管理上下文的重要组件。
        
        @param request: ListMemorySessionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemorySessionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemorySessions',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/sessions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListMemorySessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memory_sessions(
        self,
        memory_name: str,
        request: agent_run_20250910_models.ListMemorySessionsRequest,
    ) -> agent_run_20250910_models.ListMemorySessionsResponse:
        """
        @summary 列出内存会话
        
        @description 获取指定内存实例的所有会话列表，支持按时间范围过滤和分页查询。会话是AgentRun中用于存储对话历史和管理上下文的重要组件。
        
        @param request: ListMemorySessionsRequest
        @return: ListMemorySessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_memory_sessions_with_options(memory_name, request, headers, runtime)

    async def list_memory_sessions_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.ListMemorySessionsRequest,
    ) -> agent_run_20250910_models.ListMemorySessionsResponse:
        """
        @summary 列出内存会话
        
        @description 获取指定内存实例的所有会话列表，支持按时间范围过滤和分页查询。会话是AgentRun中用于存储对话历史和管理上下文的重要组件。
        
        @param request: ListMemorySessionsRequest
        @return: ListMemorySessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_memory_sessions_with_options_async(memory_name, request, headers, runtime)

    def list_model_providers_with_options(
        self,
        request: agent_run_20250910_models.ListModelProvidersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListModelProvidersResponse:
        """
        @summary 查询支持的模型提供商及其模型
        
        @param request: ListModelProvidersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_name):
            query['modelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelProviders',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-providers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListModelProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_providers_with_options_async(
        self,
        request: agent_run_20250910_models.ListModelProvidersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListModelProvidersResponse:
        """
        @summary 查询支持的模型提供商及其模型
        
        @param request: ListModelProvidersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_name):
            query['modelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelProviders',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-providers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListModelProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_providers(
        self,
        request: agent_run_20250910_models.ListModelProvidersRequest,
    ) -> agent_run_20250910_models.ListModelProvidersResponse:
        """
        @summary 查询支持的模型提供商及其模型
        
        @param request: ListModelProvidersRequest
        @return: ListModelProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_providers_with_options(request, headers, runtime)

    async def list_model_providers_async(
        self,
        request: agent_run_20250910_models.ListModelProvidersRequest,
    ) -> agent_run_20250910_models.ListModelProvidersResponse:
        """
        @summary 查询支持的模型提供商及其模型
        
        @param request: ListModelProvidersRequest
        @return: ListModelProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_providers_with_options_async(request, headers, runtime)

    def list_model_proxies_with_options(
        self,
        request: agent_run_20250910_models.ListModelProxiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListModelProxiesResponse:
        """
        @summary model列表
        
        @param request: ListModelProxiesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelProxiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_mode):
            query['proxyMode'] = request.proxy_mode
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelProxies',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListModelProxiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_proxies_with_options_async(
        self,
        request: agent_run_20250910_models.ListModelProxiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListModelProxiesResponse:
        """
        @summary model列表
        
        @param request: ListModelProxiesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelProxiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_mode):
            query['proxyMode'] = request.proxy_mode
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelProxies',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListModelProxiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_proxies(
        self,
        request: agent_run_20250910_models.ListModelProxiesRequest,
    ) -> agent_run_20250910_models.ListModelProxiesResponse:
        """
        @summary model列表
        
        @param request: ListModelProxiesRequest
        @return: ListModelProxiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_proxies_with_options(request, headers, runtime)

    async def list_model_proxies_async(
        self,
        request: agent_run_20250910_models.ListModelProxiesRequest,
    ) -> agent_run_20250910_models.ListModelProxiesResponse:
        """
        @summary model列表
        
        @param request: ListModelProxiesRequest
        @return: ListModelProxiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_proxies_with_options_async(request, headers, runtime)

    def list_model_services_with_options(
        self,
        request: agent_run_20250910_models.ListModelServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListModelServicesResponse:
        """
        @summary model列表
        
        @param request: ListModelServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelServices',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListModelServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_services_with_options_async(
        self,
        request: agent_run_20250910_models.ListModelServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListModelServicesResponse:
        """
        @summary model列表
        
        @param request: ListModelServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelServices',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListModelServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_services(
        self,
        request: agent_run_20250910_models.ListModelServicesRequest,
    ) -> agent_run_20250910_models.ListModelServicesResponse:
        """
        @summary model列表
        
        @param request: ListModelServicesRequest
        @return: ListModelServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_services_with_options(request, headers, runtime)

    async def list_model_services_async(
        self,
        request: agent_run_20250910_models.ListModelServicesRequest,
    ) -> agent_run_20250910_models.ListModelServicesResponse:
        """
        @summary model列表
        
        @param request: ListModelServicesRequest
        @return: ListModelServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_services_with_options_async(request, headers, runtime)

    def list_sandboxes_with_options(
        self,
        request: agent_run_20250910_models.ListSandboxesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListSandboxesResponse:
        """
        @summary 列出沙箱
        
        @description 获取当前用户的所有沙箱列表，支持按模板名称过滤，支持分页查询。
        
        @param request: ListSandboxesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSandboxesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSandboxes',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListSandboxesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sandboxes_with_options_async(
        self,
        request: agent_run_20250910_models.ListSandboxesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListSandboxesResponse:
        """
        @summary 列出沙箱
        
        @description 获取当前用户的所有沙箱列表，支持按模板名称过滤，支持分页查询。
        
        @param request: ListSandboxesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSandboxesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSandboxes',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListSandboxesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sandboxes(
        self,
        request: agent_run_20250910_models.ListSandboxesRequest,
    ) -> agent_run_20250910_models.ListSandboxesResponse:
        """
        @summary 列出沙箱
        
        @description 获取当前用户的所有沙箱列表，支持按模板名称过滤，支持分页查询。
        
        @param request: ListSandboxesRequest
        @return: ListSandboxesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sandboxes_with_options(request, headers, runtime)

    async def list_sandboxes_async(
        self,
        request: agent_run_20250910_models.ListSandboxesRequest,
    ) -> agent_run_20250910_models.ListSandboxesResponse:
        """
        @summary 列出沙箱
        
        @description 获取当前用户的所有沙箱列表，支持按模板名称过滤，支持分页查询。
        
        @param request: ListSandboxesRequest
        @return: ListSandboxesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sandboxes_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: agent_run_20250910_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListTemplatesResponse:
        """
        @summary 列出模板
        
        @description 获取当前用户的所有模板列表，支持按模板类型过滤，支持分页查询。
        
        @param request: ListTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: agent_run_20250910_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.ListTemplatesResponse:
        """
        @summary 列出模板
        
        @description 获取当前用户的所有模板列表，支持按模板类型过滤，支持分页查询。
        
        @param request: ListTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: agent_run_20250910_models.ListTemplatesRequest,
    ) -> agent_run_20250910_models.ListTemplatesResponse:
        """
        @summary 列出模板
        
        @description 获取当前用户的所有模板列表，支持按模板类型过滤，支持分页查询。
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: agent_run_20250910_models.ListTemplatesRequest,
    ) -> agent_run_20250910_models.ListTemplatesResponse:
        """
        @summary 列出模板
        
        @description 获取当前用户的所有模板列表，支持按模板类型过滤，支持分页查询。
        
        @param request: ListTemplatesRequest
        @return: ListTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def publish_runtime_version_with_options(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.PublishRuntimeVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.PublishRuntimeVersionResponse:
        """
        @summary 发布运行时版本
        
        @description 为指定的智能体运行时发布新版本，用于版本管理和部署。新版本可以包含代码更新、配置变更等内容。
        
        @param request: PublishRuntimeVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRuntimeVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishRuntimeVersion',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.PublishRuntimeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_runtime_version_with_options_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.PublishRuntimeVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.PublishRuntimeVersionResponse:
        """
        @summary 发布运行时版本
        
        @description 为指定的智能体运行时发布新版本，用于版本管理和部署。新版本可以包含代码更新、配置变更等内容。
        
        @param request: PublishRuntimeVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRuntimeVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishRuntimeVersion',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.PublishRuntimeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_runtime_version(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.PublishRuntimeVersionRequest,
    ) -> agent_run_20250910_models.PublishRuntimeVersionResponse:
        """
        @summary 发布运行时版本
        
        @description 为指定的智能体运行时发布新版本，用于版本管理和部署。新版本可以包含代码更新、配置变更等内容。
        
        @param request: PublishRuntimeVersionRequest
        @return: PublishRuntimeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_runtime_version_with_options(agent_runtime_id, request, headers, runtime)

    async def publish_runtime_version_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.PublishRuntimeVersionRequest,
    ) -> agent_run_20250910_models.PublishRuntimeVersionResponse:
        """
        @summary 发布运行时版本
        
        @description 为指定的智能体运行时发布新版本，用于版本管理和部署。新版本可以包含代码更新、配置变更等内容。
        
        @param request: PublishRuntimeVersionRequest
        @return: PublishRuntimeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_runtime_version_with_options_async(agent_runtime_id, request, headers, runtime)

    def retrieve_memory_with_options(
        self,
        memory_name: str,
        request: agent_run_20250910_models.RetrieveMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.RetrieveMemoryResponse:
        """
        @summary RetrieveMemory
        
        @param request: RetrieveMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveMemoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.store):
            body['store'] = request.store
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.topk):
            body['topk'] = request.topk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetrieveMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/records',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.RetrieveMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_memory_with_options_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.RetrieveMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.RetrieveMemoryResponse:
        """
        @summary RetrieveMemory
        
        @param request: RetrieveMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetrieveMemoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.store):
            body['store'] = request.store
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.topk):
            body['topk'] = request.topk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetrieveMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}/records',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.RetrieveMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_memory(
        self,
        memory_name: str,
        request: agent_run_20250910_models.RetrieveMemoryRequest,
    ) -> agent_run_20250910_models.RetrieveMemoryResponse:
        """
        @summary RetrieveMemory
        
        @param request: RetrieveMemoryRequest
        @return: RetrieveMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retrieve_memory_with_options(memory_name, request, headers, runtime)

    async def retrieve_memory_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.RetrieveMemoryRequest,
    ) -> agent_run_20250910_models.RetrieveMemoryResponse:
        """
        @summary RetrieveMemory
        
        @param request: RetrieveMemoryRequest
        @return: RetrieveMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retrieve_memory_with_options_async(memory_name, request, headers, runtime)

    def stop_sandbox_with_options(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.StopSandboxResponse:
        """
        @summary 删除沙箱
        
        @description 停止指定的沙箱实例。停止后，沙箱将进入TERMINATED状态。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSandboxResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes/{OpenApiUtilClient.get_encode_param(sandbox_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.StopSandboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_sandbox_with_options_async(
        self,
        sandbox_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.StopSandboxResponse:
        """
        @summary 删除沙箱
        
        @description 停止指定的沙箱实例。停止后，沙箱将进入TERMINATED状态。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSandboxResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopSandbox',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/sandboxes/{OpenApiUtilClient.get_encode_param(sandbox_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.StopSandboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_sandbox(
        self,
        sandbox_id: str,
    ) -> agent_run_20250910_models.StopSandboxResponse:
        """
        @summary 删除沙箱
        
        @description 停止指定的沙箱实例。停止后，沙箱将进入TERMINATED状态。
        
        @return: StopSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_sandbox_with_options(sandbox_id, headers, runtime)

    async def stop_sandbox_async(
        self,
        sandbox_id: str,
    ) -> agent_run_20250910_models.StopSandboxResponse:
        """
        @summary 删除沙箱
        
        @description 停止指定的沙箱实例。停止后，沙箱将进入TERMINATED状态。
        
        @return: StopSandboxResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_sandbox_with_options_async(sandbox_id, headers, runtime)

    def stop_template_mcpwith_options(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.StopTemplateMCPResponse:
        """
        @summary 停止模板的MCP服务器
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTemplateMCPResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTemplateMCP',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}/mcp/stop',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.StopTemplateMCPResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_template_mcpwith_options_async(
        self,
        template_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.StopTemplateMCPResponse:
        """
        @summary 停止模板的MCP服务器
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTemplateMCPResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTemplateMCP',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}/mcp/stop',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.StopTemplateMCPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_template_mcp(
        self,
        template_name: str,
    ) -> agent_run_20250910_models.StopTemplateMCPResponse:
        """
        @summary 停止模板的MCP服务器
        
        @return: StopTemplateMCPResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_template_mcpwith_options(template_name, headers, runtime)

    async def stop_template_mcp_async(
        self,
        template_name: str,
    ) -> agent_run_20250910_models.StopTemplateMCPResponse:
        """
        @summary 停止模板的MCP服务器
        
        @return: StopTemplateMCPResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_template_mcpwith_options_async(template_name, headers, runtime)

    def update_agent_runtime_with_options(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeResponse:
        """
        @summary 更新智能体运行时
        
        @description 更新指定智能体运行时的配置信息，包括资源分配、网络配置、环境变量等。更新操作会触发运行时重启。
        
        @param request: UpdateAgentRuntimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgentRuntimeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateAgentRuntimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_runtime_with_options_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeResponse:
        """
        @summary 更新智能体运行时
        
        @description 更新指定智能体运行时的配置信息，包括资源分配、网络配置、环境变量等。更新操作会触发运行时重启。
        
        @param request: UpdateAgentRuntimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgentRuntimeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAgentRuntime',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateAgentRuntimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_runtime(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeRequest,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeResponse:
        """
        @summary 更新智能体运行时
        
        @description 更新指定智能体运行时的配置信息，包括资源分配、网络配置、环境变量等。更新操作会触发运行时重启。
        
        @param request: UpdateAgentRuntimeRequest
        @return: UpdateAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_agent_runtime_with_options(agent_runtime_id, request, headers, runtime)

    async def update_agent_runtime_async(
        self,
        agent_runtime_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeRequest,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeResponse:
        """
        @summary 更新智能体运行时
        
        @description 更新指定智能体运行时的配置信息，包括资源分配、网络配置、环境变量等。更新操作会触发运行时重启。
        
        @param request: UpdateAgentRuntimeRequest
        @return: UpdateAgentRuntimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_agent_runtime_with_options_async(agent_runtime_id, request, headers, runtime)

    def update_agent_runtime_endpoint_with_options(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeEndpointResponse:
        """
        @summary Update an agent runtime endpoint
        
        @param request: UpdateAgentRuntimeEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgentRuntimeEndpointResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints/{OpenApiUtilClient.get_encode_param(agent_runtime_endpoint_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateAgentRuntimeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_runtime_endpoint_with_options_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeEndpointResponse:
        """
        @summary Update an agent runtime endpoint
        
        @param request: UpdateAgentRuntimeEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgentRuntimeEndpointResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAgentRuntimeEndpoint',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/runtimes/{OpenApiUtilClient.get_encode_param(agent_runtime_id)}/endpoints/{OpenApiUtilClient.get_encode_param(agent_runtime_endpoint_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateAgentRuntimeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_runtime_endpoint(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeEndpointRequest,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeEndpointResponse:
        """
        @summary Update an agent runtime endpoint
        
        @param request: UpdateAgentRuntimeEndpointRequest
        @return: UpdateAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_agent_runtime_endpoint_with_options(agent_runtime_id, agent_runtime_endpoint_id, request, headers, runtime)

    async def update_agent_runtime_endpoint_async(
        self,
        agent_runtime_id: str,
        agent_runtime_endpoint_id: str,
        request: agent_run_20250910_models.UpdateAgentRuntimeEndpointRequest,
    ) -> agent_run_20250910_models.UpdateAgentRuntimeEndpointResponse:
        """
        @summary Update an agent runtime endpoint
        
        @param request: UpdateAgentRuntimeEndpointRequest
        @return: UpdateAgentRuntimeEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_agent_runtime_endpoint_with_options_async(agent_runtime_id, agent_runtime_endpoint_id, request, headers, runtime)

    def update_credential_with_options(
        self,
        credential_name: str,
        request: agent_run_20250910_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateCredentialResponse:
        """
        @summary Update a credential
        
        @param request: UpdateCredentialRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCredentialResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials/{OpenApiUtilClient.get_encode_param(credential_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credential_with_options_async(
        self,
        credential_name: str,
        request: agent_run_20250910_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateCredentialResponse:
        """
        @summary Update a credential
        
        @param request: UpdateCredentialRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCredentialResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateCredential',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/credentials/{OpenApiUtilClient.get_encode_param(credential_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credential(
        self,
        credential_name: str,
        request: agent_run_20250910_models.UpdateCredentialRequest,
    ) -> agent_run_20250910_models.UpdateCredentialResponse:
        """
        @summary Update a credential
        
        @param request: UpdateCredentialRequest
        @return: UpdateCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_credential_with_options(credential_name, request, headers, runtime)

    async def update_credential_async(
        self,
        credential_name: str,
        request: agent_run_20250910_models.UpdateCredentialRequest,
    ) -> agent_run_20250910_models.UpdateCredentialResponse:
        """
        @summary Update a credential
        
        @param request: UpdateCredentialRequest
        @return: UpdateCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_credential_with_options_async(credential_name, request, headers, runtime)

    def update_memory_with_options(
        self,
        memory_name: str,
        request: agent_run_20250910_models.UpdateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateMemoryResponse:
        """
        @summary Update Memory
        
        @param request: UpdateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.long_ttl):
            body['longTtl'] = request.long_ttl
        if not UtilClient.is_unset(request.short_ttl):
            body['shortTtl'] = request.short_ttl
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_with_options_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.UpdateMemoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateMemoryResponse:
        """
        @summary Update Memory
        
        @param request: UpdateMemoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.long_ttl):
            body['longTtl'] = request.long_ttl
        if not UtilClient.is_unset(request.short_ttl):
            body['shortTtl'] = request.short_ttl
        if not UtilClient.is_unset(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMemory',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/memories/{OpenApiUtilClient.get_encode_param(memory_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory(
        self,
        memory_name: str,
        request: agent_run_20250910_models.UpdateMemoryRequest,
    ) -> agent_run_20250910_models.UpdateMemoryResponse:
        """
        @summary Update Memory
        
        @param request: UpdateMemoryRequest
        @return: UpdateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_memory_with_options(memory_name, request, headers, runtime)

    async def update_memory_async(
        self,
        memory_name: str,
        request: agent_run_20250910_models.UpdateMemoryRequest,
    ) -> agent_run_20250910_models.UpdateMemoryResponse:
        """
        @summary Update Memory
        
        @param request: UpdateMemoryRequest
        @return: UpdateMemoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_memory_with_options_async(memory_name, request, headers, runtime)

    def update_model_proxy_with_options(
        self,
        model_proxy_name: str,
        request: agent_run_20250910_models.UpdateModelProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateModelProxyResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelProxyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelProxyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies/{OpenApiUtilClient.get_encode_param(model_proxy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateModelProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_proxy_with_options_async(
        self,
        model_proxy_name: str,
        request: agent_run_20250910_models.UpdateModelProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateModelProxyResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelProxyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelProxyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateModelProxy',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-proxies/{OpenApiUtilClient.get_encode_param(model_proxy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateModelProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_proxy(
        self,
        model_proxy_name: str,
        request: agent_run_20250910_models.UpdateModelProxyRequest,
    ) -> agent_run_20250910_models.UpdateModelProxyResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelProxyRequest
        @return: UpdateModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_proxy_with_options(model_proxy_name, request, headers, runtime)

    async def update_model_proxy_async(
        self,
        model_proxy_name: str,
        request: agent_run_20250910_models.UpdateModelProxyRequest,
    ) -> agent_run_20250910_models.UpdateModelProxyResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelProxyRequest
        @return: UpdateModelProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_proxy_with_options_async(model_proxy_name, request, headers, runtime)

    def update_model_service_with_options(
        self,
        model_service_name: str,
        request: agent_run_20250910_models.UpdateModelServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateModelServiceResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelServiceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services/{OpenApiUtilClient.get_encode_param(model_service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_service_with_options_async(
        self,
        model_service_name: str,
        request: agent_run_20250910_models.UpdateModelServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateModelServiceResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelServiceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateModelService',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/agents/model-services/{OpenApiUtilClient.get_encode_param(model_service_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateModelServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_service(
        self,
        model_service_name: str,
        request: agent_run_20250910_models.UpdateModelServiceRequest,
    ) -> agent_run_20250910_models.UpdateModelServiceResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelServiceRequest
        @return: UpdateModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_service_with_options(model_service_name, request, headers, runtime)

    async def update_model_service_async(
        self,
        model_service_name: str,
        request: agent_run_20250910_models.UpdateModelServiceRequest,
    ) -> agent_run_20250910_models.UpdateModelServiceResponse:
        """
        @summary 更新模型
        
        @param request: UpdateModelServiceRequest
        @return: UpdateModelServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_service_with_options_async(model_service_name, request, headers, runtime)

    def update_template_with_options(
        self,
        template_name: str,
        request: agent_run_20250910_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateTemplateResponse:
        """
        @summary 更新模板
        
        @description 更新指定模板的配置信息，包括资源配置、网络配置、环境变量等。
        
        @param request: UpdateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        template_name: str,
        request: agent_run_20250910_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> agent_run_20250910_models.UpdateTemplateResponse:
        """
        @summary 更新模板
        
        @description 更新指定模板的配置信息，包括资源配置、网络配置、环境变量等。
        
        @param request: UpdateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2025-09-10',
            protocol='HTTPS',
            pathname=f'/2025-09-10/templates/{OpenApiUtilClient.get_encode_param(template_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            agent_run_20250910_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        template_name: str,
        request: agent_run_20250910_models.UpdateTemplateRequest,
    ) -> agent_run_20250910_models.UpdateTemplateResponse:
        """
        @summary 更新模板
        
        @description 更新指定模板的配置信息，包括资源配置、网络配置、环境变量等。
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_name, request, headers, runtime)

    async def update_template_async(
        self,
        template_name: str,
        request: agent_run_20250910_models.UpdateTemplateRequest,
    ) -> agent_run_20250910_models.UpdateTemplateResponse:
        """
        @summary 更新模板
        
        @description 更新指定模板的配置信息，包括资源配置、网络配置、环境变量等。
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(template_name, request, headers, runtime)
