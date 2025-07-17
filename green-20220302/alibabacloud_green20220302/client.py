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
        @summary Obtains the moderation results of an Image Moderation 2.0 task.
        
        @description    Billing: This operation is free of charge.
        QPS limit: You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Obtains the moderation results of an Image Moderation 2.0 task.
        
        @description    Billing: This operation is free of charge.
        QPS limit: You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Obtains the moderation results of an Image Moderation 2.0 task.
        
        @description    Billing: This operation is free of charge.
        QPS limit: You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Obtains the moderation results of an Image Moderation 2.0 task.
        
        @description    Billing: This operation is free of charge.
        QPS limit: You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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

    def describe_multimodal_moderation_result_with_options(
        self,
        request: green_20220302_models.DescribeMultimodalModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeMultimodalModerationResultResponse:
        """
        @summary 查询异步多模态检测结果
        
        @param request: DescribeMultimodalModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMultimodalModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultimodalModerationResult',
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
            green_20220302_models.DescribeMultimodalModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multimodal_moderation_result_with_options_async(
        self,
        request: green_20220302_models.DescribeMultimodalModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.DescribeMultimodalModerationResultResponse:
        """
        @summary 查询异步多模态检测结果
        
        @param request: DescribeMultimodalModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMultimodalModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultimodalModerationResult',
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
            green_20220302_models.DescribeMultimodalModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multimodal_moderation_result(
        self,
        request: green_20220302_models.DescribeMultimodalModerationResultRequest,
    ) -> green_20220302_models.DescribeMultimodalModerationResultResponse:
        """
        @summary 查询异步多模态检测结果
        
        @param request: DescribeMultimodalModerationResultRequest
        @return: DescribeMultimodalModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_multimodal_moderation_result_with_options(request, runtime)

    async def describe_multimodal_moderation_result_async(
        self,
        request: green_20220302_models.DescribeMultimodalModerationResultRequest,
    ) -> green_20220302_models.DescribeMultimodalModerationResultResponse:
        """
        @summary 查询异步多模态检测结果
        
        @param request: DescribeMultimodalModerationResultRequest
        @return: DescribeMultimodalModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_multimodal_moderation_result_with_options_async(request, runtime)

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
        @summary Queries the moderation results based on the ReqId returned by asynchronous URL moderation.
        
        @description    Billing: This operation is free of charge.
        Query timeout: We recommend that you query moderation results at least 480 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for up to 3 days. After 3 days, the results are deleted.
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Queries the moderation results based on the ReqId returned by asynchronous URL moderation.
        
        @description    Billing: This operation is free of charge.
        Query timeout: We recommend that you query moderation results at least 480 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for up to 3 days. After 3 days, the results are deleted.
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Queries the moderation results based on the ReqId returned by asynchronous URL moderation.
        
        @description    Billing: This operation is free of charge.
        Query timeout: We recommend that you query moderation results at least 480 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for up to 3 days. After 3 days, the results are deleted.
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Queries the moderation results based on the ReqId returned by asynchronous URL moderation.
        
        @description    Billing: This operation is free of charge.
        Query timeout: We recommend that you query moderation results at least 480 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for up to 3 days. After 3 days, the results are deleted.
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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

    def image_batch_moderation_with_options(
        self,
        request: green_20220302_models.ImageBatchModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageBatchModerationResponse:
        """
        @summary 图片批量调用
        
        @param request: ImageBatchModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageBatchModerationResponse
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
            action='ImageBatchModeration',
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
            green_20220302_models.ImageBatchModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_batch_moderation_with_options_async(
        self,
        request: green_20220302_models.ImageBatchModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageBatchModerationResponse:
        """
        @summary 图片批量调用
        
        @param request: ImageBatchModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageBatchModerationResponse
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
            action='ImageBatchModeration',
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
            green_20220302_models.ImageBatchModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_batch_moderation(
        self,
        request: green_20220302_models.ImageBatchModerationRequest,
    ) -> green_20220302_models.ImageBatchModerationResponse:
        """
        @summary 图片批量调用
        
        @param request: ImageBatchModerationRequest
        @return: ImageBatchModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.image_batch_moderation_with_options(request, runtime)

    async def image_batch_moderation_async(
        self,
        request: green_20220302_models.ImageBatchModerationRequest,
    ) -> green_20220302_models.ImageBatchModerationResponse:
        """
        @summary 图片批量调用
        
        @param request: ImageBatchModerationRequest
        @return: ImageBatchModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.image_batch_moderation_with_options_async(request, runtime)

    def image_moderation_with_options(
        self,
        request: green_20220302_models.ImageModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ImageModerationResponse:
        """
        @summary Identifies whether an image contains content or elements that violate relevant regulations on network content dissemination, affect the content order of a specific platform, or affect user experience. Image Moderation 2.0 supports over 90 content risk labels and over 100 risk control items. Image Moderation 2.0 of Content Moderation allows you to develop further moderation or governance measures for specific image content based on business scenarios, platform-specific content governance rules, or rich risk labels and scores of confidence levels returned by API calls.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/467826.html)[](https://www.aliyun.com/price/product?#/lvwang/detail/cdibag) of Image Moderation 2.0.
        
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
        @summary Identifies whether an image contains content or elements that violate relevant regulations on network content dissemination, affect the content order of a specific platform, or affect user experience. Image Moderation 2.0 supports over 90 content risk labels and over 100 risk control items. Image Moderation 2.0 of Content Moderation allows you to develop further moderation or governance measures for specific image content based on business scenarios, platform-specific content governance rules, or rich risk labels and scores of confidence levels returned by API calls.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/467826.html)[](https://www.aliyun.com/price/product?#/lvwang/detail/cdibag) of Image Moderation 2.0.
        
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
        @summary Identifies whether an image contains content or elements that violate relevant regulations on network content dissemination, affect the content order of a specific platform, or affect user experience. Image Moderation 2.0 supports over 90 content risk labels and over 100 risk control items. Image Moderation 2.0 of Content Moderation allows you to develop further moderation or governance measures for specific image content based on business scenarios, platform-specific content governance rules, or rich risk labels and scores of confidence levels returned by API calls.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/467826.html)[](https://www.aliyun.com/price/product?#/lvwang/detail/cdibag) of Image Moderation 2.0.
        
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
        @summary Identifies whether an image contains content or elements that violate relevant regulations on network content dissemination, affect the content order of a specific platform, or affect user experience. Image Moderation 2.0 supports over 90 content risk labels and over 100 risk control items. Image Moderation 2.0 of Content Moderation allows you to develop further moderation or governance measures for specific image content based on business scenarios, platform-specific content governance rules, or rich risk labels and scores of confidence levels returned by API calls.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/467826.html)[](https://www.aliyun.com/price/product?#/lvwang/detail/cdibag) of Image Moderation 2.0.
        
        @param request: ImageModerationRequest
        @return: ImageModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.image_moderation_with_options_async(request, runtime)

    def manual_callback_with_options(
        self,
        request: green_20220302_models.ManualCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ManualCallbackResponse:
        """
        @summary Content Security Manual Review Result Callback Interface
        
        @param request: ManualCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManualCallbackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.checksum):
            body['Checksum'] = request.checksum
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.msg):
            body['Msg'] = request.msg
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ManualCallback',
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
            green_20220302_models.ManualCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_callback_with_options_async(
        self,
        request: green_20220302_models.ManualCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ManualCallbackResponse:
        """
        @summary Content Security Manual Review Result Callback Interface
        
        @param request: ManualCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManualCallbackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.checksum):
            body['Checksum'] = request.checksum
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.msg):
            body['Msg'] = request.msg
        if not UtilClient.is_unset(request.req_id):
            body['ReqId'] = request.req_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ManualCallback',
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
            green_20220302_models.ManualCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_callback(
        self,
        request: green_20220302_models.ManualCallbackRequest,
    ) -> green_20220302_models.ManualCallbackResponse:
        """
        @summary Content Security Manual Review Result Callback Interface
        
        @param request: ManualCallbackRequest
        @return: ManualCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manual_callback_with_options(request, runtime)

    async def manual_callback_async(
        self,
        request: green_20220302_models.ManualCallbackRequest,
    ) -> green_20220302_models.ManualCallbackResponse:
        """
        @summary Content Security Manual Review Result Callback Interface
        
        @param request: ManualCallbackRequest
        @return: ManualCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manual_callback_with_options_async(request, runtime)

    def manual_moderation_with_options(
        self,
        request: green_20220302_models.ManualModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ManualModerationResponse:
        """
        @summary Content Security Manual Review Request Interface
        
        @param request: ManualModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManualModerationResponse
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
            action='ManualModeration',
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
            green_20220302_models.ManualModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_moderation_with_options_async(
        self,
        request: green_20220302_models.ManualModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ManualModerationResponse:
        """
        @summary Content Security Manual Review Request Interface
        
        @param request: ManualModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManualModerationResponse
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
            action='ManualModeration',
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
            green_20220302_models.ManualModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_moderation(
        self,
        request: green_20220302_models.ManualModerationRequest,
    ) -> green_20220302_models.ManualModerationResponse:
        """
        @summary Content Security Manual Review Request Interface
        
        @param request: ManualModerationRequest
        @return: ManualModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manual_moderation_with_options(request, runtime)

    async def manual_moderation_async(
        self,
        request: green_20220302_models.ManualModerationRequest,
    ) -> green_20220302_models.ManualModerationResponse:
        """
        @summary Content Security Manual Review Request Interface
        
        @param request: ManualModerationRequest
        @return: ManualModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manual_moderation_with_options_async(request, runtime)

    def manual_moderation_result_with_options(
        self,
        request: green_20220302_models.ManualModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ManualModerationResultResponse:
        """
        @summary Retrieve manual review results
        
        @param request: ManualModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManualModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ManualModerationResult',
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
            green_20220302_models.ManualModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_moderation_result_with_options_async(
        self,
        request: green_20220302_models.ManualModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.ManualModerationResultResponse:
        """
        @summary Retrieve manual review results
        
        @param request: ManualModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManualModerationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ManualModerationResult',
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
            green_20220302_models.ManualModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_moderation_result(
        self,
        request: green_20220302_models.ManualModerationResultRequest,
    ) -> green_20220302_models.ManualModerationResultResponse:
        """
        @summary Retrieve manual review results
        
        @param request: ManualModerationResultRequest
        @return: ManualModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manual_moderation_result_with_options(request, runtime)

    async def manual_moderation_result_async(
        self,
        request: green_20220302_models.ManualModerationResultRequest,
    ) -> green_20220302_models.ManualModerationResultResponse:
        """
        @summary Retrieve manual review results
        
        @param request: ManualModerationResultRequest
        @return: ManualModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manual_moderation_result_with_options_async(request, runtime)

    def multi_modal_guard_with_options(
        self,
        request: green_20220302_models.MultiModalGuardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.MultiModalGuardResponse:
        """
        @summary 同步检测接口
        
        @param request: MultiModalGuardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultiModalGuardResponse
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
            action='MultiModalGuard',
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
            green_20220302_models.MultiModalGuardResponse(),
            self.call_api(params, req, runtime)
        )

    async def multi_modal_guard_with_options_async(
        self,
        request: green_20220302_models.MultiModalGuardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.MultiModalGuardResponse:
        """
        @summary 同步检测接口
        
        @param request: MultiModalGuardRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultiModalGuardResponse
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
            action='MultiModalGuard',
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
            green_20220302_models.MultiModalGuardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def multi_modal_guard(
        self,
        request: green_20220302_models.MultiModalGuardRequest,
    ) -> green_20220302_models.MultiModalGuardResponse:
        """
        @summary 同步检测接口
        
        @param request: MultiModalGuardRequest
        @return: MultiModalGuardResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.multi_modal_guard_with_options(request, runtime)

    async def multi_modal_guard_async(
        self,
        request: green_20220302_models.MultiModalGuardRequest,
    ) -> green_20220302_models.MultiModalGuardResponse:
        """
        @summary 同步检测接口
        
        @param request: MultiModalGuardRequest
        @return: MultiModalGuardResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.multi_modal_guard_with_options_async(request, runtime)

    def multimodal_async_moderation_with_options(
        self,
        request: green_20220302_models.MultimodalAsyncModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.MultimodalAsyncModerationResponse:
        """
        @summary 多模态-异步检测
        
        @param request: MultimodalAsyncModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultimodalAsyncModerationResponse
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
            action='MultimodalAsyncModeration',
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
            green_20220302_models.MultimodalAsyncModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def multimodal_async_moderation_with_options_async(
        self,
        request: green_20220302_models.MultimodalAsyncModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.MultimodalAsyncModerationResponse:
        """
        @summary 多模态-异步检测
        
        @param request: MultimodalAsyncModerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultimodalAsyncModerationResponse
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
            action='MultimodalAsyncModeration',
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
            green_20220302_models.MultimodalAsyncModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def multimodal_async_moderation(
        self,
        request: green_20220302_models.MultimodalAsyncModerationRequest,
    ) -> green_20220302_models.MultimodalAsyncModerationResponse:
        """
        @summary 多模态-异步检测
        
        @param request: MultimodalAsyncModerationRequest
        @return: MultimodalAsyncModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.multimodal_async_moderation_with_options(request, runtime)

    async def multimodal_async_moderation_async(
        self,
        request: green_20220302_models.MultimodalAsyncModerationRequest,
    ) -> green_20220302_models.MultimodalAsyncModerationResponse:
        """
        @summary 多模态-异步检测
        
        @param request: MultimodalAsyncModerationRequest
        @return: MultimodalAsyncModerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.multimodal_async_moderation_with_options_async(request, runtime)

    def text_moderation_with_options(
        self,
        request: green_20220302_models.TextModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationResponse:
        """
        @summary Provides moderation services for multiple business scenarios and identifies various violation risks.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/464388.html?#section-itm-m2s-ugq) of Text Moderation 2.0.
        
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
        @summary Provides moderation services for multiple business scenarios and identifies various violation risks.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/464388.html?#section-itm-m2s-ugq) of Text Moderation 2.0.
        
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
        @summary Provides moderation services for multiple business scenarios and identifies various violation risks.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/464388.html?#section-itm-m2s-ugq) of Text Moderation 2.0.
        
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
        @summary Provides moderation services for multiple business scenarios and identifies various violation risks.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/464388.html?#section-itm-m2s-ugq) of Text Moderation 2.0.
        
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
        @summary Moderates the input command and generated text of large language models (LLMs). Specific model input commands can be used to retrieve standard answers. The feature of enabling and disabling the moderation labels is also available.
        
        @description Before you call this operation, make sure that you have [activated the Content Moderation 2.0 service](https://common-buy.aliyun.com/?commodityCode=lvwang_cip_public_cn) and are familiar with the [billing](https://help.aliyun.com/document_detail/2671445.html?#section-6od-32j-99n) of the Text Moderation 2.0 Plus service.
        
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
        @summary Moderates the input command and generated text of large language models (LLMs). Specific model input commands can be used to retrieve standard answers. The feature of enabling and disabling the moderation labels is also available.
        
        @description Before you call this operation, make sure that you have [activated the Content Moderation 2.0 service](https://common-buy.aliyun.com/?commodityCode=lvwang_cip_public_cn) and are familiar with the [billing](https://help.aliyun.com/document_detail/2671445.html?#section-6od-32j-99n) of the Text Moderation 2.0 Plus service.
        
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
        @summary Moderates the input command and generated text of large language models (LLMs). Specific model input commands can be used to retrieve standard answers. The feature of enabling and disabling the moderation labels is also available.
        
        @description Before you call this operation, make sure that you have [activated the Content Moderation 2.0 service](https://common-buy.aliyun.com/?commodityCode=lvwang_cip_public_cn) and are familiar with the [billing](https://help.aliyun.com/document_detail/2671445.html?#section-6od-32j-99n) of the Text Moderation 2.0 Plus service.
        
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
        @summary Moderates the input command and generated text of large language models (LLMs). Specific model input commands can be used to retrieve standard answers. The feature of enabling and disabling the moderation labels is also available.
        
        @description Before you call this operation, make sure that you have [activated the Content Moderation 2.0 service](https://common-buy.aliyun.com/?commodityCode=lvwang_cip_public_cn) and are familiar with the [billing](https://help.aliyun.com/document_detail/2671445.html?#section-6od-32j-99n) of the Text Moderation 2.0 Plus service.
        
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
        @summary Get Video Detection Results
        
        @description This operation is free of charge. We recommend that you query moderation results at least 30 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for at most 24 hours. After 24 hours, the results are deleted.
        
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
        @summary Get Video Detection Results
        
        @description This operation is free of charge. We recommend that you query moderation results at least 30 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for at most 24 hours. After 24 hours, the results are deleted.
        
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
        @summary Get Video Detection Results
        
        @description This operation is free of charge. We recommend that you query moderation results at least 30 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for at most 24 hours. After 24 hours, the results are deleted.
        
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
        @summary Get Video Detection Results
        
        @description This operation is free of charge. We recommend that you query moderation results at least 30 seconds after you send an asynchronous moderation request. Content Moderation retains moderation results for at most 24 hours. After 24 hours, the results are deleted.
        
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
        @summary Obtains the moderation results of a Voice Moderation 2.0 task.
        
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
        @summary Obtains the moderation results of a Voice Moderation 2.0 task.
        
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
        @summary Obtains the moderation results of a Voice Moderation 2.0 task.
        
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
        @summary Obtains the moderation results of a Voice Moderation 2.0 task.
        
        @param request: VoiceModerationResultRequest
        @return: VoiceModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.voice_moderation_result_with_options_async(request, runtime)
