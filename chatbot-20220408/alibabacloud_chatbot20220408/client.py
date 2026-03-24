# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_chatbot20220408 import models as main_models
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
        self._endpoint = self.get_endpoint('chatbot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_for_stream_access_token_with_options(
        self,
        request: main_models.ApplyForStreamAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyForStreamAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyForStreamAccessToken',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyForStreamAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_for_stream_access_token_with_options_async(
        self,
        request: main_models.ApplyForStreamAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyForStreamAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyForStreamAccessToken',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyForStreamAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_for_stream_access_token(
        self,
        request: main_models.ApplyForStreamAccessTokenRequest,
    ) -> main_models.ApplyForStreamAccessTokenResponse:
        runtime = RuntimeOptions()
        return self.apply_for_stream_access_token_with_options(request, runtime)

    async def apply_for_stream_access_token_async(
        self,
        request: main_models.ApplyForStreamAccessTokenRequest,
    ) -> main_models.ApplyForStreamAccessTokenResponse:
        runtime = RuntimeOptions()
        return await self.apply_for_stream_access_token_with_options_async(request, runtime)

    def associate_with_options(
        self,
        tmp_req: main_models.AssociateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResponse:
        tmp_req.validate()
        request = main_models.AssociateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.perspective):
            request.perspective_shrink = Utils.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
        if not DaraCore.is_null(request.recommend_num):
            query['RecommendNum'] = request.recommend_num
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Associate',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_with_options_async(
        self,
        tmp_req: main_models.AssociateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResponse:
        tmp_req.validate()
        request = main_models.AssociateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.perspective):
            request.perspective_shrink = Utils.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
        if not DaraCore.is_null(request.recommend_num):
            query['RecommendNum'] = request.recommend_num
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Associate',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate(
        self,
        request: main_models.AssociateRequest,
    ) -> main_models.AssociateResponse:
        runtime = RuntimeOptions()
        return self.associate_with_options(request, runtime)

    async def associate_async(
        self,
        request: main_models.AssociateRequest,
    ) -> main_models.AssociateResponse:
        runtime = RuntimeOptions()
        return await self.associate_with_options_async(request, runtime)

    def begin_session_with_options(
        self,
        request: main_models.BeginSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BeginSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sand_box):
            body['SandBox'] = request.sand_box
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.vendor_param):
            body['VendorParam'] = request.vendor_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BeginSession',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BeginSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def begin_session_with_options_async(
        self,
        request: main_models.BeginSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BeginSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sand_box):
            body['SandBox'] = request.sand_box
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.vendor_param):
            body['VendorParam'] = request.vendor_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BeginSession',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BeginSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def begin_session(
        self,
        request: main_models.BeginSessionRequest,
    ) -> main_models.BeginSessionResponse:
        runtime = RuntimeOptions()
        return self.begin_session_with_options(request, runtime)

    async def begin_session_async(
        self,
        request: main_models.BeginSessionRequest,
    ) -> main_models.BeginSessionResponse:
        runtime = RuntimeOptions()
        return await self.begin_session_with_options_async(request, runtime)

    def cancel_chat_with_options(
        self,
        request: main_models.CancelChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.answer):
            body['Answer'] = request.answer
        if not DaraCore.is_null(request.chat_id):
            body['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelChat',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_chat_with_options_async(
        self,
        request: main_models.CancelChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.answer):
            body['Answer'] = request.answer
        if not DaraCore.is_null(request.chat_id):
            body['ChatId'] = request.chat_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelChat',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_chat(
        self,
        request: main_models.CancelChatRequest,
    ) -> main_models.CancelChatResponse:
        runtime = RuntimeOptions()
        return self.cancel_chat_with_options(request, runtime)

    async def cancel_chat_async(
        self,
        request: main_models.CancelChatRequest,
    ) -> main_models.CancelChatResponse:
        runtime = RuntimeOptions()
        return await self.cancel_chat_with_options_async(request, runtime)

    def cancel_instance_publish_task_with_options(
        self,
        request: main_models.CancelInstancePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelInstancePublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelInstancePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelInstancePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_instance_publish_task_with_options_async(
        self,
        request: main_models.CancelInstancePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelInstancePublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelInstancePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelInstancePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_instance_publish_task(
        self,
        request: main_models.CancelInstancePublishTaskRequest,
    ) -> main_models.CancelInstancePublishTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_instance_publish_task_with_options(request, runtime)

    async def cancel_instance_publish_task_async(
        self,
        request: main_models.CancelInstancePublishTaskRequest,
    ) -> main_models.CancelInstancePublishTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_instance_publish_task_with_options_async(request, runtime)

    def cancel_publish_task_with_options(
        self,
        request: main_models.CancelPublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_publish_task_with_options_async(
        self,
        request: main_models.CancelPublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_publish_task(
        self,
        request: main_models.CancelPublishTaskRequest,
    ) -> main_models.CancelPublishTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_publish_task_with_options(request, runtime)

    async def cancel_publish_task_async(
        self,
        request: main_models.CancelPublishTaskRequest,
    ) -> main_models.CancelPublishTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_publish_task_with_options_async(request, runtime)

    def chat_with_options(
        self,
        tmp_req: main_models.ChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        tmp_req.validate()
        request = main_models.ChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.perspective):
            request.perspective_shrink = Utils.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
        if not DaraCore.is_null(request.sand_box):
            query['SandBox'] = request.sand_box
        if not DaraCore.is_null(request.sender_id):
            query['SenderId'] = request.sender_id
        if not DaraCore.is_null(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        if not DaraCore.is_null(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        tmp_req: main_models.ChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        tmp_req.validate()
        request = main_models.ChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.perspective):
            request.perspective_shrink = Utils.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
        if not DaraCore.is_null(request.sand_box):
            query['SandBox'] = request.sand_box
        if not DaraCore.is_null(request.sender_id):
            query['SenderId'] = request.sender_id
        if not DaraCore.is_null(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        if not DaraCore.is_null(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.chat_with_options(request, runtime)

    async def chat_async(
        self,
        request: main_models.ChatRequest,
    ) -> main_models.ChatResponse:
        runtime = RuntimeOptions()
        return await self.chat_with_options_async(request, runtime)

    def continue_instance_publish_task_with_options(
        self,
        request: main_models.ContinueInstancePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueInstancePublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueInstancePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueInstancePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_instance_publish_task_with_options_async(
        self,
        request: main_models.ContinueInstancePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueInstancePublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueInstancePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueInstancePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_instance_publish_task(
        self,
        request: main_models.ContinueInstancePublishTaskRequest,
    ) -> main_models.ContinueInstancePublishTaskResponse:
        runtime = RuntimeOptions()
        return self.continue_instance_publish_task_with_options(request, runtime)

    async def continue_instance_publish_task_async(
        self,
        request: main_models.ContinueInstancePublishTaskRequest,
    ) -> main_models.ContinueInstancePublishTaskResponse:
        runtime = RuntimeOptions()
        return await self.continue_instance_publish_task_with_options_async(request, runtime)

    def create_category_with_options(
        self,
        request: main_models.CreateCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.biz_code):
            body['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_category_with_options_async(
        self,
        request: main_models.CreateCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.biz_code):
            body['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_category(
        self,
        request: main_models.CreateCategoryRequest,
    ) -> main_models.CreateCategoryResponse:
        runtime = RuntimeOptions()
        return self.create_category_with_options(request, runtime)

    async def create_category_async(
        self,
        request: main_models.CreateCategoryRequest,
    ) -> main_models.CreateCategoryResponse:
        runtime = RuntimeOptions()
        return await self.create_category_with_options_async(request, runtime)

    def create_conn_question_with_options(
        self,
        request: main_models.CreateConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conn_question_with_options_async(
        self,
        request: main_models.CreateConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conn_question(
        self,
        request: main_models.CreateConnQuestionRequest,
    ) -> main_models.CreateConnQuestionResponse:
        runtime = RuntimeOptions()
        return self.create_conn_question_with_options(request, runtime)

    async def create_conn_question_async(
        self,
        request: main_models.CreateConnQuestionRequest,
    ) -> main_models.CreateConnQuestionResponse:
        runtime = RuntimeOptions()
        return await self.create_conn_question_with_options_async(request, runtime)

    def create_dsentity_with_options(
        self,
        request: main_models.CreateDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_name):
            query['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dsentity_with_options_async(
        self,
        request: main_models.CreateDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_name):
            query['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dsentity(
        self,
        request: main_models.CreateDSEntityRequest,
    ) -> main_models.CreateDSEntityResponse:
        runtime = RuntimeOptions()
        return self.create_dsentity_with_options(request, runtime)

    async def create_dsentity_async(
        self,
        request: main_models.CreateDSEntityRequest,
    ) -> main_models.CreateDSEntityResponse:
        runtime = RuntimeOptions()
        return await self.create_dsentity_with_options_async(request, runtime)

    def create_dsentity_value_with_options(
        self,
        tmp_req: main_models.CreateDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDSEntityValueResponse:
        tmp_req.validate()
        request = main_models.CreateDSEntityValueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.synonyms):
            request.synonyms_shrink = Utils.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dsentity_value_with_options_async(
        self,
        tmp_req: main_models.CreateDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDSEntityValueResponse:
        tmp_req.validate()
        request = main_models.CreateDSEntityValueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.synonyms):
            request.synonyms_shrink = Utils.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dsentity_value(
        self,
        request: main_models.CreateDSEntityValueRequest,
    ) -> main_models.CreateDSEntityValueResponse:
        runtime = RuntimeOptions()
        return self.create_dsentity_value_with_options(request, runtime)

    async def create_dsentity_value_async(
        self,
        request: main_models.CreateDSEntityValueRequest,
    ) -> main_models.CreateDSEntityValueResponse:
        runtime = RuntimeOptions()
        return await self.create_dsentity_value_with_options_async(request, runtime)

    def create_doc_with_options(
        self,
        tmp_req: main_models.CreateDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocResponse:
        tmp_req.validate()
        request = main_models.CreateDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_metadata):
            request.doc_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not DaraCore.is_null(tmp_req.tag_ids):
            request.tag_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.meta):
            query['Meta'] = request.meta
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_doc_with_options_async(
        self,
        tmp_req: main_models.CreateDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocResponse:
        tmp_req.validate()
        request = main_models.CreateDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_metadata):
            request.doc_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not DaraCore.is_null(tmp_req.tag_ids):
            request.tag_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.meta):
            query['Meta'] = request.meta
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_doc(
        self,
        request: main_models.CreateDocRequest,
    ) -> main_models.CreateDocResponse:
        runtime = RuntimeOptions()
        return self.create_doc_with_options(request, runtime)

    async def create_doc_async(
        self,
        request: main_models.CreateDocRequest,
    ) -> main_models.CreateDocResponse:
        runtime = RuntimeOptions()
        return await self.create_doc_with_options_async(request, runtime)

    def create_faq_with_options(
        self,
        tmp_req: main_models.CreateFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFaqResponse:
        tmp_req.validate()
        request = main_models.CreateFaqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.solution_content):
            body['SolutionContent'] = request.solution_content
        if not DaraCore.is_null(request.solution_type):
            body['SolutionType'] = request.solution_type
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_faq_with_options_async(
        self,
        tmp_req: main_models.CreateFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFaqResponse:
        tmp_req.validate()
        request = main_models.CreateFaqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.solution_content):
            body['SolutionContent'] = request.solution_content
        if not DaraCore.is_null(request.solution_type):
            body['SolutionType'] = request.solution_type
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_faq(
        self,
        request: main_models.CreateFaqRequest,
    ) -> main_models.CreateFaqResponse:
        runtime = RuntimeOptions()
        return self.create_faq_with_options(request, runtime)

    async def create_faq_async(
        self,
        request: main_models.CreateFaqRequest,
    ) -> main_models.CreateFaqResponse:
        runtime = RuntimeOptions()
        return await self.create_faq_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.introduction):
            query['Introduction'] = request.introduction
        if not DaraCore.is_null(request.language_code):
            query['LanguageCode'] = request.language_code
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.introduction):
            query['Introduction'] = request.introduction
        if not DaraCore.is_null(request.language_code):
            query['LanguageCode'] = request.language_code
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instance_publish_task_with_options(
        self,
        request: main_models.CreateInstancePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstancePublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstancePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstancePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_publish_task_with_options_async(
        self,
        request: main_models.CreateInstancePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstancePublishTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstancePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstancePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_publish_task(
        self,
        request: main_models.CreateInstancePublishTaskRequest,
    ) -> main_models.CreateInstancePublishTaskResponse:
        runtime = RuntimeOptions()
        return self.create_instance_publish_task_with_options(request, runtime)

    async def create_instance_publish_task_async(
        self,
        request: main_models.CreateInstancePublishTaskRequest,
    ) -> main_models.CreateInstancePublishTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_publish_task_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        tmp_req: main_models.CreateIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntentResponse:
        tmp_req.validate()
        request = main_models.CreateIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        tmp_req: main_models.CreateIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntentResponse:
        tmp_req.validate()
        request = main_models.CreateIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intent(
        self,
        request: main_models.CreateIntentRequest,
    ) -> main_models.CreateIntentResponse:
        runtime = RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: main_models.CreateIntentRequest,
    ) -> main_models.CreateIntentResponse:
        runtime = RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_lgf_with_options(
        self,
        tmp_req: main_models.CreateLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLgfResponse:
        tmp_req.validate()
        request = main_models.CreateLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lgf_with_options_async(
        self,
        tmp_req: main_models.CreateLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLgfResponse:
        tmp_req.validate()
        request = main_models.CreateLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lgf(
        self,
        request: main_models.CreateLgfRequest,
    ) -> main_models.CreateLgfResponse:
        runtime = RuntimeOptions()
        return self.create_lgf_with_options(request, runtime)

    async def create_lgf_async(
        self,
        request: main_models.CreateLgfRequest,
    ) -> main_models.CreateLgfResponse:
        runtime = RuntimeOptions()
        return await self.create_lgf_with_options_async(request, runtime)

    def create_perspective_with_options(
        self,
        request: main_models.CreatePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_perspective_with_options_async(
        self,
        request: main_models.CreatePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_perspective(
        self,
        request: main_models.CreatePerspectiveRequest,
    ) -> main_models.CreatePerspectiveResponse:
        runtime = RuntimeOptions()
        return self.create_perspective_with_options(request, runtime)

    async def create_perspective_async(
        self,
        request: main_models.CreatePerspectiveRequest,
    ) -> main_models.CreatePerspectiveResponse:
        runtime = RuntimeOptions()
        return await self.create_perspective_with_options_async(request, runtime)

    def create_publish_task_with_options(
        self,
        tmp_req: main_models.CreatePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePublishTaskResponse:
        tmp_req.validate()
        request = main_models.CreatePublishTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_id_list):
            request.data_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_publish_task_with_options_async(
        self,
        tmp_req: main_models.CreatePublishTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePublishTaskResponse:
        tmp_req.validate()
        request = main_models.CreatePublishTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_id_list):
            request.data_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePublishTask',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_publish_task(
        self,
        request: main_models.CreatePublishTaskRequest,
    ) -> main_models.CreatePublishTaskResponse:
        runtime = RuntimeOptions()
        return self.create_publish_task_with_options(request, runtime)

    async def create_publish_task_async(
        self,
        request: main_models.CreatePublishTaskRequest,
    ) -> main_models.CreatePublishTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_publish_task_with_options_async(request, runtime)

    def create_sim_question_with_options(
        self,
        request: main_models.CreateSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sim_question_with_options_async(
        self,
        request: main_models.CreateSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sim_question(
        self,
        request: main_models.CreateSimQuestionRequest,
    ) -> main_models.CreateSimQuestionResponse:
        runtime = RuntimeOptions()
        return self.create_sim_question_with_options(request, runtime)

    async def create_sim_question_async(
        self,
        request: main_models.CreateSimQuestionRequest,
    ) -> main_models.CreateSimQuestionResponse:
        runtime = RuntimeOptions()
        return await self.create_sim_question_with_options_async(request, runtime)

    def create_solution_with_options(
        self,
        tmp_req: main_models.CreateSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSolutionResponse:
        tmp_req.validate()
        request = main_models.CreateSolutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.perspective_codes):
            query['PerspectiveCodes'] = request.perspective_codes
        body = {}
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_solution_with_options_async(
        self,
        tmp_req: main_models.CreateSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSolutionResponse:
        tmp_req.validate()
        request = main_models.CreateSolutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.perspective_codes):
            query['PerspectiveCodes'] = request.perspective_codes
        body = {}
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_solution(
        self,
        request: main_models.CreateSolutionRequest,
    ) -> main_models.CreateSolutionResponse:
        runtime = RuntimeOptions()
        return self.create_solution_with_options(request, runtime)

    async def create_solution_async(
        self,
        request: main_models.CreateSolutionRequest,
    ) -> main_models.CreateSolutionResponse:
        runtime = RuntimeOptions()
        return await self.create_solution_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: main_models.CreateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: main_models.CreateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_tag_group_with_options(
        self,
        request: main_models.CreateTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_group_with_options_async(
        self,
        request: main_models.CreateTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag_group(
        self,
        request: main_models.CreateTagGroupRequest,
    ) -> main_models.CreateTagGroupResponse:
        runtime = RuntimeOptions()
        return self.create_tag_group_with_options(request, runtime)

    async def create_tag_group_async(
        self,
        request: main_models.CreateTagGroupRequest,
    ) -> main_models.CreateTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_tag_group_with_options_async(request, runtime)

    def create_user_say_with_options(
        self,
        tmp_req: main_models.CreateUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserSayResponse:
        tmp_req.validate()
        request = main_models.CreateUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_say_with_options_async(
        self,
        tmp_req: main_models.CreateUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserSayResponse:
        tmp_req.validate()
        request = main_models.CreateUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_say(
        self,
        request: main_models.CreateUserSayRequest,
    ) -> main_models.CreateUserSayResponse:
        runtime = RuntimeOptions()
        return self.create_user_say_with_options(request, runtime)

    async def create_user_say_async(
        self,
        request: main_models.CreateUserSayRequest,
    ) -> main_models.CreateUserSayResponse:
        runtime = RuntimeOptions()
        return await self.create_user_say_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: main_models.DeleteCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: main_models.DeleteCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_category(
        self,
        request: main_models.DeleteCategoryRequest,
    ) -> main_models.DeleteCategoryResponse:
        runtime = RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: main_models.DeleteCategoryRequest,
    ) -> main_models.DeleteCategoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_conn_question_with_options(
        self,
        request: main_models.DeleteConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_conn_question_with_options_async(
        self,
        request: main_models.DeleteConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_conn_question(
        self,
        request: main_models.DeleteConnQuestionRequest,
    ) -> main_models.DeleteConnQuestionResponse:
        runtime = RuntimeOptions()
        return self.delete_conn_question_with_options(request, runtime)

    async def delete_conn_question_async(
        self,
        request: main_models.DeleteConnQuestionRequest,
    ) -> main_models.DeleteConnQuestionResponse:
        runtime = RuntimeOptions()
        return await self.delete_conn_question_with_options_async(request, runtime)

    def delete_dsentity_with_options(
        self,
        request: main_models.DeleteDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dsentity_with_options_async(
        self,
        request: main_models.DeleteDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dsentity(
        self,
        request: main_models.DeleteDSEntityRequest,
    ) -> main_models.DeleteDSEntityResponse:
        runtime = RuntimeOptions()
        return self.delete_dsentity_with_options(request, runtime)

    async def delete_dsentity_async(
        self,
        request: main_models.DeleteDSEntityRequest,
    ) -> main_models.DeleteDSEntityResponse:
        runtime = RuntimeOptions()
        return await self.delete_dsentity_with_options_async(request, runtime)

    def delete_dsentity_value_with_options(
        self,
        request: main_models.DeleteDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDSEntityValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dsentity_value_with_options_async(
        self,
        request: main_models.DeleteDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDSEntityValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dsentity_value(
        self,
        request: main_models.DeleteDSEntityValueRequest,
    ) -> main_models.DeleteDSEntityValueResponse:
        runtime = RuntimeOptions()
        return self.delete_dsentity_value_with_options(request, runtime)

    async def delete_dsentity_value_async(
        self,
        request: main_models.DeleteDSEntityValueRequest,
    ) -> main_models.DeleteDSEntityValueResponse:
        runtime = RuntimeOptions()
        return await self.delete_dsentity_value_with_options_async(request, runtime)

    def delete_doc_with_options(
        self,
        request: main_models.DeleteDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_doc_with_options_async(
        self,
        request: main_models.DeleteDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_doc(
        self,
        request: main_models.DeleteDocRequest,
    ) -> main_models.DeleteDocResponse:
        runtime = RuntimeOptions()
        return self.delete_doc_with_options(request, runtime)

    async def delete_doc_async(
        self,
        request: main_models.DeleteDocRequest,
    ) -> main_models.DeleteDocResponse:
        runtime = RuntimeOptions()
        return await self.delete_doc_with_options_async(request, runtime)

    def delete_faq_with_options(
        self,
        request: main_models.DeleteFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaqResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_faq_with_options_async(
        self,
        request: main_models.DeleteFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaqResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_faq(
        self,
        request: main_models.DeleteFaqRequest,
    ) -> main_models.DeleteFaqResponse:
        runtime = RuntimeOptions()
        return self.delete_faq_with_options(request, runtime)

    async def delete_faq_async(
        self,
        request: main_models.DeleteFaqRequest,
    ) -> main_models.DeleteFaqResponse:
        runtime = RuntimeOptions()
        return await self.delete_faq_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_intent_with_options(
        self,
        request: main_models.DeleteIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: main_models.DeleteIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intent(
        self,
        request: main_models.DeleteIntentRequest,
    ) -> main_models.DeleteIntentResponse:
        runtime = RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: main_models.DeleteIntentRequest,
    ) -> main_models.DeleteIntentResponse:
        runtime = RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_lgf_with_options(
        self,
        request: main_models.DeleteLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lgf_with_options_async(
        self,
        request: main_models.DeleteLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lgf(
        self,
        request: main_models.DeleteLgfRequest,
    ) -> main_models.DeleteLgfResponse:
        runtime = RuntimeOptions()
        return self.delete_lgf_with_options(request, runtime)

    async def delete_lgf_async(
        self,
        request: main_models.DeleteLgfRequest,
    ) -> main_models.DeleteLgfResponse:
        runtime = RuntimeOptions()
        return await self.delete_lgf_with_options_async(request, runtime)

    def delete_perspective_with_options(
        self,
        request: main_models.DeletePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_perspective_with_options_async(
        self,
        request: main_models.DeletePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_perspective(
        self,
        request: main_models.DeletePerspectiveRequest,
    ) -> main_models.DeletePerspectiveResponse:
        runtime = RuntimeOptions()
        return self.delete_perspective_with_options(request, runtime)

    async def delete_perspective_async(
        self,
        request: main_models.DeletePerspectiveRequest,
    ) -> main_models.DeletePerspectiveResponse:
        runtime = RuntimeOptions()
        return await self.delete_perspective_with_options_async(request, runtime)

    def delete_sim_question_with_options(
        self,
        request: main_models.DeleteSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sim_question_with_options_async(
        self,
        request: main_models.DeleteSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sim_question(
        self,
        request: main_models.DeleteSimQuestionRequest,
    ) -> main_models.DeleteSimQuestionResponse:
        runtime = RuntimeOptions()
        return self.delete_sim_question_with_options(request, runtime)

    async def delete_sim_question_async(
        self,
        request: main_models.DeleteSimQuestionRequest,
    ) -> main_models.DeleteSimQuestionResponse:
        runtime = RuntimeOptions()
        return await self.delete_sim_question_with_options_async(request, runtime)

    def delete_solution_with_options(
        self,
        request: main_models.DeleteSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_solution_with_options_async(
        self,
        request: main_models.DeleteSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_solution(
        self,
        request: main_models.DeleteSolutionRequest,
    ) -> main_models.DeleteSolutionResponse:
        runtime = RuntimeOptions()
        return self.delete_solution_with_options(request, runtime)

    async def delete_solution_async(
        self,
        request: main_models.DeleteSolutionRequest,
    ) -> main_models.DeleteSolutionResponse:
        runtime = RuntimeOptions()
        return await self.delete_solution_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: main_models.DeleteTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: main_models.DeleteTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_tag_group_with_options(
        self,
        request: main_models.DeleteTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_group_with_options_async(
        self,
        request: main_models.DeleteTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_group(
        self,
        request: main_models.DeleteTagGroupRequest,
    ) -> main_models.DeleteTagGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_tag_group_with_options(request, runtime)

    async def delete_tag_group_async(
        self,
        request: main_models.DeleteTagGroupRequest,
    ) -> main_models.DeleteTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_tag_group_with_options_async(request, runtime)

    def delete_user_say_with_options(
        self,
        request: main_models.DeleteUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_say_with_options_async(
        self,
        request: main_models.DeleteUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_say(
        self,
        request: main_models.DeleteUserSayRequest,
    ) -> main_models.DeleteUserSayResponse:
        runtime = RuntimeOptions()
        return self.delete_user_say_with_options(request, runtime)

    async def delete_user_say_async(
        self,
        request: main_models.DeleteUserSayRequest,
    ) -> main_models.DeleteUserSayResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_say_with_options_async(request, runtime)

    def describe_category_with_options(
        self,
        request: main_models.DescribeCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_category_with_options_async(
        self,
        request: main_models.DescribeCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_category(
        self,
        request: main_models.DescribeCategoryRequest,
    ) -> main_models.DescribeCategoryResponse:
        runtime = RuntimeOptions()
        return self.describe_category_with_options(request, runtime)

    async def describe_category_async(
        self,
        request: main_models.DescribeCategoryRequest,
    ) -> main_models.DescribeCategoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_category_with_options_async(request, runtime)

    def describe_dsentity_with_options(
        self,
        request: main_models.DescribeDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dsentity_with_options_async(
        self,
        request: main_models.DescribeDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dsentity(
        self,
        request: main_models.DescribeDSEntityRequest,
    ) -> main_models.DescribeDSEntityResponse:
        runtime = RuntimeOptions()
        return self.describe_dsentity_with_options(request, runtime)

    async def describe_dsentity_async(
        self,
        request: main_models.DescribeDSEntityRequest,
    ) -> main_models.DescribeDSEntityResponse:
        runtime = RuntimeOptions()
        return await self.describe_dsentity_with_options_async(request, runtime)

    def describe_doc_with_options(
        self,
        request: main_models.DescribeDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doc_with_options_async(
        self,
        request: main_models.DescribeDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doc(
        self,
        request: main_models.DescribeDocRequest,
    ) -> main_models.DescribeDocResponse:
        runtime = RuntimeOptions()
        return self.describe_doc_with_options(request, runtime)

    async def describe_doc_async(
        self,
        request: main_models.DescribeDocRequest,
    ) -> main_models.DescribeDocResponse:
        runtime = RuntimeOptions()
        return await self.describe_doc_with_options_async(request, runtime)

    def describe_faq_with_options(
        self,
        request: main_models.DescribeFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaqResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_faq_with_options_async(
        self,
        request: main_models.DescribeFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFaqResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_faq(
        self,
        request: main_models.DescribeFaqRequest,
    ) -> main_models.DescribeFaqResponse:
        runtime = RuntimeOptions()
        return self.describe_faq_with_options(request, runtime)

    async def describe_faq_async(
        self,
        request: main_models.DescribeFaqRequest,
    ) -> main_models.DescribeFaqResponse:
        runtime = RuntimeOptions()
        return await self.describe_faq_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: main_models.DescribeIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.intent_id):
            body['IntentId'] = request.intent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_with_options_async(
        self,
        request: main_models.DescribeIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.intent_id):
            body['IntentId'] = request.intent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent(
        self,
        request: main_models.DescribeIntentRequest,
    ) -> main_models.DescribeIntentResponse:
        runtime = RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: main_models.DescribeIntentRequest,
    ) -> main_models.DescribeIntentResponse:
        runtime = RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_perspective_with_options(
        self,
        request: main_models.DescribePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_perspective_with_options_async(
        self,
        request: main_models.DescribePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_perspective(
        self,
        request: main_models.DescribePerspectiveRequest,
    ) -> main_models.DescribePerspectiveResponse:
        runtime = RuntimeOptions()
        return self.describe_perspective_with_options(request, runtime)

    async def describe_perspective_async(
        self,
        request: main_models.DescribePerspectiveRequest,
    ) -> main_models.DescribePerspectiveResponse:
        runtime = RuntimeOptions()
        return await self.describe_perspective_with_options_async(request, runtime)

    def describe_tag_with_options(
        self,
        request: main_models.DescribeTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_with_options_async(
        self,
        request: main_models.DescribeTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag(
        self,
        request: main_models.DescribeTagRequest,
    ) -> main_models.DescribeTagResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_with_options(request, runtime)

    async def describe_tag_async(
        self,
        request: main_models.DescribeTagRequest,
    ) -> main_models.DescribeTagResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_with_options_async(request, runtime)

    def describe_tag_group_with_options(
        self,
        request: main_models.DescribeTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_group_with_options_async(
        self,
        request: main_models.DescribeTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_group(
        self,
        request: main_models.DescribeTagGroupRequest,
    ) -> main_models.DescribeTagGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_group_with_options(request, runtime)

    async def describe_tag_group_async(
        self,
        request: main_models.DescribeTagGroupRequest,
    ) -> main_models.DescribeTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_group_with_options_async(request, runtime)

    def feedback_with_options(
        self,
        request: main_models.FeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.feedback_content):
            query['FeedbackContent'] = request.feedback_content
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Feedback',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_with_options_async(
        self,
        request: main_models.FeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.feedback_content):
            query['FeedbackContent'] = request.feedback_content
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Feedback',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback(
        self,
        request: main_models.FeedbackRequest,
    ) -> main_models.FeedbackResponse:
        runtime = RuntimeOptions()
        return self.feedback_with_options(request, runtime)

    async def feedback_async(
        self,
        request: main_models.FeedbackRequest,
    ) -> main_models.FeedbackResponse:
        runtime = RuntimeOptions()
        return await self.feedback_with_options_async(request, runtime)

    def generate_user_access_token_with_options(
        self,
        request: main_models.GenerateUserAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUserAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.foreign_id):
            body['ForeignId'] = request.foreign_id
        if not DaraCore.is_null(request.nick):
            body['Nick'] = request.nick
        if not DaraCore.is_null(request.telephone):
            body['Telephone'] = request.telephone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUserAccessToken',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUserAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_user_access_token_with_options_async(
        self,
        request: main_models.GenerateUserAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUserAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.foreign_id):
            body['ForeignId'] = request.foreign_id
        if not DaraCore.is_null(request.nick):
            body['Nick'] = request.nick
        if not DaraCore.is_null(request.telephone):
            body['Telephone'] = request.telephone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUserAccessToken',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUserAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_user_access_token(
        self,
        request: main_models.GenerateUserAccessTokenRequest,
    ) -> main_models.GenerateUserAccessTokenResponse:
        runtime = RuntimeOptions()
        return self.generate_user_access_token_with_options(request, runtime)

    async def generate_user_access_token_async(
        self,
        request: main_models.GenerateUserAccessTokenRequest,
    ) -> main_models.GenerateUserAccessTokenResponse:
        runtime = RuntimeOptions()
        return await self.generate_user_access_token_with_options_async(request, runtime)

    def get_agent_info_with_options(
        self,
        request: main_models.GetAgentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentInfo',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_info_with_options_async(
        self,
        request: main_models.GetAgentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentInfo',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_info(
        self,
        request: main_models.GetAgentInfoRequest,
    ) -> main_models.GetAgentInfoResponse:
        runtime = RuntimeOptions()
        return self.get_agent_info_with_options(request, runtime)

    async def get_agent_info_async(
        self,
        request: main_models.GetAgentInfoRequest,
    ) -> main_models.GetAgentInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_info_with_options_async(request, runtime)

    def get_async_result_with_options(
        self,
        request: main_models.GetAsyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncResult',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_result_with_options_async(
        self,
        request: main_models.GetAsyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncResult',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_result(
        self,
        request: main_models.GetAsyncResultRequest,
    ) -> main_models.GetAsyncResultResponse:
        runtime = RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    async def get_async_result_async(
        self,
        request: main_models.GetAsyncResultRequest,
    ) -> main_models.GetAsyncResultResponse:
        runtime = RuntimeOptions()
        return await self.get_async_result_with_options_async(request, runtime)

    def get_bot_session_data_with_options(
        self,
        request: main_models.GetBotSessionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBotSessionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBotSessionData',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBotSessionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bot_session_data_with_options_async(
        self,
        request: main_models.GetBotSessionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBotSessionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBotSessionData',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBotSessionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bot_session_data(
        self,
        request: main_models.GetBotSessionDataRequest,
    ) -> main_models.GetBotSessionDataResponse:
        runtime = RuntimeOptions()
        return self.get_bot_session_data_with_options(request, runtime)

    async def get_bot_session_data_async(
        self,
        request: main_models.GetBotSessionDataRequest,
    ) -> main_models.GetBotSessionDataResponse:
        runtime = RuntimeOptions()
        return await self.get_bot_session_data_with_options_async(request, runtime)

    def get_instance_publish_task_state_with_options(
        self,
        request: main_models.GetInstancePublishTaskStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstancePublishTaskStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstancePublishTaskState',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstancePublishTaskStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_publish_task_state_with_options_async(
        self,
        request: main_models.GetInstancePublishTaskStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstancePublishTaskStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstancePublishTaskState',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstancePublishTaskStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_publish_task_state(
        self,
        request: main_models.GetInstancePublishTaskStateRequest,
    ) -> main_models.GetInstancePublishTaskStateResponse:
        runtime = RuntimeOptions()
        return self.get_instance_publish_task_state_with_options(request, runtime)

    async def get_instance_publish_task_state_async(
        self,
        request: main_models.GetInstancePublishTaskStateRequest,
    ) -> main_models.GetInstancePublishTaskStateResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_publish_task_state_with_options_async(request, runtime)

    def get_publish_task_state_with_options(
        self,
        request: main_models.GetPublishTaskStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPublishTaskStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPublishTaskState',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPublishTaskStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_publish_task_state_with_options_async(
        self,
        request: main_models.GetPublishTaskStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPublishTaskStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPublishTaskState',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPublishTaskStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_publish_task_state(
        self,
        request: main_models.GetPublishTaskStateRequest,
    ) -> main_models.GetPublishTaskStateResponse:
        runtime = RuntimeOptions()
        return self.get_publish_task_state_with_options(request, runtime)

    async def get_publish_task_state_async(
        self,
        request: main_models.GetPublishTaskStateRequest,
    ) -> main_models.GetPublishTaskStateResponse:
        runtime = RuntimeOptions()
        return await self.get_publish_task_state_with_options_async(request, runtime)

    def init_imconnect_with_options(
        self,
        request: main_models.InitIMConnectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitIMConnectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.from_):
            body['From'] = request.from_
        if not DaraCore.is_null(request.user_access_token):
            body['UserAccessToken'] = request.user_access_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitIMConnect',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitIMConnectResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_imconnect_with_options_async(
        self,
        request: main_models.InitIMConnectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitIMConnectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.from_):
            body['From'] = request.from_
        if not DaraCore.is_null(request.user_access_token):
            body['UserAccessToken'] = request.user_access_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitIMConnect',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitIMConnectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_imconnect(
        self,
        request: main_models.InitIMConnectRequest,
    ) -> main_models.InitIMConnectResponse:
        runtime = RuntimeOptions()
        return self.init_imconnect_with_options(request, runtime)

    async def init_imconnect_async(
        self,
        request: main_models.InitIMConnectRequest,
    ) -> main_models.InitIMConnectResponse:
        runtime = RuntimeOptions()
        return await self.init_imconnect_with_options_async(request, runtime)

    def link_instance_category_with_options(
        self,
        request: main_models.LinkInstanceCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LinkInstanceCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ability_type):
            query['AbilityType'] = request.ability_type
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.category_ids):
            body['CategoryIds'] = request.category_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LinkInstanceCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LinkInstanceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def link_instance_category_with_options_async(
        self,
        request: main_models.LinkInstanceCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LinkInstanceCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ability_type):
            query['AbilityType'] = request.ability_type
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.category_ids):
            body['CategoryIds'] = request.category_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LinkInstanceCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LinkInstanceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def link_instance_category(
        self,
        request: main_models.LinkInstanceCategoryRequest,
    ) -> main_models.LinkInstanceCategoryResponse:
        runtime = RuntimeOptions()
        return self.link_instance_category_with_options(request, runtime)

    async def link_instance_category_async(
        self,
        request: main_models.LinkInstanceCategoryRequest,
    ) -> main_models.LinkInstanceCategoryResponse:
        runtime = RuntimeOptions()
        return await self.link_instance_category_with_options_async(request, runtime)

    def list_agent_with_options(
        self,
        request: main_models.ListAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.goods_codes):
            query['GoodsCodes'] = request.goods_codes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_with_options_async(
        self,
        request: main_models.ListAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.goods_codes):
            query['GoodsCodes'] = request.goods_codes
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent(
        self,
        request: main_models.ListAgentRequest,
    ) -> main_models.ListAgentResponse:
        runtime = RuntimeOptions()
        return self.list_agent_with_options(request, runtime)

    async def list_agent_async(
        self,
        request: main_models.ListAgentRequest,
    ) -> main_models.ListAgentResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_with_options_async(request, runtime)

    def list_category_with_options(
        self,
        request: main_models.ListCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_category_with_options_async(
        self,
        request: main_models.ListCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_category(
        self,
        request: main_models.ListCategoryRequest,
    ) -> main_models.ListCategoryResponse:
        runtime = RuntimeOptions()
        return self.list_category_with_options(request, runtime)

    async def list_category_async(
        self,
        request: main_models.ListCategoryRequest,
    ) -> main_models.ListCategoryResponse:
        runtime = RuntimeOptions()
        return await self.list_category_with_options_async(request, runtime)

    def list_conn_question_with_options(
        self,
        request: main_models.ListConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conn_question_with_options_async(
        self,
        request: main_models.ListConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conn_question(
        self,
        request: main_models.ListConnQuestionRequest,
    ) -> main_models.ListConnQuestionResponse:
        runtime = RuntimeOptions()
        return self.list_conn_question_with_options(request, runtime)

    async def list_conn_question_async(
        self,
        request: main_models.ListConnQuestionRequest,
    ) -> main_models.ListConnQuestionResponse:
        runtime = RuntimeOptions()
        return await self.list_conn_question_with_options_async(request, runtime)

    def list_dsentity_with_options(
        self,
        request: main_models.ListDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dsentity_with_options_async(
        self,
        request: main_models.ListDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dsentity(
        self,
        request: main_models.ListDSEntityRequest,
    ) -> main_models.ListDSEntityResponse:
        runtime = RuntimeOptions()
        return self.list_dsentity_with_options(request, runtime)

    async def list_dsentity_async(
        self,
        request: main_models.ListDSEntityRequest,
    ) -> main_models.ListDSEntityResponse:
        runtime = RuntimeOptions()
        return await self.list_dsentity_with_options_async(request, runtime)

    def list_dsentity_value_with_options(
        self,
        request: main_models.ListDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDSEntityValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_value_id):
            body['EntityValueId'] = request.entity_value_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dsentity_value_with_options_async(
        self,
        request: main_models.ListDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDSEntityValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.entity_id):
            body['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_value_id):
            body['EntityValueId'] = request.entity_value_id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dsentity_value(
        self,
        request: main_models.ListDSEntityValueRequest,
    ) -> main_models.ListDSEntityValueResponse:
        runtime = RuntimeOptions()
        return self.list_dsentity_value_with_options(request, runtime)

    async def list_dsentity_value_async(
        self,
        request: main_models.ListDSEntityValueRequest,
    ) -> main_models.ListDSEntityValueResponse:
        runtime = RuntimeOptions()
        return await self.list_dsentity_value_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.robot_type):
            query['RobotType'] = request.robot_type
        if not DaraCore.is_null(request.sandbox):
            query['Sandbox'] = request.sandbox
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.robot_type):
            query['RobotType'] = request.robot_type
        if not DaraCore.is_null(request.sandbox):
            query['Sandbox'] = request.sandbox
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_intent_with_options(
        self,
        request: main_models.ListIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intent_with_options_async(
        self,
        request: main_models.ListIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_name):
            query['IntentName'] = request.intent_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intent(
        self,
        request: main_models.ListIntentRequest,
    ) -> main_models.ListIntentResponse:
        runtime = RuntimeOptions()
        return self.list_intent_with_options(request, runtime)

    async def list_intent_async(
        self,
        request: main_models.ListIntentRequest,
    ) -> main_models.ListIntentResponse:
        runtime = RuntimeOptions()
        return await self.list_intent_with_options_async(request, runtime)

    def list_lgf_with_options(
        self,
        request: main_models.ListLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lgf_with_options_async(
        self,
        request: main_models.ListLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLgfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lgf(
        self,
        request: main_models.ListLgfRequest,
    ) -> main_models.ListLgfResponse:
        runtime = RuntimeOptions()
        return self.list_lgf_with_options(request, runtime)

    async def list_lgf_async(
        self,
        request: main_models.ListLgfRequest,
    ) -> main_models.ListLgfResponse:
        runtime = RuntimeOptions()
        return await self.list_lgf_with_options_async(request, runtime)

    def list_saas_info_with_options(
        self,
        request: main_models.ListSaasInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSaasInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.saas_group_codes):
            query['SaasGroupCodes'] = request.saas_group_codes
        if not DaraCore.is_null(request.saas_name):
            query['SaasName'] = request.saas_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSaasInfo',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSaasInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_saas_info_with_options_async(
        self,
        request: main_models.ListSaasInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSaasInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.saas_group_codes):
            query['SaasGroupCodes'] = request.saas_group_codes
        if not DaraCore.is_null(request.saas_name):
            query['SaasName'] = request.saas_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSaasInfo',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSaasInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_saas_info(
        self,
        request: main_models.ListSaasInfoRequest,
    ) -> main_models.ListSaasInfoResponse:
        runtime = RuntimeOptions()
        return self.list_saas_info_with_options(request, runtime)

    async def list_saas_info_async(
        self,
        request: main_models.ListSaasInfoRequest,
    ) -> main_models.ListSaasInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_saas_info_with_options_async(request, runtime)

    def list_saas_permission_group_infos_with_options(
        self,
        request: main_models.ListSaasPermissionGroupInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSaasPermissionGroupInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSaasPermissionGroupInfos',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSaasPermissionGroupInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_saas_permission_group_infos_with_options_async(
        self,
        request: main_models.ListSaasPermissionGroupInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSaasPermissionGroupInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSaasPermissionGroupInfos',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSaasPermissionGroupInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_saas_permission_group_infos(
        self,
        request: main_models.ListSaasPermissionGroupInfosRequest,
    ) -> main_models.ListSaasPermissionGroupInfosResponse:
        runtime = RuntimeOptions()
        return self.list_saas_permission_group_infos_with_options(request, runtime)

    async def list_saas_permission_group_infos_async(
        self,
        request: main_models.ListSaasPermissionGroupInfosRequest,
    ) -> main_models.ListSaasPermissionGroupInfosResponse:
        runtime = RuntimeOptions()
        return await self.list_saas_permission_group_infos_with_options_async(request, runtime)

    def list_sim_question_with_options(
        self,
        request: main_models.ListSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sim_question_with_options_async(
        self,
        request: main_models.ListSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sim_question(
        self,
        request: main_models.ListSimQuestionRequest,
    ) -> main_models.ListSimQuestionResponse:
        runtime = RuntimeOptions()
        return self.list_sim_question_with_options(request, runtime)

    async def list_sim_question_async(
        self,
        request: main_models.ListSimQuestionRequest,
    ) -> main_models.ListSimQuestionResponse:
        runtime = RuntimeOptions()
        return await self.list_sim_question_with_options_async(request, runtime)

    def list_solution_with_options(
        self,
        request: main_models.ListSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_solution_with_options_async(
        self,
        request: main_models.ListSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_solution(
        self,
        request: main_models.ListSolutionRequest,
    ) -> main_models.ListSolutionResponse:
        runtime = RuntimeOptions()
        return self.list_solution_with_options(request, runtime)

    async def list_solution_async(
        self,
        request: main_models.ListSolutionRequest,
    ) -> main_models.ListSolutionResponse:
        runtime = RuntimeOptions()
        return await self.list_solution_with_options_async(request, runtime)

    def list_tag_with_options(
        self,
        request: main_models.ListTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_with_options_async(
        self,
        request: main_models.ListTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag(
        self,
        request: main_models.ListTagRequest,
    ) -> main_models.ListTagResponse:
        runtime = RuntimeOptions()
        return self.list_tag_with_options(request, runtime)

    async def list_tag_async(
        self,
        request: main_models.ListTagRequest,
    ) -> main_models.ListTagResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_with_options_async(request, runtime)

    def list_tag_group_with_options(
        self,
        request: main_models.ListTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_group_with_options_async(
        self,
        request: main_models.ListTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_group(
        self,
        request: main_models.ListTagGroupRequest,
    ) -> main_models.ListTagGroupResponse:
        runtime = RuntimeOptions()
        return self.list_tag_group_with_options(request, runtime)

    async def list_tag_group_async(
        self,
        request: main_models.ListTagGroupRequest,
    ) -> main_models.ListTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_group_with_options_async(request, runtime)

    def list_tongyi_chat_historys_with_options(
        self,
        request: main_models.ListTongyiChatHistorysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTongyiChatHistorysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTongyiChatHistorys',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTongyiChatHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tongyi_chat_historys_with_options_async(
        self,
        request: main_models.ListTongyiChatHistorysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTongyiChatHistorysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTongyiChatHistorys',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTongyiChatHistorysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tongyi_chat_historys(
        self,
        request: main_models.ListTongyiChatHistorysRequest,
    ) -> main_models.ListTongyiChatHistorysResponse:
        runtime = RuntimeOptions()
        return self.list_tongyi_chat_historys_with_options(request, runtime)

    async def list_tongyi_chat_historys_async(
        self,
        request: main_models.ListTongyiChatHistorysRequest,
    ) -> main_models.ListTongyiChatHistorysResponse:
        runtime = RuntimeOptions()
        return await self.list_tongyi_chat_historys_with_options_async(request, runtime)

    def list_tongyi_conversation_logs_with_options(
        self,
        request: main_models.ListTongyiConversationLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTongyiConversationLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTongyiConversationLogs',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTongyiConversationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tongyi_conversation_logs_with_options_async(
        self,
        request: main_models.ListTongyiConversationLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTongyiConversationLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTongyiConversationLogs',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTongyiConversationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tongyi_conversation_logs(
        self,
        request: main_models.ListTongyiConversationLogsRequest,
    ) -> main_models.ListTongyiConversationLogsResponse:
        runtime = RuntimeOptions()
        return self.list_tongyi_conversation_logs_with_options(request, runtime)

    async def list_tongyi_conversation_logs_async(
        self,
        request: main_models.ListTongyiConversationLogsRequest,
    ) -> main_models.ListTongyiConversationLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_tongyi_conversation_logs_with_options_async(request, runtime)

    def list_user_say_with_options(
        self,
        request: main_models.ListUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_say_with_options_async(
        self,
        request: main_models.ListUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserSayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_say(
        self,
        request: main_models.ListUserSayRequest,
    ) -> main_models.ListUserSayResponse:
        runtime = RuntimeOptions()
        return self.list_user_say_with_options(request, runtime)

    async def list_user_say_async(
        self,
        request: main_models.ListUserSayRequest,
    ) -> main_models.ListUserSayResponse:
        runtime = RuntimeOptions()
        return await self.list_user_say_with_options_async(request, runtime)

    def nlu_with_options(
        self,
        request: main_models.NluRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NluResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Nlu',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NluResponse(),
            self.call_api(params, req, runtime)
        )

    async def nlu_with_options_async(
        self,
        request: main_models.NluRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NluResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Nlu',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NluResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def nlu(
        self,
        request: main_models.NluRequest,
    ) -> main_models.NluResponse:
        runtime = RuntimeOptions()
        return self.nlu_with_options(request, runtime)

    async def nlu_async(
        self,
        request: main_models.NluRequest,
    ) -> main_models.NluResponse:
        runtime = RuntimeOptions()
        return await self.nlu_with_options_async(request, runtime)

    def query_perspectives_with_options(
        self,
        request: main_models.QueryPerspectivesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPerspectivesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPerspectives',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPerspectivesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_perspectives_with_options_async(
        self,
        request: main_models.QueryPerspectivesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPerspectivesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPerspectives',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPerspectivesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_perspectives(
        self,
        request: main_models.QueryPerspectivesRequest,
    ) -> main_models.QueryPerspectivesResponse:
        runtime = RuntimeOptions()
        return self.query_perspectives_with_options(request, runtime)

    async def query_perspectives_async(
        self,
        request: main_models.QueryPerspectivesRequest,
    ) -> main_models.QueryPerspectivesResponse:
        runtime = RuntimeOptions()
        return await self.query_perspectives_with_options_async(request, runtime)

    def retry_doc_with_options(
        self,
        request: main_models.RetryDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_doc_with_options_async(
        self,
        request: main_models.RetryDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryDocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_doc(
        self,
        request: main_models.RetryDocRequest,
    ) -> main_models.RetryDocResponse:
        runtime = RuntimeOptions()
        return self.retry_doc_with_options(request, runtime)

    async def retry_doc_async(
        self,
        request: main_models.RetryDocRequest,
    ) -> main_models.RetryDocResponse:
        runtime = RuntimeOptions()
        return await self.retry_doc_with_options_async(request, runtime)

    def search_doc_with_options(
        self,
        tmp_req: main_models.SearchDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchDocResponse:
        tmp_req.validate()
        request = main_models.SearchDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_ids):
            request.tag_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.create_time_begin):
            query['CreateTimeBegin'] = request.create_time_begin
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_user_name):
            query['CreateUserName'] = request.create_user_name
        if not DaraCore.is_null(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.modify_time_begin):
            query['ModifyTimeBegin'] = request.modify_time_begin
        if not DaraCore.is_null(request.modify_time_end):
            query['ModifyTimeEnd'] = request.modify_time_end
        if not DaraCore.is_null(request.modify_user_name):
            query['ModifyUserName'] = request.modify_user_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_status):
            query['ProcessStatus'] = request.process_status
        if not DaraCore.is_null(request.search_scope):
            query['SearchScope'] = request.search_scope
        if not DaraCore.is_null(request.start_time_begin):
            query['StartTimeBegin'] = request.start_time_begin
        if not DaraCore.is_null(request.start_time_end):
            query['StartTimeEnd'] = request.start_time_end
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_doc_with_options_async(
        self,
        tmp_req: main_models.SearchDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchDocResponse:
        tmp_req.validate()
        request = main_models.SearchDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_ids):
            request.tag_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.create_time_begin):
            query['CreateTimeBegin'] = request.create_time_begin
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_user_name):
            query['CreateUserName'] = request.create_user_name
        if not DaraCore.is_null(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.modify_time_begin):
            query['ModifyTimeBegin'] = request.modify_time_begin
        if not DaraCore.is_null(request.modify_time_end):
            query['ModifyTimeEnd'] = request.modify_time_end
        if not DaraCore.is_null(request.modify_user_name):
            query['ModifyUserName'] = request.modify_user_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_status):
            query['ProcessStatus'] = request.process_status
        if not DaraCore.is_null(request.search_scope):
            query['SearchScope'] = request.search_scope
        if not DaraCore.is_null(request.start_time_begin):
            query['StartTimeBegin'] = request.start_time_begin
        if not DaraCore.is_null(request.start_time_end):
            query['StartTimeEnd'] = request.start_time_end
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_doc(
        self,
        request: main_models.SearchDocRequest,
    ) -> main_models.SearchDocResponse:
        runtime = RuntimeOptions()
        return self.search_doc_with_options(request, runtime)

    async def search_doc_async(
        self,
        request: main_models.SearchDocRequest,
    ) -> main_models.SearchDocResponse:
        runtime = RuntimeOptions()
        return await self.search_doc_with_options_async(request, runtime)

    def search_faq_with_options(
        self,
        tmp_req: main_models.SearchFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchFaqResponse:
        tmp_req.validate()
        request = main_models.SearchFaqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.create_time_begin):
            body['CreateTimeBegin'] = request.create_time_begin
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_user_name):
            body['CreateUserName'] = request.create_user_name
        if not DaraCore.is_null(request.end_time_begin):
            body['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            body['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.modify_time_begin):
            body['ModifyTimeBegin'] = request.modify_time_begin
        if not DaraCore.is_null(request.modify_time_end):
            body['ModifyTimeEnd'] = request.modify_time_end
        if not DaraCore.is_null(request.modify_user_name):
            body['ModifyUserName'] = request.modify_user_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_scope):
            body['SearchScope'] = request.search_scope
        if not DaraCore.is_null(request.start_time_begin):
            body['StartTimeBegin'] = request.start_time_begin
        if not DaraCore.is_null(request.start_time_end):
            body['StartTimeEnd'] = request.start_time_end
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_faq_with_options_async(
        self,
        tmp_req: main_models.SearchFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchFaqResponse:
        tmp_req.validate()
        request = main_models.SearchFaqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.create_time_begin):
            body['CreateTimeBegin'] = request.create_time_begin
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_user_name):
            body['CreateUserName'] = request.create_user_name
        if not DaraCore.is_null(request.end_time_begin):
            body['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            body['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.modify_time_begin):
            body['ModifyTimeBegin'] = request.modify_time_begin
        if not DaraCore.is_null(request.modify_time_end):
            body['ModifyTimeEnd'] = request.modify_time_end
        if not DaraCore.is_null(request.modify_user_name):
            body['ModifyUserName'] = request.modify_user_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_scope):
            body['SearchScope'] = request.search_scope
        if not DaraCore.is_null(request.start_time_begin):
            body['StartTimeBegin'] = request.start_time_begin
        if not DaraCore.is_null(request.start_time_end):
            body['StartTimeEnd'] = request.start_time_end
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_faq(
        self,
        request: main_models.SearchFaqRequest,
    ) -> main_models.SearchFaqResponse:
        runtime = RuntimeOptions()
        return self.search_faq_with_options(request, runtime)

    async def search_faq_async(
        self,
        request: main_models.SearchFaqRequest,
    ) -> main_models.SearchFaqResponse:
        runtime = RuntimeOptions()
        return await self.search_faq_with_options_async(request, runtime)

    def tongyi_chat_debug_info_with_options(
        self,
        request: main_models.TongyiChatDebugInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TongyiChatDebugInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TongyiChatDebugInfo',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TongyiChatDebugInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def tongyi_chat_debug_info_with_options_async(
        self,
        request: main_models.TongyiChatDebugInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TongyiChatDebugInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TongyiChatDebugInfo',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TongyiChatDebugInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tongyi_chat_debug_info(
        self,
        request: main_models.TongyiChatDebugInfoRequest,
    ) -> main_models.TongyiChatDebugInfoResponse:
        runtime = RuntimeOptions()
        return self.tongyi_chat_debug_info_with_options(request, runtime)

    async def tongyi_chat_debug_info_async(
        self,
        request: main_models.TongyiChatDebugInfoRequest,
    ) -> main_models.TongyiChatDebugInfoResponse:
        runtime = RuntimeOptions()
        return await self.tongyi_chat_debug_info_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: main_models.UpdateCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.biz_code):
            body['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: main_models.UpdateCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.biz_code):
            body['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCategory',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_category(
        self,
        request: main_models.UpdateCategoryRequest,
    ) -> main_models.UpdateCategoryResponse:
        runtime = RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: main_models.UpdateCategoryRequest,
    ) -> main_models.UpdateCategoryResponse:
        runtime = RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_conn_question_with_options(
        self,
        request: main_models.UpdateConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not DaraCore.is_null(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conn_question_with_options_async(
        self,
        request: main_models.UpdateConnQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not DaraCore.is_null(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conn_question(
        self,
        request: main_models.UpdateConnQuestionRequest,
    ) -> main_models.UpdateConnQuestionResponse:
        runtime = RuntimeOptions()
        return self.update_conn_question_with_options(request, runtime)

    async def update_conn_question_async(
        self,
        request: main_models.UpdateConnQuestionRequest,
    ) -> main_models.UpdateConnQuestionResponse:
        runtime = RuntimeOptions()
        return await self.update_conn_question_with_options_async(request, runtime)

    def update_dsentity_with_options(
        self,
        request: main_models.UpdateDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_name):
            query['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dsentity_with_options_async(
        self,
        request: main_models.UpdateDSEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDSEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_name):
            query['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDSEntity',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dsentity(
        self,
        request: main_models.UpdateDSEntityRequest,
    ) -> main_models.UpdateDSEntityResponse:
        runtime = RuntimeOptions()
        return self.update_dsentity_with_options(request, runtime)

    async def update_dsentity_async(
        self,
        request: main_models.UpdateDSEntityRequest,
    ) -> main_models.UpdateDSEntityResponse:
        runtime = RuntimeOptions()
        return await self.update_dsentity_with_options_async(request, runtime)

    def update_dsentity_value_with_options(
        self,
        tmp_req: main_models.UpdateDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDSEntityValueResponse:
        tmp_req.validate()
        request = main_models.UpdateDSEntityValueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.synonyms):
            request.synonyms_shrink = Utils.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dsentity_value_with_options_async(
        self,
        tmp_req: main_models.UpdateDSEntityValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDSEntityValueResponse:
        tmp_req.validate()
        request = main_models.UpdateDSEntityValueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.synonyms):
            request.synonyms_shrink = Utils.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDSEntityValue',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dsentity_value(
        self,
        request: main_models.UpdateDSEntityValueRequest,
    ) -> main_models.UpdateDSEntityValueResponse:
        runtime = RuntimeOptions()
        return self.update_dsentity_value_with_options(request, runtime)

    async def update_dsentity_value_async(
        self,
        request: main_models.UpdateDSEntityValueRequest,
    ) -> main_models.UpdateDSEntityValueResponse:
        runtime = RuntimeOptions()
        return await self.update_dsentity_value_with_options_async(request, runtime)

    def update_doc_with_options(
        self,
        tmp_req: main_models.UpdateDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocResponse:
        tmp_req.validate()
        request = main_models.UpdateDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_metadata):
            request.doc_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not DaraCore.is_null(tmp_req.tag_ids):
            request.tag_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not DaraCore.is_null(request.doc_name):
            query['DocName'] = request.doc_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.meta):
            query['Meta'] = request.meta
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_doc_with_options_async(
        self,
        tmp_req: main_models.UpdateDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocResponse:
        tmp_req.validate()
        request = main_models.UpdateDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_metadata):
            request.doc_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not DaraCore.is_null(tmp_req.tag_ids):
            request.tag_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not DaraCore.is_null(request.doc_name):
            query['DocName'] = request.doc_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.meta):
            query['Meta'] = request.meta
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDoc',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_doc(
        self,
        request: main_models.UpdateDocRequest,
    ) -> main_models.UpdateDocResponse:
        runtime = RuntimeOptions()
        return self.update_doc_with_options(request, runtime)

    async def update_doc_async(
        self,
        request: main_models.UpdateDocRequest,
    ) -> main_models.UpdateDocResponse:
        runtime = RuntimeOptions()
        return await self.update_doc_with_options_async(request, runtime)

    def update_faq_with_options(
        self,
        tmp_req: main_models.UpdateFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFaqResponse:
        tmp_req.validate()
        request = main_models.UpdateFaqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_faq_with_options_async(
        self,
        tmp_req: main_models.UpdateFaqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFaqResponse:
        tmp_req.validate()
        request = main_models.UpdateFaqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFaq',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_faq(
        self,
        request: main_models.UpdateFaqRequest,
    ) -> main_models.UpdateFaqResponse:
        runtime = RuntimeOptions()
        return self.update_faq_with_options(request, runtime)

    async def update_faq_async(
        self,
        request: main_models.UpdateFaqRequest,
    ) -> main_models.UpdateFaqResponse:
        runtime = RuntimeOptions()
        return await self.update_faq_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.introduction):
            query['Introduction'] = request.introduction
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.introduction):
            query['Introduction'] = request.introduction
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_intent_with_options(
        self,
        tmp_req: main_models.UpdateIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntentResponse:
        tmp_req.validate()
        request = main_models.UpdateIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_intent_with_options_async(
        self,
        tmp_req: main_models.UpdateIntentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntentResponse:
        tmp_req.validate()
        request = main_models.UpdateIntentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intent_definition):
            request.intent_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not DaraCore.is_null(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntent',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_intent(
        self,
        request: main_models.UpdateIntentRequest,
    ) -> main_models.UpdateIntentResponse:
        runtime = RuntimeOptions()
        return self.update_intent_with_options(request, runtime)

    async def update_intent_async(
        self,
        request: main_models.UpdateIntentRequest,
    ) -> main_models.UpdateIntentResponse:
        runtime = RuntimeOptions()
        return await self.update_intent_with_options_async(request, runtime)

    def update_lgf_with_options(
        self,
        tmp_req: main_models.UpdateLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLgfResponse:
        tmp_req.validate()
        request = main_models.UpdateLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lgf_with_options_async(
        self,
        tmp_req: main_models.UpdateLgfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLgfResponse:
        tmp_req.validate()
        request = main_models.UpdateLgfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lgf_definition):
            request.lgf_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not DaraCore.is_null(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLgf',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lgf(
        self,
        request: main_models.UpdateLgfRequest,
    ) -> main_models.UpdateLgfResponse:
        runtime = RuntimeOptions()
        return self.update_lgf_with_options(request, runtime)

    async def update_lgf_async(
        self,
        request: main_models.UpdateLgfRequest,
    ) -> main_models.UpdateLgfResponse:
        runtime = RuntimeOptions()
        return await self.update_lgf_with_options_async(request, runtime)

    def update_perspective_with_options(
        self,
        request: main_models.UpdatePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_perspective_with_options_async(
        self,
        request: main_models.UpdatePerspectiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePerspectiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePerspective',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_perspective(
        self,
        request: main_models.UpdatePerspectiveRequest,
    ) -> main_models.UpdatePerspectiveResponse:
        runtime = RuntimeOptions()
        return self.update_perspective_with_options(request, runtime)

    async def update_perspective_async(
        self,
        request: main_models.UpdatePerspectiveRequest,
    ) -> main_models.UpdatePerspectiveResponse:
        runtime = RuntimeOptions()
        return await self.update_perspective_with_options_async(request, runtime)

    def update_sim_question_with_options(
        self,
        request: main_models.UpdateSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sim_question_with_options_async(
        self,
        request: main_models.UpdateSimQuestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSimQuestionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSimQuestion',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sim_question(
        self,
        request: main_models.UpdateSimQuestionRequest,
    ) -> main_models.UpdateSimQuestionResponse:
        runtime = RuntimeOptions()
        return self.update_sim_question_with_options(request, runtime)

    async def update_sim_question_async(
        self,
        request: main_models.UpdateSimQuestionRequest,
    ) -> main_models.UpdateSimQuestionResponse:
        runtime = RuntimeOptions()
        return await self.update_sim_question_with_options_async(request, runtime)

    def update_solution_with_options(
        self,
        tmp_req: main_models.UpdateSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSolutionResponse:
        tmp_req.validate()
        request = main_models.UpdateSolutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.perspective_codes):
            body['PerspectiveCodes'] = request.perspective_codes
        if not DaraCore.is_null(request.solution_id):
            body['SolutionId'] = request.solution_id
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_solution_with_options_async(
        self,
        tmp_req: main_models.UpdateSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSolutionResponse:
        tmp_req.validate()
        request = main_models.UpdateSolutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag_id_list):
            request.tag_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.perspective_codes):
            body['PerspectiveCodes'] = request.perspective_codes
        if not DaraCore.is_null(request.solution_id):
            body['SolutionId'] = request.solution_id
        if not DaraCore.is_null(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSolution',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_solution(
        self,
        request: main_models.UpdateSolutionRequest,
    ) -> main_models.UpdateSolutionResponse:
        runtime = RuntimeOptions()
        return self.update_solution_with_options(request, runtime)

    async def update_solution_async(
        self,
        request: main_models.UpdateSolutionRequest,
    ) -> main_models.UpdateSolutionResponse:
        runtime = RuntimeOptions()
        return await self.update_solution_with_options_async(request, runtime)

    def update_tag_with_options(
        self,
        request: main_models.UpdateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_with_options_async(
        self,
        request: main_models.UpdateTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTag',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag(
        self,
        request: main_models.UpdateTagRequest,
    ) -> main_models.UpdateTagResponse:
        runtime = RuntimeOptions()
        return self.update_tag_with_options(request, runtime)

    async def update_tag_async(
        self,
        request: main_models.UpdateTagRequest,
    ) -> main_models.UpdateTagResponse:
        runtime = RuntimeOptions()
        return await self.update_tag_with_options_async(request, runtime)

    def update_tag_group_with_options(
        self,
        request: main_models.UpdateTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_group_with_options_async(
        self,
        request: main_models.UpdateTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTagGroup',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag_group(
        self,
        request: main_models.UpdateTagGroupRequest,
    ) -> main_models.UpdateTagGroupResponse:
        runtime = RuntimeOptions()
        return self.update_tag_group_with_options(request, runtime)

    async def update_tag_group_async(
        self,
        request: main_models.UpdateTagGroupRequest,
    ) -> main_models.UpdateTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_tag_group_with_options_async(request, runtime)

    def update_user_say_with_options(
        self,
        tmp_req: main_models.UpdateUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserSayResponse:
        tmp_req.validate()
        request = main_models.UpdateUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_say_with_options_async(
        self,
        tmp_req: main_models.UpdateUserSayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserSayResponse:
        tmp_req.validate()
        request = main_models.UpdateUserSayShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_say_definition):
            request.user_say_definition_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not DaraCore.is_null(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserSay',
            version = '2022-04-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_say(
        self,
        request: main_models.UpdateUserSayRequest,
    ) -> main_models.UpdateUserSayResponse:
        runtime = RuntimeOptions()
        return self.update_user_say_with_options(request, runtime)

    async def update_user_say_async(
        self,
        request: main_models.UpdateUserSayRequest,
    ) -> main_models.UpdateUserSayResponse:
        runtime = RuntimeOptions()
        return await self.update_user_say_with_options_async(request, runtime)
