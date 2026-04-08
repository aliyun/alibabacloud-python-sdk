# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_appflow20230904 import models as main_models
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
        self._endpoint = self.get_endpoint('appflow', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def generate_user_session_token_with_options(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUserSessionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.expire_second):
            query['ExpireSecond'] = request.expire_second
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.integrate_id):
            query['IntegrateId'] = request.integrate_id
        if not DaraCore.is_null(request.user_avatar):
            query['UserAvatar'] = request.user_avatar
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUserSessionToken',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUserSessionTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_user_session_token_with_options_async(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUserSessionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.expire_second):
            query['ExpireSecond'] = request.expire_second
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.integrate_id):
            query['IntegrateId'] = request.integrate_id
        if not DaraCore.is_null(request.user_avatar):
            query['UserAvatar'] = request.user_avatar
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUserSessionToken',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUserSessionTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_user_session_token(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
    ) -> main_models.GenerateUserSessionTokenResponse:
        runtime = RuntimeOptions()
        return self.generate_user_session_token_with_options(request, runtime)

    async def generate_user_session_token_async(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
    ) -> main_models.GenerateUserSessionTokenResponse:
        runtime = RuntimeOptions()
        return await self.generate_user_session_token_with_options_async(request, runtime)

    def invoke_action_with_sse(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.InvokeActionResponse, None, None]:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
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
                    main_models.InvokeActionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def invoke_action_with_sse_async(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.InvokeActionResponse, None, None]:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
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
                    main_models.InvokeActionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def invoke_action_with_options(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeActionResponse:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_action_with_options_async(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeActionResponse:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_action(
        self,
        request: main_models.InvokeActionRequest,
    ) -> main_models.InvokeActionResponse:
        runtime = RuntimeOptions()
        return self.invoke_action_with_options(request, runtime)

    async def invoke_action_async(
        self,
        request: main_models.InvokeActionRequest,
    ) -> main_models.InvokeActionResponse:
        runtime = RuntimeOptions()
        return await self.invoke_action_with_options_async(request, runtime)
