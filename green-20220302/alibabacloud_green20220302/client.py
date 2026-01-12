# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_green20220302 import models as main_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_file_moderation_result_with_options(
        self,
        request: main_models.DescribeFileModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_moderation_result_with_options_async(
        self,
        request: main_models.DescribeFileModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_moderation_result(
        self,
        request: main_models.DescribeFileModerationResultRequest,
    ) -> main_models.DescribeFileModerationResultResponse:
        runtime = RuntimeOptions()
        return self.describe_file_moderation_result_with_options(request, runtime)

    async def describe_file_moderation_result_async(
        self,
        request: main_models.DescribeFileModerationResultRequest,
    ) -> main_models.DescribeFileModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_file_moderation_result_with_options_async(request, runtime)

    def describe_image_moderation_result_with_options(
        self,
        request: main_models.DescribeImageModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_moderation_result_with_options_async(
        self,
        request: main_models.DescribeImageModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_moderation_result(
        self,
        request: main_models.DescribeImageModerationResultRequest,
    ) -> main_models.DescribeImageModerationResultResponse:
        runtime = RuntimeOptions()
        return self.describe_image_moderation_result_with_options(request, runtime)

    async def describe_image_moderation_result_async(
        self,
        request: main_models.DescribeImageModerationResultRequest,
    ) -> main_models.DescribeImageModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_image_moderation_result_with_options_async(request, runtime)

    def describe_image_result_ext_with_options(
        self,
        request: main_models.DescribeImageResultExtRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageResultExtResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.info_type):
            body['InfoType'] = request.info_type
        if not DaraCore.is_null(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageResultExt',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageResultExtResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_result_ext_with_options_async(
        self,
        request: main_models.DescribeImageResultExtRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeImageResultExtResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.info_type):
            body['InfoType'] = request.info_type
        if not DaraCore.is_null(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeImageResultExt',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeImageResultExtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_result_ext(
        self,
        request: main_models.DescribeImageResultExtRequest,
    ) -> main_models.DescribeImageResultExtResponse:
        runtime = RuntimeOptions()
        return self.describe_image_result_ext_with_options(request, runtime)

    async def describe_image_result_ext_async(
        self,
        request: main_models.DescribeImageResultExtRequest,
    ) -> main_models.DescribeImageResultExtResponse:
        runtime = RuntimeOptions()
        return await self.describe_image_result_ext_with_options_async(request, runtime)

    def describe_multimodal_moderation_result_with_options(
        self,
        request: main_models.DescribeMultimodalModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultimodalModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultimodalModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultimodalModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multimodal_moderation_result_with_options_async(
        self,
        request: main_models.DescribeMultimodalModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultimodalModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultimodalModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultimodalModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multimodal_moderation_result(
        self,
        request: main_models.DescribeMultimodalModerationResultRequest,
    ) -> main_models.DescribeMultimodalModerationResultResponse:
        runtime = RuntimeOptions()
        return self.describe_multimodal_moderation_result_with_options(request, runtime)

    async def describe_multimodal_moderation_result_async(
        self,
        request: main_models.DescribeMultimodalModerationResultRequest,
    ) -> main_models.DescribeMultimodalModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_multimodal_moderation_result_with_options_async(request, runtime)

    def describe_upload_token_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUploadTokenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUploadToken',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upload_token_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUploadTokenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeUploadToken',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_upload_token(self) -> main_models.DescribeUploadTokenResponse:
        runtime = RuntimeOptions()
        return self.describe_upload_token_with_options(runtime)

    async def describe_upload_token_async(self) -> main_models.DescribeUploadTokenResponse:
        runtime = RuntimeOptions()
        return await self.describe_upload_token_with_options_async(runtime)

    def describe_url_moderation_result_with_options(
        self,
        request: main_models.DescribeUrlModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUrlModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUrlModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUrlModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_url_moderation_result_with_options_async(
        self,
        request: main_models.DescribeUrlModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUrlModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUrlModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUrlModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_url_moderation_result(
        self,
        request: main_models.DescribeUrlModerationResultRequest,
    ) -> main_models.DescribeUrlModerationResultResponse:
        runtime = RuntimeOptions()
        return self.describe_url_moderation_result_with_options(request, runtime)

    async def describe_url_moderation_result_async(
        self,
        request: main_models.DescribeUrlModerationResultRequest,
    ) -> main_models.DescribeUrlModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_url_moderation_result_with_options_async(request, runtime)

    def file_moderation_with_options(
        self,
        request: main_models.FileModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FileModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_moderation_with_options_async(
        self,
        request: main_models.FileModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FileModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_moderation(
        self,
        request: main_models.FileModerationRequest,
    ) -> main_models.FileModerationResponse:
        runtime = RuntimeOptions()
        return self.file_moderation_with_options(request, runtime)

    async def file_moderation_async(
        self,
        request: main_models.FileModerationRequest,
    ) -> main_models.FileModerationResponse:
        runtime = RuntimeOptions()
        return await self.file_moderation_with_options_async(request, runtime)

    def image_async_moderation_with_options(
        self,
        request: main_models.ImageAsyncModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageAsyncModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageAsyncModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_async_moderation_with_options_async(
        self,
        request: main_models.ImageAsyncModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageAsyncModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageAsyncModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageAsyncModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_async_moderation(
        self,
        request: main_models.ImageAsyncModerationRequest,
    ) -> main_models.ImageAsyncModerationResponse:
        runtime = RuntimeOptions()
        return self.image_async_moderation_with_options(request, runtime)

    async def image_async_moderation_async(
        self,
        request: main_models.ImageAsyncModerationRequest,
    ) -> main_models.ImageAsyncModerationResponse:
        runtime = RuntimeOptions()
        return await self.image_async_moderation_with_options_async(request, runtime)

    def image_batch_moderation_with_options(
        self,
        request: main_models.ImageBatchModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageBatchModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageBatchModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageBatchModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_batch_moderation_with_options_async(
        self,
        request: main_models.ImageBatchModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageBatchModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageBatchModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageBatchModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_batch_moderation(
        self,
        request: main_models.ImageBatchModerationRequest,
    ) -> main_models.ImageBatchModerationResponse:
        runtime = RuntimeOptions()
        return self.image_batch_moderation_with_options(request, runtime)

    async def image_batch_moderation_async(
        self,
        request: main_models.ImageBatchModerationRequest,
    ) -> main_models.ImageBatchModerationResponse:
        runtime = RuntimeOptions()
        return await self.image_batch_moderation_with_options_async(request, runtime)

    def image_moderation_with_options(
        self,
        request: main_models.ImageModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImageModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_moderation_with_options_async(
        self,
        request: main_models.ImageModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImageModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_moderation(
        self,
        request: main_models.ImageModerationRequest,
    ) -> main_models.ImageModerationResponse:
        runtime = RuntimeOptions()
        return self.image_moderation_with_options(request, runtime)

    async def image_moderation_async(
        self,
        request: main_models.ImageModerationRequest,
    ) -> main_models.ImageModerationResponse:
        runtime = RuntimeOptions()
        return await self.image_moderation_with_options_async(request, runtime)

    def image_queue_moderation_with_options(
        self,
        request: main_models.ImageQueueModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageQueueModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImageQueueModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageQueueModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_queue_moderation_with_options_async(
        self,
        request: main_models.ImageQueueModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageQueueModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImageQueueModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageQueueModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_queue_moderation(
        self,
        request: main_models.ImageQueueModerationRequest,
    ) -> main_models.ImageQueueModerationResponse:
        runtime = RuntimeOptions()
        return self.image_queue_moderation_with_options(request, runtime)

    async def image_queue_moderation_async(
        self,
        request: main_models.ImageQueueModerationRequest,
    ) -> main_models.ImageQueueModerationResponse:
        runtime = RuntimeOptions()
        return await self.image_queue_moderation_with_options_async(request, runtime)

    def manual_callback_with_options(
        self,
        request: main_models.ManualCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualCallbackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.checksum):
            body['Checksum'] = request.checksum
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.msg):
            body['Msg'] = request.msg
        if not DaraCore.is_null(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManualCallback',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_callback_with_options_async(
        self,
        request: main_models.ManualCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualCallbackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.checksum):
            body['Checksum'] = request.checksum
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.msg):
            body['Msg'] = request.msg
        if not DaraCore.is_null(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManualCallback',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_callback(
        self,
        request: main_models.ManualCallbackRequest,
    ) -> main_models.ManualCallbackResponse:
        runtime = RuntimeOptions()
        return self.manual_callback_with_options(request, runtime)

    async def manual_callback_async(
        self,
        request: main_models.ManualCallbackRequest,
    ) -> main_models.ManualCallbackResponse:
        runtime = RuntimeOptions()
        return await self.manual_callback_with_options_async(request, runtime)

    def manual_moderation_with_options(
        self,
        request: main_models.ManualModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManualModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_moderation_with_options_async(
        self,
        request: main_models.ManualModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManualModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_moderation(
        self,
        request: main_models.ManualModerationRequest,
    ) -> main_models.ManualModerationResponse:
        runtime = RuntimeOptions()
        return self.manual_moderation_with_options(request, runtime)

    async def manual_moderation_async(
        self,
        request: main_models.ManualModerationRequest,
    ) -> main_models.ManualModerationResponse:
        runtime = RuntimeOptions()
        return await self.manual_moderation_with_options_async(request, runtime)

    def manual_moderation_result_with_options(
        self,
        request: main_models.ManualModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManualModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_moderation_result_with_options_async(
        self,
        request: main_models.ManualModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManualModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_moderation_result(
        self,
        request: main_models.ManualModerationResultRequest,
    ) -> main_models.ManualModerationResultResponse:
        runtime = RuntimeOptions()
        return self.manual_moderation_result_with_options(request, runtime)

    async def manual_moderation_result_async(
        self,
        request: main_models.ManualModerationResultRequest,
    ) -> main_models.ManualModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.manual_moderation_result_with_options_async(request, runtime)

    def multi_modal_agent_with_options(
        self,
        request: main_models.MultiModalAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MultiModalAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppID'] = request.app_id
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MultiModalAgent',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultiModalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def multi_modal_agent_with_options_async(
        self,
        request: main_models.MultiModalAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MultiModalAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppID'] = request.app_id
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MultiModalAgent',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultiModalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def multi_modal_agent(
        self,
        request: main_models.MultiModalAgentRequest,
    ) -> main_models.MultiModalAgentResponse:
        runtime = RuntimeOptions()
        return self.multi_modal_agent_with_options(request, runtime)

    async def multi_modal_agent_async(
        self,
        request: main_models.MultiModalAgentRequest,
    ) -> main_models.MultiModalAgentResponse:
        runtime = RuntimeOptions()
        return await self.multi_modal_agent_with_options_async(request, runtime)

    def multi_modal_guard_with_options(
        self,
        request: main_models.MultiModalGuardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MultiModalGuardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MultiModalGuard',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultiModalGuardResponse(),
            self.call_api(params, req, runtime)
        )

    async def multi_modal_guard_with_options_async(
        self,
        request: main_models.MultiModalGuardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MultiModalGuardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MultiModalGuard',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultiModalGuardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def multi_modal_guard(
        self,
        request: main_models.MultiModalGuardRequest,
    ) -> main_models.MultiModalGuardResponse:
        runtime = RuntimeOptions()
        return self.multi_modal_guard_with_options(request, runtime)

    async def multi_modal_guard_async(
        self,
        request: main_models.MultiModalGuardRequest,
    ) -> main_models.MultiModalGuardResponse:
        runtime = RuntimeOptions()
        return await self.multi_modal_guard_with_options_async(request, runtime)

    def multi_modal_guard_for_base_64with_options(
        self,
        request: main_models.MultiModalGuardForBase64Request,
        runtime: RuntimeOptions,
    ) -> main_models.MultiModalGuardForBase64Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        body = {}
        if not DaraCore.is_null(request.image_base_64str):
            body['ImageBase64Str'] = request.image_base_64str
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MultiModalGuardForBase64',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultiModalGuardForBase64Response(),
            self.call_api(params, req, runtime)
        )

    async def multi_modal_guard_for_base_64with_options_async(
        self,
        request: main_models.MultiModalGuardForBase64Request,
        runtime: RuntimeOptions,
    ) -> main_models.MultiModalGuardForBase64Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        body = {}
        if not DaraCore.is_null(request.image_base_64str):
            body['ImageBase64Str'] = request.image_base_64str
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MultiModalGuardForBase64',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultiModalGuardForBase64Response(),
            await self.call_api_async(params, req, runtime)
        )

    def multi_modal_guard_for_base_64(
        self,
        request: main_models.MultiModalGuardForBase64Request,
    ) -> main_models.MultiModalGuardForBase64Response:
        runtime = RuntimeOptions()
        return self.multi_modal_guard_for_base_64with_options(request, runtime)

    async def multi_modal_guard_for_base_64_async(
        self,
        request: main_models.MultiModalGuardForBase64Request,
    ) -> main_models.MultiModalGuardForBase64Response:
        runtime = RuntimeOptions()
        return await self.multi_modal_guard_for_base_64with_options_async(request, runtime)

    def multimodal_async_moderation_with_options(
        self,
        request: main_models.MultimodalAsyncModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MultimodalAsyncModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MultimodalAsyncModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultimodalAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def multimodal_async_moderation_with_options_async(
        self,
        request: main_models.MultimodalAsyncModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MultimodalAsyncModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MultimodalAsyncModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MultimodalAsyncModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def multimodal_async_moderation(
        self,
        request: main_models.MultimodalAsyncModerationRequest,
    ) -> main_models.MultimodalAsyncModerationResponse:
        runtime = RuntimeOptions()
        return self.multimodal_async_moderation_with_options(request, runtime)

    async def multimodal_async_moderation_async(
        self,
        request: main_models.MultimodalAsyncModerationRequest,
    ) -> main_models.MultimodalAsyncModerationResponse:
        runtime = RuntimeOptions()
        return await self.multimodal_async_moderation_with_options_async(request, runtime)

    def text_moderation_with_options(
        self,
        request: main_models.TextModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_moderation_with_options_async(
        self,
        request: main_models.TextModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_moderation(
        self,
        request: main_models.TextModerationRequest,
    ) -> main_models.TextModerationResponse:
        runtime = RuntimeOptions()
        return self.text_moderation_with_options(request, runtime)

    async def text_moderation_async(
        self,
        request: main_models.TextModerationRequest,
    ) -> main_models.TextModerationResponse:
        runtime = RuntimeOptions()
        return await self.text_moderation_with_options_async(request, runtime)

    def text_moderation_plus_with_options(
        self,
        request: main_models.TextModerationPlusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextModerationPlusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextModerationPlus',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextModerationPlusResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_moderation_plus_with_options_async(
        self,
        request: main_models.TextModerationPlusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextModerationPlusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextModerationPlus',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextModerationPlusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_moderation_plus(
        self,
        request: main_models.TextModerationPlusRequest,
    ) -> main_models.TextModerationPlusResponse:
        runtime = RuntimeOptions()
        return self.text_moderation_plus_with_options(request, runtime)

    async def text_moderation_plus_async(
        self,
        request: main_models.TextModerationPlusRequest,
    ) -> main_models.TextModerationPlusResponse:
        runtime = RuntimeOptions()
        return await self.text_moderation_plus_with_options_async(request, runtime)

    def url_async_moderation_with_options(
        self,
        request: main_models.UrlAsyncModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UrlAsyncModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UrlAsyncModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UrlAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def url_async_moderation_with_options_async(
        self,
        request: main_models.UrlAsyncModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UrlAsyncModerationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UrlAsyncModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UrlAsyncModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def url_async_moderation(
        self,
        request: main_models.UrlAsyncModerationRequest,
    ) -> main_models.UrlAsyncModerationResponse:
        runtime = RuntimeOptions()
        return self.url_async_moderation_with_options(request, runtime)

    async def url_async_moderation_async(
        self,
        request: main_models.UrlAsyncModerationRequest,
    ) -> main_models.UrlAsyncModerationResponse:
        runtime = RuntimeOptions()
        return await self.url_async_moderation_with_options_async(request, runtime)

    def video_moderation_with_options(
        self,
        request: main_models.VideoModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VideoModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_moderation_with_options_async(
        self,
        request: main_models.VideoModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VideoModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_moderation(
        self,
        request: main_models.VideoModerationRequest,
    ) -> main_models.VideoModerationResponse:
        runtime = RuntimeOptions()
        return self.video_moderation_with_options(request, runtime)

    async def video_moderation_async(
        self,
        request: main_models.VideoModerationRequest,
    ) -> main_models.VideoModerationResponse:
        runtime = RuntimeOptions()
        return await self.video_moderation_with_options_async(request, runtime)

    def video_moderation_cancel_with_options(
        self,
        request: main_models.VideoModerationCancelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VideoModerationCancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoModerationCancel',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoModerationCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_moderation_cancel_with_options_async(
        self,
        request: main_models.VideoModerationCancelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VideoModerationCancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoModerationCancel',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoModerationCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_moderation_cancel(
        self,
        request: main_models.VideoModerationCancelRequest,
    ) -> main_models.VideoModerationCancelResponse:
        runtime = RuntimeOptions()
        return self.video_moderation_cancel_with_options(request, runtime)

    async def video_moderation_cancel_async(
        self,
        request: main_models.VideoModerationCancelRequest,
    ) -> main_models.VideoModerationCancelResponse:
        runtime = RuntimeOptions()
        return await self.video_moderation_cancel_with_options_async(request, runtime)

    def video_moderation_result_with_options(
        self,
        request: main_models.VideoModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VideoModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_moderation_result_with_options_async(
        self,
        request: main_models.VideoModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VideoModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_moderation_result(
        self,
        request: main_models.VideoModerationResultRequest,
    ) -> main_models.VideoModerationResultResponse:
        runtime = RuntimeOptions()
        return self.video_moderation_result_with_options(request, runtime)

    async def video_moderation_result_async(
        self,
        request: main_models.VideoModerationResultRequest,
    ) -> main_models.VideoModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.video_moderation_result_with_options_async(request, runtime)

    def voice_moderation_with_options(
        self,
        request: main_models.VoiceModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VoiceModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VoiceModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VoiceModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_moderation_with_options_async(
        self,
        request: main_models.VoiceModerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VoiceModerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VoiceModeration',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VoiceModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_moderation(
        self,
        request: main_models.VoiceModerationRequest,
    ) -> main_models.VoiceModerationResponse:
        runtime = RuntimeOptions()
        return self.voice_moderation_with_options(request, runtime)

    async def voice_moderation_async(
        self,
        request: main_models.VoiceModerationRequest,
    ) -> main_models.VoiceModerationResponse:
        runtime = RuntimeOptions()
        return await self.voice_moderation_with_options_async(request, runtime)

    def voice_moderation_cancel_with_options(
        self,
        request: main_models.VoiceModerationCancelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VoiceModerationCancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VoiceModerationCancel',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VoiceModerationCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_moderation_cancel_with_options_async(
        self,
        request: main_models.VoiceModerationCancelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VoiceModerationCancelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VoiceModerationCancel',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VoiceModerationCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_moderation_cancel(
        self,
        request: main_models.VoiceModerationCancelRequest,
    ) -> main_models.VoiceModerationCancelResponse:
        runtime = RuntimeOptions()
        return self.voice_moderation_cancel_with_options(request, runtime)

    async def voice_moderation_cancel_async(
        self,
        request: main_models.VoiceModerationCancelRequest,
    ) -> main_models.VoiceModerationCancelResponse:
        runtime = RuntimeOptions()
        return await self.voice_moderation_cancel_with_options_async(request, runtime)

    def voice_moderation_result_with_options(
        self,
        request: main_models.VoiceModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VoiceModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VoiceModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VoiceModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_moderation_result_with_options_async(
        self,
        request: main_models.VoiceModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VoiceModerationResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.service):
            body['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VoiceModerationResult',
            version = '2022-03-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VoiceModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_moderation_result(
        self,
        request: main_models.VoiceModerationResultRequest,
    ) -> main_models.VoiceModerationResultResponse:
        runtime = RuntimeOptions()
        return self.voice_moderation_result_with_options(request, runtime)

    async def voice_moderation_result_async(
        self,
        request: main_models.VoiceModerationResultRequest,
    ) -> main_models.VoiceModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.voice_moderation_result_with_options_async(request, runtime)
