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

    def add_text_feedback_with_options(
        self,
        request: intelligent_creation_20240313_models.AddTextFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.AddTextFeedbackResponse:
        """
        @summary 添加文案反馈
        
        @param request: AddTextFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTextFeedbackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.quality):
            body['quality'] = request.quality
        if not UtilClient.is_unset(request.text_id):
            body['textId'] = request.text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTextFeedback',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/addTextFeedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.AddTextFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_text_feedback_with_options_async(
        self,
        request: intelligent_creation_20240313_models.AddTextFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.AddTextFeedbackResponse:
        """
        @summary 添加文案反馈
        
        @param request: AddTextFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTextFeedbackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.quality):
            body['quality'] = request.quality
        if not UtilClient.is_unset(request.text_id):
            body['textId'] = request.text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTextFeedback',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/addTextFeedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.AddTextFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_text_feedback(
        self,
        request: intelligent_creation_20240313_models.AddTextFeedbackRequest,
    ) -> intelligent_creation_20240313_models.AddTextFeedbackResponse:
        """
        @summary 添加文案反馈
        
        @param request: AddTextFeedbackRequest
        @return: AddTextFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_text_feedback_with_options(request, headers, runtime)

    async def add_text_feedback_async(
        self,
        request: intelligent_creation_20240313_models.AddTextFeedbackRequest,
    ) -> intelligent_creation_20240313_models.AddTextFeedbackResponse:
        """
        @summary 添加文案反馈
        
        @param request: AddTextFeedbackRequest
        @return: AddTextFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_text_feedback_with_options_async(request, headers, runtime)

    def batch_add_document_with_options(
        self,
        knowledge_base_id: str,
        request: intelligent_creation_20240313_models.BatchAddDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchAddDocumentResponse:
        """
        @summary 批量添加知识文档
        
        @param request: BatchAddDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_document_infos):
            body['addDocumentInfos'] = request.add_document_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddDocument',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/knowledge-base/{OpenApiUtilClient.get_encode_param(knowledge_base_id)}/documents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchAddDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_document_with_options_async(
        self,
        knowledge_base_id: str,
        request: intelligent_creation_20240313_models.BatchAddDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchAddDocumentResponse:
        """
        @summary 批量添加知识文档
        
        @param request: BatchAddDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add_document_infos):
            body['addDocumentInfos'] = request.add_document_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddDocument',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/knowledge-base/{OpenApiUtilClient.get_encode_param(knowledge_base_id)}/documents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchAddDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_document(
        self,
        knowledge_base_id: str,
        request: intelligent_creation_20240313_models.BatchAddDocumentRequest,
    ) -> intelligent_creation_20240313_models.BatchAddDocumentResponse:
        """
        @summary 批量添加知识文档
        
        @param request: BatchAddDocumentRequest
        @return: BatchAddDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_add_document_with_options(knowledge_base_id, request, headers, runtime)

    async def batch_add_document_async(
        self,
        knowledge_base_id: str,
        request: intelligent_creation_20240313_models.BatchAddDocumentRequest,
    ) -> intelligent_creation_20240313_models.BatchAddDocumentResponse:
        """
        @summary 批量添加知识文档
        
        @param request: BatchAddDocumentRequest
        @return: BatchAddDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_add_document_with_options_async(knowledge_base_id, request, headers, runtime)

    def batch_create_aicoach_task_with_options(
        self,
        request: intelligent_creation_20240313_models.BatchCreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchCreateAICoachTaskResponse:
        """
        @summary 批量发布剧本任务
        
        @param request: BatchCreateAICoachTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateAICoachTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not UtilClient.is_unset(request.student_ids):
            body['studentIds'] = request.student_ids
        if not UtilClient.is_unset(request.student_list):
            body['studentList'] = request.student_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateAICoachTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/batchCreateTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchCreateAICoachTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_aicoach_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.BatchCreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchCreateAICoachTaskResponse:
        """
        @summary 批量发布剧本任务
        
        @param request: BatchCreateAICoachTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateAICoachTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not UtilClient.is_unset(request.student_ids):
            body['studentIds'] = request.student_ids
        if not UtilClient.is_unset(request.student_list):
            body['studentList'] = request.student_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateAICoachTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/batchCreateTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchCreateAICoachTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_aicoach_task(
        self,
        request: intelligent_creation_20240313_models.BatchCreateAICoachTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchCreateAICoachTaskResponse:
        """
        @summary 批量发布剧本任务
        
        @param request: BatchCreateAICoachTaskRequest
        @return: BatchCreateAICoachTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_aicoach_task_with_options(request, headers, runtime)

    async def batch_create_aicoach_task_async(
        self,
        request: intelligent_creation_20240313_models.BatchCreateAICoachTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchCreateAICoachTaskResponse:
        """
        @summary 批量发布剧本任务
        
        @param request: BatchCreateAICoachTaskRequest
        @return: BatchCreateAICoachTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_create_aicoach_task_with_options_async(request, headers, runtime)

    def batch_get_project_task_with_options(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchGetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchGetProjectTaskResponse:
        """
        @summary 批量查询项目信息
        
        @param tmp_req: BatchGetProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetProjectTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchGetProjectTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/batchGetProjectTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchGetProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_project_task_with_options_async(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchGetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchGetProjectTaskResponse:
        """
        @summary 批量查询项目信息
        
        @param tmp_req: BatchGetProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetProjectTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchGetProjectTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/batchGetProjectTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchGetProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_project_task(
        self,
        request: intelligent_creation_20240313_models.BatchGetProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchGetProjectTaskResponse:
        """
        @summary 批量查询项目信息
        
        @param request: BatchGetProjectTaskRequest
        @return: BatchGetProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_project_task_with_options(request, headers, runtime)

    async def batch_get_project_task_async(
        self,
        request: intelligent_creation_20240313_models.BatchGetProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchGetProjectTaskResponse:
        """
        @summary 批量查询项目信息
        
        @param request: BatchGetProjectTaskRequest
        @return: BatchGetProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_project_task_with_options_async(request, headers, runtime)

    def batch_get_train_task_with_options(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchGetTrainTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchGetTrainTaskResponse:
        """
        @summary 批量查询声音复刻任务
        
        @param tmp_req: BatchGetTrainTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetTrainTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchGetTrainTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.aliyun_main_id):
            query['aliyunMainId'] = request.aliyun_main_id
        if not UtilClient.is_unset(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetTrainTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/train/task/batchGetTrainTaskInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchGetTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_train_task_with_options_async(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchGetTrainTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchGetTrainTaskResponse:
        """
        @summary 批量查询声音复刻任务
        
        @param tmp_req: BatchGetTrainTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetTrainTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchGetTrainTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.aliyun_main_id):
            query['aliyunMainId'] = request.aliyun_main_id
        if not UtilClient.is_unset(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetTrainTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/train/task/batchGetTrainTaskInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchGetTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_train_task(
        self,
        request: intelligent_creation_20240313_models.BatchGetTrainTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchGetTrainTaskResponse:
        """
        @summary 批量查询声音复刻任务
        
        @param request: BatchGetTrainTaskRequest
        @return: BatchGetTrainTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_train_task_with_options(request, headers, runtime)

    async def batch_get_train_task_async(
        self,
        request: intelligent_creation_20240313_models.BatchGetTrainTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchGetTrainTaskResponse:
        """
        @summary 批量查询声音复刻任务
        
        @param request: BatchGetTrainTaskRequest
        @return: BatchGetTrainTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_train_task_with_options_async(request, headers, runtime)

    def batch_get_video_clip_task_with_options(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchGetVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchGetVideoClipTaskResponse:
        """
        @summary 批量查询视频切片任务信息
        
        @param tmp_req: BatchGetVideoClipTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetVideoClipTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchGetVideoClipTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetVideoClipTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/clip/batchGetVideoClipTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchGetVideoClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_video_clip_task_with_options_async(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchGetVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchGetVideoClipTaskResponse:
        """
        @summary 批量查询视频切片任务信息
        
        @param tmp_req: BatchGetVideoClipTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetVideoClipTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchGetVideoClipTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetVideoClipTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/clip/batchGetVideoClipTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchGetVideoClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_video_clip_task(
        self,
        request: intelligent_creation_20240313_models.BatchGetVideoClipTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchGetVideoClipTaskResponse:
        """
        @summary 批量查询视频切片任务信息
        
        @param request: BatchGetVideoClipTaskRequest
        @return: BatchGetVideoClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_video_clip_task_with_options(request, headers, runtime)

    async def batch_get_video_clip_task_async(
        self,
        request: intelligent_creation_20240313_models.BatchGetVideoClipTaskRequest,
    ) -> intelligent_creation_20240313_models.BatchGetVideoClipTaskResponse:
        """
        @summary 批量查询视频切片任务信息
        
        @param request: BatchGetVideoClipTaskRequest
        @return: BatchGetVideoClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_video_clip_task_with_options_async(request, headers, runtime)

    def batch_query_individuation_text_with_options(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchQueryIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchQueryIndividuationTextResponse:
        """
        @summary 批量查询文案
        
        @param tmp_req: BatchQueryIndividuationTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchQueryIndividuationTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchQueryIndividuationTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.text_id_list):
            request.text_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_id_list, 'textIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.text_id_list_shrink):
            query['textIdList'] = request.text_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQueryIndividuationText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/batchQueryText',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchQueryIndividuationTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_individuation_text_with_options_async(
        self,
        tmp_req: intelligent_creation_20240313_models.BatchQueryIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.BatchQueryIndividuationTextResponse:
        """
        @summary 批量查询文案
        
        @param tmp_req: BatchQueryIndividuationTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchQueryIndividuationTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.BatchQueryIndividuationTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.text_id_list):
            request.text_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_id_list, 'textIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.text_id_list_shrink):
            query['textIdList'] = request.text_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQueryIndividuationText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/batchQueryText',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.BatchQueryIndividuationTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_individuation_text(
        self,
        request: intelligent_creation_20240313_models.BatchQueryIndividuationTextRequest,
    ) -> intelligent_creation_20240313_models.BatchQueryIndividuationTextResponse:
        """
        @summary 批量查询文案
        
        @param request: BatchQueryIndividuationTextRequest
        @return: BatchQueryIndividuationTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_query_individuation_text_with_options(request, headers, runtime)

    async def batch_query_individuation_text_async(
        self,
        request: intelligent_creation_20240313_models.BatchQueryIndividuationTextRequest,
    ) -> intelligent_creation_20240313_models.BatchQueryIndividuationTextResponse:
        """
        @summary 批量查询文案
        
        @param request: BatchQueryIndividuationTextRequest
        @return: BatchQueryIndividuationTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_query_individuation_text_with_options_async(request, headers, runtime)

    def check_session_with_options(
        self,
        request: intelligent_creation_20240313_models.CheckSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CheckSessionResponse:
        """
        @summary 检查会话状态
        
        @param request: CheckSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/checkSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CheckSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_session_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CheckSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CheckSessionResponse:
        """
        @summary 检查会话状态
        
        @param request: CheckSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/checkSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CheckSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_session(
        self,
        request: intelligent_creation_20240313_models.CheckSessionRequest,
    ) -> intelligent_creation_20240313_models.CheckSessionResponse:
        """
        @summary 检查会话状态
        
        @param request: CheckSessionRequest
        @return: CheckSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_session_with_options(request, headers, runtime)

    async def check_session_async(
        self,
        request: intelligent_creation_20240313_models.CheckSessionRequest,
    ) -> intelligent_creation_20240313_models.CheckSessionResponse:
        """
        @summary 检查会话状态
        
        @param request: CheckSessionRequest
        @return: CheckSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_session_with_options_async(request, headers, runtime)

    def close_aicoach_task_session_with_options(
        self,
        request: intelligent_creation_20240313_models.CloseAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CloseAICoachTaskSessionResponse:
        """
        @summary 学员关闭会话
        
        @param request: CloseAICoachTaskSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseAICoachTaskSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseAICoachTaskSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/closeSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CloseAICoachTaskSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_aicoach_task_session_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CloseAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CloseAICoachTaskSessionResponse:
        """
        @summary 学员关闭会话
        
        @param request: CloseAICoachTaskSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseAICoachTaskSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseAICoachTaskSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/closeSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CloseAICoachTaskSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_aicoach_task_session(
        self,
        request: intelligent_creation_20240313_models.CloseAICoachTaskSessionRequest,
    ) -> intelligent_creation_20240313_models.CloseAICoachTaskSessionResponse:
        """
        @summary 学员关闭会话
        
        @param request: CloseAICoachTaskSessionRequest
        @return: CloseAICoachTaskSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_aicoach_task_session_with_options(request, headers, runtime)

    async def close_aicoach_task_session_async(
        self,
        request: intelligent_creation_20240313_models.CloseAICoachTaskSessionRequest,
    ) -> intelligent_creation_20240313_models.CloseAICoachTaskSessionResponse:
        """
        @summary 学员关闭会话
        
        @param request: CloseAICoachTaskSessionRequest
        @return: CloseAICoachTaskSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_aicoach_task_session_with_options_async(request, headers, runtime)

    def count_text_with_options(
        self,
        request: intelligent_creation_20240313_models.CountTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CountTextResponse:
        """
        @summary 文本数量统计
        
        @param request: CountTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.generation_source):
            query['generationSource'] = request.generation_source
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.style):
            query['style'] = request.style
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/countText',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CountTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_text_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CountTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CountTextResponse:
        """
        @summary 文本数量统计
        
        @param request: CountTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.generation_source):
            query['generationSource'] = request.generation_source
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.style):
            query['style'] = request.style
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/countText',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CountTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_text(
        self,
        request: intelligent_creation_20240313_models.CountTextRequest,
    ) -> intelligent_creation_20240313_models.CountTextResponse:
        """
        @summary 文本数量统计
        
        @param request: CountTextRequest
        @return: CountTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.count_text_with_options(request, headers, runtime)

    async def count_text_async(
        self,
        request: intelligent_creation_20240313_models.CountTextRequest,
    ) -> intelligent_creation_20240313_models.CountTextResponse:
        """
        @summary 文本数量统计
        
        @param request: CountTextRequest
        @return: CountTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.count_text_with_options_async(request, headers, runtime)

    def create_aicoach_task_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskResponse:
        """
        @summary 查询剧本列表
        
        @param request: CreateAICoachTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAICoachTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not UtilClient.is_unset(request.student_audio_url):
            body['studentAudioUrl'] = request.student_audio_url
        if not UtilClient.is_unset(request.student_id):
            body['studentId'] = request.student_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAICoachTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/createTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateAICoachTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aicoach_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskResponse:
        """
        @summary 查询剧本列表
        
        @param request: CreateAICoachTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAICoachTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not UtilClient.is_unset(request.student_audio_url):
            body['studentAudioUrl'] = request.student_audio_url
        if not UtilClient.is_unset(request.student_id):
            body['studentId'] = request.student_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAICoachTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/createTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateAICoachTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aicoach_task(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskResponse:
        """
        @summary 查询剧本列表
        
        @param request: CreateAICoachTaskRequest
        @return: CreateAICoachTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_aicoach_task_with_options(request, headers, runtime)

    async def create_aicoach_task_async(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskResponse:
        """
        @summary 查询剧本列表
        
        @param request: CreateAICoachTaskRequest
        @return: CreateAICoachTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_aicoach_task_with_options_async(request, headers, runtime)

    def create_aicoach_task_session_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskSessionResponse:
        """
        @summary 学员开启对练会话
        
        @param request: CreateAICoachTaskSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAICoachTaskSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAICoachTaskSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/startSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateAICoachTaskSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aicoach_task_session_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskSessionResponse:
        """
        @summary 学员开启对练会话
        
        @param request: CreateAICoachTaskSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAICoachTaskSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAICoachTaskSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/startSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateAICoachTaskSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aicoach_task_session(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskSessionRequest,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskSessionResponse:
        """
        @summary 学员开启对练会话
        
        @param request: CreateAICoachTaskSessionRequest
        @return: CreateAICoachTaskSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_aicoach_task_session_with_options(request, headers, runtime)

    async def create_aicoach_task_session_async(
        self,
        request: intelligent_creation_20240313_models.CreateAICoachTaskSessionRequest,
    ) -> intelligent_creation_20240313_models.CreateAICoachTaskSessionResponse:
        """
        @summary 学员开启对练会话
        
        @param request: CreateAICoachTaskSessionRequest
        @return: CreateAICoachTaskSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_aicoach_task_session_with_options_async(request, headers, runtime)

    def create_anchor_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateAnchorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateAnchorResponse:
        """
        @summary 创建照片数字人
        
        @param request: CreateAnchorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnchorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.anchor_category):
            body['anchorCategory'] = request.anchor_category
        if not UtilClient.is_unset(request.anchor_material_name):
            body['anchorMaterialName'] = request.anchor_material_name
        if not UtilClient.is_unset(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.digital_human_type):
            body['digitalHumanType'] = request.digital_human_type
        if not UtilClient.is_unset(request.gender):
            body['gender'] = request.gender
        if not UtilClient.is_unset(request.use_scene):
            body['useScene'] = request.use_scene
        if not UtilClient.is_unset(request.video_oss_key):
            body['videoOssKey'] = request.video_oss_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAnchor',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/createAnchor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateAnchorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_anchor_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateAnchorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateAnchorResponse:
        """
        @summary 创建照片数字人
        
        @param request: CreateAnchorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnchorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.anchor_category):
            body['anchorCategory'] = request.anchor_category
        if not UtilClient.is_unset(request.anchor_material_name):
            body['anchorMaterialName'] = request.anchor_material_name
        if not UtilClient.is_unset(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.digital_human_type):
            body['digitalHumanType'] = request.digital_human_type
        if not UtilClient.is_unset(request.gender):
            body['gender'] = request.gender
        if not UtilClient.is_unset(request.use_scene):
            body['useScene'] = request.use_scene
        if not UtilClient.is_unset(request.video_oss_key):
            body['videoOssKey'] = request.video_oss_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAnchor',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/createAnchor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateAnchorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_anchor(
        self,
        request: intelligent_creation_20240313_models.CreateAnchorRequest,
    ) -> intelligent_creation_20240313_models.CreateAnchorResponse:
        """
        @summary 创建照片数字人
        
        @param request: CreateAnchorRequest
        @return: CreateAnchorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_anchor_with_options(request, headers, runtime)

    async def create_anchor_async(
        self,
        request: intelligent_creation_20240313_models.CreateAnchorRequest,
    ) -> intelligent_creation_20240313_models.CreateAnchorResponse:
        """
        @summary 创建照片数字人
        
        @param request: CreateAnchorRequest
        @return: CreateAnchorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_anchor_with_options_async(request, headers, runtime)

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

    def create_individuation_project_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateIndividuationProjectResponse:
        """
        @summary 创建个性化文案项目
        
        @param request: CreateIndividuationProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndividuationProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_info):
            body['projectInfo'] = request.project_info
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.purpose):
            body['purpose'] = request.purpose
        if not UtilClient.is_unset(request.scene_id):
            body['sceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndividuationProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateIndividuationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_individuation_project_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateIndividuationProjectResponse:
        """
        @summary 创建个性化文案项目
        
        @param request: CreateIndividuationProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndividuationProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_info):
            body['projectInfo'] = request.project_info
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.purpose):
            body['purpose'] = request.purpose
        if not UtilClient.is_unset(request.scene_id):
            body['sceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndividuationProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateIndividuationProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_individuation_project(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationProjectRequest,
    ) -> intelligent_creation_20240313_models.CreateIndividuationProjectResponse:
        """
        @summary 创建个性化文案项目
        
        @param request: CreateIndividuationProjectRequest
        @return: CreateIndividuationProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_individuation_project_with_options(request, headers, runtime)

    async def create_individuation_project_async(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationProjectRequest,
    ) -> intelligent_creation_20240313_models.CreateIndividuationProjectResponse:
        """
        @summary 创建个性化文案项目
        
        @param request: CreateIndividuationProjectRequest
        @return: CreateIndividuationProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_individuation_project_with_options_async(request, headers, runtime)

    def create_individuation_text_task_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateIndividuationTextTaskResponse:
        """
        @summary 创建个性化文案任务
        
        @param request: CreateIndividuationTextTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndividuationTextTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crowd_pack):
            body['crowdPack'] = request.crowd_pack
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndividuationTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/createTextTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateIndividuationTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_individuation_text_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateIndividuationTextTaskResponse:
        """
        @summary 创建个性化文案任务
        
        @param request: CreateIndividuationTextTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndividuationTextTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crowd_pack):
            body['crowdPack'] = request.crowd_pack
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndividuationTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/createTextTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateIndividuationTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_individuation_text_task(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationTextTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateIndividuationTextTaskResponse:
        """
        @summary 创建个性化文案任务
        
        @param request: CreateIndividuationTextTaskRequest
        @return: CreateIndividuationTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_individuation_text_task_with_options(request, headers, runtime)

    async def create_individuation_text_task_async(
        self,
        request: intelligent_creation_20240313_models.CreateIndividuationTextTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateIndividuationTextTaskResponse:
        """
        @summary 创建个性化文案任务
        
        @param request: CreateIndividuationTextTaskRequest
        @return: CreateIndividuationTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_individuation_text_task_with_options_async(request, headers, runtime)

    def create_product_image_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateProductImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateProductImageResponse:
        """
        @summary 创建产品图
        
        @param request: CreateProductImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background_description):
            body['backgroundDescription'] = request.background_description
        if not UtilClient.is_unset(request.background_priority):
            body['backgroundPriority'] = request.background_priority
        if not UtilClient.is_unset(request.background_url):
            body['backgroundUrl'] = request.background_url
        if not UtilClient.is_unset(request.highlight_text):
            body['highlightText'] = request.highlight_text
        if not UtilClient.is_unset(request.image_count):
            body['imageCount'] = request.image_count
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.sub_title):
            body['subTitle'] = request.sub_title
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductImage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/products',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateProductImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_image_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateProductImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateProductImageResponse:
        """
        @summary 创建产品图
        
        @param request: CreateProductImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background_description):
            body['backgroundDescription'] = request.background_description
        if not UtilClient.is_unset(request.background_priority):
            body['backgroundPriority'] = request.background_priority
        if not UtilClient.is_unset(request.background_url):
            body['backgroundUrl'] = request.background_url
        if not UtilClient.is_unset(request.highlight_text):
            body['highlightText'] = request.highlight_text
        if not UtilClient.is_unset(request.image_count):
            body['imageCount'] = request.image_count
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.sub_title):
            body['subTitle'] = request.sub_title
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductImage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/products',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateProductImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_image(
        self,
        request: intelligent_creation_20240313_models.CreateProductImageRequest,
    ) -> intelligent_creation_20240313_models.CreateProductImageResponse:
        """
        @summary 创建产品图
        
        @param request: CreateProductImageRequest
        @return: CreateProductImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_image_with_options(request, headers, runtime)

    async def create_product_image_async(
        self,
        request: intelligent_creation_20240313_models.CreateProductImageRequest,
    ) -> intelligent_creation_20240313_models.CreateProductImageResponse:
        """
        @summary 创建产品图
        
        @param request: CreateProductImageRequest
        @return: CreateProductImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_product_image_with_options_async(request, headers, runtime)

    def create_realistic_portrait_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateRealisticPortraitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateRealisticPortraitResponse:
        """
        @summary 写实人像创作
        
        @param request: CreateRealisticPortraitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRealisticPortraitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ages):
            body['ages'] = request.ages
        if not UtilClient.is_unset(request.cloth):
            body['cloth'] = request.cloth
        if not UtilClient.is_unset(request.color):
            body['color'] = request.color
        if not UtilClient.is_unset(request.custom):
            body['custom'] = request.custom
        if not UtilClient.is_unset(request.face):
            body['face'] = request.face
        if not UtilClient.is_unset(request.figure):
            body['figure'] = request.figure
        if not UtilClient.is_unset(request.gender):
            body['gender'] = request.gender
        if not UtilClient.is_unset(request.hair_color):
            body['hairColor'] = request.hair_color
        if not UtilClient.is_unset(request.hairstyle):
            body['hairstyle'] = request.hairstyle
        if not UtilClient.is_unset(request.height):
            body['height'] = request.height
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.numbers):
            body['numbers'] = request.numbers
        if not UtilClient.is_unset(request.ratio):
            body['ratio'] = request.ratio
        if not UtilClient.is_unset(request.width):
            body['width'] = request.width
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRealisticPortrait',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/portrait/realistic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateRealisticPortraitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_realistic_portrait_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateRealisticPortraitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateRealisticPortraitResponse:
        """
        @summary 写实人像创作
        
        @param request: CreateRealisticPortraitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRealisticPortraitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ages):
            body['ages'] = request.ages
        if not UtilClient.is_unset(request.cloth):
            body['cloth'] = request.cloth
        if not UtilClient.is_unset(request.color):
            body['color'] = request.color
        if not UtilClient.is_unset(request.custom):
            body['custom'] = request.custom
        if not UtilClient.is_unset(request.face):
            body['face'] = request.face
        if not UtilClient.is_unset(request.figure):
            body['figure'] = request.figure
        if not UtilClient.is_unset(request.gender):
            body['gender'] = request.gender
        if not UtilClient.is_unset(request.hair_color):
            body['hairColor'] = request.hair_color
        if not UtilClient.is_unset(request.hairstyle):
            body['hairstyle'] = request.hairstyle
        if not UtilClient.is_unset(request.height):
            body['height'] = request.height
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.numbers):
            body['numbers'] = request.numbers
        if not UtilClient.is_unset(request.ratio):
            body['ratio'] = request.ratio
        if not UtilClient.is_unset(request.width):
            body['width'] = request.width
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRealisticPortrait',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/portrait/realistic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateRealisticPortraitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_realistic_portrait(
        self,
        request: intelligent_creation_20240313_models.CreateRealisticPortraitRequest,
    ) -> intelligent_creation_20240313_models.CreateRealisticPortraitResponse:
        """
        @summary 写实人像创作
        
        @param request: CreateRealisticPortraitRequest
        @return: CreateRealisticPortraitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_realistic_portrait_with_options(request, headers, runtime)

    async def create_realistic_portrait_async(
        self,
        request: intelligent_creation_20240313_models.CreateRealisticPortraitRequest,
    ) -> intelligent_creation_20240313_models.CreateRealisticPortraitResponse:
        """
        @summary 写实人像创作
        
        @param request: CreateRealisticPortraitRequest
        @return: CreateRealisticPortraitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_realistic_portrait_with_options_async(request, headers, runtime)

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

    def create_train_task_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateTrainTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateTrainTaskResponse:
        """
        @summary 提交声音复刻任务
        
        @param request: CreateTrainTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrainTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not UtilClient.is_unset(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        if not UtilClient.is_unset(request.use_scene):
            body['useScene'] = request.use_scene
        if not UtilClient.is_unset(request.voice_gender):
            body['voiceGender'] = request.voice_gender
        if not UtilClient.is_unset(request.voice_language):
            body['voiceLanguage'] = request.voice_language
        if not UtilClient.is_unset(request.voice_name):
            body['voiceName'] = request.voice_name
        if not UtilClient.is_unset(request.voice_path):
            body['voicePath'] = request.voice_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/train/task/createTrainTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_train_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateTrainTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateTrainTaskResponse:
        """
        @summary 提交声音复刻任务
        
        @param request: CreateTrainTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrainTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not UtilClient.is_unset(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        if not UtilClient.is_unset(request.use_scene):
            body['useScene'] = request.use_scene
        if not UtilClient.is_unset(request.voice_gender):
            body['voiceGender'] = request.voice_gender
        if not UtilClient.is_unset(request.voice_language):
            body['voiceLanguage'] = request.voice_language
        if not UtilClient.is_unset(request.voice_name):
            body['voiceName'] = request.voice_name
        if not UtilClient.is_unset(request.voice_path):
            body['voicePath'] = request.voice_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/train/task/createTrainTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_train_task(
        self,
        request: intelligent_creation_20240313_models.CreateTrainTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateTrainTaskResponse:
        """
        @summary 提交声音复刻任务
        
        @param request: CreateTrainTaskRequest
        @return: CreateTrainTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_train_task_with_options(request, headers, runtime)

    async def create_train_task_async(
        self,
        request: intelligent_creation_20240313_models.CreateTrainTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateTrainTaskResponse:
        """
        @summary 提交声音复刻任务
        
        @param request: CreateTrainTaskRequest
        @return: CreateTrainTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_train_task_with_options_async(request, headers, runtime)

    def create_video_clip_task_with_options(
        self,
        request: intelligent_creation_20240313_models.CreateVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateVideoClipTaskResponse:
        """
        @summary 提交视频切片任务
        
        @param request: CreateVideoClipTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoClipTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.oss_keys):
            body['ossKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.requirement):
            body['requirement'] = request.requirement
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoClipTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/clip/createVideoClipTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateVideoClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_clip_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.CreateVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.CreateVideoClipTaskResponse:
        """
        @summary 提交视频切片任务
        
        @param request: CreateVideoClipTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoClipTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.oss_keys):
            body['ossKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.requirement):
            body['requirement'] = request.requirement
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoClipTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/clip/createVideoClipTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.CreateVideoClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_clip_task(
        self,
        request: intelligent_creation_20240313_models.CreateVideoClipTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateVideoClipTaskResponse:
        """
        @summary 提交视频切片任务
        
        @param request: CreateVideoClipTaskRequest
        @return: CreateVideoClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_video_clip_task_with_options(request, headers, runtime)

    async def create_video_clip_task_async(
        self,
        request: intelligent_creation_20240313_models.CreateVideoClipTaskRequest,
    ) -> intelligent_creation_20240313_models.CreateVideoClipTaskResponse:
        """
        @summary 提交视频切片任务
        
        @param request: CreateVideoClipTaskRequest
        @return: CreateVideoClipTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_video_clip_task_with_options_async(request, headers, runtime)

    def delete_individuation_project_with_options(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationProjectResponse:
        """
        @summary 删除个性化文案项目
        
        @param request: DeleteIndividuationProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndividuationProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIndividuationProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/deleteProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.DeleteIndividuationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_individuation_project_with_options_async(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationProjectResponse:
        """
        @summary 删除个性化文案项目
        
        @param request: DeleteIndividuationProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndividuationProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIndividuationProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/deleteProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.DeleteIndividuationProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_individuation_project(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationProjectRequest,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationProjectResponse:
        """
        @summary 删除个性化文案项目
        
        @param request: DeleteIndividuationProjectRequest
        @return: DeleteIndividuationProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_individuation_project_with_options(request, headers, runtime)

    async def delete_individuation_project_async(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationProjectRequest,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationProjectResponse:
        """
        @summary 删除个性化文案项目
        
        @param request: DeleteIndividuationProjectRequest
        @return: DeleteIndividuationProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_individuation_project_with_options_async(request, headers, runtime)

    def delete_individuation_text_with_options(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationTextResponse:
        """
        @summary 删除个性化文案
        
        @param request: DeleteIndividuationTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndividuationTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.text_id_list):
            body['textIdList'] = request.text_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIndividuationText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/deleteText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.DeleteIndividuationTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_individuation_text_with_options_async(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationTextResponse:
        """
        @summary 删除个性化文案
        
        @param request: DeleteIndividuationTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndividuationTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.text_id_list):
            body['textIdList'] = request.text_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIndividuationText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/deleteText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.DeleteIndividuationTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_individuation_text(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationTextRequest,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationTextResponse:
        """
        @summary 删除个性化文案
        
        @param request: DeleteIndividuationTextRequest
        @return: DeleteIndividuationTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_individuation_text_with_options(request, headers, runtime)

    async def delete_individuation_text_async(
        self,
        request: intelligent_creation_20240313_models.DeleteIndividuationTextRequest,
    ) -> intelligent_creation_20240313_models.DeleteIndividuationTextResponse:
        """
        @summary 删除个性化文案
        
        @param request: DeleteIndividuationTextRequest
        @return: DeleteIndividuationTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_individuation_text_with_options_async(request, headers, runtime)

    def describe_document_with_options(
        self,
        knowledge_base_id: str,
        document_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.DescribeDocumentResponse:
        """
        @summary 查询文档信息与状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDocumentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDocument',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/knowledge-base/{OpenApiUtilClient.get_encode_param(knowledge_base_id)}/documents/{OpenApiUtilClient.get_encode_param(document_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.DescribeDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_document_with_options_async(
        self,
        knowledge_base_id: str,
        document_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.DescribeDocumentResponse:
        """
        @summary 查询文档信息与状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDocumentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDocument',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/knowledge-base/{OpenApiUtilClient.get_encode_param(knowledge_base_id)}/documents/{OpenApiUtilClient.get_encode_param(document_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.DescribeDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_document(
        self,
        knowledge_base_id: str,
        document_id: str,
    ) -> intelligent_creation_20240313_models.DescribeDocumentResponse:
        """
        @summary 查询文档信息与状态
        
        @return: DescribeDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_document_with_options(knowledge_base_id, document_id, headers, runtime)

    async def describe_document_async(
        self,
        knowledge_base_id: str,
        document_id: str,
    ) -> intelligent_creation_20240313_models.DescribeDocumentResponse:
        """
        @summary 查询文档信息与状态
        
        @return: DescribeDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_document_with_options_async(knowledge_base_id, document_id, headers, runtime)

    def finish_aicoach_task_session_with_options(
        self,
        request: intelligent_creation_20240313_models.FinishAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.FinishAICoachTaskSessionResponse:
        """
        @summary 学员完成会话
        
        @param request: FinishAICoachTaskSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FinishAICoachTaskSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishAICoachTaskSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/finishSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.FinishAICoachTaskSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_aicoach_task_session_with_options_async(
        self,
        request: intelligent_creation_20240313_models.FinishAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.FinishAICoachTaskSessionResponse:
        """
        @summary 学员完成会话
        
        @param request: FinishAICoachTaskSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FinishAICoachTaskSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishAICoachTaskSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/finishSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.FinishAICoachTaskSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_aicoach_task_session(
        self,
        request: intelligent_creation_20240313_models.FinishAICoachTaskSessionRequest,
    ) -> intelligent_creation_20240313_models.FinishAICoachTaskSessionResponse:
        """
        @summary 学员完成会话
        
        @param request: FinishAICoachTaskSessionRequest
        @return: FinishAICoachTaskSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_aicoach_task_session_with_options(request, headers, runtime)

    async def finish_aicoach_task_session_async(
        self,
        request: intelligent_creation_20240313_models.FinishAICoachTaskSessionRequest,
    ) -> intelligent_creation_20240313_models.FinishAICoachTaskSessionResponse:
        """
        @summary 学员完成会话
        
        @param request: FinishAICoachTaskSessionRequest
        @return: FinishAICoachTaskSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.finish_aicoach_task_session_with_options_async(request, headers, runtime)

    def get_aicoach_assessment_point_with_options(
        self,
        request: intelligent_creation_20240313_models.GetAICoachAssessmentPointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachAssessmentPointResponse:
        """
        @summary 获取考核点详情
        
        @param request: GetAICoachAssessmentPointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachAssessmentPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.point_id):
            query['pointId'] = request.point_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachAssessmentPoint',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/getAssessmentPoint',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachAssessmentPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_assessment_point_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachAssessmentPointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachAssessmentPointResponse:
        """
        @summary 获取考核点详情
        
        @param request: GetAICoachAssessmentPointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachAssessmentPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.point_id):
            query['pointId'] = request.point_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachAssessmentPoint',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/getAssessmentPoint',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachAssessmentPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_assessment_point(
        self,
        request: intelligent_creation_20240313_models.GetAICoachAssessmentPointRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachAssessmentPointResponse:
        """
        @summary 获取考核点详情
        
        @param request: GetAICoachAssessmentPointRequest
        @return: GetAICoachAssessmentPointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aicoach_assessment_point_with_options(request, headers, runtime)

    async def get_aicoach_assessment_point_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachAssessmentPointRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachAssessmentPointResponse:
        """
        @summary 获取考核点详情
        
        @param request: GetAICoachAssessmentPointRequest
        @return: GetAICoachAssessmentPointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aicoach_assessment_point_with_options_async(request, headers, runtime)

    def get_aicoach_cheat_detection_with_options(
        self,
        request: intelligent_creation_20240313_models.GetAICoachCheatDetectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachCheatDetectionResponse:
        """
        @summary 查询作弊检测详情
        
        @param request: GetAICoachCheatDetectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachCheatDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachCheatDetection',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/getCheatDetection',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachCheatDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_cheat_detection_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachCheatDetectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachCheatDetectionResponse:
        """
        @summary 查询作弊检测详情
        
        @param request: GetAICoachCheatDetectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachCheatDetectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachCheatDetection',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/getCheatDetection',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachCheatDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_cheat_detection(
        self,
        request: intelligent_creation_20240313_models.GetAICoachCheatDetectionRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachCheatDetectionResponse:
        """
        @summary 查询作弊检测详情
        
        @param request: GetAICoachCheatDetectionRequest
        @return: GetAICoachCheatDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aicoach_cheat_detection_with_options(request, headers, runtime)

    async def get_aicoach_cheat_detection_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachCheatDetectionRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachCheatDetectionResponse:
        """
        @summary 查询作弊检测详情
        
        @param request: GetAICoachCheatDetectionRequest
        @return: GetAICoachCheatDetectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aicoach_cheat_detection_with_options_async(request, headers, runtime)

    def get_aicoach_script_with_options(
        self,
        request: intelligent_creation_20240313_models.GetAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachScriptResponse:
        """
        @summary 查询剧本详情
        
        @param request: GetAICoachScriptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.script_record_id):
            query['scriptRecordId'] = request.script_record_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachScript',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/getScript',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_script_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachScriptResponse:
        """
        @summary 查询剧本详情
        
        @param request: GetAICoachScriptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.script_record_id):
            query['scriptRecordId'] = request.script_record_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachScript',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/getScript',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_script(
        self,
        request: intelligent_creation_20240313_models.GetAICoachScriptRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachScriptResponse:
        """
        @summary 查询剧本详情
        
        @param request: GetAICoachScriptRequest
        @return: GetAICoachScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aicoach_script_with_options(request, headers, runtime)

    async def get_aicoach_script_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachScriptRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachScriptResponse:
        """
        @summary 查询剧本详情
        
        @param request: GetAICoachScriptRequest
        @return: GetAICoachScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aicoach_script_with_options_async(request, headers, runtime)

    def get_aicoach_task_session_history_with_options(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryResponse:
        """
        @summary 学员查询会话历史
        
        @param request: GetAICoachTaskSessionHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachTaskSessionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachTaskSessionHistory',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/querySessionHistory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_task_session_history_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryResponse:
        """
        @summary 学员查询会话历史
        
        @param request: GetAICoachTaskSessionHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachTaskSessionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachTaskSessionHistory',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/querySessionHistory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_task_session_history(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryResponse:
        """
        @summary 学员查询会话历史
        
        @param request: GetAICoachTaskSessionHistoryRequest
        @return: GetAICoachTaskSessionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aicoach_task_session_history_with_options(request, headers, runtime)

    async def get_aicoach_task_session_history_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionHistoryResponse:
        """
        @summary 学员查询会话历史
        
        @param request: GetAICoachTaskSessionHistoryRequest
        @return: GetAICoachTaskSessionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aicoach_task_session_history_with_options_async(request, headers, runtime)

    def get_aicoach_task_session_report_with_options(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionReportResponse:
        """
        @summary 学员查询会话评测报告
        
        @param request: GetAICoachTaskSessionReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachTaskSessionReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachTaskSessionReport',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/queryTaskSessionReport',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachTaskSessionReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_task_session_report_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionReportResponse:
        """
        @summary 学员查询会话评测报告
        
        @param request: GetAICoachTaskSessionReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAICoachTaskSessionReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAICoachTaskSessionReport',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/queryTaskSessionReport',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetAICoachTaskSessionReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_task_session_report(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionReportRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionReportResponse:
        """
        @summary 学员查询会话评测报告
        
        @param request: GetAICoachTaskSessionReportRequest
        @return: GetAICoachTaskSessionReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aicoach_task_session_report_with_options(request, headers, runtime)

    async def get_aicoach_task_session_report_async(
        self,
        request: intelligent_creation_20240313_models.GetAICoachTaskSessionReportRequest,
    ) -> intelligent_creation_20240313_models.GetAICoachTaskSessionReportResponse:
        """
        @summary 学员查询会话评测报告
        
        @param request: GetAICoachTaskSessionReportRequest
        @return: GetAICoachTaskSessionReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aicoach_task_session_report_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.upload_type):
            query['uploadType'] = request.upload_type
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
        if not UtilClient.is_unset(request.upload_type):
            query['uploadType'] = request.upload_type
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

    def get_project_task_with_options(
        self,
        request: intelligent_creation_20240313_models.GetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetProjectTaskResponse:
        """
        @summary 获取数据人合成信息
        
        @param request: GetProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/getProjectTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetProjectTaskResponse:
        """
        @summary 获取数据人合成信息
        
        @param request: GetProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/getProjectTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_task(
        self,
        request: intelligent_creation_20240313_models.GetProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.GetProjectTaskResponse:
        """
        @summary 获取数据人合成信息
        
        @param request: GetProjectTaskRequest
        @return: GetProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_task_with_options(request, headers, runtime)

    async def get_project_task_async(
        self,
        request: intelligent_creation_20240313_models.GetProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.GetProjectTaskResponse:
        """
        @summary 获取数据人合成信息
        
        @param request: GetProjectTaskRequest
        @return: GetProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_task_with_options_async(request, headers, runtime)

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

    def get_text_template_with_options(
        self,
        request: intelligent_creation_20240313_models.GetTextTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetTextTemplateResponse:
        """
        @summary 查询表单配置
        
        @param request: GetTextTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTextTemplate',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/commands/getTextTemplate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetTextTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_template_with_options_async(
        self,
        request: intelligent_creation_20240313_models.GetTextTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.GetTextTemplateResponse:
        """
        @summary 查询表单配置
        
        @param request: GetTextTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTextTemplate',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts/commands/getTextTemplate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.GetTextTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text_template(
        self,
        request: intelligent_creation_20240313_models.GetTextTemplateRequest,
    ) -> intelligent_creation_20240313_models.GetTextTemplateResponse:
        """
        @summary 查询表单配置
        
        @param request: GetTextTemplateRequest
        @return: GetTextTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_text_template_with_options(request, headers, runtime)

    async def get_text_template_async(
        self,
        request: intelligent_creation_20240313_models.GetTextTemplateRequest,
    ) -> intelligent_creation_20240313_models.GetTextTemplateResponse:
        """
        @summary 查询表单配置
        
        @param request: GetTextTemplateRequest
        @return: GetTextTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_text_template_with_options_async(request, headers, runtime)

    def interact_text_with_options(
        self,
        request: intelligent_creation_20240313_models.InteractTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.InteractTextResponse:
        """
        @summary 营销文案互动问答
        
        @param request: InteractTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InteractTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InteractText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/stream/interactText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.InteractTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def interact_text_with_options_async(
        self,
        request: intelligent_creation_20240313_models.InteractTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.InteractTextResponse:
        """
        @summary 营销文案互动问答
        
        @param request: InteractTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InteractTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InteractText',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/stream/interactText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.InteractTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def interact_text(
        self,
        request: intelligent_creation_20240313_models.InteractTextRequest,
    ) -> intelligent_creation_20240313_models.InteractTextResponse:
        """
        @summary 营销文案互动问答
        
        @param request: InteractTextRequest
        @return: InteractTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interact_text_with_options(request, headers, runtime)

    async def interact_text_async(
        self,
        request: intelligent_creation_20240313_models.InteractTextRequest,
    ) -> intelligent_creation_20240313_models.InteractTextResponse:
        """
        @summary 营销文案互动问答
        
        @param request: InteractTextRequest
        @return: InteractTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.interact_text_with_options_async(request, headers, runtime)

    def list_aicoach_script_page_with_options(
        self,
        request: intelligent_creation_20240313_models.ListAICoachScriptPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAICoachScriptPageResponse:
        """
        @summary 查询剧本列表
        
        @param request: ListAICoachScriptPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAICoachScriptPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAICoachScriptPage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/pageScript',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAICoachScriptPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aicoach_script_page_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListAICoachScriptPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAICoachScriptPageResponse:
        """
        @summary 查询剧本列表
        
        @param request: ListAICoachScriptPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAICoachScriptPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAICoachScriptPage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/pageScript',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAICoachScriptPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aicoach_script_page(
        self,
        request: intelligent_creation_20240313_models.ListAICoachScriptPageRequest,
    ) -> intelligent_creation_20240313_models.ListAICoachScriptPageResponse:
        """
        @summary 查询剧本列表
        
        @param request: ListAICoachScriptPageRequest
        @return: ListAICoachScriptPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aicoach_script_page_with_options(request, headers, runtime)

    async def list_aicoach_script_page_async(
        self,
        request: intelligent_creation_20240313_models.ListAICoachScriptPageRequest,
    ) -> intelligent_creation_20240313_models.ListAICoachScriptPageResponse:
        """
        @summary 查询剧本列表
        
        @param request: ListAICoachScriptPageRequest
        @return: ListAICoachScriptPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_aicoach_script_page_with_options_async(request, headers, runtime)

    def list_aicoach_task_page_with_options(
        self,
        request: intelligent_creation_20240313_models.ListAICoachTaskPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAICoachTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAICoachTaskPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAICoachTaskPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.student_id):
            query['studentId'] = request.student_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAICoachTaskPage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/listTaskPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAICoachTaskPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aicoach_task_page_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListAICoachTaskPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAICoachTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAICoachTaskPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAICoachTaskPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.student_id):
            query['studentId'] = request.student_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAICoachTaskPage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/aicoach/listTaskPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAICoachTaskPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aicoach_task_page(
        self,
        request: intelligent_creation_20240313_models.ListAICoachTaskPageRequest,
    ) -> intelligent_creation_20240313_models.ListAICoachTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAICoachTaskPageRequest
        @return: ListAICoachTaskPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aicoach_task_page_with_options(request, headers, runtime)

    async def list_aicoach_task_page_async(
        self,
        request: intelligent_creation_20240313_models.ListAICoachTaskPageRequest,
    ) -> intelligent_creation_20240313_models.ListAICoachTaskPageResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAICoachTaskPageRequest
        @return: ListAICoachTaskPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_aicoach_task_page_with_options_async(request, headers, runtime)

    def list_agents_with_options(
        self,
        request: intelligent_creation_20240313_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAgentsResponse:
        """
        @summary 分页查询智能体
        
        @param request: ListAgentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_scene):
            query['agentScene'] = request.agent_scene
        if not UtilClient.is_unset(request.owner):
            query['owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgents',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/agent/listAgents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAgentsResponse:
        """
        @summary 分页查询智能体
        
        @param request: ListAgentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.agent_scene):
            query['agentScene'] = request.agent_scene
        if not UtilClient.is_unset(request.owner):
            query['owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgents',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/agent/listAgents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: intelligent_creation_20240313_models.ListAgentsRequest,
    ) -> intelligent_creation_20240313_models.ListAgentsResponse:
        """
        @summary 分页查询智能体
        
        @param request: ListAgentsRequest
        @return: ListAgentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agents_with_options(request, headers, runtime)

    async def list_agents_async(
        self,
        request: intelligent_creation_20240313_models.ListAgentsRequest,
    ) -> intelligent_creation_20240313_models.ListAgentsResponse:
        """
        @summary 分页查询智能体
        
        @param request: ListAgentsRequest
        @return: ListAgentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agents_with_options_async(request, headers, runtime)

    def list_anchor_with_options(
        self,
        request: intelligent_creation_20240313_models.ListAnchorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAnchorResponse:
        """
        @summary 获取数字人模特列表
        
        @param request: ListAnchorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnchorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_category):
            query['anchorCategory'] = request.anchor_category
        if not UtilClient.is_unset(request.anchor_id):
            query['anchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_type):
            query['anchorType'] = request.anchor_type
        if not UtilClient.is_unset(request.cover_rate):
            query['coverRate'] = request.cover_rate
        if not UtilClient.is_unset(request.digital_human_type):
            query['digitalHumanType'] = request.digital_human_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.use_scene):
            query['useScene'] = request.use_scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnchor',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/listAnchor',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAnchorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_anchor_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListAnchorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAnchorResponse:
        """
        @summary 获取数字人模特列表
        
        @param request: ListAnchorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnchorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_category):
            query['anchorCategory'] = request.anchor_category
        if not UtilClient.is_unset(request.anchor_id):
            query['anchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_type):
            query['anchorType'] = request.anchor_type
        if not UtilClient.is_unset(request.cover_rate):
            query['coverRate'] = request.cover_rate
        if not UtilClient.is_unset(request.digital_human_type):
            query['digitalHumanType'] = request.digital_human_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.use_scene):
            query['useScene'] = request.use_scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnchor',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/listAnchor',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAnchorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_anchor(
        self,
        request: intelligent_creation_20240313_models.ListAnchorRequest,
    ) -> intelligent_creation_20240313_models.ListAnchorResponse:
        """
        @summary 获取数字人模特列表
        
        @param request: ListAnchorRequest
        @return: ListAnchorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_anchor_with_options(request, headers, runtime)

    async def list_anchor_async(
        self,
        request: intelligent_creation_20240313_models.ListAnchorRequest,
    ) -> intelligent_creation_20240313_models.ListAnchorResponse:
        """
        @summary 获取数字人模特列表
        
        @param request: ListAnchorRequest
        @return: ListAnchorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_anchor_with_options_async(request, headers, runtime)

    def list_avatar_project_with_options(
        self,
        tmp_req: intelligent_creation_20240313_models.ListAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAvatarProjectResponse:
        """
        @summary 批量查询数字人项目启动结果
        
        @param tmp_req: ListAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvatarProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.ListAvatarProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_id_list):
            request.project_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_id_list, 'projectIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.project_id_list_shrink):
            query['projectIdList'] = request.project_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/listAvatarProject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_avatar_project_with_options_async(
        self,
        tmp_req: intelligent_creation_20240313_models.ListAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListAvatarProjectResponse:
        """
        @summary 批量查询数字人项目启动结果
        
        @param tmp_req: ListAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvatarProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.ListAvatarProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_id_list):
            request.project_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_id_list, 'projectIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.project_id_list_shrink):
            query['projectIdList'] = request.project_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/listAvatarProject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_avatar_project(
        self,
        request: intelligent_creation_20240313_models.ListAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.ListAvatarProjectResponse:
        """
        @summary 批量查询数字人项目启动结果
        
        @param request: ListAvatarProjectRequest
        @return: ListAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_avatar_project_with_options(request, headers, runtime)

    async def list_avatar_project_async(
        self,
        request: intelligent_creation_20240313_models.ListAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.ListAvatarProjectResponse:
        """
        @summary 批量查询数字人项目启动结果
        
        @param request: ListAvatarProjectRequest
        @return: ListAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_avatar_project_with_options_async(request, headers, runtime)

    def list_knowledge_base_with_options(
        self,
        request: intelligent_creation_20240313_models.ListKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListKnowledgeBaseResponse:
        """
        @summary 查询知识库
        
        @param request: ListKnowledgeBaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKnowledgeBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.knowledge_base_id):
            query['knowledgeBaseId'] = request.knowledge_base_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKnowledgeBase',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/knowledge-base',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_base_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListKnowledgeBaseResponse:
        """
        @summary 查询知识库
        
        @param request: ListKnowledgeBaseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKnowledgeBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.knowledge_base_id):
            query['knowledgeBaseId'] = request.knowledge_base_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKnowledgeBase',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/knowledge-base',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_base(
        self,
        request: intelligent_creation_20240313_models.ListKnowledgeBaseRequest,
    ) -> intelligent_creation_20240313_models.ListKnowledgeBaseResponse:
        """
        @summary 查询知识库
        
        @param request: ListKnowledgeBaseRequest
        @return: ListKnowledgeBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_knowledge_base_with_options(request, headers, runtime)

    async def list_knowledge_base_async(
        self,
        request: intelligent_creation_20240313_models.ListKnowledgeBaseRequest,
    ) -> intelligent_creation_20240313_models.ListKnowledgeBaseResponse:
        """
        @summary 查询知识库
        
        @param request: ListKnowledgeBaseRequest
        @return: ListKnowledgeBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_knowledge_base_with_options_async(request, headers, runtime)

    def list_text_themes_with_options(
        self,
        request: intelligent_creation_20240313_models.ListTextThemesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @param request: ListTextThemesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextThemesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        request: intelligent_creation_20240313_models.ListTextThemesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @param request: ListTextThemesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextThemesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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

    def list_text_themes(
        self,
        request: intelligent_creation_20240313_models.ListTextThemesRequest,
    ) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @param request: ListTextThemesRequest
        @return: ListTextThemesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_text_themes_with_options(request, headers, runtime)

    async def list_text_themes_async(
        self,
        request: intelligent_creation_20240313_models.ListTextThemesRequest,
    ) -> intelligent_creation_20240313_models.ListTextThemesResponse:
        """
        @summary 查询文案主题列表
        
        @param request: ListTextThemesRequest
        @return: ListTextThemesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_text_themes_with_options_async(request, headers, runtime)

    def list_texts_with_options(
        self,
        request: intelligent_creation_20240313_models.ListTextsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListTextsResponse:
        """
        @summary 列举文案
        
        @param request: ListTextsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.generation_source):
            query['generationSource'] = request.generation_source
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.text_style_type):
            query['textStyleType'] = request.text_style_type
        if not UtilClient.is_unset(request.text_theme):
            query['textTheme'] = request.text_theme
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTexts',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListTextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_texts_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListTextsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListTextsResponse:
        """
        @summary 列举文案
        
        @param request: ListTextsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.generation_source):
            query['generationSource'] = request.generation_source
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not UtilClient.is_unset(request.text_style_type):
            query['textStyleType'] = request.text_style_type
        if not UtilClient.is_unset(request.text_theme):
            query['textTheme'] = request.text_theme
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTexts',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/texts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListTextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_texts(
        self,
        request: intelligent_creation_20240313_models.ListTextsRequest,
    ) -> intelligent_creation_20240313_models.ListTextsResponse:
        """
        @summary 列举文案
        
        @param request: ListTextsRequest
        @return: ListTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_texts_with_options(request, headers, runtime)

    async def list_texts_async(
        self,
        request: intelligent_creation_20240313_models.ListTextsRequest,
    ) -> intelligent_creation_20240313_models.ListTextsResponse:
        """
        @summary 列举文案
        
        @param request: ListTextsRequest
        @return: ListTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_texts_with_options_async(request, headers, runtime)

    def list_voice_models_with_options(
        self,
        request: intelligent_creation_20240313_models.ListVoiceModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListVoiceModelsResponse:
        """
        @summary 获取声音模版列表
        
        @param request: ListVoiceModelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVoiceModelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.use_scene):
            query['useScene'] = request.use_scene
        if not UtilClient.is_unset(request.voice_language):
            query['voiceLanguage'] = request.voice_language
        if not UtilClient.is_unset(request.voice_type):
            query['voiceType'] = request.voice_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceModels',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/voiceOpen/listVoiceModels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListVoiceModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_models_with_options_async(
        self,
        request: intelligent_creation_20240313_models.ListVoiceModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.ListVoiceModelsResponse:
        """
        @summary 获取声音模版列表
        
        @param request: ListVoiceModelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVoiceModelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.use_scene):
            query['useScene'] = request.use_scene
        if not UtilClient.is_unset(request.voice_language):
            query['voiceLanguage'] = request.voice_language
        if not UtilClient.is_unset(request.voice_type):
            query['voiceType'] = request.voice_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVoiceModels',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/voiceOpen/listVoiceModels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.ListVoiceModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_models(
        self,
        request: intelligent_creation_20240313_models.ListVoiceModelsRequest,
    ) -> intelligent_creation_20240313_models.ListVoiceModelsResponse:
        """
        @summary 获取声音模版列表
        
        @param request: ListVoiceModelsRequest
        @return: ListVoiceModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_voice_models_with_options(request, headers, runtime)

    async def list_voice_models_async(
        self,
        request: intelligent_creation_20240313_models.ListVoiceModelsRequest,
    ) -> intelligent_creation_20240313_models.ListVoiceModelsResponse:
        """
        @summary 获取声音模版列表
        
        @param request: ListVoiceModelsRequest
        @return: ListVoiceModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_voice_models_with_options_async(request, headers, runtime)

    def operate_avatar_project_with_options(
        self,
        request: intelligent_creation_20240313_models.OperateAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.OperateAvatarProjectResponse:
        """
        @summary 操作实时数字人项目
        
        @param request: OperateAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAvatarProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operate_type):
            body['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.res_channel_number):
            body['resChannelNumber'] = request.res_channel_number
        if not UtilClient.is_unset(request.res_type):
            body['resType'] = request.res_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/operateProjectAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.OperateAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_avatar_project_with_options_async(
        self,
        request: intelligent_creation_20240313_models.OperateAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.OperateAvatarProjectResponse:
        """
        @summary 操作实时数字人项目
        
        @param request: OperateAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAvatarProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operate_type):
            body['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.res_channel_number):
            body['resChannelNumber'] = request.res_channel_number
        if not UtilClient.is_unset(request.res_type):
            body['resType'] = request.res_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/operateProjectAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.OperateAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_avatar_project(
        self,
        request: intelligent_creation_20240313_models.OperateAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.OperateAvatarProjectResponse:
        """
        @summary 操作实时数字人项目
        
        @param request: OperateAvatarProjectRequest
        @return: OperateAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.operate_avatar_project_with_options(request, headers, runtime)

    async def operate_avatar_project_async(
        self,
        request: intelligent_creation_20240313_models.OperateAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.OperateAvatarProjectResponse:
        """
        @summary 操作实时数字人项目
        
        @param request: OperateAvatarProjectRequest
        @return: OperateAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.operate_avatar_project_with_options_async(request, headers, runtime)

    def query_avatar_project_with_options(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryAvatarProjectResponse:
        """
        @summary 查询数字人项目信息
        
        @param request: QueryAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAvatarProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/queryAvatarProject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_avatar_project_with_options_async(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryAvatarProjectResponse:
        """
        @summary 查询数字人项目信息
        
        @param request: QueryAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAvatarProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/queryAvatarProject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_avatar_project(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.QueryAvatarProjectResponse:
        """
        @summary 查询数字人项目信息
        
        @param request: QueryAvatarProjectRequest
        @return: QueryAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_avatar_project_with_options(request, headers, runtime)

    async def query_avatar_project_async(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.QueryAvatarProjectResponse:
        """
        @summary 查询数字人项目信息
        
        @param request: QueryAvatarProjectRequest
        @return: QueryAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_avatar_project_with_options_async(request, headers, runtime)

    def query_avatar_resource_with_options(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryAvatarResourceResponse:
        """
        @summary 查找资源
        
        @param request: QueryAvatarResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAvatarResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarResource',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/queryResource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryAvatarResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_avatar_resource_with_options_async(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryAvatarResourceResponse:
        """
        @summary 查找资源
        
        @param request: QueryAvatarResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAvatarResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarResource',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/queryResource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryAvatarResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_avatar_resource(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarResourceRequest,
    ) -> intelligent_creation_20240313_models.QueryAvatarResourceResponse:
        """
        @summary 查找资源
        
        @param request: QueryAvatarResourceRequest
        @return: QueryAvatarResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_avatar_resource_with_options(request, headers, runtime)

    async def query_avatar_resource_async(
        self,
        request: intelligent_creation_20240313_models.QueryAvatarResourceRequest,
    ) -> intelligent_creation_20240313_models.QueryAvatarResourceResponse:
        """
        @summary 查找资源
        
        @param request: QueryAvatarResourceRequest
        @return: QueryAvatarResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_avatar_resource_with_options_async(request, headers, runtime)

    def query_image_to_video_task_with_options(
        self,
        request: intelligent_creation_20240313_models.QueryImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryImageToVideoTaskResponse:
        """
        @summary 查询图片转视频任务
        
        @param request: QueryImageToVideoTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryImageToVideoTaskResponse
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
            action='QueryImageToVideoTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryImageToVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_image_to_video_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.QueryImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryImageToVideoTaskResponse:
        """
        @summary 查询图片转视频任务
        
        @param request: QueryImageToVideoTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryImageToVideoTaskResponse
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
            action='QueryImageToVideoTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryImageToVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_image_to_video_task(
        self,
        request: intelligent_creation_20240313_models.QueryImageToVideoTaskRequest,
    ) -> intelligent_creation_20240313_models.QueryImageToVideoTaskResponse:
        """
        @summary 查询图片转视频任务
        
        @param request: QueryImageToVideoTaskRequest
        @return: QueryImageToVideoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_image_to_video_task_with_options(request, headers, runtime)

    async def query_image_to_video_task_async(
        self,
        request: intelligent_creation_20240313_models.QueryImageToVideoTaskRequest,
    ) -> intelligent_creation_20240313_models.QueryImageToVideoTaskResponse:
        """
        @summary 查询图片转视频任务
        
        @param request: QueryImageToVideoTaskRequest
        @return: QueryImageToVideoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_image_to_video_task_with_options_async(request, headers, runtime)

    def query_individuation_text_task_with_options(
        self,
        request: intelligent_creation_20240313_models.QueryIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryIndividuationTextTaskResponse:
        """
        @summary 查询个性化文案任务
        
        @param request: QueryIndividuationTextTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndividuationTextTaskResponse
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
            action='QueryIndividuationTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/queryTextTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryIndividuationTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_individuation_text_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.QueryIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryIndividuationTextTaskResponse:
        """
        @summary 查询个性化文案任务
        
        @param request: QueryIndividuationTextTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndividuationTextTaskResponse
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
            action='QueryIndividuationTextTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/individuationText/queryTextTask',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryIndividuationTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_individuation_text_task(
        self,
        request: intelligent_creation_20240313_models.QueryIndividuationTextTaskRequest,
    ) -> intelligent_creation_20240313_models.QueryIndividuationTextTaskResponse:
        """
        @summary 查询个性化文案任务
        
        @param request: QueryIndividuationTextTaskRequest
        @return: QueryIndividuationTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_individuation_text_task_with_options(request, headers, runtime)

    async def query_individuation_text_task_async(
        self,
        request: intelligent_creation_20240313_models.QueryIndividuationTextTaskRequest,
    ) -> intelligent_creation_20240313_models.QueryIndividuationTextTaskResponse:
        """
        @summary 查询个性化文案任务
        
        @param request: QueryIndividuationTextTaskRequest
        @return: QueryIndividuationTextTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_individuation_text_task_with_options_async(request, headers, runtime)

    def query_session_info_with_options(
        self,
        tmp_req: intelligent_creation_20240313_models.QuerySessionInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QuerySessionInfoResponse:
        """
        @summary 查询会话信息
        
        @param tmp_req: QuerySessionInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.QuerySessionInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionInfo',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/querySessionInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QuerySessionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_info_with_options_async(
        self,
        tmp_req: intelligent_creation_20240313_models.QuerySessionInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QuerySessionInfoResponse:
        """
        @summary 查询会话信息
        
        @param tmp_req: QuerySessionInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySessionInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240313_models.QuerySessionInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionInfo',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/querySessionInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QuerySessionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_info(
        self,
        request: intelligent_creation_20240313_models.QuerySessionInfoRequest,
    ) -> intelligent_creation_20240313_models.QuerySessionInfoResponse:
        """
        @summary 查询会话信息
        
        @param request: QuerySessionInfoRequest
        @return: QuerySessionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_session_info_with_options(request, headers, runtime)

    async def query_session_info_async(
        self,
        request: intelligent_creation_20240313_models.QuerySessionInfoRequest,
    ) -> intelligent_creation_20240313_models.QuerySessionInfoResponse:
        """
        @summary 查询会话信息
        
        @param request: QuerySessionInfoRequest
        @return: QuerySessionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_session_info_with_options_async(request, headers, runtime)

    def query_text_stream_with_options(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryTextStreamResponse:
        """
        @summary 流式输出文案
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTextStreamResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryTextStream',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/stream/queryTextStream/{OpenApiUtilClient.get_encode_param(text_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryTextStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_text_stream_with_options_async(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.QueryTextStreamResponse:
        """
        @summary 流式输出文案
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTextStreamResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryTextStream',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/stream/queryTextStream/{OpenApiUtilClient.get_encode_param(text_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.QueryTextStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_text_stream(
        self,
        text_id: str,
    ) -> intelligent_creation_20240313_models.QueryTextStreamResponse:
        """
        @summary 流式输出文案
        
        @return: QueryTextStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_text_stream_with_options(text_id, headers, runtime)

    async def query_text_stream_async(
        self,
        text_id: str,
    ) -> intelligent_creation_20240313_models.QueryTextStreamResponse:
        """
        @summary 流式输出文案
        
        @return: QueryTextStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_text_stream_with_options_async(text_id, headers, runtime)

    def save_avatar_project_with_options(
        self,
        request: intelligent_creation_20240313_models.SaveAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SaveAvatarProjectResponse:
        """
        @summary 保存实时数字人项目
        
        @param request: SaveAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAvatarProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.bit_rate):
            body['bitRate'] = request.bit_rate
        if not UtilClient.is_unset(request.frame_rate):
            body['frameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.frames):
            body['frames'] = request.frames
        if not UtilClient.is_unset(request.operate_type):
            body['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.resolution):
            body['resolution'] = request.resolution
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.script_model_tag):
            body['scriptModelTag'] = request.script_model_tag
        if not UtilClient.is_unset(request.synchronized_display):
            body['synchronizedDisplay'] = request.synchronized_display
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/saveAvatarProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SaveAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_avatar_project_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SaveAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SaveAvatarProjectResponse:
        """
        @summary 保存实时数字人项目
        
        @param request: SaveAvatarProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveAvatarProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agentId'] = request.agent_id
        if not UtilClient.is_unset(request.bit_rate):
            body['bitRate'] = request.bit_rate
        if not UtilClient.is_unset(request.frame_rate):
            body['frameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.frames):
            body['frames'] = request.frames
        if not UtilClient.is_unset(request.operate_type):
            body['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not UtilClient.is_unset(request.resolution):
            body['resolution'] = request.resolution
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.script_model_tag):
            body['scriptModelTag'] = request.script_model_tag
        if not UtilClient.is_unset(request.synchronized_display):
            body['synchronizedDisplay'] = request.synchronized_display
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAvatarProject',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/saveAvatarProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SaveAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_avatar_project(
        self,
        request: intelligent_creation_20240313_models.SaveAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.SaveAvatarProjectResponse:
        """
        @summary 保存实时数字人项目
        
        @param request: SaveAvatarProjectRequest
        @return: SaveAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_avatar_project_with_options(request, headers, runtime)

    async def save_avatar_project_async(
        self,
        request: intelligent_creation_20240313_models.SaveAvatarProjectRequest,
    ) -> intelligent_creation_20240313_models.SaveAvatarProjectResponse:
        """
        @summary 保存实时数字人项目
        
        @param request: SaveAvatarProjectRequest
        @return: SaveAvatarProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_avatar_project_with_options_async(request, headers, runtime)

    def select_image_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SelectImageTaskResponse:
        """
        @summary 查询图片任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectImageTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SelectImageTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/portrait/select/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SelectImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_image_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SelectImageTaskResponse:
        """
        @summary 查询图片任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectImageTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SelectImageTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/portrait/select/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SelectImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_image_task(
        self,
        task_id: str,
    ) -> intelligent_creation_20240313_models.SelectImageTaskResponse:
        """
        @summary 查询图片任务
        
        @return: SelectImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_image_task_with_options(task_id, headers, runtime)

    async def select_image_task_async(
        self,
        task_id: str,
    ) -> intelligent_creation_20240313_models.SelectImageTaskResponse:
        """
        @summary 查询图片任务
        
        @return: SelectImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_image_task_with_options_async(task_id, headers, runtime)

    def select_resource_with_options(
        self,
        request: intelligent_creation_20240313_models.SelectResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SelectResourceResponse:
        """
        @summary 查询离线数字人剩余资源
        
        @param request: SelectResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectResource',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/commands/overview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SelectResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_resource_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SelectResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SelectResourceResponse:
        """
        @summary 查询离线数字人剩余资源
        
        @param request: SelectResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectResource',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/commands/overview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SelectResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_resource(
        self,
        request: intelligent_creation_20240313_models.SelectResourceRequest,
    ) -> intelligent_creation_20240313_models.SelectResourceResponse:
        """
        @summary 查询离线数字人剩余资源
        
        @param request: SelectResourceRequest
        @return: SelectResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_resource_with_options(request, headers, runtime)

    async def select_resource_async(
        self,
        request: intelligent_creation_20240313_models.SelectResourceRequest,
    ) -> intelligent_creation_20240313_models.SelectResourceResponse:
        """
        @summary 查询离线数字人剩余资源
        
        @param request: SelectResourceRequest
        @return: SelectResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_resource_with_options_async(request, headers, runtime)

    def send_sdk_message_with_options(
        self,
        request: intelligent_creation_20240313_models.SendSdkMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SendSdkMessageResponse:
        """
        @summary 发送sdk消息
        
        @param request: SendSdkMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSdkMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.header):
            body['header'] = request.header
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.operation_name):
            body['operationName'] = request.operation_name
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSdkMessage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/sdk/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SendSdkMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sdk_message_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SendSdkMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SendSdkMessageResponse:
        """
        @summary 发送sdk消息
        
        @param request: SendSdkMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSdkMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.header):
            body['header'] = request.header
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.operation_name):
            body['operationName'] = request.operation_name
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSdkMessage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/sdk/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SendSdkMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sdk_message(
        self,
        request: intelligent_creation_20240313_models.SendSdkMessageRequest,
    ) -> intelligent_creation_20240313_models.SendSdkMessageResponse:
        """
        @summary 发送sdk消息
        
        @param request: SendSdkMessageRequest
        @return: SendSdkMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_sdk_message_with_options(request, headers, runtime)

    async def send_sdk_message_async(
        self,
        request: intelligent_creation_20240313_models.SendSdkMessageRequest,
    ) -> intelligent_creation_20240313_models.SendSdkMessageResponse:
        """
        @summary 发送sdk消息
        
        @param request: SendSdkMessageRequest
        @return: SendSdkMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_sdk_message_with_options_async(request, headers, runtime)

    def send_sdk_stream_message_with_options(
        self,
        request: intelligent_creation_20240313_models.SendSdkStreamMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SendSdkStreamMessageResponse:
        """
        @summary 发送sdk流式消息
        
        @param request: SendSdkStreamMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSdkStreamMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.header):
            body['header'] = request.header
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.operation_name):
            body['operationName'] = request.operation_name
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSdkStreamMessage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/sdk/stream/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SendSdkStreamMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sdk_stream_message_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SendSdkStreamMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SendSdkStreamMessageResponse:
        """
        @summary 发送sdk流式消息
        
        @param request: SendSdkStreamMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSdkStreamMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        if not UtilClient.is_unset(request.header):
            body['header'] = request.header
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.operation_name):
            body['operationName'] = request.operation_name
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSdkStreamMessage',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/sdk/stream/sendMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SendSdkStreamMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sdk_stream_message(
        self,
        request: intelligent_creation_20240313_models.SendSdkStreamMessageRequest,
    ) -> intelligent_creation_20240313_models.SendSdkStreamMessageResponse:
        """
        @summary 发送sdk流式消息
        
        @param request: SendSdkStreamMessageRequest
        @return: SendSdkStreamMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_sdk_stream_message_with_options(request, headers, runtime)

    async def send_sdk_stream_message_async(
        self,
        request: intelligent_creation_20240313_models.SendSdkStreamMessageRequest,
    ) -> intelligent_creation_20240313_models.SendSdkStreamMessageResponse:
        """
        @summary 发送sdk流式消息
        
        @param request: SendSdkStreamMessageRequest
        @return: SendSdkStreamMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_sdk_stream_message_with_options_async(request, headers, runtime)

    def send_text_msg_with_options(
        self,
        request: intelligent_creation_20240313_models.SendTextMsgRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SendTextMsgResponse:
        """
        @summary 发送文本消息
        
        @param request: SendTextMsgRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTextMsgResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTextMsg',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/sendTextMsg',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SendTextMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_text_msg_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SendTextMsgRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SendTextMsgResponse:
        """
        @summary 发送文本消息
        
        @param request: SendTextMsgRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTextMsgResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTextMsg',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/sendTextMsg',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SendTextMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_text_msg(
        self,
        request: intelligent_creation_20240313_models.SendTextMsgRequest,
    ) -> intelligent_creation_20240313_models.SendTextMsgResponse:
        """
        @summary 发送文本消息
        
        @param request: SendTextMsgRequest
        @return: SendTextMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_text_msg_with_options(request, headers, runtime)

    async def send_text_msg_async(
        self,
        request: intelligent_creation_20240313_models.SendTextMsgRequest,
    ) -> intelligent_creation_20240313_models.SendTextMsgResponse:
        """
        @summary 发送文本消息
        
        @param request: SendTextMsgRequest
        @return: SendTextMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_text_msg_with_options_async(request, headers, runtime)

    def start_avatar_session_with_options(
        self,
        request: intelligent_creation_20240313_models.StartAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.StartAvatarSessionResponse:
        """
        @summary 启动会话
        
        @param request: StartAvatarSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAvatarSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_token):
            body['channelToken'] = request.channel_token
        if not UtilClient.is_unset(request.custom_push_url):
            body['customPushUrl'] = request.custom_push_url
        if not UtilClient.is_unset(request.custom_user_id):
            body['customUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAvatarSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/startAvatarSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.StartAvatarSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_avatar_session_with_options_async(
        self,
        request: intelligent_creation_20240313_models.StartAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.StartAvatarSessionResponse:
        """
        @summary 启动会话
        
        @param request: StartAvatarSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAvatarSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_token):
            body['channelToken'] = request.channel_token
        if not UtilClient.is_unset(request.custom_push_url):
            body['customPushUrl'] = request.custom_push_url
        if not UtilClient.is_unset(request.custom_user_id):
            body['customUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAvatarSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/startAvatarSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.StartAvatarSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_avatar_session(
        self,
        request: intelligent_creation_20240313_models.StartAvatarSessionRequest,
    ) -> intelligent_creation_20240313_models.StartAvatarSessionResponse:
        """
        @summary 启动会话
        
        @param request: StartAvatarSessionRequest
        @return: StartAvatarSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_avatar_session_with_options(request, headers, runtime)

    async def start_avatar_session_async(
        self,
        request: intelligent_creation_20240313_models.StartAvatarSessionRequest,
    ) -> intelligent_creation_20240313_models.StartAvatarSessionResponse:
        """
        @summary 启动会话
        
        @param request: StartAvatarSessionRequest
        @return: StartAvatarSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_avatar_session_with_options_async(request, headers, runtime)

    def stop_avatar_session_with_options(
        self,
        request: intelligent_creation_20240313_models.StopAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.StopAvatarSessionResponse:
        """
        @summary 停止会话
        
        @param request: StopAvatarSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAvatarSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopAvatarSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/stopAvatarSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.StopAvatarSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_avatar_session_with_options_async(
        self,
        request: intelligent_creation_20240313_models.StopAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.StopAvatarSessionResponse:
        """
        @summary 停止会话
        
        @param request: StopAvatarSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAvatarSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopAvatarSession',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/avatar/project/stopAvatarSession',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.StopAvatarSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_avatar_session(
        self,
        request: intelligent_creation_20240313_models.StopAvatarSessionRequest,
    ) -> intelligent_creation_20240313_models.StopAvatarSessionResponse:
        """
        @summary 停止会话
        
        @param request: StopAvatarSessionRequest
        @return: StopAvatarSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_avatar_session_with_options(request, headers, runtime)

    async def stop_avatar_session_async(
        self,
        request: intelligent_creation_20240313_models.StopAvatarSessionRequest,
    ) -> intelligent_creation_20240313_models.StopAvatarSessionResponse:
        """
        @summary 停止会话
        
        @param request: StopAvatarSessionRequest
        @return: StopAvatarSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_avatar_session_with_options_async(request, headers, runtime)

    def stop_project_task_with_options(
        self,
        request: intelligent_creation_20240313_models.StopProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.StopProjectTaskResponse:
        """
        @summary 视频合成任务停止
        
        @param request: StopProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.StopProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_project_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.StopProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.StopProjectTaskResponse:
        """
        @summary 视频合成任务停止
        
        @param request: StopProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.StopProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_project_task(
        self,
        request: intelligent_creation_20240313_models.StopProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.StopProjectTaskResponse:
        """
        @summary 视频合成任务停止
        
        @param request: StopProjectTaskRequest
        @return: StopProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_project_task_with_options(request, headers, runtime)

    async def stop_project_task_async(
        self,
        request: intelligent_creation_20240313_models.StopProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.StopProjectTaskResponse:
        """
        @summary 视频合成任务停止
        
        @param request: StopProjectTaskRequest
        @return: StopProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_project_task_with_options_async(request, headers, runtime)

    def submit_image_to_video_task_with_options(
        self,
        request: intelligent_creation_20240313_models.SubmitImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SubmitImageToVideoTaskResponse:
        """
        @summary 提交图片转视频任务
        
        @param request: SubmitImageToVideoTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitImageToVideoTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.pos_prompt):
            body['posPrompt'] = request.pos_prompt
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImageToVideoTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SubmitImageToVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_to_video_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SubmitImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SubmitImageToVideoTaskResponse:
        """
        @summary 提交图片转视频任务
        
        @param request: SubmitImageToVideoTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitImageToVideoTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.pos_prompt):
            body['posPrompt'] = request.pos_prompt
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitImageToVideoTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SubmitImageToVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_to_video_task(
        self,
        request: intelligent_creation_20240313_models.SubmitImageToVideoTaskRequest,
    ) -> intelligent_creation_20240313_models.SubmitImageToVideoTaskResponse:
        """
        @summary 提交图片转视频任务
        
        @param request: SubmitImageToVideoTaskRequest
        @return: SubmitImageToVideoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_image_to_video_task_with_options(request, headers, runtime)

    async def submit_image_to_video_task_async(
        self,
        request: intelligent_creation_20240313_models.SubmitImageToVideoTaskRequest,
    ) -> intelligent_creation_20240313_models.SubmitImageToVideoTaskResponse:
        """
        @summary 提交图片转视频任务
        
        @param request: SubmitImageToVideoTaskRequest
        @return: SubmitImageToVideoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_image_to_video_task_with_options_async(request, headers, runtime)

    def submit_project_task_with_options(
        self,
        request: intelligent_creation_20240313_models.SubmitProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SubmitProjectTaskResponse:
        """
        @summary 提交离线数字人合成任务
        
        @param request: SubmitProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitProjectTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.frames):
            body['frames'] = request.frames
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.subtitle_tag):
            body['subtitleTag'] = request.subtitle_tag
        if not UtilClient.is_unset(request.transparent_background):
            body['transparentBackground'] = request.transparent_background
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/submitProjectTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SubmitProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_project_task_with_options_async(
        self,
        request: intelligent_creation_20240313_models.SubmitProjectTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.SubmitProjectTaskResponse:
        """
        @summary 提交离线数字人合成任务
        
        @param request: SubmitProjectTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitProjectTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.frames):
            body['frames'] = request.frames
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.subtitle_tag):
            body['subtitleTag'] = request.subtitle_tag
        if not UtilClient.is_unset(request.transparent_background):
            body['transparentBackground'] = request.transparent_background
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitProjectTask',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/digitalHuman/project/submitProjectTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.SubmitProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_project_task(
        self,
        request: intelligent_creation_20240313_models.SubmitProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.SubmitProjectTaskResponse:
        """
        @summary 提交离线数字人合成任务
        
        @param request: SubmitProjectTaskRequest
        @return: SubmitProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_project_task_with_options(request, headers, runtime)

    async def submit_project_task_async(
        self,
        request: intelligent_creation_20240313_models.SubmitProjectTaskRequest,
    ) -> intelligent_creation_20240313_models.SubmitProjectTaskResponse:
        """
        @summary 提交离线数字人合成任务
        
        @param request: SubmitProjectTaskRequest
        @return: SubmitProjectTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_project_task_with_options_async(request, headers, runtime)

    def transfer_portrait_style_with_options(
        self,
        request: intelligent_creation_20240313_models.TransferPortraitStyleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.TransferPortraitStyleResponse:
        """
        @summary 人像风格变化
        
        @param request: TransferPortraitStyleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferPortraitStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['height'] = request.height
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.numbers):
            body['numbers'] = request.numbers
        if not UtilClient.is_unset(request.redraw_amplitude):
            body['redrawAmplitude'] = request.redraw_amplitude
        if not UtilClient.is_unset(request.style):
            body['style'] = request.style
        if not UtilClient.is_unset(request.width):
            body['width'] = request.width
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferPortraitStyle',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/portrait/transferPortraitStyle',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.TransferPortraitStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_portrait_style_with_options_async(
        self,
        request: intelligent_creation_20240313_models.TransferPortraitStyleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> intelligent_creation_20240313_models.TransferPortraitStyleResponse:
        """
        @summary 人像风格变化
        
        @param request: TransferPortraitStyleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferPortraitStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['height'] = request.height
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.numbers):
            body['numbers'] = request.numbers
        if not UtilClient.is_unset(request.redraw_amplitude):
            body['redrawAmplitude'] = request.redraw_amplitude
        if not UtilClient.is_unset(request.style):
            body['style'] = request.style
        if not UtilClient.is_unset(request.width):
            body['width'] = request.width
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferPortraitStyle',
            version='2024-03-13',
            protocol='HTTPS',
            pathname=f'/yic/yic-console/openService/v1/images/portrait/transferPortraitStyle',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240313_models.TransferPortraitStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_portrait_style(
        self,
        request: intelligent_creation_20240313_models.TransferPortraitStyleRequest,
    ) -> intelligent_creation_20240313_models.TransferPortraitStyleResponse:
        """
        @summary 人像风格变化
        
        @param request: TransferPortraitStyleRequest
        @return: TransferPortraitStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transfer_portrait_style_with_options(request, headers, runtime)

    async def transfer_portrait_style_async(
        self,
        request: intelligent_creation_20240313_models.TransferPortraitStyleRequest,
    ) -> intelligent_creation_20240313_models.TransferPortraitStyleResponse:
        """
        @summary 人像风格变化
        
        @param request: TransferPortraitStyleRequest
        @return: TransferPortraitStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.transfer_portrait_style_with_options_async(request, headers, runtime)
