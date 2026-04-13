# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_paicopilot20250731 import models as main_models
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
        self._endpoint = self.get_endpoint('paicopilot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_chat_with_sse(
        self,
        session_id: str,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.CreateChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.question):
            body['Question'] = request.question
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats',
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
                    main_models.CreateChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def create_chat_with_sse_async(
        self,
        session_id: str,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.CreateChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.question):
            body['Question'] = request.question
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats',
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
                    main_models.CreateChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def create_chat_with_options(
        self,
        session_id: str,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.question):
            body['Question'] = request.question
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_with_options_async(
        self,
        session_id: str,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.question):
            body['Question'] = request.question
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat(
        self,
        session_id: str,
        request: main_models.CreateChatRequest,
    ) -> main_models.CreateChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_chat_with_options(session_id, request, headers, runtime)

    async def create_chat_async(
        self,
        session_id: str,
        request: main_models.CreateChatRequest,
    ) -> main_models.CreateChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_chat_with_options_async(session_id, request, headers, runtime)

    def create_session_with_options(
        self,
        request: main_models.CreateSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions',
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
        request: main_models.CreateSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions',
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
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_session_with_options(request, headers, runtime)

    async def create_session_async(
        self,
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_session_with_options_async(request, headers, runtime)

    def delete_chat_with_options(
        self,
        session_id: str,
        chat_id: str,
        request: main_models.DeleteChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats/{DaraURL.percent_encode(chat_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_with_options_async(
        self,
        session_id: str,
        chat_id: str,
        request: main_models.DeleteChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats/{DaraURL.percent_encode(chat_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat(
        self,
        session_id: str,
        chat_id: str,
        request: main_models.DeleteChatRequest,
    ) -> main_models.DeleteChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_chat_with_options(session_id, chat_id, request, headers, runtime)

    async def delete_chat_async(
        self,
        session_id: str,
        chat_id: str,
        request: main_models.DeleteChatRequest,
    ) -> main_models.DeleteChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_chat_with_options_async(session_id, chat_id, request, headers, runtime)

    def delete_session_with_options(
        self,
        session_id: str,
        request: main_models.DeleteSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSession',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_session_with_options_async(
        self,
        session_id: str,
        request: main_models.DeleteSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSession',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_session(
        self,
        session_id: str,
        request: main_models.DeleteSessionRequest,
    ) -> main_models.DeleteSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_session_with_options(session_id, request, headers, runtime)

    async def delete_session_async(
        self,
        session_id: str,
        request: main_models.DeleteSessionRequest,
    ) -> main_models.DeleteSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_session_with_options_async(session_id, request, headers, runtime)

    def get_chat_with_options(
        self,
        chat_id: str,
        session_id: str,
        request: main_models.GetChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats/{DaraURL.percent_encode(chat_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_with_options_async(
        self,
        chat_id: str,
        session_id: str,
        request: main_models.GetChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChat',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats/{DaraURL.percent_encode(chat_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat(
        self,
        chat_id: str,
        session_id: str,
        request: main_models.GetChatRequest,
    ) -> main_models.GetChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_chat_with_options(chat_id, session_id, request, headers, runtime)

    async def get_chat_async(
        self,
        chat_id: str,
        session_id: str,
        request: main_models.GetChatRequest,
    ) -> main_models.GetChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_chat_with_options_async(chat_id, session_id, request, headers, runtime)

    def get_session_with_options(
        self,
        session_id: str,
        request: main_models.GetSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSession',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}',
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
        session_id: str,
        request: main_models.GetSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSession',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}',
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
        session_id: str,
        request: main_models.GetSessionRequest,
    ) -> main_models.GetSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_session_with_options(session_id, request, headers, runtime)

    async def get_session_async(
        self,
        session_id: str,
        request: main_models.GetSessionRequest,
    ) -> main_models.GetSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_session_with_options_async(session_id, request, headers, runtime)

    def list_chats_with_options(
        self,
        session_id: str,
        request: main_models.ListChatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChats',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chats_with_options_async(
        self,
        session_id: str,
        request: main_models.ListChatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChats',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions/{DaraURL.percent_encode(session_id)}/chats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chats(
        self,
        session_id: str,
        request: main_models.ListChatsRequest,
    ) -> main_models.ListChatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_chats_with_options(session_id, request, headers, runtime)

    async def list_chats_async(
        self,
        session_id: str,
        request: main_models.ListChatsRequest,
    ) -> main_models.ListChatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_chats_with_options_async(session_id, request, headers, runtime)

    def list_sessions_with_options(
        self,
        request: main_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessions',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions',
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
        request: main_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessions',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sessions',
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
        request: main_models.ListSessionsRequest,
    ) -> main_models.ListSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sessions_with_options(request, headers, runtime)

    async def list_sessions_async(
        self,
        request: main_models.ListSessionsRequest,
    ) -> main_models.ListSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sessions_with_options_async(request, headers, runtime)

    def search_info_with_options(
        self,
        request: main_models.SearchInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.knowledge_base_filters):
            body['KnowledgeBaseFilters'] = request.knowledge_base_filters
        if not DaraCore.is_null(request.web_filters):
            body['WebFilters'] = request.web_filters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchInfo',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/searches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_info_with_options_async(
        self,
        request: main_models.SearchInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.knowledge_base_filters):
            body['KnowledgeBaseFilters'] = request.knowledge_base_filters
        if not DaraCore.is_null(request.web_filters):
            body['WebFilters'] = request.web_filters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchInfo',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/searches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_info(
        self,
        request: main_models.SearchInfoRequest,
    ) -> main_models.SearchInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_info_with_options(request, headers, runtime)

    async def search_info_async(
        self,
        request: main_models.SearchInfoRequest,
    ) -> main_models.SearchInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_info_with_options_async(request, headers, runtime)
