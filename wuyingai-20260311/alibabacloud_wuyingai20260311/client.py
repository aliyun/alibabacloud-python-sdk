# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_wuyingai20260311 import models as main_models
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
        self._endpoint = self.get_endpoint('wuyingai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        tmp_req: main_models.ChatRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.settings):
            request.settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        if not DaraCore.is_null(tmp_req.stream_options):
            request.stream_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.stream_options, 'StreamOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization):
            query['Authorization'] = request.authorization
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.routing_key):
            body['RoutingKey'] = request.routing_key
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.settings_shrink):
            body['Settings'] = request.settings_shrink
        if not DaraCore.is_null(request.stream_options_shrink):
            body['StreamOptions'] = request.stream_options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-03-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
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
        tmp_req: main_models.ChatRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.settings):
            request.settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        if not DaraCore.is_null(tmp_req.stream_options):
            request.stream_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.stream_options, 'StreamOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization):
            query['Authorization'] = request.authorization
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.routing_key):
            body['RoutingKey'] = request.routing_key
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.settings_shrink):
            body['Settings'] = request.settings_shrink
        if not DaraCore.is_null(request.stream_options_shrink):
            body['StreamOptions'] = request.stream_options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-03-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
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
        tmp_req: main_models.ChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        tmp_req.validate()
        request = main_models.ChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.settings):
            request.settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        if not DaraCore.is_null(tmp_req.stream_options):
            request.stream_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.stream_options, 'StreamOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization):
            query['Authorization'] = request.authorization
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.routing_key):
            body['RoutingKey'] = request.routing_key
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.settings_shrink):
            body['Settings'] = request.settings_shrink
        if not DaraCore.is_null(request.stream_options_shrink):
            body['StreamOptions'] = request.stream_options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-03-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def chat_with_options_async(
        self,
        tmp_req: main_models.ChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatResponse:
        tmp_req.validate()
        request = main_models.ChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.settings):
            request.settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        if not DaraCore.is_null(tmp_req.stream_options):
            request.stream_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.stream_options, 'StreamOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.authorization):
            query['Authorization'] = request.authorization
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.routing_key):
            body['RoutingKey'] = request.routing_key
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.settings_shrink):
            body['Settings'] = request.settings_shrink
        if not DaraCore.is_null(request.stream_options_shrink):
            body['StreamOptions'] = request.stream_options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Chat',
            version = '2026-03-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
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

    def get_access_token_with_options(
        self,
        request: main_models.GetAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_user_id):
            query['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessToken',
            version = '2026-03-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_token_with_options_async(
        self,
        request: main_models.GetAccessTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_user_id):
            query['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessToken',
            version = '2026-03-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_token(
        self,
        request: main_models.GetAccessTokenRequest,
    ) -> main_models.GetAccessTokenResponse:
        runtime = RuntimeOptions()
        return self.get_access_token_with_options(request, runtime)

    async def get_access_token_async(
        self,
        request: main_models.GetAccessTokenRequest,
    ) -> main_models.GetAccessTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_access_token_with_options_async(request, runtime)
