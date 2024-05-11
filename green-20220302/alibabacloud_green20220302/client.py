# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20220302 import models as green_20220302_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_file_moderation_result_with_options(
        self,
        request: green_20220302_models.DescribeFileModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeFileModerationResultResponse:
        """
        @summary 文档审核结果
        
        @param request: DescribeFileModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFileModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeFileModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_moderation_result_with_options_async(
        self,
        request: green_20220302_models.DescribeFileModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeFileModerationResultResponse:
        """
        @summary 文档审核结果
        
        @param request: DescribeFileModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFileModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeFileModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_moderation_result(
        self,
        request: green_20220302_models.DescribeFileModerationResultRequest,
    ) -> green_20220302_models.DescribeFileModerationResultResponse:
        """
        @summary 文档审核结果
        
        @param request: DescribeFileModerationResultRequest
        @return: DescribeFileModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_file_moderation_result_with_options(request, runtime)

    async def describe_file_moderation_result_async(
        self,
        request: green_20220302_models.DescribeFileModerationResultRequest,
    ) -> green_20220302_models.DescribeFileModerationResultResponse:
        """
        @summary 文档审核结果
        
        @param request: DescribeFileModerationResultRequest
        @return: DescribeFileModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_moderation_result_with_options_async(request, runtime)

    def describe_image_moderation_result_with_options(
        self,
        request: green_20220302_models.DescribeImageModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeImageModerationResultResponse:
        """
        @summary 查询异步检测结果
        
        @param request: DescribeImageModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_moderation_result_with_options_async(
        self,
        request: green_20220302_models.DescribeImageModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeImageModerationResultResponse:
        """
        @summary 查询异步检测结果
        
        @param request: DescribeImageModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeImageModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_moderation_result(
        self,
        request: green_20220302_models.DescribeImageModerationResultRequest,
    ) -> green_20220302_models.DescribeImageModerationResultResponse:
        """
        @summary 查询异步检测结果
        
        @param request: DescribeImageModerationResultRequest
        @return: DescribeImageModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_moderation_result_with_options(request, runtime)

    async def describe_image_moderation_result_async(
        self,
        request: green_20220302_models.DescribeImageModerationResultRequest,
    ) -> green_20220302_models.DescribeImageModerationResultResponse:
        """
        @summary 查询异步检测结果
        
        @param request: DescribeImageModerationResultRequest
        @return: DescribeImageModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_moderation_result_with_options_async(request, runtime)

    def describe_image_result_ext_with_options(
        self,
        request: green_20220302_models.DescribeImageResultExtRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeImageResultExtResponse:
        """
        @summary 查询检测结果辅助信息
        
        @param request: DescribeImageResultExtRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageResultExtResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.info_type):
            body['InfoType'] = request.info_type
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImageResultExt',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeImageResultExtResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_result_ext_with_options_async(
        self,
        request: green_20220302_models.DescribeImageResultExtRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeImageResultExtResponse:
        """
        @summary 查询检测结果辅助信息
        
        @param request: DescribeImageResultExtRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImageResultExtResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.info_type):
            body['InfoType'] = request.info_type
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImageResultExt',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeImageResultExtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_result_ext(
        self,
        request: green_20220302_models.DescribeImageResultExtRequest,
    ) -> green_20220302_models.DescribeImageResultExtResponse:
        """
        @summary 查询检测结果辅助信息
        
        @param request: DescribeImageResultExtRequest
        @return: DescribeImageResultExtResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_result_ext_with_options(request, runtime)

    async def describe_image_result_ext_async(
        self,
        request: green_20220302_models.DescribeImageResultExtRequest,
    ) -> green_20220302_models.DescribeImageResultExtResponse:
        """
        @summary 查询检测结果辅助信息
        
        @param request: DescribeImageResultExtRequest
        @return: DescribeImageResultExtResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_result_ext_with_options_async(request, runtime)

    def describe_upload_token_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeUploadTokenResponse:
        """
        @summary 查询上传token
        
        @param request: DescribeUploadTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUploadTokenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUploadToken',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upload_token_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeUploadTokenResponse:
        """
        @summary 查询上传token
        
        @param request: DescribeUploadTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUploadTokenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUploadToken',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_upload_token(self) -> green_20220302_models.DescribeUploadTokenResponse:
        """
        @summary 查询上传token
        
        @return: DescribeUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_token_with_options(runtime)

    async def describe_upload_token_async(self) -> green_20220302_models.DescribeUploadTokenResponse:
        """
        @summary 查询上传token
        
        @return: DescribeUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_token_with_options_async(runtime)

    def describe_url_moderation_result_with_options(
        self,
        request: green_20220302_models.DescribeUrlModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeUrlModerationResultResponse:
        """
        @summary 查询 url 检测结果
        
        @param request: DescribeUrlModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUrlModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUrlModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeUrlModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_url_moderation_result_with_options_async(
        self,
        request: green_20220302_models.DescribeUrlModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeUrlModerationResultResponse:
        """
        @summary 查询 url 检测结果
        
        @param request: DescribeUrlModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUrlModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUrlModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.DescribeUrlModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_url_moderation_result(
        self,
        request: green_20220302_models.DescribeUrlModerationResultRequest,
    ) -> green_20220302_models.DescribeUrlModerationResultResponse:
        """
        @summary 查询 url 检测结果
        
        @param request: DescribeUrlModerationResultRequest
        @return: DescribeUrlModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_url_moderation_result_with_options(request, runtime)

    async def describe_url_moderation_result_async(
        self,
        request: green_20220302_models.DescribeUrlModerationResultRequest,
    ) -> green_20220302_models.DescribeUrlModerationResultResponse:
        """
        @summary 查询 url 检测结果
        
        @param request: DescribeUrlModerationResultRequest
        @return: DescribeUrlModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_url_moderation_result_with_options_async(request, runtime)

    def file_moderation_with_options(
        self,
        request: green_20220302_models.FileModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.FileModerationResponse:
        """
        @summary 文档审核
        
        @param request: FileModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.FileModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_moderation_with_options_async(
        self,
        request: green_20220302_models.FileModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.FileModerationResponse:
        """
        @summary 文档审核
        
        @param request: FileModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.FileModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_moderation(
        self,
        request: green_20220302_models.FileModerationRequest,
    ) -> green_20220302_models.FileModerationResponse:
        """
        @summary 文档审核
        
        @param request: FileModerationRequest
        @return: FileModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.file_moderation_with_options(request, runtime)

    async def file_moderation_async(
        self,
        request: green_20220302_models.FileModerationRequest,
    ) -> green_20220302_models.FileModerationResponse:
        """
        @summary 文档审核
        
        @param request: FileModerationRequest
        @return: FileModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.file_moderation_with_options_async(request, runtime)

    def image_async_moderation_with_options(
        self,
        request: green_20220302_models.ImageAsyncModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageAsyncModerationResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncModerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.ImageAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_async_moderation_with_options_async(
        self,
        request: green_20220302_models.ImageAsyncModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageAsyncModerationResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncModerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.ImageAsyncModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_async_moderation(
        self,
        request: green_20220302_models.ImageAsyncModerationRequest,
    ) -> green_20220302_models.ImageAsyncModerationResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncModerationRequest
        @return: ImageAsyncModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.image_async_moderation_with_options(request, runtime)

    async def image_async_moderation_async(
        self,
        request: green_20220302_models.ImageAsyncModerationRequest,
    ) -> green_20220302_models.ImageAsyncModerationResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncModerationRequest
        @return: ImageAsyncModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.image_async_moderation_with_options_async(request, runtime)

    def image_moderation_with_options(
        self,
        request: green_20220302_models.ImageModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageModerationResponse:
        """
        @summary 图片审核
        
        @param request: ImageModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.ImageModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_moderation_with_options_async(
        self,
        request: green_20220302_models.ImageModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageModerationResponse:
        """
        @summary 图片审核
        
        @param request: ImageModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImageModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.ImageModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_moderation(
        self,
        request: green_20220302_models.ImageModerationRequest,
    ) -> green_20220302_models.ImageModerationResponse:
        """
        @summary 图片审核
        
        @param request: ImageModerationRequest
        @return: ImageModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.image_moderation_with_options(request, runtime)

    async def image_moderation_async(
        self,
        request: green_20220302_models.ImageModerationRequest,
    ) -> green_20220302_models.ImageModerationResponse:
        """
        @summary 图片审核
        
        @param request: ImageModerationRequest
        @return: ImageModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.image_moderation_with_options_async(request, runtime)

    def text_moderation_with_options(
        self,
        request: green_20220302_models.TextModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationResponse:
        """
        @summary 文本审核
        
        @param request: TextModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_moderation_with_options_async(
        self,
        request: green_20220302_models.TextModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationResponse:
        """
        @summary 文本审核
        
        @param request: TextModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_moderation(
        self,
        request: green_20220302_models.TextModerationRequest,
    ) -> green_20220302_models.TextModerationResponse:
        """
        @summary 文本审核
        
        @param request: TextModerationRequest
        @return: TextModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.text_moderation_with_options(request, runtime)

    async def text_moderation_async(
        self,
        request: green_20220302_models.TextModerationRequest,
    ) -> green_20220302_models.TextModerationResponse:
        """
        @summary 文本审核
        
        @param request: TextModerationRequest
        @return: TextModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.text_moderation_with_options_async(request, runtime)

    def text_moderation_plus_with_options(
        self,
        request: green_20220302_models.TextModerationPlusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationPlusResponse:
        """
        @summary 文本检测Plus版
        
        @param request: TextModerationPlusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextModerationPlusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModerationPlus',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationPlusResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_moderation_plus_with_options_async(
        self,
        request: green_20220302_models.TextModerationPlusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationPlusResponse:
        """
        @summary 文本检测Plus版
        
        @param request: TextModerationPlusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextModerationPlusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModerationPlus',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationPlusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_moderation_plus(
        self,
        request: green_20220302_models.TextModerationPlusRequest,
    ) -> green_20220302_models.TextModerationPlusResponse:
        """
        @summary 文本检测Plus版
        
        @param request: TextModerationPlusRequest
        @return: TextModerationPlusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.text_moderation_plus_with_options(request, runtime)

    async def text_moderation_plus_async(
        self,
        request: green_20220302_models.TextModerationPlusRequest,
    ) -> green_20220302_models.TextModerationPlusResponse:
        """
        @summary 文本检测Plus版
        
        @param request: TextModerationPlusRequest
        @return: TextModerationPlusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.text_moderation_plus_with_options_async(request, runtime)

    def url_async_moderation_with_options(
        self,
        request: green_20220302_models.UrlAsyncModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.UrlAsyncModerationResponse:
        """
        @summary url异步检测
        
        @param request: UrlAsyncModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UrlAsyncModerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UrlAsyncModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.UrlAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def url_async_moderation_with_options_async(
        self,
        request: green_20220302_models.UrlAsyncModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.UrlAsyncModerationResponse:
        """
        @summary url异步检测
        
        @param request: UrlAsyncModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UrlAsyncModerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UrlAsyncModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.UrlAsyncModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def url_async_moderation(
        self,
        request: green_20220302_models.UrlAsyncModerationRequest,
    ) -> green_20220302_models.UrlAsyncModerationResponse:
        """
        @summary url异步检测
        
        @param request: UrlAsyncModerationRequest
        @return: UrlAsyncModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.url_async_moderation_with_options(request, runtime)

    async def url_async_moderation_async(
        self,
        request: green_20220302_models.UrlAsyncModerationRequest,
    ) -> green_20220302_models.UrlAsyncModerationResponse:
        """
        @summary url异步检测
        
        @param request: UrlAsyncModerationRequest
        @return: UrlAsyncModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.url_async_moderation_with_options_async(request, runtime)

    def video_moderation_with_options(
        self,
        request: green_20220302_models.VideoModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VideoModerationResponse:
        """
        @summary 视频检测任务提交
        
        @param request: VideoModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_moderation_with_options_async(
        self,
        request: green_20220302_models.VideoModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VideoModerationResponse:
        """
        @summary 视频检测任务提交
        
        @param request: VideoModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_moderation(
        self,
        request: green_20220302_models.VideoModerationRequest,
    ) -> green_20220302_models.VideoModerationResponse:
        """
        @summary 视频检测任务提交
        
        @param request: VideoModerationRequest
        @return: VideoModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.video_moderation_with_options(request, runtime)

    async def video_moderation_async(
        self,
        request: green_20220302_models.VideoModerationRequest,
    ) -> green_20220302_models.VideoModerationResponse:
        """
        @summary 视频检测任务提交
        
        @param request: VideoModerationRequest
        @return: VideoModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.video_moderation_with_options_async(request, runtime)

    def video_moderation_cancel_with_options(
        self,
        request: green_20220302_models.VideoModerationCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VideoModerationCancelResponse:
        """
        @summary 取消视频直播流检测
        
        @param request: VideoModerationCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoModerationCancelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModerationCancel',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_moderation_cancel_with_options_async(
        self,
        request: green_20220302_models.VideoModerationCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VideoModerationCancelResponse:
        """
        @summary 取消视频直播流检测
        
        @param request: VideoModerationCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoModerationCancelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModerationCancel',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_moderation_cancel(
        self,
        request: green_20220302_models.VideoModerationCancelRequest,
    ) -> green_20220302_models.VideoModerationCancelResponse:
        """
        @summary 取消视频直播流检测
        
        @param request: VideoModerationCancelRequest
        @return: VideoModerationCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.video_moderation_cancel_with_options(request, runtime)

    async def video_moderation_cancel_async(
        self,
        request: green_20220302_models.VideoModerationCancelRequest,
    ) -> green_20220302_models.VideoModerationCancelResponse:
        """
        @summary 取消视频直播流检测
        
        @param request: VideoModerationCancelRequest
        @return: VideoModerationCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.video_moderation_cancel_with_options_async(request, runtime)

    def video_moderation_result_with_options(
        self,
        request: green_20220302_models.VideoModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VideoModerationResultResponse:
        """
        @summary 获取视频检测结果
        
        @param request: VideoModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_moderation_result_with_options_async(
        self,
        request: green_20220302_models.VideoModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VideoModerationResultResponse:
        """
        @summary 获取视频检测结果
        
        @param request: VideoModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VideoModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VideoModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_moderation_result(
        self,
        request: green_20220302_models.VideoModerationResultRequest,
    ) -> green_20220302_models.VideoModerationResultResponse:
        """
        @summary 获取视频检测结果
        
        @param request: VideoModerationResultRequest
        @return: VideoModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.video_moderation_result_with_options(request, runtime)

    async def video_moderation_result_async(
        self,
        request: green_20220302_models.VideoModerationResultRequest,
    ) -> green_20220302_models.VideoModerationResultResponse:
        """
        @summary 获取视频检测结果
        
        @param request: VideoModerationResultRequest
        @return: VideoModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.video_moderation_result_with_options_async(request, runtime)

    def voice_moderation_with_options(
        self,
        request: green_20220302_models.VoiceModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VoiceModerationResponse:
        """
        @summary 语音审核
        
        @param request: VoiceModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_moderation_with_options_async(
        self,
        request: green_20220302_models.VoiceModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VoiceModerationResponse:
        """
        @summary 语音审核
        
        @param request: VoiceModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceModerationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_moderation(
        self,
        request: green_20220302_models.VoiceModerationRequest,
    ) -> green_20220302_models.VoiceModerationResponse:
        """
        @summary 语音审核
        
        @param request: VoiceModerationRequest
        @return: VoiceModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.voice_moderation_with_options(request, runtime)

    async def voice_moderation_async(
        self,
        request: green_20220302_models.VoiceModerationRequest,
    ) -> green_20220302_models.VoiceModerationResponse:
        """
        @summary 语音审核
        
        @param request: VoiceModerationRequest
        @return: VoiceModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.voice_moderation_with_options_async(request, runtime)

    def voice_moderation_cancel_with_options(
        self,
        request: green_20220302_models.VoiceModerationCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VoiceModerationCancelResponse:
        """
        @summary 取消检测
        
        @param request: VoiceModerationCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceModerationCancelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModerationCancel',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_moderation_cancel_with_options_async(
        self,
        request: green_20220302_models.VoiceModerationCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VoiceModerationCancelResponse:
        """
        @summary 取消检测
        
        @param request: VoiceModerationCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceModerationCancelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModerationCancel',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_moderation_cancel(
        self,
        request: green_20220302_models.VoiceModerationCancelRequest,
    ) -> green_20220302_models.VoiceModerationCancelResponse:
        """
        @summary 取消检测
        
        @param request: VoiceModerationCancelRequest
        @return: VoiceModerationCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.voice_moderation_cancel_with_options(request, runtime)

    async def voice_moderation_cancel_async(
        self,
        request: green_20220302_models.VoiceModerationCancelRequest,
    ) -> green_20220302_models.VoiceModerationCancelResponse:
        """
        @summary 取消检测
        
        @param request: VoiceModerationCancelRequest
        @return: VoiceModerationCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.voice_moderation_cancel_with_options_async(request, runtime)

    def voice_moderation_result_with_options(
        self,
        request: green_20220302_models.VoiceModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VoiceModerationResultResponse:
        """
        @summary 语音检测结果获取接口
        
        @param request: VoiceModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_moderation_result_with_options_async(
        self,
        request: green_20220302_models.VoiceModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.VoiceModerationResultResponse:
        """
        @summary 语音检测结果获取接口
        
        @param request: VoiceModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VoiceModerationResult',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.VoiceModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_moderation_result(
        self,
        request: green_20220302_models.VoiceModerationResultRequest,
    ) -> green_20220302_models.VoiceModerationResultResponse:
        """
        @summary 语音检测结果获取接口
        
        @param request: VoiceModerationResultRequest
        @return: VoiceModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.voice_moderation_result_with_options(request, runtime)

    async def voice_moderation_result_async(
        self,
        request: green_20220302_models.VoiceModerationResultRequest,
    ) -> green_20220302_models.VoiceModerationResultResponse:
        """
        @summary 语音检测结果获取接口
        
        @param request: VoiceModerationResultRequest
        @return: VoiceModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.voice_moderation_result_with_options_async(request, runtime)
