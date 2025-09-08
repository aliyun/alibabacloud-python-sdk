# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_edututor20250707 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self._endpoint = self.get_endpoint('edututor', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def answer_ssewith_sse(
        self,
        request: main_models.AnswerSSERequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.AnswerSSEResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnswerSSE',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/service/answerSSE',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.AnswerSSEResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def answer_ssewith_sse_async(
        self,
        request: main_models.AnswerSSERequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.AnswerSSEResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnswerSSE',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/service/answerSSE',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.AnswerSSEResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def answer_ssewith_options(
        self,
        request: main_models.AnswerSSERequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnswerSSEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnswerSSE',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/service/answerSSE',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnswerSSEResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_ssewith_options_async(
        self,
        request: main_models.AnswerSSERequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnswerSSEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnswerSSE',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/service/answerSSE',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnswerSSEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_sse(
        self,
        request: main_models.AnswerSSERequest,
    ) -> main_models.AnswerSSEResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.answer_ssewith_options(request, headers, runtime)

    async def answer_sse_async(
        self,
        request: main_models.AnswerSSERequest,
    ) -> main_models.AnswerSSEResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.answer_ssewith_options_async(request, headers, runtime)

    def cut_questions_with_options(
        self,
        request: main_models.CutQuestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CutQuestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CutQuestions',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/service/cutApi',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CutQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cut_questions_with_options_async(
        self,
        request: main_models.CutQuestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CutQuestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CutQuestions',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/service/cutApi',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CutQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cut_questions(
        self,
        request: main_models.CutQuestionsRequest,
    ) -> main_models.CutQuestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cut_questions_with_options(request, headers, runtime)

    async def cut_questions_async(
        self,
        request: main_models.CutQuestionsRequest,
    ) -> main_models.CutQuestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cut_questions_with_options_async(request, headers, runtime)
