# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_searchagent20260515 import models as main_models
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
        self._product_id = 'SearchAgent'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''

    def execute_acp_command_with_options(
        self,
        workspace_name: str,
        request: main_models.ExecuteAcpCommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAcpCommandResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAcpCommand',
            version = '2026-05-15',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/agent/acp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAcpCommandResponse(),
            self.execute(params, req, runtime)
        )

    async def execute_acp_command_with_options_async(
        self,
        workspace_name: str,
        request: main_models.ExecuteAcpCommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAcpCommandResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAcpCommand',
            version = '2026-05-15',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/agent/acp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAcpCommandResponse(),
            await self.execute_async(params, req, runtime)
        )

    def execute_acp_command(
        self,
        workspace_name: str,
        request: main_models.ExecuteAcpCommandRequest,
    ) -> main_models.ExecuteAcpCommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_acp_command_with_options(workspace_name, request, headers, runtime)

    async def execute_acp_command_async(
        self,
        workspace_name: str,
        request: main_models.ExecuteAcpCommandRequest,
    ) -> main_models.ExecuteAcpCommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_acp_command_with_options_async(workspace_name, request, headers, runtime)

    def generate_acp_completion_with_sse(
        self,
        workspace_name: str,
        request: main_models.GenerateAcpCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.GenerateAcpCompletionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAcpCompletion',
            version = '2026-05-15',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/agent/acp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.GenerateAcpCompletionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def generate_acp_completion_with_sse_async(
        self,
        workspace_name: str,
        request: main_models.GenerateAcpCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.GenerateAcpCompletionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAcpCompletion',
            version = '2026-05-15',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/agent/acp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.GenerateAcpCompletionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def generate_acp_completion_with_options(
        self,
        workspace_name: str,
        request: main_models.GenerateAcpCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAcpCompletionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAcpCompletion',
            version = '2026-05-15',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/agent/acp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.GenerateAcpCompletionResponse(),
            self.execute(params, req, runtime)
        )

    async def generate_acp_completion_with_options_async(
        self,
        workspace_name: str,
        request: main_models.GenerateAcpCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAcpCompletionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAcpCompletion',
            version = '2026-05-15',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/agent/acp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.GenerateAcpCompletionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def generate_acp_completion(
        self,
        workspace_name: str,
        request: main_models.GenerateAcpCompletionRequest,
    ) -> main_models.GenerateAcpCompletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_acp_completion_with_options(workspace_name, request, headers, runtime)

    async def generate_acp_completion_async(
        self,
        workspace_name: str,
        request: main_models.GenerateAcpCompletionRequest,
    ) -> main_models.GenerateAcpCompletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_acp_completion_with_options_async(workspace_name, request, headers, runtime)
