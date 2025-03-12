# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_intelligentcreation20250301 import models as intelligent_creation_20250301_models
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

    def create_label_task_with_options(
        self,
        request: intelligent_creation_20250301_models.CreateLabelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTask',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/aitag/createLabelTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateLabelTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateLabelTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def create_label_task_with_options_async(
        self,
        request: intelligent_creation_20250301_models.CreateLabelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTask',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/aitag/createLabelTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateLabelTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateLabelTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_label_task(
        self,
        request: intelligent_creation_20250301_models.CreateLabelTaskRequest,
    ) -> intelligent_creation_20250301_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @return: CreateLabelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_label_task_with_options(request, headers, runtime)

    async def create_label_task_async(
        self,
        request: intelligent_creation_20250301_models.CreateLabelTaskRequest,
    ) -> intelligent_creation_20250301_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @return: CreateLabelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_label_task_with_options_async(request, headers, runtime)

    def create_oss_upload_token_with_options(
        self,
        request: intelligent_creation_20250301_models.CreateOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.CreateOssUploadTokenResponse:
        """
        @summary 创建OSS上传token
        
        @param request: CreateOssUploadTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssUploadTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssUploadToken',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/base/createOssUploadToken',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateOssUploadTokenResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateOssUploadTokenResponse(),
                self.execute(params, req, runtime)
            )

    async def create_oss_upload_token_with_options_async(
        self,
        request: intelligent_creation_20250301_models.CreateOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.CreateOssUploadTokenResponse:
        """
        @summary 创建OSS上传token
        
        @param request: CreateOssUploadTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssUploadTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssUploadToken',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/base/createOssUploadToken',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateOssUploadTokenResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateOssUploadTokenResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_oss_upload_token(
        self,
        request: intelligent_creation_20250301_models.CreateOssUploadTokenRequest,
    ) -> intelligent_creation_20250301_models.CreateOssUploadTokenResponse:
        """
        @summary 创建OSS上传token
        
        @param request: CreateOssUploadTokenRequest
        @return: CreateOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_upload_token_with_options(request, headers, runtime)

    async def create_oss_upload_token_async(
        self,
        request: intelligent_creation_20250301_models.CreateOssUploadTokenRequest,
    ) -> intelligent_creation_20250301_models.CreateOssUploadTokenResponse:
        """
        @summary 创建OSS上传token
        
        @param request: CreateOssUploadTokenRequest
        @return: CreateOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_oss_upload_token_with_options_async(request, headers, runtime)

    def create_text_label_with_options(
        self,
        request: intelligent_creation_20250301_models.CreateTextLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.CreateTextLabelResponse:
        """
        @summary 单条文本标注
        
        @param request: CreateTextLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTextLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTextLabel',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/aitag/createTextLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateTextLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateTextLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def create_text_label_with_options_async(
        self,
        request: intelligent_creation_20250301_models.CreateTextLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.CreateTextLabelResponse:
        """
        @summary 单条文本标注
        
        @param request: CreateTextLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTextLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.label_template_id):
            body['LabelTemplateId'] = request.label_template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTextLabel',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/aitag/createTextLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateTextLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.CreateTextLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_text_label(
        self,
        request: intelligent_creation_20250301_models.CreateTextLabelRequest,
    ) -> intelligent_creation_20250301_models.CreateTextLabelResponse:
        """
        @summary 单条文本标注
        
        @param request: CreateTextLabelRequest
        @return: CreateTextLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_text_label_with_options(request, headers, runtime)

    async def create_text_label_async(
        self,
        request: intelligent_creation_20250301_models.CreateTextLabelRequest,
    ) -> intelligent_creation_20250301_models.CreateTextLabelResponse:
        """
        @summary 单条文本标注
        
        @param request: CreateTextLabelRequest
        @return: CreateTextLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_text_label_with_options_async(request, headers, runtime)

    def get_label_task_result_with_options(
        self,
        request: intelligent_creation_20250301_models.GetLabelTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务
        
        @param request: GetLabelTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLabelTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLabelTaskResult',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/aitag/getLabelTaskResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.GetLabelTaskResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.GetLabelTaskResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_label_task_result_with_options_async(
        self,
        request: intelligent_creation_20250301_models.GetLabelTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20250301_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务
        
        @param request: GetLabelTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLabelTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLabelTaskResult',
            version='2025-03-01',
            protocol='HTTPS',
            pathname=f'/tongjian/yic-tongjian/openService/v2/aitag/getLabelTaskResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                intelligent_creation_20250301_models.GetLabelTaskResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                intelligent_creation_20250301_models.GetLabelTaskResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_label_task_result(
        self,
        request: intelligent_creation_20250301_models.GetLabelTaskResultRequest,
    ) -> intelligent_creation_20250301_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务
        
        @param request: GetLabelTaskResultRequest
        @return: GetLabelTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_label_task_result_with_options(request, headers, runtime)

    async def get_label_task_result_async(
        self,
        request: intelligent_creation_20250301_models.GetLabelTaskResultRequest,
    ) -> intelligent_creation_20250301_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务
        
        @param request: GetLabelTaskResultRequest
        @return: GetLabelTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_label_task_result_with_options_async(request, headers, runtime)
