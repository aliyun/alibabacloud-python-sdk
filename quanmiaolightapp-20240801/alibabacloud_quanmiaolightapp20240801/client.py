# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('quanmiaolightapp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_async_task_with_options(
        self,
        workspace_id: str,
        request: main_models.CancelAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/cancelAsyncTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CancelAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/cancelAsyncTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_task(
        self,
        workspace_id: str,
        request: main_models.CancelAsyncTaskRequest,
    ) -> main_models.CancelAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_async_task_with_options(workspace_id, request, headers, runtime)

    async def cancel_async_task_async(
        self,
        workspace_id: str,
        request: main_models.CancelAsyncTaskRequest,
    ) -> main_models.CancelAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_async_task_with_options_async(workspace_id, request, headers, runtime)

    def export_analysis_tag_detail_by_task_id_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.ExportAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        tmp_req.validate()
        request = main_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'categories', 'json')
        body = {}
        if not DaraCore.is_null(request.categories_shrink):
            body['categories'] = request.categories_shrink
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnalysisTagDetailByTaskId',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/exportAnalysisTagDetailByTaskId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_analysis_tag_detail_by_task_id_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.ExportAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        tmp_req.validate()
        request = main_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'categories', 'json')
        body = {}
        if not DaraCore.is_null(request.categories_shrink):
            body['categories'] = request.categories_shrink
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnalysisTagDetailByTaskId',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/exportAnalysisTagDetailByTaskId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_analysis_tag_detail_by_task_id(
        self,
        workspace_id: str,
        request: main_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.export_analysis_tag_detail_by_task_id_with_options(workspace_id, request, headers, runtime)

    async def export_analysis_tag_detail_by_task_id_async(
        self,
        workspace_id: str,
        request: main_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.export_analysis_tag_detail_by_task_id_with_options_async(workspace_id, request, headers, runtime)

    def generate_broadcast_news_with_options(
        self,
        workspace_id: str,
        request: main_models.GenerateBroadcastNewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateBroadcastNewsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateBroadcastNews',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/GenerateBroadcastNews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateBroadcastNewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_broadcast_news_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GenerateBroadcastNewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateBroadcastNewsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateBroadcastNews',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/GenerateBroadcastNews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateBroadcastNewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_broadcast_news(
        self,
        workspace_id: str,
        request: main_models.GenerateBroadcastNewsRequest,
    ) -> main_models.GenerateBroadcastNewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_broadcast_news_with_options(workspace_id, request, headers, runtime)

    async def generate_broadcast_news_async(
        self,
        workspace_id: str,
        request: main_models.GenerateBroadcastNewsRequest,
    ) -> main_models.GenerateBroadcastNewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_broadcast_news_with_options_async(workspace_id, request, headers, runtime)

    def generate_output_format_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.GenerateOutputFormatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateOutputFormatResponse:
        tmp_req.validate()
        request = main_models.GenerateOutputFormatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateOutputFormat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/generateOutputFormat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateOutputFormatResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_output_format_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.GenerateOutputFormatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateOutputFormatResponse:
        tmp_req.validate()
        request = main_models.GenerateOutputFormatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateOutputFormat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/generateOutputFormat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateOutputFormatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_output_format(
        self,
        workspace_id: str,
        request: main_models.GenerateOutputFormatRequest,
    ) -> main_models.GenerateOutputFormatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_output_format_with_options(workspace_id, request, headers, runtime)

    async def generate_output_format_async(
        self,
        workspace_id: str,
        request: main_models.GenerateOutputFormatRequest,
    ) -> main_models.GenerateOutputFormatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_output_format_with_options_async(workspace_id, request, headers, runtime)

    def get_enterprise_voc_analysis_task_with_options(
        self,
        workspace_id: str,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnterpriseVocAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getEnterpriseVocAnalysisTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_voc_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnterpriseVocAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getEnterpriseVocAnalysisTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_voc_analysis_task(
        self,
        workspace_id: str,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_enterprise_voc_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def get_enterprise_voc_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_enterprise_voc_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def get_essay_correction_task_with_options(
        self,
        workspace_id: str,
        request: main_models.GetEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEssayCorrectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEssayCorrectionTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getEssayCorrectionTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEssayCorrectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_essay_correction_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEssayCorrectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEssayCorrectionTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getEssayCorrectionTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEssayCorrectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_essay_correction_task(
        self,
        workspace_id: str,
        request: main_models.GetEssayCorrectionTaskRequest,
    ) -> main_models.GetEssayCorrectionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_essay_correction_task_with_options(workspace_id, request, headers, runtime)

    async def get_essay_correction_task_async(
        self,
        workspace_id: str,
        request: main_models.GetEssayCorrectionTaskRequest,
    ) -> main_models.GetEssayCorrectionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_essay_correction_task_with_options_async(workspace_id, request, headers, runtime)

    def get_file_content_with_options(
        self,
        workspace_id: str,
        request: main_models.GetFileContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFileContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFileContent',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getFileContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_content_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetFileContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFileContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFileContent',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getFileContent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_content(
        self,
        workspace_id: str,
        request: main_models.GetFileContentRequest,
    ) -> main_models.GetFileContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_file_content_with_options(workspace_id, request, headers, runtime)

    async def get_file_content_async(
        self,
        workspace_id: str,
        request: main_models.GetFileContentRequest,
    ) -> main_models.GetFileContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_file_content_with_options_async(workspace_id, request, headers, runtime)

    def get_tag_mining_analysis_task_with_options(
        self,
        workspace_id: str,
        request: main_models.GetTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTagMiningAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTagMiningAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getTagMiningAnalysisTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTagMiningAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_mining_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTagMiningAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTagMiningAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getTagMiningAnalysisTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTagMiningAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_mining_analysis_task(
        self,
        workspace_id: str,
        request: main_models.GetTagMiningAnalysisTaskRequest,
    ) -> main_models.GetTagMiningAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_tag_mining_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def get_tag_mining_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.GetTagMiningAnalysisTaskRequest,
    ) -> main_models.GetTagMiningAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_tag_mining_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def get_video_analysis_config_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoAnalysisConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetVideoAnalysisConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoAnalysisConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_analysis_config_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoAnalysisConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetVideoAnalysisConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoAnalysisConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_analysis_config(
        self,
        workspace_id: str,
    ) -> main_models.GetVideoAnalysisConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_analysis_config_with_options(workspace_id, headers, runtime)

    async def get_video_analysis_config_async(
        self,
        workspace_id: str,
    ) -> main_models.GetVideoAnalysisConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_analysis_config_with_options_async(workspace_id, headers, runtime)

    def get_video_analysis_task_with_options(
        self,
        workspace_id: str,
        request: main_models.GetVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoAnalysisTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_analysis_task(
        self,
        workspace_id: str,
        request: main_models.GetVideoAnalysisTaskRequest,
    ) -> main_models.GetVideoAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def get_video_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.GetVideoAnalysisTaskRequest,
    ) -> main_models.GetVideoAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def get_video_detect_shot_config_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoDetectShotConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetVideoDetectShotConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoDetectShotConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoDetectShotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_detect_shot_config_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoDetectShotConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetVideoDetectShotConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/getVideoDetectShotConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoDetectShotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_detect_shot_config(
        self,
        workspace_id: str,
    ) -> main_models.GetVideoDetectShotConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_detect_shot_config_with_options(workspace_id, headers, runtime)

    async def get_video_detect_shot_config_async(
        self,
        workspace_id: str,
    ) -> main_models.GetVideoDetectShotConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_detect_shot_config_with_options_async(workspace_id, headers, runtime)

    def get_video_detect_shot_task_with_options(
        self,
        workspace_id: str,
        request: main_models.GetVideoDetectShotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoDetectShotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoDetectShotTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getVideoDetectShotTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoDetectShotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_detect_shot_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetVideoDetectShotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoDetectShotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoDetectShotTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/getVideoDetectShotTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoDetectShotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_detect_shot_task(
        self,
        workspace_id: str,
        request: main_models.GetVideoDetectShotTaskRequest,
    ) -> main_models.GetVideoDetectShotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_detect_shot_task_with_options(workspace_id, request, headers, runtime)

    async def get_video_detect_shot_task_async(
        self,
        workspace_id: str,
        request: main_models.GetVideoDetectShotTaskRequest,
    ) -> main_models.GetVideoDetectShotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_detect_shot_task_with_options_async(workspace_id, request, headers, runtime)

    def hot_news_recommend_with_options(
        self,
        workspace_id: str,
        request: main_models.HotNewsRecommendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.HotNewsRecommendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HotNewsRecommend',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/hotNewsRecommend',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotNewsRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def hot_news_recommend_with_options_async(
        self,
        workspace_id: str,
        request: main_models.HotNewsRecommendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.HotNewsRecommendResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HotNewsRecommend',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/hotNewsRecommend',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotNewsRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hot_news_recommend(
        self,
        workspace_id: str,
        request: main_models.HotNewsRecommendRequest,
    ) -> main_models.HotNewsRecommendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.hot_news_recommend_with_options(workspace_id, request, headers, runtime)

    async def hot_news_recommend_async(
        self,
        workspace_id: str,
        request: main_models.HotNewsRecommendRequest,
    ) -> main_models.HotNewsRecommendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.hot_news_recommend_with_options_async(workspace_id, request, headers, runtime)

    def list_analysis_tag_detail_by_task_id_with_options(
        self,
        workspace_id: str,
        request: main_models.ListAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnalysisTagDetailByTaskId',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/listAnalysisTagDetailByTaskId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_analysis_tag_detail_by_task_id_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListAnalysisTagDetailByTaskIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnalysisTagDetailByTaskId',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/listAnalysisTagDetailByTaskId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_analysis_tag_detail_by_task_id(
        self,
        workspace_id: str,
        request: main_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_analysis_tag_detail_by_task_id_with_options(workspace_id, request, headers, runtime)

    async def list_analysis_tag_detail_by_task_id_async(
        self,
        workspace_id: str,
        request: main_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_analysis_tag_detail_by_task_id_with_options_async(workspace_id, request, headers, runtime)

    def list_hot_topic_summaries_with_options(
        self,
        workspace_id: str,
        request: main_models.ListHotTopicSummariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHotTopicSummariesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.hot_topic):
            body['hotTopic'] = request.hot_topic
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.max_results):
            body['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotTopicSummaries',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/listHotTopicSummaries',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotTopicSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_topic_summaries_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListHotTopicSummariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHotTopicSummariesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.hot_topic):
            body['hotTopic'] = request.hot_topic
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.max_results):
            body['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotTopicSummaries',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/listHotTopicSummaries',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotTopicSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_topic_summaries(
        self,
        workspace_id: str,
        request: main_models.ListHotTopicSummariesRequest,
    ) -> main_models.ListHotTopicSummariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_hot_topic_summaries_with_options(workspace_id, request, headers, runtime)

    async def list_hot_topic_summaries_async(
        self,
        workspace_id: str,
        request: main_models.ListHotTopicSummariesRequest,
    ) -> main_models.ListHotTopicSummariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_hot_topic_summaries_with_options_async(workspace_id, request, headers, runtime)

    def run_enterprise_voc_analysis_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunEnterpriseVocAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunEnterpriseVocAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunEnterpriseVocAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.ak_proxy):
            body['akProxy'] = request.ak_proxy
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEnterpriseVocAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEnterpriseVocAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunEnterpriseVocAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_enterprise_voc_analysis_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunEnterpriseVocAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunEnterpriseVocAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunEnterpriseVocAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.ak_proxy):
            body['akProxy'] = request.ak_proxy
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEnterpriseVocAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEnterpriseVocAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunEnterpriseVocAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_enterprise_voc_analysis_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunEnterpriseVocAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunEnterpriseVocAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunEnterpriseVocAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.ak_proxy):
            body['akProxy'] = request.ak_proxy
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEnterpriseVocAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEnterpriseVocAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunEnterpriseVocAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_enterprise_voc_analysis_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunEnterpriseVocAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunEnterpriseVocAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunEnterpriseVocAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.ak_proxy):
            body['akProxy'] = request.ak_proxy
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEnterpriseVocAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEnterpriseVocAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunEnterpriseVocAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_enterprise_voc_analysis(
        self,
        workspace_id: str,
        request: main_models.RunEnterpriseVocAnalysisRequest,
    ) -> main_models.RunEnterpriseVocAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_enterprise_voc_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_enterprise_voc_analysis_async(
        self,
        workspace_id: str,
        request: main_models.RunEnterpriseVocAnalysisRequest,
    ) -> main_models.RunEnterpriseVocAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_enterprise_voc_analysis_with_options_async(workspace_id, request, headers, runtime)

    def run_essay_correction_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunEssayCorrectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunEssayCorrectionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.answer):
            body['answer'] = request.answer
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.subject):
            body['subject'] = request.subject
        if not DaraCore.is_null(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEssayCorrection',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEssayCorrection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunEssayCorrectionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_essay_correction_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunEssayCorrectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunEssayCorrectionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.answer):
            body['answer'] = request.answer
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.subject):
            body['subject'] = request.subject
        if not DaraCore.is_null(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEssayCorrection',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEssayCorrection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunEssayCorrectionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_essay_correction_with_options(
        self,
        workspace_id: str,
        request: main_models.RunEssayCorrectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunEssayCorrectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.answer):
            body['answer'] = request.answer
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.subject):
            body['subject'] = request.subject
        if not DaraCore.is_null(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEssayCorrection',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEssayCorrection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunEssayCorrectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_essay_correction_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunEssayCorrectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunEssayCorrectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.answer):
            body['answer'] = request.answer
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.subject):
            body['subject'] = request.subject
        if not DaraCore.is_null(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunEssayCorrection',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runEssayCorrection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunEssayCorrectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_essay_correction(
        self,
        workspace_id: str,
        request: main_models.RunEssayCorrectionRequest,
    ) -> main_models.RunEssayCorrectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_essay_correction_with_options(workspace_id, request, headers, runtime)

    async def run_essay_correction_async(
        self,
        workspace_id: str,
        request: main_models.RunEssayCorrectionRequest,
    ) -> main_models.RunEssayCorrectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_essay_correction_with_options_async(workspace_id, request, headers, runtime)

    def run_hot_topic_chat_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunHotTopicChatResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunHotTopicChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.hot_topics):
            request.hot_topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.hot_topics, 'hotTopics', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'messages', 'json')
        if not DaraCore.is_null(tmp_req.step_for_broadcast_content_config):
            request.step_for_broadcast_content_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_broadcast_content_config, 'stepForBroadcastContentConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.hot_topics_shrink):
            body['hotTopics'] = request.hot_topics_shrink
        if not DaraCore.is_null(request.image_count):
            body['imageCount'] = request.image_count
        if not DaraCore.is_null(request.messages_shrink):
            body['messages'] = request.messages_shrink
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.step_for_broadcast_content_config_shrink):
            body['stepForBroadcastContentConfig'] = request.step_for_broadcast_content_config_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunHotTopicChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_hot_topic_chat_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunHotTopicChatResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunHotTopicChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.hot_topics):
            request.hot_topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.hot_topics, 'hotTopics', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'messages', 'json')
        if not DaraCore.is_null(tmp_req.step_for_broadcast_content_config):
            request.step_for_broadcast_content_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_broadcast_content_config, 'stepForBroadcastContentConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.hot_topics_shrink):
            body['hotTopics'] = request.hot_topics_shrink
        if not DaraCore.is_null(request.image_count):
            body['imageCount'] = request.image_count
        if not DaraCore.is_null(request.messages_shrink):
            body['messages'] = request.messages_shrink
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.step_for_broadcast_content_config_shrink):
            body['stepForBroadcastContentConfig'] = request.step_for_broadcast_content_config_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunHotTopicChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_hot_topic_chat_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunHotTopicChatResponse:
        tmp_req.validate()
        request = main_models.RunHotTopicChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.hot_topics):
            request.hot_topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.hot_topics, 'hotTopics', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'messages', 'json')
        if not DaraCore.is_null(tmp_req.step_for_broadcast_content_config):
            request.step_for_broadcast_content_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_broadcast_content_config, 'stepForBroadcastContentConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.hot_topics_shrink):
            body['hotTopics'] = request.hot_topics_shrink
        if not DaraCore.is_null(request.image_count):
            body['imageCount'] = request.image_count
        if not DaraCore.is_null(request.messages_shrink):
            body['messages'] = request.messages_shrink
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.step_for_broadcast_content_config_shrink):
            body['stepForBroadcastContentConfig'] = request.step_for_broadcast_content_config_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunHotTopicChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_hot_topic_chat_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunHotTopicChatResponse:
        tmp_req.validate()
        request = main_models.RunHotTopicChatShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.hot_topics):
            request.hot_topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.hot_topics, 'hotTopics', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'messages', 'json')
        if not DaraCore.is_null(tmp_req.step_for_broadcast_content_config):
            request.step_for_broadcast_content_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_broadcast_content_config, 'stepForBroadcastContentConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.hot_topics_shrink):
            body['hotTopics'] = request.hot_topics_shrink
        if not DaraCore.is_null(request.image_count):
            body['imageCount'] = request.image_count
        if not DaraCore.is_null(request.messages_shrink):
            body['messages'] = request.messages_shrink
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.step_for_broadcast_content_config_shrink):
            body['stepForBroadcastContentConfig'] = request.step_for_broadcast_content_config_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunHotTopicChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_hot_topic_chat(
        self,
        workspace_id: str,
        request: main_models.RunHotTopicChatRequest,
    ) -> main_models.RunHotTopicChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_hot_topic_chat_with_options(workspace_id, request, headers, runtime)

    async def run_hot_topic_chat_async(
        self,
        workspace_id: str,
        request: main_models.RunHotTopicChatRequest,
    ) -> main_models.RunHotTopicChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_hot_topic_chat_with_options_async(workspace_id, request, headers, runtime)

    def run_hot_topic_summary_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunHotTopicSummaryResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunHotTopicSummaryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'stepForCustomSummaryStyleConfig', 'json')
        if not DaraCore.is_null(tmp_req.topic_ids):
            request.topic_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.topic_ids, 'topicIds', 'json')
        body = {}
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.step_for_custom_summary_style_config_shrink):
            body['stepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not DaraCore.is_null(request.topic_ids_shrink):
            body['topicIds'] = request.topic_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicSummary',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicSummary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunHotTopicSummaryResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_hot_topic_summary_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunHotTopicSummaryResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunHotTopicSummaryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'stepForCustomSummaryStyleConfig', 'json')
        if not DaraCore.is_null(tmp_req.topic_ids):
            request.topic_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.topic_ids, 'topicIds', 'json')
        body = {}
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.step_for_custom_summary_style_config_shrink):
            body['stepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not DaraCore.is_null(request.topic_ids_shrink):
            body['topicIds'] = request.topic_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicSummary',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicSummary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunHotTopicSummaryResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_hot_topic_summary_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunHotTopicSummaryResponse:
        tmp_req.validate()
        request = main_models.RunHotTopicSummaryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'stepForCustomSummaryStyleConfig', 'json')
        if not DaraCore.is_null(tmp_req.topic_ids):
            request.topic_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.topic_ids, 'topicIds', 'json')
        body = {}
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.step_for_custom_summary_style_config_shrink):
            body['stepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not DaraCore.is_null(request.topic_ids_shrink):
            body['topicIds'] = request.topic_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicSummary',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicSummary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunHotTopicSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_hot_topic_summary_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunHotTopicSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunHotTopicSummaryResponse:
        tmp_req.validate()
        request = main_models.RunHotTopicSummaryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'stepForCustomSummaryStyleConfig', 'json')
        if not DaraCore.is_null(tmp_req.topic_ids):
            request.topic_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.topic_ids, 'topicIds', 'json')
        body = {}
        if not DaraCore.is_null(request.hot_topic_version):
            body['hotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.step_for_custom_summary_style_config_shrink):
            body['stepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not DaraCore.is_null(request.topic_ids_shrink):
            body['topicIds'] = request.topic_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotTopicSummary',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runHotTopicSummary',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunHotTopicSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_hot_topic_summary(
        self,
        workspace_id: str,
        request: main_models.RunHotTopicSummaryRequest,
    ) -> main_models.RunHotTopicSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_hot_topic_summary_with_options(workspace_id, request, headers, runtime)

    async def run_hot_topic_summary_async(
        self,
        workspace_id: str,
        request: main_models.RunHotTopicSummaryRequest,
    ) -> main_models.RunHotTopicSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_hot_topic_summary_with_options_async(workspace_id, request, headers, runtime)

    def run_marketing_information_extract_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunMarketingInformationExtractRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunMarketingInformationExtractResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunMarketingInformationExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_materials):
            request.source_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_materials, 'sourceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.extract_type):
            body['extractType'] = request.extract_type
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.source_materials_shrink):
            body['sourceMaterials'] = request.source_materials_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationExtract',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationExtract',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunMarketingInformationExtractResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_marketing_information_extract_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunMarketingInformationExtractRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunMarketingInformationExtractResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunMarketingInformationExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_materials):
            request.source_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_materials, 'sourceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.extract_type):
            body['extractType'] = request.extract_type
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.source_materials_shrink):
            body['sourceMaterials'] = request.source_materials_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationExtract',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationExtract',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunMarketingInformationExtractResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_marketing_information_extract_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunMarketingInformationExtractRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunMarketingInformationExtractResponse:
        tmp_req.validate()
        request = main_models.RunMarketingInformationExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_materials):
            request.source_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_materials, 'sourceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.extract_type):
            body['extractType'] = request.extract_type
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.source_materials_shrink):
            body['sourceMaterials'] = request.source_materials_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationExtract',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationExtract',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMarketingInformationExtractResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_marketing_information_extract_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunMarketingInformationExtractRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunMarketingInformationExtractResponse:
        tmp_req.validate()
        request = main_models.RunMarketingInformationExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_materials):
            request.source_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_materials, 'sourceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.extract_type):
            body['extractType'] = request.extract_type
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.source_materials_shrink):
            body['sourceMaterials'] = request.source_materials_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationExtract',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationExtract',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMarketingInformationExtractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_marketing_information_extract(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationExtractRequest,
    ) -> main_models.RunMarketingInformationExtractResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_marketing_information_extract_with_options(workspace_id, request, headers, runtime)

    async def run_marketing_information_extract_async(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationExtractRequest,
    ) -> main_models.RunMarketingInformationExtractResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_marketing_information_extract_with_options_async(workspace_id, request, headers, runtime)

    def run_marketing_information_writing_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunMarketingInformationWritingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.custom_limitation):
            body['customLimitation'] = request.custom_limitation
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.input_example):
            body['inputExample'] = request.input_example
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_example):
            body['outputExample'] = request.output_example
        if not DaraCore.is_null(request.source_material):
            body['sourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.writing_type):
            body['writingType'] = request.writing_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunMarketingInformationWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_marketing_information_writing_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunMarketingInformationWritingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.custom_limitation):
            body['customLimitation'] = request.custom_limitation
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.input_example):
            body['inputExample'] = request.input_example
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_example):
            body['outputExample'] = request.output_example
        if not DaraCore.is_null(request.source_material):
            body['sourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.writing_type):
            body['writingType'] = request.writing_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunMarketingInformationWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_marketing_information_writing_with_options(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunMarketingInformationWritingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.custom_limitation):
            body['customLimitation'] = request.custom_limitation
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.input_example):
            body['inputExample'] = request.input_example
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_example):
            body['outputExample'] = request.output_example
        if not DaraCore.is_null(request.source_material):
            body['sourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.writing_type):
            body['writingType'] = request.writing_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMarketingInformationWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_marketing_information_writing_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunMarketingInformationWritingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.custom_limitation):
            body['customLimitation'] = request.custom_limitation
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.input_example):
            body['inputExample'] = request.input_example
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_example):
            body['outputExample'] = request.output_example
        if not DaraCore.is_null(request.source_material):
            body['sourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.writing_type):
            body['writingType'] = request.writing_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMarketingInformationWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runMarketingInformationWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMarketingInformationWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_marketing_information_writing(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationWritingRequest,
    ) -> main_models.RunMarketingInformationWritingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_marketing_information_writing_with_options(workspace_id, request, headers, runtime)

    async def run_marketing_information_writing_async(
        self,
        workspace_id: str,
        request: main_models.RunMarketingInformationWritingRequest,
    ) -> main_models.RunMarketingInformationWritingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_marketing_information_writing_with_options_async(workspace_id, request, headers, runtime)

    def run_network_content_audit_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunNetworkContentAuditRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunNetworkContentAuditResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunNetworkContentAuditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunNetworkContentAudit',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runNetworkContentAudit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunNetworkContentAuditResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_network_content_audit_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunNetworkContentAuditRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunNetworkContentAuditResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunNetworkContentAuditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunNetworkContentAudit',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runNetworkContentAudit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunNetworkContentAuditResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_network_content_audit_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunNetworkContentAuditRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunNetworkContentAuditResponse:
        tmp_req.validate()
        request = main_models.RunNetworkContentAuditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunNetworkContentAudit',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runNetworkContentAudit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNetworkContentAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_network_content_audit_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunNetworkContentAuditRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunNetworkContentAuditResponse:
        tmp_req.validate()
        request = main_models.RunNetworkContentAuditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunNetworkContentAudit',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runNetworkContentAudit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNetworkContentAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_network_content_audit(
        self,
        workspace_id: str,
        request: main_models.RunNetworkContentAuditRequest,
    ) -> main_models.RunNetworkContentAuditResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_network_content_audit_with_options(workspace_id, request, headers, runtime)

    async def run_network_content_audit_async(
        self,
        workspace_id: str,
        request: main_models.RunNetworkContentAuditRequest,
    ) -> main_models.RunNetworkContentAuditResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_network_content_audit_with_options_async(workspace_id, request, headers, runtime)

    def run_ocr_parse_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunOcrParseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunOcrParseResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunOcrParse',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runOcrParse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunOcrParseResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_ocr_parse_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunOcrParseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunOcrParseResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunOcrParse',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runOcrParse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunOcrParseResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_ocr_parse_with_options(
        self,
        workspace_id: str,
        request: main_models.RunOcrParseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunOcrParseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunOcrParse',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runOcrParse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunOcrParseResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_ocr_parse_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunOcrParseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunOcrParseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunOcrParse',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runOcrParse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunOcrParseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_ocr_parse(
        self,
        workspace_id: str,
        request: main_models.RunOcrParseRequest,
    ) -> main_models.RunOcrParseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_ocr_parse_with_options(workspace_id, request, headers, runtime)

    async def run_ocr_parse_async(
        self,
        workspace_id: str,
        request: main_models.RunOcrParseRequest,
    ) -> main_models.RunOcrParseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_ocr_parse_with_options_async(workspace_id, request, headers, runtime)

    def run_script_chat_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunScriptChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunScriptChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_script_chat_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunScriptChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_script_chat_with_options(
        self,
        workspace_id: str,
        request: main_models.RunScriptChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_chat_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptChat',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptChat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_chat(
        self,
        workspace_id: str,
        request: main_models.RunScriptChatRequest,
    ) -> main_models.RunScriptChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_script_chat_with_options(workspace_id, request, headers, runtime)

    async def run_script_chat_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptChatRequest,
    ) -> main_models.RunScriptChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_script_chat_with_options_async(workspace_id, request, headers, runtime)

    def run_script_continue_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunScriptContinueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunScriptContinueResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        if not DaraCore.is_null(request.user_provided_content):
            body['userProvidedContent'] = request.user_provided_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptContinue',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptContinue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptContinueResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_script_continue_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptContinueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunScriptContinueResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        if not DaraCore.is_null(request.user_provided_content):
            body['userProvidedContent'] = request.user_provided_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptContinue',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptContinue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptContinueResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_script_continue_with_options(
        self,
        workspace_id: str,
        request: main_models.RunScriptContinueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptContinueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        if not DaraCore.is_null(request.user_provided_content):
            body['userProvidedContent'] = request.user_provided_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptContinue',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptContinue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptContinueResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_continue_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptContinueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptContinueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        if not DaraCore.is_null(request.user_provided_content):
            body['userProvidedContent'] = request.user_provided_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptContinue',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptContinue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptContinueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_continue(
        self,
        workspace_id: str,
        request: main_models.RunScriptContinueRequest,
    ) -> main_models.RunScriptContinueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_script_continue_with_options(workspace_id, request, headers, runtime)

    async def run_script_continue_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptContinueRequest,
    ) -> main_models.RunScriptContinueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_script_continue_with_options_async(workspace_id, request, headers, runtime)

    def run_script_planning_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunScriptPlanningRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunScriptPlanningResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_note):
            body['additionalNote'] = request.additional_note
        if not DaraCore.is_null(request.dialogue_in_scene):
            body['dialogueInScene'] = request.dialogue_in_scene
        if not DaraCore.is_null(request.plot_conflict):
            body['plotConflict'] = request.plot_conflict
        if not DaraCore.is_null(request.script_name):
            body['scriptName'] = request.script_name
        if not DaraCore.is_null(request.script_shot_count):
            body['scriptShotCount'] = request.script_shot_count
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptPlanning',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptPlanning',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptPlanningResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_script_planning_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptPlanningRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunScriptPlanningResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_note):
            body['additionalNote'] = request.additional_note
        if not DaraCore.is_null(request.dialogue_in_scene):
            body['dialogueInScene'] = request.dialogue_in_scene
        if not DaraCore.is_null(request.plot_conflict):
            body['plotConflict'] = request.plot_conflict
        if not DaraCore.is_null(request.script_name):
            body['scriptName'] = request.script_name
        if not DaraCore.is_null(request.script_shot_count):
            body['scriptShotCount'] = request.script_shot_count
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptPlanning',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptPlanning',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptPlanningResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_script_planning_with_options(
        self,
        workspace_id: str,
        request: main_models.RunScriptPlanningRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptPlanningResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_note):
            body['additionalNote'] = request.additional_note
        if not DaraCore.is_null(request.dialogue_in_scene):
            body['dialogueInScene'] = request.dialogue_in_scene
        if not DaraCore.is_null(request.plot_conflict):
            body['plotConflict'] = request.plot_conflict
        if not DaraCore.is_null(request.script_name):
            body['scriptName'] = request.script_name
        if not DaraCore.is_null(request.script_shot_count):
            body['scriptShotCount'] = request.script_shot_count
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptPlanning',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptPlanning',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptPlanningResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_planning_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptPlanningRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptPlanningResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_note):
            body['additionalNote'] = request.additional_note
        if not DaraCore.is_null(request.dialogue_in_scene):
            body['dialogueInScene'] = request.dialogue_in_scene
        if not DaraCore.is_null(request.plot_conflict):
            body['plotConflict'] = request.plot_conflict
        if not DaraCore.is_null(request.script_name):
            body['scriptName'] = request.script_name
        if not DaraCore.is_null(request.script_shot_count):
            body['scriptShotCount'] = request.script_shot_count
        if not DaraCore.is_null(request.script_summary):
            body['scriptSummary'] = request.script_summary
        if not DaraCore.is_null(request.script_type_keyword):
            body['scriptTypeKeyword'] = request.script_type_keyword
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptPlanning',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptPlanning',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptPlanningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_planning(
        self,
        workspace_id: str,
        request: main_models.RunScriptPlanningRequest,
    ) -> main_models.RunScriptPlanningResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_script_planning_with_options(workspace_id, request, headers, runtime)

    async def run_script_planning_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptPlanningRequest,
    ) -> main_models.RunScriptPlanningResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_script_planning_with_options_async(workspace_id, request, headers, runtime)

    def run_script_refine_with_sse(
        self,
        workspace_id: str,
        request: main_models.RunScriptRefineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunScriptRefineResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptRefine',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptRefine',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptRefineResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_script_refine_with_sse_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptRefineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunScriptRefineResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptRefine',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptRefine',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunScriptRefineResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_script_refine_with_options(
        self,
        workspace_id: str,
        request: main_models.RunScriptRefineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptRefineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptRefine',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptRefine',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptRefineResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_script_refine_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptRefineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunScriptRefineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunScriptRefine',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runScriptRefine',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunScriptRefineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_script_refine(
        self,
        workspace_id: str,
        request: main_models.RunScriptRefineRequest,
    ) -> main_models.RunScriptRefineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_script_refine_with_options(workspace_id, request, headers, runtime)

    async def run_script_refine_async(
        self,
        workspace_id: str,
        request: main_models.RunScriptRefineRequest,
    ) -> main_models.RunScriptRefineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_script_refine_with_options_async(workspace_id, request, headers, runtime)

    def run_style_writing_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunStyleWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunStyleWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunStyleWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.learning_samples):
            request.learning_samples_shrink = Utils.array_to_string_with_specified_style(tmp_req.learning_samples, 'learningSamples', 'json')
        if not DaraCore.is_null(tmp_req.reference_materials):
            request.reference_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_materials, 'referenceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.learning_samples_shrink):
            body['learningSamples'] = request.learning_samples_shrink
        if not DaraCore.is_null(request.process_stage):
            body['processStage'] = request.process_stage
        if not DaraCore.is_null(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not DaraCore.is_null(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not DaraCore.is_null(request.use_search):
            body['useSearch'] = request.use_search
        if not DaraCore.is_null(request.writing_theme):
            body['writingTheme'] = request.writing_theme
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runStyleWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunStyleWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_style_writing_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunStyleWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunStyleWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunStyleWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.learning_samples):
            request.learning_samples_shrink = Utils.array_to_string_with_specified_style(tmp_req.learning_samples, 'learningSamples', 'json')
        if not DaraCore.is_null(tmp_req.reference_materials):
            request.reference_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_materials, 'referenceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.learning_samples_shrink):
            body['learningSamples'] = request.learning_samples_shrink
        if not DaraCore.is_null(request.process_stage):
            body['processStage'] = request.process_stage
        if not DaraCore.is_null(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not DaraCore.is_null(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not DaraCore.is_null(request.use_search):
            body['useSearch'] = request.use_search
        if not DaraCore.is_null(request.writing_theme):
            body['writingTheme'] = request.writing_theme
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runStyleWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunStyleWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_style_writing_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunStyleWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunStyleWritingResponse:
        tmp_req.validate()
        request = main_models.RunStyleWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.learning_samples):
            request.learning_samples_shrink = Utils.array_to_string_with_specified_style(tmp_req.learning_samples, 'learningSamples', 'json')
        if not DaraCore.is_null(tmp_req.reference_materials):
            request.reference_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_materials, 'referenceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.learning_samples_shrink):
            body['learningSamples'] = request.learning_samples_shrink
        if not DaraCore.is_null(request.process_stage):
            body['processStage'] = request.process_stage
        if not DaraCore.is_null(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not DaraCore.is_null(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not DaraCore.is_null(request.use_search):
            body['useSearch'] = request.use_search
        if not DaraCore.is_null(request.writing_theme):
            body['writingTheme'] = request.writing_theme
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runStyleWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunStyleWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_style_writing_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunStyleWritingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunStyleWritingResponse:
        tmp_req.validate()
        request = main_models.RunStyleWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.learning_samples):
            request.learning_samples_shrink = Utils.array_to_string_with_specified_style(tmp_req.learning_samples, 'learningSamples', 'json')
        if not DaraCore.is_null(tmp_req.reference_materials):
            request.reference_materials_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_materials, 'referenceMaterials', 'json')
        body = {}
        if not DaraCore.is_null(request.learning_samples_shrink):
            body['learningSamples'] = request.learning_samples_shrink
        if not DaraCore.is_null(request.process_stage):
            body['processStage'] = request.process_stage
        if not DaraCore.is_null(request.reference_materials_shrink):
            body['referenceMaterials'] = request.reference_materials_shrink
        if not DaraCore.is_null(request.style_feature):
            body['styleFeature'] = request.style_feature
        if not DaraCore.is_null(request.use_search):
            body['useSearch'] = request.use_search
        if not DaraCore.is_null(request.writing_theme):
            body['writingTheme'] = request.writing_theme
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleWriting',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runStyleWriting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunStyleWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_style_writing(
        self,
        workspace_id: str,
        request: main_models.RunStyleWritingRequest,
    ) -> main_models.RunStyleWritingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_style_writing_with_options(workspace_id, request, headers, runtime)

    async def run_style_writing_async(
        self,
        workspace_id: str,
        request: main_models.RunStyleWritingRequest,
    ) -> main_models.RunStyleWritingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_style_writing_with_options_async(workspace_id, request, headers, runtime)

    def run_tag_mining_analysis_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunTagMiningAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunTagMiningAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTagMiningAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTagMiningAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runTagMiningAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTagMiningAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_tag_mining_analysis_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunTagMiningAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunTagMiningAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTagMiningAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTagMiningAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runTagMiningAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTagMiningAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_tag_mining_analysis_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunTagMiningAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunTagMiningAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunTagMiningAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTagMiningAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runTagMiningAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTagMiningAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_tag_mining_analysis_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunTagMiningAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunTagMiningAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunTagMiningAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTagMiningAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runTagMiningAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTagMiningAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_tag_mining_analysis(
        self,
        workspace_id: str,
        request: main_models.RunTagMiningAnalysisRequest,
    ) -> main_models.RunTagMiningAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_tag_mining_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_tag_mining_analysis_async(
        self,
        workspace_id: str,
        request: main_models.RunTagMiningAnalysisRequest,
    ) -> main_models.RunTagMiningAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_tag_mining_analysis_with_options_async(workspace_id, request, headers, runtime)

    def run_video_analysis_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunVideoAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunVideoAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_document_param):
            request.add_document_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_document_param, 'addDocumentParam', 'json')
        if not DaraCore.is_null(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not DaraCore.is_null(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = Utils.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not DaraCore.is_null(tmp_req.video_caption_info):
            request.video_caption_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'videoUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.add_document_param_shrink):
            body['addDocumentParam'] = request.add_document_param_shrink
        if not DaraCore.is_null(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not DaraCore.is_null(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not DaraCore.is_null(request.split_type):
            body['splitType'] = request.split_type
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not DaraCore.is_null(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not DaraCore.is_null(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not DaraCore.is_null(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not DaraCore.is_null(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not DaraCore.is_null(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.video_urls_shrink):
            body['videoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunVideoAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_video_analysis_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunVideoAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunVideoAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_document_param):
            request.add_document_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_document_param, 'addDocumentParam', 'json')
        if not DaraCore.is_null(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not DaraCore.is_null(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = Utils.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not DaraCore.is_null(tmp_req.video_caption_info):
            request.video_caption_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'videoUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.add_document_param_shrink):
            body['addDocumentParam'] = request.add_document_param_shrink
        if not DaraCore.is_null(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not DaraCore.is_null(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not DaraCore.is_null(request.split_type):
            body['splitType'] = request.split_type
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not DaraCore.is_null(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not DaraCore.is_null(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not DaraCore.is_null(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not DaraCore.is_null(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not DaraCore.is_null(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.video_urls_shrink):
            body['videoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunVideoAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_video_analysis_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunVideoAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunVideoAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_document_param):
            request.add_document_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_document_param, 'addDocumentParam', 'json')
        if not DaraCore.is_null(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not DaraCore.is_null(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = Utils.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not DaraCore.is_null(tmp_req.video_caption_info):
            request.video_caption_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'videoUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.add_document_param_shrink):
            body['addDocumentParam'] = request.add_document_param_shrink
        if not DaraCore.is_null(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not DaraCore.is_null(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not DaraCore.is_null(request.split_type):
            body['splitType'] = request.split_type
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not DaraCore.is_null(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not DaraCore.is_null(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not DaraCore.is_null(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not DaraCore.is_null(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not DaraCore.is_null(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.video_urls_shrink):
            body['videoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunVideoAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_video_analysis_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunVideoAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunVideoAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_document_param):
            request.add_document_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_document_param, 'addDocumentParam', 'json')
        if not DaraCore.is_null(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not DaraCore.is_null(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = Utils.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not DaraCore.is_null(tmp_req.video_caption_info):
            request.video_caption_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'videoUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.add_document_param_shrink):
            body['addDocumentParam'] = request.add_document_param_shrink
        if not DaraCore.is_null(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not DaraCore.is_null(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not DaraCore.is_null(request.split_type):
            body['splitType'] = request.split_type
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not DaraCore.is_null(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not DaraCore.is_null(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not DaraCore.is_null(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not DaraCore.is_null(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not DaraCore.is_null(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.video_urls_shrink):
            body['videoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoAnalysis',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoAnalysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunVideoAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_video_analysis(
        self,
        workspace_id: str,
        request: main_models.RunVideoAnalysisRequest,
    ) -> main_models.RunVideoAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_video_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_video_analysis_async(
        self,
        workspace_id: str,
        request: main_models.RunVideoAnalysisRequest,
    ) -> main_models.RunVideoAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_video_analysis_with_options_async(workspace_id, request, headers, runtime)

    def run_video_detect_shot_with_sse(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoDetectShotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunVideoDetectShotResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunVideoDetectShotShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'options', 'json')
        if not DaraCore.is_null(tmp_req.recognition_options):
            request.recognition_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.recognition_options, 'recognitionOptions', 'json')
        body = {}
        if not DaraCore.is_null(request.intelli_simp_prompt):
            body['intelliSimpPrompt'] = request.intelli_simp_prompt
        if not DaraCore.is_null(request.intelli_simp_prompt_template_id):
            body['intelliSimpPromptTemplateId'] = request.intelli_simp_prompt_template_id
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_vl_custom_prompt_template_id):
            body['modelVlCustomPromptTemplateId'] = request.model_vl_custom_prompt_template_id
        if not DaraCore.is_null(request.options_shrink):
            body['options'] = request.options_shrink
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.pre_model_id):
            body['preModelId'] = request.pre_model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.recognition_options_shrink):
            body['recognitionOptions'] = request.recognition_options_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.vl_prompt):
            body['vlPrompt'] = request.vl_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoDetectShot',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoDetectShot',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunVideoDetectShotResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_video_detect_shot_with_sse_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoDetectShotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunVideoDetectShotResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunVideoDetectShotShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'options', 'json')
        if not DaraCore.is_null(tmp_req.recognition_options):
            request.recognition_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.recognition_options, 'recognitionOptions', 'json')
        body = {}
        if not DaraCore.is_null(request.intelli_simp_prompt):
            body['intelliSimpPrompt'] = request.intelli_simp_prompt
        if not DaraCore.is_null(request.intelli_simp_prompt_template_id):
            body['intelliSimpPromptTemplateId'] = request.intelli_simp_prompt_template_id
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_vl_custom_prompt_template_id):
            body['modelVlCustomPromptTemplateId'] = request.model_vl_custom_prompt_template_id
        if not DaraCore.is_null(request.options_shrink):
            body['options'] = request.options_shrink
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.pre_model_id):
            body['preModelId'] = request.pre_model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.recognition_options_shrink):
            body['recognitionOptions'] = request.recognition_options_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.vl_prompt):
            body['vlPrompt'] = request.vl_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoDetectShot',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoDetectShot',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunVideoDetectShotResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_video_detect_shot_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoDetectShotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunVideoDetectShotResponse:
        tmp_req.validate()
        request = main_models.RunVideoDetectShotShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'options', 'json')
        if not DaraCore.is_null(tmp_req.recognition_options):
            request.recognition_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.recognition_options, 'recognitionOptions', 'json')
        body = {}
        if not DaraCore.is_null(request.intelli_simp_prompt):
            body['intelliSimpPrompt'] = request.intelli_simp_prompt
        if not DaraCore.is_null(request.intelli_simp_prompt_template_id):
            body['intelliSimpPromptTemplateId'] = request.intelli_simp_prompt_template_id
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_vl_custom_prompt_template_id):
            body['modelVlCustomPromptTemplateId'] = request.model_vl_custom_prompt_template_id
        if not DaraCore.is_null(request.options_shrink):
            body['options'] = request.options_shrink
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.pre_model_id):
            body['preModelId'] = request.pre_model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.recognition_options_shrink):
            body['recognitionOptions'] = request.recognition_options_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.vl_prompt):
            body['vlPrompt'] = request.vl_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoDetectShot',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoDetectShot',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunVideoDetectShotResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_video_detect_shot_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RunVideoDetectShotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunVideoDetectShotResponse:
        tmp_req.validate()
        request = main_models.RunVideoDetectShotShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'options', 'json')
        if not DaraCore.is_null(tmp_req.recognition_options):
            request.recognition_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.recognition_options, 'recognitionOptions', 'json')
        body = {}
        if not DaraCore.is_null(request.intelli_simp_prompt):
            body['intelliSimpPrompt'] = request.intelli_simp_prompt
        if not DaraCore.is_null(request.intelli_simp_prompt_template_id):
            body['intelliSimpPromptTemplateId'] = request.intelli_simp_prompt_template_id
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_vl_custom_prompt_template_id):
            body['modelVlCustomPromptTemplateId'] = request.model_vl_custom_prompt_template_id
        if not DaraCore.is_null(request.options_shrink):
            body['options'] = request.options_shrink
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.pre_model_id):
            body['preModelId'] = request.pre_model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.recognition_options_shrink):
            body['recognitionOptions'] = request.recognition_options_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.vl_prompt):
            body['vlPrompt'] = request.vl_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoDetectShot',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/runVideoDetectShot',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunVideoDetectShotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_video_detect_shot(
        self,
        workspace_id: str,
        request: main_models.RunVideoDetectShotRequest,
    ) -> main_models.RunVideoDetectShotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_video_detect_shot_with_options(workspace_id, request, headers, runtime)

    async def run_video_detect_shot_async(
        self,
        workspace_id: str,
        request: main_models.RunVideoDetectShotRequest,
    ) -> main_models.RunVideoDetectShotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_video_detect_shot_with_options_async(workspace_id, request, headers, runtime)

    def submit_enterprise_voc_analysis_task_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEnterpriseVocAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitEnterpriseVocAnalysisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_enterprise_voc_analysis_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'filterTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.file_key):
            body['fileKey'] = request.file_key
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['filterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.source_trace):
            body['sourceTrace'] = request.source_trace
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEnterpriseVocAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitEnterpriseVocAnalysisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_enterprise_voc_analysis_task(
        self,
        workspace_id: str,
        request: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_enterprise_voc_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def submit_enterprise_voc_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_enterprise_voc_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_essay_correction_task_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEssayCorrectionTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitEssayCorrectionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'tasks', 'json')
        body = {}
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.subject):
            body['subject'] = request.subject
        if not DaraCore.is_null(request.tasks_shrink):
            body['tasks'] = request.tasks_shrink
        if not DaraCore.is_null(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEssayCorrectionTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitEssayCorrectionTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEssayCorrectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_essay_correction_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitEssayCorrectionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEssayCorrectionTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitEssayCorrectionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tasks):
            request.tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.tasks, 'tasks', 'json')
        body = {}
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.other_review_points):
            body['otherReviewPoints'] = request.other_review_points
        if not DaraCore.is_null(request.question):
            body['question'] = request.question
        if not DaraCore.is_null(request.subject):
            body['subject'] = request.subject
        if not DaraCore.is_null(request.tasks_shrink):
            body['tasks'] = request.tasks_shrink
        if not DaraCore.is_null(request.total_score):
            body['totalScore'] = request.total_score
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEssayCorrectionTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitEssayCorrectionTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEssayCorrectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_essay_correction_task(
        self,
        workspace_id: str,
        request: main_models.SubmitEssayCorrectionTaskRequest,
    ) -> main_models.SubmitEssayCorrectionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_essay_correction_task_with_options(workspace_id, request, headers, runtime)

    async def submit_essay_correction_task_async(
        self,
        workspace_id: str,
        request: main_models.SubmitEssayCorrectionTaskRequest,
    ) -> main_models.SubmitEssayCorrectionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_essay_correction_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_tag_mining_analysis_task_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTagMiningAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitTagMiningAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTagMiningAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitTagMiningAnalysisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTagMiningAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_tag_mining_analysis_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitTagMiningAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTagMiningAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitTagMiningAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'contents', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.contents_shrink):
            body['contents'] = request.contents_shrink
        if not DaraCore.is_null(request.extra_info):
            body['extraInfo'] = request.extra_info
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.output_format):
            body['outputFormat'] = request.output_format
        if not DaraCore.is_null(request.tags_shrink):
            body['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.url):
            body['url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTagMiningAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitTagMiningAnalysisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTagMiningAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_tag_mining_analysis_task(
        self,
        workspace_id: str,
        request: main_models.SubmitTagMiningAnalysisTaskRequest,
    ) -> main_models.SubmitTagMiningAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_tag_mining_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def submit_tag_mining_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.SubmitTagMiningAnalysisTaskRequest,
    ) -> main_models.SubmitTagMiningAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_tag_mining_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_video_analysis_task_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitVideoAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_document_param):
            request.add_document_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_document_param, 'addDocumentParam', 'json')
        if not DaraCore.is_null(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not DaraCore.is_null(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = Utils.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not DaraCore.is_null(tmp_req.video_caption_info):
            request.video_caption_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'videoUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.add_document_param_shrink):
            body['addDocumentParam'] = request.add_document_param_shrink
        if not DaraCore.is_null(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not DaraCore.is_null(request.deduplication_id):
            body['deduplicationId'] = request.deduplication_id
        if not DaraCore.is_null(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not DaraCore.is_null(request.split_type):
            body['splitType'] = request.split_type
        if not DaraCore.is_null(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not DaraCore.is_null(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not DaraCore.is_null(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not DaraCore.is_null(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not DaraCore.is_null(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not DaraCore.is_null(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.video_urls_shrink):
            body['videoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/submitVideoAnalysisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_analysis_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitVideoAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_document_param):
            request.add_document_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_document_param, 'addDocumentParam', 'json')
        if not DaraCore.is_null(tmp_req.exclude_generate_options):
            request.exclude_generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_generate_options, 'excludeGenerateOptions', 'json')
        if not DaraCore.is_null(tmp_req.frame_sample_method):
            request.frame_sample_method_shrink = Utils.array_to_string_with_specified_style(tmp_req.frame_sample_method, 'frameSampleMethod', 'json')
        if not DaraCore.is_null(tmp_req.generate_options):
            request.generate_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.generate_options, 'generateOptions', 'json')
        if not DaraCore.is_null(tmp_req.text_process_tasks):
            request.text_process_tasks_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_process_tasks, 'textProcessTasks', 'json')
        if not DaraCore.is_null(tmp_req.video_caption_info):
            request.video_caption_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_caption_info, 'videoCaptionInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'videoRoles', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'videoUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.add_document_param_shrink):
            body['addDocumentParam'] = request.add_document_param_shrink
        if not DaraCore.is_null(request.auto_role_recognition_video_url):
            body['autoRoleRecognitionVideoUrl'] = request.auto_role_recognition_video_url
        if not DaraCore.is_null(request.deduplication_id):
            body['deduplicationId'] = request.deduplication_id
        if not DaraCore.is_null(request.exclude_generate_options_shrink):
            body['excludeGenerateOptions'] = request.exclude_generate_options_shrink
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['faceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.frame_sample_method_shrink):
            body['frameSampleMethod'] = request.frame_sample_method_shrink
        if not DaraCore.is_null(request.generate_options_shrink):
            body['generateOptions'] = request.generate_options_shrink
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template):
            body['modelCustomPromptTemplate'] = request.model_custom_prompt_template
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.snapshot_interval):
            body['snapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.split_interval):
            body['splitInterval'] = request.split_interval
        if not DaraCore.is_null(request.split_type):
            body['splitType'] = request.split_type
        if not DaraCore.is_null(request.text_process_tasks_shrink):
            body['textProcessTasks'] = request.text_process_tasks_shrink
        if not DaraCore.is_null(request.video_caption_info_shrink):
            body['videoCaptionInfo'] = request.video_caption_info_shrink
        if not DaraCore.is_null(request.video_extra_info):
            body['videoExtraInfo'] = request.video_extra_info
        if not DaraCore.is_null(request.video_model_custom_prompt_template):
            body['videoModelCustomPromptTemplate'] = request.video_model_custom_prompt_template
        if not DaraCore.is_null(request.video_model_id):
            body['videoModelId'] = request.video_model_id
        if not DaraCore.is_null(request.video_roles_shrink):
            body['videoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['videoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.video_urls_shrink):
            body['videoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/submitVideoAnalysisTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_analysis_task(
        self,
        workspace_id: str,
        request: main_models.SubmitVideoAnalysisTaskRequest,
    ) -> main_models.SubmitVideoAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_video_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def submit_video_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.SubmitVideoAnalysisTaskRequest,
    ) -> main_models.SubmitVideoAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_video_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def submit_video_detect_shot_task_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitVideoDetectShotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoDetectShotTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitVideoDetectShotTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'options', 'json')
        if not DaraCore.is_null(tmp_req.recognition_options):
            request.recognition_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.recognition_options, 'recognitionOptions', 'json')
        body = {}
        if not DaraCore.is_null(request.deduplication_id):
            body['deduplicationId'] = request.deduplication_id
        if not DaraCore.is_null(request.intelli_simp_prompt):
            body['intelliSimpPrompt'] = request.intelli_simp_prompt
        if not DaraCore.is_null(request.intelli_simp_prompt_template_id):
            body['intelliSimpPromptTemplateId'] = request.intelli_simp_prompt_template_id
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_vl_custom_prompt_template_id):
            body['modelVlCustomPromptTemplateId'] = request.model_vl_custom_prompt_template_id
        if not DaraCore.is_null(request.options_shrink):
            body['options'] = request.options_shrink
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.pre_model_id):
            body['preModelId'] = request.pre_model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.recognition_options_shrink):
            body['recognitionOptions'] = request.recognition_options_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.vl_prompt):
            body['vlPrompt'] = request.vl_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoDetectShotTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitVideoDetectShotTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoDetectShotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_detect_shot_task_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitVideoDetectShotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoDetectShotTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitVideoDetectShotTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'options', 'json')
        if not DaraCore.is_null(tmp_req.recognition_options):
            request.recognition_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.recognition_options, 'recognitionOptions', 'json')
        body = {}
        if not DaraCore.is_null(request.deduplication_id):
            body['deduplicationId'] = request.deduplication_id
        if not DaraCore.is_null(request.intelli_simp_prompt):
            body['intelliSimpPrompt'] = request.intelli_simp_prompt
        if not DaraCore.is_null(request.intelli_simp_prompt_template_id):
            body['intelliSimpPromptTemplateId'] = request.intelli_simp_prompt_template_id
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.model_custom_prompt_template_id):
            body['modelCustomPromptTemplateId'] = request.model_custom_prompt_template_id
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_vl_custom_prompt_template_id):
            body['modelVlCustomPromptTemplateId'] = request.model_vl_custom_prompt_template_id
        if not DaraCore.is_null(request.options_shrink):
            body['options'] = request.options_shrink
        if not DaraCore.is_null(request.original_session_id):
            body['originalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.pre_model_id):
            body['preModelId'] = request.pre_model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.recognition_options_shrink):
            body['recognitionOptions'] = request.recognition_options_shrink
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.video_url):
            body['videoUrl'] = request.video_url
        if not DaraCore.is_null(request.vl_prompt):
            body['vlPrompt'] = request.vl_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoDetectShotTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/submitVideoDetectShotTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoDetectShotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_detect_shot_task(
        self,
        workspace_id: str,
        request: main_models.SubmitVideoDetectShotTaskRequest,
    ) -> main_models.SubmitVideoDetectShotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_video_detect_shot_task_with_options(workspace_id, request, headers, runtime)

    async def submit_video_detect_shot_task_async(
        self,
        workspace_id: str,
        request: main_models.SubmitVideoDetectShotTaskRequest,
    ) -> main_models.SubmitVideoDetectShotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_video_detect_shot_task_with_options_async(workspace_id, request, headers, runtime)

    def update_video_analysis_config_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoAnalysisConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.async_concurrency):
            body['asyncConcurrency'] = request.async_concurrency
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoAnalysisConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoAnalysisConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_analysis_config_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoAnalysisConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.async_concurrency):
            body['asyncConcurrency'] = request.async_concurrency
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoAnalysisConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoAnalysisConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_analysis_config(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisConfigRequest,
    ) -> main_models.UpdateVideoAnalysisConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_video_analysis_config_with_options(workspace_id, request, headers, runtime)

    async def update_video_analysis_config_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisConfigRequest,
    ) -> main_models.UpdateVideoAnalysisConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_video_analysis_config_with_options_async(workspace_id, request, headers, runtime)

    def update_video_analysis_task_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_analysis_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoAnalysisTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_analysis_task(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisTaskRequest,
    ) -> main_models.UpdateVideoAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_video_analysis_task_with_options(workspace_id, request, headers, runtime)

    async def update_video_analysis_task_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisTaskRequest,
    ) -> main_models.UpdateVideoAnalysisTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_video_analysis_task_with_options_async(workspace_id, request, headers, runtime)

    def update_video_analysis_tasks_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.UpdateVideoAnalysisTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoAnalysisTasksResponse:
        tmp_req.validate()
        request = main_models.UpdateVideoAnalysisTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'taskIds', 'json')
        body = {}
        if not DaraCore.is_null(request.task_ids_shrink):
            body['taskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoAnalysisTasks',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisTasks',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoAnalysisTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_analysis_tasks_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.UpdateVideoAnalysisTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoAnalysisTasksResponse:
        tmp_req.validate()
        request = main_models.UpdateVideoAnalysisTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'taskIds', 'json')
        body = {}
        if not DaraCore.is_null(request.task_ids_shrink):
            body['taskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoAnalysisTasks',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoAnalysisTasks',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoAnalysisTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_analysis_tasks(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisTasksRequest,
    ) -> main_models.UpdateVideoAnalysisTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_video_analysis_tasks_with_options(workspace_id, request, headers, runtime)

    async def update_video_analysis_tasks_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoAnalysisTasksRequest,
    ) -> main_models.UpdateVideoAnalysisTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_video_analysis_tasks_with_options_async(workspace_id, request, headers, runtime)

    def update_video_detect_shot_config_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoDetectShotConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.async_concurrency):
            body['asyncConcurrency'] = request.async_concurrency
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoDetectShotConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoDetectShotConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoDetectShotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_detect_shot_config_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoDetectShotConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.async_concurrency):
            body['asyncConcurrency'] = request.async_concurrency
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoDetectShotConfig',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/videoAnalysis/updateVideoDetectShotConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoDetectShotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_detect_shot_config(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotConfigRequest,
    ) -> main_models.UpdateVideoDetectShotConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_video_detect_shot_config_with_options(workspace_id, request, headers, runtime)

    async def update_video_detect_shot_config_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotConfigRequest,
    ) -> main_models.UpdateVideoDetectShotConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_video_detect_shot_config_with_options_async(workspace_id, request, headers, runtime)

    def update_video_detect_shot_task_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoDetectShotTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoDetectShotTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/updateVideoDetectShotTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoDetectShotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_detect_shot_task_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoDetectShotTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            body['taskStatus'] = request.task_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoDetectShotTask',
            version = '2024-08-01',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/quanmiao/lightapp/updateVideoDetectShotTask',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoDetectShotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_detect_shot_task(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotTaskRequest,
    ) -> main_models.UpdateVideoDetectShotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_video_detect_shot_task_with_options(workspace_id, request, headers, runtime)

    async def update_video_detect_shot_task_async(
        self,
        workspace_id: str,
        request: main_models.UpdateVideoDetectShotTaskRequest,
    ) -> main_models.UpdateVideoDetectShotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_video_detect_shot_task_with_options_async(workspace_id, request, headers, runtime)
