# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_ossagent20260810 import models as main_models
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

    def a_2a_with_sse(
        self,
        request: main_models.A2aRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.A2aResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'a2a',
            version = '2026-08-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'json',
            body_type = 'any'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.A2aResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def a_2a_with_sse_async(
        self,
        request: main_models.A2aRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.A2aResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'a2a',
            version = '2026-08-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'json',
            body_type = 'any'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = resp.event.data
                yield  DaraCore.from_map(
                    main_models.A2aResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def a_2a_with_options(
        self,
        request: main_models.A2aRequest,
        runtime: RuntimeOptions,
    ) -> main_models.A2aResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'a2a',
            version = '2026-08-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'json',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.A2aResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_2a_with_options_async(
        self,
        request: main_models.A2aRequest,
        runtime: RuntimeOptions,
    ) -> main_models.A2aResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.method):
            body['method'] = request.method
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'a2a',
            version = '2026-08-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'json',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.A2aResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_2a(
        self,
        request: main_models.A2aRequest,
    ) -> main_models.A2aResponse:
        runtime = RuntimeOptions()
        return self.a_2a_with_options(request, runtime)

    async def a_2a_async(
        self,
        request: main_models.A2aRequest,
    ) -> main_models.A2aResponse:
        runtime = RuntimeOptions()
        return await self.a_2a_with_options_async(request, runtime)

    def agent_card_with_options(
        self,
        request: main_models.AgentCardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentCardResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'agent_card',
            version = '2026-08-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.AgentCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def agent_card_with_options_async(
        self,
        request: main_models.AgentCardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AgentCardResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'agent_card',
            version = '2026-08-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.AgentCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agent_card(
        self,
        request: main_models.AgentCardRequest,
    ) -> main_models.AgentCardResponse:
        runtime = RuntimeOptions()
        return self.agent_card_with_options(request, runtime)

    async def agent_card_async(
        self,
        request: main_models.AgentCardRequest,
    ) -> main_models.AgentCardResponse:
        runtime = RuntimeOptions()
        return await self.agent_card_with_options_async(request, runtime)
