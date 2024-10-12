# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_aicontent20240611 import models as ai_content_20240611_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aicontent', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def aliyun_console_open_api_query_aliyun_console_servcie_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServcieList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServcieList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_aliyun_console_servcie_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServcieList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServcieList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_aliyun_console_servcie_list(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_aliyun_console_servcie_list_with_options(headers, runtime)

    async def aliyun_console_open_api_query_aliyun_console_servcie_list_async(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_aliyun_console_servcie_list_with_options_async(headers, runtime)

    def aliyun_console_open_api_query_aliyun_console_service_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServiceList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServiceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_aliyun_console_service_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServiceList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServiceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_aliyun_console_service_list(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_aliyun_console_service_list_with_options(headers, runtime)

    async def aliyun_console_open_api_query_aliyun_console_service_list_async(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_aliyun_console_service_list_with_options_async(headers, runtime)

    def personalized_text_to_image_add_inference_job_with_options(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        if not UtilClient.is_unset(request.strength):
            body['strength'] = request.strength
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addPreModelInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_add_inference_job_with_options_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        if not UtilClient.is_unset(request.strength):
            body['strength'] = request.strength
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addPreModelInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_add_inference_job(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_add_inference_job_with_options(request, headers, runtime)

    async def personalized_text_to_image_add_inference_job_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_add_inference_job_with_options_async(request, headers, runtime)

    def personalized_text_to_image_query_image_asset_with_options(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAssetFromImageId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_query_image_asset_with_options_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAssetFromImageId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_query_image_asset(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_query_image_asset_with_options(request, headers, runtime)

    async def personalized_text_to_image_query_image_asset_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_query_image_asset_with_options_async(request, headers, runtime)

    def personalized_text_to_image_query_pre_model_inference_job_info_with_options(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryPreModelInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryPreModelInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_query_pre_model_inference_job_info_with_options_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryPreModelInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryPreModelInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_query_pre_model_inference_job_info(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_query_pre_model_inference_job_info_with_options(request, headers, runtime)

    async def personalized_text_to_image_query_pre_model_inference_job_info_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_query_pre_model_inference_job_info_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_add_inference_job_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_add_inference_job_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_add_inference_job(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_add_inference_job_with_options(request, headers, runtime)

    async def personalizedtxt_2img_add_inference_job_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_add_inference_job_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_add_model_train_job_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddModelTrainJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addModelTrainJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_add_model_train_job_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddModelTrainJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addModelTrainJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_add_model_train_job(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_add_model_train_job_with_options(request, headers, runtime)

    async def personalizedtxt_2img_add_model_train_job_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_add_model_train_job_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_image_asset_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt_id):
            query['promptId'] = request.prompt_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAsset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_image_asset_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt_id):
            query['promptId'] = request.prompt_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAsset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_image_asset(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_image_asset_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_image_asset_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_image_asset_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_inference_job_info_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_inference_job_info_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_inference_job_info(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_inference_job_info_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_inference_job_info_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_inference_job_info_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_model_train_job_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainJobList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainJobList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_model_train_job_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainJobList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainJobList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_model_train_job_list(self) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_model_train_job_list_with_options(headers, runtime)

    async def personalizedtxt_2img_query_model_train_job_list_async(self) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_model_train_job_list_with_options_async(headers, runtime)

    def personalizedtxt_2img_query_model_train_status_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainStatus',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_model_train_status_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainStatus',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_model_train_status(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_model_train_status_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_model_train_status_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_model_train_status_with_options_async(request, headers, runtime)
