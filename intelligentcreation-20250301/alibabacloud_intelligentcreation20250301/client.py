# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_intelligentcreation20250301 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_label_task_with_options(
        self,
        request: main_models.CreateLabelTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLabelTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        if not DaraCore.is_null(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLabelTask',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/aitag/createLabelTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLabelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_label_task_with_options_async(
        self,
        request: main_models.CreateLabelTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLabelTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        if not DaraCore.is_null(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLabelTask',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/aitag/createLabelTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLabelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_label_task(
        self,
        request: main_models.CreateLabelTaskRequest,
    ) -> main_models.CreateLabelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_label_task_with_options(request, headers, runtime)

    async def create_label_task_async(
        self,
        request: main_models.CreateLabelTaskRequest,
    ) -> main_models.CreateLabelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_label_task_with_options_async(request, headers, runtime)

    def create_oss_upload_token_with_options(
        self,
        request: main_models.CreateOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssUploadTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssUploadToken',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/base/createOssUploadToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_upload_token_with_options_async(
        self,
        request: main_models.CreateOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssUploadTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssUploadToken',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/base/createOssUploadToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_upload_token(
        self,
        request: main_models.CreateOssUploadTokenRequest,
    ) -> main_models.CreateOssUploadTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_oss_upload_token_with_options(request, headers, runtime)

    async def create_oss_upload_token_async(
        self,
        request: main_models.CreateOssUploadTokenRequest,
    ) -> main_models.CreateOssUploadTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_oss_upload_token_with_options_async(request, headers, runtime)

    def create_text_label_with_options(
        self,
        request: main_models.CreateTextLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextLabelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTextLabel',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/aitag/createTextLabel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTextLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_text_label_with_options_async(
        self,
        request: main_models.CreateTextLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextLabelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTextLabel',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/aitag/createTextLabel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTextLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_text_label(
        self,
        request: main_models.CreateTextLabelRequest,
    ) -> main_models.CreateTextLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_text_label_with_options(request, headers, runtime)

    async def create_text_label_async(
        self,
        request: main_models.CreateTextLabelRequest,
    ) -> main_models.CreateTextLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_text_label_with_options_async(request, headers, runtime)

    def get_label_task_result_with_options(
        self,
        request: main_models.GetLabelTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLabelTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLabelTaskResult',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/aitag/getLabelTaskResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLabelTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_label_task_result_with_options_async(
        self,
        request: main_models.GetLabelTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLabelTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLabelTaskResult',
            version = '2025-03-01',
            protocol = 'HTTPS',
            pathname = f'/tongjian/yic-tongjian/openService/v2/aitag/getLabelTaskResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLabelTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_label_task_result(
        self,
        request: main_models.GetLabelTaskResultRequest,
    ) -> main_models.GetLabelTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_label_task_result_with_options(request, headers, runtime)

    async def get_label_task_result_async(
        self,
        request: main_models.GetLabelTaskResultRequest,
    ) -> main_models.GetLabelTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_label_task_result_with_options_async(request, headers, runtime)
