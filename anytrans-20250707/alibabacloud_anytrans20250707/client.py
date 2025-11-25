# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_anytrans20250707 import models as any_trans_20250707_models
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
        self._endpoint = self.get_endpoint('anytrans', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_translate_with_options(
        self,
        tmp_req: any_trans_20250707_models.BatchTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.BatchTranslateResponse:
        """
        @summary 通义多模态翻译批量翻译
        
        @param tmp_req: BatchTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchTranslateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.BatchTranslateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not UtilClient.is_unset(tmp_req.text):
            request.text_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text_shrink):
            body['text'] = request.text_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchTranslate',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.BatchTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_translate_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.BatchTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.BatchTranslateResponse:
        """
        @summary 通义多模态翻译批量翻译
        
        @param tmp_req: BatchTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchTranslateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.BatchTranslateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not UtilClient.is_unset(tmp_req.text):
            request.text_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text_shrink):
            body['text'] = request.text_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchTranslate',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.BatchTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_translate(
        self,
        request: any_trans_20250707_models.BatchTranslateRequest,
    ) -> any_trans_20250707_models.BatchTranslateResponse:
        """
        @summary 通义多模态翻译批量翻译
        
        @param request: BatchTranslateRequest
        @return: BatchTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_translate_with_options(request, headers, runtime)

    async def batch_translate_async(
        self,
        request: any_trans_20250707_models.BatchTranslateRequest,
    ) -> any_trans_20250707_models.BatchTranslateResponse:
        """
        @summary 通义多模态翻译批量翻译
        
        @param request: BatchTranslateRequest
        @return: BatchTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_translate_with_options_async(request, headers, runtime)

    def batch_translate_for_html_with_options(
        self,
        tmp_req: any_trans_20250707_models.BatchTranslateForHtmlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.BatchTranslateForHtmlResponse:
        """
        @summary 通义多模态翻译批量翻译(供js sdk使用)
        
        @param tmp_req: BatchTranslateForHtmlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchTranslateForHtmlResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.BatchTranslateForHtmlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not UtilClient.is_unset(tmp_req.text):
            request.text_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text_shrink):
            body['text'] = request.text_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchTranslateForHtml',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/batchForHtml',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.BatchTranslateForHtmlResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_translate_for_html_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.BatchTranslateForHtmlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.BatchTranslateForHtmlResponse:
        """
        @summary 通义多模态翻译批量翻译(供js sdk使用)
        
        @param tmp_req: BatchTranslateForHtmlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchTranslateForHtmlResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.BatchTranslateForHtmlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not UtilClient.is_unset(tmp_req.text):
            request.text_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text_shrink):
            body['text'] = request.text_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchTranslateForHtml',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/batchForHtml',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.BatchTranslateForHtmlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_translate_for_html(
        self,
        request: any_trans_20250707_models.BatchTranslateForHtmlRequest,
    ) -> any_trans_20250707_models.BatchTranslateForHtmlResponse:
        """
        @summary 通义多模态翻译批量翻译(供js sdk使用)
        
        @param request: BatchTranslateForHtmlRequest
        @return: BatchTranslateForHtmlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_translate_for_html_with_options(request, headers, runtime)

    async def batch_translate_for_html_async(
        self,
        request: any_trans_20250707_models.BatchTranslateForHtmlRequest,
    ) -> any_trans_20250707_models.BatchTranslateForHtmlResponse:
        """
        @summary 通义多模态翻译批量翻译(供js sdk使用)
        
        @param request: BatchTranslateForHtmlRequest
        @return: BatchTranslateForHtmlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_translate_for_html_with_options_async(request, headers, runtime)

    def get_doc_translate_task_with_options(
        self,
        request: any_trans_20250707_models.GetDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译获文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/doc/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_translate_task_with_options_async(
        self,
        request: any_trans_20250707_models.GetDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译获文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/doc/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetDocTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_translate_task(
        self,
        request: any_trans_20250707_models.GetDocTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译获文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @return: GetDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_doc_translate_task_with_options(request, headers, runtime)

    async def get_doc_translate_task_async(
        self,
        request: any_trans_20250707_models.GetDocTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译获文档翻译任务
        
        @param request: GetDocTranslateTaskRequest
        @return: GetDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_doc_translate_task_with_options_async(request, headers, runtime)

    def get_html_translate_task_with_options(
        self,
        request: any_trans_20250707_models.GetHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取html翻译结果
        
        @param request: GetHtmlTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHtmlTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHtmlTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/html/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetHtmlTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_html_translate_task_with_options_async(
        self,
        request: any_trans_20250707_models.GetHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取html翻译结果
        
        @param request: GetHtmlTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHtmlTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHtmlTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/html/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetHtmlTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_html_translate_task(
        self,
        request: any_trans_20250707_models.GetHtmlTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取html翻译结果
        
        @param request: GetHtmlTranslateTaskRequest
        @return: GetHtmlTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_html_translate_task_with_options(request, headers, runtime)

    async def get_html_translate_task_async(
        self,
        request: any_trans_20250707_models.GetHtmlTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取html翻译结果
        
        @param request: GetHtmlTranslateTaskRequest
        @return: GetHtmlTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_html_translate_task_with_options_async(request, headers, runtime)

    def get_image_translate_task_with_options(
        self,
        request: any_trans_20250707_models.GetImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/image/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_translate_task_with_options_async(
        self,
        request: any_trans_20250707_models.GetImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetImageTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/image/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetImageTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_translate_task(
        self,
        request: any_trans_20250707_models.GetImageTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @return: GetImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_translate_task_with_options(request, headers, runtime)

    async def get_image_translate_task_async(
        self,
        request: any_trans_20250707_models.GetImageTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取图片翻译任务
        
        @param request: GetImageTranslateTaskRequest
        @return: GetImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_translate_task_with_options_async(request, headers, runtime)

    def get_long_text_translate_task_with_options(
        self,
        request: any_trans_20250707_models.GetLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取长文翻译结果
        
        @param request: GetLongTextTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLongTextTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLongTextTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/longText/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetLongTextTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_long_text_translate_task_with_options_async(
        self,
        request: any_trans_20250707_models.GetLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.GetLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取长文翻译结果
        
        @param request: GetLongTextTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLongTextTranslateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLongTextTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/longText/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.GetLongTextTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_long_text_translate_task(
        self,
        request: any_trans_20250707_models.GetLongTextTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取长文翻译结果
        
        @param request: GetLongTextTranslateTaskRequest
        @return: GetLongTextTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_long_text_translate_task_with_options(request, headers, runtime)

    async def get_long_text_translate_task_async(
        self,
        request: any_trans_20250707_models.GetLongTextTranslateTaskRequest,
    ) -> any_trans_20250707_models.GetLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译获取长文翻译结果
        
        @param request: GetLongTextTranslateTaskRequest
        @return: GetLongTextTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_long_text_translate_task_with_options_async(request, headers, runtime)

    def submit_doc_translate_task_with_options(
        self,
        tmp_req: any_trans_20250707_models.SubmitDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交文档翻译任务
        
        @param tmp_req: SubmitDocTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitDocTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDocTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/doc/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_translate_task_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.SubmitDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交文档翻译任务
        
        @param tmp_req: SubmitDocTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitDocTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDocTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/doc/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitDocTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_translate_task(
        self,
        request: any_trans_20250707_models.SubmitDocTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交文档翻译任务
        
        @param request: SubmitDocTranslateTaskRequest
        @return: SubmitDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_doc_translate_task_with_options(request, headers, runtime)

    async def submit_doc_translate_task_async(
        self,
        request: any_trans_20250707_models.SubmitDocTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitDocTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交文档翻译任务
        
        @param request: SubmitDocTranslateTaskRequest
        @return: SubmitDocTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_doc_translate_task_with_options_async(request, headers, runtime)

    def submit_html_translate_task_with_options(
        self,
        tmp_req: any_trans_20250707_models.SubmitHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交html翻译任务
        
        @param tmp_req: SubmitHtmlTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitHtmlTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitHtmlTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitHtmlTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/html/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitHtmlTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_html_translate_task_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.SubmitHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交html翻译任务
        
        @param tmp_req: SubmitHtmlTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitHtmlTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitHtmlTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitHtmlTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/html/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitHtmlTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_html_translate_task(
        self,
        request: any_trans_20250707_models.SubmitHtmlTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交html翻译任务
        
        @param request: SubmitHtmlTranslateTaskRequest
        @return: SubmitHtmlTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_html_translate_task_with_options(request, headers, runtime)

    async def submit_html_translate_task_async(
        self,
        request: any_trans_20250707_models.SubmitHtmlTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitHtmlTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交html翻译任务
        
        @param request: SubmitHtmlTranslateTaskRequest
        @return: SubmitHtmlTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_html_translate_task_with_options_async(request, headers, runtime)

    def submit_image_translate_task_with_options(
        self,
        tmp_req: any_trans_20250707_models.SubmitImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交图片翻译任务
        
        @param tmp_req: SubmitImageTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitImageTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitImageTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not UtilClient.is_unset(tmp_req.target_language):
            request.target_language_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_language, 'targetLanguage', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language_shrink):
            body['targetLanguage'] = request.target_language_shrink
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImageTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/image/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_translate_task_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.SubmitImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交图片翻译任务
        
        @param tmp_req: SubmitImageTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitImageTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitImageTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not UtilClient.is_unset(tmp_req.target_language):
            request.target_language_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_language, 'targetLanguage', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language_shrink):
            body['targetLanguage'] = request.target_language_shrink
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImageTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/image/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitImageTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_translate_task(
        self,
        request: any_trans_20250707_models.SubmitImageTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交图片翻译任务
        
        @param request: SubmitImageTranslateTaskRequest
        @return: SubmitImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_image_translate_task_with_options(request, headers, runtime)

    async def submit_image_translate_task_async(
        self,
        request: any_trans_20250707_models.SubmitImageTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitImageTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交图片翻译任务
        
        @param request: SubmitImageTranslateTaskRequest
        @return: SubmitImageTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_image_translate_task_with_options_async(request, headers, runtime)

    def submit_long_text_translate_task_with_options(
        self,
        tmp_req: any_trans_20250707_models.SubmitLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交长文翻译任务
        
        @param tmp_req: SubmitLongTextTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitLongTextTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitLongTextTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLongTextTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/longText/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitLongTextTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_long_text_translate_task_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.SubmitLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.SubmitLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交长文翻译任务
        
        @param tmp_req: SubmitLongTextTranslateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitLongTextTranslateTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.SubmitLongTextTranslateTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLongTextTranslateTask',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/longText/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.SubmitLongTextTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_long_text_translate_task(
        self,
        request: any_trans_20250707_models.SubmitLongTextTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交长文翻译任务
        
        @param request: SubmitLongTextTranslateTaskRequest
        @return: SubmitLongTextTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_long_text_translate_task_with_options(request, headers, runtime)

    async def submit_long_text_translate_task_async(
        self,
        request: any_trans_20250707_models.SubmitLongTextTranslateTaskRequest,
    ) -> any_trans_20250707_models.SubmitLongTextTranslateTaskResponse:
        """
        @summary 通义多模态翻译提交长文翻译任务
        
        @param request: SubmitLongTextTranslateTaskRequest
        @return: SubmitLongTextTranslateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_long_text_translate_task_with_options_async(request, headers, runtime)

    def term_edit_with_options(
        self,
        tmp_req: any_trans_20250707_models.TermEditRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.TermEditResponse:
        """
        @summary 通义多模态翻译术语编辑
        
        @param tmp_req: TermEditRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TermEditResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.TermEditShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TermEdit',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/intervene/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.TermEditResponse(),
            self.call_api(params, req, runtime)
        )

    async def term_edit_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.TermEditRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.TermEditResponse:
        """
        @summary 通义多模态翻译术语编辑
        
        @param tmp_req: TermEditRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TermEditResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.TermEditShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TermEdit',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/intervene/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.TermEditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def term_edit(
        self,
        request: any_trans_20250707_models.TermEditRequest,
    ) -> any_trans_20250707_models.TermEditResponse:
        """
        @summary 通义多模态翻译术语编辑
        
        @param request: TermEditRequest
        @return: TermEditResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.term_edit_with_options(request, headers, runtime)

    async def term_edit_async(
        self,
        request: any_trans_20250707_models.TermEditRequest,
    ) -> any_trans_20250707_models.TermEditResponse:
        """
        @summary 通义多模态翻译术语编辑
        
        @param request: TermEditRequest
        @return: TermEditResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.term_edit_with_options_async(request, headers, runtime)

    def term_query_with_options(
        self,
        request: any_trans_20250707_models.TermQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.TermQueryResponse:
        """
        @summary 通义多模态翻译术语查询
        
        @param request: TermQueryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TermQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TermQuery',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/intervene/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.TermQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def term_query_with_options_async(
        self,
        request: any_trans_20250707_models.TermQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.TermQueryResponse:
        """
        @summary 通义多模态翻译术语查询
        
        @param request: TermQueryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TermQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TermQuery',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/intervene/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.TermQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def term_query(
        self,
        request: any_trans_20250707_models.TermQueryRequest,
    ) -> any_trans_20250707_models.TermQueryResponse:
        """
        @summary 通义多模态翻译术语查询
        
        @param request: TermQueryRequest
        @return: TermQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.term_query_with_options(request, headers, runtime)

    async def term_query_async(
        self,
        request: any_trans_20250707_models.TermQueryRequest,
    ) -> any_trans_20250707_models.TermQueryResponse:
        """
        @summary 通义多模态翻译术语查询
        
        @param request: TermQueryRequest
        @return: TermQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.term_query_with_options_async(request, headers, runtime)

    def text_translate_with_options(
        self,
        tmp_req: any_trans_20250707_models.TextTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.TextTranslateResponse:
        """
        @summary 通义多模态翻译文本翻译
        
        @param tmp_req: TextTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextTranslateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.TextTranslateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextTranslate',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/text',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.TextTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_translate_with_options_async(
        self,
        tmp_req: any_trans_20250707_models.TextTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> any_trans_20250707_models.TextTranslateResponse:
        """
        @summary 通义多模态翻译文本翻译
        
        @param tmp_req: TextTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextTranslateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = any_trans_20250707_models.TextTranslateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext):
            request.ext_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not UtilClient.is_unset(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not UtilClient.is_unset(request.format):
            body['format'] = request.format
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.target_language):
            body['targetLanguage'] = request.target_language
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextTranslate',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/anytrans/translate/text',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            any_trans_20250707_models.TextTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_translate(
        self,
        request: any_trans_20250707_models.TextTranslateRequest,
    ) -> any_trans_20250707_models.TextTranslateResponse:
        """
        @summary 通义多模态翻译文本翻译
        
        @param request: TextTranslateRequest
        @return: TextTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_translate_with_options(request, headers, runtime)

    async def text_translate_async(
        self,
        request: any_trans_20250707_models.TextTranslateRequest,
    ) -> any_trans_20250707_models.TextTranslateResponse:
        """
        @summary 通义多模态翻译文本翻译
        
        @param request: TextTranslateRequest
        @return: TextTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_translate_with_options_async(request, headers, runtime)
