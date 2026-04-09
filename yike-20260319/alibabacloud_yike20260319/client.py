# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_yike20260319 import models as main_models
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

    def batch_get_yike_aiapp_job_with_options(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_yike_aiapp_job_with_options_async(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_yike_aiapp_job(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.batch_get_yike_aiapp_job_with_options(request, runtime)

    async def batch_get_yike_aiapp_job_async(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_yike_aiapp_job_with_options_async(request, runtime)

    def create_yike_asset_upload_with_options(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeAssetUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_ext):
            query['FileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeAssetUpload',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeAssetUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_yike_asset_upload_with_options_async(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeAssetUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_ext):
            query['FileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeAssetUpload',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeAssetUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_yike_asset_upload(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
    ) -> main_models.CreateYikeAssetUploadResponse:
        runtime = RuntimeOptions()
        return self.create_yike_asset_upload_with_options(request, runtime)

    async def create_yike_asset_upload_async(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
    ) -> main_models.CreateYikeAssetUploadResponse:
        runtime = RuntimeOptions()
        return await self.create_yike_asset_upload_with_options_async(request, runtime)

    def get_yike_aiapp_job_with_options(
        self,
        request: main_models.GetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_aiapp_job_with_options_async(
        self,
        request: main_models.GetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_aiapp_job(
        self,
        request: main_models.GetYikeAIAppJobRequest,
    ) -> main_models.GetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.get_yike_aiapp_job_with_options(request, runtime)

    async def get_yike_aiapp_job_async(
        self,
        request: main_models.GetYikeAIAppJobRequest,
    ) -> main_models.GetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_aiapp_job_with_options_async(request, runtime)

    def get_yike_storyboard_job_with_options(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeStoryboardJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_storyboard_job_with_options_async(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeStoryboardJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_storyboard_job(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
    ) -> main_models.GetYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return self.get_yike_storyboard_job_with_options(request, runtime)

    async def get_yike_storyboard_job_async(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
    ) -> main_models.GetYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_storyboard_job_with_options_async(request, runtime)

    def submit_yike_aiapp_job_with_options(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_params):
            body['AppParams'] = request.app_params
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.production_id):
            body['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_yike_aiapp_job_with_options_async(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_params):
            body['AppParams'] = request.app_params
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.production_id):
            body['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_yike_aiapp_job(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.submit_yike_aiapp_job_with_options(request, runtime)

    async def submit_yike_aiapp_job_async(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_yike_aiapp_job_with_options_async(request, runtime)

    def submit_yike_storyboard_job_with_options(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.exec_mode):
            query['ExecMode'] = request.exec_mode
        if not DaraCore.is_null(request.model_params):
            query['ModelParams'] = request.model_params
        if not DaraCore.is_null(request.narration_voice_id):
            query['NarrationVoiceId'] = request.narration_voice_id
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.shot_prompt_mode):
            query['ShotPromptMode'] = request.shot_prompt_mode
        if not DaraCore.is_null(request.skip_failure_shot):
            query['SkipFailureShot'] = request.skip_failure_shot
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_model):
            query['VideoModel'] = request.video_model
        body = {}
        if not DaraCore.is_null(request.file_url):
            body['FileURL'] = request.file_url
        if not DaraCore.is_null(request.shot_split_mode):
            body['ShotSplitMode'] = request.shot_split_mode
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.style_id):
            body['StyleId'] = request.style_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeStoryboardJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_yike_storyboard_job_with_options_async(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.exec_mode):
            query['ExecMode'] = request.exec_mode
        if not DaraCore.is_null(request.model_params):
            query['ModelParams'] = request.model_params
        if not DaraCore.is_null(request.narration_voice_id):
            query['NarrationVoiceId'] = request.narration_voice_id
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.shot_prompt_mode):
            query['ShotPromptMode'] = request.shot_prompt_mode
        if not DaraCore.is_null(request.skip_failure_shot):
            query['SkipFailureShot'] = request.skip_failure_shot
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_model):
            query['VideoModel'] = request.video_model
        body = {}
        if not DaraCore.is_null(request.file_url):
            body['FileURL'] = request.file_url
        if not DaraCore.is_null(request.shot_split_mode):
            body['ShotSplitMode'] = request.shot_split_mode
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.style_id):
            body['StyleId'] = request.style_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeStoryboardJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_yike_storyboard_job(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return self.submit_yike_storyboard_job_with_options(request, runtime)

    async def submit_yike_storyboard_job_async(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_yike_storyboard_job_with_options_async(request, runtime)
