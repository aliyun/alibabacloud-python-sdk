# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_anytrans20250707 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_translate_with_options(
        self,
        tmp_req: main_models.BatchTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchTranslateResponse:
        tmp_req.validate()
        request = main_models.BatchTranslateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not DaraCore.is_null(tmp_req.text):
            request.text_shrink = Utils.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['appName'] = request.app_name
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text_shrink):
            body['text'] = request.text_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchTranslate',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/batch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_translate_with_options_async(
        self,
        tmp_req: main_models.BatchTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchTranslateResponse:
        tmp_req.validate()
        request = main_models.BatchTranslateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not DaraCore.is_null(tmp_req.text):
            request.text_shrink = Utils.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['appName'] = request.app_name
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text_shrink):
            body['text'] = request.text_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchTranslate',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/batch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_translate(
        self,
        request: main_models.BatchTranslateRequest,
    ) -> main_models.BatchTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_translate_with_options(request, headers, runtime)

    async def batch_translate_async(
        self,
        request: main_models.BatchTranslateRequest,
    ) -> main_models.BatchTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_translate_with_options_async(request, headers, runtime)

    def batch_translate_for_html_with_options(
        self,
        tmp_req: main_models.BatchTranslateForHtmlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchTranslateForHtmlResponse:
        tmp_req.validate()
        request = main_models.BatchTranslateForHtmlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not DaraCore.is_null(tmp_req.text):
            request.text_shrink = Utils.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['appName'] = request.app_name
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text_shrink):
            body['text'] = request.text_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchTranslateForHtml',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/batchForHtml',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchTranslateForHtmlResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_translate_for_html_with_options_async(
        self,
        tmp_req: main_models.BatchTranslateForHtmlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchTranslateForHtmlResponse:
        tmp_req.validate()
        request = main_models.BatchTranslateForHtmlShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not DaraCore.is_null(tmp_req.text):
            request.text_shrink = Utils.array_to_string_with_specified_style(tmp_req.text, 'text', 'json')
        body = {}
        if not DaraCore.is_null(request.app_name):
            body['appName'] = request.app_name
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text_shrink):
            body['text'] = request.text_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchTranslateForHtml',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/batchForHtml',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchTranslateForHtmlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_translate_for_html(
        self,
        request: main_models.BatchTranslateForHtmlRequest,
    ) -> main_models.BatchTranslateForHtmlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_translate_for_html_with_options(request, headers, runtime)

    async def batch_translate_for_html_async(
        self,
        request: main_models.BatchTranslateForHtmlRequest,
    ) -> main_models.BatchTranslateForHtmlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_translate_for_html_with_options_async(request, headers, runtime)

    def get_doc_translate_task_with_options(
        self,
        request: main_models.GetDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/doc/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_translate_task_with_options_async(
        self,
        request: main_models.GetDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/doc/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_translate_task(
        self,
        request: main_models.GetDocTranslateTaskRequest,
    ) -> main_models.GetDocTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_doc_translate_task_with_options(request, headers, runtime)

    async def get_doc_translate_task_async(
        self,
        request: main_models.GetDocTranslateTaskRequest,
    ) -> main_models.GetDocTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_doc_translate_task_with_options_async(request, headers, runtime)

    def get_html_translate_task_with_options(
        self,
        request: main_models.GetHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHtmlTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHtmlTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/html/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHtmlTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_html_translate_task_with_options_async(
        self,
        request: main_models.GetHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHtmlTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHtmlTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/html/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHtmlTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_html_translate_task(
        self,
        request: main_models.GetHtmlTranslateTaskRequest,
    ) -> main_models.GetHtmlTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_html_translate_task_with_options(request, headers, runtime)

    async def get_html_translate_task_async(
        self,
        request: main_models.GetHtmlTranslateTaskRequest,
    ) -> main_models.GetHtmlTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_html_translate_task_with_options_async(request, headers, runtime)

    def get_image_translate_task_with_options(
        self,
        request: main_models.GetImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetImageTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/image/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_translate_task_with_options_async(
        self,
        request: main_models.GetImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetImageTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/image/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_translate_task(
        self,
        request: main_models.GetImageTranslateTaskRequest,
    ) -> main_models.GetImageTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_image_translate_task_with_options(request, headers, runtime)

    async def get_image_translate_task_async(
        self,
        request: main_models.GetImageTranslateTaskRequest,
    ) -> main_models.GetImageTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_image_translate_task_with_options_async(request, headers, runtime)

    def get_long_text_translate_task_with_options(
        self,
        request: main_models.GetLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLongTextTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLongTextTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/longText/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLongTextTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_long_text_translate_task_with_options_async(
        self,
        request: main_models.GetLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLongTextTranslateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLongTextTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/longText/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLongTextTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_long_text_translate_task(
        self,
        request: main_models.GetLongTextTranslateTaskRequest,
    ) -> main_models.GetLongTextTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_long_text_translate_task_with_options(request, headers, runtime)

    async def get_long_text_translate_task_async(
        self,
        request: main_models.GetLongTextTranslateTaskRequest,
    ) -> main_models.GetLongTextTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_long_text_translate_task_with_options_async(request, headers, runtime)

    def submit_doc_translate_task_with_options(
        self,
        tmp_req: main_models.SubmitDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitDocTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/doc/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_translate_task_with_options_async(
        self,
        tmp_req: main_models.SubmitDocTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitDocTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/doc/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_translate_task(
        self,
        request: main_models.SubmitDocTranslateTaskRequest,
    ) -> main_models.SubmitDocTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_doc_translate_task_with_options(request, headers, runtime)

    async def submit_doc_translate_task_async(
        self,
        request: main_models.SubmitDocTranslateTaskRequest,
    ) -> main_models.SubmitDocTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_doc_translate_task_with_options_async(request, headers, runtime)

    def submit_html_translate_task_with_options(
        self,
        tmp_req: main_models.SubmitHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitHtmlTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitHtmlTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitHtmlTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/html/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitHtmlTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_html_translate_task_with_options_async(
        self,
        tmp_req: main_models.SubmitHtmlTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitHtmlTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitHtmlTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitHtmlTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/html/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitHtmlTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_html_translate_task(
        self,
        request: main_models.SubmitHtmlTranslateTaskRequest,
    ) -> main_models.SubmitHtmlTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_html_translate_task_with_options(request, headers, runtime)

    async def submit_html_translate_task_async(
        self,
        request: main_models.SubmitHtmlTranslateTaskRequest,
    ) -> main_models.SubmitHtmlTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_html_translate_task_with_options_async(request, headers, runtime)

    def submit_image_translate_task_with_options(
        self,
        tmp_req: main_models.SubmitImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitImageTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not DaraCore.is_null(tmp_req.target_language):
            request.target_language_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_language, 'targetLanguage', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language_shrink):
            body['targetLanguage'] = request.target_language_shrink
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/image/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_translate_task_with_options_async(
        self,
        tmp_req: main_models.SubmitImageTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitImageTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        if not DaraCore.is_null(tmp_req.target_language):
            request.target_language_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_language, 'targetLanguage', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language_shrink):
            body['targetLanguage'] = request.target_language_shrink
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/image/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_translate_task(
        self,
        request: main_models.SubmitImageTranslateTaskRequest,
    ) -> main_models.SubmitImageTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_image_translate_task_with_options(request, headers, runtime)

    async def submit_image_translate_task_async(
        self,
        request: main_models.SubmitImageTranslateTaskRequest,
    ) -> main_models.SubmitImageTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_image_translate_task_with_options_async(request, headers, runtime)

    def submit_long_text_translate_task_with_options(
        self,
        tmp_req: main_models.SubmitLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitLongTextTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitLongTextTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitLongTextTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/longText/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitLongTextTranslateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_long_text_translate_task_with_options_async(
        self,
        tmp_req: main_models.SubmitLongTextTranslateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitLongTextTranslateTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitLongTextTranslateTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitLongTextTranslateTask',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/longText/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitLongTextTranslateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_long_text_translate_task(
        self,
        request: main_models.SubmitLongTextTranslateTaskRequest,
    ) -> main_models.SubmitLongTextTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_long_text_translate_task_with_options(request, headers, runtime)

    async def submit_long_text_translate_task_async(
        self,
        request: main_models.SubmitLongTextTranslateTaskRequest,
    ) -> main_models.SubmitLongTextTranslateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_long_text_translate_task_with_options_async(request, headers, runtime)

    def term_edit_with_options(
        self,
        tmp_req: main_models.TermEditRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TermEditResponse:
        tmp_req.validate()
        request = main_models.TermEditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TermEdit',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/intervene/edit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TermEditResponse(),
            self.call_api(params, req, runtime)
        )

    async def term_edit_with_options_async(
        self,
        tmp_req: main_models.TermEditRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TermEditResponse:
        tmp_req.validate()
        request = main_models.TermEditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TermEdit',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/intervene/edit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TermEditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def term_edit(
        self,
        request: main_models.TermEditRequest,
    ) -> main_models.TermEditResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.term_edit_with_options(request, headers, runtime)

    async def term_edit_async(
        self,
        request: main_models.TermEditRequest,
    ) -> main_models.TermEditResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.term_edit_with_options_async(request, headers, runtime)

    def term_query_with_options(
        self,
        tmp_req: main_models.TermQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TermQueryResponse:
        tmp_req.validate()
        request = main_models.TermQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TermQuery',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/intervene/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TermQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def term_query_with_options_async(
        self,
        tmp_req: main_models.TermQueryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TermQueryResponse:
        tmp_req.validate()
        request = main_models.TermQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TermQuery',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/intervene/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TermQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def term_query(
        self,
        request: main_models.TermQueryRequest,
    ) -> main_models.TermQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.term_query_with_options(request, headers, runtime)

    async def term_query_async(
        self,
        request: main_models.TermQueryRequest,
    ) -> main_models.TermQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.term_query_with_options_async(request, headers, runtime)

    def text_translate_with_options(
        self,
        tmp_req: main_models.TextTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TextTranslateResponse:
        tmp_req.validate()
        request = main_models.TextTranslateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextTranslate',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/text',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_translate_with_options_async(
        self,
        tmp_req: main_models.TextTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TextTranslateResponse:
        tmp_req.validate()
        request = main_models.TextTranslateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ext):
            request.ext_shrink = Utils.array_to_string_with_specified_style(tmp_req.ext, 'ext', 'json')
        body = {}
        if not DaraCore.is_null(request.ext_shrink):
            body['ext'] = request.ext_shrink
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.scene):
            body['scene'] = request.scene
        if not DaraCore.is_null(request.source_language):
            body['sourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['targetLanguage'] = request.target_language
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextTranslate',
            version = '2025-07-07',
            protocol = 'HTTPS',
            pathname = f'/anytrans/translate/text',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_translate(
        self,
        request: main_models.TextTranslateRequest,
    ) -> main_models.TextTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.text_translate_with_options(request, headers, runtime)

    async def text_translate_async(
        self,
        request: main_models.TextTranslateRequest,
    ) -> main_models.TextTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.text_translate_with_options_async(request, headers, runtime)
