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

    def batch_get_medias_with_options(
        self,
        request: main_models.BatchGetMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetMedias',
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
            main_models.BatchGetMediasResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_medias_with_options_async(
        self,
        request: main_models.BatchGetMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetMedias',
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
            main_models.BatchGetMediasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_medias(
        self,
        request: main_models.BatchGetMediasRequest,
    ) -> main_models.BatchGetMediasResponse:
        runtime = RuntimeOptions()
        return self.batch_get_medias_with_options(request, runtime)

    async def batch_get_medias_async(
        self,
        request: main_models.BatchGetMediasRequest,
    ) -> main_models.BatchGetMediasResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_medias_with_options_async(request, runtime)

    def delete_medias_with_options(
        self,
        request: main_models.DeleteMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not DaraCore.is_null(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMedias',
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
            main_models.DeleteMediasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_medias_with_options_async(
        self,
        request: main_models.DeleteMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not DaraCore.is_null(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMedias',
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
            main_models.DeleteMediasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_medias(
        self,
        request: main_models.DeleteMediasRequest,
    ) -> main_models.DeleteMediasResponse:
        runtime = RuntimeOptions()
        return self.delete_medias_with_options(request, runtime)

    async def delete_medias_async(
        self,
        request: main_models.DeleteMediasRequest,
    ) -> main_models.DeleteMediasResponse:
        runtime = RuntimeOptions()
        return await self.delete_medias_with_options_async(request, runtime)

    def get_image_generation_job_with_options(
        self,
        request: main_models.GetImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageGenerationJob',
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
            main_models.GetImageGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_generation_job_with_options_async(
        self,
        request: main_models.GetImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageGenerationJob',
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
            main_models.GetImageGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_generation_job(
        self,
        request: main_models.GetImageGenerationJobRequest,
    ) -> main_models.GetImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.get_image_generation_job_with_options(request, runtime)

    async def get_image_generation_job_async(
        self,
        request: main_models.GetImageGenerationJobRequest,
    ) -> main_models.GetImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.get_image_generation_job_with_options_async(request, runtime)

    def get_media_with_options(
        self,
        request: main_models.GetMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMedia',
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
            main_models.GetMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_with_options_async(
        self,
        request: main_models.GetMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMedia',
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
            main_models.GetMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media(
        self,
        request: main_models.GetMediaRequest,
    ) -> main_models.GetMediaResponse:
        runtime = RuntimeOptions()
        return self.get_media_with_options(request, runtime)

    async def get_media_async(
        self,
        request: main_models.GetMediaRequest,
    ) -> main_models.GetMediaResponse:
        runtime = RuntimeOptions()
        return await self.get_media_with_options_async(request, runtime)

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

    def get_video_generation_job_with_options(
        self,
        request: main_models.GetVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoGenerationJob',
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
            main_models.GetVideoGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_generation_job_with_options_async(
        self,
        request: main_models.GetVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoGenerationJob',
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
            main_models.GetVideoGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_generation_job(
        self,
        request: main_models.GetVideoGenerationJobRequest,
    ) -> main_models.GetVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.get_video_generation_job_with_options(request, runtime)

    async def get_video_generation_job_async(
        self,
        request: main_models.GetVideoGenerationJobRequest,
    ) -> main_models.GetVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.get_video_generation_job_with_options_async(request, runtime)

    def import_media_with_options(
        self,
        request: main_models.ImportMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.import_source):
            query['ImportSource'] = request.import_source
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.register_config):
            query['RegisterConfig'] = request.register_config
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportMedia',
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
            main_models.ImportMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_media_with_options_async(
        self,
        request: main_models.ImportMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.import_source):
            query['ImportSource'] = request.import_source
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.register_config):
            query['RegisterConfig'] = request.register_config
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportMedia',
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
            main_models.ImportMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_media(
        self,
        request: main_models.ImportMediaRequest,
    ) -> main_models.ImportMediaResponse:
        runtime = RuntimeOptions()
        return self.import_media_with_options(request, runtime)

    async def import_media_async(
        self,
        request: main_models.ImportMediaRequest,
    ) -> main_models.ImportMediaResponse:
        runtime = RuntimeOptions()
        return await self.import_media_with_options_async(request, runtime)

    def submit_image_generation_job_with_options(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageGenerationJob',
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
            main_models.SubmitImageGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_generation_job_with_options_async(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageGenerationJob',
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
            main_models.SubmitImageGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_generation_job(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
    ) -> main_models.SubmitImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.submit_image_generation_job_with_options(request, runtime)

    async def submit_image_generation_job_async(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
    ) -> main_models.SubmitImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_image_generation_job_with_options_async(request, runtime)

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

    def submit_video_generation_job_with_options(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoGenerationJob',
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
            main_models.SubmitVideoGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_generation_job_with_options_async(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoGenerationJob',
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
            main_models.SubmitVideoGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_generation_job(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.submit_video_generation_job_with_options(request, runtime)

    async def submit_video_generation_job_async(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_video_generation_job_with_options_async(request, runtime)

    def update_media_with_options(
        self,
        request: main_models.UpdateMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMedia',
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
            main_models.UpdateMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_with_options_async(
        self,
        request: main_models.UpdateMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMedia',
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
            main_models.UpdateMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media(
        self,
        request: main_models.UpdateMediaRequest,
    ) -> main_models.UpdateMediaResponse:
        runtime = RuntimeOptions()
        return self.update_media_with_options(request, runtime)

    async def update_media_async(
        self,
        request: main_models.UpdateMediaRequest,
    ) -> main_models.UpdateMediaResponse:
        runtime = RuntimeOptions()
        return await self.update_media_with_options_async(request, runtime)
