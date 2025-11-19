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
