# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_openagent20260801 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('openagent', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_run_with_options(
        self,
        session_id: str,
        run_id: str,
        request: main_models.CancelRunRequest,
        headers: main_models.CancelRunHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelRun',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/runs/{DaraURL.percent_encode(run_id)}/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_run_with_options_async(
        self,
        session_id: str,
        run_id: str,
        request: main_models.CancelRunRequest,
        headers: main_models.CancelRunHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.reason):
            body['reason'] = request.reason
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelRun',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/runs/{DaraURL.percent_encode(run_id)}/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_run(
        self,
        session_id: str,
        run_id: str,
        request: main_models.CancelRunRequest,
    ) -> main_models.CancelRunResponse:
        runtime = RuntimeOptions()
        headers = main_models.CancelRunHeaders()
        return self.cancel_run_with_options(session_id, run_id, request, headers, runtime)

    async def cancel_run_async(
        self,
        session_id: str,
        run_id: str,
        request: main_models.CancelRunRequest,
    ) -> main_models.CancelRunResponse:
        runtime = RuntimeOptions()
        headers = main_models.CancelRunHeaders()
        return await self.cancel_run_with_options_async(session_id, run_id, request, headers, runtime)

    def create_session_with_options(
        self,
        request: main_models.CreateSessionRequest,
        headers: main_models.CreateSessionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions',
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
        headers: main_models.CreateSessionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions',
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
        headers = main_models.CreateSessionHeaders()
        return self.create_session_with_options(request, headers, runtime)

    async def create_session_async(
        self,
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateSessionHeaders()
        return await self.create_session_with_options_async(request, headers, runtime)

    def delete_session_with_options(
        self,
        session_id: str,
        request: main_models.DeleteSessionRequest,
        headers: main_models.DeleteSessionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSession',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}',
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
        headers: main_models.DeleteSessionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSession',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}',
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
        headers = main_models.DeleteSessionHeaders()
        return self.delete_session_with_options(session_id, request, headers, runtime)

    async def delete_session_async(
        self,
        session_id: str,
        request: main_models.DeleteSessionRequest,
    ) -> main_models.DeleteSessionResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSessionHeaders()
        return await self.delete_session_with_options_async(session_id, request, headers, runtime)

    def get_readonly_mode_with_options(
        self,
        request: main_models.GetReadonlyModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReadonlyModeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetReadonlyMode',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/user/configs/readonly',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReadonlyModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_readonly_mode_with_options_async(
        self,
        request: main_models.GetReadonlyModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReadonlyModeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetReadonlyMode',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/user/configs/readonly',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReadonlyModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_readonly_mode(
        self,
        request: main_models.GetReadonlyModeRequest,
    ) -> main_models.GetReadonlyModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_readonly_mode_with_options(request, headers, runtime)

    async def get_readonly_mode_async(
        self,
        request: main_models.GetReadonlyModeRequest,
    ) -> main_models.GetReadonlyModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_readonly_mode_with_options_async(request, headers, runtime)

    def get_run_with_options(
        self,
        session_id: str,
        run_id: str,
        request: main_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRun',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/runs/{DaraURL.percent_encode(run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_with_options_async(
        self,
        session_id: str,
        run_id: str,
        request: main_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRun',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/runs/{DaraURL.percent_encode(run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run(
        self,
        session_id: str,
        run_id: str,
        request: main_models.GetRunRequest,
    ) -> main_models.GetRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_run_with_options(session_id, run_id, request, headers, runtime)

    async def get_run_async(
        self,
        session_id: str,
        run_id: str,
        request: main_models.GetRunRequest,
    ) -> main_models.GetRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_run_with_options_async(session_id, run_id, request, headers, runtime)

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
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}',
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
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}',
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

    def list_messages_with_options(
        self,
        session_id: str,
        request: main_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.run_id):
            query['runId'] = request.run_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessages',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        session_id: str,
        request: main_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.run_id):
            query['runId'] = request.run_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessages',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        session_id: str,
        request: main_models.ListMessagesRequest,
    ) -> main_models.ListMessagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(session_id, request, headers, runtime)

    async def list_messages_async(
        self,
        session_id: str,
        request: main_models.ListMessagesRequest,
    ) -> main_models.ListMessagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_messages_with_options_async(session_id, request, headers, runtime)

    def list_sessions_with_options(
        self,
        request: main_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessions',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions',
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
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessions',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions',
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

    def send_message_with_sse(
        self,
        session_id: str,
        request: main_models.SendMessageRequest,
        headers: main_models.SendMessageHeaders,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.SendMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.resume):
            body['resume'] = request.resume
        if not DaraCore.is_null(request.run_id):
            body['runId'] = request.run_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/messages',
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
                    main_models.SendMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def send_message_with_sse_async(
        self,
        session_id: str,
        request: main_models.SendMessageRequest,
        headers: main_models.SendMessageHeaders,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.SendMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.resume):
            body['resume'] = request.resume
        if not DaraCore.is_null(request.run_id):
            body['runId'] = request.run_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/messages',
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
                    main_models.SendMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def send_message_with_options(
        self,
        session_id: str,
        request: main_models.SendMessageRequest,
        headers: main_models.SendMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.resume):
            body['resume'] = request.resume
        if not DaraCore.is_null(request.run_id):
            body['runId'] = request.run_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        session_id: str,
        request: main_models.SendMessageRequest,
        headers: main_models.SendMessageHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.resume):
            body['resume'] = request.resume
        if not DaraCore.is_null(request.run_id):
            body['runId'] = request.run_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        session_id: str,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.SendMessageHeaders()
        return self.send_message_with_options(session_id, request, headers, runtime)

    async def send_message_async(
        self,
        session_id: str,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        headers = main_models.SendMessageHeaders()
        return await self.send_message_with_options_async(session_id, request, headers, runtime)

    def update_readonly_mode_with_options(
        self,
        request: main_models.UpdateReadonlyModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateReadonlyModeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateReadonlyMode',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/user/configs/readonly',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateReadonlyModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_readonly_mode_with_options_async(
        self,
        request: main_models.UpdateReadonlyModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateReadonlyModeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateReadonlyMode',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/user/configs/readonly',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateReadonlyModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_readonly_mode(
        self,
        request: main_models.UpdateReadonlyModeRequest,
    ) -> main_models.UpdateReadonlyModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_readonly_mode_with_options(request, headers, runtime)

    async def update_readonly_mode_async(
        self,
        request: main_models.UpdateReadonlyModeRequest,
    ) -> main_models.UpdateReadonlyModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_readonly_mode_with_options_async(request, headers, runtime)

    def update_session_with_options(
        self,
        session_id: str,
        request: main_models.UpdateSessionRequest,
        headers: main_models.UpdateSessionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.pinned):
            body['pinned'] = request.pinned
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSession',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'PATCH',
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
        session_id: str,
        request: main_models.UpdateSessionRequest,
        headers: main_models.UpdateSessionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.pinned):
            body['pinned'] = request.pinned
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_open_agent_idempotency_key):
            real_headers['X-OpenAgent-Idempotency-Key'] = str(headers.x_open_agent_idempotency_key)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSession',
            version = '2026-08-01',
            protocol = 'HTTPS',
            pathname = f'/openapi/v1/agent/sessions/{DaraURL.percent_encode(session_id)}',
            method = 'PATCH',
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
        session_id: str,
        request: main_models.UpdateSessionRequest,
    ) -> main_models.UpdateSessionResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateSessionHeaders()
        return self.update_session_with_options(session_id, request, headers, runtime)

    async def update_session_async(
        self,
        session_id: str,
        request: main_models.UpdateSessionRequest,
    ) -> main_models.UpdateSessionResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateSessionHeaders()
        return await self.update_session_with_options_async(session_id, request, headers, runtime)
