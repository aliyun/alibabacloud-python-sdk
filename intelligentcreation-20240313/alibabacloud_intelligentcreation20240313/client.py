# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_intelligentcreation20240313 import models as intelligent_creation_20240313_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_illustration_task_with_options(
        self,
        text_id: str,
        request: intelligent_creation_20240313_models.CreateIllustrationTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateIllustrationTaskResponse:
        """
        @summary 创建配图生成任务
        
        @param request: CreateIllustrationTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIllustrationTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateIllustrationTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}/illustrationTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateIllustrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_illustration_task_with_options_async(
        self,
        text_id: str,
        request: intelligent_creation_20240313_models.CreateIllustrationTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateIllustrationTaskResponse:
        """
        @summary 创建配图生成任务
        
        @param request: CreateIllustrationTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIllustrationTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateIllustrationTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}/illustrationTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateIllustrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_illustration_task(
        self,
        text_id: str,
        request: intelligent_creation_20240313_models.CreateIllustrationTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateIllustrationTaskResponse:
        """
        @summary 创建配图生成任务
        
        @param request: CreateIllustrationTaskRequest
        @return: CreateIllustrationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_illustration_task_with_options(text_id, request, headers, runtime)

    async def create_illustration_task_async(
        self,
        text_id: str,
        request: intelligent_creation_20240313_models.CreateIllustrationTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateIllustrationTaskResponse:
        """
        @summary 创建配图生成任务
        
        @param request: CreateIllustrationTaskRequest
        @return: CreateIllustrationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_illustration_task_with_options_async(text_id, request, headers, runtime)

    def create_text_task_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateTextTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateTextTaskResponse:
        """
        @summary 创建文案生成任务
        
        @param request: CreateTextTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTextTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/textTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_text_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateTextTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateTextTaskResponse:
        """
        @summary 创建文案生成任务
        
        @param request: CreateTextTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTextTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/textTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_text_task(
        self,
        request: intelligent_creation_20240313_models.CreateTextTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateTextTaskResponse:
        """
        @summary 创建文案生成任务
        
        @param request: CreateTextTaskRequest
        @return: CreateTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_text_task_with_options(request, headers, runtime)

    async def create_text_task_async(
        self,
        request: intelligent_creation_20240313_models.CreateTextTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateTextTaskResponse:
        """
        @summary 创建文案生成任务
        
        @param request: CreateTextTaskRequest
        @return: CreateTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_text_task_with_options_async(request, headers, runtime)

    def get_illustration_with_options(
        self,
        text_id: str,
        illustration_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetIllustrationResponse:
        """
        @summary 查询配图
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIllustrationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIllustration',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}/illustrations/{OpenApiUtilClient.get_encode_param(illustration_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetIllustrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_illustration_with_options_async(
        self,
        text_id: str,
        illustration_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetIllustrationResponse:
        """
        @summary 查询配图
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIllustrationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIllustration',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}/illustrations/{OpenApiUtilClient.get_encode_param(illustration_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetIllustrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_illustration(
        self,
        text_id: str,
        illustration_id: str,
    ) -> intelligent_creation_20240313_models.GetIllustrationResponse:
        """
        @summary 查询配图
        
        @return: GetIllustrationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_illustration_with_options(text_id, illustration_id, headers, runtime)

    async def get_illustration_async(
        self,
        text_id: str,
        illustration_id: str,
    ) -> intelligent_creation_20240313_models.GetIllustrationResponse:
        """
        @summary 查询配图
        
        @return: GetIllustrationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_illustration_with_options_async(text_id, illustration_id, headers, runtime)

    def get_illustration_task_with_options(
        self,
        text_id: str,
        illustration_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetIllustrationTaskResponse:
        """
        @summary 查询配图任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIllustrationTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIllustrationTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}/illustrationTasks/{OpenApiUtilClient.get_encode_param(illustration_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetIllustrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_illustration_task_with_options_async(
        self,
        text_id: str,
        illustration_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetIllustrationTaskResponse:
        """
        @summary 查询配图任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIllustrationTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIllustrationTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}/illustrationTasks/{OpenApiUtilClient.get_encode_param(illustration_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetIllustrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_illustration_task(
        self,
        text_id: str,
        illustration_task_id: str,
    ) -> intelligent_creation_20240313_models.GetIllustrationTaskResponse:
        """
        @summary 查询配图任务
        
        @return: GetIllustrationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_illustration_task_with_options(text_id, illustration_task_id, headers, runtime)

    async def get_illustration_task_async(
        self,
        text_id: str,
        illustration_task_id: str,
    ) -> intelligent_creation_20240313_models.GetIllustrationTaskResponse:
        """
        @summary 查询配图任务
        
        @return: GetIllustrationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_illustration_task_with_options_async(text_id, illustration_task_id, headers, runtime)

    def get_oss_upload_token_with_options(
        self,
        request: intelligent_creation_20240313_models.GetOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetOssUploadTokenResponse:
        """
        @summary 获取图片上传oss token
        
        @param request: GetOssUploadTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssUploadTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUploadToken',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/uploadToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_upload_token_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetOssUploadTokenResponse:
        """
        @summary 获取图片上传oss token
        
        @param request: GetOssUploadTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssUploadTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUploadToken',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/uploadToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetOssUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_upload_token(
        self,
        request: intelligent_creation_20240313_models.GetOssUploadTokenRequest,
    ) -> intelligent_creation_20240313_models.GetOssUploadTokenResponse:
        """
        @summary 获取图片上传oss token
        
        @param request: GetOssUploadTokenRequest
        @return: GetOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_oss_upload_token_with_options(request, headers, runtime)

    async def get_oss_upload_token_async(
        self,
        request: intelligent_creation_20240313_models.GetOssUploadTokenRequest,
    ) -> intelligent_creation_20240313_models.GetOssUploadTokenResponse:
        """
        @summary 获取图片上传oss token
        
        @param request: GetOssUploadTokenRequest
        @return: GetOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_oss_upload_token_with_options_async(request, headers, runtime)

    def get_text_with_options(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetTextResponse:
        """
        @summary 查询文案
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_with_options_async(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetTextResponse:
        """
        @summary 查询文案
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/{OpenApiUtilClient.get_encode_param(text_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text(
        self,
        text_id: str,
    ) -> intelligent_creation_20240313_models.GetTextResponse:
        """
        @summary 查询文案
        
        @return: GetTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_text_with_options(text_id, headers, runtime)

    async def get_text_async(
        self,
        text_id: str,
    ) -> intelligent_creation_20240313_models.GetTextResponse:
        """
        @summary 查询文案
        
        @return: GetTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_text_with_options_async(text_id, headers, runtime)

    def get_text_task_with_options(
        self,
        text_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetTextTaskResponse:
        """
        @summary 查询文案任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/textTasks/{OpenApiUtilClient.get_encode_param(text_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_task_with_options_async(
        self,
        text_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetTextTaskResponse:
        """
        @summary 查询文案任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/textTasks/{OpenApiUtilClient.get_encode_param(text_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text_task(
        self,
        text_task_id: str,
    ) -> intelligent_creation_20240313_models.GetTextTaskResponse:
        """
        @summary 查询文案任务
        
        @return: GetTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_text_task_with_options(text_task_id, headers, runtime)

    async def get_text_task_async(
        self,
        text_task_id: str,
    ) -> intelligent_creation_20240313_models.GetTextTaskResponse:
        """
        @summary 查询文案任务
        
        @return: GetTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_text_task_with_options_async(text_task_id, headers, runtime)

    def list_text_themes_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextThemesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTextThemes',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/textThemes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListTextThemesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_text_themes_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextThemesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTextThemes',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/textThemes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListTextThemesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_text_themes(self) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @return: ListTextThemesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_text_themes_with_options(headers, runtime)

    async def list_text_themes_async(self) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @return: ListTextThemesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_text_themes_with_options_async(headers, runtime)
