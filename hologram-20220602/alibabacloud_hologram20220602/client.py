# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_hologram20220602 import models as main_models
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
        self._endpoint = self.get_endpoint('hologram', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_agent_session_with_options(
        self,
        tmp_req: main_models.CreateAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSession',
            version = '2022-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_session_with_options_async(
        self,
        tmp_req: main_models.CreateAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSession',
            version = '2022-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_session(
        self,
        request: main_models.CreateAgentSessionRequest,
    ) -> main_models.CreateAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.create_agent_session_with_options(request, runtime)

    async def create_agent_session_async(
        self,
        request: main_models.CreateAgentSessionRequest,
    ) -> main_models.CreateAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_session_with_options_async(request, runtime)

    def prompt_agent_session_with_sse(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.PromptAgentSessionResponse, None, None]:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.caller_context):
            body['Caller-Context'] = request.caller_context
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2022-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.PromptAgentSessionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def prompt_agent_session_with_sse_async(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.PromptAgentSessionResponse, None, None]:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.caller_context):
            body['Caller-Context'] = request.caller_context
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2022-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.PromptAgentSessionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def prompt_agent_session_with_options(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromptAgentSessionResponse:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.caller_context):
            body['Caller-Context'] = request.caller_context
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2022-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromptAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def prompt_agent_session_with_options_async(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromptAgentSessionResponse:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.caller_context):
            body['Caller-Context'] = request.caller_context
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2022-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromptAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def prompt_agent_session(
        self,
        request: main_models.PromptAgentSessionRequest,
    ) -> main_models.PromptAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.prompt_agent_session_with_options(request, runtime)

    async def prompt_agent_session_async(
        self,
        request: main_models.PromptAgentSessionRequest,
    ) -> main_models.PromptAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.prompt_agent_session_with_options_async(request, runtime)
