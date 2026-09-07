# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_sasclaw20260626 import models as main_models
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
        self._endpoint = self.get_endpoint('sasclaw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def chat_user_sec_agent_with_sse(
        self,
        request: main_models.ChatUserSecAgentRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatUserSecAgentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent):
            body['Agent'] = request.agent
        if not DaraCore.is_null(request.attachment_staging_id):
            body['AttachmentStagingId'] = request.attachment_staging_id
        if not DaraCore.is_null(request.attachments):
            body['Attachments'] = request.attachments
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not DaraCore.is_null(request.memory):
            body['Memory'] = request.memory
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.response_language):
            body['ResponseLanguage'] = request.response_language
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.skill):
            body['Skill'] = request.skill
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.talk_id):
            body['TalkId'] = request.talk_id
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.user_input_info):
            body['UserInputInfo'] = request.user_input_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatUserSecAgent',
            version = '2026-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.ChatUserSecAgentResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def chat_user_sec_agent_with_sse_async(
        self,
        request: main_models.ChatUserSecAgentRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatUserSecAgentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent):
            body['Agent'] = request.agent
        if not DaraCore.is_null(request.attachment_staging_id):
            body['AttachmentStagingId'] = request.attachment_staging_id
        if not DaraCore.is_null(request.attachments):
            body['Attachments'] = request.attachments
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not DaraCore.is_null(request.memory):
            body['Memory'] = request.memory
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.response_language):
            body['ResponseLanguage'] = request.response_language
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.skill):
            body['Skill'] = request.skill
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.talk_id):
            body['TalkId'] = request.talk_id
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.user_input_info):
            body['UserInputInfo'] = request.user_input_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatUserSecAgent',
            version = '2026-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.ChatUserSecAgentResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def chat_user_sec_agent_with_options(
        self,
        request: main_models.ChatUserSecAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatUserSecAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent):
            body['Agent'] = request.agent
        if not DaraCore.is_null(request.attachment_staging_id):
            body['AttachmentStagingId'] = request.attachment_staging_id
        if not DaraCore.is_null(request.attachments):
            body['Attachments'] = request.attachments
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not DaraCore.is_null(request.memory):
            body['Memory'] = request.memory
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.response_language):
            body['ResponseLanguage'] = request.response_language
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.skill):
            body['Skill'] = request.skill
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.talk_id):
            body['TalkId'] = request.talk_id
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.user_input_info):
            body['UserInputInfo'] = request.user_input_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatUserSecAgent',
            version = '2026-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ChatUserSecAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_user_sec_agent_with_options_async(
        self,
        request: main_models.ChatUserSecAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatUserSecAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent):
            body['Agent'] = request.agent
        if not DaraCore.is_null(request.attachment_staging_id):
            body['AttachmentStagingId'] = request.attachment_staging_id
        if not DaraCore.is_null(request.attachments):
            body['Attachments'] = request.attachments
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not DaraCore.is_null(request.memory):
            body['Memory'] = request.memory
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.response_language):
            body['ResponseLanguage'] = request.response_language
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.skill):
            body['Skill'] = request.skill
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.talk_id):
            body['TalkId'] = request.talk_id
        if not DaraCore.is_null(request.target):
            body['Target'] = request.target
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.user_input_info):
            body['UserInputInfo'] = request.user_input_info
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChatUserSecAgent',
            version = '2026-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.ChatUserSecAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_user_sec_agent(
        self,
        request: main_models.ChatUserSecAgentRequest,
    ) -> main_models.ChatUserSecAgentResponse:
        runtime = RuntimeOptions()
        return self.chat_user_sec_agent_with_options(request, runtime)

    async def chat_user_sec_agent_async(
        self,
        request: main_models.ChatUserSecAgentRequest,
    ) -> main_models.ChatUserSecAgentResponse:
        runtime = RuntimeOptions()
        return await self.chat_user_sec_agent_with_options_async(request, runtime)
