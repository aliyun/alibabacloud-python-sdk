# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_intelligentcreation20260101 import models as main_models
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
        self._endpoint = self.get_endpoint('intelligentcreation', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_turing_task_with_options(
        self,
        request: main_models.CheckTuringTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckTuringTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckTuringTask',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = f'/yic/aigc-turing/openService/v1/task/checkTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTuringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_turing_task_with_options_async(
        self,
        request: main_models.CheckTuringTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckTuringTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckTuringTask',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = f'/yic/aigc-turing/openService/v1/task/checkTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTuringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_turing_task(
        self,
        request: main_models.CheckTuringTaskRequest,
    ) -> main_models.CheckTuringTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_turing_task_with_options(request, headers, runtime)

    async def check_turing_task_async(
        self,
        request: main_models.CheckTuringTaskRequest,
    ) -> main_models.CheckTuringTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_turing_task_with_options_async(request, headers, runtime)

    def submit_turing_task_with_options(
        self,
        request: main_models.SubmitTuringTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTuringTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        if not DaraCore.is_null(request.idempotent_key):
            body['idempotentKey'] = request.idempotent_key
        if not DaraCore.is_null(request.img_url):
            body['imgUrl'] = request.img_url
        if not DaraCore.is_null(request.resolution):
            body['resolution'] = request.resolution
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTuringTask',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = f'/yic/aigc-turing/openService/v1/task/submitTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTuringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_turing_task_with_options_async(
        self,
        request: main_models.SubmitTuringTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTuringTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        if not DaraCore.is_null(request.idempotent_key):
            body['idempotentKey'] = request.idempotent_key
        if not DaraCore.is_null(request.img_url):
            body['imgUrl'] = request.img_url
        if not DaraCore.is_null(request.resolution):
            body['resolution'] = request.resolution
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTuringTask',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = f'/yic/aigc-turing/openService/v1/task/submitTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTuringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_turing_task(
        self,
        request: main_models.SubmitTuringTaskRequest,
    ) -> main_models.SubmitTuringTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_turing_task_with_options(request, headers, runtime)

    async def submit_turing_task_async(
        self,
        request: main_models.SubmitTuringTaskRequest,
    ) -> main_models.SubmitTuringTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_turing_task_with_options_async(request, headers, runtime)
