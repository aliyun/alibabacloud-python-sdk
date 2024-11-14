# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_intelligentcreation20241107 import models as intelligent_creation_20241107_models
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
        request: intelligent_creation_20241107_models.CreateLabelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20241107_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_url):
            body['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.idempotent_id):
            body['idempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.label_template_id):
            body['labelTemplateId'] = request.label_template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTask',
            version='2024-11-07',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aitag/createLabelTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20241107_models.CreateLabelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_label_task_with_options_async(
        self,
        request: intelligent_creation_20241107_models.CreateLabelTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20241107_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_url):
            body['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.idempotent_id):
            body['idempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.label_template_id):
            body['labelTemplateId'] = request.label_template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTask',
            version='2024-11-07',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aitag/createLabelTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20241107_models.CreateLabelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_label_task(
        self,
        request: intelligent_creation_20241107_models.CreateLabelTaskRequest,
    ) -> intelligent_creation_20241107_models.CreateLabelTaskResponse:
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
        request: intelligent_creation_20241107_models.CreateLabelTaskRequest,
    ) -> intelligent_creation_20241107_models.CreateLabelTaskResponse:
        """
        @summary 创建模型标注任务
        
        @param request: CreateLabelTaskRequest
        @return: CreateLabelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_label_task_with_options_async(request, headers, runtime)

    def get_label_task_result_with_options(
        self,
        request: intelligent_creation_20241107_models.GetLabelTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20241107_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务结果
        
        @param request: GetLabelTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLabelTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLabelTaskResult',
            version='2024-11-07',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aitag/getLabelTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20241107_models.GetLabelTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_label_task_result_with_options_async(
        self,
        request: intelligent_creation_20241107_models.GetLabelTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20241107_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务结果
        
        @param request: GetLabelTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLabelTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLabelTaskResult',
            version='2024-11-07',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aitag/getLabelTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20241107_models.GetLabelTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_label_task_result(
        self,
        request: intelligent_creation_20241107_models.GetLabelTaskResultRequest,
    ) -> intelligent_creation_20241107_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务结果
        
        @param request: GetLabelTaskResultRequest
        @return: GetLabelTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_label_task_result_with_options(request, headers, runtime)

    async def get_label_task_result_async(
        self,
        request: intelligent_creation_20241107_models.GetLabelTaskResultRequest,
    ) -> intelligent_creation_20241107_models.GetLabelTaskResultResponse:
        """
        @summary 查询模型标注任务结果
        
        @param request: GetLabelTaskResultRequest
        @return: GetLabelTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_label_task_result_with_options_async(request, headers, runtime)
