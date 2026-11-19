# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_qwenb2bchat20261105 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_tea_openapi.websocket_utils import Client as WebSocketUtilsClient
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
        self._product_id = 'QwenB2BChat'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('qwenb2bchat', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def chat_with_sse(
        self,
        request: main_models.ChatRequest,
        headers: main_models.ChatHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept):
            real_headers['Accept'] = str(headers.accept)
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-11-05',
            protocol = 'HTTPS',
            pathname = f'/v1/api/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def chat_with_sse_async(
        self,
        request: main_models.ChatRequest,
        headers: main_models.ChatHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept):
            real_headers['Accept'] = str(headers.accept)
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-11-05',
            protocol = 'HTTPS',
            pathname = f'/v1/api/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def chat_with_options(
        self,
        request: main_models.ChatRequest,
        headers: main_models.ChatHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept):
            real_headers['Accept'] = str(headers.accept)
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-11-05',
            protocol = 'HTTPS',
            pathname = f'/v1/api/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        request: main_models.ChatRequest,
        headers: main_models.ChatHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept):
            real_headers['Accept'] = str(headers.accept)
        if not DaraCore.is_null(headers.x_dash_scope_sse):
            real_headers['X-DashScope-SSE'] = str(headers.x_dash_scope_sse)
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-11-05',
            protocol = 'HTTPS',
            pathname = f'/v1/api/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat(
        self,
        request: main_models.ChatRequest,
    ) -> main_models.ChatResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChatHeaders()
        return self.chat_with_options(request, headers, runtime)

    async def chat_async(
        self,
        request: main_models.ChatRequest,
    ) -> main_models.ChatResponse:
        runtime = RuntimeOptions()
        headers = main_models.ChatHeaders()
        return await self.chat_with_options_async(request, headers, runtime)

    def open_service_with_options(
        self,
        request: main_models.OpenServiceRequest,
        headers: main_models.OpenServiceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OpenServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.open_benefits):
            body['openBenefits'] = request.open_benefits
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenService',
            version = '2026-11-05',
            protocol = 'HTTPS',
            pathname = f'/v1/api/openService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_service_with_options_async(
        self,
        request: main_models.OpenServiceRequest,
        headers: main_models.OpenServiceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.OpenServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.communication):
            body['communication'] = request.communication
        if not DaraCore.is_null(request.open_benefits):
            body['openBenefits'] = request.open_benefits
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenService',
            version = '2026-11-05',
            protocol = 'HTTPS',
            pathname = f'/v1/api/openService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_service(
        self,
        request: main_models.OpenServiceRequest,
    ) -> main_models.OpenServiceResponse:
        runtime = RuntimeOptions()
        headers = main_models.OpenServiceHeaders()
        return self.open_service_with_options(request, headers, runtime)

    async def open_service_async(
        self,
        request: main_models.OpenServiceRequest,
    ) -> main_models.OpenServiceResponse:
        runtime = RuntimeOptions()
        headers = main_models.OpenServiceHeaders()
        return await self.open_service_with_options_async(request, headers, runtime)

    def stream_voice_with_options(
        self,
        request: main_models.StreamVoiceRequest,
        headers: main_models.StreamVoiceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StreamVoiceResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StreamVoice',
            version = '2026-11-05',
            protocol = 'wss',
            pathname = f'/v1/api/voice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json',
            websocket_sub_protocol = 'general'
        )
        res = main_models.StreamVoiceResponse()
        tmp = self.call_api(params, req, runtime)
        if not DaraCore.is_null(tmp.get('webSocketClient')):
            res.web_socket_client = WebSocketUtilsClient.create_web_socket_client(tmp.get('webSocketClient'))
        return res

    async def stream_voice_with_options_async(
        self,
        request: main_models.StreamVoiceRequest,
        headers: main_models.StreamVoiceHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StreamVoiceResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_gwaccess):
            real_headers['X-GW-Access'] = str(headers.x_gwaccess)
        if not DaraCore.is_null(headers.x_gwnonce):
            real_headers['X-GW-Nonce'] = str(headers.x_gwnonce)
        if not DaraCore.is_null(headers.x_gwprotocol):
            real_headers['X-GW-Protocol'] = str(headers.x_gwprotocol)
        if not DaraCore.is_null(headers.x_gwsignature):
            real_headers['X-GW-Signature'] = str(headers.x_gwsignature)
        if not DaraCore.is_null(headers.x_gwtimestamp):
            real_headers['X-GW-Timestamp'] = str(headers.x_gwtimestamp)
        if not DaraCore.is_null(headers.x_request_id):
            real_headers['X-Request-Id'] = str(headers.x_request_id)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StreamVoice',
            version = '2026-11-05',
            protocol = 'wss',
            pathname = f'/v1/api/voice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json',
            websocket_sub_protocol = 'general'
        )
        res = main_models.StreamVoiceResponse()
        tmp = await self.call_api_async(params, req, runtime)
        if not DaraCore.is_null(tmp.get('webSocketClient')):
            res.web_socket_client = WebSocketUtilsClient.create_web_socket_client(tmp.get('webSocketClient'))
        return res

    def stream_voice(
        self,
        request: main_models.StreamVoiceRequest,
    ) -> main_models.StreamVoiceResponse:
        runtime = RuntimeOptions()
        headers = main_models.StreamVoiceHeaders()
        return self.stream_voice_with_options(request, headers, runtime)

    async def stream_voice_async(
        self,
        request: main_models.StreamVoiceRequest,
    ) -> main_models.StreamVoiceResponse:
        runtime = RuntimeOptions()
        headers = main_models.StreamVoiceHeaders()
        return await self.stream_voice_with_options_async(request, headers, runtime)
