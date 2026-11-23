# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_qweneduaisuite20261102 import models as main_models
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
        self._product_id = 'QwenEduAiSuite'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('qweneduaisuite', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_qwen_edu_api_with_options(
        self,
        request: main_models.ActivateQwenEduApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActivateQwenEduApiResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ActivateQwenEduApi',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/service/activate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateQwenEduApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_qwen_edu_api_with_options_async(
        self,
        request: main_models.ActivateQwenEduApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActivateQwenEduApiResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ActivateQwenEduApi',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/service/activate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateQwenEduApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_qwen_edu_api(
        self,
        request: main_models.ActivateQwenEduApiRequest,
    ) -> main_models.ActivateQwenEduApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.activate_qwen_edu_api_with_options(request, headers, runtime)

    async def activate_qwen_edu_api_async(
        self,
        request: main_models.ActivateQwenEduApiRequest,
    ) -> main_models.ActivateQwenEduApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.activate_qwen_edu_api_with_options_async(request, headers, runtime)

    def create_edu_homework_correct_submit_with_options(
        self,
        request: main_models.CreateEduHomeworkCorrectSubmitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEduHomeworkCorrectSubmitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dewarp):
            body['dewarp'] = request.dewarp
        if not DaraCore.is_null(request.image_base_64):
            body['imageBase64'] = request.image_base_64
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEduHomeworkCorrectSubmit',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/homework/correct/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEduHomeworkCorrectSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_edu_homework_correct_submit_with_options_async(
        self,
        request: main_models.CreateEduHomeworkCorrectSubmitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEduHomeworkCorrectSubmitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dewarp):
            body['dewarp'] = request.dewarp
        if not DaraCore.is_null(request.image_base_64):
            body['imageBase64'] = request.image_base_64
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEduHomeworkCorrectSubmit',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/homework/correct/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEduHomeworkCorrectSubmitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_edu_homework_correct_submit(
        self,
        request: main_models.CreateEduHomeworkCorrectSubmitRequest,
    ) -> main_models.CreateEduHomeworkCorrectSubmitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_edu_homework_correct_submit_with_options(request, headers, runtime)

    async def create_edu_homework_correct_submit_async(
        self,
        request: main_models.CreateEduHomeworkCorrectSubmitRequest,
    ) -> main_models.CreateEduHomeworkCorrectSubmitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_edu_homework_correct_submit_with_options_async(request, headers, runtime)

    def create_edu_problem_solve_with_sse(
        self,
        tmp_req: main_models.CreateEduProblemSolveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.CreateEduProblemSolveResponse, None, None]:
        tmp_req.validate()
        request = main_models.CreateEduProblemSolveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'query', 'json')
        body = {}
        if not DaraCore.is_null(request.query_shrink):
            body['query'] = request.query_shrink
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEduProblemSolve',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/problem/solve/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.CreateEduProblemSolveResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def create_edu_problem_solve_with_sse_async(
        self,
        tmp_req: main_models.CreateEduProblemSolveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.CreateEduProblemSolveResponse, None, None]:
        tmp_req.validate()
        request = main_models.CreateEduProblemSolveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'query', 'json')
        body = {}
        if not DaraCore.is_null(request.query_shrink):
            body['query'] = request.query_shrink
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEduProblemSolve',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/problem/solve/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.CreateEduProblemSolveResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def create_edu_problem_solve_with_options(
        self,
        tmp_req: main_models.CreateEduProblemSolveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEduProblemSolveResponse:
        tmp_req.validate()
        request = main_models.CreateEduProblemSolveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'query', 'json')
        body = {}
        if not DaraCore.is_null(request.query_shrink):
            body['query'] = request.query_shrink
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEduProblemSolve',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/problem/solve/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEduProblemSolveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_edu_problem_solve_with_options_async(
        self,
        tmp_req: main_models.CreateEduProblemSolveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEduProblemSolveResponse:
        tmp_req.validate()
        request = main_models.CreateEduProblemSolveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'query', 'json')
        body = {}
        if not DaraCore.is_null(request.query_shrink):
            body['query'] = request.query_shrink
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEduProblemSolve',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/problem/solve/stream',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEduProblemSolveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_edu_problem_solve(
        self,
        request: main_models.CreateEduProblemSolveRequest,
    ) -> main_models.CreateEduProblemSolveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_edu_problem_solve_with_options(request, headers, runtime)

    async def create_edu_problem_solve_async(
        self,
        request: main_models.CreateEduProblemSolveRequest,
    ) -> main_models.CreateEduProblemSolveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_edu_problem_solve_with_options_async(request, headers, runtime)

    def get_edu_homework_correction_result_with_options(
        self,
        request: main_models.GetEduHomeworkCorrectionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEduHomeworkCorrectionResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEduHomeworkCorrectionResult',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/homework/correct/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEduHomeworkCorrectionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edu_homework_correction_result_with_options_async(
        self,
        request: main_models.GetEduHomeworkCorrectionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEduHomeworkCorrectionResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEduHomeworkCorrectionResult',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/homework/correct/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEduHomeworkCorrectionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edu_homework_correction_result(
        self,
        request: main_models.GetEduHomeworkCorrectionResultRequest,
    ) -> main_models.GetEduHomeworkCorrectionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_edu_homework_correction_result_with_options(request, headers, runtime)

    async def get_edu_homework_correction_result_async(
        self,
        request: main_models.GetEduHomeworkCorrectionResultRequest,
    ) -> main_models.GetEduHomeworkCorrectionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_edu_homework_correction_result_with_options_async(request, headers, runtime)

    def get_qwen_edu_api_activation_status_with_options(
        self,
        request: main_models.GetQwenEduApiActivationStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQwenEduApiActivationStatusResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetQwenEduApiActivationStatus',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/service/activation/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQwenEduApiActivationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qwen_edu_api_activation_status_with_options_async(
        self,
        request: main_models.GetQwenEduApiActivationStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQwenEduApiActivationStatusResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetQwenEduApiActivationStatus',
            version = '2026-11-02',
            protocol = 'HTTPS',
            pathname = f'/v1/service/activation/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQwenEduApiActivationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qwen_edu_api_activation_status(
        self,
        request: main_models.GetQwenEduApiActivationStatusRequest,
    ) -> main_models.GetQwenEduApiActivationStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_qwen_edu_api_activation_status_with_options(request, headers, runtime)

    async def get_qwen_edu_api_activation_status_async(
        self,
        request: main_models.GetQwenEduApiActivationStatusRequest,
    ) -> main_models.GetQwenEduApiActivationStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_qwen_edu_api_activation_status_with_options_async(request, headers, runtime)
