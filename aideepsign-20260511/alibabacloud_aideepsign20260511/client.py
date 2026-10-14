# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aideepsign20260511 import models as main_models
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
        self._endpoint = self.get_endpoint('aideepsign', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_c2pa_bucket_sign_task_with_options(
        self,
        request: main_models.CancelC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelC2paBucketSignTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_c2pa_bucket_sign_task_with_options_async(
        self,
        request: main_models.CancelC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelC2paBucketSignTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_c2pa_bucket_sign_task(
        self,
        request: main_models.CancelC2paBucketSignTaskRequest,
    ) -> main_models.CancelC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_c2pa_bucket_sign_task_with_options(request, runtime)

    async def cancel_c2pa_bucket_sign_task_async(
        self,
        request: main_models.CancelC2paBucketSignTaskRequest,
    ) -> main_models.CancelC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_c2pa_bucket_sign_task_with_options_async(request, runtime)

    def create_c2pa_bucket_sign_task_with_options(
        self,
        request: main_models.CreateC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.bucket_region_id):
            query['BucketRegionId'] = request.bucket_region_id
        if not DaraCore.is_null(request.software_agent):
            query['SoftwareAgent'] = request.software_agent
        if not DaraCore.is_null(request.source_prefix):
            query['SourcePrefix'] = request.source_prefix
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateC2paBucketSignTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_c2pa_bucket_sign_task_with_options_async(
        self,
        request: main_models.CreateC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.bucket_region_id):
            query['BucketRegionId'] = request.bucket_region_id
        if not DaraCore.is_null(request.software_agent):
            query['SoftwareAgent'] = request.software_agent
        if not DaraCore.is_null(request.source_prefix):
            query['SourcePrefix'] = request.source_prefix
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateC2paBucketSignTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_c2pa_bucket_sign_task(
        self,
        request: main_models.CreateC2paBucketSignTaskRequest,
    ) -> main_models.CreateC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return self.create_c2pa_bucket_sign_task_with_options(request, runtime)

    async def create_c2pa_bucket_sign_task_async(
        self,
        request: main_models.CreateC2paBucketSignTaskRequest,
    ) -> main_models.CreateC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_c2pa_bucket_sign_task_with_options_async(request, runtime)

    def create_c2pa_sign_task_with_options(
        self,
        request: main_models.CreateC2paSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateC2paSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.software_agent):
            query['SoftwareAgent'] = request.software_agent
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateC2paSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateC2paSignTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_c2pa_sign_task_with_options_async(
        self,
        request: main_models.CreateC2paSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateC2paSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.software_agent):
            query['SoftwareAgent'] = request.software_agent
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateC2paSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateC2paSignTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_c2pa_sign_task(
        self,
        request: main_models.CreateC2paSignTaskRequest,
    ) -> main_models.CreateC2paSignTaskResponse:
        runtime = RuntimeOptions()
        return self.create_c2pa_sign_task_with_options(request, runtime)

    async def create_c2pa_sign_task_async(
        self,
        request: main_models.CreateC2paSignTaskRequest,
    ) -> main_models.CreateC2paSignTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_c2pa_sign_task_with_options_async(request, runtime)

    def create_image_defect_detection_task_with_options(
        self,
        request: main_models.CreateImageDefectDetectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageDefectDetectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageDefectDetectionTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageDefectDetectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_defect_detection_task_with_options_async(
        self,
        request: main_models.CreateImageDefectDetectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageDefectDetectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageDefectDetectionTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageDefectDetectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_defect_detection_task(
        self,
        request: main_models.CreateImageDefectDetectionTaskRequest,
    ) -> main_models.CreateImageDefectDetectionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_defect_detection_task_with_options(request, runtime)

    async def create_image_defect_detection_task_async(
        self,
        request: main_models.CreateImageDefectDetectionTaskRequest,
    ) -> main_models.CreateImageDefectDetectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_defect_detection_task_with_options_async(request, runtime)

    def create_image_detection_task_with_options(
        self,
        request: main_models.CreateImageDetectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageDetectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.detect_type):
            query['DetectType'] = request.detect_type
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.use_tamper_small_model):
            query['UseTamperSmallModel'] = request.use_tamper_small_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageDetectionTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageDetectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_detection_task_with_options_async(
        self,
        request: main_models.CreateImageDetectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageDetectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.detect_type):
            query['DetectType'] = request.detect_type
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.use_tamper_small_model):
            query['UseTamperSmallModel'] = request.use_tamper_small_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageDetectionTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageDetectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_detection_task(
        self,
        request: main_models.CreateImageDetectionTaskRequest,
    ) -> main_models.CreateImageDetectionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_detection_task_with_options(request, runtime)

    async def create_image_detection_task_async(
        self,
        request: main_models.CreateImageDetectionTaskRequest,
    ) -> main_models.CreateImageDetectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_detection_task_with_options_async(request, runtime)

    def create_image_income_tax_detection_task_with_options(
        self,
        request: main_models.CreateImageIncomeTaxDetectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageIncomeTaxDetectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageIncomeTaxDetectionTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageIncomeTaxDetectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_income_tax_detection_task_with_options_async(
        self,
        request: main_models.CreateImageIncomeTaxDetectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageIncomeTaxDetectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageIncomeTaxDetectionTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageIncomeTaxDetectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_income_tax_detection_task(
        self,
        request: main_models.CreateImageIncomeTaxDetectionTaskRequest,
    ) -> main_models.CreateImageIncomeTaxDetectionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_income_tax_detection_task_with_options(request, runtime)

    async def create_image_income_tax_detection_task_async(
        self,
        request: main_models.CreateImageIncomeTaxDetectionTaskRequest,
    ) -> main_models.CreateImageIncomeTaxDetectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_income_tax_detection_task_with_options_async(request, runtime)

    def create_image_task_with_options(
        self,
        request: main_models.CreateImageTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_extend):
            query['PromptExtend'] = request.prompt_extend
        if not DaraCore.is_null(request.seed):
            query['Seed'] = request.seed
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_task_with_options_async(
        self,
        request: main_models.CreateImageTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_extend):
            query['PromptExtend'] = request.prompt_extend
        if not DaraCore.is_null(request.seed):
            query['Seed'] = request.seed
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_task(
        self,
        request: main_models.CreateImageTaskRequest,
    ) -> main_models.CreateImageTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_task_with_options(request, runtime)

    async def create_image_task_async(
        self,
        request: main_models.CreateImageTaskRequest,
    ) -> main_models.CreateImageTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_task_with_options_async(request, runtime)

    def create_sensitive_scan_task_with_options(
        self,
        request: main_models.CreateSensitiveScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSensitiveScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSensitiveScanTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSensitiveScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sensitive_scan_task_with_options_async(
        self,
        request: main_models.CreateSensitiveScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSensitiveScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSensitiveScanTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSensitiveScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sensitive_scan_task(
        self,
        request: main_models.CreateSensitiveScanTaskRequest,
    ) -> main_models.CreateSensitiveScanTaskResponse:
        runtime = RuntimeOptions()
        return self.create_sensitive_scan_task_with_options(request, runtime)

    async def create_sensitive_scan_task_async(
        self,
        request: main_models.CreateSensitiveScanTaskRequest,
    ) -> main_models.CreateSensitiveScanTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_sensitive_scan_task_with_options_async(request, runtime)

    def create_video_task_with_options(
        self,
        request: main_models.CreateVideoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_extend):
            query['PromptExtend'] = request.prompt_extend
        if not DaraCore.is_null(request.ratio):
            query['Ratio'] = request.ratio
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.seed):
            query['Seed'] = request.seed
        if not DaraCore.is_null(request.watermark):
            query['Watermark'] = request.watermark
        if not DaraCore.is_null(request.media):
            query['Media'] = request.media
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_task_with_options_async(
        self,
        request: main_models.CreateVideoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_extend):
            query['PromptExtend'] = request.prompt_extend
        if not DaraCore.is_null(request.ratio):
            query['Ratio'] = request.ratio
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.seed):
            query['Seed'] = request.seed
        if not DaraCore.is_null(request.watermark):
            query['Watermark'] = request.watermark
        if not DaraCore.is_null(request.media):
            query['Media'] = request.media
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_task(
        self,
        request: main_models.CreateVideoTaskRequest,
    ) -> main_models.CreateVideoTaskResponse:
        runtime = RuntimeOptions()
        return self.create_video_task_with_options(request, runtime)

    async def create_video_task_async(
        self,
        request: main_models.CreateVideoTaskRequest,
    ) -> main_models.CreateVideoTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_video_task_with_options_async(request, runtime)

    def create_watermark_embed_task_with_options(
        self,
        request: main_models.CreateWatermarkEmbedTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWatermarkEmbedTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.reserved):
            query['Reserved'] = request.reserved
        if not DaraCore.is_null(request.watermark_content):
            query['WatermarkContent'] = request.watermark_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWatermarkEmbedTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWatermarkEmbedTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_watermark_embed_task_with_options_async(
        self,
        request: main_models.CreateWatermarkEmbedTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWatermarkEmbedTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.reserved):
            query['Reserved'] = request.reserved
        if not DaraCore.is_null(request.watermark_content):
            query['WatermarkContent'] = request.watermark_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWatermarkEmbedTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWatermarkEmbedTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_watermark_embed_task(
        self,
        request: main_models.CreateWatermarkEmbedTaskRequest,
    ) -> main_models.CreateWatermarkEmbedTaskResponse:
        runtime = RuntimeOptions()
        return self.create_watermark_embed_task_with_options(request, runtime)

    async def create_watermark_embed_task_async(
        self,
        request: main_models.CreateWatermarkEmbedTaskRequest,
    ) -> main_models.CreateWatermarkEmbedTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_watermark_embed_task_with_options_async(request, runtime)

    def create_watermark_extract_task_with_options(
        self,
        request: main_models.CreateWatermarkExtractTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWatermarkExtractTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.reserved):
            query['Reserved'] = request.reserved
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWatermarkExtractTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWatermarkExtractTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_watermark_extract_task_with_options_async(
        self,
        request: main_models.CreateWatermarkExtractTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWatermarkExtractTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.reserved):
            query['Reserved'] = request.reserved
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWatermarkExtractTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWatermarkExtractTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_watermark_extract_task(
        self,
        request: main_models.CreateWatermarkExtractTaskRequest,
    ) -> main_models.CreateWatermarkExtractTaskResponse:
        runtime = RuntimeOptions()
        return self.create_watermark_extract_task_with_options(request, runtime)

    async def create_watermark_extract_task_async(
        self,
        request: main_models.CreateWatermarkExtractTaskRequest,
    ) -> main_models.CreateWatermarkExtractTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_watermark_extract_task_with_options_async(request, runtime)

    def detect_aigc_image_with_options(
        self,
        request: main_models.DetectAigcImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectAigcImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectAigcImage',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectAigcImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_aigc_image_with_options_async(
        self,
        request: main_models.DetectAigcImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectAigcImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectAigcImage',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectAigcImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_aigc_image(
        self,
        request: main_models.DetectAigcImageRequest,
    ) -> main_models.DetectAigcImageResponse:
        runtime = RuntimeOptions()
        return self.detect_aigc_image_with_options(request, runtime)

    async def detect_aigc_image_async(
        self,
        request: main_models.DetectAigcImageRequest,
    ) -> main_models.DetectAigcImageResponse:
        runtime = RuntimeOptions()
        return await self.detect_aigc_image_with_options_async(request, runtime)

    def detect_image_basic_info_with_options(
        self,
        request: main_models.DetectImageBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageBasicInfo',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_basic_info_with_options_async(
        self,
        request: main_models.DetectImageBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageBasicInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageBasicInfo',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_basic_info(
        self,
        request: main_models.DetectImageBasicInfoRequest,
    ) -> main_models.DetectImageBasicInfoResponse:
        runtime = RuntimeOptions()
        return self.detect_image_basic_info_with_options(request, runtime)

    async def detect_image_basic_info_async(
        self,
        request: main_models.DetectImageBasicInfoRequest,
    ) -> main_models.DetectImageBasicInfoResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_basic_info_with_options_async(request, runtime)

    def get_c2pa_sign_result_with_options(
        self,
        request: main_models.GetC2paSignResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetC2paSignResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetC2paSignResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetC2paSignResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_c2pa_sign_result_with_options_async(
        self,
        request: main_models.GetC2paSignResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetC2paSignResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetC2paSignResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetC2paSignResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_c2pa_sign_result(
        self,
        request: main_models.GetC2paSignResultRequest,
    ) -> main_models.GetC2paSignResultResponse:
        runtime = RuntimeOptions()
        return self.get_c2pa_sign_result_with_options(request, runtime)

    async def get_c2pa_sign_result_async(
        self,
        request: main_models.GetC2paSignResultRequest,
    ) -> main_models.GetC2paSignResultResponse:
        runtime = RuntimeOptions()
        return await self.get_c2pa_sign_result_with_options_async(request, runtime)

    def get_image_defect_detection_task_result_with_options(
        self,
        request: main_models.GetImageDefectDetectionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageDefectDetectionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageDefectDetectionTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageDefectDetectionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_defect_detection_task_result_with_options_async(
        self,
        request: main_models.GetImageDefectDetectionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageDefectDetectionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageDefectDetectionTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageDefectDetectionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_defect_detection_task_result(
        self,
        request: main_models.GetImageDefectDetectionTaskResultRequest,
    ) -> main_models.GetImageDefectDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_image_defect_detection_task_result_with_options(request, runtime)

    async def get_image_defect_detection_task_result_async(
        self,
        request: main_models.GetImageDefectDetectionTaskResultRequest,
    ) -> main_models.GetImageDefectDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_image_defect_detection_task_result_with_options_async(request, runtime)

    def get_image_detection_task_result_with_options(
        self,
        request: main_models.GetImageDetectionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageDetectionTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageDetectionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_detection_task_result_with_options_async(
        self,
        request: main_models.GetImageDetectionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageDetectionTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageDetectionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_detection_task_result(
        self,
        request: main_models.GetImageDetectionTaskResultRequest,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_image_detection_task_result_with_options(request, runtime)

    async def get_image_detection_task_result_async(
        self,
        request: main_models.GetImageDetectionTaskResultRequest,
    ) -> main_models.GetImageDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_image_detection_task_result_with_options_async(request, runtime)

    def get_image_income_tax_detection_task_result_with_options(
        self,
        request: main_models.GetImageIncomeTaxDetectionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageIncomeTaxDetectionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageIncomeTaxDetectionTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageIncomeTaxDetectionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_income_tax_detection_task_result_with_options_async(
        self,
        request: main_models.GetImageIncomeTaxDetectionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageIncomeTaxDetectionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageIncomeTaxDetectionTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageIncomeTaxDetectionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_income_tax_detection_task_result(
        self,
        request: main_models.GetImageIncomeTaxDetectionTaskResultRequest,
    ) -> main_models.GetImageIncomeTaxDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_image_income_tax_detection_task_result_with_options(request, runtime)

    async def get_image_income_tax_detection_task_result_async(
        self,
        request: main_models.GetImageIncomeTaxDetectionTaskResultRequest,
    ) -> main_models.GetImageIncomeTaxDetectionTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_image_income_tax_detection_task_result_with_options_async(request, runtime)

    def get_image_task_result_with_options(
        self,
        request: main_models.GetImageTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_task_result_with_options_async(
        self,
        request: main_models.GetImageTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_task_result(
        self,
        request: main_models.GetImageTaskResultRequest,
    ) -> main_models.GetImageTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_image_task_result_with_options(request, runtime)

    async def get_image_task_result_async(
        self,
        request: main_models.GetImageTaskResultRequest,
    ) -> main_models.GetImageTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_image_task_result_with_options_async(request, runtime)

    def get_sensitive_scan_result_with_options(
        self,
        request: main_models.GetSensitiveScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSensitiveScanResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSensitiveScanResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSensitiveScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sensitive_scan_result_with_options_async(
        self,
        request: main_models.GetSensitiveScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSensitiveScanResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSensitiveScanResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSensitiveScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sensitive_scan_result(
        self,
        request: main_models.GetSensitiveScanResultRequest,
    ) -> main_models.GetSensitiveScanResultResponse:
        runtime = RuntimeOptions()
        return self.get_sensitive_scan_result_with_options(request, runtime)

    async def get_sensitive_scan_result_async(
        self,
        request: main_models.GetSensitiveScanResultRequest,
    ) -> main_models.GetSensitiveScanResultResponse:
        runtime = RuntimeOptions()
        return await self.get_sensitive_scan_result_with_options_async(request, runtime)

    def get_video_task_result_with_options(
        self,
        request: main_models.GetVideoTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_task_result_with_options_async(
        self,
        request: main_models.GetVideoTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_task_result(
        self,
        request: main_models.GetVideoTaskResultRequest,
    ) -> main_models.GetVideoTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_video_task_result_with_options(request, runtime)

    async def get_video_task_result_async(
        self,
        request: main_models.GetVideoTaskResultRequest,
    ) -> main_models.GetVideoTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_video_task_result_with_options_async(request, runtime)

    def get_watermark_embed_task_result_with_options(
        self,
        request: main_models.GetWatermarkEmbedTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWatermarkEmbedTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWatermarkEmbedTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWatermarkEmbedTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_watermark_embed_task_result_with_options_async(
        self,
        request: main_models.GetWatermarkEmbedTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWatermarkEmbedTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWatermarkEmbedTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWatermarkEmbedTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_watermark_embed_task_result(
        self,
        request: main_models.GetWatermarkEmbedTaskResultRequest,
    ) -> main_models.GetWatermarkEmbedTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_watermark_embed_task_result_with_options(request, runtime)

    async def get_watermark_embed_task_result_async(
        self,
        request: main_models.GetWatermarkEmbedTaskResultRequest,
    ) -> main_models.GetWatermarkEmbedTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_watermark_embed_task_result_with_options_async(request, runtime)

    def get_watermark_extract_task_result_with_options(
        self,
        request: main_models.GetWatermarkExtractTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWatermarkExtractTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWatermarkExtractTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWatermarkExtractTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_watermark_extract_task_result_with_options_async(
        self,
        request: main_models.GetWatermarkExtractTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWatermarkExtractTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWatermarkExtractTaskResult',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWatermarkExtractTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_watermark_extract_task_result(
        self,
        request: main_models.GetWatermarkExtractTaskResultRequest,
    ) -> main_models.GetWatermarkExtractTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_watermark_extract_task_result_with_options(request, runtime)

    async def get_watermark_extract_task_result_async(
        self,
        request: main_models.GetWatermarkExtractTaskResultRequest,
    ) -> main_models.GetWatermarkExtractTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_watermark_extract_task_result_with_options_async(request, runtime)

    def pause_c2pa_bucket_sign_task_with_options(
        self,
        request: main_models.PauseC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseC2paBucketSignTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_c2pa_bucket_sign_task_with_options_async(
        self,
        request: main_models.PauseC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseC2paBucketSignTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_c2pa_bucket_sign_task(
        self,
        request: main_models.PauseC2paBucketSignTaskRequest,
    ) -> main_models.PauseC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return self.pause_c2pa_bucket_sign_task_with_options(request, runtime)

    async def pause_c2pa_bucket_sign_task_async(
        self,
        request: main_models.PauseC2paBucketSignTaskRequest,
    ) -> main_models.PauseC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return await self.pause_c2pa_bucket_sign_task_with_options_async(request, runtime)

    def resume_c2pa_bucket_sign_task_with_options(
        self,
        request: main_models.ResumeC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeC2paBucketSignTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_c2pa_bucket_sign_task_with_options_async(
        self,
        request: main_models.ResumeC2paBucketSignTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeC2paBucketSignTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeC2paBucketSignTask',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeC2paBucketSignTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_c2pa_bucket_sign_task(
        self,
        request: main_models.ResumeC2paBucketSignTaskRequest,
    ) -> main_models.ResumeC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return self.resume_c2pa_bucket_sign_task_with_options(request, runtime)

    async def resume_c2pa_bucket_sign_task_async(
        self,
        request: main_models.ResumeC2paBucketSignTaskRequest,
    ) -> main_models.ResumeC2paBucketSignTaskResponse:
        runtime = RuntimeOptions()
        return await self.resume_c2pa_bucket_sign_task_with_options_async(request, runtime)

    def sign_user_image_with_options(
        self,
        request: main_models.SignUserImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignUserImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignUserImage',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignUserImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_user_image_with_options_async(
        self,
        request: main_models.SignUserImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignUserImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignUserImage',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignUserImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign_user_image(
        self,
        request: main_models.SignUserImageRequest,
    ) -> main_models.SignUserImageResponse:
        runtime = RuntimeOptions()
        return self.sign_user_image_with_options(request, runtime)

    async def sign_user_image_async(
        self,
        request: main_models.SignUserImageRequest,
    ) -> main_models.SignUserImageResponse:
        runtime = RuntimeOptions()
        return await self.sign_user_image_with_options_async(request, runtime)

    def verify_image_signature_with_options(
        self,
        request: main_models.VerifyImageSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyImageSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyImageSignature',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyImageSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_image_signature_with_options_async(
        self,
        request: main_models.VerifyImageSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyImageSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyImageSignature',
            version = '2026-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyImageSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_image_signature(
        self,
        request: main_models.VerifyImageSignatureRequest,
    ) -> main_models.VerifyImageSignatureResponse:
        runtime = RuntimeOptions()
        return self.verify_image_signature_with_options(request, runtime)

    async def verify_image_signature_async(
        self,
        request: main_models.VerifyImageSignatureRequest,
    ) -> main_models.VerifyImageSignatureResponse:
        runtime = RuntimeOptions()
        return await self.verify_image_signature_with_options_async(request, runtime)
