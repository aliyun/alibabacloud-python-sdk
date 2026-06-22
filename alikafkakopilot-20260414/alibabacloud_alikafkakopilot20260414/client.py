# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_alikafkakopilot20260414 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('alikafkakopilot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def kopilot_chat_stream_with_sse(
        self,
        request: main_models.KopilotChatStreamRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.KopilotChatStreamResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotChatStream',
            version = '2026-04-14',
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
                    main_models.KopilotChatStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def kopilot_chat_stream_with_sse_async(
        self,
        request: main_models.KopilotChatStreamRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.KopilotChatStreamResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotChatStream',
            version = '2026-04-14',
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
                    main_models.KopilotChatStreamResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def kopilot_chat_stream_with_options(
        self,
        request: main_models.KopilotChatStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotChatStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotChatStream',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotChatStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def kopilot_chat_stream_with_options_async(
        self,
        request: main_models.KopilotChatStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotChatStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotChatStream',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotChatStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kopilot_chat_stream(
        self,
        request: main_models.KopilotChatStreamRequest,
    ) -> main_models.KopilotChatStreamResponse:
        runtime = RuntimeOptions()
        return self.kopilot_chat_stream_with_options(request, runtime)

    async def kopilot_chat_stream_async(
        self,
        request: main_models.KopilotChatStreamRequest,
    ) -> main_models.KopilotChatStreamResponse:
        runtime = RuntimeOptions()
        return await self.kopilot_chat_stream_with_options_async(request, runtime)

    def kopilot_feedback_with_options(
        self,
        request: main_models.KopilotFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.turn_id):
            query['TurnId'] = request.turn_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotFeedback',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def kopilot_feedback_with_options_async(
        self,
        request: main_models.KopilotFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.turn_id):
            query['TurnId'] = request.turn_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotFeedback',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kopilot_feedback(
        self,
        request: main_models.KopilotFeedbackRequest,
    ) -> main_models.KopilotFeedbackResponse:
        runtime = RuntimeOptions()
        return self.kopilot_feedback_with_options(request, runtime)

    async def kopilot_feedback_async(
        self,
        request: main_models.KopilotFeedbackRequest,
    ) -> main_models.KopilotFeedbackResponse:
        runtime = RuntimeOptions()
        return await self.kopilot_feedback_with_options_async(request, runtime)

    def kopilot_list_conversation_chat_messages_with_options(
        self,
        request: main_models.KopilotListConversationChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotListConversationChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.before_turn_id):
            query['BeforeTurnId'] = request.before_turn_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotListConversationChatMessages',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotListConversationChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def kopilot_list_conversation_chat_messages_with_options_async(
        self,
        request: main_models.KopilotListConversationChatMessagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotListConversationChatMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.before_turn_id):
            query['BeforeTurnId'] = request.before_turn_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotListConversationChatMessages',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotListConversationChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kopilot_list_conversation_chat_messages(
        self,
        request: main_models.KopilotListConversationChatMessagesRequest,
    ) -> main_models.KopilotListConversationChatMessagesResponse:
        runtime = RuntimeOptions()
        return self.kopilot_list_conversation_chat_messages_with_options(request, runtime)

    async def kopilot_list_conversation_chat_messages_async(
        self,
        request: main_models.KopilotListConversationChatMessagesRequest,
    ) -> main_models.KopilotListConversationChatMessagesResponse:
        runtime = RuntimeOptions()
        return await self.kopilot_list_conversation_chat_messages_with_options_async(request, runtime)

    def kopilot_list_conversations_with_options(
        self,
        request: main_models.KopilotListConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotListConversationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotListConversations',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotListConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def kopilot_list_conversations_with_options_async(
        self,
        request: main_models.KopilotListConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotListConversationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotListConversations',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotListConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kopilot_list_conversations(
        self,
        request: main_models.KopilotListConversationsRequest,
    ) -> main_models.KopilotListConversationsResponse:
        runtime = RuntimeOptions()
        return self.kopilot_list_conversations_with_options(request, runtime)

    async def kopilot_list_conversations_async(
        self,
        request: main_models.KopilotListConversationsRequest,
    ) -> main_models.KopilotListConversationsResponse:
        runtime = RuntimeOptions()
        return await self.kopilot_list_conversations_with_options_async(request, runtime)

    def kopilot_query_status_with_options(
        self,
        request: main_models.KopilotQueryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotQueryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotQueryStatus',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotQueryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def kopilot_query_status_with_options_async(
        self,
        request: main_models.KopilotQueryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KopilotQueryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KopilotQueryStatus',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KopilotQueryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kopilot_query_status(
        self,
        request: main_models.KopilotQueryStatusRequest,
    ) -> main_models.KopilotQueryStatusResponse:
        runtime = RuntimeOptions()
        return self.kopilot_query_status_with_options(request, runtime)

    async def kopilot_query_status_async(
        self,
        request: main_models.KopilotQueryStatusRequest,
    ) -> main_models.KopilotQueryStatusResponse:
        runtime = RuntimeOptions()
        return await self.kopilot_query_status_with_options_async(request, runtime)
