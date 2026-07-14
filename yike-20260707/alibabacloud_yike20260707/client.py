# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_yike20260707 import models as main_models
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
        self._endpoint_map = {
            'cn-shanghai': 'yike.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'yike.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('yike', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_media_comprehension_job_with_options(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaComprehensionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_comprehension_job_with_options_async(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaComprehensionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_comprehension_job(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
    ) -> main_models.GetMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return self.get_media_comprehension_job_with_options(request, runtime)

    async def get_media_comprehension_job_async(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
    ) -> main_models.GetMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return await self.get_media_comprehension_job_with_options_async(request, runtime)

    def submit_media_comprehension_job_with_options(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_params):
            query['JobParams'] = request.job_params
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaComprehensionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_comprehension_job_with_options_async(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_params):
            query['JobParams'] = request.job_params
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaComprehensionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_comprehension_job(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return self.submit_media_comprehension_job_with_options(request, runtime)

    async def submit_media_comprehension_job_async(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_media_comprehension_job_with_options_async(request, runtime)
