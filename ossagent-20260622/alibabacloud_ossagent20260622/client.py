# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_ossagent20260622 import models as main_models
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
        self._endpoint = self.get_endpoint('ossagent', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/stream',
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
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/stream',
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
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        request: main_models.ChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
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
        headers = {}
        return self.chat_with_options(request, headers, runtime)

    async def chat_async(
        self,
        request: main_models.ChatRequest,
    ) -> main_models.ChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.chat_with_options_async(request, headers, runtime)

    def confirm_with_sse(
        self,
        request: main_models.ConfirmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ConfirmResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.confirmed):
            body['confirmed'] = request.confirmed
        if not DaraCore.is_null(request.phase):
            body['phase'] = request.phase
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tool_calls):
            body['toolCalls'] = request.tool_calls
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Confirm',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/confirm',
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
                    main_models.ConfirmResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def confirm_with_sse_async(
        self,
        request: main_models.ConfirmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ConfirmResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.confirmed):
            body['confirmed'] = request.confirmed
        if not DaraCore.is_null(request.phase):
            body['phase'] = request.phase
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tool_calls):
            body['toolCalls'] = request.tool_calls
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Confirm',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/confirm',
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
                    main_models.ConfirmResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def confirm_with_options(
        self,
        request: main_models.ConfirmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.confirmed):
            body['confirmed'] = request.confirmed
        if not DaraCore.is_null(request.phase):
            body['phase'] = request.phase
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tool_calls):
            body['toolCalls'] = request.tool_calls
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Confirm',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/confirm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_with_options_async(
        self,
        request: main_models.ConfirmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.confirmed):
            body['confirmed'] = request.confirmed
        if not DaraCore.is_null(request.phase):
            body['phase'] = request.phase
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.tool_calls):
            body['toolCalls'] = request.tool_calls
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Confirm',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/confirm',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm(
        self,
        request: main_models.ConfirmRequest,
    ) -> main_models.ConfirmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.confirm_with_options(request, headers, runtime)

    async def confirm_async(
        self,
        request: main_models.ConfirmRequest,
    ) -> main_models.ConfirmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.confirm_with_options_async(request, headers, runtime)

    def interrupt_with_options(
        self,
        session_id: str,
        request: main_models.InterruptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InterruptResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'Interrupt',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/interrupt/{DaraURL.percent_encode(session_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.InterruptResponse(),
            self.call_api(params, req, runtime)
        )

    async def interrupt_with_options_async(
        self,
        session_id: str,
        request: main_models.InterruptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InterruptResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'Interrupt',
            version = '2026-06-22',
            protocol = 'HTTPS',
            pathname = f'/api/chat/interrupt/{DaraURL.percent_encode(session_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.InterruptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def interrupt(
        self,
        session_id: str,
        request: main_models.InterruptRequest,
    ) -> main_models.InterruptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.interrupt_with_options(session_id, request, headers, runtime)

    async def interrupt_async(
        self,
        session_id: str,
        request: main_models.InterruptRequest,
    ) -> main_models.InterruptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.interrupt_with_options_async(session_id, request, headers, runtime)
